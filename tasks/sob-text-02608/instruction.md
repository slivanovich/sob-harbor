{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2006–07 Toronto Raptors season: The Toronto Raptors 2006–07 season is the twelfth National Basketball Association (NBA) season for the Toronto Raptors basketball franchise.  Following a poor 2005–06 season, General Manager Bryan Colangelo greatly revamped the team roster during the pre-season but continued to build the team around All-Star Chris Bosh.  Despite a sluggish start, the 2006–07 season transformed into a year for Toronto.  The Raptors captured their first division title, finished third in the Eastern Conference, made the playoffs for the first time in five years, equalled their best ever regular season record, and secured home court advantage for the first time in franchise history.  However, the Raptors met the New Jersey Nets in the first round of the playoffs and were defeated four games to two.  At the end of the regular season, head coach Sam Mitchell and Colangelo were named NBA Coach of the Year and NBA Executive of the Year respectively.\n\n2009–10 Memphis Tigers men's basketball team: The 2009–10 Memphis Tigers men's basketball team represented the University of Memphis in the 2009–10 college basketball season, the 89th season of Tiger basketball.  The Tigers were coached by first-year head coach Josh Pastner, played their home games at the FedExForum in Memphis, Tennessee and are members of Conference USA.  They finished the season 24–10, 13–3 in C-USA play.  They were the 2 seed in the 2010 Conference USA Men's Basketball Tournament where they were upset by 7 seed and eventual champion Houston.  They failed to be invited to the NCAA Tournament for the first time since 2005.  Instead, the Tigers were invited to the 2010 National Invitation Tournament where they advanced to the second round before losing to the Ole Miss Rebels.\n\nDamon Stoudamire: Damon Lamon Stoudamire (born September 3, 1973) is an American retired professional basketball player and the current head men's basketball coach at the University of the Pacific.  The 5 ft , 171 lb point guard was selected with the 7th overall pick by the Toronto Raptors in the 1995 NBA draft and won the 1995–96 NBA Rookie of the Year Award.  He played collegiately at the University of Arizona, and professionally for the Toronto Raptors, Portland Trail Blazers, Memphis Grizzlies and San Antonio Spurs.  He is the cousin of former Arizona Wildcats standout Salim Stoudamire and current NBA player Terrence Jones.\n\n2014–15 Memphis Tigers men's basketball team: The 2014–15 Memphis Tigers men's basketball team represented the University of Memphis in the 2014–15 NCAA Division I men's basketball season, the 94th season of Tiger basketball.  The Tigers, led by sixth year head coach Josh Pastner, played their home games at the FedExForum.  The 2014–15 season was the second season the Tigers participated in the American Athletic Conference.  The Tigers didn't play in a postseason tournament, the first time in 15 years.\n\n2007–08 Toronto Raptors season: The 2007–08 Toronto Raptors season was the 13th National Basketball Association (NBA) season for the Toronto Raptors basketball franchise, with the 2007–08 season scheduled to begin in October 2007.  The major acquisition was that of three-point specialist Jason Kapono from the Miami Heat, and much expectations also rested on the maturing of Andrea Bargnani, Toronto's number one draft pick in 2006.  With an overwhelming majority of home game sellouts (32, the second highest in franchise history), the Raptors qualified for the playoffs for the second year running, but this time around as the sixth seed.  The Raptors faced the third seed Orlando Magic, and were eliminated in five games.\n\nJimmy Williams (basketball coach): Jimmy Williams is an American basketball coach.  Williams is a native of Havana, Florida and graduated from Ashland University in 1970.  He was formerly an assistant coach with the University of Memphis men's basketball team under former head coach Josh Pastner.\n\n2010–11 Memphis Tigers men's basketball team: The 2010–11 Memphis Tigers men's basketball team represented the University of Memphis in the 2010–11 college basketball season, the 90th season of Tiger basketball.  The Tigers were coached by head coach Josh Pastner (assisted by Glynn Cyprien, Jack Murphy, and Willis Wilson), and played their home games at the FedExForum in Memphis, Tennessee.  They are members of Conference USA.  They finished the season 25–10, 10–6 in C-USA play and won the 2011 Conference USA Men's Basketball Tournament to earn an automatic bid in the 2011 NCAA Men's Division I Basketball Tournament where they lost in the second round to Arizona.\n\n2012–13 Memphis Tigers men's basketball team: The 2012–13 Memphis Tigers men's basketball team represented the University of Memphis in the 2012–13 NCAA Division I men's basketball season, the 92nd season of Tiger basketball.  The Tigers were coached by head coach Josh Pastner, who was assisted by Damon Stoudamire, Jimmy Williams and Aki Collins.  Stoudamire and Williams both assisted Pastner in 2011–12, and Collins left Marquette in May 2012 to join Pastner's staff.  The Tigers played their home games at the FedExForum in Memphis.  The 2012–13 season was the final season the Tigers participated in Conference USA before joining the American Athletic Conference in 2013–14.  They finished the season 31–5, 16–0 in C-USA play to be Conference USA regular season champions.  They also were champions of the Conference USA Tournament, winning the championship game in two overtimes vs Southern Miss, to earn an automatic bid to the 2013 NCAA Tournament.  In the tournament, they defeated Saint Mary's in the second round before losing in the third round to Michigan State.\n\n2015–16 Memphis Tigers men's basketball team: The 2015–16 Memphis Tigers men's basketball team represented the University of Memphis in the 2015–16 NCAA Division I men's basketball season, the 95th season of Tiger basketball.  The Tigers, led by seventh year head coach Josh Pastner, played their home games at the FedExForum.  The season marked the third season the Tigers have participated in the American Athletic Conference.  The Tigers finished with a record of 19–15, 8–10 in AAC play to finish in seventh place in conference.  The Tigers defeated Tulsa and Tulane in the AAC Tournament before losing to Connecticut in the championship.  For the second consecutive year, the Tigers did not participate in a postseason tournament.\n\n2011–12 Memphis Tigers men's basketball team: The 2011–12 Memphis Tigers men's basketball team represented the University of Memphis in the 2011–12 college basketball season, the 91st season of Tiger basketball.  The Tigers were coached by head coach Josh Pastner.  Pastner was assisted by Jack Murphy and Damon Stoudamire.  From the summer of 2011 until December 2011, NBA player Luke Walton was also an assistant coach, though he departed from the position with the end of the NBA lockout.  Jimmy Williams was brought in to replace Walton for the remainder of the 2011–12 season.  The Tigers played their home games at the FedExForum in Memphis, Tennessee and were members of Conference USA.\n\nQuestion: Which retired Toronto Raptors basketball player assisted coach Josh Pastner in 2012-13 for the Memphis Tigers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the retired basketball player.\"\n    },\n    \"player_status\": {\n      \"type\": \"string\",\n      \"description\": \"The professional status of the player (e.g., retired).\"\n    },\n    \"nba_teams_played_for\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of NBA teams the player played for.\"\n    },\n    \"coaching_assignment\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"team_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team the player assisted.\"\n        },\n        \"season\": {\n          \"type\": \"string\",\n          \"description\": \"The season of the coaching assignment.\"\n        },\n        \"head_coach_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the head coach under whom the player assisted.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The coaching role held by the player.\"\n        }\n      },\n      \"required\": [\n        \"team_name\",\n        \"season\",\n        \"head_coach_name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"nba_draft_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"draft_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the player was drafted into the NBA.\"\n        },\n        \"overall_pick\": {\n          \"type\": \"integer\",\n          \"description\": \"The overall pick number in the NBA draft.\"\n        },\n        \"drafting_team\": {\n          \"type\": \"string\",\n          \"description\": \"The NBA team that drafted the player.\"\n        }\n      },\n      \"required\": [\n        \"draft_year\",\n        \"overall_pick\",\n        \"drafting_team\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"awards_won\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of significant awards won by the player.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_status\",\n    \"nba_teams_played_for\",\n    \"coaching_assignment\",\n    \"nba_draft_info\",\n    \"awards_won\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the retired basketball player."
      },
      "player_status": {
        "type": "string",
        "description": "The professional status of the player (e.g., retired)."
      },
      "nba_teams_played_for": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of NBA teams the player played for."
      },
      "coaching_assignment": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "The name of the team the player assisted."
          },
          "season": {
            "type": "string",
            "description": "The season of the coaching assignment."
          },
          "head_coach_name": {
            "type": "string",
            "description": "The name of the head coach under whom the player assisted."
          },
          "role": {
            "type": "string",
            "description": "The coaching role held by the player."
          }
        },
        "required": [
          "team_name",
          "season",
          "head_coach_name",
          "role"
        ],
        "additionalProperties": false
      },
      "nba_draft_info": {
        "type": "object",
        "properties": {
          "draft_year": {
            "type": "integer",
            "description": "The year the player was drafted into the NBA."
          },
          "overall_pick": {
            "type": "integer",
            "description": "The overall pick number in the NBA draft."
          },
          "drafting_team": {
            "type": "string",
            "description": "The NBA team that drafted the player."
          }
        },
        "required": [
          "draft_year",
          "overall_pick",
          "drafting_team"
        ],
        "additionalProperties": false
      },
      "awards_won": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of significant awards won by the player."
      }
    },
    "required": [
      "player_name",
      "player_status",
      "nba_teams_played_for",
      "coaching_assignment",
      "nba_draft_info",
      "awards_won"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
