{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTidal Wave (film): Tidal Wave () is a 2009 South Korean disaster film.  Billed as South Korea's first disaster film, \"Tidal Wave\" is directed by Yoon Je-kyoon and stars Sol Kyung-gu, Ha Ji-won, Park Joong-hoon and Uhm Jung-hwa.\n\nSinking of MV Sewol: The sinking of \"Sewol\" (Hangul: 세월호 침몰 사고 ; Hanja: 世越號沈沒事故 ), also referred to as the \"Sewol Ferry Disaster\", occurred on the morning of 16 April 2014, en route from Incheon to Jeju in South Korea.  The Japanese-built South Korean ferry sank while carrying 476 people, mostly secondary school students from Danwon High School (Ansan City).  The 6,825-ton vessel sent a distress signal from about 2.7 km north off Byeongpungdo at 08:58 Korea Standard Time (23:58 UTC, 15 April 2014).  In total, 304 passengers and crew members died in the disaster.  Of the approximately 172 survivors, more than half were rescued by fishing boats and other commercial vessels that arrived at the scene approximately 40 minutes after the South Korean coast guard.\n\nThe Tower (2012 South Korean film): The Tower (; \"Tower\") is a 2012 South Korean disaster thriller film about a fire that breaks out in a luxury skyscraper in central Seoul on Christmas Eve.  The film is directed by Kim Ji-hoon, and stars Sol Kyung-gu, Kim Sang-kyung and Son Ye-jin in the lead roles.  It was released in theaters on Christmas Day, December 25, 2012.\n\nSaikin-rettō: Saikin-rettō (細菌列島 ) is a 2009 Japanese comedy film.  It stars comedian Naoto Takenaka as \"the General\", the dictator of a fictional Asian country, which parodies the North Korean leader Kim Jong-il.  The film also parodies the 2009 Japanese disaster film \"Pandemic\".\n\nTell Me Something: Tell Me Something () is a 1999 South Korean Thriller-Horror-Crime film directed by Chang Yoon-hyun.  It was an early South Korean film to find success abroad as part of the Korean Wave, and was selected to appear in the 2001 New York Korean Film Festival.\n\nFlu (film): Flu () is a 2013 South Korean disaster film written and directed by Kim Sung-su, about an outbreak of a deadly strain of H5N1 that kills its victims within 36 hours, throwing the district of Budang in Seongnam, with a population of nearly half a million people into chaos.  It stars Jang Hyuk and Soo Ae.\n\nCho Kyuhyun: Cho Kyu-hyun (born February 3, 1988), better known mononymously as Kyuhyun, is a South Korean singer and musical theatre actor.  He is best known as a member of South Korean boy group Super Junior, its sub-groups Super Junior-K.R.Y., Super Junior-M and a former member of the South Korean ballad group S.M. the Ballad.  He is one of the first four Korean artists to appear on Chinese postage stamps.\n\nPark Min-ha (actress): Park Min-ha (born July 2, 2007) is a South Korean actress.  Park began her career as a child actress in 2011, and has appeared in such productions as the South Korean disaster film \"Flu\" (2013), the Korean drama television series \"King of Ambition\" (2013), and the music video for K.Will's song \"Love Blossom\" (2013).  Her father is SBS anchorman Park Chan-min.\n\nPark Min-ha: Park Min-ha () is a Korean name consisting of the family name Park and the given name Min-ha, and may also refer to:\n\nPandora (2016 film): Pandora () is a 2016 South Korean disaster film written and directed by Park Jung-woo, starring Kim Nam-Gil.  The film was released in South Korea on December 7, 2016.\n\nQuestion: What South Korean disaster film did Park Min-ha appear in? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the South Korean disaster film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film, specifically 'disaster film'.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who appeared in the film.\"\n    },\n    \"actor_role_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of role the actor had in their career at the time.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"actor_name\",\n    \"actor_role_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the South Korean disaster film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film, specifically 'disaster film'."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actress who appeared in the film."
      },
      "actor_role_type": {
        "type": "string",
        "description": "The type of role the actor had in their career at the time."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "actor_name",
      "actor_role_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
