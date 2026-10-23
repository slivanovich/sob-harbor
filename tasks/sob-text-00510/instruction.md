{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFakhar Zaman (cricketer): Fakhar Zaman (Urdu/Pashto: فخر زمان‎ ; born 10 April 1990) is a Pakistani cricketer who plays for the national team.  He has also played for Lahore Qalandars in the Pakistan Super League.  In August 2017, he was named in Durban Qalandars' squad for the first season of the T20 Global League.\n\nList of Lahore Qalandars cricketers: This is a list of cricketers who have represented Lahore Qalandars in the Pakistan Super League (PSL) since the first season of the PSL in 2016.  Players are listed alphabetically using the standard naming format of their country of origin followed by the year(s) that they have been active as a Lahore player.\n\nLahore Qalandars in 2016: The Lahore Qalandars is a franchise cricket team that represents Lahore in the Pakistan Super League.  They are one of the five teams that had a competition in the 2016 Pakistan Super League.  The team was captained by Azhar Ali, and they stand on fifth position after winning just two matches from their eight matches in the PSL 2016, as a result they were eliminated in group stage.  Umar Akmal with 335 runs in 7 matches was leading run scorer of the tournament.\n\nDurban Qalandars: The Durban Qalandars is a professional franchise Twenty20 cricket team of the T20 Global League in South Africa, which represents the city of Durban.  It is owned by Fawad Rana, a Pakistani businessman who also owns the Lahore Qalandars franchise in Pakistan Super League.  The marquee player of Durban Qalandars is Hashim Amla.  The team logo is similar to Lahore Qalandars logo.\n\nAzhar Ali: Domestically, he has played for Khan Research Laboratories, Lahore, Lahore Eagles, Lahore Lions, Lahore Qalandars, Pakistan A and Huntly (Scotland) during his career.  He was the captain of Lahore Qalandars in the first edition of the Pakistan Super League.\n\nLahore Qalandars in 2017: The Lahore Qalandars is a franchise cricket team that represents Lahore in the Pakistan Super League.  They are one of the five teams that had a competition in the 2017 Pakistan Super League.  The team was captained by Brendon McCullum, and they won three matches from their eight matches in the PSL 2017.  They stand on fifth position and as a result they were eliminated in group stage.\n\nFawad Rana: Fawad Naeem Rana is a Pakistani businessman and franchise owner.  He owns Lahore Qalandars and Durban Qalandars.\n\nLahore Qalandars: Lahore Qalandars (Urdu: ‎ ; Punjabi: ; acronym LQ) is a Pakistani professional cricket franchise which plays in the Pakistan Super League. The Home ground of the team is Gaddafi Stadium. It nominally represents the city of Lahore and the province Punjab in the league.  The team is owned by Qatar Lubricants Company Limited (QALCO). The team is currently captained by Brendon McCullum and coached by Paddy Upton, a former South African cricketer.  Lahore Qalandars was the second most expensive franchise and was one of the few teams sold to an international company.\n\nAamer Yamin: Aamer Yamin (born 26 June 1990) is a Pakistani cricketer.  He was named in Pakistan's Twenty20 International (T20I) squad for their series against England in the UAE in September 2015.  He made his One Day International debut for Pakistan against Zimbabwe on 1 October 2015.  He made his Twenty20 International debut for Pakistan against England on 30 November 2015.  He represented Lahore Qalandars in the second edition of the Pakistan Super League.\n\nPaddy Upton: Patrick Anthony Howard 'Paddy' Upton (born 5 November 1968) is a South African cricket coach and former player.  He has worked as the physical fitness trainer for the South Africa cricket team and the Western Province rugby team.  He has worked as the mental conditioning coach of the India team which became number 1 in the world test rankings and won the ICC World Cup in 2011.  He worked as Performance Director of the South Africa team from 2011-2014, during which time they became the first team to simultaneously hold the world number 1 ranking in all three formats of the game.  He was the head coach of the Rajasthan Royals team in the Indian Premier League from 2012-2015.  Upton is currently the head coach of the Sydney Thunder cricket team in the Australian Big Bash League, and has also been appointed as the head coach of Lahore Qalandars for the Pakistan Super League and now he is the head coach of IPL team Delhi Daredevils.\n\nQuestion: When was Lahore Qalandars coach born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"coach_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Lahore Qalandars coach.\"\n    },\n    \"coach_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the coach.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The full birth date of the coach.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the coach.\"\n    }\n  },\n  \"required\": [\n    \"coach_name\",\n    \"coach_nationality\",\n    \"birth_date\",\n    \"birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "coach_name": {
        "type": "string",
        "description": "The name of the Lahore Qalandars coach."
      },
      "coach_nationality": {
        "type": "string",
        "description": "The nationality of the coach."
      },
      "birth_date": {
        "type": "string",
        "description": "The full birth date of the coach."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the coach."
      }
    },
    "required": [
      "coach_name",
      "coach_nationality",
      "birth_date",
      "birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
