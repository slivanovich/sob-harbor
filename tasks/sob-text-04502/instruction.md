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
Space Chimps: Space Chimps is a 2008 3D computer-animated comic science fiction film directed by Kirk DeMicco and written by DeMicco and Rob Moreland.  It features the voices of Andy Samberg, Cheryl Hines, Jeff Daniels, Patrick Warburton, Kristin Chenoweth, Kenan Thompson, Zack Shada, Carlos Alazraqui, Omid Abtahi, Patrick Breen, Jane Lynch, Kath Soucie, and Stanley Tucci.  The film follows three chimpanzees who go into space to an alien planet.

Mark McCorkle: Mark McCorkle is an American screenwriter, television writer and television producer.  Among others, he is co-creator of the popular Disney animated series, "Kim Possible".  He frequently collaborates with fellow writer Bob Schooley.  Prior to "Kim Possible", McCorkle, Schooley, and the main director of "Kim Possible", Steve Loter, also held their respective jobs (writer/producer and director respectively) on "Buzz Lightyear of Star Command".  Many voice talents on "Kim Possible", also did work of "Buzz Lightyear of Star Command" (Nicole Sullivan, Patrick Warburton).  Both series can be similarly compared to each other.  He did work on DreamWorks' "The Penguins of Madagascar" as a producer along with Schooley, again with regular voices Sullivan and John DiMaggio.  As of 2016, McCorkle and Schooley are creating and executive producing a new TV series based on the 2014 Disney animated feature, "Big Hero 6" for Disney XD.

Gale Weathers: Gale Weathers is a fictional character of the "Scream" series.  The character was created by Kevin Williamson and is portrayed by "Friends" star Courteney Cox.  She first appeared in "Scream" (1996), followed by three sequels: "Scream 2" (1997), "Scream 3" (2000) and "Scream 4" (2011).  The character appears in the "Scream" films as an ambitious, strong-willed journalist and writer who is initially built up as an antagonist, but ultimately joins forces with Sidney Prescott and Dewey Riley in order to investigate and stop the Ghostface murders.

Hollywood Melrose Hotel: The Hollywood Melrose Hotel, also known previously as the Melrose Arms and later as the Monte Cristo Island Apartments, is a historic building on Melrose Boulevard in Hollywood, California.  Designed by S. Charles Lee, the structure was built in 1927.  It has been used both as a hotel and apartments over the years of its existence, with commercial establishments on the first floor.  In 1992, the building was listed on the National Register of Historic Places based on its architecture.  In April 2010, the hotel was reopened as the newly restored Hollywood Historic Hotel.  Edmon Simonian and family own the property, and operate a furniture gallery out of its street level.  Today, the hotel is a 3 star property with big, confy beds, renovated bathrooms, and beautiful rooms, bathrooms and hallways, befit of a 3 star hotel.  All of the hotel's facades, common spaces, staircases and 62 rooms have been restored to their former 1920's glory following an 18-month-long interior and exterior renovation.

Mark Moseley (actor): Mark Moseley (born August 2, 1961) is an American voice actor, radio personality and stand-up comedian.  He has appeared in a variety of films, television shows, and video games, and is probably best known as a sound-double for actors such as Eddie Murphy, Patrick Stewart, Arnold Schwarzenegger, Patrick Warburton, and Robin Williams.

Sidney Prescott: Sidney Prescott is a fictional character and the primary protagonist of the "Scream" series.  The character was created by Kevin Williamson and is portrayed by Canadian actress Neve Campbell.  She first appeared in "Scream" (1996) followed by three sequels: "Scream 2" (1997), "Scream 3" (2000) and "Scream 4" (2011).  The character appears in the "Scream" films as the target of a series of killers who adopt the Ghostface persona, a ghost mask and black cloak, to pursue her.  In each film, the Ghostface killers often murder people close to Sidney and taunt her by phone with threats and intimate knowledge of her life or the murder of her mother, leading to a final confrontation where the true killer is revealed.

Scream 3: Scream 3 is a 2000 American slasher film directed by Wes Craven and written by Ehren Kruger.  It stars David Arquette, Neve Campbell, Courteney Cox, Patrick Dempsey, Scott Foley, Lance Henriksen, Matt Keeslar, Jenny McCarthy, Emily Mortimer, Parker Posey, Deon Richmond, and Patrick Warburton.  Released as the third installment in the "Scream" franchise, it was the concluding chapter of the series until the franchise was revived in 2011 with a sequel, "Scream 4".

List of Scream characters: Wes Craven's "Scream" series features a large cast of characters created primarily by Kevin Williamson with contributions from Craven and Ehren Kruger.  The series focuses on the character of Sidney Prescott (Neve Campbell) and a succession of murderers who adopt a ghost-like disguise, dubbed Ghostface, to taunt and attempt to kill her.  The series comprises four films: "Scream" (1996), "Scream 2" (1997), "Scream 3" (2000) and "Scream 4" (2011).

Scream (franchise): Scream is an American horror franchise created by Kevin Williamson and Wes Craven.  Starring Neve Campbell, Courteney Cox, and David Arquette, the film series grossed over $604 million in worldwide box-office receipts and consists of four motion pictures directed by Craven.  The first series entry, "Scream", was released on December 20, 1996 and is currently the highest-grossing slasher film in the United States.  The second entry "Scream 2" was released on December 12, 1997 followed by a third installment, "Scream 3", released February 4, 2000.  Eleven years after the previous film, "Scream 4" was released on April 15, 2011.  The films follow Sidney Prescott, and her war against a succession of murderers who adopt the guise of Ghostface to stalk and torment their victims.  Sidney receives support in the films from town deputy Dewey Riley, reporter Gale Weathers, and film-geek Randy Meeks.  A television spin-off of the film series was launched by MTV on June 30, 2015.  The TV series follows different characters and new storylines which are not connected to the film series.

Patrick Warburton: Patrick John Warburton (born November 14, 1964) is an American comedic actor and voice actor.  In television, he is known for playing David Puddy on "Seinfeld", the title role on "The Tick", Jeb Denton on "Less Than Perfect", Jeff Bingham on "Rules of Engagement", and Lemony Snicket on "A Series of Unfortunate Events".  His voice roles include Kronk in "The Emperor's New Groove" and its sequels, paraplegic police officer Joe Swanson on "Family Guy", Brock Samson on "The Venture Bros", Lok in the "Tak and the Power of Juju" video game series and in the television series and Flynn in "Skylanders" video games.  In advertising he has played a "control enthusiast" in a series of commercials for National Car Rental.

Question: When doe the Scream 3 star Patrick Warburton born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "film_role": {
      "type": "string",
      "description": "The role of the person in the specified film."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The full birth date of the person in YYYY-MM-DD format."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the person."
    },
    "birth_month": {
      "type": "string",
      "description": "The birth month of the person."
    },
    "birth_day": {
      "type": "integer",
      "description": "The birth day of the person."
    }
  },
  "required": [
    "person_name",
    "film_role",
    "film_title",
    "birth_date",
    "birth_year",
    "birth_month",
    "birth_day"
  ],
  "additionalProperties": false
}
