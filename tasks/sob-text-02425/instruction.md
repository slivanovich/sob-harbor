{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLove Stinks (film): Love Stinks is a 1999 American comedy film written and directed by Jeff Franklin and starring French Stewart, Bridgette Wilson, Bill Bellamy and Tyra Banks.\n\nThe Man Who Woke Up (1918 film): The Man Who Woke Up is a 1918 American silent film directed by James McLaughlin and featuring William V. Mong.\n\nOffice Space: Office Space is a 1999 American comedy film written and directed by Mike Judge.  It satirizes the everyday work life of a typical mid-to-late-1990s software company, focusing on a handful of individuals fed up with their jobs.  It stars Ron Livingston, Jennifer Aniston, Gary Cole, Stephen Root, David Herman, Ajay Naidu, and Diedrich Bader.\n\nLove's Sacrifice (film): Love's Sacrifice is a 1914 American silent short western film directed by George Osborne and featuring William Ehfe, Tsuru Aoki, Black Bull and Virginia Philley Withey in important roles.\n\nSee No Evil, Hear No Evil: See No Evil, Hear No Evil is a 1989 American comedy film directed by Arthur Hiller.  The film stars Richard Pryor as a blind man and Gene Wilder as a deaf man who work together to thwart a trio of murderous thieves.  This is the third film featuring Wilder and Pryor, who had appeared previously in the 1976 film \"Silver Streak\" and the 1980 film \"Stir Crazy\".  The film was released in the United States on May 12, 1989.\n\nThe Great McGinty: The Great McGinty is a 1940 political satire comedy film written and directed by Preston Sturges, starring Brian Donlevy and Akim Tamiroff and featuring William Demarest and (in her final screen appearance) Muriel Angelus.  It was Sturges's first film as a director; he sold the story to Paramount Pictures for just $10 on condition he direct the film.  Sturges went on to win the Academy Award for Writing Original Screenplay.\n\nRidin' Wild (1925 film): Ridin' Wild is a 1925 American western film directed by Leon De La Mothe a written by Robert J. Horner and Matilda Smith featuring William Barrymore.  The film was shot on location in Tucson, Arizona in 1924.  An 8mm print of the Film was acquired by the Tucson Historic Preservation Foundation and digitized and restored in 2011.  The film features the first 1924 Tucson Winter Rodeo: La Fiesta de los Vaqueros.\n\nFree Enterprise (film): Free Enterprise is a 1999 romantic comedy film starring Eric McCormack and Rafer Weigel, and featuring William Shatner, directed by Robert Meyer Burnett and written by Mark A. Altman and Burnett.\n\nBill Lumbergh: William \"Bill\" Lumbergh is a fictional character, who appeared initially in the Milton animated shorts, and later was portrayed by Gary Cole in the 1999 film \"Office Space\".  A caricature of corporate management, Lumbergh is a division Vice President of the software company \"Initech\", and serves as the main antagonist of the film.\n\nSouth Park: Bigger, Longer &amp; Uncut: South Park: Bigger, Longer & Uncut is a 1999 American adult animated musical comedy film based on the Comedy Central animated television series \"South Park\".  The film was directed by series creator Trey Parker and stars the regular television cast of Parker, Matt Stone, Mary Kay Bergman, and Isaac Hayes, with guest performances by George Clooney, Eric Idle and Mike Judge.  The film follows the four boys Stan Marsh, Kyle Broflovski, Eric Cartman, and Kenny McCormick as they sneak into an R-rated film featuring Canadian actors Terrance and Phillip and begin cursing incessantly.  Eventually, their mothers pressure the United States to wage war against Canada for allegedly corrupting their children.\n\nQuestion: Who directed the 1999 American comedy film featuring William \"Bill\" Lumbergh?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"featured_character\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character featured in the film.\"\n        },\n        \"actor_portraying_character\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who portrayed the character.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"actor_portraying_character\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_genre\",\n    \"director_name\",\n    \"featured_character\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "film_genre": {
        "type": "string",
        "description": "The primary genre of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "featured_character": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character featured in the film."
          },
          "actor_portraying_character": {
            "type": "string",
            "description": "The name of the actor who portrayed the character."
          }
        },
        "required": [
          "character_name",
          "actor_portraying_character"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "film_genre",
      "director_name",
      "featured_character"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
