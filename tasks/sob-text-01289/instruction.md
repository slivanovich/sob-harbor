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
Victor Fleming: Victor Lonzo Fleming (February 23, 1889 – January 6, 1949) was an American film director, cinematographer, and producer.  His most popular films were "The Wizard of Oz" (1939), and "Gone with the Wind" (1939), for which he won an Academy Award for Best Director.  Fleming has two films listed in the top 10 of the American Film Institute's 2007 AFI's 100 Years...100 Movies list.

Jim the Penman (1921 film): Jim the Penman is a 1921 American silent crime drama film produced by Whitman Bennett and distributed through Associated First National, later just First National Pictures.  It is based on a well known play, "Jim the Penman" by Charles Lawrence Young about a forger in Victorian Britain.  The film stars Lionel Barrymore and was directed by Kenneth Webb, the duo having worked on "The Great Adventure" previously.  "Jim the Penman" is preserved though incomplete (reel 5 missing) at the Library of Congress.

The Daring Years: The Daring Years is 1923 American silent melodrama, directed by Kenneth Webb and produced by Daniel Carson Goodman.  The film starred Mildred Harris, Clara Bow, Charles Emmett Mack, and Tyrone Power, Sr..  The film is now considered lost.

Salvation Nell (1921 film): Salvation Nell is a 1921 American silent drama film produced by Whitman Bennett and distributed by Associated First National Pictures, later First National Pictures.  It was directed by Kenneth Webb and stars Pauline Starke.  The film is based on a successful 1908 Broadway play that starred Minnie Maddern Fiske.

The Devil's Garden: The Devil's Garden is a lost 1920 American silent drama film produced by Whitman Bennett, directed by Kenneth Webb, and released through First National Exhibitor's Circuit, which was later known as First National Pictures.  The film starred Lionel Barrymore, May McAvoy, and Barrymore's first wife Doris Rankin.  It is based on a novel, "The Devil's Garden" by William Babington Maxwell, and was the first film for Whitman Bennett Productions.

Ameer Webb: Ameer Kenneth Webb (born March 19, 1991) is an American sprinter, who specializes in the 200 meters.

Just Suppose: Just Suppose is a surviving 1926 film produced by and starring Richard Barthelmess with distribution through First National Pictures.  Kenneth Webb directed Barthelmess and young Lois Moran star.  The film is based on a 1920 Broadway play, "Just Suppose", by Albert E. Thomas.

The Great Adventure (1921 film): The Great Adventure is a 1921 American silent romantic comedy film produced by Whitman Bennett and distributed by First National Pictures, then called Associated First National.  The film was directed by Kenneth Webb and starred Lionel Barrymore.  Fredric March made his screen debut in this film.  The film is based upon the novel "Buried Alive" by Arnold Bennett.  It was remade in 1933 as "His Double Life" starring Lillian Gish.  "The Great Adventure" is a surviving feature film held by the Library of Congress.

Kenneth Webb: Kenneth S. Webb (October 16, 1892 in New York City – March 23, 1966 in Hollywood, California) was an American film director, screenwriter, and composer noted for directing a number of films in the early age of the American film industry.  He helped write the "Gay Divorce" along with Samuel Hoffenstein.

The Master Mind (1920 film): The Master Mind (also known as Sinners Three) is a lost 1920 American silent crime drama film produced by Whitman Bennett and released by Associated First National Pictures, later just First National Pictures).  Kenneth Webb directed and Lionel Barrymore stars.  It is based on a 1913 play, "The Master Mind", by playwright Daniel David Cohen also known as Daniel D. Carter.

Question: Who was born first, Kenneth Webb or Victor Fleming?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the first person."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the second person."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        }
      },
      "required": [
        "name",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "earliest_born_person_name": {
      "type": "string",
      "description": "The name of the person who was born first."
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement comparing the birth years of the two individuals."
    }
  },
  "required": [
    "person_a",
    "person_b",
    "earliest_born_person_name",
    "comparison_result"
  ],
  "additionalProperties": false
}
