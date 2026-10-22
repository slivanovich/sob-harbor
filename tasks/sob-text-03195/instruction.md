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
Richard Pryor: Live in Concert: Richard Pryor: Live in Concert is a 1979 American stand-up comedy film starring Richard Pryor and directed by Jeff Margolis.  Pryor's performance earned him a 5th place nomination for the National Society of Film Critics Award for Best Actor.

Whose Line Is It Anyway? Australia: Whose Line is it Anyway?  Australia (also known as Whose Line?  and Whose Line?  Oz) is a 10-part Australian improvisational comedy show, based on the British show of the same name, hosted by Tommy Little on Foxtel network's The Comedy Channel, premiering on 27 November 2016.

Brewster's Millions (1985 film): Brewster's Millions is a 1985 comedy film directed by Walter Hill and starring Richard Pryor and John Candy.  The screenplay by Herschel Weingrod and Timothy Harris was based on the 1902 novel of the same name by George Barr McCutcheon.  It is the seventh film based on the story.

Richard Pryor: Live on the Sunset Strip (film): Richard Pryor: Live on the Sunset Strip is a 1982 American stand-up comedy film directed by Joe Layton and written by and starring Richard Pryor.  The film is based on Pryor's .  Released in 1982, the film was the most financially lucrative of the comedian's concert films.  The material includes Pryor's frank discussion of his drug addiction and of the night that he caught on fire while freebasing cocaine in 1980.

Christopher Smith (performer): Christopher Robin Smith (born 1959) is an American actor, director and improviser, best known for his improv workshops and his handful of appearances on "Whose Line Is It Anyway? ".

Mark Cohen (comedian): Mark Cohen is an American comedian best known for hosting Comedy Central's "Make Me Laugh" in 1998.  Cohen also appeared in two episodes of the British version of "Whose Line Is It Anyway? " and has had numerous guest roles on American sitcoms such as "The Sarah Silverman Program" and "Louie", and appeared in the 1997 independent comedy film "Who's the Caboose? " starring Sarah Silverman.

Archie Hahn (actor): Archie Hahn (sometimes credited as Archie Hahn III, born November 1, 1941) is an American character actor and improviser best known for his appearances on the British version of "Whose Line is it Anyway? " and the 1988 movie "".  He has also appeared in "Phantom of the Paradise" (1974), "Pray TV" (1980), "This Is Spinal Tap" (1984), "Brewster's Millions" (1985), "The Brady Bunch Movie" (1995), and many Joe Dante films including "Amazon Women on the Moon" (1987), "" (1990) and "Small Soldiers" (1998).  In two of his final appearances on "Whose Line is it Anyway?" , Hahn unexpectedly brought props to use as he improvised, first castanets and then a pair of false teeth.

Richard Pryor: Here and Now: Richard Pryor: Here and Now is a 1983 stand-up comedy film released by Columbia Pictures, starring, written and directed by Richard Pryor.

Richard Pryor: Richard Franklin Lennox Thomas Pryor (December 1, 1940 – December 10, 2005) was an American comedian, actor, and social critic.  Pryor was known for uncompromising examinations of racism and topical contemporary issues, which employed colorful vulgarities and profanity, as well as racial epithets.  He reached a broad audience with his trenchant observations and storytelling style.  He is widely regarded as one of the most important and influential stand-up comedians of all time: Jerry Seinfeld called Pryor "The Picasso of our profession" and Bob Newhart heralded Pryor as "the seminal comedian of the last 50 years".  Dave Chappelle said of Pryor, "You know those, like, evolution charts of man?  He was the dude walking upright.  Richard was the highest evolution of comedy."  This legacy can be attributed, in part, to the unusual degree of intimacy Pryor brought to bear on his comedy.  As Bill Cosby reportedly once said, "Richard Pryor drew the line between comedy and tragedy as thin as one could possibly paint it."

Which Way Is Up?: Which Way is Up?  is a 1977 American comedy film starring Richard Pryor and directed by Michael Schultz.  It is a remake of the 1972 Italian comedy film "The Seduction of Mimi" starring Giancarlo Giannini and directed by Lina Wertmüller.  Richard Pryor plays three roles: an orange picker who has two women at the same time, the orange picker's father, and a Reverend who gets the orange picker's wife pregnant.

Question: Archie Hahn, is an American character actor and improviser best known for his appearances on the British version of "Whose Line is it Anyway?", he has also appeared in Brewster's Millions, released in which year, a comedy film directed by Walter Hill and starring Richard Pryor and John Candy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "starring_actors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of the main actors starring in the film."
        }
      },
      "required": [
        "director",
        "genre",
        "starring_actors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "film_details"
  ],
  "additionalProperties": false
}
