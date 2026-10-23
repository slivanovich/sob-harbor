{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShahin Kheiri: Shahin Kheiri (born April 20, 1980) is an Iranian footballer who plays for Naft Tehran F.C. in the IPL.\n\nAli Karimi: Ali Karimi (Persian: علی کریمی‎ ‎ ] (born 8 November 1978) is an Iranian coach and retired footballer.  He has played for Fath Tehran, Persepolis, Al-Ahli Dubai, Bayern Munich, Qatar SC, Steel Azin, Schalke 04, Tractor Sazi, and the Iran national team for which he scored 38 goals in 127 appearances.  In 2004, he became the fourth Iranian player to win the Asian Footballer of the Year.  He announced his retirement at the end of the 2013–14 season and, on 11 April 2014, played the final game of his 18-year career.  He is currently manager of Naft Tehran.\n\nFath Tehran F.C.: Fath Tehran F.C. was an Iranian Football club based in Tehran, Iran.  It was the first club of former Bayern Munich midfielder Ali Karimi, and former VfL Bochum striker Vahid Hashemian.\n\nMajid Halvaei: Majid Halvaei (Persian: مجید حلوایی‎ ‎ , born 7 February 1948) is a retired Iranian association football defender.  Between 1970 and 1974 he played 15 international matches, at the 1970 Asian Games, 1972 Summer Olympics and 1972 AFC Asian Cup, which Iran won.  Domestically he mostly stayed with PAS Tehran F.C.\n\nQaani: Mirza Habibollah Shirazi, known as Qaani, is one of the most famous poets of the Qajar era.  He was born in 1223 AH in Shiraz, where he attended elementary school.  At an early age, Qaani went to Mashhad for further study.  He wrote a poem to praise Fath Ali Shah Qajar during the former's visit to Tehran, and called him \"mojtahed o sho'ara\".\n\nKamiar Ghanbari: Kamiar Ghanbari (Persian: کامیار قنبری‎ ‎ ; born 1988 in Tehran) is an Iranian football defender who currently plays for Persepolis F.C. in Iran's Premier Football League.  He is a talented left footed defender who can play in the left back and central defender position.  He has represented Iran in most youth levels.  He left the PAS Tehran F.C. youth system at the beginning of 2007 at the age of 19 after being approved by Hamid Estili he put pen to paper to a contract keeping him at Persepolis until 2010.\n\nMohammad Panjali: Seyed Mohammad Panjali Qomi (born July 26, 1955 in Tehran, Iran) is a retired Iranian footballer and a football coach.  He played for Bargh Tehran, Fath Tehran, F.C. Aboomoslem, Persepolis FC, Al-Ittihad and the Iran national football team, where he made 45 appearances.  He usually played in the defender position.  He was also team manager of Persepolis from 1993 until 1994.\n\nShahid Dastgerdi Stadium: The Shahid Dastgerdi Stadium (also known as PAS Tehran Stadium) (Persian: ورزشگاه شهيد دستگردی‎ ‎ ) is a football stadium located in the Ekbatan area of Tehran, Iran.  It was named after a casualty of the Iran–Iraq War.  It is the former home of PAS Tehran F.C. and now hosts the Iran national under-20 football team.\n\nVahid Hashemian: Vahid Hashemian (Persian: وحيد هاشميان‎ ‎ , born 21 July 1976) is a retired Iranian footballer and current coach.\n\nJader da Silva Brazeiro: Jader da Silva Brazeiro (born February 21, 1984) is a Brazilian footballer who plays for Naft Tehran F.C. in the Iran Pro League.\n\nQuestion: Former Fath Tehran F.C. member, Vahid Hashemian, was born in what year? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the person was born.\"\n    },\n    \"former_club\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former football club mentioned in the question.\"\n    },\n    \"is_retired_footballer\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the person is a retired footballer.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"birth_year\",\n    \"former_club\",\n    \"is_retired_footballer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "birth_year": {
        "type": "integer",
        "description": "The year the person was born."
      },
      "former_club": {
        "type": "string",
        "description": "The name of the former football club mentioned in the question."
      },
      "is_retired_footballer": {
        "type": "boolean",
        "description": "Indicates if the person is a retired footballer."
      }
    },
    "required": [
      "person_name",
      "birth_year",
      "former_club",
      "is_retired_footballer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
