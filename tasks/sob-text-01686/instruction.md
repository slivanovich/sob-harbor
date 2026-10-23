{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMyreside Stadium: Myreside Stadium is a sports ground that is used by Edinburgh Rugby for most of its home matches.  Often simply known as Myreside, Watsonians RFC have used this venue on the east side of Myreside Road as their home ground for rugby union matches since 1933.  Edinburgh Rugby played six Pro12 matches at the stadium in 2017 and following this agreed to play at the stadium for a further three seasons, which will include some Pro14 and European Rugby Challenge Cup matches.  A main stand is positioned along the west side of the grass pitch, with floodlights around the ground.  Ahead of the Edinburgh Rugby team's return to play home matches at the stadium, temporary stands were installed to increase seating capacity to 5,500.\n\nEstádio Municipal João Lamego Netto: Estádio Municipal João Lamego Netto, usually known as Lamegão, is a multi-purpose stadium in Ipatinga, Brazil.  It is currently used mostly for football matches.  Ideal futebol Clube usually play their home matches at the stadium.  Social Futebol Clube, from the neighbor city Coronel Fabriciano, has its own stadium, but sometimes plays its home matches at Ipatingão, because of its larger capacity and better structure.  The stadium has a current maximum capacity of 10,000 people and was built in 1982.\n\nAl Kuwait Sports Club Stadium: Al Kuwait Kaifan Stadium is a multi-purpose stadium in Kuwait City, Kuwait.  It is currently used mostly for football matches and hosts the home matches of Al Kuwait Kaifan.  The stadium holds 18,500.  This stadium had also hosted Kuwait's national team matches during the 2010 FIFA World Cup qualification, which they failed to reach.  The stadium hosted the final matches of the Kuwait Emir Cup and Kuwait Crown Cup for the last 5 seasons.  This stadium also hosted matches for the national team during the 1974 Gulf Cup of Nations, were Kuwait won their third title after winning 4-0 against Saudi Arabia.\n\nArena Barueri: Arena Barueri is a multi-use stadium located in Barueri, São Paulo state, Brazil.  It is used mostly for football matches and hosts the home matches of Sport Club Barueri, and hosted the matches of Grêmio Recreativo Barueri until the 2010 season.  The stadium has a maximum capacity of 31,452 people and was built in 2007.  It is owned by the City of Barueri.  During the reforming of Palestra Italia Stadium the Barueri Arena was being used for some home matches of Palmeiras.\n\nEstádio José de Melo: Estádio José de Melo, sometimes called Stadium José de Melo, is a multi-use stadium located in Rio Branco, Brazil.  It is used mostly for football matches and hosts the home matches of Andirá Esporte Clube, Atlético Acreano, Independência Futebol Clube, Atlético Clube Juventus, Rio Branco Football Club and Associação Desportiva Vasco da Gama.  It also hosted the home matches of América-AC The stadium has a maximum capacity of 8,000 people and was built in 1929 (according to some sources, it was inaugurated in 1935).  The stadium is owned by Rio Branco Football Club and is named after the commissioner José Francisco de Melo, who is a former player and former president of Rio Branco Football Club.  He also donated the groundplot where the stadium was built.\n\nEverton L.F.C.: Everton Ladies Football Club are a women's association football team from the city of Liverpool, who compete in the FA WSL 1, the first division of women's football in England.  Formed in 1983 as Hoylake W.F.C., they are now part of Everton F.C. but play their home games at the Select Security Stadium, previously known as Halton Stadium in Widnes, home of Widnes Vikings.  The team have won the Premier League National Division once, the Premier League Cup once, and the FA Women's Cup twice.  From 2002 until 2012 they were managed by former captain Mo Marley and are now managed by former Assistant Manager Andy Spence.\n\nWidnes Vikings: Widnes Vikings R.L.F.C. is an English professional rugby league club based in Widnes, Cheshire which currently plays in the Super League, the top tier of European rugby league.  The club plays its home matches at the Select Security Stadium.\n\nSelect Security Stadium: The Select Security Stadium (historically known as Lowerhouse Lane and Naughton Park) is a rugby league stadium in Widnes, Cheshire, England.  Widnes Vikings play their home games there.  The stadium is all seater and has a total capacity of 13,350.\n\nDanny Mills (rugby league): Danny Mills is a professional rugby league player for Batley.  His position is Wing .  He formerly played for Huddersfield, Doncaster, Widnes and Sheffield Eagles.\n\nList of Glamorgan County Cricket Club grounds: Glamorgan County Cricket Club was established on 6 July 1888.  The county entered the Minor Counties Championship in 1896 and competed in the competition until 1920, after which it was elevated to first-class status for the 1921 season, and has played first-class cricket since.  Following their elevation to first-class status, Glamorgan alternated their home matches between Cardiff Arms Park in Cardiff and St Helen's in Swansea.  It wasn't until 1966 that Glamorgan began playing at their current home ground, the SWALEC Stadium (known more commonly as Sophia Gardens) in Cardiff.  Cardiff Arms Park played host to Glamorgan's first home fixture in first-class cricket against Sussex in 1921, as well as its first home List A fixture against Worcestershire in 1963.  Forty years later Sophia Gardens played host to the clubs first Twenty20 fixture against Northamptonshire.  Glamorgan have played home matches at nineteen grounds, but have played the majority of their home fixtures since 1966 at the SWALEC Stadium, which also holds Test, One Day International and Twenty20 International cricket matches.\n\nQuestion: What team did Danny Mills play for that has home matches at Select Security Stadium \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the rugby league player.\"\n    },\n    \"stadium_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the stadium in question.\"\n    },\n    \"teams_player_played_for\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of teams the player formerly played for.\"\n    },\n    \"stadium_home_teams\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"team_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the team that plays home matches at the stadium.\"\n          },\n          \"sport\": {\n            \"type\": \"string\",\n            \"description\": \"The sport the team plays.\"\n          }\n        },\n        \"required\": [\n          \"team_name\",\n          \"sport\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of teams that use the stadium for home matches.\"\n    },\n    \"matching_team\": {\n      \"type\": \"string\",\n      \"description\": \"The team that satisfies both conditions: played for by the player and plays home matches at the stadium.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"stadium_name\",\n    \"teams_player_played_for\",\n    \"stadium_home_teams\",\n    \"matching_team\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the rugby league player."
      },
      "stadium_name": {
        "type": "string",
        "description": "The name of the stadium in question."
      },
      "teams_player_played_for": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of teams the player formerly played for."
      },
      "stadium_home_teams": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "team_name": {
              "type": "string",
              "description": "The name of the team that plays home matches at the stadium."
            },
            "sport": {
              "type": "string",
              "description": "The sport the team plays."
            }
          },
          "required": [
            "team_name",
            "sport"
          ],
          "additionalProperties": false
        },
        "description": "A list of teams that use the stadium for home matches."
      },
      "matching_team": {
        "type": "string",
        "description": "The team that satisfies both conditions: played for by the player and plays home matches at the stadium."
      }
    },
    "required": [
      "player_name",
      "stadium_name",
      "teams_player_played_for",
      "stadium_home_teams",
      "matching_team"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
