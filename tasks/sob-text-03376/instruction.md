{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCanoeing at the 2014 Summer Youth Olympics: Canoeing at the 2014 Summer Youth Olympics is scheduled to be held between August 23 to August 27.  The events will take place at the Nanjing Rowing-Canoeing School in Nanjing, China.\n\nNanking Massacre: The Nanking Massacre was an episode of mass murder and mass rape committed by Japanese troops against the residents of Nanjing (\"Nanking\"), then the capital of the Republic of China, during the Second Sino-Japanese War.  The massacre is also known as the Rape of Nanking or, using Pinyin romanization, the Nanjing Massacre or Rape of Nanjing.\n\nDon't Cry, Nanking: Don't Cry, Nanking, also known as \"Nanjing 1937\" (), is a 1995 Chinese film about the 1937 Nanking Massacre committed by the Imperial Japanese Army in the former capital city Nanjing, China.\n\nAniversario: Never Compromise: Aniversario: Never Compromise was a professional wrestling internet pay-per-view (iPPV) event produced by the Chikara promotion, that took place on June 2, 2013, at the Trocadero Theatre in Philadelphia, Pennsylvania.  The event marked Chikara's fourth iPPV, third to take place at the Trocadero Theatre and the promotion's only event to take place in Philadelphia in 2013.  Much like the previous iPPV, Under the Hood, Aniversario: Never Compromise also aired through Smart Mark Video.  Aniversario: Never Compromise celebrated Chikara's eleventh anniversary and was the first anniversary event to take place on iPPV; in the past, the promotion had celebrated its anniversaries with weekends of two shows.  The event saw all three Chikara championships being defended with one title change, where Pieces of Hate (Jigsaw and The Shard) defeated 3.0 (Scott Parker and Shane Matthews) for the Campeonatos de Parejas.  Another major match during the event saw former Campeones de Parejas, Amasis and Ophidian, end their nineteen-month storyline rivalry in a Sarcophagus match.  The event concluded with a major storyline development, where Chikara's authority figure Wink Vavasseur ended the event and shut down the promotion, while the main event was still going on in the ring, leading to the promotion going inactive for a full year.\n\nDragons of the Dwarven Depths: Dragons of the Dwarven Depths is a fantasy novel by Margaret Weis and Tracy Hickman, set in the \"Dragonlance\" fictional campaign setting.  It is the beginning of the Lost Chronicles trilogy, designed to fill in the gaps in the storyline between the books in the \"Chronicles trilogy\" (\"Dragons of Autumn Twilight\", \"Dragons of Winter Night\", and \"Dragons of Spring Dawning\").  The events in the book take place between the events of \"Dragons of Autumn Twilight\" and \"Dragons of Winter Night\".  While parts of the book foreshadow some of the events to take place in the Dragonlance Legends trilogy, the novel is otherwise free of spoilers.\n\nAthletics at the 2014 Summer Youth Olympics: Athletics at the 2014 Summer Youth Olympics was held from August 20 to August 26.  The events will take place at the Nanjing Olympic Sports Center in Nanjing, China.\n\nLindenstraße: Lindenstraße (literally \"Lime Street\") is a German television drama series, broadcast by Das Erste.  The first episode aired on 8 December 1985 and since then new episodes have aired weekly.  Its current timeslot on Das Erste is Sundays at 18:50.  The events of the Sunday episode usually take place on the Thursday before the show, based on the TV station's original plan of airing the episodes Thursday night.  Prior of the start of the show, the timeslot was switched to Sunday evening but the Thursday remained the day the events usually take place as the show shall feature the daily life routine of the protagonists on a working day.  Exceptions are the so-called holiday episodes that take place on Sunday, such as for Christmas and Easter and also on important election days (especially the election to the German Bundestag).\n\nTennis at the 2014 Summer Youth Olympics: Tennis at the 2014 Summer Youth Olympics were held on 17–24 August.  The events will take place at the Nanjing Sport Institute in Nanjing, China.\n\n2016 WTA 125K series: The WTA 125K series is the secondary professional tennis circuit organised by the Women's Tennis Association.  The 2016 WTA 125K series calendar consists of eight tournaments, each with a total prize fund of $125,000.  After 2015, the Nanchang event was upgraded to a WTA International level tournament, and with new events starting in San Antonio, West Hempstead and Bol.  The planned tournament in West Hempstead was then cancelled, and the tournament scheduled to take place in Carlsbad, California was moved to Oahu, Hawaii.  Following the death of the Thai king Bhumibol Abdulyadej, the event due to take place in Hua Hin was also cancelled, in accordance with Thai tradition that sporting events cannot take place in the month after a monarch's death.\n\nBoxing at the 2014 Summer Youth Olympics: Boxing at the 2014 Summer Youth Olympics was held from August 23 to August 27.  The events took place at the Nanjing International Expo Center in Nanjing, China.  For the first time three female boxing events will take place at the Youth Olympics.\n\nQuestion: During what war do the events in the film \"Nanjing 1937\" take place?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"alternative_title\": {\n          \"type\": \"string\",\n          \"description\": \"An alternative title for the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the film was released.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"alternative_title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"historical_event_depicted\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the historical event depicted in the film.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the historical event took place.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"war_context\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the war during which the events depicted in the film occurred.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"historical_event_depicted\",\n    \"war_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "alternative_title": {
            "type": "string",
            "description": "An alternative title for the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          }
        },
        "required": [
          "title",
          "alternative_title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "historical_event_depicted": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the historical event depicted in the film."
          },
          "year": {
            "type": "integer",
            "description": "The year the historical event took place."
          }
        },
        "required": [
          "name",
          "year"
        ],
        "additionalProperties": false
      },
      "war_context": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the war during which the events depicted in the film occurred."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_details",
      "historical_event_depicted",
      "war_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
