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
The Blues Brothers: The Blues Brothers are an American blues and soul revivalist band which was founded in 1978 by comedy actors Dan Aykroyd and John Belushi as part of a musical sketch on "Saturday Night Live."  Belushi and Aykroyd, respectively in character as lead vocalist "Joliet" Jake Blues and harmonica player/vocalist Elwood Blues, fronted the band, which was composed of well-known and respected musicians.  The band made its debut as the musical guest on the April 22, 1978, episode of "Saturday Night Live," performing "Hey Bartender."

1941 (film): 1941 is a 1979 American period comedy film directed by Steven Spielberg, written by Robert Zemeckis and Bob Gale, and featuring an ensemble cast including Dan Aykroyd, Ned Beatty, John Belushi, John Candy, Christopher Lee, Toshiro Mifune, and Robert Stack.  The story involves a panic in the Los Angeles area after the December 1941 attack on Pearl Harbor.

The Blues Brothers (film): The Blues Brothers is a 1980 American musical crime comedy film directed by John Landis.  It stars John Belushi and Dan Aykroyd as "Joliet" Jake and Elwood Blues, characters developed from "The Blues Brothers" musical sketch on the NBC variety series "Saturday Night Live".  The film's screenplay was written by Aykroyd and Landis.  It features musical numbers by rhythm and blues (R&B), soul, and blues singers James Brown, Cab Calloway, Aretha Franklin, Ray Charles, and John Lee Hooker.  The film is set in and around Chicago, Illinois, where it was filmed.  It features non-musical supporting performances by John Candy, Carrie Fisher, Charles Napier, and Henry Gibson.

Spies Like Us: Spies Like Us is a 1985 American comedy film directed by John Landis and starring Chevy Chase, Dan Aykroyd, Steve Forrest, and Donna Dixon.  The film presents the comic adventures of two novice intelligence agents sent to the Soviet Union.  Originally written by Aykroyd and Dave Thomas to star Aykroyd and John Belushi at Universal, the script went into turnaround and was later picked up by Warner Bros. with Aykroyd and Chase starring.

Belushi: A Biography: Belushi: A Biography is an "oral history" biography of John Belushi, written and collaborated by John's widow, Judith Belushi Pisano and co-author Tanner Colby, with an introduction by Dan Aykroyd.  Filled with anecdotes and interviews from John's personal friends, fellow "Saturday Night Live" alumni, and film co-stars, it is a non-objective, positive portrayal of the actor's life and influence.

The Land of Gorch: The Land of Gorch was a recurring skit that appeared in season one of the American comedy television program "Saturday Night Live," featuring Jim Henson's Muppets.  Prior to his work for children on "Sesame Street", Henson had created puppetry work, including his show "Sam and Friends", for adult audiences.  His characters appeared regularly on the late-night comedy television programs, and "The Ed Sullivan Show".  After "Sesame Street", Henson feared he would become typecast into working on children's television series.  His talent agent Bernie Brillstein, who represented Gilda Radner, Dan Aykroyd, and John Belushi, helped him transition to "Saturday Night Live".

John Landis: John David Landis (born August 3, 1950) is an American film director, screenwriter, actor, and producer.  He is best known for the comedy films that he has directed such as "National Lampoon's Animal House" (1978), "The Blues Brothers" (1980), "An American Werewolf in London" (1981), "Trading Places" (1983), "¡Three Amigos! " (1986), "Coming to America" (1988) and "Beverly Hills Cop III" (1994), and for directing Michael Jackson's music videos for "Thriller" (1983) and "Black or White" (1991).

John Belushi: John Adam Belushi ( ; January 24, 1949 – March 5, 1982) was an American comedian, actor and musician.  Belushi is best known for his "intense energy and raucous attitude" which he displayed as one of the seven original cast members of the NBC sketch comedy show "Saturday Night Live" ("SNL").  Throughout his career, Belushi had a close personal and artistic partnership with his fellow "SNL" star Dan Aykroyd, whom he met while they were both working at Chicago's The Second City comedy club.

Neighbors (1981 film): Neighbors is a 1981 American comedy film based on the novel of the same name by Thomas Berger.  It was released through Columbia Pictures, was directed by John G. Avildsen, and starred John Belushi, Dan Aykroyd, Cathy Moriarty, and Kathryn Walker.  The film takes liberties with Berger's story, and features a more upbeat ending.  The screenplay of the film is officially credited to Larry Gelbart, although it was extensively rewritten, to Gelbart's public disapproval.  Released two and a half months before John Belushi's death, the film marks the actor's last film performance.

Monteith and Rand: Monteith and Rand are a comedy team who had their own Broadway show at the Booth Theater in 1979, produced by James Lipton, after a successful off-Broadway run.  Suzanne Rand and John Monteith are graduates of Second City; Suzanne was in the famed company that included John Belushi and Bill Murray in Chicago, and John performed with John Candy, Dan Aykroyd and Gilda Radner in Toronto.  Monteith and Rand live in New York City where they teach and perform.

Question: The 1980 American musical crime comedy film set in Chicago, Illinois, starring John Belushi and Dan Aykroyd was directed by this American film director, screenwriter, actor, and producer who was born in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the director."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the director."
        },
        "occupation": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Occupations of the director."
        }
      },
      "required": [
        "name",
        "birth_year",
        "occupation"
      ],
      "additionalProperties": false
    },
    "setting_location": {
      "type": "string",
      "description": "The primary location where the film is set."
    }
  },
  "required": [
    "film_title",
    "director",
    "setting_location"
  ],
  "additionalProperties": false
}
