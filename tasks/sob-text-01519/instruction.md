{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJiaozhoubei Railway Station: The Jiaozhoubei Railway Station () is a railway station found in the boundary between Jiaodong Subdistrict and Jiaolai Town of Jiaozhou City, Qingdao, China.  It currently lies on the Qingdao–Jinan High-Speed Railway.\n\nYinghai Subdistrict, Jiaozhou: Yinghai Subdistrict () is a subdistrict of Jiaozhou City, Shandong, People's Republic of China, located south of G22 Qingdao–Lanzhou Expressway southeast of downtown.  , it has 47 villages under its administration.\n\nYingkou: Yingkou () is a prefecture-level city of Liaoning province, People's Republic of China.  It is a port city of the Bohai Sea, and is the location of the mouth of the Liao River.\n\nJiaozhou City: Jiaozhou (), formerly Jiaoxian or Jiao County, is a county-level city of Qingdao sub-provincial city, Shandong Province, China.  It gained its current county-level city designation in 1987.  It has an area of 1,313 km and a population at the 2000 Census of 783,478.\n\nQuestion: Jiaozhou City and Yingkou, are in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"country_of_location\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the mentioned cities are located.\"\n    },\n    \"entities_located\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each entity mentioned in the question and its location.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"entity_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the city or entity.\"\n          },\n          \"entity_type\": {\n            \"type\": \"string\",\n            \"description\": \"The administrative type of the entity (e.g., county-level city, prefecture-level city).\"\n          },\n          \"province_or_region\": {\n            \"type\": \"string\",\n            \"description\": \"The province or region within the country where the entity is located.\"\n          }\n        },\n        \"required\": [\n          \"entity_name\",\n          \"entity_type\",\n          \"province_or_region\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"total_entities_found\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of entities whose location was identified.\"\n    }\n  },\n  \"required\": [\n    \"country_of_location\",\n    \"entities_located\",\n    \"total_entities_found\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "country_of_location": {
        "type": "string",
        "description": "The country where the mentioned cities are located."
      },
      "entities_located": {
        "type": "array",
        "description": "Details about each entity mentioned in the question and its location.",
        "items": {
          "type": "object",
          "properties": {
            "entity_name": {
              "type": "string",
              "description": "The name of the city or entity."
            },
            "entity_type": {
              "type": "string",
              "description": "The administrative type of the entity (e.g., county-level city, prefecture-level city)."
            },
            "province_or_region": {
              "type": "string",
              "description": "The province or region within the country where the entity is located."
            }
          },
          "required": [
            "entity_name",
            "entity_type",
            "province_or_region"
          ],
          "additionalProperties": false
        }
      },
      "total_entities_found": {
        "type": "integer",
        "description": "The total number of entities whose location was identified."
      }
    },
    "required": [
      "country_of_location",
      "entities_located",
      "total_entities_found"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
