{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2000 Toray Pan Pacific Open – Doubles: Lindsay Davenport and Natasha Zvereva were the defending champions, but Davenport did not compete this year.  Zvereva teamed up with Katarina Srebotnik and lost in quarterfinals to Lisa Raymond and Rennae Stubbs.\n\nNatasha Zvereva: Natasha Zvereva, or Zverava, (born Natallya Maratawna Zverava; Belarusian: Наталля Маратаўна Зверава; 16 April 1971) is a former tennis player from Belarus.  Zvereva was the first major athlete in the Soviet Union to demand publicly that she should be able to keep her tournament earnings.  The team of Zvereva and Gigi Fernández won more women's doubles titles and Grand Slam women's doubles championships than any other team since that of Martina Navratilova and Pam Shriver.\n\nKatarina Srebotnik: Katarina Srebotnik (born March 12, 1981) is a Slovenian professional tennis player.  She reached a career-high singles ranking of No. 20 on the Sony Ericsson WTA Tour on August 7, 2006, and a career-high doubles ranking of No. 1 on July 4, 2011.\n\n2016 Aegon International Eastbourne – Doubles: Caroline Garcia and Katarina Srebotnik were the defending champions, but Garcia chose not to participate this year.  Srebotnik played alongside Andreja Klepač, but lost in the first round to Anna-Lena Grönefeld and Květa Peschke.\n\n1999 WTA German Open – Doubles: The 1999 WTA German Open – Singles was the singles event of the fifty-fifth edition of the tennis tournament played at Berlin, Germany, the most prestigious tennis tournament in Latin Europe.  It was the sixth WTA Tier I tournament of the year, and part of the European claycourt season.  Lindsay Davenport and Natasha Zvereva were the defending champions, but only Zvereva participated this year with Mary Pierce.  They were eliminated in the first round by Brie Rippner and Tara Snyder.\n\n1999 Wimbledon Championships – Women's Doubles: The 1999 Wimbledon Championships – Women's Doubles was the women's doubles event of the hundred-and-thirteenth edition of Wimbledon, the third Grand Slam of the year, the most prestigious tournament on grass courts, and the oldest tennis tournament in the world.  Martina Hingis and Jana Novotná were the defending champions but only Novotná competed that year with Natasha Zvereva.  Novotná and Zvereva lost in the semifinals to Mariaan de Swardt and Elena Tatarkova.\n\n1999 Kremlin Cup – Women's Doubles: The 1999 Kremlin Cup – Women's Doubles was the women's doubles event of the fourth WTA edition of the Kremlin Cup; a WTA Tier I tournament and the most prestigious tournament held in Russia.  Mary Pierce and Natasha Zvereva were the defending champions, but Pierce competed this year with Barbara Schett, whereas Zvereva competed with Elena Tatarkova.\n\n1999 Porsche Tennis Grand Prix – Doubles: The 1999 Porsche Tennis Grand Prix – Doubles was the tennis doubles event at the 1999 Porsche Tennis Grand Prix, the twenty-second edition of the most prestigious tournament in Baden-Württemberg.  Lindsay Davenport and Natasha Zvereva were the defending champions, but they did not compete this year.  Davenport competed with Martina Hingis as the first seed, while Zvereva competed with Elena Tatarkova.  Davenport and Hingis withdrew in the quarterfinals due to Davenport having a wrist injury, whilst Tatarkova and Zvereva were knocked out in the first round.\n\n2014 Sony Open Tennis – Women's Doubles: Nadia Petrova and Katarina Srebotnik were the defending champions, but they decided not to participate together.  Petrova was scheduled to play alongside Bethanie Mattek-Sands, but the team withdrew before the first round due to Mattek-Sands's hip injury.  Srebotnik teamed up with Květa Peschke, but they lost in the quarterfinals to Cara Black and Sania Mirza.\n\n1999 Acura Classic – Doubles: The 1999 Acura Classic – Doubles was the doubles event of the twentieth edition of the third tournament in the US Open Series.  Martina Hingis and Natasha Zvereva were the defending champions but Hingis did not compete this year.  Zvereva played with Mary Pierce, and they were defeated in the first time by Cara Black and Irina Selyutina.\n\nQuestion: Who was the first major athlete in the Soviet Union to demand publicly to keep their tournament earnings was Natasha Zvereva or Katarina Srebotnik?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"athlete_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the athlete who made the demand.\"\n    },\n    \"demand_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the demand made by the athlete.\"\n        },\n        \"context\": {\n          \"type\": \"string\",\n          \"description\": \"The specific context or entity where the demand was made (e.g., Soviet Union).\"\n        },\n        \"is_public_demand\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the demand was made publicly.\"\n        }\n      },\n      \"required\": [\n        \"description\",\n        \"context\",\n        \"is_public_demand\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_first_major_athlete\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the athlete was the first major athlete in the specified context to make this demand.\"\n    }\n  },\n  \"required\": [\n    \"athlete_name\",\n    \"demand_details\",\n    \"is_first_major_athlete\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "athlete_name": {
        "type": "string",
        "description": "The name of the athlete who made the demand."
      },
      "demand_details": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string",
            "description": "Description of the demand made by the athlete."
          },
          "context": {
            "type": "string",
            "description": "The specific context or entity where the demand was made (e.g., Soviet Union)."
          },
          "is_public_demand": {
            "type": "boolean",
            "description": "Indicates if the demand was made publicly."
          }
        },
        "required": [
          "description",
          "context",
          "is_public_demand"
        ],
        "additionalProperties": false
      },
      "is_first_major_athlete": {
        "type": "boolean",
        "description": "True if the athlete was the first major athlete in the specified context to make this demand."
      }
    },
    "required": [
      "athlete_name",
      "demand_details",
      "is_first_major_athlete"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
