{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouthwark Cathedral: Southwark Cathedral ( ) or The Cathedral and Collegiate Church of St Saviour and St Mary Overie, Southwark, London, lies on the south bank of the River Thames close to London Bridge.  It is the mother church of the Anglican Diocese of Southwark.  It has been a place of Christian worship for more than 1,000 years, but a cathedral only since the creation of the diocese of Southwark in 1905.\n\nWinchester Palace: Winchester Palace was a 12th-century palace which served as the London townhouse of the Bishops of Winchester.  It was located on the south bank of the River Thames in what is now the London Borough of Southwark, near the medieval priory which later became Southwark Cathedral.  Remains of the demolished palace survive on the site today.\n\nAnchor Bankside: The Anchor Bankside is a pub in the London Borough of Southwark.  It is in the Bankside locality on the south bank of the Thames close to Southwark Cathedral and London Bridge station.  A tavern establishment (under various names) has been at the pub's location for over 800 years.  Behind the pub are buildings that were operated by the Anchor Brewery.\n\nSouthwark St Olave: Southwark St Olave was an ancient civil and ecclesiastical parish on the south bank of the River Thames, covering the area around where Shard London Bridge now stands in the modern London Borough of Southwark.  The boundaries varied over time but in general the parish stretched east from London Bridge past Tower Bridge to St Saviour's Dock.  Southwark St Olave and St Thomas replaced the civil parish in 1896.  It was abolished in 1904 and absorbed by Bermondsey parish.\n\nMartin Kitchen (priest): He was on 18 May 1947; educated at Sir Walter St John's Grammar School For Boys and the Polytechnic of North London, before training for the priesthood at King's College London and the Southwark Ordination Course and being ordained in 1980.  He was a Lecturer at the Church Army Training College, and Curate at St James, Kidbrooke from 1979 to 1983 when he became Chaplain of Manchester Polytechnic and Team Vicar of Whitworth, Manchester.  He was Advisor for Training for the Diocese of Southwark and a Residentiary Canon at Southwark Cathedral from 1988 to 1997; and then a Residentiary Canon at Durham Cathedral from then until 2004 (Vice Dean from 1999 to 2004).\n\nBrentwood Cathedral: The Cathedral of St Mary and St Helen is the Roman Catholic cathedral in the English town of Brentwood, Essex.  It is the seat of the Diocese of Brentwood.\n\nLondon Bridge City Pier: London Bridge City Pier (also known as London Bridge Pier and City Pier) is situated on the south bank of the River Thames in London, UK, close to London Bridge.  It serves as the main pier for the City of London and City Hall, headquarters of the London Assembly.\n\nSt Thomas' Church, Southwark: St Thomas Church, Southwark, London, England.  The first church building was part of the original St. Thomas' Hospital which was located to the area around the present St Thomas Street, from the infirmary at St Mary Overie priory (see Southwark Cathedral) in 1212.  The hospital was therefore also an Augustinian house.  The hospital/conventual precinct became a parish no later than 1496.  It was named after Thomas Becket whose cult pilgrimage to Canterbury began at London Bridge.  The church was renamed St Thomas the Apostle following the abolition of the Becket cult in 1538 during the Reformation.\n\nJane Steen: Jane Elizabeth Steen (born 1964) is a British Church of England priest.  Since 2013, she has been the Archdeacon of Southwark.  This makes her one of the most senior priests in the Diocese of Southwark.  Previously, from 2005 to 2013, she served as Canon Chancellor of Southwark Cathedral, and also as Director of Ministerial Education and Canon Theologian for the Diocese of Southwark.\n\nDean of Southwark: The Dean of Southwark is the head (\"primus inter pares\" – first among equals) and chair of the chapter of canons, the ruling body of Southwark Cathedral.  The dean and chapter are based at the \"Cathedral and Collegiate Church of Saint Saviour and Saint Mary Overie\" in Southwark.  Before 2000 the post was designated as a provost, which was then the equivalent of a dean at most English cathedrals.  The cathedral is the mother church of the Anglican Diocese of Southwark and seat of the Bishop of Southwark.  The current dean is Andrew Nunn.\n\nQuestion: What Catherdral lies on the south bank close to the London Bridge, Brentwood Cathedral or Southwark Cathedral?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"identified_cathedral\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the cathedral that matches the location criteria.\"\n        },\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the cathedral's location from the context.\"\n        },\n        \"is_on_south_bank\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the cathedral is explicitly stated to be on the south bank of the River Thames.\"\n        },\n        \"is_near_london_bridge\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the cathedral is explicitly stated to be close to London Bridge.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location_description\",\n        \"is_on_south_bank\",\n        \"is_near_london_bridge\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"comparison_cathedral\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the other cathedral mentioned in the question for comparison.\"\n        },\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of this cathedral's location from the context.\"\n        },\n        \"is_on_south_bank\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if this cathedral is explicitly stated to be on the south bank of the River Thames, otherwise false.\"\n        },\n        \"is_near_london_bridge\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if this cathedral is explicitly stated to be close to London Bridge, otherwise false.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location_description\",\n        \"is_on_south_bank\",\n        \"is_near_london_bridge\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer_cathedral_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the cathedral that correctly answers the question.\"\n    }\n  },\n  \"required\": [\n    \"identified_cathedral\",\n    \"comparison_cathedral\",\n    \"final_answer_cathedral_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "identified_cathedral": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the cathedral that matches the location criteria."
          },
          "location_description": {
            "type": "string",
            "description": "A description of the cathedral's location from the context."
          },
          "is_on_south_bank": {
            "type": "boolean",
            "description": "True if the cathedral is explicitly stated to be on the south bank of the River Thames."
          },
          "is_near_london_bridge": {
            "type": "boolean",
            "description": "True if the cathedral is explicitly stated to be close to London Bridge."
          }
        },
        "required": [
          "name",
          "location_description",
          "is_on_south_bank",
          "is_near_london_bridge"
        ],
        "additionalProperties": false
      },
      "comparison_cathedral": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the other cathedral mentioned in the question for comparison."
          },
          "location_description": {
            "type": "string",
            "description": "A description of this cathedral's location from the context."
          },
          "is_on_south_bank": {
            "type": "boolean",
            "description": "True if this cathedral is explicitly stated to be on the south bank of the River Thames, otherwise false."
          },
          "is_near_london_bridge": {
            "type": "boolean",
            "description": "True if this cathedral is explicitly stated to be close to London Bridge, otherwise false."
          }
        },
        "required": [
          "name",
          "location_description",
          "is_on_south_bank",
          "is_near_london_bridge"
        ],
        "additionalProperties": false
      },
      "final_answer_cathedral_name": {
        "type": "string",
        "description": "The name of the cathedral that correctly answers the question."
      }
    },
    "required": [
      "identified_cathedral",
      "comparison_cathedral",
      "final_answer_cathedral_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
