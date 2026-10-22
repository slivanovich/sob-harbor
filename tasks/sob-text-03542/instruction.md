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
The Fly (1986 film): The Fly is a 1986 American science-fiction horror film directed and co-written by David Cronenberg.  Produced by Brooksfilms and distributed by 20th Century Fox, the film stars Jeff Goldblum, Geena Davis and John Getz.  Loosely based on George Langelaan's 1957 short story of the same name, the film tells of an eccentric scientist who, after one of his experiments goes wrong, slowly turns into a fly-hybrid creature.  The score was composed by Howard Shore and the make-up effects were created by Chris Walas, along with makeup artist Stephan Dupuis.

Tommy Swerdlow: Tommy Swerdlow is an American actor and screenwriter.  He has appeared in such films as "Howard the Duck" (1986) and "Spaceballs" (1987) and co-wrote the screenplays of "Cool Runnings" (1993), "Little Giants" (1994) and "Snow Dogs" (2002).  Swerdlow made his directorial debut with the 2017 feature "A Thousand Junkies".  He has also written a biopic about the life of Matisyahu titled "King Without a Crown".

Class of Nuke 'Em High: Class of Nuke 'Em High (also known as Atomic High School) is a 1986 American science-fiction horror comedy film made by cult classic B-movie production group Troma Entertainment.  It was directed by Richard W. Haines and Lloyd Kaufman under the pseudonym "Samuel Weil".  New York holographer Jason Sapan created the laser effects.

A Thousand Junkies: A Thousand Junkies is a 2017 American comedy-drama film directed by and starring Tommy Swerdlow.  It is Swerdlow's directorial debut.

Aliens (film): Aliens is a 1986 American science-fiction action horror film written and directed by James Cameron, produced by Gale Anne Hurd and starring Sigourney Weaver, Carrie Henn, Michael Biehn, Paul Reiser, Lance Henriksen, Jenette Goldstein, William Hope, and Bill Paxton.  It is the sequel to the 1979 film "Alien" and the second installment in the "Alien" franchise.  The film follows Weaver's character Ellen Ripley as she returns to the moon where her crew encountered the hostile Alien creature, this time accompanied by a unit of space marines.

Bill &amp; Ted's Excellent Adventure: Bill & Ted's Excellent Adventure is a 1989 American science-fiction comedy buddy film in which two slackers travel through time to assemble a menagerie of historical figures for their high school history presentation.

The Stepford Wives (2004 film): The Stepford Wives is a 2004 American science-fiction comedy film.  It was directed by Frank Oz from a screenplay by Paul Rudnick and stars Nicole Kidman, Matthew Broderick, Bette Midler, Christopher Walken, Faith Hill and Glenn Close.  The film is a remake of the 1975 film of the same title; both films are based on the Ira Levin novel "The Stepford Wives".  The remake grossed $102 million worldwide on a $90 million budget.

Howard the Duck (film): Howard the Duck (titled Howard: A New Breed of Hero in the UK) is a 1986 American science-fiction comedy film directed by Willard Huyck and starring Chip Zien, Lea Thompson, Jeffrey Jones, and Tim Robbins.  Produced by Gloria Katz and written by Huyck and Katz, with George Lucas as executive producer, the screenplay was originally intended to be an animated film based on the Marvel comic book of the same name, but the film adaptation became live-action because of a contractual obligation.  Although several TV adaptations of Marvel characters had aired during the preceding 21 years, this was the first theatrical released feature film, coming after the serial "Captain America".

The Unkissed Bride: The Unkissed Bride is a 1966 comedy starring Tommy Kirk.  The film is also known as Mother Goose-A-Go-Go.

Purple People Eater (film): Purple People Eater is a 1988 American science-fiction comedy film based on Sheb Wooley's 1958 novelty song of the same name, written and directed by Linda Shayne, and stars Neil Patrick Harris, Ned Beatty, Shelley Winters, Thora Birch in her film debut, Dustin Diamond and Peggy Lipton, with Chubby Checker and Little Richard making musical guest appearances.  The film was released on December 16, 1988.

Question: Who directed a 1986 American science-fiction comedy starring Tommy Swerdlow?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres the film belongs to."
    },
    "starring_actor": {
      "type": "string",
      "description": "The name of the actor who starred in the film, as specified in the question."
    }
  },
  "required": [
    "film_title",
    "director_name",
    "release_year",
    "genres",
    "starring_actor"
  ],
  "additionalProperties": false
}
