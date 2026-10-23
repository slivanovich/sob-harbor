{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPhotinia: Photinia ( ) is a genus of about 40–60 species of small trees and large shrubs, but the taxonomy has recently varied greatly, with the genera \"Heteromeles\", \"Stranvaesia\" and \"Aronia\" sometimes included in \"Photinia\".\n\nNandina: Nandina domestica ( ) commonly known as nandina, heavenly bamboo or sacred bamboo, is a species of flowering plant in the family Berberidaceae, native to eastern Asia from the Himalayas to Japan.  It is the only member of the monotypic genus Nandina.\n\nQuestion: Which genus has more species, Nandina or Photinia \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"comparison_result\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"genus_with_more_species\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the genus identified as having more species.\"\n        },\n        \"more_species_count_range\": {\n          \"type\": \"string\",\n          \"description\": \"The range of species count for the genus with more species, as stated in the context.\"\n        },\n        \"less_species_genus\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the genus identified as having fewer species.\"\n        },\n        \"less_species_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The exact species count for the genus with fewer species.\"\n        }\n      },\n      \"required\": [\n        \"genus_with_more_species\",\n        \"more_species_count_range\",\n        \"less_species_genus\",\n        \"less_species_count\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"photinia_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"genus_name\": {\n          \"type\": \"string\"\n        },\n        \"species_count_range\": {\n          \"type\": \"string\",\n          \"description\": \"The stated range of species for Photinia.\"\n        }\n      },\n      \"required\": [\n        \"genus_name\",\n        \"species_count_range\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"nandina_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"genus_name\": {\n          \"type\": \"string\"\n        },\n        \"species_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The exact species count for Nandina.\"\n        }\n      },\n      \"required\": [\n        \"genus_name\",\n        \"species_count\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"comparison_result\",\n    \"photinia_details\",\n    \"nandina_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "comparison_result": {
        "type": "object",
        "properties": {
          "genus_with_more_species": {
            "type": "string",
            "description": "The name of the genus identified as having more species."
          },
          "more_species_count_range": {
            "type": "string",
            "description": "The range of species count for the genus with more species, as stated in the context."
          },
          "less_species_genus": {
            "type": "string",
            "description": "The name of the genus identified as having fewer species."
          },
          "less_species_count": {
            "type": "integer",
            "description": "The exact species count for the genus with fewer species."
          }
        },
        "required": [
          "genus_with_more_species",
          "more_species_count_range",
          "less_species_genus",
          "less_species_count"
        ],
        "additionalProperties": false
      },
      "photinia_details": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string"
          },
          "species_count_range": {
            "type": "string",
            "description": "The stated range of species for Photinia."
          }
        },
        "required": [
          "genus_name",
          "species_count_range"
        ],
        "additionalProperties": false
      },
      "nandina_details": {
        "type": "object",
        "properties": {
          "genus_name": {
            "type": "string"
          },
          "species_count": {
            "type": "integer",
            "description": "The exact species count for Nandina."
          }
        },
        "required": [
          "genus_name",
          "species_count"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "comparison_result",
      "photinia_details",
      "nandina_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
