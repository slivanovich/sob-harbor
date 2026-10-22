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
1989 Virginia Slims of Albuquerque – Doubles: Nicole Provis and Elna Reinach won in the final 4–6, 6–4, 6–2 against Raffaella Reggi and Arantxa Sánchez Vicario.

Raffaella Reggi: Raffaella Reggi (born 27 November 1965; ] ) is a former professional tennis player from Italy.

1989 Virginia Slims of Oklahoma – Doubles: Jana Novotná and Catherine Suire were the defending champions but only Suire competed that year with Raffaella Reggi.

1987 US Open – Mixed Doubles: Raffaella Reggi and Sergio Casal were the defending champions but lost in the semifinals to Martina Navratilova and Emilio Sánchez.

1988 Virginia Slims of San Diego – Singles: Raffaella Reggi was the defending champion but did not compete that year.

1988 Belgian Open – Doubles: Bettina Bunge and Katerina Maleeva were the defending champions but only Maleeva competed that year with Raffaella Reggi.

Oslo Open: The Oslo Open was a women's professional tennis tournament held in Oslo, Norway.  The event was part of the Women's Tennis Association (WTA) Tour and was played only once, in 1991.  It was classed as a Tier V event, and it was competed on an indoor carpet surface.  Catarina Lindqvist won the singles competition and Claudia Kohde-Kilsch and Silke Meier won the doubles; Raffaella Reggi finished runner-up in both events.  There was a total prize money on offer of US$100,000.

1989 Eckerd Open – Doubles: Terry Phelps and Raffaella Reggi were the defending champions but did not compete that year.

1989 Pilkington Glass Championships – Singles: Martina Navratilova was the defending champion and won in the final 7–6, 6–2 against Raffaella Reggi.

Marion Bartoli: Marion Bartoli (] ; born 2 October 1984) is a French former professional tennis player.  She won the 2013 Wimbledon Championships singles title after previously being runner-up in 2007 and was a semifinalist at the 2011 French Open.  She also won eight Women's Tennis Association singles titles and three doubles titles.  She announced her immediate retirement from professional tennis on 14 August 2013.

Question: Are Raffaella Reggi and Marion Bartoli both former tennis players?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question asked."
    },
    "player_comparison": {
      "type": "object",
      "properties": {
        "player_one": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "Name of the first player."
            },
            "is_former_professional": {
              "type": "boolean",
              "description": "True if the player is a former professional tennis player."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the player."
            }
          },
          "required": [
            "name",
            "is_former_professional",
            "nationality"
          ],
          "additionalProperties": false
        },
        "player_two": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "Name of the second player."
            },
            "is_former_professional": {
              "type": "boolean",
              "description": "True if the player is a former professional tennis player."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the player."
            }
          },
          "required": [
            "name",
            "is_former_professional",
            "nationality"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "player_one",
        "player_two"
      ],
      "additionalProperties": false
    },
    "both_are_former_players": {
      "type": "boolean",
      "description": "True if both players are former professional tennis players, false otherwise."
    }
  },
  "required": [
    "question_asked",
    "player_comparison",
    "both_are_former_players"
  ],
  "additionalProperties": false
}
