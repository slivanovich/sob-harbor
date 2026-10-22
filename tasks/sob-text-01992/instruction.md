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
Joe Whyte: Joseph "Joe" Whyte (born April 18, 1961) is an American actor and voice actor.  He attended California State University, where he performed in acting groups.  Whyte has also been working for Disney.  He is best known for voicing Mermaid Man in the "SpongeBob SquarePants" video games series, as well as voicing Mr. Krabs in some of the SpongeBob video games, when Clancy Brown was not available.

Thunder Alley: Thunder Alley is an American sitcom which aired from March 9, 1994 to July 4, 1995 on ABC.

Thunder Alley (1985 film): Thunder Alley is a 1985 American drama film written and directed by J. S. Cardone.  The film stars Leif Garrett, Roger Wilson, Jill Schoelen, Scott McGinnis, Cindy Eilbacher and Clancy Brown.  The film was released on August 1, 1985, by The Cannon Group, Inc..

Thunder Alley (film): Thunder Alley is a 1967 film about auto racing, directed by Richard Rush and starring Annette Funicello and Fabian Forte.  It was released by American International Pictures.

Robin Riker: Robin Riker (born October 2, 1952) is an American actress and author.  After deciding to pursue a career in film and television, she moved to Hollywood and landed her first film role in "Alligator" penned by John Sayles.  She went on to have starring roles in the prime-time sitcoms "Brothers", "Shaky Ground", "Thunder Alley", "The Gregory Hines Show" and "Get a Life".  She also became the fourth and final actress to play Beth Logan on the CBS daytime soap opera "The Bold and the Beautiful".

Brown Publishing Company: Brown Publishing Company was a privately owned Cincinnati, Ohio newspaper business started by Congressman Clarence J. Brown in 1920.  It ended 90 years of operations in August/September 2010 with its bankruptcy and sale of assets to a new company formed by its creditors and called Ohio Community Media Inc.  The company was previously a family-owned business; it published 18 daily newspapers, 27 weekly newspapers, and 26 free weeklies.  The former CEO was Brown's grandson, Roy Brown.  The chairman of the board was Roy's brother Clancy Brown, who is also an actor.

Shoot to Kill (1988 film): Shoot to Kill (known outside North America as Deadly Pursuit) is a 1988 American adventure crime thriller film directed by Roger Spottiswoode and starring Sidney Poitier, Tom Berenger, Clancy Brown, Andrew Robinson and Kirstie Alley.

Carmen Finestra: Carmen Finestra (born 1947) is an American producer and TV writer who currently is partnered with Matt Williams and David McFadzean in Wind Dancer Productions, a firm which Finestra also co-owns and co-founded with actor Tim Allen.  For Wind Dancer, Finestra has produced or executive produced "Where the Heart Is", "Firelight", "Soul Man", "Thunder Alley" and his company's best known series, "Home Improvement", which starred Allen as a feisty home-improvement host, and in turn based on Allen's stand-up comedy routines.

Clancy Brown: Clarence J. "Clancy" Brown III (born January 5, 1959) is an American actor and voice actor known for his roles

Mr. Krabs: Mr. Krabs is a fictional character in the American animated comedy television series "SpongeBob SquarePants".  He is voiced by actor Clancy Brown and first appeared in the series' pilot episode "Help Wanted" on May 1, 1999.  The character was created and designed by marine biologist and animator Stephen Hillenburg.

Question: What year was the Thunder Alley actor Clancy Brown born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the actor."
    },
    "film_role_context": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film the actor was in."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "film_title",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "birth_year",
    "film_role_context"
  ],
  "additionalProperties": false
}
