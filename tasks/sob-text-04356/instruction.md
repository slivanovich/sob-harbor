Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
2003 FIA GT Donington 500km: The 2003 FIA GT Donington 500 km was the fifth round the 2003 FIA GT Championship season.  It took place at Donington Park, United Kingdom, on 29 June 2003.

Circuit de Nevers Magny-Cours: Circuit de Nevers Magny-Cours, which has a capacity of 90,000, is a motor racing circuit located in central France, near the towns of Magny-Cours and Nevers, some 250 km (160 miles) from Paris.

2000 FIA GT Magny-Cours 500km: The 2000 FIA GT Magny-Cours 500 km was the tenth and final round the 2000 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on October 22, 2000.

2003 FIA GT Brno 500km: The 2003 FIA GT Brno 500 km was the fourth round the 2003 FIA GT Championship season.  It took place at the Brno Circuit, Czech Republic, on May 25, 2003.

2003 FIA GT Barcelona 500km: The 2003 FIA GT Barcelona 500 km was the opening round the 2003 FIA GT Championship season.  It took place at the Circuit de Catalunya, Spain, on April 6, 2003.

2004 FIA GT Magny-Cours 500km: The 2004 FIA GT Magny-Cours 500 km was the third round the 2004 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on 2 May 2004.

2003 FIA GT Magny-Cours 500km: The 2003 FIA GT Magny-Cours 500 km was the second round the 2003 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on April 27, 2003.

2002 FIA GT Magny-Cours 500km: The 2002 FIA GT Magny-Cours 500 km was the opening round the 2002 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on April 21, 2002.

2001 FIA GT Magny-Cours 500km: The 2001 FIA GT Magny-Cours 500 km was the third round the 2001 FIA GT Championship season.  It took place at the Circuit de Nevers Magny-Cours, France, on May 1, 2001.

2003 FIA GT Pergusa 500km: The 2003 FIA GT Pergusa 500 km was the third round the 2003 FIA GT Championship season.  It took place at the Autodromo di Pergusa, Italy, on May 11, 2003.

Question: What is the capacity of the circuit that the 2003 FIA GT Magny-Cours 500km took place?

Respond with JSON matching this schema:
{
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
}
