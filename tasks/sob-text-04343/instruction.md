{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLucy Gordon (actress): Lucy Gordon (22 May 1980 – 20 May 2009) was an English actress and model.  She became a face of CoverGirl in 1997 before starting an acting career.  Her first film was \"Perfume\" in 2001 before going on to have small roles in \"Spider-Man 3\", \"Serendipity\" and \"The Four Feathers\".  Gordon had played the actress and singer Jane Birkin in the film \"\", a biopic of singer-songwriter Serge Gainsbourg.  Before the film was released, she was found hanged in her flat in Paris on 20 May 2009 after committing suicide.\n\nThe Space Between Us (film): The Space Between Us is a 2017 American romantic science fiction film directed by Peter Chelsom and written by Allan Loeb, from a story by Stewart Schill, Richard Barton Lewis and Loeb.  The film stars Gary Oldman, Asa Butterfield, Britt Robertson, and Carla Gugino, and follows a teenage boy, born on Mars, who travels to Earth.\n\nHear My Song: Hear My Song is a 1991 drama film, written by the actors Peter Chelsom (who directed) and Adrian Dunbar (who plays the lead), based on the story of Irish tenor Josef Locke.  It was nominated for Best Original Screenplay at the 1993 BAFTA awards.\n\nTown &amp; Country (film): Town & Country is a 2001 American romantic comedy film directed by Peter Chelsom, written by Buck Henry and Michael Laughlin, and starring Warren Beatty, Diane Keaton, Goldie Hawn, Garry Shandling, Andie MacDowell, Jenna Elfman, Nastassja Kinski, and Charlton Heston.  Beatty plays an architect, with Keaton as his wife, and Hawn and Shandling as their best friends.  This is Beatty's and Keaton's first film together since 1981's \"Reds,\" and Beatty's third film with Hawn, after 1971's \"$\" and 1975's \"Shampoo\".\n\nHannah Montana: The Movie: Hannah Montana: The Movie is a 2009 American teen musical comedy-drama film based on the Disney Channel television series of the same name.  It was the second theatrical film based on a Disney Channel Original Series, after \"The Lizzie McGuire Movie\" (2003).  The film was directed by Peter Chelsom with screenplay penned by Daniel Berendsen.  The film was produced by David Blocker, Billy Ray Cyrus, Alfred Gough, Miles Millar, Steven Peterman and Michael Poryes.  The film stars series regulars Miley Cyrus, Billy Ray Cyrus, Emily Osment, Jason Earles, Mitchel Musso, and Moisés Arias, as well as Lucas Till, Vanessa Williams, Margo Martindale, and Melora Hardin.\n\nFunny Bones: Funny Bones is a 1995 British-American comedy-drama film from Hollywood Pictures.  It was written, directed and produced by Peter Chelsom, co produced by Simon Fields, and co written by Peter Flannery.  The music score was by John Altman, and the cinematography by Eduardo Serra.  Set in Las Vegas and Blackpool, England, the film stars Oliver Platt, Jerry Lewis, Lee Evans, Leslie Caron, Richard Griffiths, Sadie Corre, Oliver Reed, George Carl, Freddie Davies and Ian McNeice.\n\nThe Mighty: The Mighty is a 1998 drama film directed by Peter Chelsom and based on the book \"Freak the Mighty\" by Rodman Philbrick.  The film stars Sharon Stone, Gena Rowlands, Gillian Anderson, Harry Dean Stanton, Kieran Culkin, James Gandolfini, and Elden Henson.\n\nHector and the Search for Happiness (film): Hector and the Search for Happiness is a 2014 German-British-Canadian comedy-drama film directed by Peter Chelsom and co-written with Tinker Lindsay and Maria von Heland, based on François Lelord's novel of the same name.  The film stars Simon Pegg and Rosamund Pike.\n\nPeter Chelsom: Peter Chelsom (born 20 April 1956) is a British film director, writer, and actor.  He has directed such films as \"Hector and the Search for Happiness\", \"Serendipity\", and \"Shall We Dance? \" Peter Chelsom is a member of the British Academy, the American Academy, The Directors Guild Of America, and The Writers Guild Of America.\n\nSerendipity (film): Serendipity is a 2001 American romantic comedy film directed by Peter Chelsom, written by Marc Klein, and starring John Cusack and Kate Beckinsale.  The music score was composed by Alan Silvestri.\n\nQuestion: The Lucy Gordon acted in what Peter Chelsom directed movie?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress.\"\n    },\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie they both worked on.\"\n    },\n    \"movie_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    },\n    \"movie_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the movie.\"\n    }\n  },\n  \"required\": [\n    \"director_name\",\n    \"actress_name\",\n    \"movie_title\",\n    \"movie_release_year\",\n    \"movie_genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_name": {
        "type": "string",
        "description": "The name of the director."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress."
      },
      "movie_title": {
        "type": "string",
        "description": "The title of the movie they both worked on."
      },
      "movie_release_year": {
        "type": "integer",
        "description": "The release year of the movie."
      },
      "movie_genre": {
        "type": "string",
        "description": "The genre of the movie."
      }
    },
    "required": [
      "director_name",
      "actress_name",
      "movie_title",
      "movie_release_year",
      "movie_genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
