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
Fantastic Four: The Fantastic Four is a fictional superhero team appearing in American comic books published by Marvel Comics.  The group debuted in "The Fantastic Four" #1 (cover dated Nov. 1961), which helped to usher in a new level of realism in the medium.  The Fantastic Four was the first superhero team created by editor/co-plotter Stan Lee and artist/co-plotter Jack Kirby, who developed a collaborative approach to creating comics with this title that they would use from then on.

All-Winners Squad: The All-Winners Squad is a fictional superhero team appearing in American comic books published by Marvel Comics.  The company's first such team, it first appeared in "All Winners Comics" #19 (Fall 1946), published by Marvel predecessor Timely Comics during the period fans and historians call the Golden Age of Comic Books.

Bruce Davison: Bruce Davison (born June 28, 1946) is an American actor and director.  Davison is well known for his starring role in the cult horror film "Willard" (1971), as well as his Academy Award-nominated and Golden Globe-winning performance in "Longtime Companion" (1989).  He featured prominently in the X-Men film franchise – through "X-Men" (2000) and "X2" (2003) – as antagonist Senator Robert Kelly.

Knights of Pendragon: The Knights of Pendragon is a superhero team appearing in American comic books published by Marvel Comics.  The team was published by the imprint Marvel UK in a self-titled comic from 1990 to 1993, and in the anthology title "Overkill".  It was written by Dan Abnett and John Tomlinson with art by Gary Erskine.  Pendragon is an alternate name for King Arthur.

Justice Society of America: The Justice Society of America (JSA) is a superhero team appearing in American comic books published by DC Comics.  The Justice Society of America was conceived by editor Sheldon Mayer and writer Gardner Fox.  The JSA first appeared in "All Star Comics" #3 (Winter 1940–1941), making it the first team of superheroes in comic books.

Stormwatch (comics): Stormwatch is a fictional superhero team appearing in American comic books published by WildStorm, which later became an imprint of DC Comics.  Created by Jim Lee, the team first appeared in "Stormwatch" #1 (March 1993).  After the WildStorm imprint was retired and its universe was merged with the main DC Universe, the group was depicted as a secretive team of superheroes who tackle dangerous missions while remaining unknown to the larger superhero community.

Agents of Atlas: Agents of Atlas is a fictional superhero team appearing in American comic books published by Marvel Comics.  It is composed of characters originally appearing in unrelated stories published in the 1950s by Marvel's predecessor company, Atlas Comics.

X2 (film): X2 (often promoted as X2: X-Men United and internationally as X-Men 2) is a 2003 American superhero film based on the X-Men superhero team appearing in Marvel Comics.  It is the sequel to 2000's "X-Men", and the second installment in the "X-Men" film series.  The film was directed by Bryan Singer, written by Michael Dougherty, Dan Harris, and David Hayter, and features an ensemble cast including Hugh Jackman, Patrick Stewart, Ian McKellen, Halle Berry, Famke Janssen, James Marsden, Rebecca Romijn-Stamos, Brian Cox, Alan Cumming, Bruce Davison, Shawn Ashmore, Aaron Stanford, Kelly Hu, and Anna Paquin.  The plot, inspired by the graphic novel "", pits the X-Men and their enemies, the Brotherhood, against the genocidal Colonel William Stryker (Brian Cox).  He leads an assault on Professor Xavier's school to build his own version of Xavier's mutant-tracking computer Cerebro, in order to destroy every mutant on Earth and to save the human race from them.

Teen Titans: The Teen Titans, also known as the New Teen Titans and the Titans, are a fictional superhero team appearing in American comic books published by DC Comics, often in an eponymous monthly series.  As the group's name suggests, its members are teenage superheroes, many of whom have acted as sidekicks to DC's premiere superheroes in the Justice League.  First appearing in 1964 in "The Brave and the Bold" #54, the team was founded by Kid Flash (Wally West), Robin (Dick Grayson), and Aqualad (Garth), with the team adopting the name Teen Titans in issue 60 following the addition of Wonder Girl (Donna Troy) to its ranks.

Liberty Legion: The Liberty Legion is a fictional superhero team appearing in American comic books published by Marvel Comics.  The team was first created in 1976 and set during World War II.  Composed of existing heroes from Marvel's 1940s Golden Age of Comic Books predecessor, Timely Comics, the team was assembled and named by writer Roy Thomas in a story arc running through "The Invaders" #5–6 (March & May 1976) and "Marvel Premiere" #29–30 (April & June 1976).  Inspired by the "Liberty Legion", a second fictional team called the "Liberteens" was published in 2007 as part of the .

Question: The movie franchise in which Bruce Davidson plays antagonist Senator Robert Kelly is based on a superhero team appearing in what company's comic books?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor mentioned in the question."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "film_franchise_name": {
      "type": "string",
      "description": "The name of the film franchise in which the character appears."
    },
    "superhero_team_name": {
      "type": "string",
      "description": "The name of the superhero team the film franchise is based on."
    },
    "comic_book_company": {
      "type": "string",
      "description": "The comic book company that publishes the superhero team."
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "film_franchise_name",
    "superhero_team_name",
    "comic_book_company"
  ],
  "additionalProperties": false
}
