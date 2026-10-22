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
Fat Man and Little Boy: Fat Man and Little Boy (a.k.a. Shadow Makers in the UK) is a 1989 film that reenacts the Manhattan Project, the secret Allied endeavor to develop the first nuclear weapons during World War II.  The film is named after the weapons "Little Boy" and "Fat Man" that were detonated over Hiroshima and Nagasaki, respectively.  The code names, originally Fat Man and Thin Man, were drawn from characters in the works of Dashiell Hammett.  However, there's a possible secondary allusion to stout project director Gen. Leslie Groves and the slim scientific director, Dr. J. Robert Oppenheimer.  The film focuses much attention on the frequently strained relationship between the two men.

TVB Anniversary Award for Best Supporting Actor: The TVB Anniversary Award for Best Actor in a Supporting Role is one of the TVB Anniversary Awards presented annually by Television Broadcasts Limited (TVB) to recognize an actor who has delivered an outstanding performance in Hong Kong television dramas throughout the designated year.  This award was not introduced to the awards ceremony until 2003, six years after its establishment.  The Best Supporting Actor award was first called the My Favourite Powerhouse Actor of the Year (本年度我最喜愛的實力非凡男藝員) in 2003.  The name was changed to Best Actor in a Supporting Role (最佳男配角) in 2005.

Katie Cassidy: Katherine Evelyn Anita Cassidy (born November 25, 1986) is an American actress.  After initially appearing in minor television roles, she made her film debut in "When a Stranger Calls" (2006).  During the same year, she also had her first starring role as Kelli Presley in "Black Christmas" (2006).  In 2007, Cassidy gained attention for her role as Ruby on the supernatural-horror television series "Supernatural", during its third season.  She later had a supporting role in "Taken".  In 2009, Cassidy became a cast member of the series "Harper's Island" and "Melrose Place", both of which lasted for only one season.  During 2010, she had a supporting role as Kris Fowles in "A Nightmare on Elm Street" and a recurring role during the fourth season of "Gossip Girl".

Gerald Hiken: Gerald Hiken (born May 27, 1927) is an American actor.  A native of Milwaukee, Hiken was nominated for the Tony Award for Best Actor in a Play in 1980 for his performance in "Strider".  He has performed in many other Broadway plays and has appeared in supporting and bit roles in various films including "The Candidate" (1972), "Reds" (1981), and "Fat Man and Little Boy" (1989).

Bodil Award for Best Actor in a Supporting Role: The Bodil Award for Best Actor in a Supporting Role (Danish: "Bodilprisen for bedste mandlige birolle" ) is one of the merit categories presented by the Danish Film Critics Association at the annual Bodil Awards.  Created in 1948, it is one of the oldest film awards in Europe, and it honours the best performance by an actor in a supporting role in a Danish produced film.  The jury can decide not to hand out the award, which happened numerous times between 1950 and 1985.  Since 1986 it has been awarded every year.

Haskell V. Anderson III: Haskell Vaughn Anderson III is an American film, television and theater actor.  He is most known for his prominent supporting role in the 1989 film "Kickboxer", which starred Jean-Claude Van Damme.  Other Independent Film Star roles include the 1978 film "Brotherhood of Death", which was his first starring role on film and the 2007 Independent feature "Boy and Dog".

Armed Forces Special Weapons Project: The Armed Forces Special Weapons Project (AFSWP) was a United States military agency responsible for those aspects of nuclear weapons remaining under military control after the Manhattan Project was succeeded by the Atomic Energy Commission on 1 January 1947.  These responsibilities included the maintenance, storage, surveillance, security and handling of nuclear weapons, as well as supporting nuclear testing.  The AFSWP was a joint organization, staffed by the United States Army, United States Navy and United States Air Force; its chief was supported by deputies from the other two services.  Major General Leslie R. Groves, the former head of the Manhattan Project, was its first chief.

Raghavendra Rajkumar: Raghavendra Rajkumar is an Indian film producer and former actor in Kannada cinema.  He is the second son of actor Rajkumar and film producer Parvathamma.  He made his film debut as a lead actor in "Chiranjeevi Sudhakara" (1988) before appearing the hugely successful 1989 film "Nanjundi Kalyana".  Following this, he had a largely forgettable career, and retired from acting in 2004.  He has since produced three films under Vajreshwari Combines.  His son Vinay Rajkumar is an actor.

Arthur W. Adamson: Arthur Wilson Adamson (1919–2003) was an American chemist who is considered a pioneer in inorganic photochemistry.  His research made significant contributions to the understanding of physical adsorption and contact angle phenomena, and the thermodynamics of surfaces and irreversible adsorption.  Born to American missionaries in Shanghai, China, he received his B.S. in chemistry at the University of California at Berkeley in 1940 and his Ph.D. in physical chemistry at the University of Chicago in 1944.  After two years as a research associate for the Manhattan Project in Oak Ridge, Tennessee, he began a career at the University of Southern California that extended through his appointment as professor emeritus in 1989.  He chaired the USC Department of Chemistry from 1972 to 1975.

Bob Frazer: Bob Frazer (born 1971) is an award winning actor, born in Ontario.  He currently lives in British Columbia.  He has appeared in many roles both on stage and in television, and has won multiple Jessie Richardson Theatre Awards, including: "Outstanding Performance by an Actor in a Leading Role" (2005–2006) for his role in "Hamlet", "Outstanding Performance by an Actor in a Supporting Role" (2005–2006) for his role in "Prodigal Son", and won for "Significant Artistic Achievement" (2003–2004).  He has also been a nominee over ten times including "Outstanding Performance by an Actor in a Supporting Role" (2003–2004) for "The Glass Menagerie"; Iago in Shakespeare's "Othello"; and as Antipholus of Ephesus in "Comedy of Errors" during the 2009 season of Bard on the Beach.

Question: Appearing in a supporting role in a 1989 film that reenacts the Manhattan Project, what other film did this actor appear in in 1972?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor identified by the criteria."
    },
    "film_manhattan_project": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film reenacting the Manhattan Project."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "role_type": {
          "type": "string",
          "description": "The type of role the actor had in this film (e.g., supporting, bit)."
        }
      },
      "required": [
        "title",
        "year",
        "role_type"
      ],
      "additionalProperties": false
    },
    "other_film_1972": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the other film the actor appeared in in 1972."
        },
        "year": {
          "type": "integer",
          "description": "The release year of this film."
        }
      },
      "required": [
        "title",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "film_manhattan_project",
    "other_film_1972"
  ],
  "additionalProperties": false
}
