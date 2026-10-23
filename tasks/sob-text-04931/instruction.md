{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGod Bless the Child (film): God Bless the Child is a 1988 film, directed by Lary Elikann.  It depicts the struggle of homelessness and the perpetual cycle of poverty and how it affects people, and tells the story of the sacrifices of a single mother, Theresa Johnson (played by Mare Winningham), in hope of a better life for her daughter, Hillary Johnson (played by Grace Johnston).\n\nA Short Film About Killing: A Short Film About Killing (Polish: \"Krótki film o zabijaniu\" ) is a 1988 film directed by Krzysztof Kieślowski and starring Mirosław Baka, Krzysztof Globisz, and Jan Tesarz.  Written by Krzysztof Kieślowski and Krzysztof Piesiewicz, the film was expanded from \"\" of the Polish television series \"Dekalog\".  Set in Warsaw, Poland, the film compares the senseless, violent murder of an individual to the cold, calculated execution by the state.  \"A Short Film About Killing\" won both the Jury Prize and the FIPRESCI Prize at the 1988 Cannes Film Festival, as well as the European Film Award for Best Film.\n\nChocolat (1988 film): Chocolat is a 1988 film directed by Claire Denis, about a French family that lives in colonial Cameroon.  Marc and Aimée Dalens (François Cluzet and Giulia Boschi) are the parents of France (Cécile Ducasse), a young girl who befriends Protée (Isaach De Bankolé), a Cameroon native who is the family's household servant.  The film was entered into the 1988 Cannes Film Festival.\n\nAlice in Wonderland (1988 film): Alice in Wonderland is an Australian 51-minute direct-to-video animated film from Burbank Films Australia.  It was originally released in 1988.  The film is based on Lewis Carroll's classic English novel, \"Alice's Adventures in Wonderland\", first published in 1865, and was adapted by Paul Leadon.  Unlike many other adaptations of the novel, this one did not borrow elements from its sequel, \"Through the Looking-Glass\" (1871), combined into one film.  The production company produced a 73-minute adaptation of the second novel the year before, in 1987, entitled \"Alice: Through the Looking-Glass\".  The 1988 film was produced by Roz Phillips and directed by Rich Trueblood.  Quite uncommon among Burbank Films Australia's adaptations of classic literary works, \"Alice in Wonderland\" featured one original theme song, composed by Mark Isaacs.  The copyright in this film is now owned by Pulse Distribution and Entertainment and administered by digital rights management firm NuTech Digital.\n\nAnupam Kher: Anupam Kher (born 7 March 1955) is an Indian actor who has appeared in over 500 films and many plays.  Mainly working in Hindi films, he has also appeared in acclaimed international films such as the 2002 Golden Globe nominated \"Bend It Like Beckham\", Ang Lee's 2007 Golden Lion-winning \"Lust, Caution\", and David O. Russell's 2013 Oscar-winning \"Silver Linings Playbook\".  Kher has won the Filmfare Award for Best Performance in a Comic Role five times.  For his performance in the 1988 film \"Vijay\" he won the Filmfare Award for Best Supporting Actor.\n\nTiger Moon (band): Tiger Moon was a disco/freestyle Miami-based group that is known for their 1987 song \"Something Tells Me\".  The song has appeared in several Gay, Miami and freestyle compilations.  The track was sampled by Prince in his song \"Thieves In the Temple\" and by other artists.  \"Something Tells Me\" was used in the 1988 movie \"Frantic\" during a scene in which Harrison Ford's character, Richard Walker, enters The Blue Parrot looking for Dédé Martin.\n\nSomething Tells Me (Something's Gonna Happen Tonight): Something Tells Me (Something's Gonna Happen Tonight)\n\nFrantic (film): Frantic is a 1988 American-French mystery thriller film directed by Roman Polanski and starring Harrison Ford and Emmanuelle Seigner.  The theme was written, arranged and performed by Simply Red.\n\nCilla All Mixed Up: Cilla All Mixed Up is the title of Cilla Black's sixteenth and final solo album released worldwide on 7 September 2009 by EMI to digital download.  The album was conceived to celebrate Cilla Black's 45th year in the music business.  An array of original hit singles and album tracks held at Abbey Road studios were given a club makeover alongside a few more recent songs taken from Black's last studio album \"\".  The project featured contributions from production team Almighty as well as other club DJs from the UK, Middle East and Asia.  The lead single for the album project was the Almighty mix of \"Something Tells Me\".\n\nDoug Hutchison: Doug Anthony Hutchison (born May 26, 1960) is an American character actor, known for playing disturbing and antagonistic characters.  Such characters include Obie Jameson in the 1988 film \"The Chocolate War\", Sproles in the 1988 film \"Fresh Horses\", the sadistic corrections officer Percy Wetmore in the 1999 film adaptation of Stephen King's \"The Green Mile\", Eugene Victor Tooms on the series \"The X-Files\", and Horace Goodspeed in \"Lost\".  He has a production company, Dark Water Inc.  In 2011, at the age of 50, he received widespread criticism when he married 16-year-old singer Courtney Stodden.\n\nQuestion: Something Tells Me appeared in a 1988 film that was directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"featured_song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song featured in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director_name\",\n    \"featured_song_title\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "featured_song_title": {
        "type": "string",
        "description": "The title of the song featured in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director_name",
      "featured_song_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
