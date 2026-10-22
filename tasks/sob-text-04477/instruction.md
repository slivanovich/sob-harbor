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
Highlander: Endgame: Highlander: Endgame is a 2000 American fantasy action film directed by Doug Aarniokoski and starring Adrian Paul, Christopher Lambert, Bruce Payne and Lisa Barbuscia, It is the fourth theatrical release in the "Highlander" film series, and it serves as a continuation of both the "Highlander" film from 1986 and the .  The film reunites Duncan MacLeod, the lead character of the series, and Connor MacLeod, the lead character of the films.  In the film, the Macleods need to deal against a new enemy named Jacob Kell, a powerful immortal who is willing to win the Prize.  "Highlander: Endgame" was released on September 1, 2000.  It was followed by "" which released seven years later, with Paul reprising his role.

Russell Mulcahy: Russell Mulcahy (born 23 June 1953 in Melbourne, Australia) is an Australian film director.  Mulcahy's work is recognizable by the use of fast cuts, tracking shots and use of glowing lights, and he was one of the most prominent music video directors of the 1980s.  He has also worked in television since the early 1990s and as a director on episodes of MTV's "Teen Wolf".

Highlander (film): Highlander is a 1986 British-American adventure action fantasy film directed by Russell Mulcahy and based on a story by Gregory Widen.  It stars Christopher Lambert, Sean Connery, Clancy Brown, and Roxanne Hart.  The film narrates the climax of an ages-old battle between immortal warriors, depicted through interwoven past and present-day storylines.

Kelly Makin: Kelly Makin is a Canadian television and film director.  He directed episodes of "The Kids in the Hall" comedy television series and also directed several episodes of "Queer as Folk" including that series' last episode.  More recently, Makin has directed episodes of "Flashpoint", "Less Than Kind" and "Death Comes to Town".  He also directed two episodes of "Being Erica".

Thomas J. Wright: Thomas J. Wright is an American television director, film director, artist, and set designer.  Wright has directed episodes of "Smallville", "One Tree Hill", "Firefly", and many other programs.  He also worked extensively on Chris Carter's "Millennium", on which he was a producer as well as directing 26 of the show's 67 episodes.  He also directed the 1989 Hulk Hogan film "No Holds Barred".  He also was the artist who created the paintings used in the television horror anthology series "Night Gallery".

James Strong (director): James Strong is a British television and film director and writer, best known for his work on "Broadchurch" for which he was BAFTA nominated for Best Director Fiction 2015.  He trained as Director at Granada TV and has directed episodes of the shows "Holby City" and "Doctors", as well as six episodes of "Doctor Who" and two episodes of its spin-off series "Torchwood".  His work on the "Doctor Who" episode "Voyage of the Damned" won him a BAFTA Cymru award for Best Director in 2008.

Making the Video: Making the Video is an MTV show, consisting of half-hour episodes, which chronicles the process of filming various music videos. Usually the director outlines the concept of the video (or treatment) and the show often includes light-hearted and humorous moments.  It always concludes with a premiere of the finished video.  The show premiered on July 11, 1999 and is currently on a hiatus as of 2009.

Momo (film): Momo is a 1986 fantasy film directed by Johannes Schaaf and based on the 1973 novel "Momo" by Michael Ende.  It is about the concept of time and how it is used by humans in modern societies.  The film features the final acting role of actor / writer / director John Huston.

Jason Woliner: Jason Woliner (born June 1, 1980) is an American comedy director, writer, and a former child actor.  He was the non-performing member of the comedy group Human Giant and directed the bulk of their output.  The group, which also consisted of comedians Aziz Ansari, Rob Huebel, and Paul Scheer, produced an MTV sketch comedy show that ran for two seasons.  He has been directing, writing on, and executive producing the Adult Swim series "Eagleheart", starring Chris Elliott.  The show has completed production of three seasons and is on hiatus.  Woliner has directed episodes of Fox TV's "The Last Man On Earth", NBC's "Parks and Recreation", and Comedy Central's "Nathan for You" and "Jon Benjamin Has A Van", among others.

Highlander (franchise): Highlander is a film and television franchise that began with a 1986 fantasy movie starring Christopher Lambert, who played Connor MacLeod, the Highlander.  Born in Glenfinnan, in the Scottish Highlands in the 16th century, MacLeod is one of a number of Immortals.  There have been five "Highlander" movies, two television series, an animated series, an animated movie, an animated flash-movie series, ten original novels, nineteen comic book issues, and various licensed merchandise.

Question: Highlander is a 1986 fantasy film directed by an Australian film director who directed episodes of what MTV show?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film in question."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's director."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the director."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "mtv_show_directed": {
      "type": "string",
      "description": "The name of the MTV show directed by the film's director."
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "director",
    "mtv_show_directed"
  ],
  "additionalProperties": false
}
