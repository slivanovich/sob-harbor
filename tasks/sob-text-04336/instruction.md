{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRosario Dawson: Rosario Isabel Dawson (born May 9, 1979) is an American actress, producer, singer, comic book writer, and political activist.  She made her film debut in the 1995 teen drama \"Kids\".  Her subsequent film roles include \"He Got Game\", \"Men in Black II\", \"25th Hour\", \"Rent\", \"Sin City\", \"Death Proof\", \"Seven Pounds\", \"\", and \"Top Five\".  Dawson has also provided voice-over work for Disney and DC.\n\nRachael Leigh Cook: Rachael Leigh Cook (born October 4, 1979) is an American actress, model, voice artist, and producer, who is best known for her starring role in films \"She's All That\" (1999), \"Josie and the Pussycats\" (2001), and the television series \"Into the West\" and \"Perception\", as well as being the voice behind various characters in \"Robot Chicken\" and Tifa Lockhart in the English version of \"\".\n\nJosie and the Pussycats (film): Josie and the Pussycats is a 2001 American musical comedy film released by Universal Pictures, and Metro-Goldwyn-Mayer.  Directed and co-written by Harry Elfont and Deborah Kaplan, the film is loosely based upon the Archie comic of the same name, as well as the Hanna-Barbera cartoon.  The film is about a young all-female band which signs a record contract with a New York City record label, only to discover that the company does not have the musicians' best interests at heart.  The film stars Rachael Leigh Cook, Tara Reid, and Rosario Dawson as the Pussycats, with Alan Cumming, Parker Posey, and Gabriel Mann in supporting roles.  The film received mixed reviews and was a box office bomb, earning about $15 million against a $39 million budget.\n\nSoher Al Bably: Soheir Al Bably (Arabic: ‎ ‎ ; born 14 February 1935) is an Egyptian actress born in Damietta.  After completing secondary school, she attended the Institute of Theatrical Arts.  ٍShe starred in the play \"Madrast Al-Mushaghebeen\" in 1973, and also in a stage version of the life of Raya and Sakina in 1985.  She married four times, and her second husband was Mounir Mourad.\n\nJackie Joseph: Jackie Joseph (born Sammie Jacqueline Joseph; November 7, 1933) is an American character actress, voice artist, and writer known for portraying Alan Brady's niece Jackie on the \"Dick van Dyke Show\", as well as the film characters of: Audrey Fulquard in the original \"The Little Shop of Horrors\" (1960), Sheila Futterman in \"Gremlins\" (1984) and \"\" (1990), Mrs Kirkland in \"\" (1985) and \"\" (1987), and the voice of Melody in the animated series \"Josie and the Pussycats\" and \"Josie and the Pussycats in Outer Space\".\n\nSherry Alberoni: Sharyn Eileen \"Sherry\" Alberoni (born December 4, 1946) is an American actress and voice artist.  Alberoni got her start as a Mouseketeer on the weekday ABC television program \"The Mickey Mouse Club\".  As an adult, she became a voice artist for Hanna-Barbera Productions.  Besides providing voices for numerous incidental characters in series such as \"Jeannie\", Alberoni is best known as the voice of nasty rich-girl Alexandra Cabot from \"Josie and the Pussycats\" , \"superhero-in-training\" Wendy from the first season of \"Super Friends\", the heroic robot, Bo in \"Mighty Orbots\" and Glumdalclitch in \"The Three Worlds of Gulliver\".  In 1971, she starred alongside Patty Andrews in the Sherman Brothers stage musical, \"Victory Canteen\".\n\nRachel Devirys: Rachel Devirys (28 February 1890 - 16 May 1983) was a French film actress born in the Crimea, Russian Empire (now Ukraine).  She starred in some 50 films between 1916 and 1956.\n\nIrene Montalà: Irene Montalà is a Spanish actress born in the district of Nou Barris of Barcelona.  She is the daughter of Mercè Montalà.  She studied interpretation with Txiki Berrando and Manuel Lillo.  She has also studied dancing and singing.  Her mother tongues are Spanish and catalan, although she has also studied English and french.  She started as an actress in series \"Poblenou\" (TV3).  In 2001, she starred in the film \"Fausto 5.0\".  In 2002, she participated in the series <nowiki>\"Por Palabras\"</nowiki> like Barbara which in the end it wasn't finished.  In 2004 she appeared in an episodic way in the series \"Cuéntame como pasó\" (La 1), where she played the role of Mila.\n\nSuet Nei: Hung Suet-nei (Chinese: 熊雪妮), known as Suet Nei or Suet Nay (Chinese: 雪妮) is a Hong Kong actress born in 1945, Hong Kong.  She is a veteran actress, having acted for many years.  She has starred in martial arts Cantonese operas, due to her skill in martial arts.  She signed with TVB in 1988.\n\nMayu Gamō: Mayu Gamō (蒲生 麻由 , Gamō Mayu , born March 16, 1982) is a Japanese actress born in Saitama Prefecture, Japan.  She has starred in many films, most notably in Tokusou Sentai Dekaranger as Succubus Hells/ Human Fatale Camille.  She reprised her role in Tokusou Sentai Dekaranger vs. Abaranger for a brief appearance.  She also starred in Kamen Rider Hibiki as Kasumi Tachibana.  Gamō is an active amateur marathon competitor and triathlete, having competed both in the Tokyo Marathon and in Hawaii, Paris, and Australia.  She completed the 2011 Lavaman Triathlon in Anaehoomalu Bay, Hawaii.\n\nQuestion: This actress born on May, 1979 starred in Josie and the Pussycats?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"birth_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"birth_month\": {\n          \"type\": \"string\",\n          \"description\": \"The month of birth.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year of birth.\"\n        }\n      },\n      \"required\": [\n        \"birth_month\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"role_in_film\": {\n          \"type\": \"string\",\n          \"description\": \"The character or group the actress portrayed in the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"film_title\",\n        \"role_in_film\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"meets_all_criteria\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the actress meets all specified criteria (birth month/year and film appearance).\"\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"birth_details\",\n    \"film_details\",\n    \"meets_all_criteria\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "birth_details": {
        "type": "object",
        "properties": {
          "birth_month": {
            "type": "string",
            "description": "The month of birth."
          },
          "birth_year": {
            "type": "integer",
            "description": "The year of birth."
          }
        },
        "required": [
          "birth_month",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "film_details": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film."
          },
          "role_in_film": {
            "type": "string",
            "description": "The character or group the actress portrayed in the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "film_title",
          "role_in_film",
          "release_year"
        ],
        "additionalProperties": false
      },
      "meets_all_criteria": {
        "type": "boolean",
        "description": "Indicates if the actress meets all specified criteria (birth month/year and film appearance)."
      }
    },
    "required": [
      "actress_name",
      "birth_details",
      "film_details",
      "meets_all_criteria"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
