{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEe Snehatheerathu: Ee Snehatheerathu or Saamam is a 2004 Malayalam film directed by Prof. Sivaprasad and written by Dr. Ramakrishnan, starring Kunchacko Boban, Lal, Nedumudi Venu and Jagathy Sreekumar.  Kunchacko Boban won the Special Jury Award at the Kerala State Film Awards for this movie.\n\nVeruthe Oru Bharya: Veruthe Oru Bharya (English: A Wife for Nothing) is a 2008 Malayalam film written by K. Gireesh Kumar and directed by Akku Akbar.  The film stars Jayaram, Gopika and Nivetha Thomas in the lead roles.\n\nMayilpeelikkavu: Mayilpeelikkavu is a Malayalam film released in 1998 starring Kunchacko Boban and Jomol.  This is the third film of Kunchacko Boban.  The film is about re-incarnation and revenge.This movie is a remake of English film Dead Again.\n\nKunchacko Boban: Kunchacko Boban (born 2 November1976) is an Indian film actor and producer who appears in Malayalam films.  He is the grandson of producer Kunchacko, who established the film production studio Udaya Pictures.\n\nBharya Athra Pora: Bharya Athra Pora is a 2013 Malayalam family film, directed by Akku Akbar, starring Jayaram and Gopika in the lead roles.  The cast and crew of 2008 film \"Veruthe Oru Bharya\" came together for making the film which is not a sequel to the first film.\n\nKadhalukku Mariyadhai: Kadhalukku Mariyadhai (English: \"Respect for love\" ) is a 1997 Tamil romantic musical film directed by Fazil.  It starred Shalini and Vijay in the lead roles with Sivakumar, Srividya and Manivannan playing other supporting roles.  The film became a blockbuster soon after release and was dubbed by critics as a \"classic\", with the lead pair in the film profiting from the widespread success.  The film was a remake of Fazil's successful Malayalam film, \"Aniathipravu\", which featured Kunchacko Boban and Shalini in the lead roles.\n\nAniyathipraavu: Aniyathipraavu (English: \"Younger Sister Dove\") is a 1997 Malayalam musical-romance film directed by Fazil and produced by Swargachitra Appachan.  It stars Kunchacko Boban and Shalini in the lead roles.  The film tells the story of Sudhish Kumar (Kunchacko Boban) and Mini (Shalini) who fall in love despite being from two different religious communities.  The film explores love, relationships and the various aspects to them.  The music was composed by Ouseppachan with the lyrics by S. Ramesan Nair.\n\nNiveda Thomas: Nivetha Thomas is an Indian film actress known for her natural acting style.  She has acted in various Tamil, Malayalam, and Telugu films.  She is well known for her role in the 2008 Malayalam film \"Veruthe Oru Bharya\" and won the Kerala State Film Award for Best Child Artist for her performance.  She made her debut as a leading actress in Telugu cinema with the 2016 film \"Gentleman\", which won her critical acclaim and recognition.\n\nNiram: Niram (English: \"Colour\") is a 1999 Malayalam Romantic film directed by Kamal, starring Kunchacko Boban and Shalini in the lead roles.  The film is about a special friendship between a boy and girl, Aby (Kunchacko Boban) and Sona (Shalini).  The film's music was composed by Vidyasagar.\n\nRomans (2013 film): Romans is a 2013 Malayalam comedy thriller film directed by Boban Samuel.  The film is produced by Arun Ghosh and Bijoy Chandran under the banner Chand V Creations.  The film stars Kunchacko Boban, Biju Menon and Niveda Thomas in the lead roles, along with Lalu Alex, T. G. Ravi, Nelson Sooranad, Kalabhavan Shaju, Kochu Preman, and Vijayaraghavan in supporting roles.  The movie is an unofficial remake of 1989 American comedy film We're No Angels, directed by Neil Jordan.\n\nQuestion: The actress known for her rolle in Veruthe Oru Bharya  also starred with Kunchacko Boban in a Malayalam remake of what film by Neil Jordan?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"known_for_film\": {\n          \"type\": \"string\",\n          \"description\": \"The film the actress is known for, as per the question.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"known_for_film\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"malayalam_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the Malayalam film where the actress co-starred with Kunchacko Boban.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the Malayalam film.\"\n        },\n        \"co_star\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the co-star mentioned in the question.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"co_star\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"original_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the original film by Neil Jordan that was remade.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the original film.\"\n        },\n        \"original_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the original film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"director\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actress_details\",\n    \"malayalam_film_details\",\n    \"original_film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "known_for_film": {
            "type": "string",
            "description": "The film the actress is known for, as per the question."
          }
        },
        "required": [
          "name",
          "known_for_film"
        ],
        "additionalProperties": false
      },
      "malayalam_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the Malayalam film where the actress co-starred with Kunchacko Boban."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the Malayalam film."
          },
          "co_star": {
            "type": "string",
            "description": "The name of the co-star mentioned in the question."
          }
        },
        "required": [
          "title",
          "co_star"
        ],
        "additionalProperties": false
      },
      "original_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the original film by Neil Jordan that was remade."
          },
          "director": {
            "type": "string",
            "description": "The director of the original film."
          },
          "original_release_year": {
            "type": "integer",
            "description": "The release year of the original film."
          }
        },
        "required": [
          "title",
          "director"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actress_details",
      "malayalam_film_details",
      "original_film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
