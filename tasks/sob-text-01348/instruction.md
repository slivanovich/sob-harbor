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
Sonia Prim: Sonia Prim Fernández (born 5 November 1984) is a Spanish football defender who is the captain of Primera División club Levante UD.  She previously played for CF Pozuelo and Atlético Madrid.

Alexandra López: Alexandra López Rosillo (born 26 February 1989), commonly known as Ale, is a Spanish football defender who plays for Atlético Madrid in Spain's Primera División.  She previously played for Sevilla FC.

Sonia Bermúdez: Sonia Bermúdez Tribano (born 18 November 1984 in Vallecas, Madrid), commonly known as Sonia or Soni, is a Spanish footballer who plays as a forward for Primera División club Atlético Madrid and the Spain women's national football team.  With previous passages for Rayo Vallecano, FC Barcelona and NWSL club Western New York Flash, she won the women's Primera División seven consecutive times (three with Rayo Vallecano and four with Barcelona) from 2008–09 until 2014–15.

Georgina Carreras: Georgina Carreras Caner (born 9 June 1989), commonly known as Gio, is a Spanish football midfielder who plays for Valencia CF of Spain's Primera División.  She previously played for UE L'Estartit, Atlético Madrid and CE Sant Gabriel.

Claudia Barea: Claudia Barea Moreno (born 19 January 1994), commonly known as Congui, is a Spanish football midfielder who plays for Sporting Plaza de Argel of the Segunda División.  She previously played for Primera División clubs Valencia CF and Sevilla FC.  In summer 2013 she joined Sporting Plaza de Argel.

Esther González: Esther González Rodríguez (born 8 December 1992) is a Spanish football striker who plays for Atlético Madrid of Spain's Primera División and the Spain Spain national team.  At club level she previously played for Levante UD, Atlético Málaga, and Sporting Huelva.

Cristina Pizarro: Cristina Pizarro Mingo, also known as Chini, is a Spanish football defender, currently playing for Real Sociedad in Spain's Primera División.  She previously played for Atlético Madrid and Rayo Vallecano.

Sevilla FC: Sevilla Fútbol Club, S.A.D. (] ), or simply Sevilla, is Spain’s oldest sporting club solely devoted to football.  Sevilla FC is based in Seville, capital and largest city of the autonomous community of Andalusia.  Sevilla FC is one of the teams that play in Spain’s top flight, La Liga.  The club was formed on 25 January 1890, Scot Mr. Edward Farquharson Johnston being their first president.  A few years later, on October 14, 1905, the club’s articles of association were registered in the Civil Government of Seville under the presidency of the Jerez-born José Luis Gallegos Arnosa.

Marta Carro: Marta Carro Nolasco is a Spanish football defender who plays for AGSM Verona in Italy's women's Serie A.  She previously played in Spain's women Primera División for Atlético Madrid.

Sandra García: Sandra García Giraldez is a Spanish football defender, currently playing for Sporting Huelva in Spain's Primera División.  She previously played for Estudiantes Huelva, Sevilla FC.  and Sporting Plaza de Argel.

Question: Alexandra López Rosillo, commonly known as Ale, is a Spanish football defender who plays for Atlético Madrid in Spain's Primera División, and previously played for Sevilla FC, which country's oldest sporting club solely devoted to football?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "club_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the football club."
        },
        "country": {
          "type": "string",
          "description": "The country where the club is based."
        },
        "is_oldest_football_club_in_country": {
          "type": "boolean",
          "description": "Indicates if the club is the oldest sporting club solely devoted to football in its country."
        },
        "league": {
          "type": "string",
          "description": "The name of the top-flight league the club plays in."
        }
      },
      "required": [
        "name",
        "country",
        "is_oldest_football_club_in_country",
        "league"
      ],
      "additionalProperties": false
    },
    "player_details": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the player mentioned in the question."
        },
        "common_name": {
          "type": "string",
          "description": "The commonly known name of the player."
        },
        "previous_club_name": {
          "type": "string",
          "description": "The name of the player's previous club relevant to the question."
        }
      },
      "required": [
        "full_name",
        "common_name",
        "previous_club_name"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The country that is the answer to the question."
    }
  },
  "required": [
    "club_details",
    "player_details",
    "answer"
  ],
  "additionalProperties": false
}
