{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPaul Saltzman: Paul Saltzman is a two-time Canadian Emmy Award-winning film and television producer-director with more than 300 films, both dramas and documentaries, to his credit.  The 2008 documentary feature, \"Prom Night in Mississippi\", featuring actor Morgan Freeman, premiered at the 2009 Sundance Film Festival.  His most recent film, the feature documentary, \"The Last White Knight—Is Reconciliation Possible?\"  premiered at TIFF (Toronto International Film Festival) in 2012.  It features Morgan Freeman, Harry Belafonte, Delay de la Beckwith (son of Byron De La Beckwith) as well as Saltzman himself.  He is also founder, CEO and president of the charitable, non-profit organization Moving Beyond Prejudice, which works with students, educators, youth-at-risk and community groups.\n\nRamin Djawadi: Ramin Djawadi ( , Persian: رامین جوادی‎ ‎ ; born July 19, 1974) is an Iranian-German composer.  Djawadi is best known for his score for HBO's popular television series \"Game of Thrones\".  He is also known for his works on movies such as \"Clash of the Titans\", \"Pacific Rim\", \"Warcraft\" and the Grammy-nominated score for the 2008 Marvel film \"Iron Man\", and television series including \"Prison Break\", \"Person of Interest\", and \"Westworld\".\n\nConcorde Affaire '79: Concorde Affaire '79 (1979) (Italian: \"Affare Concorde\" ), also known as The Concorde Affair, is an Italian action thriller directed by Ruggero Deodato and written by Ernesto Gastaldi and Renzo Genta.  Released in the same year as \"The Concorde ... Airport '79\" and featuring actor Joseph Cotten, who appeared in \"Airport '77\", the film was an attempt by producers to take advantage of the success of the \"Airport\" film franchise of the 1970s.\n\nJamie James (musician): Jamie James (born August 4, 1953 in Toronto, Ontario) is a Canadian guitarist, singer and songwriter, best known for his roles in DQ And The Sharks and Steppenwolf.  He was also lead singer and founding member of RSO recording trio The Kingbees.  The Kingbees recorded 2 albums with David J. Holman producing on RSO.  The first, titled \"The Kingbees\", (released March, 1980) received much critical acclaim and regional success with the James-penned hit \"My Mistake\".  The second album, titled \"The Big Rock\", was released in March 1981 and also spawned national touring, a performance on Dick Clark's American Bandstand and a cameo role in the movie \"The Idolmaker\".  Shortly thereafter the band split up.  In 1983 James released a solo EP with Vanity Records titled \"The Big One\".  In the late 1980s, James hooked up with noted actor Harry Dean Stanton to form a unique musical ensemble which performed until the year 2000.  In 2000 James went on to form the rock and roll band \"DQ and The Sharks\" featuring actor/musician Dennis Quaid.  In 1993 James had also released a solo LP on Schoolkids Records titled \"Cruel World\".  In 2000 he released his latest solo LP on Oglio Records, titled \"Crossroads\".  Oglio also released a two-album CD issue of the Kingbees first and second LPs.  James resides in Los Angeles, where he just formed a new record label with friend and business partner Fred Wehba.  We Jam Music was created by James and Wehba to produce and release new albums including James' newest release Love Attack.\n\nI. N. Murthy: I. N. Murthy was an Indian film director, known for his spy thrillers, featuring actor Jaishankar in the 1970s.\n\nStatross le Magnifique: Statross le Magnifique is a 2006 film by director Rémi Lange featuring actor Jann Halexander.\n\nGokula Krishnan: Gokula Krishnan was an Indian film director, who has directed Tamil films.  He was primarily active in the 1980s and early 1990s and is most noted for his work on films featuring actor Karthik.  He also extensively worked with Malayalam director Fazil, when he made Tamil films, helping write dialogues.\n\nRadha Bharathi: Radha Bharathi is an Indian film director who has worked on Tamil and Kannada language films.  He was active in the early 1990s and worked on two high-profile films featuring actor Prashaath, and has since worked on a few low budget projects.\n\nJames Bethea: James A. Bethea Jr. (born January 14, 1965) is an American writer, producer and occasional performer, primarily in the field of television.  As the former Head of Current Programming for UPN, he is among a handful of African Americans to head a programming department at a broadcast network.  Series overseen by him at UPN include Star Trek Voyager, Dilbert, Clueless and Moesha.  As an actor, he appears in the 2008 Iron Man (2008 film) and 2010 sequel, Iron Man 2.\n\nIron Man (2008 film): Iron Man is a 2008 American superhero film based on the Marvel Comics character of the same name, produced by Marvel Studios and distributed by Paramount Pictures.  It is the first film in the Marvel Cinematic Universe.  The film was directed by Jon Favreau, with a screenplay by the writing teams of Mark Fergus and Hawk Ostby and Art Marcum and Matt Holloway.  It stars Robert Downey Jr., Terrence Howard, Jeff Bridges, Shaun Toub, and Gwyneth Paltrow.  In \"Iron Man\", Tony Stark, an industrialist and master engineer, builds a powered exoskeleton and becomes the technologically advanced superhero Iron Man.\n\nQuestion: Who directed the 2008 Marvel film featuring actor James Bethea?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the director.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"featured_actor\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor featured in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"featured_actor\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the director."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "featured_actor": {
        "type": "string",
        "description": "The name of the actor featured in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "featured_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
