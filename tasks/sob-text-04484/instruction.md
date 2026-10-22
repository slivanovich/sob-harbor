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
Atlantic Sun Conference: The Atlantic Sun Conference, branded as the ASUN Conference, is a collegiate athletic conference operating mostly in the Southeastern United States.  The league participates at the NCAA Division I level, and does not sponsor football.  Originally established as the Trans America Athletic Conference (TAAC) in 1978, its headquarters are located in Macon, Georgia.

2016–17 Lipscomb Bisons women's basketball team: The 2016–17 Lipscomb Bisons women's basketball team will represent Lipscomb University in the 2016–17 NCAA Division I women's basketball season.  The Bisons, led by fifth year head coach Greg Brown, played their home games at Allen Arena and are members of the Atlantic Sun Conference.  They finished the season 6–24, 3–11 in A-Sun play to finish in a tie for sixth place.  They lost in the quarterfinals of A-Sun Tournament to Jacksonville.

2012–13 Lipscomb Bisons men's basketball team: The 2012–13 Lipscomb Bisons men's basketball team represented Lipscomb University during the 2012–13 NCAA Division I men's basketball season.  The Bisons, led by 14th year head coach Scott Sanderson, played their home games at Allen Arena and were members of the Atlantic Sun Conference.  They finished the season 12–18, 7–11 in A-Sun play to finish in ninth place.  They lost in the quarterfinals of the Atlantic Sun Basketball Tournament to Mercer.

2015–16 Lipscomb Bisons men's basketball team: The 2015–16 Lipscomb Bisons men's basketball team represented Lipscomb University during the 2015–16 NCAA Division I men's basketball season.  The Bisons, led by third year head coach Casey Alexander, played their home games at Allen Arena and were members of the Atlantic Sun Conference.  They finished the season 12–21, 7–7 in A-Sun play to finish in a tie for fifth place.  They defeated Jacksonville in the quarterfinals of the A-Sun Tournament to advance to the semifinals where they lost to Stetson.

Lipscomb Bisons women's basketball: The Lipscomb Bisons women's basketball team is the women's basketball team that represents Lipscomb University in Nashville, Tennessee, United States.  The school's team currently competes in the Atlantic Sun Conference.

2015–16 Lipscomb Bisons women's basketball team: The 2015–16 Lipscomb Bisons women's basketball team will represent Lipscomb University in the 2015–16 NCAA Division I women's basketball season.  The Bisons, led by fourth year head coach Greg Brown, played their home games at Allen Arena and were members of the Atlantic Sun Conference.  They finished the season 5–25, 2–12 in A-Sun play to finish in seventh place.  They lost in the quarterfinals of A-Sun Tournament to Jacksonville.

2016–17 Lipscomb Bisons men's basketball team: The 2016–17 Lipscomb Bisons men's basketball team represented Lipscomb University during the 2016–17 NCAA Division I men's basketball season.  The Bisons, led by fourth-year head coach Casey Alexander, played their home games at Allen Arena in Nashville, Tennessee as members of the Atlantic Sun Conference.  They finished the season 20–13, 11–3 in ASUN play to finish in second place.  As the No. 2 seed in the ASUN Tournament, they defeated NJIT in the quarterfinals to advance to the semifinals where they lost to North Florida.  Despite having 20 wins, they did not participate in a postseason tournament.

2014–15 Lipscomb Bisons women's basketball team: The 2014–15 Lipscomb Bisons women's basketball team will represent Lipscomb University in the 2014–15 NCAA Division I women's basketball season.  The Lady Bisons were coached by third year head coach Greg Brown and were a member of the Atlantic Sun Conference.  They finished the season 8-21, 3-11 in A-Sun play for a seventh-place finish.  They lost in the quarterfinals of the 2015 Atlantic Sun Women's Basketball Tournament to Stetson.

Lipscomb Bisons men's basketball: The Lipscomb Bisons men's basketball team is the men's basketball team that represents Lipscomb University in Nashville, Tennessee, United States.  The school's team currently competes in the Atlantic Sun Conference.  They are coached by Casey Alexander.  The Bisons are yet to make a trip to the NCAA tournament.

2017–18 Lipscomb Bisons men's basketball team: The 2017–18 Lipscomb Bisons men's basketball team will represent Lipscomb University during the 2017–18 NCAA Division I men's basketball season.  The Bisons, led by fifth-year head coach Casey Alexander, will play their home games at Allen Arena in Nashville, Tennessee as members of the Atlantic Sun Conference.

Question: The 2015–16 Lipscomb Bisons women's basketball team were members of a conference that is headquartered where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_season": {
      "type": "string",
      "description": "The season of the basketball team."
    },
    "team_gender": {
      "type": "string",
      "description": "The gender of the basketball team (men's or women's)."
    },
    "conference_name": {
      "type": "string",
      "description": "The name of the athletic conference the team belongs to."
    },
    "conference_headquarters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the conference headquarters is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the conference headquarters is located."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The full location of the conference headquarters."
    }
  },
  "required": [
    "team_season",
    "team_gender",
    "conference_name",
    "conference_headquarters",
    "final_answer"
  ],
  "additionalProperties": false
}
