{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCistus ladanifer: Cistus ladanifer is a species of flowering plant in the family Cistaceae.  It is native to the western Mediterranean region.  Common names include gum rockrose, laudanum, labdanum, common gum cistus, and brown-eyed rockrose.\n\nAbelia: Abelia is a genus of about 30 species and many hybrids in the honeysuckle family Caprifoliaceae.  Some authors, including the Angiosperm Phylogeny Group, consider \"Abelia\" and related genera to belong instead in the segregate family Linnaeaceae, also including such genera as \"Linnaea\", \"Abelia\", \"Dipelta\", \"Kolkwitzia\", and \"Zabelia\", but not such others as \"Lonicera\" or \"Symphoricarpos,\" included by them instead in a more narrowly viewed Caprifoliaceae.\n\nCistus: Cistus (from the Greek \"kistos\") is a genus of flowering plants in the rockrose family Cistaceae, containing about 20 species (Ellul \"et al.\" 2002).  They are perennial shrubs found on dry or rocky soils throughout the Mediterranean region, from Morocco and Portugal through to the Middle East, and also on the Canary Islands.\n\nCistus monspeliensis: Cistus monspeliensis is a species of rockrose known by the common name Montpellier cistus.  It is native to southern Europe and northern Africa, in the Mediterranean forests, woodlands, and scrub ecosystems of matorral—maquis shrublands.\n\nCistus salviifolius: Cistus salviifolius, common names sage-leaved rock-rose, salvia cistus or Gallipoli rose, is a perennial ligneous plant of the family Cistaceae.\n\nQuestion: What does Cistus and Abelia have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_classification_type\": {\n      \"type\": \"string\",\n      \"description\": \"The common biological classification level shared by the entities.\"\n    },\n    \"entities_compared\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity.\"\n          },\n          \"family\": {\n            \"type\": \"string\",\n            \"description\": \"The family to which the entity belongs.\"\n          },\n          \"species_count\": {\n            \"type\": \"integer\",\n            \"description\": \"The approximate number of species within this genus, if specified.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"family\",\n          \"species_count\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Details of the entities being compared.\"\n    },\n    \"comparison_summary\": {\n      \"type\": \"string\",\n      \"description\": \"A brief summary of what the entities have in common.\"\n    }\n  },\n  \"required\": [\n    \"common_classification_type\",\n    \"entities_compared\",\n    \"comparison_summary\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_classification_type": {
        "type": "string",
        "description": "The common biological classification level shared by the entities."
      },
      "entities_compared": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the entity."
            },
            "family": {
              "type": "string",
              "description": "The family to which the entity belongs."
            },
            "species_count": {
              "type": "integer",
              "description": "The approximate number of species within this genus, if specified."
            }
          },
          "required": [
            "name",
            "family",
            "species_count"
          ],
          "additionalProperties": false
        },
        "description": "Details of the entities being compared."
      },
      "comparison_summary": {
        "type": "string",
        "description": "A brief summary of what the entities have in common."
      }
    },
    "required": [
      "common_classification_type",
      "entities_compared",
      "comparison_summary"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
