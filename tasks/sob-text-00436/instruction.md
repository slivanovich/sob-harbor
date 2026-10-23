{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n.com for Murder: . com for Murder is a 2001 science fiction crime drama film written by Nico Mastorakis and Phill Marr and directed by Mastorakis, starring Nastassja Kinski, Nicollette Sheridan, Roger Daltrey, and Huey Lewis.  After being screened at various film festivals, it was released direct-to-video on 14 January 2003.\n\nMaria's Lovers: Maria's Lovers is a 1984 drama film directed by Andrei Konchalovsky and starring Nastassja Kinski, John Savage, and Robert Mitchum.  The plot follows a soldier returning from World War II who marries the woman of his dreams, but he is unable to consummate his marriage ruining the couple's chances of a shared happiness.\n\nStay as You Are: Stay as You Are (Italian: \"Così come sei\" ), also known as Stay the Way You Are, is a 1978 Italian–Spanish erotic drama film, directed by Alberto Lattuada, starring Nastassja Kinski, Marcello Mastroianni, Barbara De Rossi, and Ania Pieroni.  It follows the May–December romance between a vivacious young coed and a middle-aged professional who is unhappy in his marriage.\n\nTime Share: Time Share is a TV movie starring Nastassja Kinski and Timothy Dalton.  It premiered on Fox Family Channel on June 18, 2000.  It is directed by .\n\nBlind Terror: Blind Terror is a 2001 suspense thriller starring Nastassja Kinski, Stewart Bick and Gordon Pinsent.  It was written by Douglas Soesbe and directed by Giles Walker.\n\nCat People (1982 film): Cat People is a 1982 American erotic horror film directed by Paul Schrader.  It stars Nastassja Kinski and Malcolm McDowell; John Heard, Annette O'Toole, Ruby Dee, Ed Begley, Jr., Scott Paulin, and Frankie Faison play supporting roles.  Jerry Bruckheimer served as executive producer.  Alan Ormsby wrote the screenplay, basing it loosely on the story by DeWitt Bodeen, the screenwriter for the original \"Cat People\" (1942).  Giorgio Moroder composed the film's score, including the theme song, which features lyrics and vocals by David Bowie.\n\nSusan's Plan: Susan's Plan (also released as \"Dying to Get Rich\" on video) is a 1998 black comedy film directed by John Landis and starring Nastassja Kinski, Dan Aykroyd, Billy Zane, Rob Schneider, Lara Flynn Boyle and Michael Biehn.  The plot revolves around Susan's (played by Kinski) plan to kill her former husband (with the help of a group of misfits) and collect his life insurance.\n\nPaul Schrader: Paul Joseph Schrader (born July 22, 1946) is an American screenwriter, film director, and film critic.  Schrader wrote or co-wrote screenplays for four Martin Scorsese films: \"Taxi Driver\" (1976), \"Raging Bull\" (1980), \"The Last Temptation of Christ\" (1988), and \"Bringing Out the Dead\" (1999).  Schrader has also directed 18 feature films, including his directing debut crime drama, \"Blue Collar\" (co-written with his brother, Leonard Schrader), the crime drama \"Hardcore\" (a loosely autobiographical film also written by Schrader), his 1982 remake of the horror classic \"Cat People\", the crime drama \"American Gigolo\" (1980), the biographical drama \"\" (1985), the cult film \"Light Sleeper\" (1992), the drama \"Affliction\" (1997), the biographical film \"Auto Focus\" (2002), and the erotic dramatic thriller \"The Canyons\" (2013).\n\nThe Ring (1996 film): The Ring is a 1996 film, directed by Armand Mastroianni, written by Danielle Steel, and starring Nastassja Kinski and Michael York.\n\nCold Heart: Cold Heart is a 2001 thriller genre film starring Nastassja Kinski and Jeff Fahey.  The film conveys the atmosphere of conspiracy, the essence of which becomes clear to an innocent victim at the very last moment.\n\nQuestion: Which film starring Nastassja Kinski and Malcolm McDowell did this American screenwriter, film director, and film critic who co-wrote the screenplay for  \"Taxi Driver\" (1976) direct?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"director_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of the director's professional occupations.\"\n        },\n        \"notable_screenplay_credits\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"title\": {\n                \"type\": \"string\"\n              },\n              \"year\": {\n                \"type\": \"integer\"\n              }\n            },\n            \"required\": [\n              \"title\",\n              \"year\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of films for which the director co-wrote screenplays, including their release year.\"\n        }\n      },\n      \"required\": [\n        \"occupations\",\n        \"notable_screenplay_credits\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the main actors starring in the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director\",\n    \"director_attributes\",\n    \"starring_actors\",\n    \"film_genre\",\n    \"release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "director_attributes": {
        "type": "object",
        "properties": {
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of the director's professional occupations."
          },
          "notable_screenplay_credits": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "title": {
                  "type": "string"
                },
                "year": {
                  "type": "integer"
                }
              },
              "required": [
                "title",
                "year"
              ],
              "additionalProperties": false
            },
            "description": "A list of films for which the director co-wrote screenplays, including their release year."
          }
        },
        "required": [
          "occupations",
          "notable_screenplay_credits"
        ],
        "additionalProperties": false
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the main actors starring in the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The primary genre of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      }
    },
    "required": [
      "film_title",
      "director",
      "director_attributes",
      "starring_actors",
      "film_genre",
      "release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
