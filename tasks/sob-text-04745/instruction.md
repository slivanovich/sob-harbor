{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUntold Scandal: Untold Scandal (; lit.  \"Scandal: The Love Story of Men and Women in Joseon\") is a 2003 South Korean romantic drama film directed by E J-yong, and starring Bae Yong-joon, Jeon Do-yeon, and Lee Mi-sook.  Loosely based on the 18th century French novel \"Les Liaisons dangereuses\", this adaptation takes place in late 18th century Korea, during the Joseon dynasty.\n\nMy Brilliant Life: My Brilliant Life (; lit.  \"My Palpitating Life\") is a 2014 South Korean drama film starring Song Hye-kyo and Kang Dong-won.  It was co-written and directed by E J-yong based on the 2011 novel \"My Palpitating Life\" by Kim Aeran.\n\nSong Jae-ho: Song Jae-ho (born Song Jae-eon on March 10, 1937) is a South Korean actor.  He made his acting debut in 1959, and became best known for his work in 1970s and 1980s Korean cinema, notably \"Yeong-ja's Heydays\" (1975).  Song has since become one of the most respected veteran actors in Korean film and television, with more recent starring roles in the films \"Memories of Murder\" (2003), \"The President's Last Bang\" (2005) and \"Late Blossom\" (2011), as well as the television drama \"Precious Family\" (2004).\n\nLee Mi-sook: Lee Mi-sook (born April 2, 1960) is a South Korean actress.  One of the best-known actresses of 1980s Korean cinema, Lee's most famous films from this era include Bae Chang-ho's \"Whale Hunting\" and \"The Winter That Year Was Warm\", Lee Doo-yong's \"Mulberry\" and \"Eunuch\", and Kwak Ji-kyoon's \"Wanderer in Winter\".  She retired from film after getting married in 1987, though she still appeared on television in dramas such as \"How's Your Husband?\"  (1993).  Then a decade later, Lee made her comeback with an award-winning leading role in E J-yong's feature debut \"An Affair\" (1998).  She has since remained active in film and television, notably in the May–December romance \"Solitude\" (2002), the \"Dangerous Liaisons\" adaptation \"Untold Scandal\" (2003), the mockumentary \"Actresses\" (2009), and the family dramas \"Smile, Mom\" (2010)\n\nE J-yong: E J-yong (; born September 5, 1966) is a South Korean film director and screenwriter.  His feature films include \"An Affair\" (1998), \"Untold Scandal\" (2003), \"Dasepo Naughty Girls\" (2006), and \"Actresses\" (2009).\n\nThe Dreamers (film): The Dreamers is a 2003 romantic drama film directed by Bernardo Bertolucci.  The screenplay is by Gilbert Adair, based on his own novel \"The Holy Innocents\".  An international co-production by companies from France, the United Kingdom, and Italy, the film tells the story of an American university student in Paris who, after meeting a peculiar brother and sister who are fellow film enthusiasts, becomes entangled in an erotic conflict.  It is set against the backdrop of the 1968 Paris student riots.  The film makes several references to various movies of classical and New Wave cinema, incorporating clips from films that are often imitated by the actors in particular scenes.\n\nA Thousand Clouds of Peace: A Thousand Clouds of Peace is a 2003 romantic drama film written and directed by Julián Hernández.  Its original Spanish title is Mil nubes de paz cercan el cielo, amor, jamás acabarás de ser amor and alternative titles for it are \"A Thousand Clouds of Peace Fence the Sky, Love; Your Being Love Will Never End\" and \"A Thousand Peace Clouds Encircle the Sky\".\n\nActresses (film): Actresses () is a 2009 South Korean mockumentary-style drama film directed by E J-yong.\n\nThe Bacchus Lady: The Bacchus Lady (Korean: 죽여주는 여자, \"The Killer Woman\" ) is a 2016 South Korean drama film directed by E J-yong.  It was shown in the Panorama section at the 66th Berlin International Film Festival as well as the Seattle International Film Festival.  The director describes the film as a \"bittersweet drama\".\n\nThe Lover of Camille: The Lover of Camille was a 1924 American silent romantic drama film directed by Harry Beaumont, and starring Monte Blue.  The film was based on the French novel \"Deburau\" by Sacha Guitry, which was also adapted into a Broadway play by Harley Granville-Barker.\n\nQuestion: A 2003 romantic drama directed by E J-yong, starring one of the best-known actresses of 1980s Korean cinema was based on what french novel?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"starring_actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the prominent actress in the film.\"\n        },\n        \"description_keywords\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Keywords describing the actress's prominence.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"description_keywords\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"based_on_novel\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the French novel the film was based on.\"\n        },\n        \"origin_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country of origin of the novel.\"\n        },\n        \"century\": {\n          \"type\": \"string\",\n          \"description\": \"The century the novel was written.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"origin_country\",\n        \"century\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"starring_actress\",\n    \"based_on_novel\",\n    \"genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "starring_actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the prominent actress in the film."
          },
          "description_keywords": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Keywords describing the actress's prominence."
          }
        },
        "required": [
          "name",
          "description_keywords"
        ],
        "additionalProperties": false
      },
      "based_on_novel": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the French novel the film was based on."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin of the novel."
          },
          "century": {
            "type": "string",
            "description": "The century the novel was written."
          }
        },
        "required": [
          "title",
          "origin_country",
          "century"
        ],
        "additionalProperties": false
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "starring_actress",
      "based_on_novel",
      "genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
