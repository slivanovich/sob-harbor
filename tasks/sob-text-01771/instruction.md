{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStrangers (The Walking Dead): \"Strangers\" is the second episode of the fifth season and 53rd episode overall of the post-apocalyptic horror television series \"The Walking Dead\", which aired on AMC on October 19, 2014.  The episode was written by series creator Robert Kirkman and directed by David Boyd.  In the episode, Rick Grimes (Andrew Lincoln)'s group encounters a priest, Father Gabriel Stokes (Seth Gilliam), who provides them solace in his church, while Rick contemplates Abraham Ford's (Michael Cudlitz) proposition to escort Dr. Eugene Porter (Josh McDermitt) to Washington, D.C. to cure the walker virus.\n\nInside Amy Schumer: Inside Amy Schumer is an American sketch comedy television series created and hosted by its star, Amy Schumer.  The series premiered on April 30, 2013, on Comedy Central.  Schumer and Daniel Powell serve as the show's executive producers.  \"Inside Amy Schumer\" completed its second season on June 3, 2014, and was renewed for a third season a week later.  The third season premiered on April 21, 2015, with a fourth season ordered the same day.  The fourth season premiered on April 21, 2016.  The show has received a Peabody Award and has been nominated for eight Primetime Emmy Awards, winning two.  On January 6, 2016, the show was renewed for a fifth season.  However, in August 2016, Schumer revealed that while a fifth season would happen at some point, there were no plans for it to begin production in the near future.\n\n4 Years, 6 Months, 2 Days: \"4 Years, 6 Months, 2 Days\" is the first episode of the fifth season of the television series \"One Tree Hill\", and eighty-ninth episode in total.  The episode premiered on The CW on January 8, 2008.  It became the first episode that has been ordered for mid-season.  The episode aired at 8/7C, with the second episode, \"Racing Like a Pro\", airing straight after.  The season then moved to the regular time of 9/8C.\n\nTina in the Sky with Diamonds: \"Tina in the Sky with Diamonds\" is the second episode of the fifth season of the American musical television series \"Glee\", and the ninetieth episode overall.  The episode was written and directed by series co-creator Ian Brennan and first aired on October 3, 2013 on Fox in the United States.  The episode is the second of two tribute episodes to the Beatles.  It features the prom, Tina Cohen-Chang (Jenna Ushkowitz) runs for prom queen, the crush of Sam Evans (Chord Overstreet) on new school nurse (Phoebe Strole), the new romance between Santana Lopez (Naya Rivera) and Dani (Demi Lovato), and a surprising news for Rachel Berry (Lea Michele) about \"Funny Girl\".  Special guest star Demi Lovato makes her first appearance as Dani, a struggling artist in New York City, and Peter Facinelli returns as Rupert Campion, the \"Funny Girl\" director.\n\nGlee (TV series): The series was created by Ryan Murphy, Brad Falchuk, and Ian Brennan, the latter of whom first conceived of \"Glee\" as a film.  The three wrote all of the show's episodes for the first two seasons, and Murphy and Falchuk initially served as the show's main directors.  The pilot episode was broadcast on May 19, 2009, and the first season aired from September 9, 2009, to June 8, 2010.  Subsequent seasons aired in September through May.  The sixth and final season aired from January to March 2015.  \"Glee\" features on-screen performance-based musical numbers that were selected by Murphy, who aimed to maintain a balance between show tunes and chart hits, and produced by Adam Anders and Peer Åström.  Songs covered in the show were released through the iTunes Store during the week of broadcast, and a series of \"Glee\" albums have been released by Columbia Records.  The music of \"Glee\" has been a commercial success, with over thirty-six million digital single sales and eleven million album sales worldwide through October 2011.  The series' merchandise also includes DVD and Blu-ray releases, an iPad application, and karaoke games for the Wii.  There were live concert tours by the show's cast after the first and second seasons completed shooting; a concert film based on the 2011 tour, \"\", was produced by Murphy and Fox and directed by Kevin Tancharoen.\n\nBlue Bloods (season 5): The fifth season of \"Blue Bloods\", a police procedural drama series created by Robin Green and Mitchell Burgess, premiered on CBS on September 26, 2014 and concluded on May 1, 2015.  Leonard Goldberg serves as executive producer.  CBS had renewed the series for a fifth season on March 13, 2014, with a 22-episode order.  The series aired its 100th episode (\"Baggage\") during the fifth season.\n\nTina and the Real Ghost: \"Tina and the Real Ghost\" is the second episode of the fifth season of the animated comedy series \"Bob's Burgers\" and the overall 69th episode, and is written by Steven Davis and Kelvin Yu and directed by Boohwan Lim and Kyounghee Lim.  It aired on Fox in the United States on November 2, 2014.\n\nGlee Sings the Beatles: Glee Sings the Beatles is the fifteenth soundtrack album by the cast of the American musical television show \"Glee\".  It was made available for pre-order on iTunes on September 10, 2013 with the expected to be released date on September 24, 2013, two days before the fifth season premiere.  The album features fourteen songs recorded for the first two episodes of the season: \"Love Love Love\" and \"Tina in the Sky with Diamonds\".\n\nDani (Glee): Dani was a recurring character in Glee.  Dani was portrayed by actress and singer Demi Lovato.  Dani’s main storylines was centred around her brief relationship with Santana Lopez.  Dani made her first appearance in the second episode of the fifth season, Tina in the Sky with Diamonds.\n\nTime's Arrow (Star Trek: The Next Generation): \"Time’s Arrow\" comprises the 126th and 127th episodes overall, and 26th episode of the and first episode of the of the American science fiction television series \"\".  A two-part episode of \"Star Trek: TNG\", the first episode was a cliffhanger season finale for the fifth season and the second episode was the premiere for the sixth season.\n\nQuestion: \"Tina in the Sky with Diamonds\" is the second episode of the fifth season of a television series created by who ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"episode_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the episode.\"\n    },\n    \"season_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The season number to which the episode belongs.\"\n    },\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"series_creators\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the creators of the television series.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"creator_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of a series creator.\"\n          }\n        },\n        \"required\": [\n          \"creator_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"episode_title\",\n    \"season_number\",\n    \"series_name\",\n    \"series_creators\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "episode_title": {
        "type": "string",
        "description": "The title of the episode."
      },
      "season_number": {
        "type": "integer",
        "description": "The season number to which the episode belongs."
      },
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "series_creators": {
        "type": "array",
        "description": "A list of the creators of the television series.",
        "items": {
          "type": "object",
          "properties": {
            "creator_name": {
              "type": "string",
              "description": "The name of a series creator."
            }
          },
          "required": [
            "creator_name"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "episode_title",
      "season_number",
      "series_name",
      "series_creators"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
