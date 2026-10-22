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
Jerry Lewis: Jerry Lewis (born either Jerome Levitch or Joseph Levitch, depending on the source; March 16, 1926 – August 20, 2017) was an American comedian, actor, singer, producer, director, screenwriter, and humanitarian.

Eddie Murphy: Edward Regan Murphy (born April 3, 1961) is an American comedian, actor, writer, singer, and producer.  Murphy was a regular cast member on "Saturday Night Live" from 1980 to 1984.  He has worked as a stand-up comedian and was ranked #10 on Comedy Central's list of the 100 Greatest Stand-ups of All Time.

Jack Burns: John Francis Burns (born November 15, 1933) is an American comedian, actor, voice actor, writer and producer.  During the 1960's, he was part of two notable stand-up comedy partnerships, first with George Carlin and later Avery Schreiber.  By the 1970s, he had transitioned to working behind the camera, as a writer and producer on such notable comedy series as "The Muppet Show" and "Hee Haw".  He also had many notable roles as a voice actor.

Steve Oedekerk: Steven Brent Oedekerk (born November 27, 1961) is an American comedian, director, editor, producer, screenwriter and actor.  Oedekerk is best known for his collaborations with actor Jim Carrey and director Tom Shadyac (particularly the "Ace Ventura" franchise), his series of "Thumbmation" shorts and his film "" (2002).

Don Barnhart: Don Barnhart Jr (born July 2, 1963) is an American comedian, actor, writer and filmmaker who stars in his own comedy show in Las Vegas author, actor, filmmaker and hypnotist.  He has directed and produced, China Dolls, The Freedom of Speech Comedy Series, The Ice House Anniversary Show, The DeEvolution of Man and more.  He also appeared in the indie film Vicious Lips.

Who's Minding the Store?: Who's Minding the Store?  is a comedy film directed by Frank Tashlin and starring Jerry Lewis.  It was released on November 28, 1963, by Paramount Pictures.

Allen Covert: Allen Stephen Covert (born October 13, 1964) is an American comedian, actor, writer, and producer.  Best known for his starring role in the 2006 comedy film "Grandma's Boy", he is also a frequent collaborator with actor and friend Adam Sandler with prominent roles in such films as "Happy Gilmore" (1996), "The Wedding Singer" (1997), "Big Daddy" (1999), "Little Nicky" (2000), "Mr. Deeds" (2002), "Anger Management" (2003), "50 First Dates" (2004), and the Happy Madison Productions film "Strange Wilderness" (2008).

Frank Ferrante: Frank Vincent Ferrante (born April 26, 1963) is an American stage actor, comedian and director known for his stage portrayals of legendary American comedian Groucho Marx in the Arthur Marx/Robert Fisher play "" and in "An Evening With Groucho", which tours internationally.

Charley Chase: Charley Chase (born Charles Joseph Parrott, October 20, 1893 – June 20, 1940) was an American comedian, actor, screenwriter and film director, best known for his work in Hal Roach short film comedies.  He was the older brother of comedian/director James Parrott.

Curly Howard: Jerome Lester Horwitz (October 22, 1903 – January 18, 1952), better known by his stage name Curly Howard, was an American comedian and vaudevillian actor.  He was best known as a member of the American farce comedy team the Three Stooges, which also featured his older brothers Moe and Shemp Howard and actor Larry Fine.  Curly was generally considered the most popular and recognizable of the Stooges.  He was well known for his high-pitched voice and vocal expressions ("nyuk-nyuk-nyuk!" , "woob-woob-woob!" , "soitenly!"  (certainly), and barking like a dog) as well as his physical comedy (e.g., falling on ground and pivoting on his shoulder as he "walked" in circular motion), improvisations, and athleticism.  An untrained actor, Curly borrowed (and significantly exaggerated) the "woob woob" from "nervous" and soft-spoken comedian Hugh Herbert.  Curly's unique version of "woob-woob-woob" was firmly established by the time of the Stooges' second Columbia film, "Punch Drunks" (1934).

Question: A comedy film that was released in 1963, stars an American comedian, actor, singer, producer, director, screenwriter, and humanitarian, and was directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the comedy film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "starring_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the main actor in the film."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions held by the starring actor."
        }
      },
      "required": [
        "name",
        "professions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "starring_actor"
  ],
  "additionalProperties": false
}
