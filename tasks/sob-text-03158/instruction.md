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
Jekyll and Hyde... Together Again: Jekyll and Hyde...Together Again is a 1982 comedy based on the novella "Strange Case of Dr. Jekyll and Mr. Hyde" by Robert Louis Stevenson and stars Mark Blankfield, Bess Armstrong, Tim Thomerson, Krista Errickson, Cassandra Peterson and Michael McGuire.

Constantine Maroulis: Constantine James Maroulis ( ; born September 17, 1975) is a Greek-American actor and rock singer from Wyckoff, New Jersey.  He was the sixth-place finalist on the fourth season of the reality television series "American Idol", and received a nomination for the Tony Award for Best Performance by a Leading Actor in a Musical for his role in "Rock of Ages".  He starred in the title role in "Jekyll and Hyde" on Broadway, for which he received a Drama League Award Nomination for a Distinguished Performance Award.

Steve Baker (illusionist): Steve "Mr. Escape" Baker (July 26, 1938 – September 17, 2017) is a comedian, magician and is most well known as an escape artist.  During his career from 1967 through the early 1990s Baker appeared on "Dick Clark's LIVE Wednesday", "Games People Play", and was a star on an HBO special along with Tony Curtis and special guest star Dorothy Dietrich, called "The World's Greatest Escapes", and several times on "That's Incredible! ".  Baker died on September 17, 2017 at the age of 79.

Marta Ribera: Marta Ribera is a Spanish theatrical actress star born in 1971.  She is perhaps best known for her roles in the Frank Wildhorn musical Jekyll & Hyde (musical) in the starring role of Lucy Harris and her most recent role as The Lady of the Lake in Monty Python's Spamalot.  She has also appeared as Sally Bowles in Cabaret (musical), amongst other roles.

Chatt G. Wright: Chatt G. Wright (born September 17, 1941) is a former president of Hawaii Pacific University.  He was one of the longest serving presidents of a private university.  He joined what was then Hawaii Pacific College on September 17, 1972 as the Dean of Business, then became President of the college on September 17, 1976.  He retired in June 2011.

Niamh Walsh: Niamh Walsh (born 17 April 1988) is an Irish actress best known for her role as Cara Martinez the in BBC One medical drama "Holby City".  Walsh has also appeared in "Casualty" and "Jekyll & Hyde".  She also stars in the Sky 1 period drama "Jamestown" as Verity Rutter née Bridges.

Brad Oscar: Brad Oscar (born September 22, 1964) is an American musical theatre actor known for his Broadway performances in musicals such as "The Producers" and "Jekyll and Hyde".  He earned two Tony Award nominations; one for "The Producers" as Franz Liebkind, and one for "Something Rotten! " as Nostradamus.

Zachary Bennett: Zachary Bennett (born February 17, 1980) is a Canadian actor and musician in Toronto, Ontario, who is best known for playing Felix King in "Road to Avonlea".  He also co-starred in the 2006 TV film "Jekyll + Hyde".

Mark Blankfield: Mark Blankfield (born May 8, 1950) is an American comedic actor from Pasadena, Texas, who is perhaps best known as a regular cast member of the television variety series "Fridays".  Other work includes roles in "Jekyll and Hyde...Together Again", "The Incredible Shrinking Woman", "", "", and "The Jerk, Too", a TV-movie sequel to "The Jerk".

Cassandra Peterson: Cassandra Peterson (born September 17, 1951) is an American actress best known for her portrayal of the horror hostess character Elvira, Mistress of the Dark.  She gained fame on Los Angeles television station KHJ-TV wearing a revealing, black, gothic, cleavage-enhancing gown as host of "Elvira's Movie Macabre", a weekly horror movie presentation.  Her wickedly vampish appearance is offset by her comical character, quirky and quick-witted personality, and Valley girl-type speech.

Question: Which star of Jekyll and Hyde... Together Again was born on September 17, 1951 ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the actor in YYYY-MM-DD format."
    },
    "role_description": {
      "type": "string",
      "description": "A brief description of the actor's known role or persona."
    }
  },
  "required": [
    "movie_title",
    "actor_name",
    "birth_date",
    "role_description"
  ],
  "additionalProperties": false
}
