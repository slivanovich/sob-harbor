{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFanorona: Fanorona (] ) is a strategy board game for two players.  The game is indigenous to Madagascar.\n\nLimaye: Limaye is a family name, common among the Chitpavan Kokanastha Brahmin community in Western Maharashtra, India.  The names Karandikar, Dixit and Khasgiwale are supposedly derived from the same clan.  The origin of the Limaye/Karandikar/Dixit and Khasgiwale family is believed to be from the Western Coast of India, Maharashtra - Ratnagiri, a Southern District of Konkan - Maharashtra region.\n\nDixit (card game): Dixit is a card game created by Jean-Louis Roubira, and published by Libellud.  Using a deck of cards illustrated with dreamlike images, players select cards that match a title suggested by the \"storyteller\", and attempt to guess which card the \"storyteller\" selected.  The game was introduced in 2008.  \"Dixit\" won the 2010 Spiel des Jahres award.\n\nQuestion: Dixit and Fanorona are the names of what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the entities being categorized.\"\n    },\n    \"common_category\": {\n      \"type\": \"string\",\n      \"description\": \"The common category that both entities belong to.\"\n    },\n    \"games\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the game.\"\n          },\n          \"type\": {\n            \"type\": \"string\",\n            \"description\": \"The specific type of game (e.g., board game, card game).\"\n          },\n          \"origin_or_creator\": {\n            \"type\": \"string\",\n            \"description\": \"The origin country or the creator of the game.\"\n          },\n          \"number_of_players\": {\n            \"type\": \"integer\",\n            \"description\": \"The number of players for the game.\"\n          },\n          \"publisher\": {\n            \"type\": \"string\",\n            \"description\": \"The publisher of the game.\"\n          },\n          \"introduction_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the game was introduced.\"\n          },\n          \"award_won\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the award won by the game.\"\n          },\n          \"award_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the award was won.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"type\",\n          \"origin_or_creator\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Detailed information about each game.\"\n    }\n  },\n  \"required\": [\n    \"entity_names\",\n    \"common_category\",\n    \"games\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "Names of the entities being categorized."
      },
      "common_category": {
        "type": "string",
        "description": "The common category that both entities belong to."
      },
      "games": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the game."
            },
            "type": {
              "type": "string",
              "description": "The specific type of game (e.g., board game, card game)."
            },
            "origin_or_creator": {
              "type": "string",
              "description": "The origin country or the creator of the game."
            },
            "number_of_players": {
              "type": "integer",
              "description": "The number of players for the game."
            },
            "publisher": {
              "type": "string",
              "description": "The publisher of the game."
            },
            "introduction_year": {
              "type": "integer",
              "description": "The year the game was introduced."
            },
            "award_won": {
              "type": "string",
              "description": "The name of the award won by the game."
            },
            "award_year": {
              "type": "integer",
              "description": "The year the award was won."
            }
          },
          "required": [
            "name",
            "type",
            "origin_or_creator"
          ],
          "additionalProperties": false
        },
        "description": "Detailed information about each game."
      }
    },
    "required": [
      "entity_names",
      "common_category",
      "games"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
