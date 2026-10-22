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
1994 Gerry Weber Open – Doubles: Petr Korda and Cyril Suk were the defending champions, but Korda did not participate this year.  Suk partnered Daniel Vacek, losing in the quarterfinals.

2005 Qatar Open – Doubles: Martin Damm and Cyril Suk were the defending champions.  Damm partnered with Jared Palmer, losing in the first round.  Suk partnered with Pavel Vízner, losing in the quarterfinals.

2001 Generali Open – Doubles: Pablo Albano and Cyril Suk were the defending champions but they competed with different partners that year, Albano with Lucas Arnold and Suk with Marius Barnard.

Vania King: Vania King (; born February 3, 1989) is an American tennis player.  King won both the 2010 Wimbledon and 2010 US Open women's doubles titles with Kazakhstani partner Yaroslava Shvedova.

1996 Italian Open – Men's Doubles: Cyril Suk and Daniel Vacek were the defending champions but they competed with different partners that year, Suk with Hendrik Jan Davids and Vacek with Richey Reneberg.

2006 Ordina Open – Men's Doubles: Cyril Suk and Pavel Vízner were the defending champions, but did not play together this year.  Suk partnered Robin Vik, losing in the first round.  Vízner partnered Lukáš Dlouhý, losing in the semifinals.

1996 Davidoff Swiss Indoors – Doubles: Cyril Suk and Daniel Vacek were the defending champions but they competed with different partners that year, Suk with Petr Korda and Vacek with Yevgeny Kafelnikov.

1999 US Open – Men's Doubles: Sandon Stolle and Cyril Suk were the defending champions, but Stolle competed with Wayne Black, while Suk competed with Donald Johnson this year.  Suk and Johnson were defeated by Stolle and Black in the third round, while Stolle and Black were defeated by Andrei Olhovskiy and David Prinosil in the quarterfinals.

1993 Volvo International – Doubles: The 1993 Volvo International was a tennis tournament played on outdoor hard courts at the Cullman-Heyman Tennis Center in New Haven, Connecticut, United States and was part of the Championship Series of the 1993 ATP Tour.  The tournament ran from August 16 through August 23, 1993.  Kelly Jones and Rick Leach were the defending champions but only Jones competed that year with Paul Annacone.  Annacone and Jones lost in the semifinals to Cyril Suk and Daniel Vacek.  Suk and Vacek won in the final 7–5, 6–4 against Steve DeVries and David Macpherson.

Cyril Suk: Cyril Suk III (born 29 January 1967) is a former professional tennis player.  A doubles specialist, Suk won one Grand Slam men's doubles title and four Grand Slam mixed doubles titles during his career.

Question: Vania King and Cyril Suk III both specialize in what type of Tennis play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_specialists": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string"
          },
          "specialization": {
            "type": "string"
          }
        },
        "required": [
          "player_name",
          "specialization"
        ],
        "additionalProperties": false
      }
    },
    "common_specialization_type": {
      "type": "string",
      "description": "The type of tennis play that both players specialize in."
    },
    "number_of_specialists_found": {
      "type": "integer",
      "description": "The count of players identified with a specialization."
    }
  },
  "required": [
    "player_specialists",
    "common_specialization_type",
    "number_of_specialists_found"
  ],
  "additionalProperties": false
}
