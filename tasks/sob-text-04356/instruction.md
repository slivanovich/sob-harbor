{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2003 FIA GT Donington 500km: The 2003 FIA GT Donington 500 km was the fifth round the 2003 FIA GT Championship season.  It took place at Donington Park, United Kingdom, on 29 June 2003.\n\nCircuit de Nevers Magny-Cours: Circuit de Nevers Magny-Cours, which has a capacity of 90,000, is a motor racing circuit located in central France, near the towns of Magny-Cours and Nevers, some 250 km (160 miles) from Paris.\n\n2000 FIA GT Magny-Cours 500km: The 2000 FIA GT Magny-Cours 500 km was the tenth and final round the 2000 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on October 22, 2000.\n\n2003 FIA GT Brno 500km: The 2003 FIA GT Brno 500 km was the fourth round the 2003 FIA GT Championship season.  It took place at the Brno Circuit, Czech Republic, on May 25, 2003.\n\n2003 FIA GT Barcelona 500km: The 2003 FIA GT Barcelona 500 km was the opening round the 2003 FIA GT Championship season.  It took place at the Circuit de Catalunya, Spain, on April 6, 2003.\n\n2004 FIA GT Magny-Cours 500km: The 2004 FIA GT Magny-Cours 500 km was the third round the 2004 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on 2 May 2004.\n\n2003 FIA GT Magny-Cours 500km: The 2003 FIA GT Magny-Cours 500 km was the second round the 2003 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on April 27, 2003.\n\n2002 FIA GT Magny-Cours 500km: The 2002 FIA GT Magny-Cours 500 km was the opening round the 2002 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on April 21, 2002.\n\n2001 FIA GT Magny-Cours 500km: The 2001 FIA GT Magny-Cours 500 km was the third round the 2001 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on May 1, 2001.\n\n2003 FIA GT Pergusa 500km: The 2003 FIA GT Pergusa 500 km was the third round the 2003 FIA GT Championship season.  It took place at the Autodromo di Pergusa, Italy, on May 11, 2003.\n\nQuestion: What is the capacity of the circuit that the 2003 FIA GT Magny-Cours 500km took place?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the motor racing event.\"\n    },\n    \"event_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the event took place.\"\n    },\n    \"circuit\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the circuit.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the circuit is located.\"\n        },\n        \"capacity\": {\n          \"type\": \"integer\",\n          \"description\": \"The spectator capacity of the circuit.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country\",\n        \"capacity\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_capacity\": {\n      \"type\": \"integer\",\n      \"description\": \"The capacity of the circuit where the event took place.\"\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"event_year\",\n    \"circuit\",\n    \"answer_capacity\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the motor racing event."
      },
      "event_year": {
        "type": "integer",
        "description": "The year the event took place."
      },
      "circuit": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the circuit."
          },
          "country": {
            "type": "string",
            "description": "The country where the circuit is located."
          },
          "capacity": {
            "type": "integer",
            "description": "The spectator capacity of the circuit."
          }
        },
        "required": [
          "name",
          "country",
          "capacity"
        ],
        "additionalProperties": false
      },
      "answer_capacity": {
        "type": "integer",
        "description": "The capacity of the circuit where the event took place."
      }
    },
    "required": [
      "event_name",
      "event_year",
      "circuit",
      "answer_capacity"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
