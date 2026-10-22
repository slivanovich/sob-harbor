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
The Tic Code: The Tic Code (also known as Lessons in the Tic Code) is a drama film directed by Gary Winick and written by Polly Draper.  It tells of a single mother, the relationship she forms with a jazz musician who has Tourette syndrome, and her young son—a jazz piano prodigy—also with the disorder.  The musician and the boy form a friendship, and the film is loosely based upon the experiences of Draper's jazz musician husband Michael Wolff, who provided the film's score.  Draper, known for her role in "Thirtysomething", portrays the mother; Gregory Hines plays the musician; and Christopher George Marquette stars as the young boy.

Curfew (1989 film): Curfew is an American action/horror 1989 film directed by Gary Winick.

Sweet Home Alabama (film): Sweet Home Alabama is a 2002 American romantic comedy film directed by Andy Tennant, starring Reese Witherspoon, Josh Lucas, Patrick Dempsey and Candice Bergen.  The film was released by Touchstone Pictures on September 27, 2002.

Tadpole (film): Tadpole is a 2002 American romantic comedy film directed by Gary Winick and written by Heather McGowan and Niels Mueller.  It stars Sigourney Weaver, Bebe Neuwirth, Aaron Stanford, John Ritter, Robert Iler, and Kate Mara.

The Sweetest Thing: The Sweetest Thing is a 2002 American romantic comedy film directed by Roger Kumble and written by Nancy Pimental, who based the characters on herself and friend Kate Walsh.  It stars Cameron Diaz, Christina Applegate and Selma Blair.

Bebe Neuwirth: Beatrice "Bebe" Neuwirth ( ; born December 31, 1958) is an American actress, singer and dancer.  On television, she is known for her portrayal of Dr. Lilith Sternin, Dr. Frasier Crane's wife (later former wife), on both the TV sitcom "Cheers" (in a starring role), and its spin-off "Frasier" (in a recurring guest role).  The role won her two Emmy Awards.  On stage, she is known for her Tony Award winning roles of Nickie in the revival of "Sweet Charity" (1986), and Velma Kelly in the revival of "Chicago" (1996).  Other Broadway musical roles include Morticia Addams in "The Addams Family" (2010).  Since 2014, she has starred as Nadine Tolliver in the CBS drama "Madam Secretary".

Sam the Man: Sam the Man is a 2000 American film directed by Gary Winick and starring Fisher Stevens.

Letters to Juliet: Letters to Juliet is a 2010 American romantic drama film starring Amanda Seyfried, Christopher Egan, Vanessa Redgrave, Gael García Bernal and Franco Nero.  This was the final film of director Gary Winick.  The film was released theatrically in North America and other countries on May 14, 2010.  The idea for the film was inspired by the 2006 non-fiction book "Letters to Juliet", by Lise Friedman and Ceil Friedman, which chronicles the phenomenon of letter-writing to Shakespeare's most famous romantic heroine.

13 Going on 30: 13 Going on 30 (released as Suddenly 30 in some countries) is a 2004 American romantic comedy fantasy film written by Josh Goldsmith and Cathy Yuspa and directed by Gary Winick.  Starring Jennifer Garner, the film was produced by Revolution Studios for Columbia Pictures, and was released on April 23, 2004.  It follows a 13-year-old girl who dreams of being popular.  During her birthday party, she is humiliated by classmates and wishes that she was thirty years old.  When she eventually does emerge, she finds herself five days shy of her 30th birthday, uncertain to how she got there.

Bride Wars: Bride Wars is a 2009 American romantic comedy film directed by Gary Winick and written by Greg DePaul, June Diane Raphael, and Casey Wilson.  The film stars Kate Hudson, Anne Hathaway, Candice Bergen, Bryan Greenberg, Chris Pratt, Steve Howey, and Kristen Johnston.

Question: Tadpole is a 2002 American romantic comedy film directed by Gary Winick, it stars which American actress, singer and dancer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "starring_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the actress."
        },
        "profession": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The professions of the actress."
        }
      },
      "required": [
        "name",
        "profession"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "film_year",
    "director_name",
    "starring_actress"
  ],
  "additionalProperties": false
}
