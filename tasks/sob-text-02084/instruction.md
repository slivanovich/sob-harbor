{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSamuel T. Hubbard Jr.: Samuel Thomas Hubbard Jr. (1884–1962) was a cotton industry executive and military intelligence officer with the American Expeditionary Forces during World War I.  Hubbard served as chief of the Enemy Order of Battle Section in the G2 Military Intelligence Division and then as a liaison to the Allied Forces' headquarters for General John Pershing.  He also served as director of the military intelligence school in Langres, France at the end of the war.  Recognizing these efforts, the U.S. Army awarded Hubbard their Distinguished Service Medal, and France awarded him their Officier d'Académie Medal.  Returning to the U.S., Hubbard worked as an executive with Hubbard Brothers & Company (HBC), a cotton grower launched by his family members.  Representing HBC, he served as vice president and then as president of the New York Cotton Exchange, the oldest commodity exchange in New York City.\n\nWilliam Woodward Sr.: Born in New York City to William Woodward and Sarah Abagail Rodman, William came from a prominent and wealthy Maryland family that dates back to colonial times.  The family made their fortune in selling textiles to the Confederate government, and his father was the founder of the New York Cotton Exchange.\n\nMatka gambling: Matka\" gambling or satta\" is a form of lottery which originally involved betting on the opening and closing rates of cotton transmitted from the New York Cotton Exchange.  It originates from before the era of Indian independence when it was known as \"Ankada Jugar\" (\"figures gambling\").  In the 1960s, the system was replaced with other ways of generating random numbers, including pulling slips from a large earthenware pot known as a \"matka\", or dealing playing cards.\n\nNew York Cotton Exchange: The New York Cotton Exchange (NYCE) is a commodities exchange founded in 1870 by a group of one hundred cotton brokers and merchants at 1 Hanover Square in New York City.  In 1998, the New York Board of Trade (NYBOT) became the parent company of both the New York Cotton Exchange, and it is now owned by IntercontinentalExchange (ICE).  Since 2003, its headquarters and trading facility have been in the New York Mercantile Exchange Building.\n\nCoffee, Sugar and Cocoa Exchange: The Coffee, Sugar and Cocoa Exchange (CSCE) was founded in 1882 as the Coffee Exchange in the City of New York.  Sugar futures were added in 1914, and, on September 28, 1979, the New York Coffee and Sugar Exchange merged with the New York Cocoa Exchange (which in turn had been founded in 1925) to form CSCE.  In 1998, CSCE merged with the New York Cotton Exchange as subsidiaries of the New York Board of Trade (NYBOT).  The CSCE operates as an independent unit of NYBOT trading futures and options on coffee, sugar and cocoa and the S&P Commodity Index.  Trading is by open outcry, from 8 a.m. to 2:45 p.m., Monday through Friday.  In January 2007, NYBOT merged with IntercontinentalExchange (ICE) and became a wholly owned subsidiary of ICE.\n\nMobile Cotton Exchange: The Mobile Cotton Exchange was a commodities exchange that operated from 1871 until 1942 in the Alabama port city of Mobile to enable key local cotton factors and merchants to maintain control over cotton sales, warehousing, and shipping from Mobile Bay.  It was the third cotton exchange founded in the United States, following those in New York and New Orleans.  The exchange in Mobile was followed by exchanges in Savannah and Memphis.\n\nDayavan: Dayavan: Truth is Power (English: \"The Compassionate\") is a 1988 Hindi thriller movie remake of the Tamil film \"Nayagan\" (1987).  The movie was directed by Feroz Khan, and starred Vinod Khanna, Feroz Khan and Madhuri Dixit in lead roles with Aditya Pancholi in an important role.\n\n1 Hanover Square: 1 Hanover Square, formerly known as the New York Cotton Exchange building and as India House, is on the southern edge of Hanover Square in Lower Manhattan, New York City.\n\nDharmatma: Dharmatama is a 1975 Hindi thriller movie and the first Bollywood film to be shot in Afghanistan.  It was produced and directed by Feroz Khan.  The movie is the first attempt in India to localise \"The Godfather\".  The title character was based on matka (form of Indian gambling) king Ratan Khatri.  It is said that Khan sat down with Khatri to learn more about him and understand the nuances of matka.  The cast includes Feroz Khan, Hema Malini, Rekha, Premnath, Imtiaz Khan, Danny Denzongpa, Farida Jalal, Ranjeet, Helen, Madan Puri, Jeevan, Iftekhar and Dara Singh, satyen kappu and sudhir.  The music is by Kalyanji Anandji.  This film took Feroz Khan to new heights in his career as this was a blockbuster movie.  The same year, \"Sholay\" and \"Deewar\" were released.  The film is also its scenes featuring Buzkashi a Central Asian sport on horses, including aerial shots, which in turn won film's cinematographer, Kamal Bose, Filmfare Award for Best Cinematographer.\n\nR.H. Hooper &amp; Company: R.H. Hooper & Cooper & Company was the name used by two stock traders, Joseph C. Monier and Clifford M. Story, before they were suspended from the New York Cotton Exchange on June 18, 1930.  The company was reportedly insolvent by June 18, 1930, announcing its intention\n\nQuestion:  Dharmatama is a 1975 Hindi thriller movie and the first Bollywood film to be shot in which country, the title character was based on Ratan Khatri, Matka gambling is a form of lottery which originally involved betting on the opening and closing rates of cotton transmitted from the New York Cotton Exchange?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"genre\": {\n          \"type\": \"string\"\n        },\n        \"director\": {\n          \"type\": \"string\"\n        },\n        \"is_first_bollywood_film_shot_in_country\": {\n          \"type\": \"boolean\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"genre\",\n        \"director\",\n        \"is_first_bollywood_film_shot_in_country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"shooting_location_country\": {\n      \"type\": \"string\"\n    },\n    \"title_character_inspiration\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"role\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"matka_gambling_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"description\": {\n          \"type\": \"string\"\n        },\n        \"original_betting_subject\": {\n          \"type\": \"string\"\n        },\n        \"original_source_of_rates\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"description\",\n        \"original_betting_subject\",\n        \"original_source_of_rates\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"movie_details\",\n    \"shooting_location_country\",\n    \"title_character_inspiration\",\n    \"matka_gambling_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "genre": {
            "type": "string"
          },
          "director": {
            "type": "string"
          },
          "is_first_bollywood_film_shot_in_country": {
            "type": "boolean"
          }
        },
        "required": [
          "title",
          "release_year",
          "genre",
          "director",
          "is_first_bollywood_film_shot_in_country"
        ],
        "additionalProperties": false
      },
      "shooting_location_country": {
        "type": "string"
      },
      "title_character_inspiration": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "matka_gambling_details": {
        "type": "object",
        "properties": {
          "description": {
            "type": "string"
          },
          "original_betting_subject": {
            "type": "string"
          },
          "original_source_of_rates": {
            "type": "string"
          }
        },
        "required": [
          "description",
          "original_betting_subject",
          "original_source_of_rates"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "movie_details",
      "shooting_location_country",
      "title_character_inspiration",
      "matka_gambling_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
