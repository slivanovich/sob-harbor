{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFloyd, New York: Floyd is a town in Oneida County, New York, United States.  The population was 3,819 at the 2010 census.  The town is named after William Floyd, a signer of the Declaration of Independence.\n\nCounty Route 46 (Suffolk County, New York): County Route 46 (CR 46) is a major county road in eastern Suffolk County, New York, in the United States.  It runs south-to-north from CR 75 in Smith Point County Park (part of the Fire Island National Seashore) to New York State Route 25A (NY 25A) near the border of Shoreham and Wading River.  The road is known as the William Floyd Parkway along its entire length, and is named after William Floyd, a Long Island native and a signer of the United States Declaration of Independence.  Despite its \"parkway\" designation within the State of New York, the road is open to commercial vehicles.\n\nWilliam Floyd School District: The William Floyd School District is located in the southern area of the Town of Brookhaven on Long Island in New York.  The district serves the contiguous communities of Shirley, Mastic, Mastic Beach and Moriches.  The William Floyd School District is one of the larger school districts on Long Island and is named after William Floyd, one of only 56 men to sign the Declaration of Independence.  The district is located on the south shore of Long Island, approximately 60 miles east of New York City, with an enrollment of 8,653 students as of 2016.  William Floyd students attend five elementary schools, two middle schools, and a senior high school.\n\nSouthaven County Park: Southaven County Park is located in Brookhaven and South Haven, New York in central Long Island.  It is located between Sunrise Highway (Route 27) just west of William Floyd Parkway, off of Victory Avenue (Suffolk CR 56/North Sunrise Service Road), and crossed by the Carmans River.\n\nWestern Town Hall: Western Town Hall, also known as Liberty Hall, is a historic town hall building located at Westernville in Oneida County, New York.  It was built in 1911 and is a two story, gable roofed timber frame structure.  It was constructed from dismantled components of the ca. 1850 Empire Hotel in Delta.  It was rebuilt as \"Liberty Hall,\" a social gathering hall, and named in honor of General William Floyd.  The second floor has an auditorium.  It has been used as the town hall since 1962.\n\nWilliam Floyd House: William Floyd House, also known as Nicholl Floyd House and Old Mastic House, was a home of William Floyd, a signer of the United States Declaration of Independence, in Mastic Beach, New York.  It was his home from 1734 until 1803.  This home is distinct from Gen. William Floyd House, his later home in Westernville, New York, that is also on the National Register and which was designated a National Historic Landmark.\n\nManor St. George: Manor St. George or St. George's Manor was a large tract of land purchased by William \"Tangier\" Smith in the 17th century on Long Island, in central Suffolk County, New York.  Parts of the original parcel, which was approximately 64000 acre of land, are preserved in bits and pieces: 127 acres (0.51 km²) and the main house and buildings are called the Manor of St. George and located in Shirley; 35 acres (0.14 km²) and another house are called the Longwood Estate and located in Ridge; and 35 acres (0.14 km²) became part of the William Floyd Estate.\n\nJohn G. Floyd: John Gelston Floyd (February 5, 1806 – October 5, 1881) was a U.S. Representative from New York, grandson of William Floyd.\n\nGen. William Floyd House: Gen. William Floyd House in Westernville, New York is a National Historic Landmark.  It was the home of William Floyd, 1734–1821, a signer of the Declaration of Independence.  This is distinct from William Floyd House, a prior home of his in Mastic Beach, New York that is also on the National Register.\n\nMastic Beach, New York: Mastic Beach is a village in the southeast part of the town of Brookhaven in Suffolk County, New York, United States.  The population was 12,930 at the 2010 census, at which time it was an unincorporated census-designated place.  The village is located in the general vicinity of the hamlet of Mastic Beach.\n\nQuestion: The William Floyd House is located in what county in New York? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity being located.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of entity, e.g., 'historic house', 'residence'.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the entity is located.\"\n        },\n        \"city_or_village\": {\n          \"type\": \"string\",\n          \"description\": \"The city or village where the entity is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the entity is located.\"\n        }\n      },\n      \"required\": [\n        \"county\",\n        \"city_or_village\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"entity_type\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the entity being located."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of entity, e.g., 'historic house', 'residence'."
      },
      "location": {
        "type": "object",
        "properties": {
          "county": {
            "type": "string",
            "description": "The county where the entity is located."
          },
          "city_or_village": {
            "type": "string",
            "description": "The city or village where the entity is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the entity is located."
          }
        },
        "required": [
          "county",
          "city_or_village",
          "state"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_name",
      "entity_type",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
