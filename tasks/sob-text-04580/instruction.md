{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Leguizamo: John Alberto Leguizamo ( ; born July 22, 1964) is a Colombian-American actor, voice actor, stand-up comedian, film producer, playwright and screenwriter.  He came to prominence with a co-starring role in the action/comedy \"Super Mario Bros.\" (1993) and a supporting role in the crime drama \"Carlito's Way\" (1993).  Other notable roles include Sid the Sloth in the animated \"Ice Age\" films (2002–2016) and the narrator of the sitcom \"The Brothers García\" (2000–2004).  As of 2009, he has appeared in over 75 films, produced over 10 films, starred on Broadway in several productions (winning several awards), made over 12 television appearances, and has produced or starred in many other television shows.\n\nMichael Yo: Michael Yo Simmons (born November 20, 1974) is an American actor, TV Host, Hollywood expert and stand-up comedian.  He currently co-hosts The Insider on CBS, as well as Yo Show on Yahoo! TV, which garners an average of 1.5 million views per episode.  Yo also appears regularly on the comedy panel of E!'s Chelsea Lately and as a guest host for The Talk on CBS.  Yo continues to appear as a Pop Culture expert on HLN's Showbiz Tonight hosted by A.J. Hammer.  Michael tours the country as a professional stand-up comedian, appearing at the Improv’s, Stand-Up Live, Palms Hotel, Laugh Factory, Comedy Store, and Comedy Juice among others.  His Hot Mess Tour also performs at colleges throughout the country.\n\nRonnie Schell: Ronald Ralph \"Ronnie\" Schell (born December 23, 1931) is an American actor, stand-up comedian, and voice actor.  He appeared on May 28, 1959, episode of the TV quiz program \"You Bet Your Life\", hosted by Groucho Marx.  Schell demonstrated a comic barrage of beatnik jive talk.  As a stand-up comedian, he first developed his act at the world-famous hungry-i nightclub in San Francisco, California.  Schell is probably best known in his 1960s television role as Duke Slater in \"Gomer Pyle, U.S.M.C.\"\n\nRon Lynch (comedian): Ron Lynch is an American stand-up comedian, actor, and writer.  He has appeared in a number of movies and television shows.  He has worked as a voice actor for several animated shows, including \"Home Movies\", \"Bob's Burgers\", and \"Tom Goes to the Mayor\", and has made guest appearances on \"Dr. Katz, Professional Therapist\", \"The Sarah Silverman Program\", \"Andy Richter Controls the Universe\", \"Adventure Time\", and \"Comedy Bang!  Bang! \".\n\nGary Owen (comedian): Gary Owen (born July 26, 1974) is an American actor and stand-up comedian.  After being named \"Funniest Serviceman In America,\" his big break came in 1997 on Black Entertainment Television's stand-up showcase \"Comic View\".  Owen followed this debut with featured roles in the films \"Daddy Day Care\", \"Little Man\", and \"College\".  He has cultivated an African-American following after headlining on cable channel BET and performing at targeted events, such as Shaquille O'Neal's All-Star Comedy Jam Tour.  He has an upcoming TV show on BET called \"The Gary Owen Show\".\n\nD. L. Hughley: Darryl Lynn \"D. L.\" Hughley ( ; born March 6, 1963) is an American actor, political commentator, radio host and stand-up comedian.  D.L. Hughley is best known as the original host of BET's \"ComicView\" from 1992-1993, the eponymous character on the ABC/UPN sitcom \"The Hughleys\" and performed in \"The Original Kings of Comedy\".  Additionally, he has been the host of CNN's \"D. L. Hughley Breaks the News\", a correspondent for \"The Jay Leno Show\" on NBC, and a local radio personality and interviewer in New York City.  In early 2013, D.L. Hughley landed in 9th place on \"Dancing with the Stars\".\n\nRawle D. Lewis: Rawle D. Lewis (c. 1974) is an American actor and comedian best known for portraying Junior Bevil in the 1993 comedy film \"Cool Runnings\".\n\nDorf Goes Fishing: Dorf Goes Fishing is a 1993 comedy film starring Tim Conway, Ronnie Schell and Yvonne Wilder.\n\nDon Curry: Don \"D.C.\" Curry (born September 5, 1959) is an American actor and stand-up comedian.  He is best known for starring as Craig's sex-crazed Uncle Elroy Jones in \"Next Friday\" and \"Friday After Next\" and for his role on the sitcom \"Grace Under Fire\".  Curry was also featured in The Boondocks episode, \"The Color Rucks\", in which he voice acts Uncle Ruckus' Caucasian-hating adoptive father.  He also hosted 2013 \"BET's Comic View\".  Curry got his first start on BET's \"Comic View\".\n\nVignesh Karthick: Vignesh Karthick is an Indian film and television actor, Video jockey, Stand-up comedian Radio jockey and Film director.  He started his career by acting and directing Short films and participating in reality shows, including the comedy game shows like \"Athu Ithu Ethu\" in STAR Vijay and Comedy Jodies in Zee Thamizh as a stand-up comedian.  He later went on to host of those shows, especially the popular shows like \"Suriya Vanakkam\", \"Thapal Petti En 8484\" and many other shows in Sun TV and STAR Vijay respectively.  In 2015, he started to work as Radio jockey with the radio station BIG FM 92.7.  In 2016, he made his acting debut in films with \"Natpadhigaram 79\" and in television with \"Pagal Nilavu\".  He will also making directorial debut in films with \"Yenda Thalaila Yenna Vekkala\".\n\nQuestion: What 1993 comedy film stars  an American actor, stand-up comedian, and voice actor who appeared on May 28, 1959, episode of the TV quiz program \"You Bet Your Life\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the comedy film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"starring_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"List of occupations for the actor.\"\n        },\n        \"notable_tv_appearance\": {\n          \"type\": \"string\",\n          \"description\": \"A notable television appearance of the actor mentioned in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"occupations\",\n        \"notable_tv_appearance\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"starring_actor\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the comedy film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "starring_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of occupations for the actor."
          },
          "notable_tv_appearance": {
            "type": "string",
            "description": "A notable television appearance of the actor mentioned in the context."
          }
        },
        "required": [
          "name",
          "occupations",
          "notable_tv_appearance"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "starring_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
