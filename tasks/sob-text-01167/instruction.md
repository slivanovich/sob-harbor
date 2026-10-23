{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKuytun: Kuytun or Kuitun () is a county-level city with about 285,000 residents (2000 census) in Ili Kazakh Autonomous Prefecture, Xinjiang, China.  Kuitun is located between Wusu and Shihezi on the railway from Ürümqi to Kazakhstan, close to a desert.\n\nZaoyang: Zaoyang () is a city in northern Hubei province, People's Republic of China, near the border with Henan province.  Administratively, it is a county-level city under the administration of Xiangyang.\n\nQuestion: Zaoyang and Kuytun, are in which country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cities_mentioned\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"city_name\": {\n            \"type\": \"string\"\n          },\n          \"administrative_division\": {\n            \"type\": \"string\"\n          },\n          \"country\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"city_name\",\n          \"country\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"number_of_cities\": {\n      \"type\": \"integer\"\n    },\n    \"common_country\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"cities_mentioned\",\n    \"number_of_cities\",\n    \"common_country\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cities_mentioned": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "city_name": {
              "type": "string"
            },
            "administrative_division": {
              "type": "string"
            },
            "country": {
              "type": "string"
            }
          },
          "required": [
            "city_name",
            "country"
          ],
          "additionalProperties": false
        }
      },
      "number_of_cities": {
        "type": "integer"
      },
      "common_country": {
        "type": "string"
      }
    },
    "required": [
      "cities_mentioned",
      "number_of_cities",
      "common_country"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
