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
Merrily We Roll Along (musical): Merrily We Roll Along is a musical with a book by George Furth and lyrics and music by Stephen Sondheim.  It is based on the 1934 play of the same name by George S. Kaufman and Moss Hart.

Thomas Doherty (actor): Thomas Doherty (born April 21, 1995) is a Scottish actor, best known for his roles as Harry Hook in Disney's "Descendants 2" and as Sean in the British musical drama sitcom, "The Lodge".  In 2017, it was announced that Doherty would play the role of Zander in Michael Damian's film, High Strung: Free Dance.

Adam Stennett: Adam Stennett (born 1972 in Kotzebue, Alaska) is an internationally exhibited American painter based in Brooklyn, New York best known for his hyperrealist works.  He was raised in Oregon and received his Bachelor of Arts degree in from Willamette University in Salem.  For several years he was the assistant to the painter Damian Loeb.  His work has been the subject of three solo exhibitions at the gallery 31Grand in 2004, 2005 and 2007.  In 2013 his outdoor installation transferred indoors aka his "Survival Shack" was the basis for an exhibition at the Glenn Horowitz Bookseller space in East Hampton, New York and received widespread press coverage.

Terry Finn: Teresa Jo Ann Bernadette "Terry" Finn (born August 6, 1955) is an American actress best known for creating the role of Gussie Carnegie in the original Broadway cast of the Stephen Sondheim/Hal Prince/George Furth musical comedy "Merrily We Roll Along" and its Original Cast Album.

Ann Morrison: Ann Morrison (born April 9, 1956) is an American actress, best known for her Broadway debut as Mary Flynn in the Stephen Sondheim/George Furth musical, "Merrily We Roll Along" directed by Harold Prince for which she won the 1982 Theatre World Award.  Off-Broadway she played Lizzie in the highly acclaimed Polly Pen/Peggy Harmon musical "Goblin Market" which garnered her a 1986 Drama Desk Award Nomination as Best Actress in a Musical and a Best Plays Theatrical Yearbook Citation as Best Actress in a Musical.

Company (musical): Company is a 1970 musical comedy with music and lyrics by Stephen Sondheim and book by George Furth.  The original production was nominated for a record-setting fourteen Tony Awards and won six.

Rob Ellis (producer): Robert Damian Ellis (born 13 February 1962, in Bristol, England) is a producer, arranger, instrumentalist and composer.  He is best known for his work with PJ Harvey, with whom he has been most closely associated as producer, arranger and musician since 1990.

Paul Collins (American writer): Paul Collins (born January 12, 1969) is an American writer, editor and Chair of English at Portland State University, in Portland, Oregon.  He is best known for his work with McSweeney's and "The Believer", as editor of the Collins Library imprint for McSweeney's Books, and for his appearances on National Public Radio's "Weekend Edition Saturday" with Scott Simon.  His own books deal primarily with quirky forgotten figures from history, sometimes interwoven with memoir.  Damian Kulash of the band OK Go has stated that the chapter in Collins' book "Banvard's Folly" about Augustus Pleasonton's patent on blue light led to them naming their third album "Of the Blue Colour of the Sky".

The Act (musical): The Act is a musical with a book by George Furth, lyrics by Fred Ebb, and music by John Kander.

Damian Humbley: Damian Humbley (born 13 February 1979) is an Australian singer and actor.  Born in Queensland, he trained at the Western Australian Academy of Performing Arts.  He is best known for his work on the stage in the UK, notable credits including acclaimed productions of Stephen Sondheim musicals such as "Company" at the Sheffield Crucible and "Merrily We Roll Along" at the Menier Chocolate Factory.

Question: Damian Humbley is best known for his work on what musical with a book writted by George Furth?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musical_title": {
      "type": "string",
      "description": "The title of the musical."
    },
    "book_writer": {
      "type": "string",
      "description": "The writer of the musical's book."
    },
    "composer": {
      "type": "string",
      "description": "The composer of the musical's music."
    },
    "lyricist": {
      "type": "string",
      "description": "The lyricist of the musical."
    },
    "actor_known_for_work": {
      "type": "string",
      "description": "The actor known for their work in this musical."
    }
  },
  "required": [
    "musical_title",
    "book_writer",
    "composer",
    "lyricist",
    "actor_known_for_work"
  ],
  "additionalProperties": false
}
