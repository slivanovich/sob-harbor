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
Oscar Hiljemark: Oscar Carl Niclas Hiljemark (] ; born 28 June 1992) is a Swedish footballer who plays as a midfielder for Greek club Panathinaikos on loan from Genoa.

Víctor Sánchez: Víctor Sánchez del Amo (born 23 February 1976), known simply as Víctor, is a Spanish retired footballer who played as a right midfielder, and a current manager.

Igor Bišćan: Igor Bišćan (; born 4 May 1978) is a Croatian former professional footballer and manager who currently manages Slovenian PrvaLiga club Olimpija Ljubljana.  In his playing career, he was a versatile player and could play almost every position in the defence or midfield, but featured mostly as a central midfielder, or as a central defender in his latter years.

2007–08 Panathinaikos F.C. season: In the 2007–08 season Panathinaikos played for 49th consecutive time in Greece's top division, Super League.  They also competed in UEFA CUP and Greek Cup.  Season started with José Peseiro as team manager.  In summer of 2007 many players left the club including Igor Bišćan and Víctor Sánchez who hadn't fulfilled the expectations of Panathinaikos' fans with their performance.  On the other end the return of Giorgos Karagounis after four years pulled the spotlight and considered one of the most important signings of the 2007 summer transfer window.  Panathinaikos also signed Brazilian midfielder Marcelo Mattos from Corinthians, Dame N'Doye from Academica, Josu Sarriegi from Athletic Bilbao and some other players to help the team win its first championship in four years and celebrate the club's centesimal anniversary in the most appropriate way.

Nuno Reis: Nuno Miguel Pereira Reis (born 31 January 1991) is a Portuguese professional footballer who plays for Greek club Panathinaikos F.C. as a central defender.

Antonio Méndez: Antonio Méndez Méndez (born 7 February 1970) is a Spanish retired footballer who played mainly as a right midfielder, who lastly was the manager of San Fernando CD.

Claus Nielsen: Claus Illemann Nielsen (born 13 January 1964), known as Claus Nielsen, is a Danish former association football player in the striker position.  He spent the bulk of his career with Brøndby IF, but also played for the Greek club Panathinaikos and the Dutch club FC Twente.

Andrés Chávez: Andrés Eliseo Chávez (born 21 March 1991) is an Argentine professional footballer who plays as a forward for Greek club Panathinaikos.

Ioannis Samaras: Ioannis Samaras (Greek: Ἰωάννης Σαμαράς ) (born 3 May 1961) is an Australian-born Greek former footballer who played as a midfielder during the 1980s and 1990s and currently works as youth academy technical director and general manager at Greek club Panathinaikos.

Krzysztof Warzycha: Krzysztof "Kristof" Warzycha (; Greek: Κριστόφ Βαζέχα ; born November 17, 1964 in Katowice) is a former Polish professional footballer.  For the majority of his career he played for Greek club Panathinaikos.

Question: Which Spanish retired footballer who played as a right midfielder and is currently a manager, left the Greek club Panathinaikos in the summer of 2007 alongside Igor Bišćan and many others?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "footballer_name": {
      "type": "string",
      "description": "The full name of the footballer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the footballer."
    },
    "playing_position": {
      "type": "string",
      "description": "The primary playing position of the footballer."
    },
    "current_role": {
      "type": "string",
      "description": "The current role of the individual (e.g., manager, retired footballer)."
    },
    "club_departed_from": {
      "type": "string",
      "description": "The name of the club the footballer left."
    },
    "departure_year": {
      "type": "integer",
      "description": "The year the footballer departed from the club."
    },
    "departed_with_notable_players": {
      "type": "boolean",
      "description": "Indicates if the footballer left the club alongside other specifically mentioned players."
    },
    "other_departing_players": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of other players who left the club at the same time."
    }
  },
  "required": [
    "footballer_name",
    "nationality",
    "playing_position",
    "current_role",
    "club_departed_from",
    "departure_year",
    "departed_with_notable_players",
    "other_departing_players"
  ],
  "additionalProperties": false
}
