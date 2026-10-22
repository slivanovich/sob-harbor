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
Ride 'Em Cowboy: Ride 'Em Cowboy is a 1942 film starring the comedy team of Abbott and Costello.  The supporting cast features Dick Foran, Anne Gwynne, Johnny Mack Brown, Ella Fitzgerald, Samuel S. Hinds, Douglas Dumbrille and Morris Ankrum, and the movie was directed by Arthur Lubin.

Vanilla and Chocolate: Vanilla and Chocolate (Italian: "Vaniglia e cioccolato" ) is a 2004 Italian romance film directed by Ciro Ippolito.

Arthur Lubin: Arthur Lubin (July 25, 1898 – May 12, 1995) was an American film director and producer who directed several "Abbott & Costello" films, "Phantom of the Opera" (1943), the "Francis the Talking Mule" series and created the talking-horse TV series "Mister Ed".  A prominent director for Universal Pictures in the 1940s and 1950s, he is perhaps best known today as the man who gave Clint Eastwood his first contract in film.

Buck Privates: Buck Privates is a 1941 musical military comedy film that turned Bud Abbott and Lou Costello into bona fide movie stars.  It was the first service comedy based on the peacetime draft of 1940.  The comedy team made two more service comedies before the United States entered the war ("In the Navy" and "Keep 'Em Flying").  A sequel to this movie, "Buck Privates Come Home", was released in 1947.  "Buck Privates" is one of three Abbott and Costello films featuring The Andrews Sisters, who were also under contract to Universal Pictures at the time.

Francis (film): Francis is a 1950 American black-and-white comedy film from Universal-International that launched the Francis the Talking Mule film series.  "Francis" is produced by Robert Arthur, directed by Arthur Lubin, and stars Donald O'Connor and Patricia Medina.  The distinctive voice of Francis is a voice-over by actor Chill Wills.

Ciro Ippolito: Ciro Ippolito (born Naples, Italy, 27 January 1947) is an Italian film director and producer.  He is known to horror film fans for his 1980 opus "", which he coproduced, wrote and directed.

Alien 2: On Earth: Alien 2: On Earth/ Alien 2 Sulla Terra, also known as Alien Terror and Strangers, is a 1980 science fiction film, written and directed by Ciro Ippolito before the trademark "Alien" was registered.  It was released following the success of the 1979 film "Alien" as an unofficial sequel, albeit having little connection to the film.

In Society: In Society is a 1944 film starring the comedy team of Abbott and Costello.  It was the first of five Abbott and Costello films to be directed by Jean Yarbrough.  It was re-released in 1953.

A Successful Failure: A Successful Failure (1934) is an American film directed by Arthur Lubin.  It was Lubin's first movie as director.

The Incredible Mr. Limpet: The Incredible Mr. Limpet is a 1964 American live-action/animated adventure film from Warner Bros. It is about a man named Henry Limpet who turns into a talking fish resembling a tilefish and helps the U.S. Navy locate and destroy Nazi submarines.  Don Knotts plays the title character.  The live action was directed by Arthur Lubin, while the animation was directed by Bill Tytla, Robert McKimson, Hawley Pratt, and Gerry Chiniquy.  Music includes songs by Sammy Fain, in collaboration with Harold Adamson, including "I Wish I Were a Fish," "Be Careful How You Wish," and "Deep Rapture."

Question: Who directed more Abbot and Costello films, Arthur Lubin or Ciro Ippolito?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "directors": {
      "type": "array",
      "description": "List of directors and their Abbott and Costello film counts.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the director."
          },
          "abott_costello_films_count": {
            "type": "integer",
            "description": "The number of Abbott and Costello films directed by this person, based on explicit mentions in the context."
          },
          "abott_costello_films": {
            "type": "array",
            "description": "Titles of Abbott and Costello films explicitly mentioned as directed by this person.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "abott_costello_films_count",
          "abott_costello_films"
        ],
        "additionalProperties": false
      }
    },
    "director_with_most_abott_costello_films": {
      "type": "string",
      "description": "The name of the director who directed more Abbott and Costello films."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement comparing the number of Abbott and Costello films directed by the two individuals."
    }
  },
  "required": [
    "directors",
    "director_with_most_abott_costello_films",
    "comparison_summary"
  ],
  "additionalProperties": false
}
