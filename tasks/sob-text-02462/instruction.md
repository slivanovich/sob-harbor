{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDal-ja's Spring: Dal-ja's Spring () is a 2007 South Korean romantic comedy television series starring Chae Rim, Lee Min-ki, Lee Hyun-woo, Lee Hye-young and Gong Hyung-jin.  It aired on KBS2 from January 3 to March 15, 2007 on Wednesdays and Thursdays at 21:55 for 22 episodes.\n\nBoys Over Flowers (TV series): Boys Over Flowers () is a 2009 South Korean television series starring Lee Min-ho, Ku Hye-sun, Kim Hyun-joong (of SS501), Kim Bum, Kim Joon (of T-Max) and Kim So-eun.  It aired on KBS2 from January 5 to March 31, 2009 on Mondays and Tuesdays at 22:00 for 25 episodes.\n\nAnju Kurian: Anju Kurian is an Indian film actress, mainly acted in Malayalam films.  Best known for her role in the 2016 Malayalam film \"Kavi Uddheshichathu\".  She started her career through Malayalam film industry by doing a supporting role in the movie Neram which directed by Alphonse Puthren.  The followed year she played a supporting cast Ohm Shanthi Oshaana and became famous through the supporting role in the big hit movie Premam.\n\nLee Hye-young (actress, born 1962): Lee Hye-young (born November 25, 1962) is a South Korean actress.  She is the daughter of celebrated film director Lee Man-hee, who died in 1975 when she was in middle school.  Lee began her acting career in 1981 at the age of 17 through a local musical theatre production of \"The Sound of Music\".  Since then she has performed in theater, feature and short films, and television.  She was one of the most prominent South Korean actresses in the 1980s, starring in films such as \"The Blazing Sun\" (1985), \"Winter Wanderer\" (1986), \"Ticket\" (1986), \"The Age of Success\" (1988), \"North Korean Partisan in South Korea\" (1990), \"Fly High Run Far\" (1991), \"Passage to Buddha\" (1993), and \"No Blood No Tears\" (2002).  Lee also played supporting roles in the Korean dramas \"I'm Sorry, I Love You\" (2004), \"Fashion 70's\" (2005) and \"Boys Over Flowers\" (2009).\n\nShriya Saran filmography: Shriya Saran is an Indian actress and model who has acted mostly in Telugu, Tamil and Hindi language films.  She made her acting debut with the Telugu film \"Ishtam\" (2001) and had her first commercial success with \"Santosham\" (2002).  The following year, she made her Hindi cinema debut with a supporting role in \"Tujhe Meri Kasam\", alongside Ritesh Deshmukh and Genelia D'Souza.  It was followed by the commercially successful crime drama \"Tagore\" (2003), in which she was paired opposite Chiranjeevi.  The same year, she played a supporting role in the Tamil-Telugu bilingual film \"Enakku 20 Unakku 18\", which marked her debut in Tamil cinema.  In 2005, she had ten releases including \"Mazhai\", S. S. Rajamouli's \"Chhatrapati\", and \"Mogudu Pellam O Dongodu\", in which she was among the only three characters of the film.  Saran's solitary release as a lead actress in 2006 was the Tamil film \"Thiruvilaiyaadal Aarambam\".\n\nBob Frazer: Bob Frazer (born 1971) is an award winning actor, born in Ontario.  He currently lives in British Columbia.  He has appeared in many roles both on stage and in television, and has won multiple Jessie Richardson Theatre Awards, including: \"Outstanding Performance by an Actor in a Leading Role\" (2005–2006) for his role in \"Hamlet\", \"Outstanding Performance by an Actor in a Supporting Role\" (2005–2006) for his role in \"Prodigal Son\", and won for \"Significant Artistic Achievement\" (2003–2004).  He has also been a nominee over ten times including \"Outstanding Performance by an Actor in a Supporting Role\" (2003–2004) for \"The Glass Menagerie\"; Iago in Shakespeare's \"Othello\"; and as Antipholus of Ephesus in \"Comedy of Errors\" during the 2009 season of Bard on the Beach.\n\nLee Hye-young: Lee Hye-young () is a Korean name consisting of the family name Lee and the given name Hye-young, and may also refer to:\n\nQueen of Housewives: Queen of Housewives (; also known as My Wife Is a Superwoman) is a 2009 South Korean romantic comedy television series, starring Kim Nam-joo, Oh Ji-ho, Yoon Sang-hyun, Lee Hye-young, Choi Cheol-ho, and Sunwoo Sun.  It depicts the life of \"naejo,\" housewives who devote their entire lives to their husbands' success, but with a more comedic and aggressive twist.  It aired on MBC from March 16 to May 19, 2009 on Mondays and Tuesdays at 21:55 for 20 episodes.\n\nLee Hye-young (actress, born 1971): Lee Hye-young (born December 22, 1971) is a South Korean actress, singer and businesswoman.  As a singer in the 1990s, Lee released two dance music albums each with 1730 and Coco, and one album as a solo artist.  When she switched to acting, Lee starred in television series such as \"Premonition\" (1997), \"Dal-ja's Spring\" (2007) and \"Queen of Housewives\" (2009), and also founded the fashion brand Miss Dorothy.\n\nKatie Cassidy: Katherine Evelyn Anita Cassidy (born November 25, 1986) is an American actress.  After initially appearing in minor television roles, she made her film debut in \"When a Stranger Calls\" (2006).  During the same year, she also had her first starring role as Kelli Presley in \"Black Christmas\" (2006).  In 2007, Cassidy gained attention for her role as Ruby on the supernatural-horror television series \"Supernatural\", during its third season.  She later had a supporting role in \"Taken\".  In 2009, Cassidy became a cast member of the series \"Harper's Island\" and \"Melrose Place\", both of which lasted for only one season.  During 2010, she had a supporting role as Kris Fowles in \"A Nightmare on Elm Street\" and a recurring role during the fourth season of \"Gossip Girl\".\n\nQuestion: Which station did the film that Lee Hye-young played a supporting role in air on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"actress_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the actress.\"\n    },\n    \"production_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the TV series or film.\"\n        },\n        \"production_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of production (e.g., TV series, film).\"\n        },\n        \"role_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of role played by the actress (e.g., starring, supporting).\"\n        },\n        \"airing_station\": {\n          \"type\": \"string\",\n          \"description\": \"The television station on which the production aired.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"production_type\",\n        \"role_type\",\n        \"airing_station\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"actress_birth_year\",\n    \"production_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "actress_birth_year": {
        "type": "integer",
        "description": "The birth year of the actress."
      },
      "production_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the TV series or film."
          },
          "production_type": {
            "type": "string",
            "description": "The type of production (e.g., TV series, film)."
          },
          "role_type": {
            "type": "string",
            "description": "The type of role played by the actress (e.g., starring, supporting)."
          },
          "airing_station": {
            "type": "string",
            "description": "The television station on which the production aired."
          }
        },
        "required": [
          "title",
          "production_type",
          "role_type",
          "airing_station"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actress_name",
      "actress_birth_year",
      "production_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
