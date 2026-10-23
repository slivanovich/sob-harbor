{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGeorgina Leonidas: Georgina Leonidas (born 28 February 1990) is an English actress best known for playing Molly in \"The Basil Brush Show\", and Katie Bell in \"Harry Potter and the Half-Blood Prince\" and \"Harry Potter and the Deathly Hallows – Part 2\".\n\nHarry Potter and the Half-Blood Prince: Harry Potter and the Half-Blood Prince is the sixth and penultimate novel in the \"Harry Potter\" series, written by British author J. K. Rowling.  Set during protagonist Harry Potter's sixth year at Hogwarts, the novel explores the past of Harry's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.\n\nHalf-Blood Prince (disambiguation): Half-Blood Prince generally refers to the novel \"Harry Potter and the Half-Blood Prince\" by J. K. Rowling.\n\nSuzie Toase: Suzie Toase or Suzanne Toase is a British actress who is possibly best known for her role as Alecto Carrow in the film adaptations of J. K. Rowling's \"Harry Potter and the Half-Blood Prince\" and \"Harry Potter and the Deathly Hallows – Part 1\" and \"Part 2\".\n\nLego Harry Potter: Years 5–7: Lego Harry Potter: Years 5–7 is a Lego-themed action-adventure video game developed by Traveller's Tales and published by Warner Bros.  Interactive Entertainment.  Released on 11 November 2011 in North America and 18 November in Europe, the game is based on the Lego Harry Potter line and is based on the final three books and four films in the \"Harry Potter\" series: \"Harry Potter and the Order of the Phoenix\", \"Harry Potter and the Half-Blood Prince\", \"Harry Potter and the Deathly Hallows – Part 1\", and \"Harry Potter and the Deathly Hallows – Part 2\".  The game was released for the PlayStation 3, Xbox 360, PlayStation Portable, PlayStation Vita, Wii, Nintendo DS, Nintendo 3DS, Microsoft Windows, iOS and Android.  The first trailer of three trailers was released 6 October 2011, and the demo was released on 1 November.  The game was released on Steam on 5 January 2012.  The OS X version of the game was released by Feral Interactive on 7 March 2012.  The game was released for the PlayStation 4 on October 21, 2016, as part of the \"Lego Harry Potter Collection\", which bundles the game with its predecessor, \"\".\n\nRob Knox: Robert Arthur Knox (21 August 1989 – 24 May 2008) was an English actor who portrayed the character of Marcus Belby in the film \"Harry Potter and the Half-Blood Prince\" (2009), and had signed to appear in the planned film \"Harry Potter and the Deathly Hallows\" (2010).\n\nHarry Potter and the Deathly Hallows: Harry Potter and the Deathly Hallows is the seventh and final novel of the \"Harry Potter\" series, written by British author J. K. Rowling.  The book was released on 21 July 2007, ten years after publication of \"Harry Potter and the Philosopher's Stone\" (1997), by Bloomsbury Publishing in the United Kingdom, in the United States by Scholastic, and in Canada by Raincoast Books, ending the series that began in 1997 with the publication of \"Harry Potter and the Philosopher's Stone\".  The novel chronicles the events directly following \"Harry Potter and the Half-Blood Prince\" (2005), and the final confrontation between the wizards Harry Potter and Lord Voldemort, as well as revealing the previously concealed back story of several main characters.  The title of the book refers to three mythical objects featured in the story, collectively known as the \"Deathly Hallows\"—an unbeatable wand, a stone to bring the dead to life, and a cloak of invisibility.\n\nTom Felton: Thomas Andrew Felton (born September 22, 1987) is an English actor.  Felton began appearing in commercials when he was eight years old for companies such as Commercial Union and Barclaycard.  He made his screen debut in the role of Peagreen Clock in \"The Borrowers\" (1997) and he portrayed Louis T. Leonowens in \"Anna and the King\" (1999).  He rose to prominence for his role as Draco Malfoy in the film adaptions of the best-selling \"Harry Potter\" fantasy novels by J.K. Rowling.  His performances in \"Harry Potter and the Half-Blood Prince\" and \"Harry Potter and the Deathly Hallows – Part 1\" won him two consecutive MTV Movie Awards for Best Villain in 2010 and 2011.\n\nHarry Potter and the Half-Blood Prince (film): Harry Potter and the Half-Blood Prince is a 2009 British-American fantasy film directed by David Yates and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film, which is the sixth instalment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by David Heyman and David Barron.  The story follows Harry Potter's sixth year at Hogwarts as he receives a mysterious textbook, falls in love, and attempts to retrieve a memory that holds the key to Lord Voldemort's downfall.\n\nVincent Cirelli: Vincent Cirelli is a special effects supervisor.  Known for his works at Luma Pictures as a visual effects supervisor in acclaimed films such as \"\" (2007), \"No Country for Old Men\" (2007), \"The Midnight Meat Train\" (2008), \"\" (2008), \"Harry Potter and the Half-Blood Prince\" (2009), \"The Book of Eli\" (2010), \"\" (2011), \"\" (2012), \"Prometheus\" (2012), \"The Avengers\" (2012), \"Saving Mr. Banks\" (2013), \"Guardians of the Galaxy\" (2014), \"\" (2015), \"In the Heart of the Sea\" (2015), \"Deadpool\" (2015) and \"Doctor Strange\" (2016), for which he received an Academy Award for Best Visual Effects nomination at the 89th Academy Awards.\n\nQuestion: Who is Harry's nemesis in the Half-Blood Prince?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"harry_potter_character\": {\n      \"type\": \"string\",\n      \"description\": \"The main protagonist character.\"\n    },\n    \"nemesis_character\": {\n      \"type\": \"string\",\n      \"description\": \"The character identified as the nemesis.\"\n    },\n    \"context_work\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the work where the nemesis is identified.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the work (e.g., novel, film).\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"harry_potter_character\",\n    \"nemesis_character\",\n    \"context_work\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "harry_potter_character": {
        "type": "string",
        "description": "The main protagonist character."
      },
      "nemesis_character": {
        "type": "string",
        "description": "The character identified as the nemesis."
      },
      "context_work": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the work where the nemesis is identified."
          },
          "type": {
            "type": "string",
            "description": "The type of the work (e.g., novel, film)."
          }
        },
        "required": [
          "title",
          "type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "harry_potter_character",
      "nemesis_character",
      "context_work"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
