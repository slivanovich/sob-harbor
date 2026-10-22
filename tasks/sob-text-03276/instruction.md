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
Garry Walberg: Garry Walberg (June 10, 1921 – March 27, 2012) was an American character actor primarily known for his work on television.  He performed in numerous TV shows from the early 1950s, until the early 1990s, including "Johnny Staccato", "Perry Mason", "Lassie", "Peyton Place", "Gunsmoke", "The Fugitive", "Star Trek", "Columbo", "The Tony Randall Show" and "The Rockford Files".  He appeared in the first episode of "The Twilight Zone", entitled "Where Is Everybody? ".

Joel Heyman: Joel Pearce Heyman (born September 16, 1971) is an American actor best-known for voicing Private Michael J. Caboose in the Rooster Teeth web series "Red vs. Blue" (2003–present).  He co-founded Rooster Teeth with Burnie Burns, Matt Hullum, Geoff Ramsey and Gus Sorola and has appeared in a large amount of their other projects, including "The Strangerhood" (2004–2006, 2015), "The Gauntlet" (2012) and "RWBY" (2013–present).

Robert Sacchi: Robert Sacchi (born March 3, 1941 in Bronx, New York) is an American character actor who, since the 1970s, has been known for his close resemblance to Humphrey Bogart.  Sacchi has appeared in many films and TV shows playing either Bogart or a character who happens to look and sound like him.  In a notable episode of "Tales from the Crypt" called "You, Murderer", in 1995 ( season 6 épisode 15 ), Sacchi only provided the voice of a character who looks like Bogart; computer manipulated stock footage of Bogart himself provided the visuals.

Paul Sparer: Paul Sparer (December 19, 1923, in Boston, Massachusetts – November 19, 1999) was an American character actor.  He appeared as Rex Cooper in the soap operas "Somerset" and "Another World".  He was also known for narrating the anthology TV series "Tales from the Darkside".  His film roles include "Loving" and "The House on Carroll Street" while television appearances include "Armstrong Circle Theater", "Kojak", "The Adams Chronicles", "Lou Grant" and "".  Sparer also played Dr. Edward Auster in the first episode of "Law & Order", "Prescription for Death".

Don S. Davis: Don Sinclair Davis, PhD (August 4, 1942 – June 29, 2008) was an American character actor best-known for playing General Hammond in the television series "Stargate SG-1" (1997–2007), and earlier for playing Major Garland Briggs on the television series "Twin Peaks" (1990–1991).  He was also a theater professor, painter, and United States Army captain.

Davis Roberts: Davis Roberts (born Robert A. Davis, March 7, 1917 – July 18, 1993) was an American character actor whose career spanned five decades, from the late 1940s until just before his death in 1993.  He started out making films in the 1940s and 1950s and expanded into television work in the following decades.  Davis was known for his dignified portrayals which were often in contrast to prevailing stereotypical roles.  He played the role of Dr. Caldwell in three episodes in the second and third seasons of the NBC-TV sitcom series "Sanford and Son", and as Dr. Ozaba in the 1968 episode "The Empath" in the original "Star Trek" series.

George Hammond (Stargate): Lieutenant General George S. Hammond, USAF (Ret.)  is a fictional character in the "Stargate franchise".  Played by American actor Don S. Davis, General Hammond serves as the commander of Stargate Command (SGC) in the first seven seasons of the television series "Stargate SG-1".  He is relieved of command in the series' season 7 finale "Lost City", but becomes head of the new Homeworld Security department at the beginning of season 8.  Hammond's off-screen retirement is confirmed in "SG-1"' s season 10, and the character's death is mentioned in the series finale of "SG-1"' s spin-off series "Stargate Atlantis", "Enemy at the Gate".

Top Gear (series 9): The ninth series of "Top Gear" aired during 2007 and consisted of six episodes, beginning on 28 January and concluding on 4 March.  The series featured two specials that were broadcast after the series had ended, -"Top Gear of the Pops" on 16 March and the "" on 25 July.  Production of the series was delayed due to Hammond's accident in September 2006, and did not begin until the following month, and the first episode of the series has subsequently never been repeated on TV owing to Hammond's near-death experience.  In addition, the "Best of Top Gear" special meant to be broadcast before Series 9 and showcase the best moments of Series 8, was delayed and later shown in place of the repeat of the fifth episode of the series.

Episode 8 (Twin Peaks): "Episode 8", also known as "May the Giant Be with You", is the first episode of the second season of the American mystery television series "Twin Peaks".  The episode was written by series co-creators David Lynch and Mark Frost, and directed by Lynch.  It features series regulars Kyle MacLachlan, Michael Ontkean, Ray Wise and Richard Beymer; and guest stars Grace Zabriskie as Sarah Palmer, Chris Mulkey as Hank Jennings, Miguel Ferrer as Albert Rosenfield, Don S. Davis as Major Garland Briggs, and Victoria Catlin as Blackie O'Reilly.

Gage Clarke: Gage Clarke (March 3, 1900 – October 22, 1964) was an American character actor best known for his role as the principal in "Mister Peepers".  His other work consisted largely of one-shot appearances in television series such as seven major supporting roles as different characters in "Maverick", twelve roles in "Gunsmoke" (Clarke played a key role in the "Maverick" spoof of "Gunsmoke", an episode entitled "Gun-Shy"), "Mister Ed", "Laramie", "Ben Casey", "Checkmate", "The Twilight Zone", "The Real McCoys" (twice), four roles in "Alfred Hitchcock Presents", "Bourbon Street Beat", "Thriller", "Have Gun Will Travel", and many others, as well as movies including "I Want to Live! ", "The Bad Seed", "The Brothers Karamazov", and "The Absent-Minded Professor".  Clarke, a slightly overweight actor with a double chin, specialized in playing avuncular, rather timid characters, with one of his largest parts being frightened gambler "Foursquare Farley" in the "Maverick" episode "Greenbacks, Unlimited" opposite James Garner and John Dehner.  He made two guest appearances on "Perry Mason", including the role of Frederick Rollins in "The Case of the Glittering Goldfish" in 1959.  He also played the part of Mr. Murg in "Pollyanna" in 1960.

Question: What series does the American character actor best-known for playing General Hammond star in the first episode?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the American character actor."
    },
    "best_known_role": {
      "type": "string",
      "description": "The role the actor is best known for."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the television series where the actor appeared in a first episode."
    },
    "episode_details": {
      "type": "object",
      "properties": {
        "episode_title": {
          "type": "string",
          "description": "The title of the specific episode."
        },
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "episode_number_in_season": {
          "type": "integer",
          "description": "The episode number within that season."
        },
        "character_played": {
          "type": "string",
          "description": "The character played by the actor in this episode."
        }
      },
      "required": [
        "episode_title",
        "season_number",
        "episode_number_in_season",
        "character_played"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "best_known_role",
    "series_name",
    "episode_details"
  ],
  "additionalProperties": false
}
