{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOlearia solandri: Olearia solandri, commonly known as coastal daisy-bush or coastal tree daisy, is a coastal shrub of New Zealand.\n\nOlearia macrodonta: Olearia macrodonta (mountain holly or arorangi in New Zealand, or New Zealand holly elsewhere) is a small sub-alpine evergreen tree endemic to New Zealand, from the plant family Asteraceae.  It is closely related to the narrow-leaved \"Olearia ilicifolia\", with which it shares several characteristics including largely undulating and serrated grey-green leaves.  These common characteristics mean the two species are often confused with one another.  It is found in lowland to sub-alpine forests from the East Cape of the North Island of New Zealand southwards throughout the South Island and Stewart Island, at 450 - in altitude.\n\nOlearia ilicifolia: Olearia ilicifolia is a shrub or small tree endemic to New Zealand.  Common names include Maori-holly, mountain holly, hakeke or hakekeke and New Zealand holly.  It is a spreading shrub or small tree of the family Asteraceae, and has largely serrated and undulating grey-green leaves.  It is closely related to the sub-alpine \"Olearia macrodonta\", with which it shares the names mountain holly and New Zealand holly, however it is much more common than \"Olearia macrodonta\".  It is found in lowland and sub-alpine forests from sea level to 1200 m .\n\nLaw of New Zealand: The law of New Zealand can be found in several sources.  The primary sources of New Zealand law are statutes enacted by the New Zealand Parliament and decisions of the Courts of New Zealand.  At a more fundamental level, the law of New Zealand is based on three related principles: parliamentary sovereignty; the rule of law; and the separation of powers.  As a former British colony, the New Zealand legal system is heavily based on the English law, and remains similar in many respects.  There are also important differences, which reflect the unique legal culture that has developed in New Zealand.\n\nBrachyglottis stewartiae: Brachyglottis stewartiae is a species of flowering plant, often referred to as a tree daisy, in the Asteraceae family.  It is found only in New Zealand, especially on its subantarctic islands.  With another tree daisy, \"Olearia lyallii\", it is common in the forest of the Snares Islands, growing to about 6 m in height.  It bears conspicuous clusters of yellow daisy-like flowers.\n\nOlearia paniculata: Olearia paniculata, commonly called akiraho, is a species of shrub or tree in the Asteraceae family, found only in New Zealand.  The tree can grow to 7.5 metres high, and has yellow-green, oval-shaped leaves, with white undersides and wavy margins.\n\nAtomotricha colligatella: Atomotricha colligatella, the Olearia Skeletoniser, is a moth of the Oecophoridae family.  It was described by Francis Walker in 1864.  It is found in New Zealand.\n\nOlearia lyallii: Olearia lyallii is a New Zealand plant from the genus \"Olearia\".  It is commonly known as the subantarctic tree daisy.  The species is endemic to the Snares Islands and southern New Zealand, and has also established itself as an introduced species on the Auckland Islands, where the type specimen was described from.  \"O. lyallii\" forms trees up to 10 m tall with trunks 50 cm in diameter.\n\nOlearia: Olearia is a genus of flowering plants belonging to the family Asteraceae.  There are about 130 different species within the genus found mostly in Australia, New Guinea and New Zealand.  The genus includes herbaceous plants, shrubs and small trees.  The latter are unusual among the Asteraceae and are called \"tree daisies\" in New Zealand.  All bear the familiar daisy-like composite flowerheads.\n\nBreynia: Breynia is a plant genus in the family Phyllanthaceae, first described as a genus in 1776.  It is native to Southeast Asia, China, the Indian Subcontinent, Papuasia, Australia, and the island of Réunion.\n\nQuestion: Are both Olearia and Breynia found in New Zealand?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"genus_names\": {\n      \"type\": \"array\",\n      \"description\": \"List of plant genera mentioned in the question.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"genus_location_details\": {\n      \"type\": \"array\",\n      \"description\": \"Details about the location of each genus.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"genus_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the plant genus.\"\n          },\n          \"is_found_in_new_zealand\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the genus is found in New Zealand, false otherwise.\"\n          },\n          \"known_native_regions\": {\n            \"type\": \"array\",\n            \"description\": \"A list of regions where the genus is known to be native.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"required\": [\n          \"genus_name\",\n          \"is_found_in_new_zealand\",\n          \"known_native_regions\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"both_found_in_new_zealand\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both specified genera are found in New Zealand, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"genus_names\",\n    \"genus_location_details\",\n    \"both_found_in_new_zealand\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "genus_names": {
        "type": "array",
        "description": "List of plant genera mentioned in the question.",
        "items": {
          "type": "string"
        }
      },
      "genus_location_details": {
        "type": "array",
        "description": "Details about the location of each genus.",
        "items": {
          "type": "object",
          "properties": {
            "genus_name": {
              "type": "string",
              "description": "The name of the plant genus."
            },
            "is_found_in_new_zealand": {
              "type": "boolean",
              "description": "True if the genus is found in New Zealand, false otherwise."
            },
            "known_native_regions": {
              "type": "array",
              "description": "A list of regions where the genus is known to be native.",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "genus_name",
            "is_found_in_new_zealand",
            "known_native_regions"
          ],
          "additionalProperties": false
        }
      },
      "both_found_in_new_zealand": {
        "type": "boolean",
        "description": "True if both specified genera are found in New Zealand, false otherwise."
      }
    },
    "required": [
      "question_asked",
      "genus_names",
      "genus_location_details",
      "both_found_in_new_zealand"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
