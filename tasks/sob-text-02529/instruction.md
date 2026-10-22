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
Joe Turner's Come and Gone: Joe Turner's Come and Gone is a play by American playwright August Wilson.  It is the second installment of his decade-by-decade chronicle of the African-American experience, "The Pittsburgh Cycle".  The play was first staged 1984 at the Eugene O'Neill Theater Center in Waterford, Connecticut and opened on Broadway on 27 March 1988 at the Ethel Barrymore Theatre—running for 105 performances.  Directed by Lloyd Richards, the cast included Delroy Lindo as Herald Loomis and television and movie star Angela Bassett, as Loomis's wife, Martha.

Mykelti Williamson: Michael T. "Mykelti" Williamson (born March 4, 1960) is an American actor best known for his roles in the films "Forrest Gump" and "Con Air", and the television shows "Boomtown", "24", and "Justified".  In 2016, he portrayed Gabriel Maxson in Denzel Washington's acclaimed film adaptation of August Wilson's play "Fences", reprising his role from the 2010 Broadway revival.

The Piano Lesson: The Piano Lesson is a 1990 play by American playwright August Wilson.  It is the fourth play in Wilson's "The Pittsburgh Cycle".  Wilson began writing this play by playing with the various answers regarding the possibility of "acquir[ing] a sense of self-worth by denying one's past".  "The Piano Lesson" received the 1990 Pulitzer Prize for Drama.

Gem of the Ocean: Gem of the Ocean is a play by American playwright August Wilson.  It is the first installment of his decade-by-decade, ten-play chronicle, "The Pittsburgh Cycle", dramatizing the African-American experience in the twentieth century.

August Wilson House: The August Wilson House at 1727 Bedford Avenue in the Crawford-Roberts neighborhood of Pittsburgh, Pennsylvania, United States, was built in the 1840s and was the childhood home for his first 13 years of playwright August Wilson (1945–2005).  The house was placed on the List of City of Pittsburgh historic designations on February 26, 2008, and it was listed on the National Register of Historic Places on April 30, 2013.

Fences (play): Fences is a 1985 play by American playwright August Wilson.  Set in the 1950s, it is the sixth in Wilson's ten-part "Pittsburgh Cycle".  Like all of the "Pittsburgh" plays, "Fences" explores the evolving African-American experience and examines race relations, among other themes.  The play won the 1987 Pulitzer Prize for Drama and the 1987 Tony Award for Best Play.  The play was first developed at the Eugene O'Neill Theater Center's 1983 National Playwrights Conference and premiered at the Yale Repertory Theatre in 1985.

Fences (film): Fences is a 2016 American period drama film directed by and starring Denzel Washington and written by August Wilson, based on his Pulitzer Prize-winning play of the same name (Wilson died in 2005, but completed a screenplay before his death).  In addition to Washington, the film also stars Viola Davis, Stephen Henderson, Jovan Adepo, Russell Hornsby, Mykelti Williamson and Saniyya Sidney.

Two Trains Running: Two Trains Running is a play by American playwright August Wilson, the seventh in his ten-part series "The Pittsburgh Cycle".  The play premiered on Broadway in 1992 and was a finalist for the Pulitzer Prize for Drama.

King Hedley II: King Hedley II is a play by American playwright August Wilson, the ninth in his ten-part series, "The Pittsburgh Cycle".  The play ran on Broadway in 2001 and was revived Off-Broadway in 2007.

Seven Guitars: Seven Guitars is a 1995 play by American playwright August Wilson.  It focuses on seven African-American characters in the year 1948.  The play begins and ends after the funeral of one of the main characters, showing events leading to the funeral in flashbacks.  "Seven Guitars" represents the 1940s entry in Wilson's "Pittsburgh Cycle", a decade-by-decade anthology of African-American life in Pittsburgh, Pennsylvania during the twentieth century; Wilson would revisit the stories of some of these characters in "King Hedley II", set in the 1980s.

Question: Mykelti Williamson is an American actor who portrayed Gabriel Maxson in what film adaption of the1985 play by American playwright August Wilson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "role_played": {
      "type": "string",
      "description": "The name of the character portrayed by the actor."
    },
    "film_adaptation": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film adaptation."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film adaptation."
        },
        "director": {
          "type": "string",
          "description": "The director of the film adaptation."
        }
      },
      "required": [
        "title",
        "release_year",
        "director"
      ],
      "additionalProperties": false
    },
    "original_play": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the original play."
        },
        "premiere_year": {
          "type": "integer",
          "description": "The premiere year of the original play."
        },
        "playwright": {
          "type": "string",
          "description": "The playwright of the original play."
        }
      },
      "required": [
        "title",
        "premiere_year",
        "playwright"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "role_played",
    "film_adaptation",
    "original_play"
  ],
  "additionalProperties": false
}
