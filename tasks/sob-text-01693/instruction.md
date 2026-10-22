Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Paddington (film): Paddington is a 2014 comedy film directed by Paul King, written by King and Hamish McColl and produced by David Heyman.  Based on "Paddington Bear" by Michael Bond, the film stars Ben Whishaw as the voice of the title character, along with Hugh Bonneville, Sally Hawkins, Julie Walters, Jim Broadbent, Peter Capaldi and Nicole Kidman in live-action roles.  The film was co-produced by the French company StudioCanal and the British company Heyday Films.  It was released in the United Kingdom on 28 November 2014 and grossed $265.3 million worldwide on a €38.5 million budget.  Among several honours, King was nominated for the BAFTA Award for Best Adapted Screenplay and both he and Heyman were nominated for the BAFTA Award for Best British Film.  A sequel, "Paddington 2", is scheduled to be released in 2017.

M (James Bond): M is a fictional character in Ian Fleming's James Bond book and film series; the character is the Head of the Secret Intelligence Service—also known as MI6—and is Bond's superior.  Fleming based the character on a number of people he knew who commanded sections of British intelligence.  M has appeared in the novels by Fleming and seven continuation authors, as well as appearing in twenty-four films.  In the Eon Productions series of films, M has been portrayed by four actors: Bernard Lee, Robert Brown, Judi Dench and Ralph Fiennes, the incumbent; in the two independent productions, M was played by John Huston, David Niven and Edward Fox.

Paddington (TV series): Paddington is an animated television programme based on the Paddington Bear books by Michael Bond.  The series was scripted by Bond himself, and produced by FilmFair London; it was narrated by actor Michael Hordern, who also voices all characters.

Michael Bond: Thomas Michael Bond {'1': ", '2': ", '3': ", '4': "} (13 January 1926 – 27 June 2017), who wrote under the pen name Michael Bond, was a British author.  He is best known for a series of fictional stories for children, featuring the character of Paddington Bear.  More than 35 million Paddington books have been sold around the world, and the characters have also been featured in film and on television.  His first book was published in 1958 and his last in 2017, a span of 59 years.

The Herbs: The Herbs is a television series for young children made for the BBC by Graham Clutterbuck's FilmFair company.  It was written by Michael Bond (creator of Paddington Bear), directed by Ivor Wood using 3D stop motion model animation and first transmitted from 12 February 1968 in the BBC1 "Watch with Mother" timeslot.  There were 13 episodes in the series, each one 15 minutes long.

Doctor Who: Legacy (video game): Doctor Who: Legacy is a match-3 puzzle RPG video game released on 27 November 2013 based upon the BBC television programme.  It is a free-to-play game release to coincide with the 50th Anniversary of the popular BBC sci-fi TV show, with rights licensed by BBC Worldwide.  The game launched focusing on the 11th Doctor (as played by Matt Smith), then later shifted the focus to the 12th Doctor (played by Peter Capaldi), upon his debut in the show.  New characters and content are added to the game regularly upon them being "signed off" with both the actors and the BBC brand team.  The game includes every incarnation of the Doctor from the television series (including the War Doctor) and well over 200 companions from both Classic and Modern Doctor Who.  The game also closely followed Series 8 and 9 of the show with new levels launching each weekend alongside each episode and included new characters, costumes, and enemies from most of the episodes.

James Bond 007: Agent Under Fire: James Bond 007 in... Agent Under Fire is a first-person shooter video game based on the James Bond franchise.  Developed and published by Electronic Arts, it was released for PlayStation 2, GameCube and Xbox game consoles.  It is the fourth Bond game which is not based on a film or book in the James Bond series, following "", "James Bond 007" and EA's own "007 Racing".  The game's story arc continues in the following sequel, "Nightfire", released a year later.  Unlike previous Bond games which featured the likeness of then current Bond actor Pierce Brosnan, "Agent Under Fire" used the voice of Adam Blackwood and the likeness of English actor Andrew Bicknell for Bond.

Peter Capaldi: Peter Dougan Capaldi (born 14 April 1958) is a Scottish actor, writer and director, best known for playing the twelfth incarnation of the Doctor in "Doctor Who" and as spin doctor Malcolm Tucker in "The Thick of It", for which he has received four British Academy Television Award nominations, winning Best Male Comedy Performance in 2010.  For reprising the role in the spinoff film "In the Loop", Capaldi was honoured with several film critic award nominations for Best Supporting Actor.  He further took on the role of Paddington Bear's neighbour Mr. Curry in the family comedy film "Paddington"; he is set to reprise the role in "Paddington 2".

Moneyball: Moneyball: The Art of Winning an Unfair Game is a book by Michael Lewis, published in 2003, about the Oakland Athletics baseball team and its general manager Billy Beane.  Its focus is the team's analytical, evidence-based, sabermetric approach to assembling a competitive baseball team, despite Oakland's disadvantaged revenue situation.  A film based on the book starring Brad Pitt and Jonah Hill was released in 2011.

The Adventures of Paddington Bear: The Adventures of Paddington Bear is a British-Canadian-French animated children's television series.  It is based on the book "Paddington Bear" by Michael Bond and was written by Bruce Robb.  It was produced by CINAR and Protecrea and ran for 117 episodes.

Question: Who directed the 2014 film based on a Michael Bond book starring the 12th Doctor Who actor?

Respond with JSON matching this schema:
{
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
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "source_book_author": {
      "type": "string",
      "description": "The author of the book the film is based on."
    },
    "starring_actor": {
      "type": "string",
      "description": "The actor who played the 12th Doctor Who and also starred in the film."
    },
    "actor_role_in_film": {
      "type": "string",
      "description": "The role played by the starring actor in the film."
    },
    "actor_doctor_who_incarnation": {
      "type": "string",
      "description": "The specific Doctor Who incarnation played by the actor."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "source_book_author",
    "starring_actor",
    "actor_role_in_film",
    "actor_doctor_who_incarnation"
  ],
  "additionalProperties": false
}
