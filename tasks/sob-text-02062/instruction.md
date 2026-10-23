{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLindsay Davenport: Lindsay Ann Davenport Leach (born June 8, 1976) is an American former professional tennis player.  She was ranked World No. 1 on eight different occasions, for a total of 98 weeks.  Davenport is one of five women who have been the year-end World No. 1 at least four times (1998, 2001, 2004, and 2005) since 1975; the others are Chris Evert, Steffi Graf, Martina Navratilova and Serena Williams.  She has achieved the No. 1 ranking in doubles as well.\n\nOlga Zaitseva (tennis): Olga Zaitseva (born 12 March 1962) is a former competitor for the Soviet Union at the 1979, 1980, 1981 and 1983 editions of the Federation Cup.  Despite posting doubles victories over top professionals such as Betty Stöve, Hana Mandlíková and Renáta Tomanová, Zaitseva did not compete at any point on the women's professional tennis circuit or at any of the Grand Slams and thus never attained a world ranking.\n\nBettie Serveert: Bettie Serveert are a Dutch indie rock band.  Their name translates to \"Bettie Serves\", or \"Service to Bettie\", which is the title of a book written by Dutch tennis player Betty Stöve, who made it to the Wimbledon ladies singles final in 1977.\n\nJoAnne Russell: JoAnne Russell (born October 30, 1954) is an American former professional tennis player.  With playing partner Helen Gourlay Cawley, she won the Wimbledon Ladies' Doubles title in 1977.  They beat the team of Chris Evert and Rosie Casals in the first round and the top-ranked team of Martina Navratilova and Betty Stöve in the final (6–3, 6–3).  Russell reached a career-high singles ranking of No. 22.\n\n1973 Dutch Open (tennis): The 1973 Dutch Open was a combined men's and women's tennis tournament staged in Hilversum, Netherlands.  The men's event was part of the Grand Prix circuit and categorized in Group C.  The tournament was played on outdoor clay courts and was held from 16 July to 23 July 1973.  It was the 17th edition of the tournament.  Tom Okker and Betty Stöve won the singles titles.\n\n1999 Porsche Tennis Grand Prix – Doubles: The 1999 Porsche Tennis Grand Prix – Doubles was the tennis doubles event at the 1999 Porsche Tennis Grand Prix, the twenty-second edition of the most prestigious tournament in Baden-Württemberg.  Lindsay Davenport and Natasha Zvereva were the defending champions, but they did not compete this year.  Davenport competed with Martina Hingis as the first seed, while Zvereva competed with Elena Tatarkova.  Davenport and Hingis withdrew in the quarterfinals due to Davenport having a wrist injury, whilst Tatarkova and Zvereva were knocked out in the first round.\n\nBetty Stöve: Betty Stöve (born 24 June 1945) is a Dutch former professional tennis player.  She is best remembered for reaching the ladies' singles final at Wimbledon in 1977.  She also won ten Grand Slam titles in women's doubles and mixed doubles.\n\n1976 Toray Sillook Open: The 1976 Toray Sillook Open was a women's tennis tournament played on indoor carpet courts in Tokyo, Japan that was a non-tour event, independent of the 1976 WTA Tour.  It was the fifth edition of the tournament and was held from 28 September through 2 October, 1976.  The first round was played at the Nichi Dai University Auditorium while the semifinals and final were held at the Yoyogi National Gymnasium.  The singles event was the only competition held and was won by unseeded Betty Stöve who earned $15,000 first-prize money.\n\nFred McNair: Frederick V. McNair IV (born July 22, 1950 in Washington, D.C.) is a former professional tennis player from the United States who reached the World No. 1 doubles ranking in 1976.  That year, he teamed up with Sherwood Stewart to capture the men's doubles titles at French Open, the German Open and the Masters.  McNair was also a mixed doubles runner-up at the French Open in 1981, partnering Betty Stöve.  In 1978, he was a member of the US team that won the Davis Cup.  In nine years on the professional tour, McNair won 16 doubles titles.  His career-high singles ranking was World No. 67.\n\n1980 US Open – Women's Doubles: Betty Stöve and Wendy Turnbull were the defending champions but they competed with different partners that year, Stöve with Pam Shriver and Turnbull with Rosemary Casals.\n\nQuestion: Who was born first, Betty Stöve or Lindsay Davenport?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_one_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first tennis player.\"\n    },\n    \"player_one_birth_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The birth date of the first tennis player in YYYY-MM-DD format.\"\n    },\n    \"player_two_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second tennis player.\"\n    },\n    \"player_two_birth_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The birth date of the second tennis player in YYYY-MM-DD format.\"\n    },\n    \"player_born_first_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the player who was born first.\"\n    },\n    \"birth_year_difference\": {\n      \"type\": \"integer\",\n      \"description\": \"The difference in birth years between the two players.\"\n    }\n  },\n  \"required\": [\n    \"player_one_name\",\n    \"player_one_birth_date\",\n    \"player_two_name\",\n    \"player_two_birth_date\",\n    \"player_born_first_name\",\n    \"birth_year_difference\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_one_name": {
        "type": "string",
        "description": "The name of the first tennis player."
      },
      "player_one_birth_date": {
        "type": "string",
        "format": "date",
        "description": "The birth date of the first tennis player in YYYY-MM-DD format."
      },
      "player_two_name": {
        "type": "string",
        "description": "The name of the second tennis player."
      },
      "player_two_birth_date": {
        "type": "string",
        "format": "date",
        "description": "The birth date of the second tennis player in YYYY-MM-DD format."
      },
      "player_born_first_name": {
        "type": "string",
        "description": "The name of the player who was born first."
      },
      "birth_year_difference": {
        "type": "integer",
        "description": "The difference in birth years between the two players."
      }
    },
    "required": [
      "player_one_name",
      "player_one_birth_date",
      "player_two_name",
      "player_two_birth_date",
      "player_born_first_name",
      "birth_year_difference"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
