{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSteven Gerrard: Steven George Gerrard {'1': \", '2': \", '3': \", '4': \"} (born 30 May 1980) is an English professional football coach and former professional footballer who serves as an academy coach at Liverpool.  He spent the majority of his playing career as a central midfielder for Liverpool and the England national team, with most of that time spent as club captain.  Regarded as one of the greatest midfielders of his generation, Gerrard was awarded the UEFA Club Footballer of the Year award in 2005, and the Ballon d'Or Bronze Award.  In 2009, Zinedine Zidane and Pelé said that they considered Gerrard to be the best footballer in the world.  A versatile and well-rounded player, highly regarded for his leadership, Gerrard is the only footballer in history to score in an FA Cup Final, a League Cup Final, a UEFA Cup Final and a UEFA Champions League Final, winning on each occasion.\n\nHugo Sánchez: Hugo Sánchez Márquez (born 11 July 1958) is a retired Mexican professional footballer and manager, who played as a forward.  A prolific goalscorer known for his spectacular strikes and volleys, Sánchez is widely regarded as Mexico's greatest-ever footballer, and one of the greatest players of his generation.  In 1999, the International Federation of Football History and Statistics voted Sánchez the 26th best footballer of the 20th century, and the best footballer from the CONCACAF region.  In 2004 Sánchez was named in the FIFA 100 list of the world's greatest living players.  He is the fourth highest scorer in the history of Spain's top division, and is the sixth highest goalscorer in Real Madrid's history.\n\nBest Footballer in Asia 2015: The 2015 Best Footballer in Asia, given to the best football player in Asia as judged by a panel of 20 sports journalists, was awarded to Son Heung-min on the 28th December, 2015.  Son Heung-min became the first footballer who won Best Footballer in Asia for more than one time, and the first footballer who won this trophy in succession.\n\nBest Footballer in Asia: Best Footballer in Asia () is an annual association football award organized and presented by Titan Sports.  It is awarded to the player who had the best performance for Asian football during the previous calendar year.\n\nBest Footballer in Asia 2014: The 2014 Best Footballer in Asia, given to the best football player in Asia as judged by a panel of sports journalists, was awarded to Son Heung-min on 28th.  November, 2014.\n\nOleksandr Zavarov: Oleksandr Anatoliyovych Zavarov, also spelt Aleksandr Anatoljević Zavarov (Ukrainian: Олександр Анатолійович Заваров , Russian: Заваров, Александр Анатольевич ) – (born 26 April 1961 in Luhansk, Ukrainian SSR) is a former Ukrainian football midfielder and the former head coach at FC Arsenal Kyiv.  In 1986, he was named the best footballer in the USSR and Ukraine and the 6th best footballer in Europe according to France Football.  Zavarov is widely regarded to be among the greatest footballers in the history of the USSR and Ukraine, and in 2000 he was included in the Ukrainian Team of The Century according to a poll by the \"Ukrainsky Futbol\" weekly.\n\nShinji Okazaki: Shinji Okazaki (岡崎 慎司 , Okazaki Shinji , born 16 April 1986) is a Japanese footballer who plays for Leicester City and the Japan national team as a forward.\n\nBest Footballer in Asia 2013: The Best Footballer in Asia 2013 was the inaugural Best Footballer in Asia.  Based upon the voting of a panel of 22 journalists the winner was Keisuke Honda.  On March 16, 2014, the trophy was conferred to Keisuke Honda by Luo Ming, the deputy chief editor of Titan Sports in San Siro stadium.\n\nBest Footballer in Asia 2016: The 2016 Best Footballer in Asia, given to the best football player in Asia as judged by a panel of 38 sports journalists, was awarded to Shinji Okazaki on Dec 26th, 2016.\n\nSouth American Footballer of the Year: The Rey del Fútbol de América (\"King of Football of America\"), often referred to as the South American Footballer of the Year, is an annual association football award presented to the best footballer in South America over the previous calendar year.  The award was conceived by Venezuelan newspaper \"El Mundo\", which awarded it from 1971 to 1985.  Uruguayan newspaper \"El País\" took over from 1986 onwards.\n\nQuestion: The 2016 Best Footballer in Asia was awarded to a footballer born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"award_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football award.\"\n    },\n    \"award_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the award was given.\"\n    },\n    \"winner_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"player_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the player who won the award.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the award-winning player.\"\n        }\n      },\n      \"required\": [\n        \"player_name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"award_name\",\n    \"award_year\",\n    \"winner_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "award_name": {
        "type": "string",
        "description": "The name of the football award."
      },
      "award_year": {
        "type": "integer",
        "description": "The year the award was given."
      },
      "winner_details": {
        "type": "object",
        "properties": {
          "player_name": {
            "type": "string",
            "description": "The name of the player who won the award."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the award-winning player."
          }
        },
        "required": [
          "player_name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "award_name",
      "award_year",
      "winner_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
