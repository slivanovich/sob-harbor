{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouth Dakota Department of Transportation: The South Dakota Department of Transportation is a state government organization in charge of maintaining public roadways of the U.S. state of South Dakota.  South Dakota has 82,447 miles of highways, roads and streets; 5,905 bridges.  The SD DOT is responsible for 7,830 miles of the roadway system.\n\nNew Mexico Department of Transportation: The New Mexico Department of Transportation (NMDOT; Spanish: Departamento de Transporte de Nuevo México ) is a state government organization which oversees transportation in the U.S. state of New Mexico.  The agency has four main focuses—transit, rail, aviation and highways.\n\nMissouri Department of Transportation: The Missouri Department of Transportation (MoDOT — pronounced \"MO-dot\") is a state government organization in charge of maintaining public roadways of the U.S. state of Missouri.\n\nOhio Department of Transportation: The Ohio Department of Transportation (ODOT, pronounced \"oh-dot\") is the administrative department of the Ohio state government responsible for developing and maintaining all state and federal roadways in the state of Ohio with exception of the Ohio Turnpike.  In addition to highways, the department also helps develop public transportation and public aviation programs.  ODOT is headquartered in Columbus, Ohio.  The Director of Transportation is part of the Governor's Cabinet.\n\nKansas Department of Transportation: The Kansas Department of Transportation (KDOT) is a state government organization in charge of maintaining public roadways of the U.S. state of Kansas.\n\nDeb Miller: Deborah Miller is a former Secretary of Transportation at the Kansas Department of Transportation (KDOT) who served from 2003 to 2012.  She was Kansas' first female and longest-serving Secretary of Transportation.  She joined Cambridge Systematics as a senior associate in January 2012.\n\nGeorgia Department of Transportation: The Georgia Department of Transportation (GDOT) is the organization in charge of developing and maintaining all state and federal roadways in the U.S. state of Georgia.  In addition to highways, the department also has a limited role in developing public transportation and general aviation programs.  GDOT is headquartered in downtown Atlanta and is part of the executive branch of state government.\n\nIllinois Department of Transportation: The Illinois Department of Transportation (IDOT) is a state agency in charge of state-maintained public roadways of the U.S. state of Illinois.  In addition, IDOT provides funding for rail, public transit and airport projects and administers fuel tax and federal funding to local jurisdictions in the state.  The Secretary of Transportation reports to the Governor of Illinois.  IDOT is headquartered in unincorporated Sangamon County, located near the state capital, Springfield.  In addition, the IDOT Division of Highways has offices in nine locations throughout the state.\n\nHawaii Department of Transportation: The Hawaii Department of Transportation (HDOT) is a state government organization which oversees transportation in the U.S. state of Hawaii.  The agency is divided into three divisions dealing with aviation, maritime, and roads.\n\nPublic Works Department (Western Australia): The Public Works Department (PWD) was the State Government Agency of Western Australia, which was charged with providing and maintaining public infrastructure such as dams, water supplies, schools, hospitals, harbours and other public buildings.  The Department is no longer operational, having its responsibilities reassigned to other State Government Departments and corporate entities since 1985.\n\nQuestion: Who is the former Secretary of Transportation at the state government organization in charge of maintaining public roadways of the U.S. state of Kansas?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the individual.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The position held by the individual.\"\n    },\n    \"organization\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the government organization.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The U.S. state the organization serves.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"service_period\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the individual started their service.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the individual ended their service.\"\n        }\n      },\n      \"required\": [\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"distinctions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Notable achievements or facts about the individual's service.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role\",\n    \"organization\",\n    \"service_period\",\n    \"distinctions\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the individual."
      },
      "role": {
        "type": "string",
        "description": "The position held by the individual."
      },
      "organization": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the government organization."
          },
          "state": {
            "type": "string",
            "description": "The U.S. state the organization serves."
          }
        },
        "required": [
          "name",
          "state"
        ],
        "additionalProperties": false
      },
      "service_period": {
        "type": "object",
        "properties": {
          "start_year": {
            "type": "integer",
            "description": "The year the individual started their service."
          },
          "end_year": {
            "type": "integer",
            "description": "The year the individual ended their service."
          }
        },
        "required": [
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "distinctions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Notable achievements or facts about the individual's service."
      }
    },
    "required": [
      "person_name",
      "role",
      "organization",
      "service_period",
      "distinctions"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
