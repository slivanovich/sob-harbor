{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDomino Vitali: Dominetta Vitali, known simply as Domino, is a fictional character and the main Bond girl in the James Bond novel, \"Thunderball\".  For the 1965 film adaptation of the same name, her name was changed to Dominique Derval, nicknamed Domino, and she was portrayed by French actress Claudine Auger.  In the 1983 film adaptation \"Never Say Never Again\", her character was renamed Domino Petachi and she was portrayed by American actress Kim Basinger.\n\nThe Natural (film): The Natural is a 1984 American sports drama film adaptation of Bernard Malamud's 1952 baseball novel of the same name, directed by Barry Levinson and starring Robert Redford, Glenn Close, and Robert Duvall.  The film, like the book, recounts the experiences of Roy Hobbs, an individual with great \"natural\" baseball talent, spanning decades of Roy's success and his suffering.  It was the first film produced by TriStar Pictures.\n\nThe Marrying Man: The Marrying Man (known as Too Hot to Handle in the United Kingdom and Australia) is an American 1991 romantic comedy film starring Alec Baldwin and Kim Basinger.  The film was directed by Jerry Rees, and written by Neil Simon.  The film opened to poor reviews and flopped at the box office, with Basinger's performance in the film earning her a Golden Raspberry Award nomination for Worst Actress, where she lost to Sean Young for \"A Kiss Before Dying\".\n\nKim Basinger filmography: Kim Basinger is an American actress who made her television debut as Sheila in \"Night Train to Dallas\", an episode of the action/adventure drama series \"Gemini Man\" that aired on NBC in 1976.  She starred in two canceled series as well as several made-for-TV films, including a remake of \"From Here to Eternity\" (1979).  Her feature film debut was in 1981 drama \"Hard Country\".  Basinger came to prominence playing Bond girl Domino Petachi in the 1983 film \"Never Say Never Again\", opposite Sean Connery, and went on to receive a Golden Globe nomination for her role as Memo Paris in \"The Natural\" (1984).  She also starred as Elizabeth in the controversial erotic romantic drama \"9½ Weeks\" (1986) with Mickey Rourke, as the title character in \"Nadine\" with Jeff Bridges (1987) and as Vicki Vale in Tim Burton's blockbuster \"Batman\" (1989), which remains the highest-grossing film of her career.\n\nGemini Man: Gemini Man is an American action-adventure drama miniseries that aired on NBC in 1976.  The third television series based on the H. G. Wells science fiction novel, \"The Invisible Man\", \"Gemini Man\" was created to replace the previous season's \"The Invisible Man\" (1975 TV series), utilizing simpler and less expensive special effects.\n\nSandra Bullock filmography: Sandra Bullock is an American actress who made her film debut with a minor role in the 1987 thriller \"Hangmen\".  She made her television debut in the television film \"Bionic Showdown: The Six Million Dollar Man and the Bionic Woman\" (1989) and played the lead role in the short-lived sitcom \"Working Girl\" (1990) before making her breakthrough starring in the action film \"Speed\" (1994).  She starred with Sylvester Stallone in \"Demolition Man\" (1994).  Bullock founded her own production company, Fortis Films, and starred in the romantic comedy \"While You Were Sleeping\" in 1995.  Her performance in the film earned her first nomination for the Golden Globe Award for Best Actress – Motion Picture Comedy or Musical.  The following year, Bullock starred with Matthew McConaughey in the film adaptation of John Grisham's novel \"A Time to Kill\" (1996).  In 1997, she reprised her \"Speed\" role in the sequel, \"\".  The following year, Bullock starred in the romantic comedy \"Practical Magic\", voiced Miriam in the animated biblical film \"The Prince of Egypt\" and also executive produced her first film, the romantic drama \"Hope Floats\".\n\nBang the Drum Slowly (film): Bang the Drum Slowly is a 1973 American sports drama film directed by John D. Hancock, about a baseball player of limited intellect who has a terminal illness, and his brainier, more skilled teammate.  It is film adaptation of the 1956 baseball novel of the same name by Mark Harris.  It was previously dramatized in 1956 on the \"U.S. Steel Hour\" with Paul Newman, Albert Salmi and George Peppard.\n\nBernard Malamud: Bernard Malamud (April 26, 1914 – March 18, 1986) was an American novelist and short story writer.  Along with Saul Bellow and Philip Roth, he was one of the best known American Jewish authors of the 20th century.  His baseball novel, \"The Natural\", was adapted into a 1984 film starring Robert Redford.  His 1966 novel \"The Fixer\" (also filmed), about antisemitism in Tsarist Russia, won both the National Book Award and the Pulitzer Prize.\n\nGeraldine Chaplin: Geraldine Leigh Chaplin (born July 31, 1944) is a prolific actress of English, French, and Spanish language films, the fourth child of Charlie Chaplin, the first of eight with fourth wife Oona O'Neill.  After beginnings in dance and modeling, she turned her attention to acting, and made her American acting debut (and came to prominence in what would be a Golden Globe–nominated role) in her portrayal of Tonya in David Lean's \"Doctor Zhivago\" (1965).  She made her Broadway acting debut in Lillian Hellman's \"The Little Foxes\" in 1967, and received her second Golden Globe nomination for Robert Altman's \"Nashville\" (1975).  She also appeared in his other pictures, including \"Buffalo Bill and the Indians, or Sitting Bull's History Lesson\" (1976), and \"A Wedding\" (1978).  She received a BAFTA nomination for her role in \"Welcome to L.A.\" (1976), and then appeared in \"Roseland\" (1977) and \"Remember My Name\" (1978).  She played her grandmother Hannah Chaplin in the biopic, \"Chaplin\" (1992) for which she received her third Golden Globe nomination.  She also appeared in \"The Age of Innocence\" (1993), \"Jane Eyre\" (1996), \"\" (1997), and a decade later, in \"The Wolfman\" (2010).\n\nRupert Everett: Rupert James Hector Everett ( ; born 29 May 1959) is an English actor and writer.  He first came to public attention in 1981, when he was cast in Julian Mitchell's play and subsequent film \"Another Country\" (1984) as an openly gay pupil at an English public school in the 1930s; the role earned him his first BAFTA Award nomination.  He went on to receive a second BAFTA Award nomination and his first Golden Globe Award nomination for his role in \"My Best Friend's Wedding\" (1997), followed by a second Golden Globe nomination for \"An Ideal Husband\" (1999).\n\nQuestion: Kim Basinger is an American actress who made her television debut as Sheila in \"Night Train to Dallas\", an episode of the action/adventure drama series \"Gemini Man\", Basinger went on to receive a Golden Globe nomination for her role as Memo Paris in which 1984 American sports drama film adaptation of Bernard Malamud's 1952 baseball novel of the same name, directed by Barry Levinson?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"source_novel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"novel_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel the film is adapted from.\"\n        },\n        \"novel_author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the novel.\"\n        },\n        \"novel_publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The publication year of the novel.\"\n        }\n      },\n      \"required\": [\n        \"novel_title\",\n        \"novel_author\",\n        \"novel_publication_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actress_performance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actress_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character portrayed by the actress.\"\n        },\n        \"award_nomination\": {\n          \"type\": \"string\",\n          \"description\": \"The award nomination received for the role.\"\n        }\n      },\n      \"required\": [\n        \"actress_name\",\n        \"character_name\",\n        \"award_nomination\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"film_director\",\n    \"source_novel_details\",\n    \"actress_performance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the film."
      },
      "source_novel_details": {
        "type": "object",
        "properties": {
          "novel_title": {
            "type": "string",
            "description": "The title of the novel the film is adapted from."
          },
          "novel_author": {
            "type": "string",
            "description": "The author of the novel."
          },
          "novel_publication_year": {
            "type": "integer",
            "description": "The publication year of the novel."
          }
        },
        "required": [
          "novel_title",
          "novel_author",
          "novel_publication_year"
        ],
        "additionalProperties": false
      },
      "actress_performance": {
        "type": "object",
        "properties": {
          "actress_name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "character_name": {
            "type": "string",
            "description": "The name of the character portrayed by the actress."
          },
          "award_nomination": {
            "type": "string",
            "description": "The award nomination received for the role."
          }
        },
        "required": [
          "actress_name",
          "character_name",
          "award_nomination"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "film_director",
      "source_novel_details",
      "actress_performance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
