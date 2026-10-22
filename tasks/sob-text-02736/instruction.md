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
List of Happy Endings episodes: "Happy Endings" is an American television sitcom broadcast on ABC.  Starring Eliza Coupe, Elisha Cuthbert, Zachary Knighton, Adam Pally, Damon Wayans, Jr., and Casey Wilson, the single-camera ensemble comedy revolves around the lives of a group of friends whose group is rocked when the couple that brought them together, Alex and Dave, break up.  This leaves the rest of the group—Max, Brad, Jane, and Penny—in an awkward position of either trying to stay together as friends or having to choose sides.

Miles Copeland Jr.: Miles Axe Copeland Jr. (July 16, 1916 – January 14, 1991) was an American musician, businessman, and Central Intelligence Agency (CIA) officer best known for his close personal relationship with Egyptian leader Gamal Abdel Nasser and his "controversial books on intelligence," including "The Game of Nations: The Amorality of Power Politics" (1969) and "The Game Player: Confessions of the CIA's Original Political Operative" (1989).  In his memoirs, Copeland recounted his involvement in numerous covert operations, including the March 1949 Syrian coup d'état and the 1953 Iranian coup d'état.  A conservative influenced by the ideas of James Burnham, Copeland was associated with the American political magazine "National Review".  In a 1986 "Rolling Stone" interview, he stated: "Unlike "The New York Times", Victor Marchetti and Philip Agee, my complaint has been that the CIA isn't overthrowing enough anti-American governments or assassinating enough anti-American leaders, but I guess I'm getting old."

Arrested Development (TV series): Arrested Development is an American television sitcom created by Mitchell Hurwitz, which originally aired on Fox for three seasons from November 2, 2003, to February 10, 2006.  A fourth season of 15 episodes was released on Netflix on May 26, 2013.  The show follows the fictitious Bluth family, a formerly wealthy and habitually dysfunctional family.  It is presented in a continuous format, incorporating handheld camera work and voice-over narration, as well as the use of occasional archival photos and historical footage.  The show also utilizes several long-running "Easter egg" jokes throughout each season.  Ron Howard serves as both an executive producer and the series' uncredited narrator.  Set in Newport Beach, California, "Arrested Development" was filmed primarily in Culver City and Marina del Rey.

Stewart Copeland: Stewart Armstrong Copeland (born July 16, 1952) is an American musician and composer, best known as the former drummer for the English rock band the Police, and for his film and video game soundtracks.  Copeland has also written various pieces of music for ballet, opera and orchestra.  According to MusicRadar, Copeland’s "distinctive drum sound and uniqueness of style has made him one of the most popular drummers to ever get behind a drumset".  He was inducted into the Rock and Roll Hall of Fame as a member of the Police in 2003, the "Modern Drummer" Hall of Fame in 2005, and the "Classic Drummer" Hall of Fame in 2013.  In 2016, Copeland was ranked 10th on "Rolling Stone"' s "100 Greatest Drummers of All Time".

Brad Copeland: Brad Copeland is an American television writer and producer, best known for his work on the Fox TV series "Arrested Development".

The Inbetweeners (U.S. TV series): The Inbetweeners is an American comedy television series developed by Brad Copeland for MTV.  The show stars Joey Pollari, Bubba Lewis, Mark L. Young, Zack Pearlman, Alex Frnka and Brett Gelman.  The show is a remake of the original UK series of the same name written and created by Damon Beesley and Iain Morris, who serve as executive producers alongside Copeland, Aaron Kaplan and Lauren Corra.  The show premiered on MTV on August 20, 2012.  On November 28, 2012, MTV decided to cancel the show due to low ratings.

Everybody Loves Raymond: Everybody Loves Raymond is an American television sitcom starring Ray Romano, Patricia Heaton, Brad Garrett, Doris Roberts, Peter Boyle, Madylin Sweeten, and Monica Horan.  It premiered on CBS on September 13, 1996, and concluded on May 16, 2005 after nine seasons.

The Single Guy: The Single Guy is an American television sitcom that ran for two seasons on NBC, from September 1995 to April 1997.  It stars Jonathan Silverman as struggling New York City writer Jonathan Eliot, and followed several of his close friends (some of whom came and left as the show was re-tooled between seasons).  The series also starred Joey Slotnick as Eliot's best friend Sam Sloan, Ming-Na Wen as Sam's wife Trudy and Ernest Borgnine as doorman Manny, throughout its entire run.  "The Single Guy" was created by Brad Hall.

Portia de Rossi: Portia Lee James DeGeneres (born Amanda Lee Rogers; January 31, 1973), also known professionally as Portia de Rossi ( ), is an Australian and American actress, model, and philanthropist.  She appeared as a regular cast member on the American political thriller television series "Scandal" in the role of Elizabeth North from 2014 to 2017.  She is also known for her roles as lawyer Nelle Porter on the American television series "Ally McBeal"—for which she won a Screen Actors Guild Award in 1999—and as Lindsay Fünke on the American television sitcom "Arrested Development."  She also portrayed Veronica Palmer on the ABC television sitcom "Better Off Ted", and Olivia Lord on the television drama "Nip/Tuck".  De Rossi is married to comedian and television host Ellen DeGeneres.

Yogi Bear (film): Yogi Bear is a 2010 American 3D live-action/computer-animated family comedy film directed by Eric Brevig, produced by Donald De Line and Karen Rosenfelt, written by Brad Copeland, Joshua Sternin and Jeffrey Ventimilia and based on the animated television series "The Yogi Bear Show" and the character created by William Hanna and Joseph Barbera.  The film stars Dan Aykroyd, Justin Timberlake, Anna Faris, Tom Cavanagh, T.J. Miller, Nate Corddry and Andrew Daly with narration by Josh Robert Thompson.  The movie tells the story of Yogi Bear as he tries to save his park from being logged.  Principal photography began in November 2009.  It was preceded by the cartoon short "Rabid Rider", starring Wile E. Coyote and Road Runner.

Question: Who created the American television sitcom that Brad Copeland is best known for?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "string",
      "description": "The person whose best-known work is being inquired about."
    },
    "best_known_for_series": {
      "type": "string",
      "description": "The name of the television series the person is best known for."
    },
    "person_role_in_series": {
      "type": "string",
      "description": "The role of the person of interest in their best-known series."
    },
    "series_creator": {
      "type": "string",
      "description": "The creator of the television series."
    }
  },
  "required": [
    "person_of_interest",
    "best_known_for_series",
    "person_role_in_series",
    "series_creator"
  ],
  "additionalProperties": false
}
