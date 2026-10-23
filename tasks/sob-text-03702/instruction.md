{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2011–12 FC Schalke 04 season: The 2011–12 season is the 108th season in Schalke 04's history.  The team will compete in the Bundesliga, DFB-Pokal and the UEFA Europa League.  The team's top scorer is Klaas-Jan Huntelaar with 29 goals in the Bundesliga and 48 in total.\n\nKlaas-Jan Huntelaar: Dirk Jan Klaas \"Klaas-Jan\" Huntelaar (] ; born 12 August 1983), nicknamed \"The Hunter\", is a Dutch professional footballer who plays as a striker for Ajax and the Netherlands national team.\n\nRuud van Nistelrooy: Rutgerus Johannes Martinus \"Ruud\" van Nistelrooy (Dutch: \"Ruud van Nistelrooij\" ; ] ; born 1 July 1976) is a retired Dutch footballer and a current manager for the PSV youth team.  A former striker, he is the fourth-highest goalscorer in UEFA Champions League history with 56 goals.  He is a three-time Champions League top scorer, as well as a top scorer in three different European domestic leagues.\n\nAmjad Radhi: Amjad Radhi Yousif Al-Janabi (Arabic: أمجد راضي يوسف الجنابي‎ ‎ ), (born 15 July 1990) is an Iraqi professional footballer who currently plays for Al-Quwa Al-Jawiya in the Iraqi Premier League.  He won the 2009–10 Iraqi Premier League and 2012–13 Iraqi Premier League top scorer awards, as well as the 2012 AFC Cup top scorer award.\n\nPetre Grosu: Petre Grosu (born 27 November 1955) is a Romanian former professional footballer who played as a midfielder or as a forward.  He started his professional career at Sportul Studențesc, but he would have known full glory at Bihor Oradea being the top scorer of the team in the 1981–82 Divizia B season, also succeeding in promoting with Bihor Oradea.  The best performance would come at the end of the 1982–83 Divizia A season when Grosu has become the top scorer of the Divizia A, the first and the last in the history of FC Bihor.  With this performance, he secured a place in the Bihor Oradea hall of fame and a well-established place in the memory of supporters.\n\nAbdul Mumuni: Abdul Ali Mumuni (born 25 August 1973) is a former Ghanaian footballer who played as a forward.  He was the Ghanaian Premier League's top scorer while playing for Dawu Youngstars in the 1991–92 season.  This was the first and only occasion Mumuni was the league's top scorer and the first time Dawu Youngstars had had the league's top scorer.  Mumuni was also capped once for Ghana.\n\nLothar Kobluhn: Lothar Kobluhn (born 12 April 1943) is a German former professional footballer who played as a midfielder.  Kobluhn, who was playing for Rot-Weiß Oberhausen at the time, was the Bundesliga's top scorer in the 1970–71 season, scoring 24 goals.  Kobluhn had to wait 36 years for the top scorer trophy to be awarded because his club at the time, Rot-Weiß Oberhausen, was involved in the Bundesliga scandal.  He finally received his award in 2007.\n\nEbbe Sand: Ebbe Sand (born 19 July 1972) is a Danish former professional footballer who played as a striker for Brøndby IF in Denmark and FC Schalke 04 in Germany.  He was the German Bundesliga top scorer in 2001, and he won the DFB-Pokal in 2001 and 2002 with Schalke.  On the international stage, he represented the Denmark national football team at the 1998 and 2002 FIFA World Cup, as well as the 2000 and 2004 European Championships.  At the 1998 World Cup, he scored the fastest-ever World Cup goal by a substitute – 16 seconds after entering the match.\n\nBobby Tambling: Robert Victor \"Bobby\" Tambling (born 18 September 1941) is an English former professional footballer, who played as a forward, most notably for Chelsea, Crystal Palace and England.  He was Chelsea's all-time top scorer for 47 years, with 202 goals in all competitions until Frank Lampard surpassed this total on 11 May 2013.  Tambling remains Chelsea's all-time top scorer in league competition with 164 goals.  After enjoying a successful career in the Football League during the 1960s and early 1970s, Tambling moved to Ireland.  He subsequently played for several clubs in the League of Ireland and also represented the League of Ireland XI.  After retiring as a player he continued to live in Ireland, residing in Crosshaven, County Cork.\n\nManon Melis: Gabriëlla Maria \"Manon\" Melis (] ; born 31 August 1986) is a Dutch professional footballer who played as a forward for the Seattle Reign FC in the National Women's Soccer League.  Melis has spent most of her career playing in the Swedish Damallsvenskan.  At international level, since making her debut in 2004, she has won over 100 caps and is the all-time top scorer for the Netherlands women's national football team.  She is the daughter of former Feyenoord and ADO Den Haag player Harry Melis.\n\nQuestion: Schalke's top scorer is which Dutch professional footballer born on August 12, 1983?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the player.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the player.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the player.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"team_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team for which the player was top scorer.\"\n        },\n        \"season\": {\n          \"type\": \"string\",\n          \"description\": \"The season in which the player was top scorer for the team.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"season\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"top_scorer_statistics\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"total_goals\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of goals scored by the player in all competitions for the season.\"\n        },\n        \"bundesliga_goals\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of goals scored by the player specifically in the Bundesliga for the season.\"\n        }\n      },\n      \"required\": [\n        \"total_goals\",\n        \"bundesliga_goals\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_details\",\n    \"team_details\",\n    \"top_scorer_statistics\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the player."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the player."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the player."
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_date"
        ],
        "additionalProperties": false
      },
      "team_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the team for which the player was top scorer."
          },
          "season": {
            "type": "string",
            "description": "The season in which the player was top scorer for the team."
          }
        },
        "required": [
          "name",
          "season"
        ],
        "additionalProperties": false
      },
      "top_scorer_statistics": {
        "type": "object",
        "properties": {
          "total_goals": {
            "type": "integer",
            "description": "The total number of goals scored by the player in all competitions for the season."
          },
          "bundesliga_goals": {
            "type": "integer",
            "description": "The number of goals scored by the player specifically in the Bundesliga for the season."
          }
        },
        "required": [
          "total_goals",
          "bundesliga_goals"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_details",
      "team_details",
      "top_scorer_statistics"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
