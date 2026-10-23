{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMars Attacks!: Mars Attacks!  is a 1996 American comic science fiction film directed by Tim Burton, who also co-produced it with Larry J. Franco.  The screenplay, which was based on the cult trading card series of the same name, was written by Jonathan Gems.  The film features an ensemble cast consisting of Jack Nicholson (in a dual role), Glenn Close, Annette Bening, Pierce Brosnan, Danny DeVito, Martin Short, Sarah Jessica Parker, Michael J. Fox, Rod Steiger, Tom Jones, Lukas Haas, Natalie Portman, Jim Brown, Lisa Marie Smith, and Sylvia Sidney.  The film is a parody of science fiction B movies overall and includes elements of black comedy and political satire.\n\nHenry Hopper: Henry Lee Hopper (born September 11, 1990) is an American actor.  He is son of actor and director Dennis Hopper and actress Katherine LaNasa.\n\nJames Cameron filmography: James Cameron is a Canadian director, screenwriter, and producer who has had an extensive career in film and television.  Cameron's debut was the 1978 science fiction short \"Xenogenesis\", which he directed, wrote and produced.  In the early part of his career, he did various technical jobs such as special visual effects producer, set dresser assistant, matte artist, and photographer.  His feature directorial debut was the 1981 release \"\".  The next film he directed was the science fiction action thriller \"The Terminator\" (1984).  It starred Arnold Schwarzenegger as the titular cyborg assassin, and was Cameron's breakthrough feature.  In 1986, he directed and wrote the science fiction action sequel \"Aliens\" starring Sigourney Weaver.  He followed this by directing another science fiction film \"The Abyss\" (1989).  In 1991, Cameron directed the sequel to \"The Terminator\", \"\" (with Schwarzenegger reprising his role), and also executive produced the action crime film \"Point Break\".  Three years later he directed a third Schwarzenegger-starring action film \"True Lies\" (1994).\n\nCatchfire: Catchfire is a 1990 American action thriller film directed by Dennis Hopper and starring Jodie Foster, Dennis Hopper, Fred Ward and Vincent Price.  Several other notable actors have cameos.  The film was disowned by Hopper before release and he is therefore credited under the fictional pseudonym Alan Smithee.  The original screenplay was written by Rachel Kronstadt Mann, then re-written by Ann Louise Bardach, who was hired by Dennis Hopper and producer Steven Reuther.  During the 1988 Writers Guild of America strike, Hopper hired Alex Cox to do another polish while the film was shooting.\n\nSpace Chimps: Space Chimps is a 2008 3D computer-animated comic science fiction film directed by Kirk DeMicco and written by DeMicco and Rob Moreland.  It features the voices of Andy Samberg, Cheryl Hines, Jeff Daniels, Patrick Warburton, Kristin Chenoweth, Kenan Thompson, Zack Shada, Carlos Alazraqui, Omid Abtahi, Patrick Breen, Jane Lynch, Kath Soucie, and Stanley Tucci.  The film follows three chimpanzees who go into space to an alien planet.\n\nStephen Dorff: Stephen Dorff Jr. (born July 29, 1973) is an American actor, known for portraying PK in \"The Power of One\", Stuart Sutcliffe in \"Backbeat\", Johnny Marco in Sofia Coppola's \"Somewhere\", and for his roles in \"Blade\" (as self-styled vampire-overlord Deacon Frost), \"Cecil B. DeMented\", \"The Motel Life\", \"S.F.W.\" and \"Space Truckers\".\n\nDennis Hopper: Dennis Lee Hopper (May 17, 1936 – May 29, 2010) was an American actor, filmmaker, photographer and artist.  He attended the Actors Studio, made his first television appearance in 1954, and soon after appeared alongside James Dean in \"Rebel Without a Cause\" (1955) and \"Giant\" (1956).  In the next ten years he made a name in television, and by the end of the 1960s had appeared in several films.  Hopper also began a prolific and acclaimed photography career in the 1960s.\n\nSpace Truckers: Space Truckers is a 1996 American-British-Irish comic science fiction film directed by Stuart Gordon and starring Dennis Hopper, Stephen Dorff, Debi Mazar and Charles Dance.  It was filmed at Ardmore Studios, County Wicklow, Ireland.\n\nThe American Way (film): The American Way, also known as Riders of the Storm, is a 1986 American science fiction comedy film directed by Maurice Phillips and starring Dennis Hopper and Michael J. Pollard.\n\nOut of the Blue (1980 film): Out of the Blue (released in Canada as No Looking Back) is a 1980 Canadian drama film directed by and starring Dennis Hopper.  The film was written and produced by Gary Jules Jouvenat.  It competed for the Palme d'Or at the 1980 Cannes Film Festival.  This was the first film Hopper directed since 1971's \"The Last Movie\", stepping in at the last minute to replace the original director (screenwriter Leonard Yakir).\n\nQuestion: Space Truckers is a 1996 American-British-Irish comic science fiction film, starring Dennis Lee Hopper, the American actor, filmmaker, photographer and artist, who directed it?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"dennis_hopper_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role Dennis Hopper played in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"director_name\",\n    \"dennis_hopper_role\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "dennis_hopper_role": {
        "type": "string",
        "description": "The role Dennis Hopper played in the film."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "director_name",
      "dennis_hopper_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
