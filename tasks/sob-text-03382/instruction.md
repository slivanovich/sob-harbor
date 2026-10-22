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
Super Bowl XII: Super Bowl XII was an American football game between the National Football Conference (NFC) champion Dallas Cowboys and the American Football Conference (AFC) champion Denver Broncos to decide the National Football League (NFL) champion for the 1977 season.  The Cowboys defeated the Broncos 27–10 to win their second Super Bowl.  The game was played on January 15, 1978, at the Louisiana Superdome in New Orleans.  This was the first time that the Super Bowl was played in a domed stadium, and the first time that the game was played in prime time.

Super Bowl XXIV: Super Bowl XXIV was an American football game between the National Football Conference (NFC) champion San Francisco 49ers and the American Football Conference (AFC) champion Denver Broncos to decide the National Football League (NFL) champion for the 1989 season.  Played on January 28, 1990, at the Louisiana Superdome in New Orleans, Louisiana, the 49ers defeated the Broncos by the score of 55–10, winning their second consecutive Super Bowl, and tying the Pittsburgh Steelers with four Super Bowl victories.  San Francisco also became the first team to win back-to-back Super Bowls with two different head coaches; rookie head coach George Seifert took over after Bill Walsh retired following the previous season's Super Bowl.

Super Bowl 50: Super Bowl 50 was an American football game to determine the champion of the National Football League (NFL) for the 2015 season.  The American Football Conference (AFC) champions Denver Broncos defeated the National Football Conference (NFC) champions Carolina Panthers.  The game was played on February 7, 2016, at Levi's Stadium in Santa Clara, California (located in the San Francisco Bay Area).  As this was the 50th Super Bowl game, the league emphasized the "golden anniversary" with various gold-themed initiatives during the 2015 season, as well as suspending the tradition of naming each Super Bowl game with Roman numerals (under which the game would have been known as "Super Bowl L"), so the logo could prominently feature the Arabic numerals 50.

Super Bowl XXXII: Super Bowl XXXII was an American football game between the National Football Conference (NFC) champion Green Bay Packers and the American Football Conference (AFC) champion Denver Broncos to decide the National Football League (NFL) champion for the 1997 season.  The Broncos defeated the Packers by the score of 31–24.  The game was played on January 25, 1998 at Qualcomm Stadium in San Diego, California, the second time that the Super Bowl was held in that city.  Super Bowl XXXII also made Qualcomm Stadium the only stadium in history to have the Super Bowl and the World Series in the same year.

Super Bowl XLVIII: Super Bowl XLVIII was an American football game between the American Football Conference (AFC) champion Denver Broncos and National Football Conference (NFC) champion Seattle Seahawks to decide the National Football League (NFL) champion for the 2013 season.  The Seahawks defeated the Broncos 43–8, the largest margin of victory for an underdog and tied for the third largest point differential overall (35) in Super Bowl history with Super Bowl XXVII (1993).  It was the first time the winning team scored over 40 points, while holding their opponent to under 10.  This became the first Super Bowl victory for the Seahawks and the fifth Super Bowl loss for the Broncos, the most of any team.  The game was played on February 2, 2014, at MetLife Stadium at the Meadowlands Sports Complex in East Rutherford, New Jersey, the first Super Bowl played outdoors in a cold-weather city and the first Super Bowl to be played on a February 2.

Calvin Collins: Calvin Lewis Collins (born January 5, 1974 in Beaumont, Texas) is a former American football guard who played seven seasons in the National Football League from 1997–2004.  He started in Super Bowl XXXIII for the Atlanta Falcons.

Super Bowl XXXIII: Super Bowl XXXIII was an American football game played between the American Football Conference (AFC) champion Denver Broncos and the National Football Conference (NFC) champion Atlanta Falcons to decide the National Football League (NFL) champion for the 1998 season.  The Broncos defeated the Falcons by the score of 34–19, winning their second consecutive Super Bowl.  The game was played on January 31, 1999, at Pro Player Stadium in Miami (now part of the suburb of Miami Gardens, which became a separate city in 2003).

Super Bowl XXII: Super Bowl XXII was an American football game between the National Football Conference (NFC) champion Washington Redskins and American Football Conference (AFC) champion Denver Broncos to decide the National Football League (NFL) champion for the 1987 season.  The Redskins defeated the Broncos by the score of 42–10, winning their second Super Bowl.  The game was played on January 31, 1988 at Jack Murphy Stadium in San Diego, the first time that the Super Bowl was played in that city.

Super Bowl XXVI: Super Bowl XXVI was an American football game between the National Football Conference (NFC) champion Washington Redskins and the American Football Conference (AFC) champion Buffalo Bills to decide the National Football League (NFL) champion for the 1991 season.  The Redskins defeated the Bills by the score of 37–24, becoming the fourth team after the Pittsburgh Steelers, the Oakland Raiders, and the San Francisco 49ers to win three Super Bowls.  The Bills became the third team, after the Minnesota Vikings (Super Bowls VIII and IX) and the Denver Broncos (Super Bowls XXI and XXII), to lose back-to-back Super Bowls.  The game was played on January 26, 1992, at the Hubert H. Humphrey Metrodome in Minneapolis, Minnesota, the first time the city has played host to a Super Bowl (the city will host Super Bowl LII at U.S. Bank Stadium).

Super Bowl XXI: Super Bowl XXI was an American football game between the American Football Conference (AFC) champion Denver Broncos and the National Football Conference (NFC) champion New York Giants to decide the National Football League (NFL) champion for the 1986 season.  The Giants defeated the Broncos by the score of 39–20, winning their first ever Super Bowl, and their first NFL title since 1956.  The game was played on January 25, 1987, at the Rose Bowl in Pasadena, California.

Question: Calvin Collins started in an American football game played between the Denver Broncos and what other team, to determine the champion of the 1998 season?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "super_bowl_identifier": {
      "type": "string",
      "description": "The official name or identifier of the Super Bowl game."
    },
    "nfl_season": {
      "type": "string",
      "description": "The NFL season for which the Super Bowl determined the champion."
    },
    "player_who_started": {
      "type": "string",
      "description": "The name of the player mentioned in the context who started in this Super Bowl."
    },
    "teams_involved": {
      "type": "array",
      "description": "A list of teams that participated in the Super Bowl.",
      "items": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "The name of the participating team."
          },
          "conference": {
            "type": "string",
            "enum": [
              "AFC",
              "NFC"
            ],
            "description": "The conference the team represents (AFC or NFC)."
          },
          "is_winner": {
            "type": "boolean",
            "description": "True if this team won the Super Bowl, false otherwise."
          },
          "score": {
            "type": "integer",
            "description": "The final score of the team in the Super Bowl."
          },
          "is_question_answer": {
            "type": "boolean",
            "description": "True if this team is the answer to the specific question asked."
          }
        },
        "required": [
          "team_name",
          "conference",
          "is_winner",
          "score",
          "is_question_answer"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "super_bowl_identifier",
    "nfl_season",
    "player_who_started",
    "teams_involved"
  ],
  "additionalProperties": false
}
