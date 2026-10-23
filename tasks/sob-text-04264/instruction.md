{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRadhi Shenaishil: Radhi Shenaishil Swadi (Arabic: راضي شنيشل سوادي‎ ‎ ; born 11 August 1966) is a former Iraqi footballer and former coach of the Iraq national football team.\n\nHabib Jafar: Habib Jafar (Arabic: حبيب حعفر‎ ‎ ) (born July 1, 1966) is a former Iraqi footballer.  He was featured on the national team many times and is remembered for competing in various Gulf Cup competitions.  In the 1988 Gulf Cup, he was voted as the best player of the competition.  He became a regular of the national team at a young age and was almost even called up for the 1986 World Cup in Mexico, but he was thought to be to unexperienced by then-coach, Evaristo de Macedo.\n\n1986 FIFA World Cup Group B: Group B of the 1986 FIFA World Cup was one of the groups of nations competing at the 1986 FIFA World Cup.  The group's first round of matches began on June 3 and its last matches were played on June 11.  Matches were played at the Estadio Azteca in Mexico City and at the Estadio Nemesio Díez in Toluca.  Host Mexico topped the group, joined in the second round by Belgium and by Paraguay, who were making their first appearance in the finals since 1958.  Iraq, making their debut in the World Cup, lost all three of their matches.\n\nManuel Rosas: Manuel Rosas Sánchez (April 17, 1912 in Mexico City – February 20, 1989), nicknamed \"Chaquetas\", was a Mexican footballer who participated in the 1930 FIFA World Cup.  He was the first player in the history of FIFA World Cup who scored a goal from the penalty kick spot (against Argentina).  With the first goal he scored during the World Cup, he became at the time the youngest player to have scored in the FIFA World Cup, a record later broken by Pelé, although Rosas remains second youngest.  He was also the first Mexican player to score multiple goals in world cup play (the first to score more than two goals was Luis Hernandez, 68 years later) and the first player to score a own goal in the history of FIFA World Cup (against Chile).\n\nAhmed Radhi: Ahmed Radhi Amaiesh Al-Salehi (Arabic: أحمد راضي هميش الصالحي‎ ‎ , born on 21 March 1964 in Baghdad, Iraq, but originally from Basra) is a former Iraqi footballer who played as a forward.  Widely regarded as Iraq's best player of all-time, Radhi scored the only Iraqi goal in the 1986 FIFA World Cup, a low shot to the corner of the net against Belgium in the 2–1 defeat.  He was voted the 1988 Asian Footballer of the Year.\n\nKarim Saddam: Karim Saddam Menshid (born 26 May 1960) is an Iraqi football forward who played for Iraq in the 1986 FIFA World Cup.  He also played for many Iraqi clubs : Al Jaish, Al Zawraa, Al Shorta & Al Sinaa, Karim Saddam had been Top scorer of Iraqi League for 4 times.  He scored unforgettable goal against UAE in 1986 FIFA World Cup Qualification which secured Iraq to go throw to the next stage .\n\nHussein Saeed: Hussein Saeed Mohammed Al-Ubaidi (Arabic: حسين سعيد محمد العبيدي‎ ‎ , born 21 January 1958 in Al Adhamiya, Baghdad) is a retired Iraqi footballer who played as a forward for the Iraqi Premier League club Al-Talaba and the Iraqi national team and is a former president of the Iraq Football Association.  Saeed is in 4th place in the list of top international association goal scorers, with 78 goals.  Along with Ahmed Radhi, he is considered to be the best Iraqi player of the 20th century and features in 25th place in Asia's Best Players of the Century list.  On 24 April 1987, Saeed broke Falah Hassan's record to become the most capped Iraqi player with 110 caps.  Hussein is currently the Iraqi national team's highest scoring player with 78 goals.\n\nEdwin Picon-Ackong: Edwin Sydney Picon-Ackong (born November 4, 1940) is a retired Mauritian football referee.  He is known for having refereed one match in the 1986 FIFA World Cup in Mexico between Iraq and Paraguay.  This match caused controversy as Picon-Ackong blew the whistle for half time a split-second before Iraq striker Ahmed Radhi's header hit the back of the net, and the goal was ruled out.  Picon-Ackong received a lot of criticism for blowing the whistle when Iraq had such a big goalscoring opportunity.\n\n1986 FIFA World Cup: The 1986 FIFA World Cup, the 13th FIFA World Cup, was held in Mexico from 31 May to 29 June 1986.  The tournament was the second to feature a 24-team format.  With European nations not allowed to host after the previous World Cup in Spain, Colombia had been originally chosen to host the competition by FIFA but, largely due to economic reasons, was not able to do so and officially resigned in 1982.  Mexico was selected as the new host in May 1983.  This was the third FIFA World Cup tournament in succession that was hosted by a Hispanophonic country, after Spain in 1982, and Argentina in 1978.\n\nMahir Habib Radhi: Mahir Habib Radhi (born 19 June 1977) is a former Iraqi football defender and is currently the assistant manager of Al-Shorta.  He also played for Al-Shorta and scored the winning goal in the 2001 Umm Al Ma'arik Cup final.  He played for the Iraqi national team in the 2000 AFC Asian Cup.\n\nQuestion: Ahmed Radhi Amaiesh Al-Salehi, is a former Iraqi footballer who played as a forward, widely regarded as Iraq's best player of all-time, Radhi scored the only Iraqi goal in the 1986 FIFA World Cup, was held in Mexico, from which time span?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the footballer mentioned in the question.\"\n    },\n    \"world_cup_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the FIFA World Cup was held.\"\n    },\n    \"host_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country that hosted the FIFA World Cup.\"\n    },\n    \"tournament_start_date\": {\n      \"type\": \"string\",\n      \"description\": \"The start date of the FIFA World Cup tournament.\"\n    },\n    \"tournament_end_date\": {\n      \"type\": \"string\",\n      \"description\": \"The end date of the FIFA World Cup tournament.\"\n    },\n    \"player_achievement\": {\n      \"type\": \"string\",\n      \"description\": \"The specific achievement of the player in the mentioned World Cup.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"world_cup_year\",\n    \"host_country\",\n    \"tournament_start_date\",\n    \"tournament_end_date\",\n    \"player_achievement\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the footballer mentioned in the question."
      },
      "world_cup_year": {
        "type": "integer",
        "description": "The year the FIFA World Cup was held."
      },
      "host_country": {
        "type": "string",
        "description": "The country that hosted the FIFA World Cup."
      },
      "tournament_start_date": {
        "type": "string",
        "description": "The start date of the FIFA World Cup tournament."
      },
      "tournament_end_date": {
        "type": "string",
        "description": "The end date of the FIFA World Cup tournament."
      },
      "player_achievement": {
        "type": "string",
        "description": "The specific achievement of the player in the mentioned World Cup."
      }
    },
    "required": [
      "player_name",
      "world_cup_year",
      "host_country",
      "tournament_start_date",
      "tournament_end_date",
      "player_achievement"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
