{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDante's Peak: Dante's Peak is a 1997 American dramatic disaster thriller film directed by Roger Donaldson.  Starring Pierce Brosnan, Linda Hamilton, Charles Hallahan, Elizabeth Hoffman, Jamie Renée Smith, Jeremy Foley and Grant Heslov, the film was set in the fictional town of Dante's Peak where the inhabitants must survive a volcanic eruption and the resultant dangers.  It was released on February 7, 1997 under the production of Sony Pictures, Universal Pictures and Pacific Western Productions.\n\nBede Aircraft: Bede Aircraft Corporation was founded by controversial aeronautical engineer Jim Bede in 1961 to produce the BD-1 kit aircraft, which eventually became the American Aviation Corporation's AA-1.  The company also created and produced a number of advanced kit planes including the famous Bede BD-5 (pusher propeller driven) and BD-5J (turbojet driven).  The BD-5J has held the Guinness record as the World's Smallest Jet Aircraft for more than a quarter century.  Versions of it saw use in various Budweiser commercials (the Bud Light Jet, which was lost in an inflight fire and crash unrelated to airshow work).  The tiny jet also appeared in two James Bond movies; \"Octopussy\" starring Sir Roger Moore, and later in a cameo appearance, hanging from the wall of Q's workshop in \"Die Another Day\" starring Pierce Brosnan as Agent 007.\n\nGrey Owl (film): Grey Owl is a 1999 biopic directed by Richard Attenborough and starring Pierce Brosnan in the role of real life British schoolboy turned Indian trapper \"Grey Owl,\" Archibald Belaney (1888–1938), and Annie Galipeau as his wife Anahareo, with brief appearances by Graham Greene and others.  The screenplay was written by William Nicholson.  This film was released September 10, 1999.\n\nMike Gomez: Mike Gomez (born April 18, 1951) is an American actor.  Best known for his performances in such cult classics as \"The Big Lebowski\" and \"\", Gomez has costarred in numerous films including \"Heartbreak Ridge\" and \"Milagro Beanfield War\", \"Zoot Suit\", \"The Border\" and \"El Norte\", to name a few.  His TV credits include \"Bones\", \"The Shield\", \"Desperate Housewives\", and a series regular role as 'Capt. Gallardo' on the NBC series, \"Hunter\", among others.  On stage, Gomez' numerous theater credits include \"Zoot Suit\" at the Winter Garden on Broadway and the Pre-Broadway run of \"Selena\".\n\nNight Watch (1995 film): Night Watch (also known as Detonator II: Night Watch) is a 1995 American television spy film directed by David Jackson starring Pierce Brosnan and Alexandra Paul.  The film, also known as \"Alistair MacLean's Nightwatch\", was shot in Hong Kong.  The film aired on the USA Network.\n\nRemington Steele: Remington Steele is an American television series co-created by Robert Butler and Michael Gleason.  The series, starring Stephanie Zimbalist and Pierce Brosnan, was produced by MTM Enterprises and first broadcast on the NBC network from 1982 to 1987.  The series blended the genres of romantic comedy, drama, and detective procedural.  \"Remington Steele\" is best known for launching the career of Pierce Brosnan.\n\nThe Thomas Crown Affair (1999 film): The Thomas Crown Affair is a 1999 American heist film directed by John McTiernan.  The film, starring Pierce Brosnan, Rene Russo and Denis Leary, is a remake of the 1968 film of the same name.  The film generally received positive reviews.  It was a success at the box office, grossing $124 million worldwide.\n\nAfter the Sunset: After the Sunset is a 2004 action comedy film starring Pierce Brosnan as Max Burdett, a master thief caught in a cat-and-mouse game with FBI agent Stan Lloyd, played by Woody Harrelson.  The film was directed by Brett Ratner and shot in the Bahamas.\n\nThe Matador: The Matador is a 2005 dark comedy film written and directed by Richard Shepard and starring Pierce Brosnan and Greg Kinnear.  The film was released on DVD on July 4, 2006 and on HD DVD on December 18, 2006.  Brosnan was nominated for both a Golden Globe Award and a Saturn Award for his well-received performance as disillusioned, unstable hitman Julian Noble.\n\nBen Gazzara: Biagio Anthony Gazzarra (August 28, 1930 – February 3, 2012), known as Ben Gazzara, was an American film, stage, and television actor and director.  His best known films include \"Anatomy of a Murder\" (1959), \"Voyage of the Damned\" (1976), \"Inchon\" (1981), \"Road House\" (1989), \"The Big Lebowski\" (1998), \"Buffalo '66\" (1998), \"Happiness\" (1998), \"The Thomas Crown Affair\" (1999), \"Summer of Sam\" (1999), \"Dogville\" (2003) and \"Paris, je t'aime\" (2006).  He was a recurring collaborator with John Cassavetes, working with him on \"Husbands\" (1970), \"The Killing of a Chinese Bookie\" (1976) and \"Opening Night\" (1977).\n\nQuestion: Who directed the 1999 American heist film, starring Pierce Brosnan, Rene Russo, Denis Leary and an American film, stage and television actor best known for films including 'Anatomy of a Murder', 'Voyage of the Damned' and 'The Big Lebowski'?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the main actors starring in the film.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"other_featured_actor\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the additional actor described in the question.\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"known_for_films\": {\n          \"type\": \"array\",\n          \"description\": \"A list of films the actor is best known for, as mentioned in the context.\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"known_for_films\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_genre\",\n    \"director_name\",\n    \"starring_actors\",\n    \"other_featured_actor\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The genre of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "starring_actors": {
        "type": "array",
        "description": "A list of the main actors starring in the film.",
        "items": {
          "type": "string"
        }
      },
      "other_featured_actor": {
        "type": "object",
        "description": "Details about the additional actor described in the question.",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "known_for_films": {
            "type": "array",
            "description": "A list of films the actor is best known for, as mentioned in the context.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "actor_name",
          "known_for_films"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "film_genre",
      "director_name",
      "starring_actors",
      "other_featured_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
