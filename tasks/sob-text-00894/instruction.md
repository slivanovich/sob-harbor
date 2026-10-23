{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTo Die like a Man: To Die like a Man (Portuguese: Morrer Como Um Homem ) is a 2009 Portuguese drama film directed by João Pedro Rodrigues, produced by the production company Rosa Filmes.\n\nThe Ornithologist (film): The Ornithologist (original title: O Ornitólogo) is a 2016 Portuguese film directed by João Pedro Rodrigues.  It was released in 2016.\n\nTwo Drifters: Two Drifters (also known as Odete) is a Portuguese feature film directed by João Pedro Rodrigues, produced at the independent production company Rosa Filmes and released in 2005.\n\nJoão Pedro Mendes Silva: João Pedro Mendes Silva, known as João Pedro (born 27 July 1989) is a Portuguese football player who plays for Vizela.\n\nJoão Pedro Guerra Cunha: João Pedro Guerra Cunha (born 4 May 1986 in Figueira de Castelo Rodrigo, Guarda), known as João Pedro, is a Portuguese professional footballer who plays for Cypriot club Apollon Limassol as a midfielder.\n\nA Última Vez Que Vi Macau: A Última Vez Que Vi Macau is a 2012 Portuguese film directed by João Pedro Rodrigues and João Rui Guerra da Mata.  It will be in competition for the Golden Leopard at the 2012 Locarno International Film Festival.  It was shot in Macau.\n\nJoão Pedro (Brazilian footballer): João Pedro Geraldino dos Santos Galvão (born 9 March 1992), commonly known as João Pedro, is a Brazilian professional footballer who plays for Cagliari Calcio as an attacking midfielder.\n\nJoão Pedro Sousa Silva: João Pedro Sousa Silva (born 13 November 1996 in Ponta Delgada, Azores), known as João Pedro, is a Portuguese professional footballer who plays for Gil Vicente F.C. as a forward.\n\nJoão Pedro Rodrigues: João Pedro Rodrigues is a Portuguese film director.  He is considered to be part of \"The School of Reis\" film family.\n\nMaurice Pialat: Maurice Pialat (] ; 31 August 1925 – 11 January 2003) was a French film director, screenwriter and actor noted for the rigorous and unsentimental style of his films.  His work is often described as being \"realist\", though many film critics acknowledge that it does not fit the traditional definition of realism.\n\nQuestion: What career did Maurice Pialat and João Pedro Rodrigues share?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"careers\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"careers\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"careers\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"careers\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"shared_career\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"person_1\",\n    \"person_2\",\n    \"shared_career\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "careers": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "careers"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "careers": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "careers"
        ],
        "additionalProperties": false
      },
      "shared_career": {
        "type": "string"
      }
    },
    "required": [
      "person_1",
      "person_2",
      "shared_career"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
