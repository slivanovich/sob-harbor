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
2004 Hawaii Warriors football team: The 2004 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2004 NCAA Division I-A football season.  Hawaii finished the 2004 season with an 8–5 record, going 4–4 in Western Athletic Conference (WAC) play.  The Warriors made their third straight appearance in the Hawaii Bowl, facing off against the UAB Blazers.  The Warriors would go on to defeat the Blazers and cap off their third straight winning season, the fifth in six seasons under head coach June Jones.

2010 Hawaii Warriors football team: The 2010 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2010 college football season.  The Warriors, led by third-year head coach Greg McMackin, were members of the Western Athletic Conference (WAC) and played their home games at Aloha Stadium in Honolulu, Hawaii.  They finished the season 10–4, 7–1 in WAC play to claim a share of the WAC championship with Boise State and Nevada.  They were invited to the Hawaii Bowl where they were defeated by Tulsa, 62–35.

2006 Hawaii Warriors football team: The 2006 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2006 NCAA Division I-Bowl Subdivision college football season.  The Warriors tied the school record for most victories in a season with 11, with their only losses coming against the University of Alabama in Tuscaloosa, an undefeated Boise State team that would go on to participate in the Bowl Championship Series and an Oregon State program that won ten games and finished the season nationally ranked.  The Warriors finished in second place in the Western Athletic Conference behind Boise State and returned to the Hawaii Bowl after missing out on postseason play in 2005 due to a losing record.  The Warriors defeated the Arizona State Sun Devils in the bowl game by a score of 41–24 to round out one of the school's most successful football seasons ever.

2012 Hawaii Warriors football team: The 2012 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2012 NCAA Division I FBS football season.  They were led by first-year head coach Norm Chow and played their home games at Aloha Stadium.  They were first year members of the Mountain West Conference.  They finished the season 3–9, 1–7 in Mountain West play to finish in a tie for ninth place.

2008 Hawaii Warriors football team: The 2008 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2008 NCAA Division I FBS college football season.  The Warriors started the season with a new coaching staff headed by Greg McMackin, who had previously been the team's defensive coordinator.

2009 Hawaii Warriors football team: The 2009 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2009 NCAA Division I FBS football season.  They were leadby second-year head coach Greg McMackin The Warriors finished the season 6–7 and 3–5 in Western Athletic Conference (WAC) play.

June Jones: June Sheldon Jones III (born February 19, 1953) is an American football coach and former player, currently serving as a head coach of the Hamilton Tiger-Cats of the Canadian Football League (CFL).  He was the head football coach at Southern Methodist University (SMU), where he served as head coach from 2008 to 2014, before resigning on September 8, 2014.  Jones was also the head football coach at the University of Hawaii at Manoa from 1999 to 2007.  Previously, he coached in the National Football League (NFL): a three-year tenure as head coach of the Atlanta Falcons from 1994 to 1996 and a ten-game stint as interim head coach of the San Diego Chargers in 1998.

2003 Hawaii Warriors football team: The 2003 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2003 NCAA Division I-A football season.  Hawaii finished the 2003 season with a 9–5 record, going 6–2 in Western Athletic Conference (WAC) play.  The Warriors made their second straight appearance in the Hawaii Bowl, facing off against Houston.  The Warriors capped off their second straight winning season, and the fourth in five seasons, under head coach June Jones with a bowl win.

2011 Hawaii Warriors football team: The 2011 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2011 NCAA Division I FBS football season.  The Warriors were led by fourth-year head coach Greg McMackin and played their home games at Aloha Stadium.  They were members of the Western Athletic Conference.  They finished the season 6–7, and 3–4 in WAC play to finish in a three way tie for fourth place.  Head coach Greg McMackin resigned at the end of the season due to mounting backlash from boosters and fans.

2005 Hawaii Warriors football team: The 2005 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2005 NCAA Division I-A college football season.  Hawaii finished the 2005 season with a 5–7 record, going 4–4 in WAC play.  The losing record was the first for Hawaii since 2000 and the team did not play in a bowl game for the first time since 2002.

Question: Which Canadian team is the former coach of the 2003 Hawaii Warriors football team now coaching?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the coach."
    },
    "previous_team_year": {
      "type": "integer",
      "description": "The year of the Hawaii Warriors team the coach previously led."
    },
    "current_coaching_position": {
      "type": "object",
      "properties": {
        "league": {
          "type": "string",
          "description": "The league of the current team."
        },
        "team_name": {
          "type": "string",
          "description": "The name of the Canadian team the coach is currently leading."
        }
      },
      "required": [
        "league",
        "team_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "previous_team_year",
    "current_coaching_position"
  ],
  "additionalProperties": false
}
