{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1983 Miami Dolphins season: The 1983 season was the 18th season in football for the Miami Dolphins and they sought to return to the Super Bowl after losing to the Washington Redskins in Super Bowl XVII.  It was also a turning point in the team's history, as in the 1983 NFL Draft a young quarterback slipped to deep in the opening round, being passed over by such teams as division rivals New York who drafted Ken O'Brien and New England who drafted Tony Eason.  With the 27th pick, the Dolphins decided to take a chance on Dan Marino.  In the draft's eighth round the Dolphins also selected receiver Mark Clayton.\n\nMelvin Baker: Melvin Clyde Baker (born August 12, 1950) is a former American football wide receiver who played three seasons in the National Football League with the Miami Dolphins, New Orleans Saints, San Diego Chargers, New England Patriots and Houston Oilers.  He was drafted by the Miami Dolphins in the eighth round of the 1974 NFL Draft.  He played college football at Texas Southern University and attended Sam Houston High School in Houston, Texas.  Baker was also a member of the St. Louis Cardinals and Buffalo Bills.\n\nScott Schwedes: Scott Andrew Schwedes (born June 30, 1965) is a former American football wide receiver who played four seasons in the National Football League (NFL) with the Miami Dolphins and San Diego Chargers.  He was drafted by the Dolphins in the second round of the 1987 NFL Draft with the 56th overall pick.  He played college football at Syracuse University and attended Jamesville-DeWitt High School in DeWitt, New York.  His father Gerhard Schwedes also played football at Syracuse and later the American Football League.\n\nMark Clayton (American football, born 1961): Mark Gregory Clayton (born April 8, 1961) is a former American football wide receiver who played most of his career with the Miami Dolphins, entering the league in 1983 with the Dolphins and playing there until 1992.  He finished out his career with the Green Bay Packers, playing a single season with them in 1993.  He attended the University of Louisville.\n\nChad Johnson: Chad Javon Johnson (born January 9, 1978), formerly Chad Ochocinco, is a former American football wide receiver.  He played college football for both Santa Monica College and Oregon State University, and played eleven seasons in the National Football League (NFL) for the Cincinnati Bengals, New England Patriots, and the Miami Dolphins.  He was drafted by the Cincinnati Bengals of the National Football League (NFL) in the second round of the 2001 NFL Draft, and played for the Bengals for 10 seasons.  In 2011, Johnson was traded to the New England Patriots which he played for in Super Bowl XLVI.  In 2012, Johnson played for the Miami Dolphins during preseason but was released following his arrest for domestic violence.  He played for the Montreal Alouettes of the Canadian Football League (CFL) from 2014 to 2015, and played one game in 2017 for Mexican team Monterrey Fundidores of the Liga de Fútbol Americano Profesional.\n\nKenny Stafford: Kenny Stafford (born April 20, 1990) is a Canadian football wide receiver who is currently a member of the Edmonton Eskimos of the Canadian Football League (CFL).  In the United States he has been a member of the Atlanta Falcons (NFL), Pittsburgh Power (AFL) and Miami Dolphins (NFL).  Elsewhere in the CFL Stafford has been a member of the Calgary Stampeders, Montreal Alouettes and Winnipeg Blue Bombers.  He is the nephew of former American football wide receiver and 2013 Hall of Fame Inductee Cris Carter.\n\nNat Moore: Nathaniel Moore (born September 19, 1951) is an American former college and professional football player who was a wide receiver in the National Football League (NFL) for thirteen seasons during the 1970s and 1980s.  Moore played college football for the University of Florida, and thereafter, he played professionally for the Miami Dolphins of the NFL.  He is best known as a favorite passing target of Dolphins quarterbacks Bob Griese and Dan Marino.\n\n2000 Miami Dolphins season: The 2000 Miami Dolphins season was the franchise's 35th season in the National Football League.  Dave Wannstedt was named the fourth head coach in franchise history on January 16, 2000, the same day that Jimmy Johnson resigned.  Prior to the season, Dan Marino retired after 17 seasons with the Miami Dolphins.  Jay Fiedler, who left the Jacksonville Jaguars, succeeded Marino as starting quarterback.  Additionally, Damon Huard remained a backup quarterback and started for Fiedler in one game during the season.\n\nJim Lash: James Verle Lash (born November 12, 1951) is a former American football wide receiver in the National Football League in the 1970s and played on three Super Bowl teams.  He attended Garfield High School in Akron, Ohio, the same high school that fellow NFL wide receiver Steve Craig attended.  His five-year pro-career was spent with the Minnesota Vikings in which he helped lead to Super Bowl VIII, Super Bowl IX and Super Bowl XI all coming up a bit short against the dynasty teams of the Miami Dolphins, the Pittsburgh Steelers and the Oakland Raiders.\n\nFrank Jackson (American football): Frank Hardin Jackson (born April 14, 1939) is a former American football wide receiver.  He played college football at Southern Methodist University (SMU) and professionally with the American Football League's Dallas Texans, the Kansas City Chiefs, and the Miami Dolphins.  As a halfback, he scored four TDs (two rushing, two receiving) for the Texans in a 49–21 victory over the Denver Broncos in 1961.  As a wide receiver, in 1964 he caught four touchdown passes from Len Dawson in a 49–6 Chiefs defeat of the San Diego Chargers.  That tied the pro football record at the time.  He was an American Football League All-Star in 1965.  He played on the Texans' 1962 AFL Championship team, winning the longest pro football game ever played up to that time in the AFL Championship game against the two-time defending AFL Champion Houston Oilers.\n\nQuestion: What former American football wide receiver played for the Miami Dolphins with Dan Marino?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former American football wide receiver.\"\n    },\n    \"position\": {\n      \"type\": \"string\",\n      \"description\": \"The primary playing position of the player.\"\n    },\n    \"team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the NFL team the player played for with Dan Marino.\"\n    },\n    \"played_with_dan_marino\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the player's tenure with the team overlapped with Dan Marino's.\"\n    },\n    \"dolphins_tenure_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the player started playing for the Miami Dolphins.\"\n    },\n    \"dolphins_tenure_end_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the player ended playing for the Miami Dolphins.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"position\",\n    \"team_name\",\n    \"played_with_dan_marino\",\n    \"dolphins_tenure_start_year\",\n    \"dolphins_tenure_end_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the former American football wide receiver."
      },
      "position": {
        "type": "string",
        "description": "The primary playing position of the player."
      },
      "team_name": {
        "type": "string",
        "description": "The name of the NFL team the player played for with Dan Marino."
      },
      "played_with_dan_marino": {
        "type": "boolean",
        "description": "Indicates if the player's tenure with the team overlapped with Dan Marino's."
      },
      "dolphins_tenure_start_year": {
        "type": "integer",
        "description": "The year the player started playing for the Miami Dolphins."
      },
      "dolphins_tenure_end_year": {
        "type": "integer",
        "description": "The year the player ended playing for the Miami Dolphins."
      }
    },
    "required": [
      "player_name",
      "position",
      "team_name",
      "played_with_dan_marino",
      "dolphins_tenure_start_year",
      "dolphins_tenure_end_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
