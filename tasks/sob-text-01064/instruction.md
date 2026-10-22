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
2010 Shanghai Rolex Masters – Doubles: Julien Benneteau and Jo-Wilfried Tsonga were the defending champions, but Benneteau chose to not participate due to left wrist injury.

Pete Sampras: Pete Sampras (born August 12, 1971) is a retired American tennis player widely regarded as one of the greatest in the history of the sport.  He was a right-handed player with a single-handed backhand and a precise and powerful serve that earned him the nickname "Pistol Pete".  His professional career began in 1988 and ended at the 2002 US Open, which he won, defeating rival Andre Agassi in the final.

2010 Open Sud de France – Doubles: Julien Benneteau and Nicolas Mahut were the defending champions, however Benneteau was injured (left wrist).

Sampras Tennis 96: Sampras Tennis 96 is a 1995 tennis video game developed by Codemasters.  It is the sequel to "Pete Sampras Tennis".  Like its predecessor, it was one of the few titles released on the J-Cart format, which provided two additional controller ports for multiplayer games.  The game was followed by "Pete Sampras Tennis '97", which was released for the PlayStation and personal computers.

Julien Benneteau: Julien Benneteau (] ; born 20 December 1981) is a French professional tennis player.  His career-high singles ranking is ATP world no. 25, which he reached in November 2014.  He formerly resided in Boulogne-Billancourt and now lives in Geneva.  Benneteau is generally regarded as one of the best singles players on the tour who has not won a title, finishing as runner-up in ten ATP tournaments.  He reached the quarterfinals of the 2006 French Open and the semifinals of the 2014 Cincinnati Masters.

2015 Open 13 – Doubles: Julien Benneteau and Édouard Roger-Vasselin were the defending champions, but did not participate due to Benneteau's injury.

2014 Monte-Carlo Rolex Masters – Doubles: Julien Benneteau and Nenad Zimonjić were the defending champions, but decided not to participate together.  Benneteau played alongside Édouard Roger-Vasselin, but lost to Bob and Mike Bryan in the quarterfinals.  Zimonjić teamed up with Daniel Nestor, but lost to the Bryan brothers in the semifinals.  The Bryans became the new champions, defeating Ivan Dodig and Marcelo Melo 6–3, 3–6, [10–8] in the final.

Pete Sampras Tennis '97: Pete Sampras Tennis '97 is a tennis video game developed and published by Codemasters.  It was released for Microsoft Windows and MS-DOS.  It was also released for the PlayStation as Sampras Extreme Tennis.  It was endorsed by multiple Grand Slam champion Pete Sampras who appears in the game as an unlockable character.  It is the final game in the Pete Sampras Tennis series.

Pete Sampras Tennis: Pete Sampras Tennis was the first game of three of this celebrity-endorsed tennis video game series, released by British software house Codemasters.  It was followed by "Sampras Tennis 96" still on Sega's 16-bit console and later by "Pete Sampras Tennis '97", released for the PlayStation and Windows/DOS.

2011 Winston-Salem Open – Singles: Sergiy Stakhovsky was the defending champion, but lost to Julien Benneteau in the quarterfinals.  John Isner defeated Benneteau in the final, 4–6, 6–3, 6–4.

Question: Julien Benneteau and Pete Sampras, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_names": {
      "type": "array",
      "description": "The names of the individuals for whom a mutual occupation is sought.",
      "items": {
        "type": "string"
      }
    },
    "mutual_occupation_found": {
      "type": "boolean",
      "description": "Indicates whether a mutual occupation was found for the specified individuals."
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The identified mutual occupation between the individuals."
    },
    "individual_occupations": {
      "type": "array",
      "description": "A list of each person's occupation(s) as stated in the context.",
      "items": {
        "type": "object",
        "properties": {
          "person_name": {
            "type": "string",
            "description": "The name of the person."
          },
          "occupations": {
            "type": "array",
            "description": "A list of occupations for the person.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "person_name",
          "occupations"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "person_names",
    "mutual_occupation_found",
    "mutual_occupation",
    "individual_occupations"
  ],
  "additionalProperties": false
}
