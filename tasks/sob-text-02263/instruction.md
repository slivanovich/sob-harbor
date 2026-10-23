{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Maze Runner (series): The Maze Runner is a series of young adult dystopian science fiction novels written by American author James Dashner.  The series consists of \"The Maze Runner\" (2009), \"The Scorch Trials\" (2010) and \"The Death Cure\" (2011), as well as the two prequel novels, \"The Kill Order\" (2012) and \"The Fever Code\" (2016), and a companion book titled \"The Maze Runner Files\" (2013).\n\nThe Death Cure: The Death Cure is a 2011 young adult dystopian science fiction novel written by American writer James Dashner and the third book, fifth chronologically, in the \"Maze Runner\" series.  It was published on October 11, 2011 by Delacorte Press and was preceded by \"The Maze Runner\" and \"The Scorch Trials\" and followed by the series prequels, \"The Kill Order and The Fever Code.\"\n\nThe Eye of Minds: The Eye of Minds is a 2013 teenage science fiction novel written by American author James Dashner, and the first book in \"The Mortality Doctrine\" series.  The book was first published on October 8, 2013 by Delacorte Press and is set in a futuristic world where a young gamer must help stop a rogue hacker intent on causing mass destruction.\n\nThe Maze Runner (film): The Maze Runner is a 2014 American dystopian science fiction action thriller film directed by Wes Ball, in his directorial debut, based on James Dashner's 2009 novel of the same name.  The film is the first installment in \"The Maze Runner\" film series and was produced by Ellen Goldsmith-Vein, Wyck Godfrey, Marty Bowen, and Lee Stollman with a screenplay by Noah Oppenheim, Grant Pierce Myers, and T.S. Nowlin.  The film stars Dylan O'Brien, Kaya Scodelario, Aml Ameen, Thomas Brodie-Sangster, Ki Hong Lee, Will Poulter, and Patricia Clarkson.  The story follows sixteen-year-old Thomas, portrayed by O'Brien, who awakens in a rusty elevator with no memory of who he is, only to learn he's been delivered to the middle of an intricate maze, along with a large number of other boys, who have been trying to find their way out of the ever-changing labyrinth — all while establishing a functioning society in what they call the Glade.\n\nMaze Runner: The Scorch Trials: Maze Runner: The Scorch Trials (stylized onscreen simply as The Scorch Trials) is a 2015 American dystopian science fiction action thriller film based on James Dashner's novel \"The Scorch Trials\", the second novel in \"The Maze Runner\" book series.  The film is the sequel to the 2014 film \"The Maze Runner\" and the second installment in \"The Maze Runner\" film series.  It was directed by Wes Ball, with a screenplay by T.S. Nowlin.  Adding to the original film's cast of Dylan O'Brien, Kaya Scodelario, Thomas Brodie-Sangster, Dexter Darden, Alexander Flores, Ki Hong Lee, and Patricia Clarkson, the new supporting cast includes Nathalie Emmanuel, Giancarlo Esposito, Aidan Gillen, Jacob Lofland, Barry Pepper, Rosa Salazar, Lili Taylor, and Alan Tudyk.\n\nAndre Norton Award: The Andre Norton Award for Young Adult Science Fiction and Fantasy is an annual award presented by the Science Fiction and Fantasy Writers of America (SFWA) to the author of the best young adult or middle grade science fiction or fantasy book published in the United States in the preceding year.  It is named to honor prolific science fiction and fantasy author Andre Norton (1912–2005), and it was established by then SFWA president Catherine Asaro and the SFWA Young Adult Fiction committee and announced on February 20, 2005.  Any published young adult or middle grade science fiction or fantasy novel is eligible for the prize, including graphic novels.  There is no limit on word count.  The award is presented along with the Nebula Awards and follows the same rules for nominations and voting; as the awards are separate, works may be simultaneously nominated for both the Andre Norton award and a Nebula Award.\n\nThe Scorch Trials: The Scorch Trials is a 2010 young adult post-apocalyptic dystopian science fiction novel written by American author James Dashner and the second book, fourth chronologically, in \"The Maze Runner\" series.  The novel was published on September 18, 2010 by Delacorte Press.  It is preceded by \"The Maze Runner\", and followed by \"The Death Cure\".  A was released on September 18, 2015 by 20th Century Fox.\n\nThe Maze Runner: The Maze Runner is a 2009 young adult post-apocalyptic dystopian science fiction novel written by American author James Dashner and the first book released in \"The Maze Runner\" series, although it is the third chronologically.  The novel was published on October 7, 2009 by Delacorte Press, an imprint of Random House, and was made into a 2014 major motion picture by 20th Century Fox.\n\nThe Kill Order: The Kill Order is a 2012 young adult dystopian science fiction novel written by American author James Dashner and published on August 14, 2012 by Delacorte Press.  It is the first prequel book in \"The Maze Runner\" series and the fourth installment overall.  The book is set prior to the events of \"The Fever Code\" and 13 years before \"The Maze Runner\" book.\n\nThe Fever Code: The Fever Code is a 2016 young adult dystopian science fiction novel written by American author James Dashner and published on September 27, 2016 by Delacorte Press.  It is the second prequel book in \"The Maze Runner\" series and the fifth installment overall.  The book is chronologically set in between the events of \"The Kill Order\" and immediately before \"The Maze Runner\" book.\n\nQuestion: Which young adult dystopian science fiction novel by James Dashner was published in 2010?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel.\"\n    },\n    \"author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the novel.\"\n    },\n    \"publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the novel was published.\"\n    },\n    \"genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres the novel belongs to.\"\n    },\n    \"series_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"series_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the book series.\"\n        },\n        \"book_number_in_series\": {\n          \"type\": \"integer\",\n          \"description\": \"The sequential number of the book within its series.\"\n        },\n        \"chronological_position\": {\n          \"type\": \"integer\",\n          \"description\": \"The chronological position of the book within its series' timeline.\"\n        }\n      },\n      \"required\": [\n        \"series_name\",\n        \"book_number_in_series\",\n        \"chronological_position\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"publisher\": {\n      \"type\": \"string\",\n      \"description\": \"The publisher of the novel.\"\n    }\n  },\n  \"required\": [\n    \"novel_title\",\n    \"author\",\n    \"publication_year\",\n    \"genre\",\n    \"series_information\",\n    \"publisher\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "novel_title": {
        "type": "string",
        "description": "The title of the novel."
      },
      "author": {
        "type": "string",
        "description": "The author of the novel."
      },
      "publication_year": {
        "type": "integer",
        "description": "The year the novel was published."
      },
      "genre": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres the novel belongs to."
      },
      "series_information": {
        "type": "object",
        "properties": {
          "series_name": {
            "type": "string",
            "description": "The name of the book series."
          },
          "book_number_in_series": {
            "type": "integer",
            "description": "The sequential number of the book within its series."
          },
          "chronological_position": {
            "type": "integer",
            "description": "The chronological position of the book within its series' timeline."
          }
        },
        "required": [
          "series_name",
          "book_number_in_series",
          "chronological_position"
        ],
        "additionalProperties": false
      },
      "publisher": {
        "type": "string",
        "description": "The publisher of the novel."
      }
    },
    "required": [
      "novel_title",
      "author",
      "publication_year",
      "genre",
      "series_information",
      "publisher"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
