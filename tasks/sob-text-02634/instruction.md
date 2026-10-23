{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJamaica: Jamaica ( ) is an island country situated in the Caribbean Sea, consisting of the third-largest island of the Greater Antilles.  The island, 10,990 sqkm in area, lies about 145 km south of Cuba, and 191 km west of Hispaniola (the island containing the countries of Haiti and the Dominican Republic).  Jamaica is the fourth-largest island country in the Caribbean, by area.\n\nMappillai (1989 film): Mappillai (English: Son-in-law ) is a 1989 Tamil action comedy film directed by Rajasekhar starring Rajinikanth and Amala in lead roles.  It is a remake of Telugu film \"Athaku Yamudu Ammayiki Mogudu\", the Tamil version was produced by Geetha Arts, and Chiranjeevi who played the lead role in the original telugu version made a special appearance in this film.  The film opened to positive response from the public and was a Mega hit Blockbuster movie ran 200 days at the Box-office history of Tamil cinema 890 shows were houseful, all the credits once again goes to superb mass style acting approach of Superstar Rajinikanth.  The film was remade again in Tamil under the same name.\n\nList of companies of Jamaica: Jamaica is an island country situated in the Caribbean Sea, consisting of the third-largest island of the Greater Antilles.  The island, 10,990 sqkm in area, lies about 145 km south of Cuba, and 191 km west of Hispaniola (the island containing the nation-states of Haiti and the Dominican Republic).  Jamaica is the fourth-largest island country in the Caribbean, by area.\n\nSri Lanka: Sri Lanka ( or ; Sinhalese: ශ්‍රී ලංකා \"Śrī Laṃkā \", Tamil: இலங்கை \"Ilaṅkai\"), officially the Democratic Socialist Republic of Sri Lanka, is an island country located southeast of the Republic of India and northeast of the Maldives.  Its current existence is due to the merger of several empires present on the island under European colonial rule.\n\nThushaaram: Thushaaram is a 1981 Malayalam-language Indian feature film directed I. V. Sasi, starring Ratheesh, Seema, Rani Padmini and Jose.  The movie ran more than 75 days .\n\nEzhumalai: Ezhumalai is an Indian Tamil language action-drama film directed and acted by Arjun in the titular character.  It features Arjun, Simran, Gajala, Mumtaj in lead roles.  The Film is the remake of Telugu Blockbuster \"Narasimha Naidu\" starring Balakrishna, Mukesh Rishi.  This movie was later dubbed in Telugu again as \"Simhabaludu\".  Despite citing mixed reviews at the time of release, this movie ran well and had good box office collections.\n\nRan Kevita 2: Ran Kevita 2, distributed as \"Ran Kevita II - Gopaluge Wickrama\" in CEL and NFC Theatres, (Sinhalese: \"රන් කෙවිට 2\" ) is a 2013 Sri Lankan Sinhala children's fantasy film directed by Udayakantha Warnasuriya and co-produced by Pravin Jayarathne, Ranjith Jayasooriya, Janitha Marasinghe and Udayakantha Warnasuriya.  It is the sequel to 2009 film \"Ran Kevita\" directed by the same director.  It stars Hisham Samsudeen and Harith Samarasinghe in lead roles along with Ananda Wickramage and Asela Jayakody.  Music composed by Mahesh Denipitiya.  It is the 1192nd Sri Lankan film in the Sinhala cinema.\n\nRan Kevita: Ran Kevita, (Sinhalese: \"රන් කෙවිට\" ) is a 2007 Sri Lankan Sinhala children's fantasy film directed by Udayakantha Warnasuriya and co-produced by Pravin Jayarathne, Dilman Jayaratne, Janith Marasinghe and Udayakantha Warnasuriya for Millenium Entertainments.  Its sequel film \"Ran Kevita 2\" directed by the same director released in 2013.  It stars Hisham Samsudeen in lead role along with Vijaya Nandasiri and Srinath Maddumage.  Music composed by Sangeeth Wickramasinghe.  It is the 1084th Sri Lankan film in the Sinhala cinema.\n\nVeerappa Nayaka: Veerappa Nayaka is an Indian Kannada language film directed by S. Narayan starring Vishnuvardhan and Shruti in the lead roles.  It is a story of a Gandhian's son turning into a terrorist.  This was also the first film in Vishnuvardhan and Narayan's combination and the movie ran for 30 weeks at the box office.\n\nBai Chali Sasariye: Bai Chali Sasariye is a 1988 Rajasthani language film.  The movie ran for 100 days and thus created a history in Rajasthan cinema.\n\nQuestion: What island country is the movie Ran Kevita from \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"origin_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the movie is from.\"\n    },\n    \"country_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_island_country\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the origin country is an island country.\"\n        }\n      },\n      \"required\": [\n        \"is_island_country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"origin_country\",\n    \"country_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "origin_country": {
        "type": "string",
        "description": "The country where the movie is from."
      },
      "country_attributes": {
        "type": "object",
        "properties": {
          "is_island_country": {
            "type": "boolean",
            "description": "Indicates if the origin country is an island country."
          }
        },
        "required": [
          "is_island_country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "movie_title",
      "origin_country",
      "country_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
