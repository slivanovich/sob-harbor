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
Nico Marlet: Nicolas "Nico" Marlet is a French-American animation artist, character designer and skilled drummer.  He is well known for his character design work in the Dreamworks films "Kung Fu Panda" and "How to Train Your Dragon", although early in his career he worked on Disney television shows such as "TaleSpin" and "DuckTales".  He also worked on an unproduced animated version of Andrew Lloyd Webber's "Cats".  His work has appeared in several "art of" books, including "The Art of Kung Fu Panda", "The Art of How to Train Your Dragon", "The Art of Bee Movie", and his own limited edition sketchbook containing some of his personal works.

Kung Fu Panda: Secrets of the Scroll: Kung Fu Panda: Secrets of the Scroll is an animated short film in the "Kung Fu Panda" film series.  It was included on the 2015 Digital HD and 2016 Blu-ray, and DVD re-release of "Kung Fu Panda" and "Kung Fu Panda 2".

Mick Wingert: Mick Wingert (born July 4, 1974) is an American voice actor, comedian and voice-over coach.  He is known for his voice over work in video games, movies and TV shows, as well as the new voice of Master Po and Zeng in "", taking over the roles from actors Jack Black and Dan Fogler.  Wingert has been praised by fans of the "Kung Fu Panda" franchise for his Po voice impression sounding exactly like Jack Black's voice.  He also does additional voice over work in "Kung Fu Panda", "Mass Effect 2", "", "The Technomancer" and "The Princess and the Frog".  He is not related to fellow voice actor Wally Wingert.

Kung Fu Panda (franchise): The "Kung Fu Panda" franchise from DreamWorks Animation consists of three films: "Kung Fu Panda" (2008), "Kung Fu Panda 2" (2011) and "Kung Fu Panda 3" (2016).  The first two were distributed by Paramount Pictures, while the third film was distributed by 20th Century Fox.  Three shorts, "Secrets of the Furious Five" (2008), "Kung Fu Panda Holiday Special" (2010) and "" (2011), were also released.  A television series for Nickelodeon television network, "", premiered in the fall of 2011.

Jack Black: Thomas Jacob "Jack" Black (born August 28, 1969) is an American actor, comedian, writer, producer, and singer.  His acting career has been extensive, starring primarily in comedy films.  He is best known for his roles in "Shallow Hal" (2001), "School of Rock" (2003), "King Kong" (2005), "The Holiday" (2006), the "Kung Fu Panda" franchise (2008–2016), "Tropic Thunder" (2008), and "Bernie" (2011).  He has been nominated for two Golden Globe Awards.  Black is the lead vocalist of the comedic rock group Tenacious D which he formed in 1994 with friend Kyle Gass.  They have released the albums "Tenacious D", "The Pick of Destiny" and "Rize of the Fenix".

Kung Fu Panda 3: Kung Fu Panda 3 is a 2016 3D computer-animated action-comedy martial arts film produced by DreamWorks Animation and distributed by 20th Century Fox.  It is the third installment in the "Kung Fu Panda" franchise, and the sequel to 2011's "Kung Fu Panda 2".  In the film, Po enters the panda village and re-unites with his birth father and other pandas, but problems arise when a villainous spirit warrior, named Kai, returns to the mortal realm and steals chi from the kung fu masters.  To prevent Kai from taking chi from all kung fu masters and pandas, Po forms the army of pandas to battle Kai's jade minions and Po must become a master of chi to defeat him and save his friends.

Kung Fu Panda: Kung Fu Panda is a 2008 American computer-animated action comedy martial arts film produced by DreamWorks Animation and distributed by Paramount Pictures.  It was directed by John Stevenson and Mark Osborne and produced by Melissa Cobb, and stars the voices of Jack Black, Dustin Hoffman, Angelina Jolie, Ian McShane, Seth Rogen, Lucy Liu, David Cross, Randall Duk Kim, James Hong, and Jackie Chan.  Set in a version of ancient China populated by anthropomorphic talking animals, the plot revolves around a bumbling panda named Po who aspires to be a kung fu master.  When an evil kung fu warrior is foretold to escape after twenty years in prison, Po is unwittingly named the chosen one destined to defeat him and bring peace to the land, much to the chagrin of the resident kung fu warriors.

Kung Fu Panda 2: Kung Fu Panda 2 is a 2011 3D American computer-animated comedy-drama martial arts film, directed by Jennifer Yuh Nelson, produced by DreamWorks Animation, and distributed by Paramount Pictures.  It is the sequel to the 2008 film "Kung Fu Panda" and the second installment in the "Kung Fu Panda" franchise.

The Big Year: The Big Year is a 2011 American comedy film directed by David Frankel, written by Howard Franklin and starring Jack Black, Steve Martin, and Owen Wilson.  It was based on the nonfiction book "The Big Year: A Tale of Man, Nature and Fowl Obsession" which was written by journalist Mark Obmascik.  The book followed three men on a quest for a Big Year—a competition among birders to see who can see and identify the greatest number of species of birds in North America (north of Mexico) in a calendar year.  The film uses the same premise with fictional characters loosely modeled on the actual personalities.

List of Kung Fu Panda characters: The following is a list of characters from the DreamWorks animated film media franchise "Kung Fu Panda", with their shorts and specials "Secrets of the Furious Five", "Kung Fu Panda Holiday", "", and "", as well as the video games and TV show "".

Question: Who starred in Kung Fu Panda as well as The Big Year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in both films."
    },
    "films_matched": {
      "type": "array",
      "description": "A list of films the actor starred in, as specified in the question.",
      "items": {
        "type": "string"
      }
    },
    "number_of_films_matched": {
      "type": "integer",
      "description": "The count of films the actor starred in, as specified in the question."
    }
  },
  "required": [
    "actor_name",
    "films_matched",
    "number_of_films_matched"
  ],
  "additionalProperties": false
}
