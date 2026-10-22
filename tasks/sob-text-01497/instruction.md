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
Mario Puzo: Mario Gianluigi Puzo ( ; ] ; October 15, 1920 – July 2, 1999) was an American author, screenwriter and journalist of Italian descent.  He is known for his crime novels about the Mafia, most notably "The Godfather" (1969), which he later co-adapted into a three-part film saga directed by Francis Ford Coppola.  He received the Academy Award for Best Adapted Screenplay for the first film in 1972 and "Part II" in 1974.  Puzo also wrote the original screenplay for the 1978 "Superman" film.  His last novel, "The Family", was released posthumously in 2001.

The Family (Puzo novel): The Family is a 2001 novel written by Mario Puzo.  The novel is about Pope Alexander VI and his family.  Puzo spent over twenty years working on the book off and on, while he wrote others.  The novel was finished by his longtime girlfriend, Carol Gino.  "The Family" is effectively his last novel.

Scuba Duba: Scuba Duba is a 1967 comedy play from Bruce Jay Friedman which was a success off-Broadway starring Jerry Orbach, Judd Hirsch, Conrad Bain and Cleavon Little in a production that ran for 692 performances.

Bruce Jay Friedman: Bruce Jay Friedman is an American novelist, screenwriter, playwright, and actor.

Doctor Detroit: Doctor Detroit is a 1983 American comedy film directed by Michael Pressman with writing by Bruce Jay Friedman, Carl Gottlieb, and Robert Boris.  The film stars Dan Aykroyd, Howard Hesseman, Lynn Whitfield, Fran Drescher, and Donna Dixon, with a special appearance by James Brown.

Fools Die: Fools Die is a 1978 novel by Italian American author Mario Puzo.  Played out in the worlds of gambling, publishing and the film industry, Merlyn and his brother Artie obey their own code of honor in the ferment of contemporary America, where law and organized crime are one and the same.  Set in New York, Hollywood, and Las Vegas, Mario Puzo considered "Fools Die" to be his personal favorite.  The paperback rights to the book were sold in 1978 by the publisher, G. P. Putnam's Sons, to New American Library for a then record $2.55 million.

Steambath (play): Steambath is the second play by American author Bruce Jay Friedman.  It was first performed Off-Broadway at the Truck and Warehouse Theater where it opened on June 30, 1970, closing on October 18, 1970 after 128 performances.

Swank: Swank is an adult or pornographic magazine published in the United States.  The first incarnation was launched by Victor Fox of Fox Comics in 1941 (and again in 1945) as a men's lifestyle and pin-up magazine in the style of "Esquire".  Around 1954–1955, it was relaunched by Martin Goodman, the founder of Marvel Comics, and ran spicy adventure or suspense fiction by the likes of Ian Fleming, Graham Greene, Norman Mailer and Arthur C. Clarke.  Humorist Bruce Jay Friedman was an editor in the late 1950s.

The Lonely Guy: The Lonely Guy is a 1984 American romantic comedy film directed by Arthur Hiller and starring Steve Martin.  The screenplay is credited to Ed.  Weinberger and Stan Daniels (of "Taxi") as well as Neil Simon (for "adaptation"), and is based on the 1978 book "The Lonely Guy's Book of Life" by Bruce Jay Friedman.

Stir Crazy (film): Stir Crazy is a 1980 American comedy film directed by Sidney Poitier, produced by Hannah Weinstein and written by Bruce Jay Friedman.  The film stars Gene Wilder and Richard Pryor as down-on-their-luck friends who are given 125-year prison sentences after being framed for a bank robbery.  While in prison they befriend other prison inmates.  The film reunited Wilder and Pryor who had appeared previously in the 1976 comedy thriller film "Silver Streak".  The film was released in the United States on December 12, 1980.

Question: In between Mario Puzo and Bruce Jay Friedman who's last novel is "The Family"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The full name of the author."
    },
    "novel_title": {
      "type": "string",
      "description": "The title of the novel in question."
    },
    "is_last_novel": {
      "type": "boolean",
      "description": "Indicates if the novel is the author's last published novel."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the novel was released."
    }
  },
  "required": [
    "author_name",
    "novel_title",
    "is_last_novel",
    "release_year"
  ],
  "additionalProperties": false
}
