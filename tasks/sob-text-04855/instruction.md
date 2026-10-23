{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2008 Galway United F.C. season: 2008 Galway United F.C. season.  This is a list of competitive matches played by Galway United F.C. in during the 2008 League of Ireland Premier Division season.  Jeff Kenna served as player-manager of Galway United F.C. during this season.  During the season there were rumours of financial troubles and the selling of the players within the squad, most notably Derek O'Brien.  Relegation also loomed on the horizon.  However, a surge of great form which saw the United reach the 2008 FAI Cup semi-finals gave the club a fighting chance of survival.  A 3–0 victory over Finn Harps in the penultimate game of the season put survival in United's own hands and their victory the following week away to UCD ensured that Galway United would be playing in the League of Ireland Premier Division in 2009.\n\n2007–08 Paris Saint-Germain F.C. season: The 2007–08 season was French football club Paris Saint-Germain's 35th professional season, their 35th season in Ligue 1 and their 34th consecutive season in French top-flight.  PSG was managed by Paul Le Guen - in his first full season since replacing Guy Lacombe.  The club was chaired by Alain Cayzac until Simon Tahar took over.  Paris Saint-Germain was present in the 2007–08 Ligue 1, the 2007–08 Coupe de France and the 2007–08 Coupe de la Ligue.  Last season's poor results prevented the capital club to participate in consecutive years in a European competition.  Paris Saint-Germain's average home gate for the 2007–08 season was 36,947, the third highest in the Ligue 1.\n\nAnders Gozzi: Anders Gozzi (born (1967--) 12, 1967 ) is a Swedish former professional ice hockey player and currently the general manager of the AIK IF organization.  In his career as a professional ice hockey player he played for AIK, Brynäs IF, and Düsseldorfer EG.  In his first season with AIK, in the 1986–87 season, the team became promoted to Elitserien.  He played in AIK during the majority of his career, and scored 315 points in 579 Elitserien (SEL) games.  He became Elitserien champions with Brynäs IF in the 1992–93 season.  He ended his ice hockey player career with AIK in the 2003–04 season, when the team played in HockeyAllsvenskan.  He also was the general manager of AIK that season, and in the 2004–05 season he also became an assistant coach, replacing Tomas Winje mid-season.  In the 2007–08 season he was the head coach of AIK from early December 2007 until the end of the season.  Since the end of the 2007–08 season, he has been the general manager of AIK.\n\nDennis Wise: Dennis Frank Wise (born 16 December 1966) is an English former football player and manager, and former Executive Director of Football at Newcastle United.\n\nLeeds Fans Utd: Leeds Fans Utd is a private limited company which intends to secure a stake in Leeds United F.C. Part of the funding for the effort comes from ordinary Leeds fans, who collectively acquire shares in the company through the Leeds Fans Community Benefit Society.  If the company is successful in acquiring a stake in the club, the society will be able to elect representation to the club's board.  If the company cannot acquire a stake, the society will return fans at least 90% of their investment.\n\nLeeds United F.C. Reserves and Youth Team: Leeds United Reserves were the English football reserve team of Leeds United F.C. In previous seasons, they played at York City's Bootham Crescent, South Leeds Stadium and the first team's ground Elland Road.  The reserves were generally a mix of recovering or fringe first-team players, young professionals and promising scholars.\n\nLeeds United F.C.–Millwall F.C. rivalry: The rivalry between Leeds United and Millwall is a bitter North–South divide game in English football.  Millwall were founded in South London in 1885 and Leeds United in West Yorkshire in 1919, over 170 miles (170 mi ) apart.  Both sides entered the Football League in 1920–21 season, albeit in different divisions.  From 1920 to 2003 the sides met just 12 times; competing in different tiers for the majority of their histories, and neither considering the other a rival on the pitch.  Since Leeds were relegated from the Premier League in 2004, the teams have met 23 times in 13 years.  The rivalry began in League One during the 2007–08 season, with disorder and violent clashes between both sets of fans and the police at Elland Road.  It continued into the 2008–09 season; where the teams were vying for promotion to the Championship, culminating in Millwall knocking Leeds out of the League One playoffs at the semi-final stage.\n\n2007–08 Leeds United F.C. season: The 2007–08 season was Leeds United F.C.'s first ever season in the third tier of English football and saw them finish in the play-offs in League One.  Dennis Wise started the season as manager, but left the club in January 2008 to join Newcastle as Executive Director of Football.  Wise was replaced just days later with former Leeds captain, Gary McAllister.\n\nMarching On Together: \"Leeds!  Leeds!  Leeds!\"  (commonly known as \"Marching On Together\") is the name of the anthem of Leeds United A.F.C. Unlike many football songs that are just new words set to existing music, \"Leeds!  Leeds!  Leeds!\"  is an original composition by Les Reed and Barry Mason.  The song first appeared in 1972 as the B-side of the record released by Leeds United to coincide with the team reaching the 1972 FA Cup Final, the A-side being titled \"Leeds United\".  The vocals on the original recording were sung by the then-members of the Leeds United team and their supporters.  The record stayed in the UK Singles Chart for almost 3 months, peaking at number 10.\n\nTom Rogers (footballer): Tom Rogers (born 1885) was an English footballer who played as a defender for Liverpool in The Football League.  Rogers started his career at Rossendale United F.C. where his performances led to a transfer to Liverpool.  He made his debut for the club on the last day of the 1907–08 season.  The next season, he was a regular in the starting lineup he made 12 appearances for the team before he suffered a serious injury in a match against Nottingham Forest F.C. which meant he did not play for 13 months.  Following his return he was unable to reclaim his place in the side and only played sporadically.\n\nQuestion: What is the birthday of the first manager for Leeds United F.C. in the 2007-08 season?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football club.\"\n    },\n    \"season\": {\n      \"type\": \"string\",\n      \"description\": \"The specific football season.\"\n    },\n    \"manager\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the manager.\"\n        },\n        \"birthday\": {\n          \"type\": \"string\",\n          \"description\": \"The birthday of the manager in 'DD Month YYYY' format.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birthday\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"club_name\",\n    \"season\",\n    \"manager\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "club_name": {
        "type": "string",
        "description": "The name of the football club."
      },
      "season": {
        "type": "string",
        "description": "The specific football season."
      },
      "manager": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the manager."
          },
          "birthday": {
            "type": "string",
            "description": "The birthday of the manager in 'DD Month YYYY' format."
          }
        },
        "required": [
          "name",
          "birthday"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "club_name",
      "season",
      "manager"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
