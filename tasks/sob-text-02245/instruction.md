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
Carlos Hasselbaink: Carlos Hasselbaink (born December 13, 1968 in Paramaribo, Suriname) is a former Dutch football (soccer) player.  He played as a striker for several Dutch clubs, including AZ Alkmaar, Telstar, VVV-Venlo, FC Utrecht and HFC Haarlem, before retiring in 2005.  He is the older brother of former Chelsea and Middlesbrough striker Jimmy Floyd Hasselbaink.

Jimmy Floyd Hasselbaink: Jerrel "Jimmy" Floyd Hasselbaink (born 27 March 1972) is a Dutch former professional footballer and current manager of EFL League One club Northampton Town.

Robert Verbeek: Robert Verbeek (born 26 July 1961) is a Dutch former soccer player and subsequently a manager.  Verbeek is the younger brother of former Australia manager Pim Verbeek.  As a player, he featured for Sparta Rotterdam, where he retired at the age of 31.

Ronald Koeman: Ronald Koeman (] ; born 21 March 1963) is a former Dutch footballer and the current manager of English club Everton.  He is the younger brother of former Feyenoord coach Erwin Koeman and the son of former Dutch international Martin Koeman.  A composed player on the ball, Koeman was capable of being deployed both as a defender and as a midfielder, and he frequently played as a sweeper, due to his vision and his ability on the ball.  Regarded as one of the best and most prolific attacking central defenders of all time, Koeman was renowned for his long-range passing, as well as his shooting accuracy and power from distance, especially on free kicks, and is the top scoring defender in world football; he was also an accurate penalty kick taker.

Garry Thompson (footballer, born 1959): Garry Thompson (born 7 October 1959) is an English former professional footballer and football manager, who played as a striker.  His younger brother, Keith Thompson, was also a professional footballer.

Ferruccio Mazzola: Ferruccio Mazzola (1 February 1945 – 7 May 2013) was an Italian former professional footballer and manager, who played as a midfielder.  He was the son of former footballer Valentino Mazzola, and the younger brother of retired footballer Sandro Mazzola.

Mike Ford (footballer): Michael Paul "Mike" Ford (born 9 February 1966) is an English former professional footballer and current manager of Banbury United.  His father, Tony Ford, was also a professional footballer.

Rick Kruys: Rick Kruijs, commonly known as Rick Kruys, (born 9 May 1985 in Utrecht) is a Dutch former professional footballer who played as a midfielder.  His father, Gert Kruys, was a former professional football player as well, currently working as a manager in Dutch football.

Carlos Fabián Leeb: Carlos Fabián "cat" Leeb (born July 18, 1968, in Buenos Aires) is a former Argentine football striker and the current manager for Bolivian first division club Sport Boys Warnes.  Carlos is the son of Luis Félix "cat" Leeb, a professional footballer who played over 300 games in Argentine football.

Michel Vonk: Michel Vonk (born 28 October 1968) is a Dutch former professional footballer and the current manager of Eerste Divisie side Telstar.

Question: What is the birthdate of this Dutch former professional footballer and current manager, who is the younger brother of Carlos Hasselbaink?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person identified."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the person."
    },
    "birth_date": {
      "type": "string",
      "description": "The birthdate of the person in 'Day Month Year' format."
    },
    "current_role": {
      "type": "string",
      "description": "The current professional role of the person."
    },
    "former_role": {
      "type": "string",
      "description": "The former professional role of the person."
    },
    "sibling_relationship": {
      "type": "object",
      "properties": {
        "sibling_name": {
          "type": "string",
          "description": "The name of the sibling mentioned in the context."
        },
        "relationship_type": {
          "type": "string",
          "description": "Describes the relationship of the identified person to their sibling (e.g., 'younger brother')."
        }
      },
      "required": [
        "sibling_name",
        "relationship_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "nationality",
    "birth_date",
    "current_role",
    "former_role",
    "sibling_relationship"
  ],
  "additionalProperties": false
}
