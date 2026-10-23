{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRacing with the Moon: Racing with the Moon is a 1984 American drama film starring Sean Penn, Elizabeth McGovern, and Nicolas Cage.  It was directed by Richard Benjamin and written by Steven Kloves.  The original music score was composed by Dave Grusin.\n\nKara Zediker: Kara Zediker is an American actress born in Kankakee, Illinois.  She guest starred on \"\" as the young T'Pau in the fourth-season episodes \"Awakening\" and \"Kir'Shara\".  She has also guest-starred on such shows as \"Charmed\", \"The King of Queens\", \"Becker\", \"Joan of Arcadia\" and \"24\".\n\nBlanche Whiffen: Blanche Whiffen, better known as Mrs. Thomas Whiffen, (1845–1936) was an American actress born in London.  Her maiden name was Galton.  She was educated in France; made her stage début at the Royalty Theatre, London, in 1865; came to America in 1868; and toured the United States under John Templeton's management.  In 1879 she played Buttercup in the first American production of Gilbert and Sullivan's \"Pinafore\".  She joined Daniel Frohman's stock company at his old Lyceum Theatre, where she appeared in more than 25 plays between 1887 and 1899 including \"The Wife\" (1887), \"The Charity Ball\" (1889), and \"Trelawny of the 'Wells'\" (1898).  Later she was part of Charles Frohman's company at the Empire.  She became Broadway's resident old lady character player after the death of Mrs. G. H. Gilbert in 1904.  Mrs Whiffen in later years appeared in \"Zira\" (1905); \"The Great Divide\" (1905–07); \"The Builder of Bridges\" (1909); \"The Brass Bottle\" (1910); \"Electricity\" (1910); \"Cousin Kate\" (1912); \"Tante\" (1913); \"A Scrap of Paper\" (1914); \"Rosemary\" (1915).  She was still active at 70 and a great favorite.\n\nHailey McCann: Hailey McCann (born October 3, 1995) is an American actress born in Riverside, California.  McCann is one of four children and has two sisters and a brother.  She played her first role in the 2003 short film \"Give or Take an Inch\".  In the movie \"The Time Traveler's Wife\" she appeared alongside her younger sister, Tatum McCann as well as Eric Bana and Rachel McAdams.  The sisters both played the character of Alba DeTamble in different time periods.\n\nRenée Bourque: Renée Lee Moniz (born October 16, 1977) is an American actress born and raised in Rhode Island.  She is also known as \"Renée Moniz\" and \"Renee Bourque Moniz\".  She has appeared in \"American Hustle\" and in the movie \"27 Dresses\" where she plays Katherine Heigl's co-worker at Urban Everest.\n\nJacqueline Lovell: Jacqueline Lovell (born 9 December 1974) is an American actress born and raised in Southern California.  Most of her roles have been in B-films and erotic movies.\n\nIrene Gorovaia: Irene Gorovaia (Russian: Ирина Горовая ; born June 13, 1989), also credited as Irina Gorovaia, is an American actress born in Russia and raised in Brooklyn, New York.  She has been a ballet dancer for many years, training with the School of American Ballet.\n\nJean Fenwick: Jean Fenwick, born Harriet Krauth (May 30, 1907 — December 5, 1998) was an American actress born in Trinidad.\n\nElizabeth McGovern: Elizabeth Lee McGovern (born July 18, 1961) is an American film, television, and theater actor, and musician.  She received an Academy Award nomination for her role as Evelyn Nesbit in the 1981 film \"Ragtime\".  She is also known for her performance as Lady Cora Crawley, Countess of Grantham in the British drama series \"Downton Abbey\", for which she has been nominated for an Emmy Award and Golden Globe Award.  Her other films include \"Ordinary People\" (1980), \"Once Upon a Time in America\" (1984), \"The Handmaid's Tale\" (1990) and \"The Wings of the Dove\" (1997).\n\nEvelyn Ankers: Evelyn Felisa Ankers (August 17, 1918 – August 29, 1985) was an American actress born in Valparaiso, Chile.  She often played variations on the role of the cultured young leading lady in many American horror films during the 1940s, most notably \"The Wolf Man\" (1941) opposite Lon Chaney, Jr., a frequent screen partner.\n\nQuestion: Racing with the Moon starred an American actress born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"starred_actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the American actress who starred in the film.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actress.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the actress.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"question_answer\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the American actress who starred in the film, which is the answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"starred_actress\",\n    \"question_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "starred_actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the American actress who starred in the film."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actress."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the actress."
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "question_answer": {
        "type": "integer",
        "description": "The birth year of the American actress who starred in the film, which is the answer to the question."
      }
    },
    "required": [
      "film_title",
      "starred_actress",
      "question_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
