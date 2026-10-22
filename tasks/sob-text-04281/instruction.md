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
2002 French Open – Mixed Doubles: Virginia Ruano Pascual and Tomás Carbonell were the defending champions, but had different outcomes.  Ruano Pascual teamed up with Gastón Etlis and lost in second round to Cara and Wayne Black, while Carbonell did not compete this year due to retiring from professional tennis in 2001.

2000 Estoril Open – Men's Doubles: Tomás Carbonell and Donald Johnson were the defending champions, but did not participate together this year.  Carbonell partnered Juan Balcells, losing in the first round.  Johnson partnered Piet Norval and successfully defended his title.

Elizabeth Smylie: Elizabeth Smylie (née Sayers, born 11 April 1963), sometimes known as Liz Smylie, is a retired Australian professional tennis player.  During her career, she won four Grand Slam titles, one of them in women's doubles and three in mixed doubles.  She also won three singles titles and 36 doubles titles.

2000 Majorca Open – Doubles: Lucas Arnold and Tomás Carbonell were the defending champions, but did not participate together this year.  Arnold partnered Martín García, losing in the first round.  Carbonell partnered Piet Norval, losing in the first round.

1991 US Open – Mixed Doubles: Elizabeth Smylie and Todd Woodbridge were the defending champions but they competed with different partners that year, Smylie with John Fitzgerald and Woodbridge with Nicole Provis.

1986 Wimbledon Championships – Women's Doubles: Kathy Jordan and Elizabeth Smylie were the defending champions but they competed with different partners that year, Jordan with Alycia Moulton and Smylie with Catherine Tanvier.

1989 Pilkington Glass Championships – Doubles: Eva Pfaff and Elizabeth Smylie were the defending champions but they competed with different partners that year, Pfaff with Manon Bollegraf and Smylie with Wendy Turnbull.

1988 New South Wales Open – Women's Doubles: Betsy Nagelsen and Elizabeth Smylie were the defending champions but they competed with different partners that year, Nagelsen with Lori McNeil and Smylie with Jana Novotná.

Tomás Carbonell: Tomás Carbonell Lladó (born 7 August 1968) is a former professional tennis player from Spain.

1994 ATP Buenos Aires – Doubles: Tomás Carbonell and Carlos Costa were the defending champions, but did not participate together this year.  Carbonell partnered Francisco Roig, losing in the final.  Costa partnered Christian Miniussi, losing in the first round.

Question: Elizabeth Smylie and Tomás Carbonell, share which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the individuals sharing the mutual occupation."
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The occupation shared by both individuals."
    },
    "all_are_retired_or_former": {
      "type": "boolean",
      "description": "Indicates if all listed individuals are described as retired or former in their occupation."
    }
  },
  "required": [
    "person_names",
    "mutual_occupation",
    "all_are_retired_or_former"
  ],
  "additionalProperties": false
}
