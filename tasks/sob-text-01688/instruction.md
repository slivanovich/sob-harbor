{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCorky Romano: Corky Romano is a 2001 American mafia comedy film starring former \"Saturday Night Live\" cast member Chris Kattan.  Also starring are Fred Ward, Vinessa Shaw, Chris Penn, and Peter Berg.  The movie was produced by Robert Simond, directed by Rob Pritts, and was written by David Garrett and Jason Ward.  In the movie, Kattan plays the title character, a veterinarian who is forced by his mobster family to infiltrate the local FBI facility to steal evidence incriminating his father, Mafia boss Francis A. \"Pops\" Romano (Peter Falk), of racketeering charges.  It first opened in theaters on October 12, 2001.\n\nKurt Sayenga: Kurt Sayenga is a writer, director, and producer living in the Los Angeles area.  He is the executive producer/showrunner of the science anthology series \"Breakthrough\", a coproduction of National Geographic Channel, GE, Imagine Entertainment, and Asylum Entertainment.  The first season of the series, which premiered in 2015, featured films directed by Ron Howard, Paul Giamatti, Angela Bassett, Peter Berg, Akiva Goldsman, and Brett Ratner.  The second season, which premiered May 2017, featured films directed by Ana Lily Amirpour, David Lowery, Shane Carruth and Kurt Sayenga, The Malloys, Steven Hoggard, and Shalini Kantayya.\n\nPrime Suspect (U.S. TV series): Prime Suspect was an American police procedural television drama series that aired on NBC from September 22, 2011 to January 22, 2012.  It stars Maria Bello as Detective Jane Timoney.  The series was a \"re-imagining\" of the original British series \"Prime Suspect\".  The series was created by Lynda La Plante and was redeveloped by Alexandra Cunningham who also serves as executive producer and writer.  Peter Berg serves as executive producer and director.  Sarah Aubrey, Julie Meldal-Johnson, Paul Buccieri, Lynda La Plante, and John McNamara all serve as executive producers.  The series is produced by Universal Television, ITV Studios America, and Film 44.\n\nJerry and Tom: Jerry and Tom is a 1998 American black comedy film directed by Saul Rubinek in his directorial debut.  The screenplay was adapted by Rick Cleveland from his own 1994 one-act play.  The film stars Joe Mantegna and Sam Rockwell as contract killers who work at a used car dealership.  The film premiered at Sundance in January 1998, and, after Miramax declined to release it theatrically, aired on Showtime.\n\nLate for Dinner: Late for Dinner is a 1991 American film directed by W. D. Richter and starring Peter Berg, Brian Wimmer and Marcia Gay Harden.  The supporting cast features Peter Gallagher and Richard Steinmetz, along with Janeane Garofalo's first movie appearance, briefly playing a cashier during a comical sequence in a burger joint.\n\nThe Rundown: The Rundown (also known as Welcome to the Jungle) is a 2003 American action comedy film starring Dwayne Johnson as a bounty hunter who must head for Brazil to retrieve his employer's renegade son (Seann William Scott).  It was directed by Peter Berg.  The film received positive reviews but failed at the box office.\n\nPeter Berg: Peter Berg (born March 11, 1964) is an American director, actor, producer, and writer of film, television, and music videos.  His directorial film works include the black comedy \"Very Bad Things\" (1998), the action comedy \"The Rundown\" (2003), the sports drama \"Friday Night Lights\" (2004), the action thriller \"The Kingdom\" (2007), the superhero comedy-drama \"Hancock\" (2008), the military science fiction war film \"Battleship\" (2012), the war film \"Lone Survivor\" (2013), the disaster drama \"Deepwater Horizon\" (2016), and the Boston Marathon bombing drama \"Patriots Day\" (2016), the latter three all starring Mark Wahlberg.  In addition to cameo appearances in the last six of these titles, he has had prominent acting roles in films including \"Cop Land\" (1997), \"Corky Romano\" (2001), \"Collateral\" (2004), \"Smokin' Aces\" (2006) and \"Lions for Lambs\" (2007).\n\nRace for Glory: Race for Glory (also known as American Built) is a 1989 American action film directed by Rocky Lang. This film has been music composed by Jay Ferguson. The film starring Alex McArthur, Peter Berg, Pamela Ludwig, Ray Wise, Oliver Stritzel and Barbara Blossom in the lead roles.\n\nFrank Harts: Frank Harts is an American film, television, and theatre actor.  He played George Murchison in the 2004 Tony Award-winning Broadway revival of \"A Raisin In The Sun\" opposite Sean Combs, Audra McDonald, Phylicia Rashad, and Sanaa Lathan.  Harts has played supporting roles in several films, including the film \"Home\" directed by Jono Oliver which was nominated for an NAACP Image Award for best director in 2014.  He played recurring character Deputy Dennis Luckey on the HBO series \"The Leftovers\" created by Damon Lindelof and Tom Perrotta, directed by Peter Berg.  He currently plays recurring character Dale Christo on the new Showtime series \"Billions\" Harts is a graduate of The Juilliard School.\n\nVery Bad Things: Very Bad Things is a 1998 American black comedy film directed by Peter Berg.  It stars Cameron Diaz, Jon Favreau, Daniel Stern, Jeremy Piven, Christian Slater, Leland Orser and Jeanne Tripplehorn.\n\nQuestion: Peter Berg, is an American director, actor, producer, and writer of film, television, and music videos, his directorial film works include which 1998 American black comedy film directed by Peter Berg?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin of the film.\"\n    }\n  },\n  \"required\": [\n    \"director_name\",\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"country_of_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_name": {
        "type": "string",
        "description": "The name of the director."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country of origin of the film."
      }
    },
    "required": [
      "director_name",
      "film_title",
      "release_year",
      "genre",
      "country_of_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
