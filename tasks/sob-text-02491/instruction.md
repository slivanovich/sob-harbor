{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOnoclea: Onoclea is a genus of plants in the Onocleaceae family, native to moist habitats in eastern Asia and eastern North America.  They are deciduous ferns with sterile fronds arising from creeping rhizomes in spring, dying down at first frost.  Fertile fronds appear in late summer.  Depending on the authority, the genus contains one to five species.\n\nBunchosia: Bunchosia is a genus in the Malpighiaceae, a family of about 75 genera of flowering plants in the order Malpighiales.  It contains roughly 75 species of trees and shrubs, which are native to dry woodlands, savannas, and wet forests.  Their range extends from Mexico and the Caribbean to southeastern Brazil and adjacent Argentina.  \"Bunchosia\" is one of three arborescent genera of Malpighiaceae with fleshy, bird-dispersed fruits.\n\nQuestion: Are both Bunchosia and Onoclea genus of plants?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_context\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the main subject of the question.\"\n    },\n    \"onoclea_classification\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_genus\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if Onoclea is classified as a genus.\"\n        },\n        \"is_plant\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if Onoclea is a genus of plants.\"\n        },\n        \"family\": {\n          \"type\": \"string\",\n          \"description\": \"The botanical family Onoclea belongs to.\"\n        }\n      },\n      \"required\": [\n        \"is_genus\",\n        \"is_plant\",\n        \"family\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"bunchosia_classification\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_genus\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if Bunchosia is classified as a genus.\"\n        },\n        \"is_plant\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if Bunchosia is a genus of plants.\"\n        },\n        \"family\": {\n          \"type\": \"string\",\n          \"description\": \"The botanical family Bunchosia belongs to.\"\n        }\n      },\n      \"required\": [\n        \"is_genus\",\n        \"is_plant\",\n        \"family\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"both_are_plant_genera\": {\n      \"type\": \"boolean\",\n      \"description\": \"The final answer to whether both Onoclea and Bunchosia are genera of plants.\"\n    }\n  },\n  \"required\": [\n    \"question_context\",\n    \"onoclea_classification\",\n    \"bunchosia_classification\",\n    \"both_are_plant_genera\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_context": {
        "type": "string",
        "description": "Describes the main subject of the question."
      },
      "onoclea_classification": {
        "type": "object",
        "properties": {
          "is_genus": {
            "type": "boolean",
            "description": "Indicates if Onoclea is classified as a genus."
          },
          "is_plant": {
            "type": "boolean",
            "description": "Indicates if Onoclea is a genus of plants."
          },
          "family": {
            "type": "string",
            "description": "The botanical family Onoclea belongs to."
          }
        },
        "required": [
          "is_genus",
          "is_plant",
          "family"
        ],
        "additionalProperties": false
      },
      "bunchosia_classification": {
        "type": "object",
        "properties": {
          "is_genus": {
            "type": "boolean",
            "description": "Indicates if Bunchosia is classified as a genus."
          },
          "is_plant": {
            "type": "boolean",
            "description": "Indicates if Bunchosia is a genus of plants."
          },
          "family": {
            "type": "string",
            "description": "The botanical family Bunchosia belongs to."
          }
        },
        "required": [
          "is_genus",
          "is_plant",
          "family"
        ],
        "additionalProperties": false
      },
      "both_are_plant_genera": {
        "type": "boolean",
        "description": "The final answer to whether both Onoclea and Bunchosia are genera of plants."
      }
    },
    "required": [
      "question_context",
      "onoclea_classification",
      "bunchosia_classification",
      "both_are_plant_genera"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
