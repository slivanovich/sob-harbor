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
The SpongeBob SquarePants Movie: The SpongeBob SquarePants Movie is a 2004 American live-action/animated comedy film based on the Nickelodeon television series "SpongeBob SquarePants".  The film was co-written, directed, and co-produced by series creator Stephen Hillenburg and starred the series' cast of Tom Kenny, Bill Fagerbakke, Clancy Brown, Rodger Bumpass and Mr. Lawrence, with guest performances by Scarlett Johansson, Jeffrey Tambor, Alec Baldwin and David Hasselhoff.  It was produced by Hillenburg's production company United Plankton Pictures and Nickelodeon Movies, it was distributed by Paramount Pictures and was also the first film in the "SpongeBob SquarePants" film series.  In the film, Plankton devises a plan to steal King Neptune's crown and send it to Shell City, and SpongeBob and Patrick must retrieve the crown to save Mr. Krabs from King Neptune's wrath and Bikini Bottom from Plankton's plan.

Paul Tibbitt: Paul Harrison Tibbitt is an American animator, television producer, writer, storyboard artist, songwriter, voice actor, and director, best known for working on the animated series "SpongeBob SquarePants".  He was the co-executive producer of the show and was also the voice of Potty the Parrot; he has also voiced DoodleBob and previously voiced Betsy Krabs before Sirena Irwin took over.  He made his feature film directorial debut directing "".  Tibbitt studied in the Character Animation program at the California Institute of the Arts.

SpongeBob, You're Fired: "SpongeBob, You're Fired" is a television special of the American animated television series "SpongeBob SquarePants".  It serves as the 11th episode of the ninth season and the 189th overall episode.  The animation directors were the supervising director, Alan Smart and Tom Yasumi, and was written by Marc Ceccarelli, Luke Brookshier, and Mr. Lawrence.  Ceccarelli and Brookshier also served as storyboard directors.  The episode originally aired in Greece on July 3, 2013.  In the United States, it aired on Nickelodeon on November 11.  In this episode of the series, which follows the adventures and endeavors of the title character and his various friends in the underwater city of Bikini Bottom, SpongeBob gets fired from the Krusty Krab after Mr. Krabs discovers he can save a nickel by eliminating him.  SpongeBob subsequently decides to apply at other restaurants.

List of SpongeBob SquarePants cast members: "SpongeBob SquarePants" is an American animated television series created by marine biologist and animator Stephen Hillenburg that debuted on Nickelodeon in the United States on May 1, 1999.  The regular voice cast consists of Tom Kenny, Clancy Brown, Rodger Bumpass, Bill Fagerbakke, Mr. Lawrence, Jill Talley, Carolyn Lawrence, Mary Jo Catlett and Lori Alan.  Most one-off and background characters are voiced by Dee Bradley Baker, Sirena Irwin, Bob Joles, Mark Fite and Thomas F. Wilson.  Throughout the show's run, it has employed numerous guest stars from many ranges of professions.  Repeat guests include Ernest Borgnine, Tim Conway, Brian Doyle-Murray, Marion Ross, John O'Hurley and Michael McKean.

Friend or Foe (SpongeBob SquarePants): "Friend or Foe" is the first episode of the fifth season and the 81st overall episode of the American animated television sitcom "SpongeBob SquarePants".  It was written by Casey Alexander, Zeus Cervas, Mike Mitchell, Steven Banks and Tim Hill, and the animation was directed by supervising director, Alan Smart and Tom Yasumi.  Alexander, Cervas and Mitchell also function as storyboard directors.  The episode originally aired on Nickelodeon in the United States on April 13, 2007.

Sirena Irwin: Sirena Irwin is an actress whose credits include Mrs. SquarePants on the animated television comedy, "SpongeBob SquarePants".  She also voiced Mama Krabs in the episodes "Enemy In-Law" and "Friend or Foe" among many others and also voiced Squilvia in "Love that Squid" (SpongeBob SquarePants).  She was a series regular on Stan Lee's "Stripperella" as Persephone Cliche and has guest and co-starred in multiple television shows.  She was a lead in "The Trip", a popular gay film.  She also provided the voices for Mera and Lois Lane in "".  In 2011 she premiered the role of Lucy Ricardo in "I Love Lucy: Live on Stage" in Los Angeles, and has toured with that show for several years.  She was awarded Best Actress in a Touring Production at the BroadwayWorld Chicago Awards for the role.

SpongeBob SquarePants: Lights, Camera, Pants!: SpongeBob SquarePants: Lights, Camera, Pants!  is a 2005 party video game based on the TV series "SpongeBob SquarePants".  It was released in October 2005 for the Xbox, PlayStation 2, GameCube, Game Boy Advance, and the PC.  It was released for the Nintendo DS in Korea in 2007, but its North American release was cancelled.  It is the first "SpongeBob SquarePants" title to feature multiplayer mini-games, similar to the "Mario Party" video game series.  It is also the last SpongeBob game for the Xbox.  It is also the last time Charles Nelson Reilly would voice the Dirty Bubble before his death in 2007.  For reasons unknown, Mermaid Man was not voiced by his original voice actor Ernest Borgnine but instead Joe Alaskey, who would voice him again in .

Krusty Krab: The Krusty Krab is a fictional fast food restaurant in the American animated television series "SpongeBob SquarePants".  It was founded by Mr. Krabs, who is also the owner.  The restaurant has two employees: SpongeBob SquarePants and Squidward Tentacles.  Famous for its Krabby Patty sandwiches, it is a rival of Plankton's across-the-street restaurant The Chum Bucket and as a result, the character frequently plots schemes to obtain the Krabby Patty formula.  The restaurant first appears in the pilot episode, "Help Wanted" and has since become a common setting in the series.

List of SpongeBob SquarePants guest stars: In addition to the show's regular cast of voice actors, guest stars have been featured on "SpongeBob SquarePants", an American animated television series created by marine biologist and animator Stephen Hillenburg for Nickelodeon.  "SpongeBob SquarePants" chronicles the adventures and endeavors of the title character and his various friends in the fictional underwater city of Bikini Bottom.  Many of the ideas for the show originated in an unpublished, educational comic book titled "The Intertidal Zone", which Hillenburg created in the mid-1980s.  He began developing "SpongeBob SquarePants" into a television series in 1996 upon the cancellation of "Rocko's Modern Life", which Hillenburg directed.  The pilot episode first aired on Nickelodeon in the United States on May 1, 1999.  The show's ninth season premiered in 2012, and episodes of "SpongeBob SquarePants" have aired.  A feature-length film adaptation of the show, "The SpongeBob SquarePants Movie", was released in 2004; in 2015, a sequel, "", was released.

Help Wanted (SpongeBob SquarePants): "Help Wanted" is the pilot episode of the American animated television series "SpongeBob SquarePants".  It originally aired on Nickelodeon in the United States on May 1, 1999, following the television airing of the 1999 Kids' Choice Awards.  The episode follows the protagonist, an anthropomorphic sea sponge named SpongeBob SquarePants, attempting to get a job at a local restaurant called the Krusty Krab.  However, he is tasked to find a seemingly non-existent high-caliber spatula because the owner, Mr. Krabs, considers him unqualified for the position.  Eventually, crowds of ravenous anchovies stop by the Krusty Krab and demand meals.  SpongeBob returns from his errand, having fulfilled the request of Mr. Krabs and found a mechanical spatula.  He utilizes the spatula to fulfill the anchovies' hunger.  SpongeBob is then welcomed by Mr. Krabs as a Krusty Krab employee.

Question: Sirena Irwin voiced Mama Krabs in which first episode of the 5th season of SpongeBob SquarePants?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "episode_title": {
      "type": "string",
      "description": "The title of the episode."
    },
    "season_number": {
      "type": "integer",
      "description": "The season number of the episode."
    },
    "episode_order_in_season": {
      "type": "integer",
      "description": "The order of the episode within its season."
    },
    "character_voiced": {
      "type": "string",
      "description": "The character voiced by the actor in the episode."
    },
    "voice_actor": {
      "type": "string",
      "description": "The name of the voice actor."
    }
  },
  "required": [
    "episode_title",
    "season_number",
    "episode_order_in_season",
    "character_voiced",
    "voice_actor"
  ],
  "additionalProperties": false
}
