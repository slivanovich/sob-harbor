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
The Dirty Dozen: The Dirty Dozen is a 1967 American war film directed by Robert Aldrich, released by MGM, and starring Lee Marvin.  The picture was filmed in the United Kingdom and features an ensemble supporting cast including Ernest Borgnine, Charles Bronson, Jim Brown, John Cassavetes, Telly Savalas, Robert Webber, and Donald Sutherland.  The film is based on E. M. Nathanson's novel of the same name that was inspired by a real-life group called the "Filthy Thirteen".  In 2001, the American Film Institute placed the film at number 65 on their 100 Years... 100 Thrills list.

The Inglorious Bastards: The Inglorious Bastards (Italian: "Quel maledetto treno blindato" , literally: "That damned armored train") is a 1978 Italian action/war film directed by Enzo G. Castellari, written by Sandro Continenza, Sergio Grieco, Franco Marotta, Romano Migliorini, and Laura Toscano, and starring Bo Svenson, Peter Hooten, Fred Williamson, Michael Pergolani, and Jackie Basehart.  The film score was written by Francesco De Masi.  The film—which concerns a group of prisoners who are drafted into a special war mission in 1944—is a loose remake of the 1967 American film, "The Dirty Dozen".

Calvin A. Johnson Jr.: Calvin A. Johnson Jr. (born November 21, 1985) is an American saxophonist, bandleader, composer, producer, and actor from New Orleans, Louisiana, United States.  A multi-instrumentalist, he is best known as a tenor and soprano saxophone player but also performs and records on alto and baritone saxophones, clarinet, and flute.  Johnson has worked with many of the biggest names in New Orleans music, including Aaron Neville, Harry Connick, Jr., the Dirty Dozen Brass Band, Mystikal, Irvin Mayfield, Mannie Fresh, and others.  Johnson is the nephew of New Orleans clarinetist Ralph Johnson, a longtime member of the Preservation Hall Jazz Band.  Johnson began playing saxophone at the age of seven, and since 2008 has been playing with his own band, Calvin Johnson & Native Son.  In 2015, he started a new band with Dirty Dozen Brass Band founding member and sousaphone player, Kirk Joseph, called Chapter:SOUL.

The Dirty Dozen: Next Mission: The Dirty Dozen: Next Mission is a made-for-TV film and sequel to the original "Dirty Dozen", directed by Andrew V. McLaglen and reuniting Lee Marvin, Ernest Borgnine and Richard Jaeckel 18 years after the original hit war film.  Marvin returns to lead an all-new dirty dozen on a mission to assassinate an SS General played by Wolf Kahler.

The Secret Invasion: The Secret Invasion is a 1964 American war film directed by Roger Corman.  It stars Stewart Granger, Raf Vallone, Mickey Rooney, Edd Byrnes, Henry Silva, Spela Rozin and William Campbell.  Appearing three years before "The Dirty Dozen" (1967), the film features a similar World War II mission where convicts are recruited by the Allies for an extremely hazardous operation behind enemy lines.

Lee Marvin: Lee Marvin (February 19, 1924 – August 29, 1987) was an American film and television actor.  Known for his distinctive voice and prematurely white hair, Marvin initially appeared in supporting roles, mostly villains, soldiers, and other hardboiled characters.  A prominent television role was that of Detective Lieutenant Frank Ballinger in the NBC crime series "M Squad" (1957–1960).

Dirty Dozen: The Dirty Dozen is a 1967 American war film.  Dirty Dozen may also refer to:

Deadly Dozen: Deadly Dozen is a 2001 World War II oriented squad-based first-person shooter video game developed by nFusion Interactive.  The title refers to the famous World War II movie "The Dirty Dozen".  As in the movie, the main protagonists are military misfits sentenced to death or long term imprisonment who are given a chance to redeem themselves by going on dangerous missions.  The game was followed by a sequel titled "".

The Dirty Dozen: The Deadly Mission: The Dirty Dozen: The Deadly Mission is a 1987 made-for-TV film and is the second sequel to the original "The Dirty Dozen".  It features an all-new 'dirty dozen,' this time under the leadership of Major Wright (Telly Savalas), playing a different role than in the 1967 film.

The Dirty Dozen: The Fatal Mission: The Dirty Dozen: The Fatal Mission is a 1988 made-for-TV film directed by Lee H. Katzin, and is the third sequel to "The Dirty Dozen".  It features an all-new 'dirty dozen,' with the exception of the returning Joe Stern, under the leadership of Major Wright (performed by Telly Savalas in his final film appearance).

Question: The Dirty Dozen: Next Mission is a made-for-TV film and sequel to the original "Dirty Dozen", directed by Andrew V. McLaglen and reuniting which American film and television actor, with Ernest Borgnine and Richard Jaeckel 18 years after the original hit war film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film being discussed."
    },
    "film_type": {
      "type": "string",
      "description": "Description of the film's nature (e.g., made-for-TV, sequel)."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "reunited_actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the American film and television actor reunited."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the actor."
        }
      },
      "required": [
        "name",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    },
    "other_reunited_cast_members": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other cast members reunited for the film."
    },
    "years_since_original_film": {
      "type": "integer",
      "description": "Number of years since the original film for the reunion."
    }
  },
  "required": [
    "film_title",
    "film_type",
    "director",
    "reunited_actor",
    "other_reunited_cast_members",
    "years_since_original_film"
  ],
  "additionalProperties": false
}
