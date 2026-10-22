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
Anthony Clarvoe: Anthony Clarvoe is an American playwright born in 1958.

Edward Locke: Edward Locke (1869–1945) was an American playwright born in England.

London Suite (play): London Suite is a play by Neil Simon, consisting of four one-act plays.  "London Suite" also was a 1996 television movie.  It is in a similar style to Simon's earlier works "Plaza Suite" and "California Suite".

Jen Silverman: Jen Silverman is an American playwright born in the United States.  She grew up living and traveling in Scandinavia, Asia, and Europe as well as the United States.  She completed a BA in comparative literature at Brown University, a MFA in playwriting at the University of Iowa, and also studied at Juilliard.

Vinegar Tom: Vinegar Tom is the title of a 1976 play by the British playwright Caryl Churchill.  The play examines gender and power relationships through the lens of 17th century witchcraft trials in England.  The script employs features of the epic theater associated with German playwright Bertolt Brecht, particularly the realistic use of songs.  The play's title comes from the name of one character's pet cat, supposed to be her familiar spirit, likely inspired by the supposed imp of one Elizabeth Clarke, a woman tried and executed for witchcraft in Essex in 1645.  The play was inspired by the Women's Rights Act in 1970 and explored the thought that women were treated unequally to men in England, both at the time in which the play takes place, and the time in which the play was written.

California Suite: California Suite is a 1976 play by Neil Simon.  Similar in structure to his earlier "Plaza Suite", the comedy is composed of four playlets set in Suite 203-04, which consists of a living room and an adjoining bedroom with an ensuite bath, in The Beverly Hills Hotel.

The Vietnamization of New Jersey: The Vietnamization of New Jersey (subtitled "A American Tragedy" ["sic"] ) is a 1976 play written by American playwright Christopher Durang.

Eden (Steve Carter play): Eden is a 1976 play by American playwright Steve Carter.  Set in the 1920s, it is the first of Carter's Caribbean trilogy.  "Eden" explores intra-racial conflicts between recent immigrants from the Caribbean and the African-American population.  The West Coast premiere of this critically acclaimed play received five Los Angeles Drama Critics Circle Awards.

California Suite (film): California Suite is a 1978 American comedy film directed by Herbert Ross.  The screenplay by Neil Simon is based on his play of the same name.  Similar to his earlier "Plaza Suite", the film focuses on the dilemmas of guests staying in a suite in a luxury hotel.  Maggie Smith won the Academy Award for Best Supporting Actress for her performance in the film.

Neil Simon: Marvin Neil Simon (born July 4, 1927) is an American playwright, screenwriter and author.  He has written more than thirty plays and nearly the same number of movie screenplays, mostly adaptations of his plays.  He has received more combined Oscar and Tony nominations than any other writer.

Question: California Suite is a 1976 play by an american playwright born in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "play_title": {
      "type": "string",
      "description": "The title of the play."
    },
    "play_year": {
      "type": "integer",
      "description": "The year the play was released."
    },
    "playwright": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the playwright."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the playwright."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the playwright."
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "integer",
      "description": "The birth year of the playwright who wrote the specified play."
    }
  },
  "required": [
    "play_title",
    "play_year",
    "playwright",
    "answer"
  ],
  "additionalProperties": false
}
