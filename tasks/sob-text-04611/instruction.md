{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJenma Natchathiram: Jenma Natchathiram (தமிழ்: ஜென்ம நட்சத்திரம், English: Birth Star) is a 1991 Tamil supernatural horror film directed and Screenplays by Thakkali Srinivasan for Thirai Gangai Films.  The film dialogue were written by Ma.  Pandarinathan, and story were written by Krishnan respectively.  Music by Premi - Srini assets to the soundtrack.  It Stars Baby Vichithra played titular role with Pramoth, Sindhuja and Vivek played pivotal role.  The film was unofficial remake of \"The Omen\", 1976 British/American supernatural horror drama film directed by Richard Donner.\n\nDeliver Us from Evil (2014 film): Deliver Us from Evil is a 2014 American supernatural horror film directed by Scott Derrickson and produced by Jerry Bruckheimer.  The film is officially based on a 2001 non-fiction book entitled \"Beware the Night\" by Ralph Sarchie and Lisa Collier Cool, and its marketing campaign highlighted that it was \"inspired by actual accounts\".  The film stars Eric Bana, Édgar Ramírez, Sean Harris, Olivia Munn, and Joel McHale in the main roles and was released on July 2, 2014.\n\nShelley Hennig: Shelley Catherine Hennig (born January 2, 1987) is an American model and actress.  She is also a beauty pageant titleholder who held the Miss Teen USA 2004 title.  She played Stephanie Johnson on \"Days of Our Lives\" and starred in the CW series \"The Secret Circle\" as Diana Meade.  She played the character Malia Tate in \"Teen Wolf\".  Hennig also starred in horror films \"Unfriended\" as Blaire Lily and \"Ouija\" as Debbie Galardi.  She has been nominated for two Emmys for her role on \"Days of Our Lives\".  She has won a 2016 Teen Choice Award.\n\nUnfriended: Unfriended is a 2014 American found footage supernatural horror film directed by Levan Gabriadze, written by Nelson Greaves, executive produced by Jason Blum, co-produced by Adam Sidman, and produced by Greaves and Timur Bekmambetov.  The film stars Shelley Hennig, Moses Jacob Storm, Renee Olstead, Will Peltz, Jacob Wysocki, and Courtney Halverson as high school students in a Skype conversation that is haunted by a student who was bullied and committed suicide named Laura Barns, played by Heather Sossaman.\n\nOuija (2014 film): Ouija is a 2014 American supernatural horror film directed by Stiles White in his directorial debut, produced by Jason Blum, Michael Bay, Andrew Form, Bradley Fuller, and Bennett Schneir and written by Juliet Snowden and White, who previously together wrote \"The Possession\".  It stars Olivia Cooke, Ana Coto, Daren Kagasoff, Douglas Smith, and Bianca A. Santos as teenagers who have unleashed spirits from a Ouija board.\n\nJessabelle: Jessabelle is a 2014 American supernatural horror film directed by Kevin Greutert and written by Ben Garant.  The film stars Sarah Snook, Mark Webber, Joelle Carter, David Andrews, Amber Stevens and Ana de la Reguera.  The film was released on November 7, 2014 by Lionsgate.\n\nClown (film): Clown is a 2014 American supernatural horror film directed by Jon Watts, produced by Mac Cappuccino, Eli Roth and Cody Ryder, and written by Christopher D. Ford and Watts.  The film stars Laura Allen, Andy Powers, and Peter Stormare.  The visual effects for the clown monster were done by Alterian, Inc. and Tony Gardner.  Principal photography began in November 2012, in Ottawa.  The film was released in Italy on November 13, 2014, and was released in the UK on March 2, 2015, and in the United States on June 17, 2016, by Dimension Films.\n\nThe Apparition: The Apparition is a 2012 American supernatural horror film, written and directed by Todd Lincoln, making his directorial debut, and starring Ashley Greene, Sebastian Stan, Tom Felton, Julianna Guill and Rick Gomez.  The plot follows three college students who, after the death of their friend, must battle a supernatural force they summoned themselves.  The film was loosely inspired by the Philip experiment conducted in 1972.  The film was a box office bomb and was cited by critics as one of the worst horror movies of 2012.  It was also the last Warner Bros.  Pictures horror film to be released under its own label before resorting to New Line Cinema to release all future horror movies made by Warner Bros.\n\nAnnabelle (film): Annabelle is a 2014 American supernatural horror film directed by John R. Leonetti, written by Gary Dauberman and produced by Peter Safran and James Wan.  It is a prequel to 2013's \"The Conjuring\" and the second installment in \"The Conjuring\" series.  The film was inspired by a story of a doll named Annabelle told by Ed and Lorraine Warren.  The film stars Annabelle Wallis, Ward Horton, and Alfre Woodard.\n\nFlight 7500: Flight 7500 is a 2014 American supernatural horror film directed by Takashi Shimizu, from a screenplay by Craig Rosenberg.  It stars Leslie Bibb, Jerry Ferrara, Ryan Kwanten, Jamie Chung, Christian Serratos, Nicky Whelan and Amy Smart.  It revolves around a supernatural force on a plane.  The film was released in the United States on April 12, 2016, by CBS Films and Lionsgate.\n\nQuestion: Shelley Hennig starred in the 2014 American supernatural horror film directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the supernatural horror film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director of the film.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_genre\",\n    \"director_name\",\n    \"actress_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the supernatural horror film."
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
        "description": "The name of the director of the film."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who starred in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "film_genre",
      "director_name",
      "actress_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
