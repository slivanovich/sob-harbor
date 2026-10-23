{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHarry Potter and the Half-Blood Prince (film): Harry Potter and the Half-Blood Prince is a 2009 British-American fantasy film directed by David Yates and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film, which is the sixth instalment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by David Heyman and David Barron.  The story follows Harry Potter's sixth year at Hogwarts as he receives a mysterious textbook, falls in love, and attempts to retrieve a memory that holds the key to Lord Voldemort's downfall.\n\nLego Harry Potter: Lego \"Harry Potter\" is a Lego theme based on the films of the \"Harry Potter\" series.  Lego models of important scenes, vehicles and characters were made for the first six films and all the books released.  The first sets appeared in 2001, to coincide with the release of the first film \"Harry Potter and the Philosopher's Stone\" (Harry Potter and the Sorcerer's Stone in the United States).  Subsequent sets were released alongside the new films, until Harry Potter and the Order of the Phoenix.  The line then went dormant for three years.  It is unknown if the theme will again be revived to coincide with future installations in the Harry Potter franchise, such as the film Fantastic Beasts and Where to Find Them.\n\nHarry Potter and the Order of the Phoenix (film): Harry Potter and the Order of the Phoenix is a 2007 British-American fantasy film directed by David Yates and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film, which is the fifth instalment in the \"Harry Potter\" film series, was written by Michael Goldenberg (making this the only film in the series not to be scripted by Steve Kloves) and produced by David Heyman and David Barron.  The story follows Harry Potter's fifth year at Hogwarts as the Ministry of Magic is in denial of Lord Voldemort's return.\n\nHarry Potter and the Deathly Hallows – Part 2: Harry Potter and the Deathly Hallows – Part 2 is a 2011 British-American fantasy film directed by David Yates and distributed by Warner Bros.  Pictures.  It is the second of two cinematic parts based on the novel of the same name by J. K. Rowling.  The film, which is the eighth and final instalment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by David Heyman, David Barron, and Rowling.  It is the sequel to \"Harry Potter and the Deathly Hallows – Part 1\".  The story continues to follow Harry Potter's quest to find and destroy Lord Voldemort's Horcruxes in order to stop him once and for all.\n\nHarry Potter and the Prisoner of Azkaban (film): Harry Potter and the Prisoner of Azkaban is a 2004 British-American fantasy film directed by Alfonso Cuarón and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film, which is the third instalment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by Chris Columbus (director of the first two instalments), David Heyman, and Mark Radcliffe.  The story follows Harry Potter's third year at Hogwarts as he is informed that a prisoner named Sirius Black has escaped from Azkaban intending to kill him.\n\nThe Amazing Spider-Man (2012 film): The Amazing Spider-Man is a 2012 American superhero film based on the Marvel Comics character Spider-Man, and sharing the title of the character's longest-running comic book.  It is the fourth theatrical \"Spider-Man\" film produced by Columbia Pictures and Marvel Entertainment, and a reboot of Sam Raimi's \"Spider-Man\" 2002-2007 trilogy preceding it.  The film was directed by Marc Webb.  It was written by James Vanderbilt, Alvin Sargent and Steve Kloves and it stars Andrew Garfield as Peter Parker / Spider-Man, Emma Stone as Gwen Stacy, Rhys Ifans as Dr. Curtis Connors, Denis Leary as NYPD Captain George Stacy, along with Martin Sheen and Sally Field as the uncle and aunt of Peter Parker, Ben Parker and May Parker.  The film tells the story of Peter Parker, a teenager from New York who becomes Spider-Man after being bitten by a genetically altered spider.  Parker must stop Dr. Curt Connors as a mutated lizard, from spreading a mutation serum to the city's human population.\n\nHarry Potter and the Deathly Hallows – Part 1: Harry Potter and the Deathly Hallows – Part 1 is a 2010 British-American fantasy film directed by David Yates and distributed by Warner Bros.  Pictures.  It is the first of two cinematic parts based on the novel of the same name by J. K. Rowling and features an ensemble cast.  The film, which is the seventh and penultimate installment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by David Heyman, David Barron, and Rowling.\n\nWonder Boys (film): Wonder Boys is a 2000 comedy-drama film directed by Curtis Hanson and written by Steve Kloves.  An international co-production between the United States, the United Kingdom, Germany, and Japan, it is based on the novel of the same name by Michael Chabon.  Michael Douglas stars as professor Grady Tripp, a novelist who teaches creative writing at an unnamed Pittsburgh university.  He has been unable to finish his second novel, his young wife has left him, and he is having an affair with the Chancellor of the university (Frances McDormand), who is the wife of the chairman of his department.  Grady's editor (Robert Downey, Jr.) is in town to see his new book and becomes interested in a book that one of Grady's students (Tobey Maguire) has just completed.\n\nHarry Potter and the Goblet of Fire (film): Harry Potter and the Goblet of Fire is a 2005 British-American fantasy film directed by Mike Newell and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film, which is the fourth instalment in the \"Harry Potter\" film series, was written by Steve Kloves and produced by David Heyman.  The story follows Harry Potter's fourth year at Hogwarts as he is chosen by the Goblet of Fire to compete in the Triwizard Tournament.\n\nHarry Potter and the Philosopher's Stone (film): Harry Potter and the Philosopher's Stone (released in some countries as Harry Potter and the Sorcerer's Stone) is a 2001 British-American fantasy film directed by Chris Columbus and distributed by Warner Bros.  Pictures.  It is based on the novel of the same name by J. K. Rowling.  The film is the first instalment in the long-running \"Harry Potter\" film series, and was written by Steve Kloves and produced by David Heyman.  Its story follows Harry Potter's first year at Hogwarts School of Witchcraft and Wizardry as he discovers that he is a famous wizard and begins his education.  The film stars Daniel Radcliffe as Harry Potter, with Rupert Grint as Ron Weasley, and Emma Watson as Hermione Granger.\n\nQuestion: What movie had Legos based off of it and was written by Steve Kloves?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie that meets the specified criteria.\"\n    },\n    \"criteria_met\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"has_lego_theme\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if Lego models were based on this movie.\"\n        },\n        \"written_by_steve_kloves\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if Steve Kloves was one of the writers for this movie.\"\n        }\n      },\n      \"required\": [\n        \"has_lego_theme\",\n        \"written_by_steve_kloves\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_series_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"series_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the film series the movie belongs to.\"\n        },\n        \"installment_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The sequential number of this movie within its film series.\"\n        }\n      },\n      \"required\": [\n        \"series_name\",\n        \"installment_number\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation of why this movie fits both criteria based on the context.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"criteria_met\",\n    \"film_series_info\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie that meets the specified criteria."
      },
      "criteria_met": {
        "type": "object",
        "properties": {
          "has_lego_theme": {
            "type": "boolean",
            "description": "True if Lego models were based on this movie."
          },
          "written_by_steve_kloves": {
            "type": "boolean",
            "description": "True if Steve Kloves was one of the writers for this movie."
          }
        },
        "required": [
          "has_lego_theme",
          "written_by_steve_kloves"
        ],
        "additionalProperties": false
      },
      "film_series_info": {
        "type": "object",
        "properties": {
          "series_name": {
            "type": "string",
            "description": "The name of the film series the movie belongs to."
          },
          "installment_number": {
            "type": "integer",
            "description": "The sequential number of this movie within its film series."
          }
        },
        "required": [
          "series_name",
          "installment_number"
        ],
        "additionalProperties": false
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation of why this movie fits both criteria based on the context."
      }
    },
    "required": [
      "movie_title",
      "criteria_met",
      "film_series_info",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
