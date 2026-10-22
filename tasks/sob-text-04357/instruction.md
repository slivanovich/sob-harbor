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
A Tramp Shining: A Tramp Shining is the debut album of Richard Harris, released in 1968 by Dunhill Records.  The album was written, arranged, and produced by singer-songwriter Jimmy Webb.  Although Harris sang several numbers on the soundtrack album to the film musical "Camelot" the previous year, "A Tramp Shining" was Harris' first solo album. " MacArthur Park" was one of the biggest singles of that year, reaching #2 on the "Billboard" Hot 100 chart in the United States.  The album as a whole was also highly successful, and was nominated for a Grammy Award for "Album of the Year" in 1969.

Unidentified Flying Oddball: Unidentified Flying Oddball (also known as The Spaceman and King Arthur and A Spaceman in King Arthur's Court) is a 1979 film adaptation of Mark Twain's "A Connecticut Yankee in King Arthur's Court", directed by Russ Mayberry and produced by Walt Disney Productions.  Subsequently re-released in the United States under the titles "The Spaceman and King Arthur" and "A Spaceman in King Arthur’s Court", the film starred Dennis Dugan as NASA employee Tom Trimble who unintentionally travels back in time with his look-alike android Hermes.  Trimble’s NASA spacecraft travels faster than the speed of light, landing him and the android near King Arthur’s Camelot, where – with the aid of their 20th-century technology – they must defeat a plot by the evil Sir Mordred and Merlin to oust King Arthur from the throne.

Titus (film): Titus is a 1999 Italian-American-British film adaptation of William Shakespeare's revenge tragedy "Titus Andronicus", about the downfall of a Roman general.  Starring Anthony Hopkins and Jessica Lange, it was the first theatrically-released feature film adaptation of the play.  The film was made by Overseas Filmgroup and Clear Blue Sky Productions and released by Fox Searchlight Pictures.  It was the film directorial debut of Julie Taymor, who co-produced and wrote the screenplay.  It was produced by Jody Patton, Conchita Airoldi and executive produced by Paul G. Allen.

Camelot (musical): Camelot is a musical by Alan Jay Lerner (book and lyrics) and Frederick Loewe (music).  It is based on the King Arthur legend as adapted from the T. H. White novel "The Once and Future King".

Chris Weitz: Christopher John "Chris" Weitz (born November 30, 1969) is an American film producer, screenwriter, author, occasional actor, and film director.  He is the brother of filmmaker Paul Weitz.  He is best known for his work with his brother on the comedy films "American Pie" and "About a Boy," the latter of which was Oscar-nominated for adapted screenplay.  Weitz directed the film adaptation of the novel "The Golden Compass" and the of "New Moon" from the series of "Twilight" books, as well wrote the screenplay for Disney's 2015 live-action adaptation of "Cinderella" and co-wrote "Rogue One: A Star Wars Story" alongside with Tony Gilroy.

Quest for Camelot: Quest for Camelot (released in the United Kingdom as The Magic Sword: Quest for Camelot) is a 1998 American animated musical fantasy film directed by Frederik Du Chau and based on the novel "The King's Damosel" by Vera Chapman.  The film stars Jessalyn Gilsig, Cary Elwes, Jane Seymour, Gary Oldman, Eric Idle, Don Rickles, Pierce Brosnan, Bronson Pinchot, Jaleel White, Gabriel Byrne, and John Gielgud.  Céline Dion, Bryan White, Steve Perry, and Andrea Corr perform vocals.  The film was released on May 15, 1998, by Warner Bros.  Family Entertainment.

Camelot (film): Camelot is a 1967 American musical comedy-drama film directed by Joshua Logan and starring Richard Harris as King Arthur, Vanessa Redgrave as Guenevere, and Franco Nero as Lancelot.  The film is an adaptation of the homonymous musical by Alan Jay Lerner and Frederick Loewe.  Lerner also wrote the screenplay.

M'el Dowd: M'el Dowd (February 2, 1933 – September 26, 2012) was an American stage, musical theatre and film actress, and singer, whose career spanned more than 50 years.  Beginning in Shakespeare roles and films in the 1950s, Dowd continued to perform on stage, film and television into the 21st century.  A frequent performer on Broadway in the 1960s, Dowd originated the role of Morgan le Fay in the musical "Camelot".

Matthew Michael Carnahan: Matthew Michael Carnahan (sometimes credited as Matt Carnahan) is an American screenwriter who wrote the feature film "The Kingdom" (2007), and "the film adaptation" of the hit BBC television drama serial "State of Play".  Carnahan also wrote the screenplay for "Lions for Lambs" for United Artists.  His brother is Joe Carnahan, who wrote and directed "Narc" (2002), "Smokin' Aces" (2006) and "The A-Team" (2010).

New Line Theatre: New Line Theatre in St. Louis, Missouri, is an alternative musical theatre company producing challenging, adult, politically and socially relevant works of musical theatre.  The company was created in 1991 and produces world premieres such as "Love Kills, Johnny Appleweed, Woman with Pocketbook, She's Hideous, In the Blood, Attempting the Absurd", and "The AmberKlavier"; lesser known Broadway and off Broadway shows such as "High Fidelity, Passing Strange, , The Wild Party, Floyd Collins, A New Brain, March of the Falsettos, Passion, The Robber Bridegroom, The Nervous Set", and ""; abstract musicals such as "Hair, Jacques Brel is Alive and Well and Living in Paris", and "Songs for a New World"; absurdist musicals such as "Reefer Madness, Attempting the Absurd, The Cradle Will Rock", and "Anyone Can Whistle"; concept musicals such as "Company", "Assassins", "Urinetown", "Chicago", "Sunday in the Park with George", and "Cabaret"; and reinterpretations of more mainstream works, such as "Evita", "Man of La Mancha", "Camelot", "Pippin", "Sweeney Todd", "Grease", and "Into the Woods".

Question: Who created the Camelot musical and wrote the screenplay for the Camelot film adaptation? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who made contributions to the Camelot musical and film."
    },
    "musical_contribution": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the musical."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in creating the musical."
        }
      },
      "required": [
        "title",
        "role"
      ],
      "additionalProperties": false
    },
    "film_contribution": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film adaptation."
        },
        "role": {
          "type": "string",
          "description": "The role of the person in the film adaptation."
        }
      },
      "required": [
        "title",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "musical_contribution",
    "film_contribution"
  ],
  "additionalProperties": false
}
