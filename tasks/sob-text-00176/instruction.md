{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAbsarokee, Montana: Absarokee ( ) is a census-designated place (CDP) in Stillwater County, Montana, United States, approximately 14 mi south of Columbus on Highway 78.  It is named after the Crow Indians who formerly inhabited the land.  The population was 1,234 at the 2000 census.  The Stillwater Mine, operated by the Stillwater Mining Company, is located near Absarokee.\n\nPeloncillo Mountains (Hidalgo County): The Peloncillo Mountains of Hidalgo County, (Spanish language \"pelo\", hair, \"pelón\", hairless, bald; \"peloncillo\", Little Baldy), is a major 35 mi long mountain range southwest of New Mexico's Hidalgo County, and also part of the New Mexico Bootheel region.  The range continues to the northwest into Arizona as the Peloncillo Mountains of Cochise County, Arizona.  The extreme southwest corner of the range also lies in Arizona.  It is a linear range bordering the linear San Bernardino Valley of southeast Cochise County, Arizona.\n\nGranite Range (Washoe County): The Granite Range is a mountain range in Washoe County, Nevada west of the town of Gerlach and the lower Black Rock Desert playa.\n\nHighland Mountains: The Highland Mountains, highest point Table Mountain, el.  10223 ft , are a small mountain range southwest of Whitehall, Montana in Silver Bow and Madison County, Montana.\n\nGravelly Range: The Gravelly Range, highest peak Black Butte, el.  10542 ft , is a mountain range southwest of Cameron, Montana in Madison County, Montana.\n\nGranite Range (Elko County): The Granite Range is a mountain range in Elko County, Nevada.\n\nKomatke, Arizona: Komatke (O'odham: Komaḍk) is a census-designated place in Maricopa County, Arizona, United States.  The area currently comprising the CDP had a population of 821 at the 2010 census.  It is located within the Gila River Indian Community.  Its name refers to the Sierra Estrella mountain range.  Komatke is located at the base of the mountain range.\n\nGranite Range (Montana): The Granite Range, el.  11092 ft , is a mountain range southwest of Absarokee, Montana in Stillwater County, Montana.\n\nLewis and Clark Range: The Lewis and Clark Range, el.  7109 ft , is a small mountain range southwest of Seeley Lake, Montana in Powell County, Montana.\n\nYuna River: The Yuna River (Spanish: Río Yuna) is the second longest river in the Dominican Republic at 185.17 km in length.  It forms within the Cordillera Central mountain range southwest of the city of Bonao and passes through the fertile Cibao Valley.  The river from there turns north-northeast passing the city of Bonao along the way.  Southwest of Cotuí, the river reaches Hatillo Dam (Spanish: \"Presa de Hatillo\") before turning northeast then east as it reaches its mouth at the Samaná Bay in the northeast part of the Dominican Republic.  Like many rivers in the Dominican Republic, the name is derived from the Taíno language.\n\nQuestion:  The Granite Range is a mountain range southwest of a census-designated place with a population of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"mountain_range_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the mountain range.\"\n    },\n    \"associated_cdp\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the census-designated place (CDP).\"\n        },\n        \"population\": {\n          \"type\": \"integer\",\n          \"description\": \"The population of the CDP.\"\n        },\n        \"census_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the population was recorded.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the CDP is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the CDP is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"population\",\n        \"census_year\",\n        \"county\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mountain_range_location_relative_to_cdp\": {\n      \"type\": \"string\",\n      \"description\": \"The geographical relationship of the mountain range to the CDP.\"\n    }\n  },\n  \"required\": [\n    \"mountain_range_name\",\n    \"associated_cdp\",\n    \"mountain_range_location_relative_to_cdp\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "mountain_range_name": {
        "type": "string",
        "description": "The name of the mountain range."
      },
      "associated_cdp": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the census-designated place (CDP)."
          },
          "population": {
            "type": "integer",
            "description": "The population of the CDP."
          },
          "census_year": {
            "type": "integer",
            "description": "The year the population was recorded."
          },
          "county": {
            "type": "string",
            "description": "The county where the CDP is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the CDP is located."
          }
        },
        "required": [
          "name",
          "population",
          "census_year",
          "county",
          "state"
        ],
        "additionalProperties": false
      },
      "mountain_range_location_relative_to_cdp": {
        "type": "string",
        "description": "The geographical relationship of the mountain range to the CDP."
      }
    },
    "required": [
      "mountain_range_name",
      "associated_cdp",
      "mountain_range_location_relative_to_cdp"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
