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
Finn Laudrup: Finn Laudrup (born 31 July 1945) is a Danish former association football player who played as a forward.  He represented a number of Danish clubs and played professionally with Wiener Sport-Club in Austria.  He played 19 matches and scored six goals for the Denmark national football team.  He is the father of former Denmark national team players Michael Laudrup and Brian Laudrup.

Michael Manniche: Michael Manniche (born 17 July 1959) is a retired Danish footballer who played as a centre forward.

Mark Strudal: Mark Agner Boecking Strudal (born 29 April 1968 in Glostrup) is a retired Danish footballer who played as a striker and scored three goals in nine games for the Danish national team.  He became known for his extravagant lifestyle, but in later years he reentered the minds of the Danish public as the manager of FC Zulu.

Kurt Stendal: Kurt Stendal (born 19 February 1951) is a retired Danish footballer who played as a midfielder.  He was born in Frederiksberg.

Kasper Bøgelund: Kasper Bøgelund Nielsen (born 8 October 1980 in Odense) is a retired Danish footballer.  He last played as a right back for AaB in the Danish Superliga.  Bøgelund has played 17 games for the Danish national team, and he represented Denmark at the 2002 FIFA World Cup and 2004 European Championship.

Brian Laudrup: Brian Laudrup (born 22 February 1969) is a retired Danish footballer who played as a forward or as a midfielder.  He currently works as a football commentator, pundit and analyst on Kanal 5 and 6'eren.  Along with former international goalkeeper Lars Høgh, Laudrup manages a football academy for marginalised youth.

Jeppe Curth: Jeppe Lund Curth (born 21 March 1984) is a retired Danish footballer.  He has played 43 matches and scored 15 goals for various Danish youth national teams, most recently the Danish national under-21 team.

Stefan Bidstrup: Stefan Bidstrup (born 24 February 1975) is a retired Danish footballer who played as a midfielder.

Mariann Gajhede Knudsen: Mariann Gajhede Knudsen (born 16 November 1984) is a retired Danish footballer who last played as a central midfielder for Linköpings FC of Sweden's Damallsvenskan.  She won over 100 caps for the Danish national team, before announcing her retirement from international football in November 2014 and making a brief comeback the following year.  She was named Danish Player of the Year in 2008.  In 2017, she joined the Norwegian national team as fitness coach and physiotherapist to the team.

Emil Larsen: Emil Larsen (born 22 June 1991 in Copenhagen) is a retired Danish footballer.  He most recently played for Lyngby BK in the Danish Superliga, and has played for various Danish national youth teams.

Question: Who was the brother of a retired Danish footballer who played as a forward or as a midfielder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_brother_name": {
      "type": "string",
      "description": "The name of the person identified as the brother."
    },
    "sibling_who_matches_description": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the sibling who matches the description."
        },
        "is_retired": {
          "type": "boolean",
          "description": "Indicates if the sibling is a retired footballer."
        },
        "positions_played": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The positions played by the sibling."
        }
      },
      "required": [
        "name",
        "is_retired",
        "positions_played"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "The type of relationship between the identified person and the sibling."
    }
  },
  "required": [
    "identified_brother_name",
    "sibling_who_matches_description",
    "relationship_type"
  ],
  "additionalProperties": false
}
