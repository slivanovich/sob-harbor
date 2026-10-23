{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAmanda Posey: Amanda Rachel Posey (born June 1965) is a British film producer, best known for her films \"An Education\" and \"Brooklyn\", produced with frequent collaborator Finola Dwyer.  She is the wife of novelist and screenwriter Nick Hornby.\n\nBrooklyn (film): Brooklyn is a 2015 British-Canadian-Irish romantic drama film directed by John Crowley and written by Nick Hornby, based on Colm Tóibín's 2009 novel of the same name.  The film stars Saoirse Ronan, Emory Cohen, Domhnall Gleeson, Jim Broadbent, and Julie Walters.  Set in 1951 and 1952, the film tells the story of a young Irish woman's immigration to Brooklyn, where she falls in love.  When her past catches up with her she must choose between two countries and the lives that exist within them for her.\n\nList of Harry Potter cast members: Several actors of the United Kingdom and Ireland have voiced or portrayed characters appearing in the \"Harry Potter\" film series based on the book series by J. K. Rowling.  Daniel Radcliffe, Rupert Grint and Emma Watson have played Harry Potter, Ron Weasley and Hermione Granger in all the films.  When they were cast only Radcliffe had previously acted in a film.  Complementing them on screen are such actors as Helena Bonham Carter, Jim Broadbent, John Cleese, Robbie Coltrane, Warwick Davis, Ralph Fiennes, Michael Gambon, Brendan Gleeson, Richard Griffiths, Richard Harris, John Hurt, Jason Isaacs, Miriam Margolyes, Helen McCrory, Gary Oldman, Alan Rickman, Fiona Shaw, Maggie Smith, Timothy Spall, Imelda Staunton, David Thewlis, Emma Thompson, and Julie Walters, among others.  Thirteen actors have appeared as the same character in all eight films of the series.\n\nAn Education: An Education is a 2009 coming-of-age drama film based on a memoir of the same name by British journalist Lynn Barber.  The film was directed by Lone Scherfig from a screenplay by Nick Hornby.  It stars Carey Mulligan as Jenny, a bright schoolgirl, and Peter Sarsgaard as David, the charming con man who seduces her.  The film was nominated for three Academy Awards in 2010: Best Picture and Writing (Adapted Screenplay) for Nick Hornby, and Best Actress for Carey Mulligan.\n\nRevolution!!: Revolution!!  (also known as The French Revolution by the National Theatre of Brent) is a 1989 television comedy film by the National Theatre of Brent, the British comedy double-act.  It stars Patrick Barlow as Desmond Olivier Dingle and Jim Broadbent as Wallace, and is written by Patrick Barlow, with Jim Broadbent and Martin Duncan.  Directed by Jonathan Stedall.  Desmond and Wallace act out major events of the French Revolution, portraying different characters simply by slightly changing their grey suit costumes.\n\nList of accolades received by Brooklyn: Brooklyn is a 2015 Irish-Canadian historical period drama film directed by John Crowley.  Writer Nick Hornby adapted the screenplay from Colm Tóibín's novel of the same name.  The plot follows Eilis Lacey (Saoirse Ronan), a young Irish woman who emigrates to Brooklyn to find employment.  There she marries an Italian plumber called Tony (Emory Cohen), before being forced to choose between her home town of Enniscorthy or her new life in Brooklyn.  The film premiered at the 2015 Sundance Film Festival.  It was released by Fox Searchlight Pictures in a limited capacity on 6 November 2015.\n\nPaddington 2: Paddington 2 is an upcoming British-French family-comedy film directed by Paul King, co written by King and Simon Farnaby, and produced by David Heyman.  It is the sequel to 2014's \"Paddington\".  The film stars Hugh Grant, Brendan Gleeson, Hugh Bonneville, Sally Hawkins, Julie Walters, Jim Broadbent, Peter Capaldi, Madeleine Harris, Samuel Joslin, and the voices of Ben Whishaw and Imelda Staunton.  Production began in October 2016, and ended in June 2017.  The film is set to release on 10 November 2017.\n\nPaddington (film): Paddington is a 2014 comedy film directed by Paul King, written by King and Hamish McColl and produced by David Heyman.  Based on \"Paddington Bear\" by Michael Bond, the film stars Ben Whishaw as the voice of the title character, along with Hugh Bonneville, Sally Hawkins, Julie Walters, Jim Broadbent, Peter Capaldi and Nicole Kidman in live-action roles.  The film was co-produced by the French company StudioCanal and the British company Heyday Films.  It was released in the United Kingdom on 28 November 2014 and grossed $265.3 million worldwide on a €38.5 million budget.  Among several honours, King was nominated for the BAFTA Award for Best Adapted Screenplay and both he and Heyman were nominated for the BAFTA Award for Best British Film.  A sequel, \"Paddington 2\", is scheduled to be released in 2017.\n\nCherry Wine (Hozier song): \"Cherry Wine\" is a song by Hozier released in February 2016 as the final single from the 2014 album \"Hozier\".  The song was issued to promote awareness of the issue of domestic violence, and sales from downloads go to anti-domestic violence charities.  The video, starring Saoirse Ronan as a domestic violence victim, which premiered on Valentine's Day, was given wide coverage in the Irish press.  In March Hozier performed the song at the UN Women HeForShe event, supported by SAFE Ireland.\n\nBilly Howle: Billy Howle (born November 9, 1989) is an actor, known for his work as James Warwick on the E4 television series, \"Glue\".  He has since co-starred in the film, \"The Sense of an Ending\" (as the younger version of Jim Broadbent's lead character) and the miniseries \"The Witness for the Prosecution\" in the pivotal role of defendant, Leonard Vole.  He also appeared in \"Dunkirk\".  Howle will next be seen opposite Saoirse Ronan in the drama, \"On Chesil Beach\", in the adaptation of Anton Chekhov's iconic play, \"The Seagull\", and in Netflix film \"Outlaw King\".\n\nQuestion: When was the film produced by the wife of Nick Hornby, starring Saoirse Ronan, Emory Cohen, Domhnall Gleeson, Jim Broadbent, and Julie Walters released?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film identified by the criteria.\"\n    },\n    \"producer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the film's producer.\"\n        },\n        \"relationship_to_nick_hornby\": {\n          \"type\": \"string\",\n          \"description\": \"The relationship of the producer to Nick Hornby.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"relationship_to_nick_hornby\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"main_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of the main actors starring in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"producer\",\n    \"release_year\",\n    \"main_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film identified by the criteria."
      },
      "producer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the film's producer."
          },
          "relationship_to_nick_hornby": {
            "type": "string",
            "description": "The relationship of the producer to Nick Hornby."
          }
        },
        "required": [
          "name",
          "relationship_to_nick_hornby"
        ],
        "additionalProperties": false
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "main_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of the main actors starring in the film."
      }
    },
    "required": [
      "film_title",
      "producer",
      "release_year",
      "main_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
