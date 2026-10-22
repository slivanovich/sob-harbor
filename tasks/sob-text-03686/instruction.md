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
Addicted (Devin Townsend Project album): Addicted is the twelfth studio album by Canadian musician Devin Townsend, and the second album in the Devin Townsend Project series.  The album was released on November 17, 2009, on Townsend's independent record label HevyDevy Records.  The album was written and produced by Townsend, and features Ryan Van Poederooyen, Brian Waddell, Mark Cimino, and Anneke van Giersbergen.

Geoffrey Wilder: Geoffrey Wilder is a fictional supervillain in the Marvel Comics series "Runaways".  Geoffrey is the leader of the Pride, a supervillain crime ring in Los Angeles.  He is the father of Alex Wilder.

Runaways (TV series): Marvel's Runaways, or simply Runaways, is an upcoming American web television series created for Hulu by Josh Schwartz and Stephanie Savage, based on the Marvel Comics superhero team of the same name.  It is set in the Marvel Cinematic Universe (MCU), sharing continuity with the films and other television series of the franchise.  The series is produced by ABC Signature Studios, Marvel Television and Fake Empire Productions, with Schwartz and Savage serving as showrunners.

Body of Proof (season 2): The second season of "Body of Proof", an American television series created by Christopher Murphey, commenced airing in the United States on September 20, 2011, concluded April 10, 2012, and consisted of 20 episodes.  It follows the life and career of Dr. Megan Hunt, a medical examiner, once a neurosurgeon, who now works in Philadelphia's Medical Examiner's office after a car accident ended her neurosurgery career.  Along with Hunt solving homicide cases are her colleagues, Nicholas Bishop as Peter Dunlop, Jeri Ryan as Dr. Kate Murphy, John Carroll Lynch and Sonja Sohn as Detective's Bud Morris and Samantha Baker and fellow medical examiners, Geoffrey Arend as Dr. Ethan Gross and Windell Middlebrooks as Dr. Curtis Brumfield.  Mary Mouser who plays Megan's daughter Lacey was promoted to "regular" from "recurring" status from season 1.  Jeffrey Nordling who plays Megan's ex-husband Todd, Joanna Cassidy who plays her mother Joan and Eric Sheffer Stevens who plays Bill Parkson all reprise their roles, whilst Cliff Curtis, Nathalie Kelley and Jamie Bamber join the show, all of which appear on a "recurring" basis.

Jack Ryan: Shadow Recruit: Jack Ryan: Shadow Recruit is a 2014 American action spy thriller film directed by Kenneth Branagh.  Chris Pine, Kevin Costner, Kenneth Branagh, and Keira Knightley star in leading roles.  The film features the fictional character Jack Ryan created by author Tom Clancy.  It is the fifth film in the "Jack Ryan" series but is presented as a reboot that departs from the previous installments.  Unlike its predecessors, it is not an adaptation of a particular Clancy novel, but rather an original story.  Pine stars in the title role, becoming the fourth actor to play Ryan, following Alec Baldwin, Harrison Ford, and Ben Affleck.

Magi-Nation Duel: Magi-Nation Duel, sometimes abbreviated "MND" or simply Magi-Nation, is a collectible card game (CCG) published by Interactive Imagination Corp (2i).  It was previewed at Gen Con 2000 and was released in October 2000.  Lead Designer and Co-Founder of 2i Phillip Tavel created a game with mechanics which resembled and were partially based on , while much of the flavor of the game was based on the anime-style artwork of Matt Holmberg.  Greg Richardson Von Oy (the other original Co-Founder of 2i) and Josh Lytle (a former professional gamer) helped to playtest and finalize the original design of the game.  Several manga-style American artists led by Art Director: Thomas Cook include Matt Holmberg, Rich Werner (Main character designer for Kybar's Teeth, Weave, Paradwyn, Bograth, Nar and The Sands of Dresh), Tim Gillette, Chana Goodman, and Ryan Shreve helped to expand the universe of art based on the original creations of Matt Holmberg.  The game was originally designed as a bridge between Pokémon and .  The idea was that younger players whose first game was Pokémon would eventually seek out a new game to play and that Magic: The Gathering might be too complex for some players, leaving a void in the market between the two massively popular card games .  The game is now out of print.  A new version of the game, licensed by Cookie Jar tm, was to be released in 2008, but no relaunch ever surfaced.

Tumbleweeds (comic strip): Tumbleweeds was an American comic strip that offered a skewed perspective on life in the Old West.  Writer-artist Tom K. Ryan (1926 – ) (who signed the strip "T.K. Ryan") was very familiar with conventions of the Western genre he satirized.  Launched September 1965, the strip was distributed for decades initially by the Register and Tribune Syndicate and later by the King Features Syndicate after its acquisition.  Jim Davis, who created "Garfield", was Ryan's assistant (from 1969 to 1978) while developing another strip, "Gnorm Gnat".  After a 42-year run, Ryan retired and brought "Tumbleweeds" to a conclusion on December 30, 2007.

Rocketeer (song): "Rocketeer" is the second single from Far East Movement's 2010 album "Free Wired".  The track features Ryan Tedder of OneRepublic.  It was written by Far East Movement, as well as members of the production teams The Stereotypes, The Smeezingtons, and produced by The Stereotypes and The Smeezingtons.  It was released as a single on October 29, 2010, and peaked at number 7 on the "Billboard" Hot 100.

Steve Ryan (author): Steve Ryan (born February 15, 1949 in San Diego, California) is an American author who specializes in the creation of games and puzzles.  Ryan is also a television game show historian and creator.  Ryan was a long-standing staff member of Goodson-Todman Productions and Mark Goodson Productions, where he created the concept for the game show "Blockbusters".  Ryan also created the rebus puzzles for the game show "Classic Concentration".  He was also a writer and creator of puzzles for the game shows "Body Language", "Catch Phrase", "Password Plus" and "Trivia Trap".

Ryan Sands: Ryan Sands is best recognized as Officer Lloyd "Truck" Garrick on "The Wire" and has since made one off appearances in shows such as "Grimm", "Castle", "Scorpion", "NCIS" and "Prison Break".  Sands was cast as Geoffrey Wilder in the Hulu adaptation of "Marvel's Runaways".

Question: Who created the show that features Ryan Sands as Geoffrey Wilder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_title": {
      "type": "string",
      "description": "The title of the television series."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "creators": {
      "type": "array",
      "description": "A list of individuals credited as creators of the show.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "show_title",
    "character_played",
    "actor_name",
    "creators"
  ],
  "additionalProperties": false
}
