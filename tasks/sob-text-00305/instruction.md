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
2015–16 Real Oviedo season: The 2015–16 season is the 33rd season in Segunda División played by Real Oviedo, a Spanish football club based in Oviedo, Asturias.  The team promoted last season by winning Segunda División B

1978–79 Segunda División B: The 1978–79 Segunda División B was the 2nd season of Segunda División B, the third highest level of the Spanish football league system, since its establishment in 1977.  First and 2nd in each group were promoted to Segunda División, and the bottom three were relegated to the Tercera División.

Deportivo Rayo Cantabria: Deportivo Rayo Cantabria is a Spanish football team based in Santander, in the autonomous community of Cantabria.  Founded in 1993 it currently plays in Tercera División – Group 3, holding home games at the Campo Municipal Mies de Cozada sports ground, which they share with a Segunda Regional football side (Juventud Atlético San Román) and a División de Honor rugby club (Independiente Rugby Club).  Before they played at the Campos de San Juan de Monte".

1989–90 Segunda División: The 1989–90 Segunda División season saw 20 teams participate in the second flight Spanish league.  Real Burgos, Real Betis and RCD Español were promoted to Primera División.  Racing de Santander, Castilla CF, Recreativo de Huelva and Atlético Madrileño were relegated to Segunda División B.

1999 Segunda División B play-offs: The 1999 Segunda División B play-offs (Playoffs de Ascenso or Promoción de Ascenso) were the final playoffs for promotion from Spanish 1998–99 Segunda División B to the 1999–2000 Segunda División.  The four first placed teams in each of the four Segunda División B groups played the "Playoffs de Ascenso" and the four last placed teams in Segunda División were relegated to Segunda División B.

1977–78 Segunda División B: The 1977–78 Segunda División B was the first season of Segunda División B, the third highest level of the Spanish football league system.  The league was made up of last 4 teams from 1976-77 Segunda División and 2nd to 10th teams from 1976-77 Tercera División.  In concept, the Segunda División B was identical to the old Tercera Division, which was now reduced to two divisions.  First and 2nd in each group were promoted to Segunda División, and the bottom three were relegated to the Tercera División.

Segunda División B: Segunda División B (English: Second Division B ) is the third level of the Spanish football league system.  It is administered by the RFEF.  It is below the top two levels of the league, the "Primera División" (also known as La Liga) and the "Segunda División", and above the "Tercera División".  The Segunda División B includes the reserve teams of several La Liga and Segunda División teams.

Racing de Santander: Real Racing Club de Santander, S.A.D. is a Spanish football club based in Santander, in the autonomous community of Cantabria.  Founded in 1913 it plays in Segunda División B – Group 2, holding home games at "Estadio El Sardinero", with a capacity for 22,222 spectators.

1979–80 Segunda División B: The 1979–80 Segunda División B was the 3rd season of Segunda División B, the third highest level of the Spanish football league system, since its establishment in 1977.  First and 2nd in each group were promoted to Segunda División, and the bottom four were relegated to the Tercera División.

1980–81 Segunda División B: The 1980–81 Segunda División B was the 4th season of Segunda División B, the third highest level of the Spanish football league system, since its establishment in 1977.  First and 2nd in each group were promoted to Segunda División, and the bottom three were relegated to the Tercera División.

Question: What Spanish football club from Cantabria participated in the1989–90 Segunda División?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "club_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "club_location_community": {
      "type": "string",
      "description": "The autonomous community where the club is based."
    },
    "league_season": {
      "type": "string",
      "description": "The specific season of the league."
    },
    "league_name": {
      "type": "string",
      "description": "The name of the football league."
    },
    "season_outcome": {
      "type": "string",
      "description": "The outcome for the club in that specific league season (e.g., promoted, relegated)."
    }
  },
  "required": [
    "club_name",
    "club_location_community",
    "league_season",
    "league_name",
    "season_outcome"
  ],
  "additionalProperties": false
}
