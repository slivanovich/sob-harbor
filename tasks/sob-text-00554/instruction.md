{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe President's Mystery: The President's Mystery is a 1936 American film directed by Phil Rosen.\n\nI Killed That Man: I Killed That Man is a 1941 American film directed by Phil Rosen that was a remake of his 1933 film \"The Devil's Mate\".  It starred Ricardo Cortez and was produced by the King Brothers.\n\nBeggars in Ermine: Beggars in Ermine is a 1934 American film directed by Phil Rosen.\n\nPaul Bogart: Paul Bogart (November 21, 1919 – April 15, 2012) was an American television and film director and producer.\n\nBorn to Gamble: Born to Gamble (1935) is an American film directed by Phil Rosen and released by Republic Pictures.\n\nPhil Rosen: Phil Rosen (May 8, 1888 – October 22, 1951) was an American film director and cinematographer.  He directed 142 films between 1915 and 1949.\n\nThe Scarlet Clue: The Scarlet Clue is a 1945 American film directed by Phil Rosen.\n\nRoad to Happiness: Road to Happiness is a 1942 American film directed by Phil Rosen.\n\nRoar of the Press: Roar of the Press is a 1941 American film directed by Phil Rosen.\n\nPaper Bullets: Paper Bullets is a 1941 American film directed by Phil Rosen and starring Joan Woodbury.  It was the first film produced by the King Brothers, launching their career.\n\nQuestion: Are Phil Rosen and Paul Bogart American film directors?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"overall_answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals are American film directors, false otherwise.\"\n    },\n    \"individuals_checked\": {\n      \"type\": \"array\",\n      \"description\": \"Details for each individual mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"is_american\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is American.\"\n          },\n          \"is_film_director\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is a film director.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The stated nationality of the individual.\"\n          },\n          \"professions\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"A list of professions attributed to the individual.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_american\",\n          \"is_film_director\",\n          \"nationality\",\n          \"professions\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"number_of_individuals_found\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of individuals found in the context that were asked about.\"\n    }\n  },\n  \"required\": [\n    \"overall_answer\",\n    \"individuals_checked\",\n    \"number_of_individuals_found\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "overall_answer": {
        "type": "boolean",
        "description": "True if both individuals are American film directors, false otherwise."
      },
      "individuals_checked": {
        "type": "array",
        "description": "Details for each individual mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "is_american": {
              "type": "boolean",
              "description": "True if the individual is American."
            },
            "is_film_director": {
              "type": "boolean",
              "description": "True if the individual is a film director."
            },
            "nationality": {
              "type": "string",
              "description": "The stated nationality of the individual."
            },
            "professions": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of professions attributed to the individual."
            }
          },
          "required": [
            "name",
            "is_american",
            "is_film_director",
            "nationality",
            "professions"
          ],
          "additionalProperties": false
        }
      },
      "number_of_individuals_found": {
        "type": "integer",
        "description": "The total number of individuals found in the context that were asked about."
      }
    },
    "required": [
      "overall_answer",
      "individuals_checked",
      "number_of_individuals_found"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
