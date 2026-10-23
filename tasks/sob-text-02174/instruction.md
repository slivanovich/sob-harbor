{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nYutaka Akita: Yutaka Akita (秋田 豊 , Akita Yutaka , born August 6, 1970) is a former Japanese football player and manager.  He played for Japan national team.  He was on the Japan national team at the 1998 and 2002 FIFA World Cup.\n\nHisashi Kato: Hisashi Kato (加藤 久 , Kato Hisashi , born April 24, 1956) is a former Japanese football player and manager.  He played for Japan national team.  He made 61 appearances for the senior Japan national team from 1978 to 1987, including 7 matches in the 1986 FIFA World Cup qualifying rounds.\n\nNoritada Saneyoshi: Noritada Saneyoshi (實好 礼忠 , Saneyoshi Noritada , born October 19, 1972) is a former Japanese football player and manager.  He spent his entire senior career at Gamba Osaka.  He was a member of the Japan national football team at the 1993 Summer Universiade.\n\nYasuharu Sorimachi: Yasuharu Sorimachi (反町 康治 , Yasuharu Sorimachi , born March 8, 1964) is a former Japanese football player and manager who currently manages Japanese club Matsumoto Yamaga FC.  A midfielder, He played for Japan national team 4 times between 1990 and 1991.  At club level, he scored 23 goals from 188 appearances in the domestic leagues.  He subsequently became a manager and has worked for Albirex Niigata, Shonan Bellmare and Japan national under-23 football team.\n\nMasakuni Yamamoto: Masakuni Yamamoto (山本 昌邦 , Yamamoto Masakuni , born April 4, 1958) is a former Japanese football player.  He played for Japan national team.  He is currently a commentator of football match program of NHK.  He coached Japan national team at 1997 FIFA World Youth Championship and 2004 Summer Olympics.\n\nKunishige Kamamoto: Kunishige Kamamoto (釜本 邦茂 , Kamamoto Kunishige , born April 15, 1944) is a former Japanese football player.  He won the bronze medal with the Japan national team at the 1968 Summer Olympics in Mexico City, Mexico, finishing as the tournament's top scorer with seven goals.  Kamamoto is often considered to be the greatest Japanese football player of all-time.\n\nFootball at the Summer Universiade: Men's Association football was a Summer Universiade sport from the 1979 edition.  In the 1979 edition, it was an optional sport.  From 1985, football was a recognized mandatory sport.  The women's football competition began in the 1993 edition.\n\nSaburō Kawabuchi: Saburō Kawabuchi (川淵 三郎 , Kawabuchi Saburō ) is a former Japanese football player and manager of Japan national football team.  He is the founder and the honorable chairman of the Japan Professional Soccer League.  Between 2002 and 2008 he served as president of the Japan Football Association.\n\nAkihiro Nishimura (footballer): Akihiro Nishimura (西村 昭宏 , Nishimura Akihiro , born August 8, 1958) is a former Japanese football player and manager.  He played for Japan national team.  He managed U-20 Japan national football team at the 2001 FIFA World Youth Championship in Argentina.\n\nKazushi Kimura: Kazushi Kimura (木村 和司 , Kimura Kazushi , born July 19, 1958) is a former Japanese football player.  He played for Japan national team.  He made 54 appearances and scored 26 goals for the Japan national football team from 1979 to 1986.\n\nQuestion: Noritada Saneyoshi, is a former Japanese football player and manager, in 1993, he was a member of which Japan national football team?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the football player.\"\n    },\n    \"year_of_membership\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the player was a member of the team.\"\n    },\n    \"team_type\": {\n      \"type\": \"string\",\n      \"description\": \"The general type of the national football team.\"\n    },\n    \"tournament_or_event\": {\n      \"type\": \"string\",\n      \"description\": \"The specific tournament or event the team participated in.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"year_of_membership\",\n    \"team_type\",\n    \"tournament_or_event\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the football player."
      },
      "year_of_membership": {
        "type": "integer",
        "description": "The year the player was a member of the team."
      },
      "team_type": {
        "type": "string",
        "description": "The general type of the national football team."
      },
      "tournament_or_event": {
        "type": "string",
        "description": "The specific tournament or event the team participated in."
      }
    },
    "required": [
      "player_name",
      "year_of_membership",
      "team_type",
      "tournament_or_event"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
