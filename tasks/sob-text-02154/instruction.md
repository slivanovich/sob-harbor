{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCleaver (The Sopranos): Cleaver is a metafictional film within a TV-series that serves as an important plot element toward the end of the HBO television drama series \"The Sopranos\".  Although very little film material is actually shown in the series, its planning and development are discussed at large throughout multiple seasons of the show.  The extent to which Sopranos character Christopher Moltisanti mixes confidential and personal information about the Soprano mob family into the story elements of Cleaver is the focal point throughout its development.  After the project eventually materializes, Cleaver can be categorized as a direct-to-DVD mafia-slasher film, described alternately as \"\"Saw\" meets \"the Godfather II\"\", \"\"the Ring\" meets \"The Godfather\"\", and \"a story about a young man who goes to pieces and then manages to pull himself together again\".  Several characters are credited for their involvement in the project.  The screenplay was written by J. T. Dolan based on a story by Christopher Moltisanti, directed by Morgan Yam and produced by Carmine Lupertazzi, Jr. and Moltisanti.  The film starred Jonathan LaPaglia as Michael \"the Cleaver\" and Daniel Baldwin as mob boss Salvatore (\"Sally Boy\").  Also starring as Sally-boy's key advisors are George Pogatsia as Frankie and Lenny Ligotti as Nicky.  Moltisanti and Lupertazzi initially attempts to recruit Ben Kingsley to fill the role of the mafia don in \"Luxury Lounge (6x07),\" but Kingsley eventually turns down the part.\n\nAli (film): Ali is a 2001 American biographical sports drama film written, produced and directed by Michael Mann.  The film focuses on ten years in the life of the boxer Muhammad Ali, played by Will Smith, from 1964 to 1974, featuring his capture of the heavyweight title from Sonny Liston, his conversion to Islam, criticism of the Vietnam War, and banishment from boxing, his return to fight Joe Frazier in 1971, and, finally, his reclaiming the title from George Foreman in the Rumble in the Jungle fight of 1974.  It also touches on the great social and political upheaval in the United States following the assassinations of Malcolm X and Martin Luther King, Jr.\n\nStage Struck (1958 film): Stage Struck is a 1958 American drama film directed by Sidney Lumet, and stars Henry Fonda, Susan Strasberg and Christopher Plummer in his film debut.  It was based on the 1925 Paramount Pictures film of the same name.  The screenplay, by Augustus and Ruth Goetz, is based on the stage play \"Morning Glory\" by Zoë Akins, which also served as the basis for the 1933 film \"Morning Glory\" which starred Katharine Hepburn, Douglas Fairbanks, Jr. and Adolphe Menjou in corresponding roles.\n\nBand of the Hand: Band of the Hand is an American 1986 action crime film directed by Paul Michael Glaser and produced by Michael Mann, starring Stephen Lang, Leon Robinson, James Remar, Lauren Holly, and Laurence Fishburne.\n\nList of accolades received by American Beauty: \"American Beauty\" is a 1999 American drama film directed by Sam Mendes and written by Alan Ball.  The film stars Kevin Spacey as Lester Burnham, a middle-aged office worker who has a midlife crisis when he becomes infatuated with his teenage daughter's best friend.  Released in North America on September 15, 1999, \"American Beauty\" was positively received by critics and audiences alike; it was the best-reviewed American film of the year and grossed over $350 million worldwide.  Reviewers praised all aspects of the production, with particular emphasis on Mendes, Spacey and Ball; criticism tended to focus on the familiarity of the characters and setting.  At the 1999 Academy Awards, the film won Best Picture, Best Director, Best Actor (for Spacey), Best Original Screenplay and Best Cinematography (for Conrad Hall).  The film was nominated for and won numerous other awards and honors, mainly for the direction, writing, and acting.\n\nChristopher Plummer: Arthur Christopher Orme Plummer {'1': \", '2': \", '3': 'CC', '4': \"} (born December 13, 1929) is a Canadian actor.  Making his film debut in \"Stage Struck\" (1958), Plummer's career spans more than five decades with substantial roles in each of the dramatic arts.  Plummer has portrayed several historical figures, including Arthur Wellesley, First Duke of Wellington in \"Waterloo\" (1970), Rudyard Kipling in \"The Man Who Would Be King\" (1975), Mike Wallace in \"The Insider\" (1999), and Leo Tolstoy in \"The Last Station\" (2009).\n\nThe Insider (film): The Insider is a 1999 American drama film directed by Michael Mann, from a script adapted by Eric Roth and Mann from Marie Brenner's \"Vanity Fair\" article \"The Man Who Knew Too Much\".  The film stars Al Pacino and Russell Crowe, with supporting actors including Christopher Plummer, Bruce McGill, Diane Venora and Michael Gambon.\n\nHeat (1995 film): Heat is a 1995 American crime film written, produced and directed by Michael Mann, and starring Robert De Niro, Al Pacino, and Val Kilmer.  De Niro plays Neil McCauley, a professional thief, while Pacino plays Lt. Vincent Hanna, a LAPD robbery-homicide detective tracking down McCauley's crew.  The story is based on the former Chicago police officer Chuck Adamson's pursuit during the 1960s of a criminal named McCauley, after whom De Niro's character is named.  Heat is a remake by Mann of a TV series he had worked on, the pilot of which was released as a TV movie, \"L.A. Takedown\" in 1989.\n\nThe Last of the Mohicans (1992 film): The Last of the Mohicans is a 1992 American epic historical drama, set in 1757 during the French and Indian War.  It was directed by Michael Mann, based on James Fenimore Cooper's eponymous 1826 novel and George B. Seitz's 1936 film adaptation, owing more to the latter than the novel.  The film stars Daniel Day-Lewis, Madeleine Stowe, and Jodhi May, with Russell Means, Wes Studi, Eric Schweig, and Steven Waddington in supporting roles.  It was produced by Morgan Creek Pictures.\n\nPublic Enemies (2009 film): Public Enemies is a 2009 American biographical mob drama film directed by Michael Mann and written by Mann, Ronan Bennett and Ann Biderman.  It is an adaptation of Bryan Burrough's non-fiction book \"Public Enemies: America's Greatest Crime Wave and the Birth of the FBI, 1933–34\".  Set during the Great Depression, the film chronicles the final years of the notorious bank robber John Dillinger (Johnny Depp) as he is pursued by FBI agent Melvin Purvis (Christian Bale), Dillinger's relationship with Billie Frechette (Marion Cotillard), as well as Purvis' pursuit of Dillinger's associates and fellow criminals Homer Van Meter (Stephen Dorff) and Baby Face Nelson (Stephen Graham).\n\nQuestion: Which character Christopher Orme Plummer potrayed in a 1999 American drama film directed by Michael Mann?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"character_portrayed\": {\n      \"type\": \"string\",\n      \"description\": \"The character portrayed by the actor in the specified film.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_title\",\n    \"release_year\",\n    \"film_genre\",\n    \"director_name\",\n    \"character_portrayed\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
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
        "description": "The genre of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The director of the film."
      },
      "character_portrayed": {
        "type": "string",
        "description": "The character portrayed by the actor in the specified film."
      }
    },
    "required": [
      "actor_name",
      "film_title",
      "release_year",
      "film_genre",
      "director_name",
      "character_portrayed"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
