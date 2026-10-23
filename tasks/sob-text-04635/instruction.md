{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMary Joe Fernández: Mary Joe Fernández Godsick (born María José Fernández; August 19, 1971) is an American former professional tennis player.  She reached a career-high ranking of world No. 4 in both singles and doubles.  Fernández was the runner-up in three Grand Slam singles tournaments and won two Grand Slam women's doubles titles and two Olympic gold medals.\n\n2015 US Open – Women's Champions Invitational: Lindsay Davenport and Mary Joe Fernández were scheduled to play Tracy Austin and Gigi Fernández in the final.  However, the match was canceled on 12 September due to rain and was not rescheduled.\n\n1997 WTA German Open: The 1997 WTA German Open was a women's tennis tournament played on outdoor clay courts at the Rot-Weiss Tennis Club in Berlin, Germany that was part of the Tier I categiry of the 1997 WTA Tour.  It was the 26th edition of the tournament and was held from 12 May through 18 May 1997.  Tenth-seeded Mary Joe Fernández won the singles title.\n\n1996 Family Circle Cup – Doubles: Nicole Arendt and Manon Bollegraf were the defending champions but lost in the semifinals to Gigi Fernández and Mary Joe Fernández.\n\n1991 Australian Open – Women's Doubles: Patty Fendick and Mary Joe Fernández won their first career Grand Slam title, defeating Gigi Fernández and Jana Novotná 7–6, 6–1 in the final.\n\n1997 French Open – Women's Doubles: Lindsay Davenport and Mary Joe Fernández were the defending champions, but played this year with different partners.  Davenport teamed up with Jana Novotná and lost in third round to Conchita Martínez and Patricia Tarabini, while Fernández teamed up with Lisa Raymond, losing in the final.\n\nDaniel Nestor: Daniel Mark Nestor {'1': \", '2': \", '3': \", '4': \"} (Serbian Cyrillic: Данијел Несторовић; born September 4, 1972 as Danijel Nestorović) is a Canadian professional tennis player.  He is one of the foremost doubles players in tennis history due to his longevity and continued success at the top of the men's game.  s of 2016 , he is 11th for most men's ATP titles in Open Era history.  In January 2016, Nestor became the first doubles player in ATP history to win 1000 matches.\n\n2014 French Open – Women's Legends Doubles: Lindsay Davenport and Martina Hingis were the defending champions, but Hingis instead competed in the Women's Doubles event.  Davenport played alongside Mary Joe Fernández and was eliminated in the round robin.\n\n1996 French Open – Women's Doubles: Gigi Fernández and Natasha Zvereva were the defending champions, but lost 6–2, 6–1 in the final to Lindsay Davenport and Mary Joe Fernández.  It was the 1st Grand Slam doubles title and the 8th title overall for Davenport, and the 2nd Grand Slam doubles title and the 14th title overall for Fernández, in their respective careers.\n\n2016 US Open – Women's Champions Invitational: Lindsay Davenport and Mary Joe Fernández were scheduled to play Tracy Austin and Gigi Fernández in the previous year's final.  However, the match was canceled on 12 September due to rain and was not rescheduled.\n\nQuestion: Daniel Nestor and Mary Joe Fernández, played which sports to win many titles ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the sport played by the individuals.\"\n    },\n    \"players\": {\n      \"type\": \"array\",\n      \"description\": \"List of players mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"player_name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the player.\"\n          },\n          \"is_professional\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the player is described as a professional in the context.\"\n          }\n        },\n        \"required\": [\n          \"player_name\",\n          \"is_professional\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"context_confirms_many_titles\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the context indicates the players won many titles in the identified sport, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"sport_name\",\n    \"players\",\n    \"context_confirms_many_titles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sport_name": {
        "type": "string",
        "description": "The name of the sport played by the individuals."
      },
      "players": {
        "type": "array",
        "description": "List of players mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "player_name": {
              "type": "string",
              "description": "The full name of the player."
            },
            "is_professional": {
              "type": "boolean",
              "description": "Indicates if the player is described as a professional in the context."
            }
          },
          "required": [
            "player_name",
            "is_professional"
          ],
          "additionalProperties": false
        }
      },
      "context_confirms_many_titles": {
        "type": "boolean",
        "description": "True if the context indicates the players won many titles in the identified sport, false otherwise."
      }
    },
    "required": [
      "sport_name",
      "players",
      "context_confirms_many_titles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
