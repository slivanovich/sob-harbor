{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSnake in the Eagle's Shadow: Snake in the Eagle's Shadow () is a 1978 Hong Kong martial arts action film directed by Yuen Woo-ping in his directorial debut, and starring Jackie Chan, Hwang Jang Lee and Yuen Woo-ping's real life father, Yuen Siu Tien.\n\nLegend of a Fighter: Legend of a Fighter is a 1982 Hong Kong martial arts film based on the story of Chinese martial artist Huo Yuanjia (Cantonese: Fok Yuen-gap).  Directed by Yuen Woo-ping, the film starred Bryan Leung as the lead character.\n\nEastern Condors: Eastern Condors () is a 1987 Hong Kong action film directed by Sammo Hung, who also starred in the lead role.  The film co-stars Yuen Biao, Joyce Godenzi, Yuen Wah, Lam Ching-ying, Yuen Woo-ping, Corey Yuen and Billy Chow.  The film was released in the Hong Kong on 9 July 1987.\n\nBryan Leung: Bryan Leung Kar-yan (born 20 January 1949) is a Hong Kong film and television actor and film director who has played roles in numerous acclaimed martial arts films.  He is affectionately known as \"Beardy\" due to his trademark facial hair.  He also has characteristic hyper-extendable fingers, which can be observed when he has his palms open and his fingers outstretched.  Despite being one of the most well-known faces in Hong Kong action cinema, he had no formal martial arts training, relying on his talents at mimicry to imitate the moves shown to him by the action directors.\n\nHero (1997 film): Hero () is a 1997 Hong Kong martial arts film written and directed by Corey Yuen.  The film stars Taiwanese-Japanese actor Takeshi Kaneshiro, established Hong Kong action stars from the Peking Opera School (Yuen Biao, Yuen Wah, Corey Yuen, Yuen Tak) and Hong Kong actresses Valerie Chow and Jessica Hsuan.  \"Hero\" is a remake of the 1972 film, \"Boxer from Shantung\".  The film was produced by then TVB chairwoman Mona Fong.\n\nYuen Woo-ping: Yuen Woo-ping (; born 1945) is a Chinese martial arts choreographer and film director, renowned as one of the most successful and influential figures in the world of Hong Kong action cinema.  He is one of the inductees on the Avenue of Stars in Hong Kong.  Yuen is also a son of Yuen Siu-tien, a renowned martial arts film actor.\n\nDuncan Jones: Duncan Zowie Jones ( ; born 30 May 1971) is an English film director, film producer, and screenwriter.  He is best known for directing the science fiction film \"Moon\" (2009), winning the BAFTA Award for Outstanding Debut by a British Writer, Director or Producer, \"Source Code\" (2011) and \"Warcraft\" (2016).  He is the son of late English singer David Bowie and American model Angie Bowie.\n\nTrue Legend: True Legend is a 2010 Chinese martial arts film directed by Yuen Woo-ping, starring Vincent Zhao, Zhou Xun, Jay Chou, Michelle Yeoh, Andy On, David Carradine, Guo Xiaodong, Feng Xiaogang, Cung Le, Gordon Liu, Bryan Leung and Jacky Heung.  This was Yuen Woo-ping's first film directing since 1996's \"Tai Chi Boxer\".\n\nSammo Hung: Sammo Hung (born 7 January 1952), also known as Hung Kam-bo (洪金寶), is a Hong Kong actor, martial artist, film producer and director, known for his work in many martial arts films and Hong Kong action cinema.  He has been a fight choreographer for other actors such as Jackie Chan, King Hu and John Woo.\n\nDrunken Master: Drunken Master () is a 1978 Hong Kong comedy martial arts film directed by Yuen Woo-ping, and starring Jackie Chan, Yuen Siu-tien, and Hwang Jang Lee.  The film was a success at the Hong Kong box office, earning two and a half times the amount of Chan's previous film, \"Snake in the Eagle's Shadow\", which was also considered a successful film.  It is an early example of the comedic kung fu genre for which Jackie Chan became famous.  The film popularised the Zui Quan (\"drunken fist\") fighting style.  Ranked number 3 on totalfilm.com's 50 greatest kung fu movies of all time.\n\nQuestion: Who is a Chinese martial arts choreographer and film director, renowned as one of the most successful and influential figures in the world of Hong Kong action cinema, Duncan Jones or Yuen Woo-ping ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_identified\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified from the description.\"\n    },\n    \"roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professional roles held by the identified person.\"\n    },\n    \"notable_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the person's renown or influence.\"\n    },\n    \"is_hong_kong_action_cinema_figure\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the person is a significant figure in Hong Kong action cinema.\"\n    },\n    \"other_candidate_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other candidate mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"person_identified\",\n    \"roles\",\n    \"notable_description\",\n    \"is_hong_kong_action_cinema_figure\",\n    \"other_candidate_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_identified": {
        "type": "string",
        "description": "The name of the person identified from the description."
      },
      "roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professional roles held by the identified person."
      },
      "notable_description": {
        "type": "string",
        "description": "A description of the person's renown or influence."
      },
      "is_hong_kong_action_cinema_figure": {
        "type": "boolean",
        "description": "Indicates if the person is a significant figure in Hong Kong action cinema."
      },
      "other_candidate_name": {
        "type": "string",
        "description": "The name of the other candidate mentioned in the question."
      }
    },
    "required": [
      "person_identified",
      "roles",
      "notable_description",
      "is_hong_kong_action_cinema_figure",
      "other_candidate_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
