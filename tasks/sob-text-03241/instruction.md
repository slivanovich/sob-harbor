{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDundarg Castle: Dundarg Castle is a ruined castle about 2 km north-northeast of New Aberdour, Aberdeenshire, Scotland, built within the ramparts of an earlier iron age promontory fort.  It was described by W. Douglas Simpson as one of the nine castles of the Knuckle, referring to the rocky headland of north-east Aberdeenshire.\n\nBužim Fort: Bužim Castle (Bosnian: \"Tvrđava Bužim\", \"Stari grad Bužim\" , \"Old City of Bužim\") is a castle in the Bužim municipality in northwestern Bosnia and Herzegovina.  The castle was built during the 12th century, and is located at 325 m above sea level.  It was the second-biggest medieval castle in Cazinska krajina, after Bihać.  The castle is an example of renaissance architecture, and served as both a military hill fort and a residence for the nobility.  Bužim Castle and a nearby old mosque are protected as national monuments in Bosnia and Herzegovina.\n\nFedderate Castle: Fedderate Castle is a ruined castle near New Deer in Aberdeenshire, Scotland.  A drawbridge and causeway provided access to the castle.  Lord William Oliphant with Jacobite forces, took control of Fedderate Castle and held out against the forces of Hugh Mackay for more than 3 weeks, surrendering in October 1690.\n\nKildrummy Castle: Kildrummy Castle is a ruined castle near Kildrummy, in Aberdeenshire, Scotland.  Though ruined, it is one of the most extensive castles dating from the 13th century to survive in eastern Scotland, and was the seat of the Earls of Mar.  It is owned today by Historic Scotland and is open to the public as a scheduled ancient monument.\n\nOld Slains Castle: Old Slains Castle (otherwise known as Old Castle Slains) is a ruined castle near Collieston in Aberdeenshire, Scotland.\n\nNew Slains Castle: Slains Castle, also known as New Slains Castle to distinguish it from nearby Old Slains Castle, is a ruined castle in Aberdeenshire, Scotland.  It overlooks the North Sea from its cliff-top site 1 km east of Cruden Bay.  The core of the castle is a 16th-century tower house, built by the 9th Earl of Erroll.  Significant reconstruction of the castle has been carried out a number of times, lastly in 1837 when it was rebuilt as a Scots Baronial mansion.  At one time it had three extensive gardens, but is now a roofless ruin.  Plans to restore the castle have been on hold since 2009.\n\nBognie Castle: Bognie Castle (also called Conzie Castle) is a ruined castle near Huntly, in the Aberdeenshire region of Scotland.  It was built in the 17th century and is now ruined.  It once rose 4 storeys high.\n\nSlains Castle: Slains Castle may refer to one of two ruined castles in Aberdeenshire, Scotland:\n\nPitsligo Castle: Pitsligo Castle is a ruined castle half a mile east of Rosehearty, Aberdeenshire, Scotland.  It was described by W. Douglas Simpson as one of the nine castles of the Knuckle, referring to the rocky headland of north-east Aberdeenshire.\n\nNational Museum of Wildlife Art: The National Museum of Wildlife Art (NMWA) is a museum located in Jackson Hole, Wyoming, United States that preserves and exhibits wildlife art.  The 51,000 square foot building with its Idaho quartzite façade was inspired by the ruins of Slains Castle in Aberdeenshire, Scotland and echoes the hillside behind the facility.  Located on a bluff called East Gros Ventre Butte in the midst of a real wildlife habitat, the institution overlooks the National Elk Refuge and is situated 2.5 miles north of the town of Jackson.  The core of the collections reflects traditional and contemporary realism.  The Museum's centerpiece is a collection of works by Carl Rungius (1869-1959) and Bob Kuhn (1920-2007).  In addition to 14 galleries, the museum has a Sculpture Trail, Museum Shop, Restaurant, Children’s Discovery Gallery, and Library.  More than 80,000 people visit every year, and over 10,000 children visit the Museum each year, often as part of their school curricula.\n\nQuestion: Which ruined castle, located in Aberdeenshire, Scotland, is located nearby Old Slains Castle?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"castle_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the castle.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"region\": {\n          \"type\": \"string\",\n          \"description\": \"The region where the castle is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the castle is located.\"\n        }\n      },\n      \"required\": [\n        \"region\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"condition\": {\n      \"type\": \"string\",\n      \"description\": \"The current condition of the castle, e.g., 'ruined'.\"\n    },\n    \"nearby_landmark\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the landmark the castle is located near.\"\n    }\n  },\n  \"required\": [\n    \"castle_name\",\n    \"location\",\n    \"condition\",\n    \"nearby_landmark\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "castle_name": {
        "type": "string",
        "description": "The name of the castle."
      },
      "location": {
        "type": "object",
        "properties": {
          "region": {
            "type": "string",
            "description": "The region where the castle is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the castle is located."
          }
        },
        "required": [
          "region",
          "country"
        ],
        "additionalProperties": false
      },
      "condition": {
        "type": "string",
        "description": "The current condition of the castle, e.g., 'ruined'."
      },
      "nearby_landmark": {
        "type": "string",
        "description": "The name of the landmark the castle is located near."
      }
    },
    "required": [
      "castle_name",
      "location",
      "condition",
      "nearby_landmark"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
