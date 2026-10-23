{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMonanthes: Monanthes is a genus of small, succulent, subtropical plants of the Crassulaceae family.  The about ten species are mostly endemic to the Canary Islands and Savage Islands, with some found on Madeira.  Its center of diversity is Tenerife, with seven species occurring on this island.  On Fuerteventura and Lanzarote, only \"M. laxiflora\" occurs.\n\nAichryson: Aichryson is a genus of about 15 species of succulent, subtropical plants, mostly native to the Canary Islands, with a few in the Azores, Madeira and Morocco, and one in Portugal.\n\nGlottiphyllum: Glottiphyllum is a genus of about 57 species of succulent subtropical plants of the family \"Aizoaceae\".\n\nChrysosplenium: Chrysosplenium (golden saxifrage or golden-saxifrage) is a genus of 57 species of flowering plants in the family Saxifragaceae.  Species can be found throughout the arctic and northern temperate parts of the Northern Hemisphere, with the highest species diversity in eastern Asia; two species are found disjunctly in South America.\n\nGlottiphyllum longum: Glottiphyllum longum is a species of succulent plant in the Aizoaceae family, native to South Africa.\n\nAriocarpus: Ariocarpus is a genus of 8 species of succulent, subtropical plants of the Cactaceae family.\n\nGlottiphyllum cruciatum: Glottiphyllum cruciatum is a species that are part of over 50 succulents that are subtropical plants of the family \"Aizoaceae\".  The plant has many synonyms including \"Glottiphyllum angustum\".\n\nAeonium: Aeonium (tree houseleek) is a genus of about 35 species of succulent, subtropical plants of the family Crassulaceae.  Many species are popular in horticulture.  The genus name comes from the ancient Greek \"aionos\" (ageless).  While most of them are native to the Canary Islands, some are found in Madeira, Morocco, and in East Africa (for example in the Semien Mountains of Ethiopia).\n\nGlottiphyllum uncatum: Glottiphyllum uncatum is a species of succulent plant in the Aizoaceae family, native to South Africa.\n\nArthrocereus: Arthrocereus is a genus of cactus, originating from southern Minas Gerais, Brazil.\n\nQuestion: What is a genus of about 57 species of succulent subtropical plants of the family \"Aizoaceae\", Arthrocereus or Glottiphyllum ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"identified_genus_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the genus that matches the description.\"\n    },\n    \"species_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The approximate number of species in the genus.\"\n    },\n    \"plant_characteristics\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of characteristics describing the plants in the genus.\"\n    },\n    \"family\": {\n      \"type\": \"string\",\n      \"description\": \"The botanical family to which the genus belongs.\"\n    },\n    \"is_correct_answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if this genus is the correct answer to the question posed.\"\n    }\n  },\n  \"required\": [\n    \"identified_genus_name\",\n    \"species_count\",\n    \"plant_characteristics\",\n    \"family\",\n    \"is_correct_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "identified_genus_name": {
        "type": "string",
        "description": "The name of the genus that matches the description."
      },
      "species_count": {
        "type": "integer",
        "description": "The approximate number of species in the genus."
      },
      "plant_characteristics": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of characteristics describing the plants in the genus."
      },
      "family": {
        "type": "string",
        "description": "The botanical family to which the genus belongs."
      },
      "is_correct_answer": {
        "type": "boolean",
        "description": "Indicates if this genus is the correct answer to the question posed."
      }
    },
    "required": [
      "identified_genus_name",
      "species_count",
      "plant_characteristics",
      "family",
      "is_correct_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
