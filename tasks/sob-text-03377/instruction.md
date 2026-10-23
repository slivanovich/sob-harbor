{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShane Stafford: Shane Stafford (born March 14, 1976) is a former arena football quarterback.  Stafford is currently an offensive assistant for the Tampa Bay Storm of the Arena Football League (AFL).  He was signed by the Tallahassee Thunder as a street free agent in 2000.  He played college football at Connecticut.\n\nTaylor Potts: Taylor Potts (born October 13, 1987) is a former American football quarterback.  He played college football at Texas Tech, and was signed by the St. Louis Rams as an undrafted free agent in 2011.  He was waived during training camp, and then signed as a free agent by the San Diego Chargers in May 2012, where he was expected to compete for the third-string quarterback position.\n\nBret Stafford: Bret Alan Stafford (born December 15, 1964) is a former American football player.  He started as quarterback for the Texas Longhorns for almost 2½ seasons, 1985-87 during which time he established 14 UT records, among them most passing yards in a season (2,233) in 1986, and most passing yards over a career (4,735).  However, most of his records have since been surpassed by Peter Gardere, James Brown, Major Applewhite, and Vince Young.\n\nJake Delhomme: Jake Christopher Delhomme ( ; born January 10, 1975) is a former American football quarterback who played professionally in the National Football League (NFL).  Delhomme played college football at the University of Louisiana at Lafayette, then known as the University of Southwestern Louisiana, before being signed by the New Orleans Saints as an undrafted free agent after the 1997 NFL Draft.  Delhomme began his professional career as a practice squad player with the Saints in 1997 and 1998 and played in the NFL Europe for two years in between NFL seasons.  Returning to the Saints, Delhomme played his first NFL games in 1999.  Delhomme played as the Carolina Panthers starting quarterback from 2003 to 2009.  Delhomme held most of Carolina's quarterback records until Cam Newton broke most of them.  Delhomme led the team to Super Bowl XXXVIII in his first season with Carolina.\n\nAlex Carder: Alex Carder (born October 22, 1989) is an American football quarterback who is currently a free agent.  He was signed as a free agent by the Detroit Lions of the National Football League.  He was formerly the starting quarterback at Western Michigan University.\n\nVince Young: Vincent Paul Young Jr. (born May 18, 1983) is an American football quarterback who is currently a free agent.  Young played in the National Football League (NFL) for six seasons.  Young was drafted by the Tennessee Titans with the third overall pick in the 2006 NFL Draft.  He spent the first five seasons of his career with the Titans.  In his rookie season, Young was named the NFL Offensive Rookie of the Year and was named to the AFC Pro Bowl team as a reserve.  In 2009, Young earned his second Pro Bowl selection and was named \"Sporting News\" NFL Comeback Player of the Year.\n\nJarrett Brown: Jarrett Brown (born January 23, 1987) is an American football quarterback who is currently a free agent.  He played college football at West Virginia, and was signed by the San Francisco 49ers as an undrafted free agent following the 2010 NFL Draft.  He served as the starting quarterback for the West Virginia Mountaineers at West Virginia University during the 2009 season after three seasons as the backup to Pat White.  He was also a member of the Cleveland Browns, Indianapolis Colts, BC Lions and Spokane Shock.\n\nJerrod Johnson: Jerrod Terrel Johnson (born July 27, 1988) is an American football quarterback who is currently a free agent.  He was signed by the Philadelphia Eagles as an undrafted free agent in 2011.  He played college football at Texas A&M.  Johnson was Texas A&M's starting quarterback from 2008 to 2010, finishing his collegiate career ranked first in school history with 8,011 passing yards and 8,888 yards total offense.\n\nGraham Harrell: Graham Stanton Harrell (born May 22, 1985) is an American Football assistant coach and former American football and Canadian football quarterback.  He is currently the offensive coordinator and quarterbacks coach for the North Texas Mean Green.  He had been an assistant for the Washington State Cougars for the previous two seasons and had also worked for Oklahoma State in a quality control position .  He played college football at Texas Tech University, where he was an All-American quarterback, Heisman Trophy finalist in 2008, and set school, conference and national records for passing yards, attempts, completions, and touchdown passes.  Harrell was signed into the National Football League in 2010 by the Green Bay Packers.  He was a part of the Super Bowl XLV win with the Packers over the Pittsburgh Steelers.  He was also a member the New York Jets.  Prior to his time in the NFL, he was signed by the Saskatchewan Roughriders in 2009 as an undrafted free agent in the Canadian Football League.\n\nKeith Price: Keith Price (born June 28, 1991) is an American football quarterback who is currently a free agent.  He played college football at Washington, where he was the starting quarterback from 2011 to 2013.  He was signed as an undrafted free agent by the Seattle Seahawks in 2014.  He has also played professionally in the Canadian Football League (CFL), where he was a member of the Saskatchewan Roughriders and the BC Lions.\n\nQuestion: Bret Alan Stafford is a former American football player, who records have since been surpassed by which American football quarterback, who is currently a free agent?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_whose_records_were_surpassed\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the player whose records were surpassed.\"\n        },\n        \"position\": {\n          \"type\": \"string\",\n          \"description\": \"The position of the player whose records were surpassed.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"position\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"players_who_surpassed_records\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of players mentioned as having surpassed the records.\"\n    },\n    \"identified_surpassing_free_agent\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the American football quarterback who is currently a free agent and surpassed the records.\"\n        },\n        \"is_free_agent\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the identified player is currently a free agent.\"\n        },\n        \"position\": {\n          \"type\": \"string\",\n          \"description\": \"The position of the identified player.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_free_agent\",\n        \"position\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_whose_records_were_surpassed\",\n    \"players_who_surpassed_records\",\n    \"identified_surpassing_free_agent\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_whose_records_were_surpassed": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the player whose records were surpassed."
          },
          "position": {
            "type": "string",
            "description": "The position of the player whose records were surpassed."
          }
        },
        "required": [
          "name",
          "position"
        ],
        "additionalProperties": false
      },
      "players_who_surpassed_records": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of players mentioned as having surpassed the records."
      },
      "identified_surpassing_free_agent": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the American football quarterback who is currently a free agent and surpassed the records."
          },
          "is_free_agent": {
            "type": "boolean",
            "description": "Indicates if the identified player is currently a free agent."
          },
          "position": {
            "type": "string",
            "description": "The position of the identified player."
          }
        },
        "required": [
          "name",
          "is_free_agent",
          "position"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_whose_records_were_surpassed",
      "players_who_surpassed_records",
      "identified_surpassing_free_agent"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
