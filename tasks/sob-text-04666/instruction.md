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
1989 Paris Open – Doubles: Paul Annacone and John Fitzgerald were the defending champions but they competed with different partners that year, Annacone with Christo van Rensburg and Fitzgerald with Anders Järryd.

2005 Challenge Bell – Doubles: Carly Gullickson and María Emilia Salerni were the defending champions, but Gullickson decided not to participate this year.  Salerni partnered with Marion Bartoli, but withdrew from their semifinal match against Līga Dekmeijere and Ashley Harkleroad.

2010 US Open – Mixed Doubles: Carly Gullickson and Travis Parrott were the defending champions, but lost in the first round to Gisela Dulko and Pablo Cuevas 2–6, 4–6.

Carly Gullickson: Carly Gullickson (born November 26, 1986) is a former American professional tennis player.

2010 Australian Open – Mixed Doubles: Sania Mirza and Mahesh Bhupathi were the defending champions.  They accepted the invitation for the tournament, but withdrew before their match against Carly Gullickson and Bernard Tomic and were replaced by Akgul Amanmuradova and Rik de Voest.

1990 Volvo U.S. National Indoor – Doubles: Paul Annacone and Christo van Rensburg were the defending champions.  Annacone competed alongside Kelly Evernden but lost in the semifinals, while van Rensburg played with Kevin Curren and lost in the quarterfinals. <br>Darren Cahill and Mark Kratzmann won the title, defeating Udo Riglewski and Michael Stich 7–5, 6–2, in the final.

2009 Hansol Korea Open – Doubles: Chuang Chia-jung and Hsieh Su-wei were the defending champion, but Hsieh chose not to participate that year.  Chuang partnered with Yan Zi, but they lost in the semifinals against Chan Yung-jan and Abigail Spears. Chan Yung-jan and Abigail Spears won in the final 6–3, 6–4 against Carly Gullickson and Nicole Kriz.

Paul Annacone: Paul Annacone (born March 20, 1963) is an American former touring professional tennis player and current tennis coach.  He is the former coach of open-era leader in Grand Slams Roger Federer and former World No. 1 Pete Sampras.  Annacone is currently a coach at ProTennisCoach.com and a commentator at Tennis Channel

1993 Volvo International – Doubles: The 1993 Volvo International was a tennis tournament played on outdoor hard courts at the Cullman-Heyman Tennis Center in New Haven, Connecticut, United States and was part of the Championship Series of the 1993 ATP Tour.  The tournament ran from August 16 through August 23, 1993.  Kelly Jones and Rick Leach were the defending champions but only Jones competed that year with Paul Annacone.  Annacone and Jones lost in the semifinals to Cyril Suk and Daniel Vacek.  Suk and Vacek won in the final 7–5, 6–4 against Steve DeVries and David Macpherson.

1990 Ebel U.S. Pro Indoor – Doubles: Paul Annacone and Christo van Rensburg were the defending champions.  Annacone participated with John Fitzgerald, and lost in the quarterfinals to Scott Davis and David Pate, while Van Rensburg played with Kevin Curren, and lost in the semifinals to Grant Connell and Glenn Michibata. <br>Rick Leach and Jim Pugh defeated Connell and Michibata 3–6, 6–4, 6–2, in the final.

Question: Who was born first, Paul Annacone or Carly Gullickson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "player_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        },
        "birth_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "born_first_player_name": {
      "type": "string"
    },
    "comparison_statement": {
      "type": "string"
    }
  },
  "required": [
    "player_one",
    "player_two",
    "born_first_player_name",
    "comparison_statement"
  ],
  "additionalProperties": false
}
