{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBessera: Bessera is a genus of Mexican plants in the cluster lily subfamily within the asparagus family.  It is a small genus of 3 known species of mostly herbaceous flowering plants with corms.  They have flowers with petals and petaloid sepals (tepals) with compound pistils.\n\nSesleria: Sesleria is a Eurasian and North African genus of perennial plants in the grass family.\n\nSesleria caerulea: Sesleria caerulea, known as blue moor-grass, is a species of perennial grass in the Poaceae family, native to Europe.\n\nSesleria insularis: Sesleria insularis is a species of perennial grass in the Poaceae family, with culms 30–65 cm long.\n\nSesleria albicans: Sesleria albicans is a species of perennial grass in the Poaceae family which can be found throughout Europe.\n\nSesleria heufleriana: Sesleria heufleriana is a species of perennial grass in the Poaceae family, native to central, southeastern, and eastern Europe and the Caucasus.  Culms are erect, ranging from 30–70 cm long; leaf-blades are conduplicate or convolute, and 20–35 cm long by 2–3 mm wide.\n\nSesleria argentea: Sesleria argentea is a species of perennial grass in the Poaceae family.  It is 35 – long with a 0.5 – long ciliolate membrane.  Its leaves are either conduplicate or convolute, and are 10 – long and 3 – wide.  It also has a linear panicle spiciform which is 3.5 – long and 0.5 – wide.\n\nQuestion: Both Bessera and Sesleria are?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_classification\": {\n      \"type\": \"string\",\n      \"description\": \"The common biological classification level for both entities.\"\n    },\n    \"common_plant_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general type of organism both entities represent.\"\n    },\n    \"genera_information\": {\n      \"type\": \"array\",\n      \"description\": \"Detailed information about each genus mentioned.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"genus_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the genus.\"\n          },\n          \"family\": {\n            \"type\": \"string\",\n            \"description\": \"The plant family the genus belongs to.\"\n          },\n          \"origin_regions\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"Regions where the genus is native.\"\n          },\n          \"is_perennial\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the genus consists of perennial plants.\"\n          },\n          \"number_of_known_species\": {\n            \"type\": \"integer\",\n            \"description\": \"The number of known species within the genus.\"\n          }\n        },\n        \"required\": [\n          \"genus_name\",\n          \"family\",\n          \"origin_regions\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"common_classification\",\n    \"common_plant_type\",\n    \"genera_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_classification": {
        "type": "string",
        "description": "The common biological classification level for both entities."
      },
      "common_plant_type": {
        "type": "string",
        "description": "The general type of organism both entities represent."
      },
      "genera_information": {
        "type": "array",
        "description": "Detailed information about each genus mentioned.",
        "items": {
          "type": "object",
          "properties": {
            "genus_name": {
              "type": "string",
              "description": "The name of the genus."
            },
            "family": {
              "type": "string",
              "description": "The plant family the genus belongs to."
            },
            "origin_regions": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Regions where the genus is native."
            },
            "is_perennial": {
              "type": "boolean",
              "description": "Indicates if the genus consists of perennial plants."
            },
            "number_of_known_species": {
              "type": "integer",
              "description": "The number of known species within the genus."
            }
          },
          "required": [
            "genus_name",
            "family",
            "origin_regions"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "common_classification",
      "common_plant_type",
      "genera_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
