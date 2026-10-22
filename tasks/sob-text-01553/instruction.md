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
Pichichi Trophy: In Spanish football, the Trofeo Pichichi is awarded by the sports newspaper "Marca" to the top goalscorer of each La Liga season.  Named after the Athletic Bilbao striker Rafael "Pichichi" Moreno, the trophy has been awarded annually since the 1952–53 season.  All top scorers who preceded the award's creation were retroactively named Pichichi winners by "Marca".

Récord: Récord is a Mexican daily sports newspaper.  It follows a similar format as the Spanish newspaper Marca.  Récord is owned by Notmusa.

Diario Las Américas: Diario las Américas is the oldest Spanish newspaper in Miami for the Hispanic community.  The newspaper was founded by Nicaraguan born Horacio Aguirre Baca.  The newspaper has been an active member of the Inter-American Press Association (IAPA) since its founding.

Miguel Muñoz Trophy: The Miguel Muñoz Trophy (Spanish: "Trofeo Miguel Muñoz" ) is a football award established by Spanish newspaper MARCA for the 2005–06 season, in memory of the legendary Real Madrid manager Miguel Muñoz.

AEDE: The Spanish Newspaper Publishers' Association (Spanish: "Asociación de Editores de Diarios Españoles" ; AEDE) is a trade association for Spanish newspaper publishers based in Madrid, Spain.

Juan Alonso: Juan Adelarpe Alonso (13 December 1927 – 8 September 1994), sometimes called Juanito Alonso, was a Spanish footballer who played for Real Madrid and was part of their European Cup victories in 1956, 1957 and 1958.  He earned 2 caps for the Spain national football team.  Alonso won the Ricardo Zamora Trophy in the season 1954–55.

Ricardo Zamora Trophy: The Zamora Trophy (Spanish: "Trofeo Ricardo Zamora" ) is a football award, established by Spanish newspaper "MARCA" in 1958.  The award goes to the goalkeeper who has the lowest "goals-to-games" ratio.

Marca Leyenda: Marca Leyenda (Marca legend) is an award given by the Spanish sports newspaper Marca to the best sport professionals in history.  Since its inception in 1997 over 40 people have received this award.

Eduardo Lago: Eduardo Lago (born 31 January 1954) is a Spanish novelist, translator, and literary critic, born in Madrid and currently living in Manhattan, New York, United States.  In 2002, he was the recipient of the Bartolomé March Award for Excellence in Literary Criticism for his critical comparison of three Spanish translations of James Joyce’s novel, "Ulysses".  In 2006, he won the Premio Nadal, Spain's oldest and most prestigious literary award, for his first novel, "Llámame Brooklyn" ("Call Me Brooklyn").  For many years, he interviewed North American writers for the literary supplement "Babelia" in the Spanish newspaper "El País".  He returned to teaching Spanish, Spanish literature, and European Literature at Sarah Lawrence College in Yonkers in 2011, after leaving in 2005 for the position of Director of the Cervantes Institute in New York.

José Ortega Spottorno: José Ortega Spottorno (November 13, 1916 – February 18, 2002) was a Spanish journalist and publisher.  Born in Madrid to famous philosopher José Ortega y Gasset and Rosa Spottorno Topete, José Ortega Spottorno was the founder of affordable paperback publishing firm Alianza Editorial and the Spanish daily newspaper "El País", which quickly became the bestselling Spanish newspaper, a crown it holds to this day.  He was survived by his wife, Simone Ortega, and three children, one of whom works as a journalist for "El País".

Question: For which team did the winner of an award established by Spanish newspaper "MARCA" play?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award established by the Spanish newspaper."
        },
        "establishing_newspaper": {
          "type": "string",
          "description": "The name of the Spanish newspaper that established the award."
        },
        "establishment_year": {
          "type": "integer",
          "description": "The year the award was established."
        }
      },
      "required": [
        "award_name",
        "establishing_newspaper",
        "establishment_year"
      ],
      "additionalProperties": false
    },
    "award_winner_details": {
      "type": "object",
      "properties": {
        "winner_name": {
          "type": "string",
          "description": "The name of the player who won the award."
        },
        "winning_season": {
          "type": "string",
          "description": "The season in which the player won the award."
        },
        "team_played_for": {
          "type": "string",
          "description": "The team the winner played for."
        }
      },
      "required": [
        "winner_name",
        "winning_season",
        "team_played_for"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the team for which the award winner played."
    }
  },
  "required": [
    "award_details",
    "award_winner_details",
    "final_answer"
  ],
  "additionalProperties": false
}
