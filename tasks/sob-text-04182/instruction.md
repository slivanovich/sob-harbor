{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nListed buildings in Parbold: Parbold is a civil parish in the West Lancashire district of Lancashire, England.  It contains 15 buildings that are recorded in the National Heritage List for England as designated listed buildings. Of these, two are at Grade II*, the middle grade, and the others are at Grade II, the lowest grade.  The parish contains the large village of Parbold and the surrounding countryside.  The Leeds and Liverpool Canal passes through the parish and the listed buildings associated with this are four bridges, two milestones, and a lock.  The other listed buildings are houses, a farm building, a former windmill, a railway signal box, and two churches.\n\nParbold: Parbold is a large commuter village and civil parish in Lancashire, England.\n\nCraw (surname): Craw is an English habitational name that arrived in Britain with Anglo-Saxon tribes.  Residents of the village Cronkshaw in the county of Lancashire adopted Craw as their surname.\n\nFairhurst: Fairhurst is an English habitational surname, and may refer to a now vanished hamlet near Parbold in Lancashire.  The name is derived from Old English fæger (meaning beautiful) with hyrst (wooded hill).\n\nWrightington: Wrightington is a civil parish in West Lancashire, England, with an area of 3,915½ acres.  The surface is hilly, rising to over 400 ft. at Harrock on the border of Parbold, and then falling to the north, northeast and southeast.  On the southern border, the boundary at Appley Bridge touches the River Douglas.  Wrightington Hall is to the north of this point.  Tunley and Broadhurst lie to the north of the park, and Fairhurst, to the west of Harrock, reaches down to the Douglas.  At the 2001 census, Wrightington had a population of 4,055, falling to 2,886 at the 2011 Census.\n\nMyerscough: Myerscough ( or or ) is an English surname, which is most common in Lancashire.  The name originates from the hamlet of Myerscough, in the parish of Myerscough and Bilsborrow near Preston, which has been an important land holding by the Duchy of Lancaster since 1267.  Although the name originates from a hamlet near Preston, the town with the highest proportions of Myerscough's is Fleetwood in Lancashire.  The name is virtually unheard of in the midlands and the south of England.  People with the name are used to it being pronounced or spelt incorrectly, mainly due to people being unfamiliar with the name and pronouncing it how they think it is pronounced or spelt.  Historically the name had the more phonetic spelling 'Myerscoe'.\n\nAshford (surname): Ashford is an English habitational surname from any of several places called Ashford.  Those in Essex, Devon, Derbyshire, and Shropshire are named from Old English \"æsc\" ‘ash’ + \"ford\" ‘ford’.\n\nRutherford (surname): The surname Rutherford, also Rutherfurd, is a Scottish and Northern English habitational surname deriving from a place in the Scottish borders region near Roxburgh.  It may refer to:\n\nTrnka: Trnka is a Czech habitational surname, meaning a person who lived by a blackthorn bush, or \"trnka\" in Czech.  The name may refer to:\n\nCollingwood: Collingwood is an English placename (meaning \"wood of disputed ownership\") and the source of an English habitational surname.  It may refer to:\n\nQuestion: Fairhurst is an English habitational surname, and may refer to a now vanished hamlet near Parbold, a large commuter village and civil parish in Lancashire, in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"surname_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the surname being discussed.\"\n    },\n    \"surname_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of surname, e.g., habitational.\"\n    },\n    \"associated_place_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the place associated with the surname's origin.\",\n      \"properties\": {\n        \"place_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the associated place.\"\n        },\n        \"place_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the associated place, e.g., hamlet, village, civil parish.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the associated place is located.\"\n        }\n      },\n      \"required\": [\n        \"place_name\",\n        \"place_type\",\n        \"county\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the surname or its associated place originates.\"\n    }\n  },\n  \"required\": [\n    \"surname_name\",\n    \"surname_type\",\n    \"associated_place_details\",\n    \"country_of_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "surname_name": {
        "type": "string",
        "description": "The name of the surname being discussed."
      },
      "surname_type": {
        "type": "string",
        "description": "The type of surname, e.g., habitational."
      },
      "associated_place_details": {
        "type": "object",
        "description": "Details about the place associated with the surname's origin.",
        "properties": {
          "place_name": {
            "type": "string",
            "description": "The name of the associated place."
          },
          "place_type": {
            "type": "string",
            "description": "The type of the associated place, e.g., hamlet, village, civil parish."
          },
          "county": {
            "type": "string",
            "description": "The county where the associated place is located."
          }
        },
        "required": [
          "place_name",
          "place_type",
          "county"
        ],
        "additionalProperties": false
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the surname or its associated place originates."
      }
    },
    "required": [
      "surname_name",
      "surname_type",
      "associated_place_details",
      "country_of_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
