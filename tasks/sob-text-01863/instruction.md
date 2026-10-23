{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n7th Heaven (1927 film): 7th Heaven (also known as Seventh Heaven) is a 1927 American silent romantic drama directed by Frank Borzage, and starring Janet Gaynor and Charles Farrell.  The film is based upon the 1922 play \"Seventh Heaven\", by Austin Strong and was adapted for the screen by Benjamin Glazer.  \"7th Heaven\" was initially released as a standard silent film in May of 1927.  On September 10, 1927, Fox Film Corporation re-released the film with a synchronized Movietone soundtrack with a musical score and sound effects.\n\n7th Heaven (season 11): Season eleven of \"7th Heaven\"—an American family-drama television series, created and produced by Brenda Hampton.  It premiered on September 25, 2006, on The CW, and concluded on May 13, 2007 (22 episodes).  It is the final season of the series.  Stephen Collins, Catherine Hicks, Beverley Mitchell, and Mackenzie Rosman are the only cast members to star in all eleven seasons of the series, along with Happy the dog.\n\nSeventh Heaven: Seventh Heaven or 7th Heaven is a state of euphoria.  It may also refer to:\n\nBrooke Ramel: Brooke Ramel is an American singer-songwriter based in Los Angeles, California.  She has released eight studio albums to date; her first album was \"Movie Star\" (1996).  On December 18, 2000, Ramel appeared as a street performer on the television series, \"7th Heaven\", performing the opening song.\n\nKeith Semple: Keith Semple (born 20 September 1981 in Larne, Northern Ireland) is a Northern Irish singer and musician.  He originally had his own band Keith Semple Band.  In 2002, he took part and was a winner in \"Popstars: The Rivals\", consequently becoming a member of the boyband One True Voice (OTV).  After the split-up of the band, he had a solo career before joining the American Chicago-based rock band 7th Heaven in 2006 as their lead singer.  In 2010, he took a shot at the ninth season of \"American Idol\", but lost his \"golden ticket\" place due to his legal status and residency considerations.  In October 2012, Keith announced he would be leaving 7th Heaven to pursue his original music and announced the formation of his new band, SEMPLE.  In September 2015, Keith auditioned for Season 9 of \"The Voice\" as part of Team Adam.  He was eliminated from competition after the Top 24 round.\n\nSafe Harbor (TV series): Safe Harbor is an American television drama series that aired on The WB Television Network from September 20, 1999 to November 28, 1999.  The series was created and executive produced by Brenda Hampton, who at the time was best known for work on the fellow WB series \"7th Heaven\", the series was paired with \"7th Heaven\" on the network's Monday night lineup.  Despite \"7th Heaven\" being the No. 1 show on The WB during the 1999-2000 season, \"Safe Harbor\" was unable to hold a solid audience after \"7th Heaven\" and was canceled after ten episodes and one season with the show moving to Sunday nights where the last two episodes aired.\n\nBarret Swatek: Barret Swatek (born March 3, 1977) is an American actress and comedian who has appeared in films such as \"Lethal Weapon 4\", \"The 40-Year-Old Virgin\", and \"High School\".  She has also made guest appearances on television shows such as \"Just Shoot Me! \", \"American Dad! \", and \"2 Broke Girls\", and recurred as teacher Ms. Sommers on \"10 Things I Hate About You\".  She played resident bad girl gone good, Cheryl, on the WB series \"7th Heaven\" for three seasons, and played the role of Brittany on the NBC comedy series \"Quarterlife\".  She is a frequent panelist on the late-night Fox News show \"Red Eye w/Greg Gutfeld\".  Swatek plays the recurring character Ally on the MTV comedy series \"Awkward\".\n\nJessica Biel: Jessica Claire Timberlake (née Biel; born March 3, 1982) is an American actress, model and producer.  Biel began her career as a vocalist appearing in musical productions until she was cast as Mary Camden in the family-drama series \"7th Heaven\", for which she achieved recognition.  The series is the longest-running series that ever aired on The WB channel and is the longest-running family drama in television history.  As of late summer 2017, she is the series lead, title character, and executive producer of USA Network's new limited-series-format murder mystery \"The Sinner\".\n\nNew Year's Eve (2011 film): New Year's Eve is a 2011 American romantic comedy film directed by Garry Marshall and stars Halle Berry, Jessica Biel, Jon Bon Jovi, Abigail Breslin, Ludacris, Robert De Niro, Josh Duhamel, Zac Efron, Héctor Elizondo, Katherine Heigl, Ashton Kutcher, Seth Meyers, Lea Michele, Sarah Jessica Parker, Michelle Pfeiffer, Til Schweiger, Hilary Swank, Sofía Vergara and Alyssa Milano.\n\nCharles Farrell: Charles Farrell (August 9, 1900 – May 6, 1990) was an American film actor of the 1920s silent era and into the 1930s, and later a television actor.  Farrell is probably best recalled for his onscreen romances with actress Janet Gaynor in more than a dozen films, including \"7th Heaven\", \"Street Angel\", and \"Lucky Star\".\n\nQuestion: Who directed a romantic comedy starring a \"7th Heaven\" star and Ludacris?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director.\"\n    },\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"movie_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"actor_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the actor.\"\n          },\n          \"connection_to_7th_heaven\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the actor was a star in '7th Heaven'.\"\n          },\n          \"is_ludacris\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the actor is Ludacris.\"\n          }\n        },\n        \"required\": [\n          \"actor_name\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of key actors in the film, including the '7th Heaven' star and Ludacris.\"\n    }\n  },\n  \"required\": [\n    \"director_name\",\n    \"movie_title\",\n    \"movie_genre\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_name": {
        "type": "string",
        "description": "The name of the director."
      },
      "movie_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "movie_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "actor_name": {
              "type": "string",
              "description": "The name of the actor."
            },
            "connection_to_7th_heaven": {
              "type": "boolean",
              "description": "True if the actor was a star in '7th Heaven'."
            },
            "is_ludacris": {
              "type": "boolean",
              "description": "True if the actor is Ludacris."
            }
          },
          "required": [
            "actor_name"
          ],
          "additionalProperties": false
        },
        "description": "A list of key actors in the film, including the '7th Heaven' star and Ludacris."
      }
    },
    "required": [
      "director_name",
      "movie_title",
      "movie_genre",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
