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
Romance &amp; Cigarettes: Romance & Cigarettes is a 2005 American musical romantic comedy film written and directed by John Turturro.  The film stars an ensemble cast which includes James Gandolfini, Susan Sarandon, Kate Winslet, Steve Buscemi, Bobby Cannavale, Mandy Moore, Mary-Louise Parker, Aida Turturro, Christopher Walken, Barbara Sukowa, Elaine Stritch, Eddie Izzard, and Amy Sedaris.  The film was nominated for a Golden Lion at the 2005 Venice Film Festival.

A Midsummer Night's Dream (1999 film): A Midsummer Night's Dream is a 1999 romantic comedy fantasy film based on the play "A Midsummer Night's Dream" by William Shakespeare.  It was directed by Michael Hoffman.  The ensemble cast features Kevin Kline as Bottom, Michelle Pfeiffer and Rupert Everett as Titania and Oberon, Stanley Tucci as Puck, and Calista Flockhart, Anna Friel, Christian Bale, and Dominic West as the four lovers.

The Hunger Games: Mockingjay – Part 1: The Hunger Games: Mockingjay – Part 1 is a 2014 American dystopian science fiction adventure film directed by Francis Lawrence with a screenplay by Peter Craig and Danny Strong.  It is the first of two films based on Suzanne Collins' novel " Mockingjay", the final book in "The Hunger Games" trilogy, and the third installment in "The Hunger Games" film series, produced by Nina Jacobson and Jon Kilik and distributed by Lionsgate.  The film features an ensemble cast that includes Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth, Woody Harrelson, Elizabeth Banks, Julianne Moore, Philip Seymour Hoffman, Jeffrey Wright, Stanley Tucci, and Donald Sutherland.  Principal photography for both parts of the film began on September 23, 2013, in Atlanta, before moving to Paris for two weeks of filming and officially concluding on June 20, 2014, in Berlin.

Margin Call (film): Margin Call is a 2011 American independent drama film written and directed by J. C. Chandor.  The principal story takes place over a 24-hour period at a large Wall Street investment bank during the initial stages of the financial crisis of 2007–08.  In focus are the actions taken by a group of employees during the subsequent financial collapse.  The ensemble cast features Kevin Spacey, Paul Bettany, Jeremy Irons, Zachary Quinto, Penn Badgley, Simon Baker, Demi Moore, and Stanley Tucci.

Aladdin (2019 film): Aladdin is an upcoming American musical romantic fantasy film directed by Guy Ritchie from a screenplay written by John August, Ritchie and Vanessa Taylor, and co-produced by Walt Disney Pictures, Lin Pictures, and Marc Platt Productions.  It is a live-action adaptation of Disney's 1992 animated film of the same name, which is in turn based on the Arab-style folktale of the same name from "One Thousand and One Nights" and the French interpretation by Antoine Galland.  The film stars Mena Massoud as the titular character with Naomi Scott, Will Smith, Marwan Kenzari, Navid Negahban, Nasim Pedrad, Billy Magnussen, and Numan Acar in supporting roles.  It is scheduled to be released on May 24, 2019 in the United States.

Beauty and the Beast (1991 film): Beauty and the Beast is a 1991 American animated musical romantic fantasy film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  The 30th Disney animated feature film and the third released during the Disney Renaissance period, it is based on the French fairy tale of the same name by Jeanne-Marie Leprince de Beaumont (who was also credited in the English version as well as in the French version), and ideas from the 1946 French film of the same name directed by Jean Cocteau.  "Beauty and the Beast" focuses on the relationship between the Beast (voice of Robby Benson), a prince who is magically transformed into a monster and his servants into household objects as punishment for his arrogance, and Belle (voice of Paige O'Hara), a young woman whom he imprisons in his castle.  To become a prince again, Beast must learn to love Belle and earn her love in return to avoid remaining a monster forever.  The film also features the voices of Richard White, Jerry Orbach, David Ogden Stiers, and Angela Lansbury.

Beauty and the Beast (1946 film): Beauty and the Beast (French: La Belle et la Bête ) is a 1946 French romantic fantasy film directed by French poet and filmmaker Jean Cocteau.  Starring Josette Day as Belle and Jean Marais as the Beast, it is an adaptation of the 1757 story "Beauty and the Beast", written by Jeanne-Marie Leprince de Beaumont and published as part of a fairy tale anthology.

Beauty and the Beast (1962 film): Beauty and the Beast is a 1962 American romantic fantasy film directed by Edward L. Cahn and starring Joyce Taylor and Mark Damon.  It is based on the 18th century fairy tale "Beauty and the Beast" written by Jeanne-Marie Leprince de Beaumont and features title creature make-up by the legendary Jack Pierce.

Beauty and the Beast (2017 film): Beauty and the Beast is a 2017 American musical romantic fantasy film directed by Bill Condon from a screenplay written by Stephen Chbosky and Evan Spiliotopoulos, and co-produced by Walt Disney Pictures and Mandeville Films.  The film is based on Disney's 1991 animated film of the same name, itself an adaptation of Jeanne-Marie Leprince de Beaumont's eighteenth-century fairy tale.  The film features an ensemble cast that includes Emma Watson and Dan Stevens as the titular characters with Luke Evans, Kevin Kline, Josh Gad, Ewan McGregor, Stanley Tucci, Audra McDonald, Gugu Mbatha-Raw, Ian McKellen, and Emma Thompson in supporting roles.

Stanley Tucci: Stanley Tucci ( ; ] ; born November 11, 1960) is an American character actor, writer, producer and film director.

Question: Beauty and the Beast, is an American musical romantic fantasy film,released in which year, the film features an ensemble cast that includes Stanley Tucci, an American character actor, writer, producer and film director?

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
      "description": "The year the film was released."
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "cast_members": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of actors in the film's ensemble cast."
    },
    "stanley_tucci_role": {
      "type": "string",
      "description": "Stanley Tucci's profession as described in the context."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_genre",
    "director",
    "cast_members",
    "stanley_tucci_role"
  ],
  "additionalProperties": false
}
