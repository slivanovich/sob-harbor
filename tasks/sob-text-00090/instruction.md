{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlf Garnett: Alfred Edward \"Alf\" Garnett is a fictional character from the British sitcom \"Till Death Us Do Part\" and its follow-on and spin-off series \"Till Death...\" and \"In Sickness and in Health\".  Alf also starred in the chat show \"The Thoughts of Chairman Alf\".  The character was created by Johnny Speight and played by Warren Mitchell.\n\nList of ALF episodes: The following is a list of episodes of the American sitcom \"ALF\".  Most episode titles derive from those of American and British popular songs.\n\nBenji Gregory: Benji Gregory (born Benjamin Gregory Hertzberg; May 26, 1978) is a former American actor.  He is best known for playing the role of Brian Tanner on the sitcom \"ALF\".\n\nMax Wright: George Edward Maxwell Wright (born August 2, 1943), credited professionally as Max Wright, is an American actor, best known for his role as Willie Tanner on the sitcom \"ALF\".\n\nTanner Smith (basketball): Tanner James Smith (born March 30, 1990) is a former American professional basketball player for MHP Riesen Ludwigsburg in the Basketball Bundesliga in Germany and a former basketball player for Clemson University and Landstede Basketball in the Netherlands.  He currently serves as the Director of Basketball Operations for the Charlotte 49ers Basketball Team.  He has been noted by such sources as The Post and Courier, The Times and Democrat, and The Atlanta Journal-Constitution for founding Tanner’s Totes, an organization that helps to cheer up children and teenagers with cancer through donations of large tote bags filled with toys and other recreational items.  Tanner's Totes have delivered to hospitals in 25 states across the US.  Over 3000 totes have been delivered.  Smith has also been interviewed by ESPN in print and in televised interviews and has been featured on the ABC special \"Everyday Health\".\n\nElmo Tanner: William Elmo Tanner, known as Elmo Tanner (August 8, 1904 – December 20, 1990) was an American whistler, singer, bandleader and disc jockey, best known for his whistling on the chart-topping song “Heartaches” with the Ted Weems Orchestra.  Tanner and Weems recorded the song for two different record companies within a period of five years.  Neither recording was successful originally.  The song became a hit for both record companies after a Charlotte, North Carolina disk jockey played it at random in 1947.\n\nALF (TV series): ALF is an American sitcom that aired on NBC from September 22, 1986, to March 24, 1990.\n\nProject ALF: Project: ALF (also known as Project: ALF, Part 2) is a 1996 American made-for-television science fiction film directed by Dick Lowry which serves as a sequel to the final episode \"Consider Me Gone\" of the 1986–1990 sitcom \"ALF\".  It was broadcast in the U.S. by ABC and in Canada on CHCH on February 17, 1996.  The film was released on DVD in 2005.\n\nAlf's Hit Talk Show: ALF's Hit Talk Show was an American cable television talk show that aired on TV Land in 2004 for seven episodes.  The host is the puppet character ALF, of 1980s television fame.  At the beginning of each show, ALF is introduced by his \"sidekick\", Ed McMahon.  The show ran in a 30-minute block and featured guests such as Drew Carey and Joe Mantegna.  Prior to the series' debut, \"Entertainment Weekly\" described \"ALF's Hit Talk Show\" as \"a one-shot, a lead-in\" for TV Land's marathon of the original \"ALF\" sitcom.\n\nAnne Schedeen: Luanne Ruth Schedeen (born January 8, 1949), known professionally as Anne Schedeen, is an American actress who was born in Portland, Oregon.  She is best known for her role as Kate Tanner on \"ALF,\" which ran from 1986 to 1990.\n\nQuestion: Who starred as Brian Tanner in the 1990 American sitcom ALF?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played the character.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"tv_series_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the TV series.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the TV series.\"\n        },\n        \"air_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the TV series started airing.\"\n        },\n        \"air_end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the TV series stopped airing.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"genre\",\n        \"air_start_year\",\n        \"air_end_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"character_name\",\n    \"tv_series_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played the character."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "tv_series_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the TV series."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the TV series."
          },
          "air_start_year": {
            "type": "integer",
            "description": "The year the TV series started airing."
          },
          "air_end_year": {
            "type": "integer",
            "description": "The year the TV series stopped airing."
          }
        },
        "required": [
          "title",
          "genre",
          "air_start_year",
          "air_end_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "character_name",
      "tv_series_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
