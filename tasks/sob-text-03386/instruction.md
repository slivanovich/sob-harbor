{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCatch Me If You Can: Catch Me If You Can is a 2002 American biographical crime film based on the life of Frank Abagnale, who, before his 19th birthday, successfully performed cons worth millions of dollars by posing as a Pan American World Airways pilot, a Georgia doctor and a Louisiana parish prosecutor.  His primary crime was check fraud; he became so experienced that the FBI eventually turned to him for help in catching other check forgers.  The film was directed by Steven Spielberg and stars Leonardo DiCaprio and Tom Hanks, with Christopher Walken, Martin Sheen, and Nathalie Baye in supporting roles.\n\nCatch Me if You Can (book): Catch Me if You Can is the autobiography of Frank Abagnale, a former con artist who, as a young man, cashed $2.5 million worth of bad checks while impersonating a Pan Am pilot, a doctor, a teacher, and an attorney.  The book is co-written by Stan Redding, and was adapted into a 2002 film of the same name by director Steven Spielberg, starring Leonardo DiCaprio as Abagnale and Tom Hanks as the FBI agent who pursued him.\n\nSaving Private Ryan: Saving Private Ryan is a 1998 American epic war drama film set during the Invasion of Normandy in World War II.  Directed by Steven Spielberg and written by Robert Rodat, the film is notable for its graphic portrayal of war, and for the intensity of its opening 27 minutes, which includes a depiction of the Omaha Beach assault during the Normandy landings.  It follows United States Army Rangers Captain John H. Miller (Tom Hanks) and a squad (Tom Sizemore, Edward Burns, Barry Pepper, Giovanni Ribisi, Vin Diesel, Adam Goldberg, and Jeremy Davies) as they search for a paratrooper, Private First Class James Francis Ryan (Matt Damon), who is the last-surviving brother of four servicemen.\n\nBridge of Spies (film): Bridge of Spies is a 2015 historical drama legal thriller film directed and co-produced by Steven Spielberg, written by Matt Charman, Ethan and Joel Coen and stars Tom Hanks, Mark Rylance, Amy Ryan, and Alan Alda.  Set during the Cold War, the film tells the story of lawyer James B. Donovan, who is entrusted with negotiating the release of Francis Gary Powers—a U.S. Air Force pilot whose U-2 spy plane was shot down over the Soviet Union in 1960—in exchange for Rudolf Abel, a convicted Soviet KGB spy held under the custody of the United States, whom he represented at trial.  The name of the film refers to the Glienicke Bridge, which connects Potsdam with Berlin, where the prisoner exchange took place.  The film was an international co-production of the United States and Germany.\n\nThe Last Shot: The Last Shot is a 2004 comedy film starring Matthew Broderick, Alec Baldwin, Toni Collette, Tim Blake Nelson, Joan Cusack (uncredited), Tony Shalhoub, Buck Henry, Ray Liotta, Calista Flockhart and Ian Gomez.  The movie is written and directed by Jeff Nathanson, who wrote \"Catch Me If You Can\" and \"The Terminal\".\n\nThe Post (film): The Post is an upcoming historical drama film directed and co-produced by Steven Spielberg from a script written by Liz Hannah and Josh Singer and starring Tom Hanks and Meryl Streep.\n\nThe Money Pit: The Money Pit is a 1986 American comedy film directed by Richard Benjamin starring Tom Hanks and Shelley Long as a couple who attempt to renovate a recently purchased house.  It was filmed in New York City and Lattingtown, New York, and was co-executive produced by Steven Spielberg.\n\nCatch Me If You Can (soundtrack): Catch Me If You Can: Music from the Motion Picture is the original soundtrack of the 2002 film of the same name, starring Leonardo DiCaprio, Tom Hanks, Christopher Walken, Martin Sheen and Amy Adams.  The original score was composed by John Williams.  The film was the twentieth collaboration between Williams and director Steven Spielberg.\n\nYou've Got Mail: You've Got Mail is a 1998 American romantic comedy-drama film directed by Nora Ephron, co-written by Nora and Delia Ephron, and starring Tom Hanks and Meg Ryan.  The film is about two people in an online romance who are unaware that they are also business rivals.  It marks the third coupling of stars Tom Hanks and Meg Ryan, who had previously appeared together in \"Joe Versus the Volcano\" (1990) and \"Sleepless in Seattle\" (1993).\n\nThe Terminal: The Terminal is a 2004 American comedy-drama film directed by Steven Spielberg and starring Tom Hanks and Catherine Zeta-Jones.  The film is about a man who becomes stuck in New York's John F. Kennedy Airport terminal when he is denied entry into the United States and at the same time cannot return to his native country because of a military coup.\n\nQuestion: Who wrote the script for a 2002 film directed by Steven Spielberg starring Tom Hanks?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"lead_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the main actors in the film.\"\n    },\n    \"scriptwriter\": {\n      \"type\": \"string\",\n      \"description\": \"The person who wrote the script for the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director\",\n    \"lead_actors\",\n    \"scriptwriter\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The year the film was released."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "lead_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the main actors in the film."
      },
      "scriptwriter": {
        "type": "string",
        "description": "The person who wrote the script for the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director",
      "lead_actors",
      "scriptwriter"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
