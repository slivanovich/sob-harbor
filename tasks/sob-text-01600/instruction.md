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
2016 San Diego State Aztecs football team: The 2016 San Diego State Aztecs football team represented San Diego State University in the 2016 NCAA Division I FBS football season.  The Aztecs were led by sixth-year head coach Rocky Long and played their home games at Qualcomm Stadium.  They were members of the West Division of the Mountain West Conference.  They finished the season 11–3, 6–2 in Mountain West play to be champions of the West Division.  They represented the West Division in the Mountain West Championship Game where they defeated Wyoming to be crowned Mountain West champions for the second consecutive year.  They were invited to the Las Vegas Bowl where they defeated Houston.

1998 San Diego State Aztecs football team: The 1998 San Diego State Aztecs football team represented San Diego State University during the 1998 NCAA Division I-A football season as a member of the Western Athletic Conference (WAC).  This was the last season for the Aztecs in the WAC, as they became a charter member of the Mountain West Conference in the 1999 season.

2001 San Diego State Aztecs football team: The 2001 San Diego State Aztecs football team represented San Diego State University in the 2001 NCAA Division I-A football season.  The Aztecs, led by head coach Ted Tollner, who was fired after the season, and they played their home games at the Qualcomm Stadium.

1999 San Diego State Aztecs football team: The 1999 San Diego State Aztecs football team represented San Diego State University in the 1999 NCAA Division I-A football season.  The Aztecs, led by head coach Ted Tollner and they played their home games at the Qualcomm Stadium.

1984 USC Trojans football team: The 1984 USC Trojans football team represented the University of Southern California (USC) in the 1984 NCAA Division I-A football season.  In their second year under head coach Ted Tollner, the Trojans compiled a 9–3 record (7–1 against conference opponents), won the Pacific-10 Conference (Pac-10) championship, and outscored their opponents 220 to 173.

1983 USC Trojans football team: The 1983 USC Trojans football team represented the University of Southern California (USC) in the 1983 NCAA Division I-A football season.  In their first year under head coach Ted Tollner, the Trojans compiled a 4–6–1 record (5–2 against conference opponents), finished in fourth place in the Pacific-10 Conference (Pac-10), and were outscored by their opponents by a combined total of 238 to 210.

2000 San Diego State Aztecs football team: The 2000 San Diego State Aztecs football team represented San Diego State University in the 2000 NCAA Division I-A football season.  They were coached by Ted Tollner and played their home games at Qualcomm Stadium.

2008 San Diego State Aztecs football team: The 2008 San Diego State Aztecs football team represented San Diego State University in the 2008 NCAA Division I FBS football season.  They were coached by Chuck Long and played their home games at Qualcomm Stadium.  The 2008 season was expected to be rough for the Aztecs after losing several key offensive players to the National Football League (NFL).  The team looked to redshirt freshman quarterback Ryan Lindley to replace star quarterback Kevin O'Connell.  The team also lost two of its leading wide receivers in Brett Swain and Chaz Schilens along with four starting offensive linemen.

1986 USC Trojans football team: The 1986 USC Trojans football team represented the University of Southern California (USC) in the 1986 NCAA Division I-A football season.  In their fourth and final year under head coach Ted Tollner, the Trojans compiled a 7–5 record (5–3 against conference opponents), finished in a three-way tie for fourth place in the Pacific-10 Conference (Pac-10), and outscored their opponents by a combined total of 264 to 239.

San Diego State University: San Diego State University (SDSU, San Diego State) is a public research university in San Diego, California, and is the largest and oldest higher education institution in San Diego County.  Founded in 1897 as San Diego Normal School, it is the third-oldest university in the 23-member California State University (CSU).  SDSU has a Fall 2016 student body of 34,688 and an alumni base of more than 280,000.

Question: the 1999 Aztecs football team lead by Ted Tollner represented a public research university founded in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_year": {
      "type": "integer",
      "description": "The year of the football team."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the football team."
    },
    "head_coach": {
      "type": "string",
      "description": "The head coach of the team."
    },
    "university": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the university was founded."
        },
        "type": {
          "type": "string",
          "description": "The type of university (e.g., public research)."
        }
      },
      "required": [
        "name",
        "founding_year",
        "type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "team_year",
    "team_name",
    "head_coach",
    "university"
  ],
  "additionalProperties": false
}
