{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBilly Batty: William \"Billy\" Batty (13 July 1886 – after 1922) was an English footballer who scored 24 goals in 85 appearances in the Football League playing for Sheffield United, Bristol City, Swindon Town and Barnsley.  He played as an inside forward.  He also played in Lincoln City's 1911–12 Central League title-winning side, and in the Southern League for Swindon Town, during which time he appeared four times for the Southern League representative eleven.\n\nWill Dalton: Will Dalton from Queenstown, Maryland is a professional lacrosse transition player for the San Jose Stealth of the National Lacrosse League.  Before college, Dalton was a member of the 2004 All-Tewaaraton Team for the Baltimore/Washington area.  The newspapers, Baltimore Sun and Washington Post named him first team all-Metro.  He was the 2004 Baltimore Sun Anne Arundel County Player of the Year, making him the third straight St. Mary's player to win the honor.  The Baltimore Sun also picked Dalton for first team all-county.  In high school, Dalton won 71 percent of face-offs as a senior.  He scored 22 goals and added seven assists despite being double and triple-teamed almost every time he touched the ball.  Dalton was also all-county and all-metro as a junior and scored 24 goals and added 10 assists while winning 72 percent of his face-offs in 2003.\n\nIlkka Pikkarainen: Ilkka Pikkarainen (born April 19, 1981 in Sonkajärvi, Finland) is a Finnish ice hockey right winger who plays for Pelicans in the Sm-liiga.  Pikkarainen began his professional career in the SM-liiga (FNL) with HIFK at the end of the 2000–01 season.  He played there for two full seasons and was drafted by the New Jersey Devils in the seventh round of the 2002 NHL Entry Draft, 218th overall.  Pikkarainen came over to North America to play for the Albany River Rats, the Devils' American Hockey League affiliate, starting in the 2003–04 season.  After playing in the AHL for three seasons, Pikkarainen returned to play with HIFK for the 2008–09 season, where he played in 54 games and scored 24 goals, leading the team.\n\n1962–63 Liverpool F.C. season: Liverpool F.C. made its comeback in the Football League's First Division.  Roger Hunt, who had scored 41 goals in the promotion winning league campaign, proved himself in the top flight and scored 24 goals, as Liverpool finished in 8th position of the league, and also reached the semi finals of the FA Cup.\n\nInvincible Eleven: Union of Invincible Eleven & Majestic Sports Association Inc. also known as Invincible Eleven (I.E.) is a football club from Liberia based in Monrovia.  They are one of the founding members of football in Liberia.  Their home stadium is the Antonette Tubman Stadium.  Invincible Eleven is one of Liberia's most popular and historic clubs, along with Mighty Barolle.  George Weah, Liberia's most famous footballer, scored 24 goals in 23 games during a spell at I.E. early in his career, in the 1986/87 season.\n\nChris Morgan (footballer): Christopher Paul Morgan (born 9 November 1977) is an English former professional footballer who now works as joint-caretaker-manager at EFL League Two club Port Vale, alongside David Kelly.  An \"uncompromising\" defender, he scored 24 goals in 491 league and cup appearances in a 16-year career in English football.\n\n1989 WAFU Club Championship: The 1989 WAFU Club Championship was the thirteenth football club tournament season that took place for the runners-up of each West African country's domestic league, the West African Club Championship.  It was won by Nigeria's Ranchers Bees after defeating ASEC Abidjan under the away goals rule with a total of 4-3 goals in two matches.  A total of 37 goals were scored, second time in a row, fewer than last season.  Originally a 28 match season, neither clubs from the Gambia, Guinea-Bissau, Mauritania nor Togo participated.  Invincible Eleven directly headed to the semis, later Ranchers Bees directly headed to the finals.\n\nGeorge Weah: George Tawlon Manneh Oppong Ousman Weah (born 1 October 1966) is a Liberian humanitarian, politician, and retired professional footballer who played as a striker.  Regarded as one of the greatest African players of all-time and as one of the best forwards of his generation, in 1995 he was named FIFA World Player of the Year and won the Ballon d'Or, becoming the first African player to win these awards.  In 1989, 1994 and 1995, he was named the African Footballer of the Year, and in 1996, he was named African Player of the Century.  Known for his acceleration, speed, and dribbling ability, in addition to his goalscoring and clinical finishing, Weah was described by FIFA as \"the precursor of the multi-functional strikers of today\".  In 2004, he was named by Pelé in the FIFA 100 list of the world's greatest living players.\n\nAnis Ahmed: Muhammad Anis Ahmed (born 10 December 1973 in Gojra) is a field hockey player and former member of the Pakistan National Hockey Team.  With the national team he participated in the 2000 Summer Olympics and the 1998 Asian Games, where the team won bronze medals.  He played 87 matches for Pakistan and scored 24 goals in his career.\n\nTed Wade (footballer, born 1901): Edward \"Ted\" Wade (born 29 September 1901, date of death unknown) was an English professional association footballer who played as an inside forward.  He started his career with Burnley, but failed to make an appearance for the club and left at the end of the 1922–23 season.  In the summer of 1924, he joined Football League Third Division North side New Brighton, where he scored 24 goals in 72 league games over a four-year period.  At the start of the 1928–29 season, he signed for Third Division South outfit Exeter City, where he played nine matches, scoring five league goals.  He left Exeter City in 1929, and subsequently had a spell in non-league football with Aldershot.\n\nQuestion: What Liberian humanitarian, politician, and retired professional footballer, scored 24 goals in 23 games during a spell at Invincible Eleven, early in his career, in the 1986/87 season?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the player.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the player.\"\n    },\n    \"career_roles\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the player's significant career roles.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"club_performance\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the player's performance at a specific club during a particular season.\",\n      \"properties\": {\n        \"club_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the football club.\"\n        },\n        \"season\": {\n          \"type\": \"string\",\n          \"description\": \"The season in which the performance occurred.\"\n        },\n        \"goals_scored\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of goals scored.\"\n        },\n        \"games_played\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of games played.\"\n        }\n      },\n      \"required\": [\n        \"club_name\",\n        \"season\",\n        \"goals_scored\",\n        \"games_played\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"nationality\",\n    \"career_roles\",\n    \"club_performance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The full name of the player."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the player."
      },
      "career_roles": {
        "type": "array",
        "description": "A list of the player's significant career roles.",
        "items": {
          "type": "string"
        }
      },
      "club_performance": {
        "type": "object",
        "description": "Details about the player's performance at a specific club during a particular season.",
        "properties": {
          "club_name": {
            "type": "string",
            "description": "The name of the football club."
          },
          "season": {
            "type": "string",
            "description": "The season in which the performance occurred."
          },
          "goals_scored": {
            "type": "integer",
            "description": "The number of goals scored."
          },
          "games_played": {
            "type": "integer",
            "description": "The number of games played."
          }
        },
        "required": [
          "club_name",
          "season",
          "goals_scored",
          "games_played"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "nationality",
      "career_roles",
      "club_performance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
