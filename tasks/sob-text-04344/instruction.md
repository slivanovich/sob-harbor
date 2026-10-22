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
Miłogost Reczek: Miłogost Reczek (born February 10, 1961) is a Polish actor.  He is known for dubbing voices.  He is known as the Polish dub voice for Homer Simpson in "The Simpsons Movie".  He has dubbed in films like "Star Wars" original trilogy, "Despicable Me", "Thomas and Friends", "Monsters vs Aliens", the Simpsons Movie.

Monsters vs. Aliens: Monsters vs. Aliens is a 2009 American 3D computer-animated science fiction film produced by DreamWorks Animation and distributed by Paramount Pictures.  It was DreamWorks Animation's first feature film to be directly produced in a stereoscopic 3-D format instead of being converted into 3-D after completion, which added $15 million to the film's budget.

Conrad Vernon: Conrad Vernon (born July 11, 1968) is an American director, storyboard artist, writer, and voice actor, best known for his work on the DreamWorks animated film series "Shrek" as well as other films such as "Monsters vs. Aliens", "", and "Penguins of Madagascar".  He also co-directed the adult animated film, "Sausage Party", which is a spoof of his notable works in DreamWorks.

Monsters vs. Aliens (franchise): Monsters vs. Aliens is a media franchise created by DreamWorks Animation.  The franchise began with the 2009 film "Monsters vs. Aliens" and has since grown to include a short film, two television specials, a television series, and a video game.

Mary and Max: Mary and Max is a 2009 Australian stop motion animated comedy-drama film written and directed by Adam Elliot as his first animated feature film with music by Dale Cornelius and produced by Melanie Coombs and Melodrama Pictures.  The voice cast included Philip Seymour Hoffman, Toni Collette, Eric Bana, Bethany Whitmore with narration by Barry Humphries.  The film premiered on the opening night of the 2009 Sundance Film Festival on January 15, 2009.  The film won the Annecy Cristal in June 2009 from the Annecy International Animated Film Festival, and Best Animated Feature Film at the Asia Pacific Screen Awards in November 2009.  The film was theatrically released on April 9, 2009 by Icon Entertainment International.  "Mary and Max" received very positive reviews from critics and it earned $1.7 million USD on a $8.2 million AUD budget.

Night of the Living Carrots: Night of the Living Carrots is a 2011 Halloween short animated film, based on "Monsters vs. Aliens" and produced by DreamWorks Animation.  Following the 2009 short, "", a mutated carrot has spawned hundreds of zombie carrots taking control of the subject's mind.  Dr. Cockroach determines that the only way to defeat them and free their victims is for B.O.B. to eat all of the carrots.

Monsters vs. Aliens (TV series): Monsters vs. Aliens is an American computer-animated television series based on the 2009 film of the same name.  After being first announced in 2009, the series premiered on Nickelodeon on March 23, 2013, after the Nickelodeon Kids' Choice Awards, then began airing in its regular timeslot on April 6, 2013.  A total of 26 episodes consisting of 52 segments were released, with the last episode airing on February 8, 2014.

Bob Schooley: Robert "Bob" Schooley is an American screenwriter, television writer and television producer.  He and Mark McCorkle are the creators of the 2002 animated television series "Kim Possible", which aired on Disney Channel.  He was also an executive producer of the series, as well as having written scripts for several episodes.  He was working as a producer for "The Penguins of Madagascar" and "Monsters vs. Aliens" along with McCorkle.  He also wrote a book called ""Liar of Kudzu"" with McCorkle.  He comes from Levittown, Pennsylvania.  As of 2016, he and McCorkle are currently creating and executive producing a new TV series based on the 2014 Disney animated feature, "Big Hero 6" for Disney XD.

Buchanan Brothers: The Buchanan Brothers were two brothers, Chester and Lester Buchanan, who recorded country music during the 1940s on the RCA Victor label.  They had a top ten hit, "Atomic Power", released in August 1946; this song was also featured in the 1982 movie "The Atomic Café".  Another song, 1947's "(When You See) Those Flying Saucers", was used in the opening scene of the 2009 animated release "Monsters vs. Aliens".

Monsters vs. Aliens (video game): Monsters vs. Aliens is a 2009 video game based on the film with the same name.  The game was released on March 24, 2009 on PlayStation 2, Nintendo DS, Xbox 360, PlayStation 3 And Wii.

Question: Which year were the animated films Mary and Max and Monsters vs. Aliens released?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "films": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "all_released_in_same_year": {
      "type": "boolean"
    },
    "shared_release_year": {
      "type": "integer"
    }
  },
  "required": [
    "films",
    "all_released_in_same_year",
    "shared_release_year"
  ],
  "additionalProperties": false
}
