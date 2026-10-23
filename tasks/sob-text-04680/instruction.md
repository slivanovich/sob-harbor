{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMingguang: Mingguang (), formerly Jiashan County (), is a county-level city of Anhui Province, China.  It is under the administration of Chuzhou city.\n\nXiaogan: Xiaogan () is a prefecture-level city in east-central Hubei province, People's Republic of China, some 60 km northwest of the provincial capital of Wuhan.  According to the 2010 census, its population totaled 4,814,542, of whom 908,266 lived in the built-up (\"or metro\") area of Xiaonan District.\n\nQuestion: Xiaogan and Mingguang, are located in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"country_name\": {\n      \"type\": \"string\",\n      \"description\": \"The common name of the country where the cities are located.\"\n    },\n    \"country_full_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full official name of the country where the cities are located.\"\n    },\n    \"cities_details\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each city mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"city_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the city.\"\n          },\n          \"administrative_level\": {\n            \"type\": \"string\",\n            \"description\": \"The administrative classification of the city (e.g., county-level, prefecture-level).\"\n          },\n          \"province\": {\n            \"type\": \"string\",\n            \"description\": \"The province where the city is located.\"\n          },\n          \"parent_administration\": {\n            \"type\": \"string\",\n            \"description\": \"The larger administrative entity that the city is under, if specified.\"\n          }\n        },\n        \"required\": [\n          \"city_name\",\n          \"administrative_level\",\n          \"province\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"country_name\",\n    \"country_full_name\",\n    \"cities_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "country_name": {
        "type": "string",
        "description": "The common name of the country where the cities are located."
      },
      "country_full_name": {
        "type": "string",
        "description": "The full official name of the country where the cities are located."
      },
      "cities_details": {
        "type": "array",
        "description": "Details about each city mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "city_name": {
              "type": "string",
              "description": "The name of the city."
            },
            "administrative_level": {
              "type": "string",
              "description": "The administrative classification of the city (e.g., county-level, prefecture-level)."
            },
            "province": {
              "type": "string",
              "description": "The province where the city is located."
            },
            "parent_administration": {
              "type": "string",
              "description": "The larger administrative entity that the city is under, if specified."
            }
          },
          "required": [
            "city_name",
            "administrative_level",
            "province"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "country_name",
      "country_full_name",
      "cities_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
