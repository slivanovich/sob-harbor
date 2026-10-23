{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichael Ballack: Michael Ballack (] ; born 26 September 1976) is a retired German footballer.  He is among the top goal scorers in the history of the German national team.  Ballack wore the number 13 shirt for every team he has played for, save for 1.  FC Kaiserslautern.  He was selected by Pelé as one of FIFA's 125 Greatest Living Players, and as the UEFA Club Midfielder of the Year in 2002.  He won the German Footballer of the Year award three times – in 2002, 2003 and 2005.  Ballack was known for his passing range, powerful shot, physical strength and commanding presence in midfield.\n\nWolfgang Kolczyk: Wolfgang Kolcyk (born 21 August 1971) is a retired German footballer who played his entire career for Hertha BSC, most of it for the reserves.  He played one season for the first team.  He was also part of the reserve team that made the final of the German Cup in 1993.\n\nThomas Ritter: Thomas Ritter (born 10 October 1967 in Görlitz) is a retired German footballer.  He played one game for Germany on 13 October 1993 in a friendly against Uruguay, as a substitute for Stefan Effenberg.\n\nStephan Straub: Stefan Straub (born 25 January 1971 in Tübingen) is a retired German footballer who last played for Alemannia Aachen in the 2nd Bundesliga.\n\nKarsten Baumann: Karsten Baumann (born 14 October 1969) is a retired German footballer who last managed Hansa Rostock.\n\nLorenz-Günther Köstner: Lorenz-Günther Köstner (born 30 January 1952) is a retired German footballer who is now a football manager who last managed Fortuna Düsseldorf.  Following the sacking of Armin Veh on 25 January 2010, he was named interim manager of VfL Wolfsburg until 30 June 2010.\n\nStefan Müller (footballer, born 1974): Stefan Müller (born 8 March 1974 in Schopfheim) is a retired German footballer.  He spent his entire career with SC Freiburg, joining the club in 1993, and making his debut the following season as the club went on to finish third in the Bundesliga.  He played a further ten seasons for the club, eight of which were at the highest level – Freiburg were relegated in 1997 and 2002, but bounced back immediately on both occasions.  In total he made 203 league appearances for the club, scoring 12 times before retiring in 2005.  He won five caps for German under-21 team in the mid-1990s.\n\nStefan Effenberg: Stefan Effenberg (] ; born 2 August 1968) is a retired German footballer who last managed SC Paderborn.  A midfielder, he possessed leadership skills, fantastic passing range, powerful shooting ability, physical strength, but also a fearsome and controversial character.\n\nUli Hoeneß: Ulrich \"Uli\" Hoeneß (] ; born 5 January 1952) is the president of German football club Bayern Munich and a retired German footballer who played as a forward for club and country.  Hoeneß represented Germany at one World Cup and two European Championships, winning one tournament in each competition.\n\nStefan Wessels: Stefan Wessels (born 28 February 1979) is a retired German footballer who played as a goalkeeper.\n\nQuestion: Thomas Ritter  is a retired German footballer who played one game for Germany in 1993 against Uruguay, as a substitute for Stefan Effenberg, a retired German footballer who last managed what club?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the footballer.\"\n    },\n    \"player_status\": {\n      \"type\": \"string\",\n      \"description\": \"The current status of the footballer (e.g., retired).\"\n    },\n    \"last_managed_club\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the last club managed by the footballer.\"\n    },\n    \"player_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role of the individual (e.g., footballer, manager).\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"player_status\",\n    \"last_managed_club\",\n    \"player_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the footballer."
      },
      "player_status": {
        "type": "string",
        "description": "The current status of the footballer (e.g., retired)."
      },
      "last_managed_club": {
        "type": "string",
        "description": "The name of the last club managed by the footballer."
      },
      "player_role": {
        "type": "string",
        "description": "The primary role of the individual (e.g., footballer, manager)."
      }
    },
    "required": [
      "player_name",
      "player_status",
      "last_managed_club",
      "player_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
