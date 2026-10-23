{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLa straniera: La straniera (\"The Foreign Woman\") is an opera in two acts with music by Vincenzo Bellini to an Italian libretto by Felice Romani, based on the novel \"L'Étrangère\" (2 vols, 1825) by Charles-Victor Prévot, vicomte d'Arlincourt, although writer Herbert Weinstock also adds that it is \"more likely [based on] a dramatization of [that novel] in Italian by Giovan Carlo, barone di Cosenza\" since he then quotes a letter from Bellini to his friend Francesco Florimo in which he says that Romani \"certainly will not follow the play\" [suggesting then that they were aware of its existence.]\n\nPlatée: Rameau's first attempt at comic opera, the plot concerns an ugly water nymph who believes that Jupiter, the king of the gods, is in love with her.  The work was initially called a \"ballet bouffon\", though it was later styled a \"comédie lyrique\", putting it in the same category as Rameau's \"Les Paladins\".  It was written for the celebrations of the wedding of Louis, Dauphin of France, son of King Louis XV of France, to the Infanta Maria Theresa of Spain, who, according to contemporary sources, like the title character was no beauty.  Instead of getting the composer into trouble, the entertainment at Versailles seems to have been well received, and Rameau was appointed a few months later to the position of Composer of the King's Chamber Music with a sizable annual pension.\n\nQuestion:  Platée and La straniera are what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the entities being classified.\"\n    },\n    \"common_classification\": {\n      \"type\": \"string\",\n      \"description\": \"The common classification or type for all listed entities.\"\n    },\n    \"entity_details\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the specific entity.\"\n          },\n          \"specific_type_description\": {\n            \"type\": \"string\",\n            \"description\": \"The specific type or description of the entity as found in the context.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"specific_type_description\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Detailed information for each entity, including its specific type.\"\n    }\n  },\n  \"required\": [\n    \"entity_names\",\n    \"common_classification\",\n    \"entity_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the entities being classified."
      },
      "common_classification": {
        "type": "string",
        "description": "The common classification or type for all listed entities."
      },
      "entity_details": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the specific entity."
            },
            "specific_type_description": {
              "type": "string",
              "description": "The specific type or description of the entity as found in the context."
            }
          },
          "required": [
            "name",
            "specific_type_description"
          ],
          "additionalProperties": false
        },
        "description": "Detailed information for each entity, including its specific type."
      }
    },
    "required": [
      "entity_names",
      "common_classification",
      "entity_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
