{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAmmobium: Ammobium is genus of perennial Asteraceae species described as a genus in 1824.\n\nSidalcea: Sidalcea is a genus (approx. 25 species) of the botanical family Malvaceae.  It contains several species of flower known generally as checkerblooms or checkermallows, or prairie mallows in the United Kingdom.  They can be annuals or perennials, some rhizomatous.  They are native to West and Central North America.\n\nSidalcea candida: Sidalcea candida, the white checkerbloom, prairie mallow or white checkermallow, is a wildflower found from Nevada to Wyoming and south to the southern part of New Mexico.  The plant grows to three feet, and is also known as wild hollyhock.  Its flowers are about one inch wide with five petals.  It is found mostly in mountain meadows and along streams.  It flowers between June and September.\n\nQuestion: Are Ammobium and Sidalcea both flowers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_topic\": {\n      \"type\": \"string\",\n      \"description\": \"The main topic or subject of the question.\"\n    },\n    \"genera_information\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each genus mentioned in the context.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"genus_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the plant genus.\"\n          },\n          \"is_flower_genus\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the genus is known to contain flower species.\"\n          },\n          \"botanical_family\": {\n            \"type\": \"string\",\n            \"description\": \"The botanical family to which the genus belongs.\"\n          },\n          \"life_cycle\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"Describes the life cycle of the plants in the genus (e.g., perennial, annual).\"\n          },\n          \"common_names\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"Common names associated with the genus or its species.\"\n          }\n        },\n        \"required\": [\n          \"genus_name\",\n          \"is_flower_genus\",\n          \"botanical_family\",\n          \"life_cycle\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"overall_answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"The direct answer to the question: Are both genera flowers?\"\n    }\n  },\n  \"required\": [\n    \"question_topic\",\n    \"genera_information\",\n    \"overall_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_topic": {
        "type": "string",
        "description": "The main topic or subject of the question."
      },
      "genera_information": {
        "type": "array",
        "description": "Details about each genus mentioned in the context.",
        "items": {
          "type": "object",
          "properties": {
            "genus_name": {
              "type": "string",
              "description": "The name of the plant genus."
            },
            "is_flower_genus": {
              "type": "boolean",
              "description": "Indicates if the genus is known to contain flower species."
            },
            "botanical_family": {
              "type": "string",
              "description": "The botanical family to which the genus belongs."
            },
            "life_cycle": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Describes the life cycle of the plants in the genus (e.g., perennial, annual)."
            },
            "common_names": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Common names associated with the genus or its species."
            }
          },
          "required": [
            "genus_name",
            "is_flower_genus",
            "botanical_family",
            "life_cycle"
          ],
          "additionalProperties": false
        }
      },
      "overall_answer": {
        "type": "boolean",
        "description": "The direct answer to the question: Are both genera flowers?"
      }
    },
    "required": [
      "question_topic",
      "genera_information",
      "overall_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
