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
The Karate Kid Part II: The Karate Kid Part II is a 1986 American martial arts drama film and the first sequel to "The Karate Kid" (1984).  Ralph Macchio and Pat Morita reprise their respective roles as young karate student Daniel LaRusso and his mentor Kesuke Miyagi.  Like the original film, the sequel was a success, earning even more at the box office than its predecessor, although it received mixed reviews from critics.

Jaden Smith: Jaden Christopher Syre Smith (born July 8, 1998) is an American actor and rapper.  He is the son of Jada Pinkett Smith and Will Smith.  Jaden Smith's first movie role was with his father in the 2006 film "The Pursuit of Happyness".  He also acted in the 2008 remake of "The Day the Earth Stood Still" and the 2010 remake of "The Karate Kid", and was in the 2013 film "After Earth" with his father.

The Karate Kid (2010 film): The Karate Kid is a 2010 family martial arts drama film directed by Harald Zwart.  It stars Jaden Smith, Jackie Chan and Taraji P. Henson in lead roles, and it was produced by Jerry Weintraub, James Lassiter, Ken Stovitz and Jaden's parents Will and Jada.  The screenplay by Christopher Murphey was from the story written by Robert Mark Kamen for the original 1984 film of the same name.  Unlike the original, this remake is set in the People's Republic of China, and features Kung Fu instead of Japanese Karate.  The film's music was composed by James Horner.  It is an international co-production between China, Hong Kong, and the United States.

The Next Karate Kid: The Next Karate Kid (also known as The Karate Kid Part IV) is a 1994 American martial arts drama film starring Pat Morita and Hilary Swank.  It is the fourth and final installment in "The Karate Kid" series.  It was directed by Christopher Cain and produced by Jerry Weintraub, with music by Bill Conti.  It was the only film in the series released in the 1990s, ten years after the first installment, and is also the first film in the series not to feature Ralph Macchio in the lead role as Daniel LaRusso or be written for the screen by Robert Mark Kamen or directed by John G. Avildsen.

Willow Smith: Willow Camille Reign Smith (born October 31, 2000), known professionally as Willow, is an American singer, actress and dancer.  She is the daughter of Will Smith and Jada Pinkett Smith, the younger sister of Jaden Smith and the half-sister of Willard Carroll "Trey" Smith III.  Smith made her acting debut in 2007 in the film "I Am Legend" and later appeared in "" alongside Abigail Breslin.  She received a Young Artist Award for her performance.

Never Say Never: The Remixes: Never Say Never: The Remixes is the second remix album by Canadian recording artist Justin Bieber.  Released on February 14, 2011, the album accompanies the release of his film, "".  The album includes remixes of five songs from his first album, "My World 2.0", featuring guest appearances from Jaden Smith, Rascal Flatts, Usher, Chris Brown, Kanye West, Raekwon and Miley Cyrus.  In addition a new track is also included.  The Jaden Smith-assisted "Never Say Never", originally the theme song for "The Karate Kid", was re-released as the album's lead single and only single on January 25, 2011.

The Karate Kid Part III: The Karate Kid Part III is a 1989 American martial arts drama film and the second sequel to "The Karate Kid" (1984).  The film stars Ralph Macchio, Noriyuki "Pat" Morita, Robyn Lively and Thomas Ian Griffith.  As was the case with the first two films in the series, it was directed by John G. Avildsen and written by Robert Mark Kamen, with stunts choreographed by Pat E. Johnson and the music composed by Bill Conti.  In the film, with the help of his best friend, Terry Silver, the returning John Kreese attempts to gain revenge on Daniel and Mr. Miyagi which involves hiring a ruthless martial artist and harming their relationship.

The Karate Kid: The Karate Kid is a 1984 American martial arts drama film produced by Jerry Weintraub, directed by John G. Avildsen, written by Robert Mark Kamen, and stars Ralph Macchio, Pat Morita and Elisabeth Shue.  It is an underdog story in the mold of a previous success with "Rocky" (1976), which Avildsen also directed.  The film features the Gōjū-ryū style of karate.  "The Karate Kid" was a commercial success upon release and garnered critical acclaim, earning Morita an Academy Award nomination for Best Supporting Actor.  The film became the first installment in an ongoing film series, spawning three sequels, a 2010 remake and an upcoming follow-up television series.

The Karate Kid (franchise): The Karate Kid is an American martial arts drama multi-media franchise created by screenwriter Robert Mark Kamen.  It began in 1984 with "The Karate Kid", and was followed by three sequels, a remake and two TV series: "The Karate Kid Part II" (1986), "The Karate Kid Part III" (1989), "The Next Karate Kid" (1994), "The Karate Kid" (2010) and "Cobra Kai" (2018)

Jada Pinkett Smith: Jada Koren Pinkett-Smith ( ; née Pinkett; born September 18, 1971) is an American actress, dancer, singer-songwriter, and businesswoman.  She began her career in 1990, when she made a guest appearance in the short-lived sitcom "True Colors".  She starred in "A Different World", produced by Bill Cosby, and she featured opposite Eddie Murphy in "The Nutty Professor" (1996).  She starred in dramatic films such as "Menace II Society" (1993) and "Set It Off" (1996).  She has appeared in more than 20 films in a variety of genres, including "Scream 2", "Ali", "The Matrix Reloaded", "The Matrix Revolutions", "Madagascar", "", and "".

Question: The Karate Kid is a family martial arts drama film, released in what year, directed by Harald Zwart, it stars Jaden Smith, produced by Jaden's parents Will and Jada, Jada Koren Pinkett-Smith, is an American actress, dancer, singer-songwriter, and businesswoman?

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
    "lead_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of lead actors in the film."
    },
    "producers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the producer."
          },
          "is_jaden_smith_parent": {
            "type": "boolean",
            "description": "Indicates if the producer is a parent of Jaden Smith."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions for the producer, if available."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "description": "A list of producers for the film, including details about Jaden Smith's parents."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "lead_actors",
    "producers"
  ],
  "additionalProperties": false
}
