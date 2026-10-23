{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBinzhou: Binzhou, formerly Putai, is a prefecture-level city in northern Shandong Province in the People's Republic of China.  The city proper sits on the northern bank of the Yellow River, while its administrative area straddles both sides of its lower course before its present delta.\n\nXinzhou: Xinzhou () is a prefecture-level city occupying the north-central section of Shanxi province, People's Republic of China.\n\nQuestion: What do Xinzhou and Binzhou have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cities_compared\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the cities being compared.\"\n    },\n    \"common_features\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"feature_type\": {\n            \"type\": \"string\",\n            \"description\": \"The category of the common feature (e.g., 'country', 'administrative_level').\"\n          },\n          \"feature_value\": {\n            \"type\": \"string\",\n            \"description\": \"The specific value that is common between the cities.\"\n          }\n        },\n        \"required\": [\n          \"feature_type\",\n          \"feature_value\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of common attributes shared by the cities.\"\n    },\n    \"number_of_common_features\": {\n      \"type\": \"integer\",\n      \"description\": \"The total count of common features identified.\"\n    }\n  },\n  \"required\": [\n    \"cities_compared\",\n    \"common_features\",\n    \"number_of_common_features\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cities_compared": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the cities being compared."
      },
      "common_features": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "feature_type": {
              "type": "string",
              "description": "The category of the common feature (e.g., 'country', 'administrative_level')."
            },
            "feature_value": {
              "type": "string",
              "description": "The specific value that is common between the cities."
            }
          },
          "required": [
            "feature_type",
            "feature_value"
          ],
          "additionalProperties": false
        },
        "description": "A list of common attributes shared by the cities."
      },
      "number_of_common_features": {
        "type": "integer",
        "description": "The total count of common features identified."
      }
    },
    "required": [
      "cities_compared",
      "common_features",
      "number_of_common_features"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
