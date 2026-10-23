{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCliff Branch: Clifford Branch (born August 1, 1948) is a retired American football wide receiver who spent his entire 14-year National Football League career with the Oakland/Los Angeles Raiders, winning three Super Bowl rings in Super Bowl XI, Super Bowl XV and Super Bowl XVIII.  He is the only wide receiver to have played on all three Raiders Super Bowl teams.\n\nRoynell Young: Roynell Young (born December 1, 1957) is a former professional American football safety and cornerback who played for the Philadelphia Eagles his entire National Football League (NFL) career, from 1980 to 1988.  Young was selected by the Eagles from Alcorn State University in the first round (23rd overall) of the 1980 NFL Draft.  In his rookie year, he played in Super Bowl XV and was selected to the Pro Bowl in his second season.  He was one of two players who played in both Super Bowl XV and The Fog Bowl for the Eagles.  The other was offensive lineman Ron Baker.\n\nIra Matthews: Ira Richard Matthews, III (born August 23, 1957) is a former professional American football player who played kick returner and punt returner for three seasons for the Oakland Raiders.  Matthews stood 5\"8' and weighed 175 lbs which made it difficult to catch him.  Matthews was named to the NFL 1979 All-Pro Team as a return man during his rookie season.  On October 25, 1979, Matthews set a Monday Night Football record for kick-off returns with a 104-yard return against the San Diego Chargers.  Matthews was a member of the Oakland Raiders Super Bowl XV championship team.  During his three seasons with the Raiders he helped lead his team to win the 1980 Wild Card, 1981 AFC West Conference Championship, and Super Bowl XV.  His career ended at the end of his 1981 season due to injuries, only playing for three seasons total.\n\nHenry Lawrence (American football): Henry Lawrence (born September 26, 1951) is a former professional American football player.  A two-time Pro Bowler, he played in the National Football League for 13 seasons as an offensive tackle with the Oakland/Los Angeles Raiders.  He played in Super Bowl XI and was a starter in Super Bowl XV and Super Bowl XVIII for the Raiders earning three Super Bowl Championship Rings.  Lawrence is a member of Alpha Phi Alpha fraternity.  At the 2010 Alpha Phi Alpha Convention, Henry was the recipient of the Jesse Owens Achievement Award for his athletic excellence.\n\nMonte Johnson: Monte C. Johnson (born October 26, 1951) is a retired American football player.  Johnson, who never started in college, was selected by The Oakland Raiders during the second round of the 1973 NFL Draft as the 49th player selected overall.  Johnson attended the University of Nebraska and won two National Championships with Nebraska, and one Super Bowl (XI) with the Oakland Raiders.  Johnson was injured in the 1980 season, and as a result did not play in Super Bowl XV, when the Raiders defeated the Eagles.  Johnson considers the 1977 AFC Divisional playoff game against the Baltimore Colts, a game known as, \"Ghost to the Post\", to be his greatest game.  Johnson finished the game, which went to double overtime, with 22 tackles despite suffering a broken vertebra during regulation.  Johnson retired from professional football in 1981, after eight seasons in Oakland, as a result of a career-ending knee injury he incurred early in the 1980 season.\n\nDave Pear: David Pear (born June 1, 1953 in Vancouver, Washington) is a retired NFL football player.  He was the first Tampa Bay Buccaneers player to be selected to the Pro Bowl and played in Super Bowl XV for the winning Oakland Raiders.\n\nTom Kelleher (American football official): Thomas \"Tom\" Kelleher (August 31, 1925March 31, 2011) was an American football official in the National Football League (NFL) for 28 years, from 1960 until the conclusion of the 1987 NFL season.  Working as a back judge, Kelleher was assigned five Super Bowls; Super Bowl IV, Super Bowl VII, Super Bowl XI, Super Bowl XV and Super Bowl XIX; one of five officials to reach such an achievement.  He wore number 25 for the major part of his career.  For 1979 through 1981, Kelleher wore the number 7.  He was born in Philadelphia, and died in Miami.\n\nSuper Bowl XV: Super Bowl XV was an American football game between the American Football Conference (AFC) champion Oakland Raiders and the National Football Conference (NFC) champion Philadelphia Eagles to decide the National Football League (NFL) champion for the 1980 season.  The Raiders defeated the Eagles by the score of 27–10, becoming the first wild card playoff team to win a Super Bowl.\n\nSuper Bowl XXXVII: Super Bowl XXXVII was an American football game between the American Football Conference (AFC) champion Oakland Raiders and the National Football Conference (NFC) champion Tampa Bay Buccaneers to decide the National Football League (NFL) champion for the 2002 season.  The Buccaneers defeated the Raiders by the score of 48–21, tied with Super Bowl XXXV for the seventh largest Super Bowl margin of victory, and winning their first ever Super Bowl.  The game, played on January 26, 2003 at Qualcomm Stadium in San Diego, California, was the sixth Super Bowl to be held a week after the conference championship games (XVII, XXV, XXVIII, XXXIV, and XXXVI).  It was also the last Super Bowl played in the month of January.  Super Bowl XXXVI was the first to be played in February, due to the NFL postponing games for a week after the September 11 attacks.  Starting with Super Bowl XXXVIII in 2004, the Super Bowl has been permanently played in February.  This was the last Super Bowl until Super Bowl 50 to take place in California.\n\nDean Look: Dean Zachary Look (born July 23, 1937) was an American football and baseball player.  He played college football as quarterback at Michigan State University and professional football for the New York Titans of the American Football League (AFL).  He was also a Major League Baseball (MLB) outfielder, and American football official in the National Football League (NFL).  He is most notable for his 29 years of service as an NFL official: first as line judge in 1971 and as side judge in 1978.  He was the side judge who signaled touchdown on the historical Joe Montana to Dwight Clark pass better known as \"The Catch\" during the 1982 NFC Championship game between the Dallas Cowboys and the San Francisco 49ers.  As an official, Look wore the uniform number 49 and was assigned to three Super Bowls—Super Bowl XIII in 1979, Super Bowl XV in 1981, and Super Bowl XXVII in 1993.\n\nQuestion: David Pear was a NFL football player, that won Super Bowl XV, playing on which team?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the NFL player.\"\n    },\n    \"super_bowl_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"super_bowl_identifier\": {\n          \"type\": \"string\",\n          \"description\": \"The official identifier of the Super Bowl (e.g., Super Bowl XV).\"\n        },\n        \"season_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The NFL season year for which the Super Bowl was played.\"\n        },\n        \"winning_team\": {\n          \"type\": \"string\",\n          \"description\": \"The team that won this Super Bowl.\"\n        },\n        \"losing_team\": {\n          \"type\": \"string\",\n          \"description\": \"The team that lost this Super Bowl.\"\n        },\n        \"winning_score\": {\n          \"type\": \"integer\",\n          \"description\": \"The score of the winning team.\"\n        },\n        \"losing_score\": {\n          \"type\": \"integer\",\n          \"description\": \"The score of the losing team.\"\n        }\n      },\n      \"required\": [\n        \"super_bowl_identifier\",\n        \"season_year\",\n        \"winning_team\",\n        \"losing_team\",\n        \"winning_score\",\n        \"losing_score\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"player_team_for_super_bowl_win\": {\n      \"type\": \"string\",\n      \"description\": \"The team the player was on when they won the specified Super Bowl.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"super_bowl_details\",\n    \"player_team_for_super_bowl_win\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the NFL player."
      },
      "super_bowl_details": {
        "type": "object",
        "properties": {
          "super_bowl_identifier": {
            "type": "string",
            "description": "The official identifier of the Super Bowl (e.g., Super Bowl XV)."
          },
          "season_year": {
            "type": "integer",
            "description": "The NFL season year for which the Super Bowl was played."
          },
          "winning_team": {
            "type": "string",
            "description": "The team that won this Super Bowl."
          },
          "losing_team": {
            "type": "string",
            "description": "The team that lost this Super Bowl."
          },
          "winning_score": {
            "type": "integer",
            "description": "The score of the winning team."
          },
          "losing_score": {
            "type": "integer",
            "description": "The score of the losing team."
          }
        },
        "required": [
          "super_bowl_identifier",
          "season_year",
          "winning_team",
          "losing_team",
          "winning_score",
          "losing_score"
        ],
        "additionalProperties": false
      },
      "player_team_for_super_bowl_win": {
        "type": "string",
        "description": "The team the player was on when they won the specified Super Bowl."
      }
    },
    "required": [
      "player_name",
      "super_bowl_details",
      "player_team_for_super_bowl_win"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
