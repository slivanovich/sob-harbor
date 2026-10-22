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
Moe'N'a Lisa: "Moe'N'a Lisa" is the sixth episode of "The Simpsons"<nowiki>'</nowiki> eighteenth season.  It first aired on the Fox network in the United States on November 19, 2006.  Lisa aids Moe in discovering his inner-poet and he gains swift popularity and recognition from a group of successful American authors, when Lisa helps to get his poetry published.  However, Lisa is crushed when Moe enjoys his newfound success with famous writers and deliberately refuses to credit Lisa for her assistance in his poetry.  It was written by Matt Warburton and directed by Mark Kirkland.  The episode guest stars J. K. Simmons as the voice of J. Jonah Jameson, while Tom Wolfe, Gore Vidal, Michael Chabon, and Jonathan Franzen make cameos as themselves.  During its first airing, the episode gained 9.31 million viewers, beating the previous episode.

Songs in the Key of Springfield: Songs in the Key of Springfield is a soundtrack/novelty album from "The Simpsons" compiling many of the musical numbers from the series.  The album was released in the United States on March 18, 1997, and in the United Kingdom in June 1997.  This was the second album released in association with the "Simpsons" television series; however, the previous release, "The Simpsons Sing the Blues", contained original recordings as opposed to songs featured in episodes of the series.

Lost Our Lisa: "Lost Our Lisa" is the twenty-fourth episode in the ninth season of the American animated television series "The Simpsons".  It originally aired on the Fox network in the United States on May 10, 1998.  The episode contains the last appearance of the character Lionel Hutz.  When Lisa learns that Marge cannot give her a ride to the museum and forbids her to take the bus, she tricks Homer into giving her permission.  After Lisa gets lost, Homer goes looking for her and the two end up visiting the museum together.  The episode is analyzed in the books "Planet Simpson", "The Psychology of the Simpsons: D'oh! ", and "", and received positive mention in "I Can't Believe It's a Bigger and Better Updated Unofficial Simpsons Guide".

I Love Lisa: "I Love Lisa" is the fifteenth episode of "The Simpsons"<nowiki>'</nowiki> fourth season.  It originally aired on the Fox network in the United States on February 11, 1993.  In the episode, Lisa gives Ralph Wiggum a Valentine's Day card when she sees that he has not received any.  Ralph reads too much into Lisa's gesture and, much to Lisa's dismay, relentlessly pursues her with affection.  Lisa snaps at Ralph and angrily tells him they are not together and that she never liked him.  Heartbroken, Ralph channels his feelings into his performance as George Washington in the school's President's Day pageant.  After a thunderous applause from the audience, he is able to accept Lisa as just a friend.

The Simpsons Sing the Blues: The Simpsons Sing the Blues is the first album released as an offshoot of "The Simpsons".  The album contains originally recorded music not featured in the series save for the first verse of the track "Moaning Lisa Blues" which was first featured in the episode "Moaning Lisa", which aired in the United States on February 11, 1990.  The album was released on December 4, 1990, and peaked at No. 3 on the "Billboard" 200.

The Simpsons discography: "The Simpsons" is an American animated television sitcom created by Matt Groening that has aired on the Fox Broadcasting Company since December 1989.  It is a satirical parody of a middle class American lifestyle epitomized by its eponymous family, which consists of Homer, Marge, Bart, Lisa and Maggie.  The show is set in the fictional town of Springfield, and lampoons American culture, society, and many aspects of the human condition.  The popularity of "The Simpsons" led to the release of the 1990 double platinum album "The Simpsons Sing the Blues", which contains original songs performed by the cast members of the show as their characters.  The album spawned two hit singles—"Do the Bartman" and "Deep, Deep Trouble".  A less successful sequel, "The Yellow Album", was released in 1998.

Homer and Lisa Exchange Cross Words: "Homer and Lisa Exchange Cross Words" is the sixth episode of "The Simpsons"<nowiki>'</nowiki> twentieth season.  It originally aired on the Fox network in the United States on November 16, 2008.  In the episode, Lisa discovers that she has a talent for solving crossword puzzles, and she enters a crossword tournament.  Lisa's feelings are hurt when she discovers that Homer bet against her in the championship match.

Good Night (The Simpsons short): "Good Night" (also known as "Good Night Simpsons") is the first of forty-eight Simpsons shorts that appeared on the variety show "The Tracey Ullman Show".  It originally aired on the Fox network in the United States on April 19, 1987, during the third episode of "The Tracey Ullman Show" and marks the first appearance of the Simpson family — Homer, Marge, Bart, Lisa, and Maggie — on television.  After three seasons on Tracey Ullman, the shorts would be adapted into the animated show "The Simpsons".  "Good Night" has since been aired on the show in the episode "The Simpsons 138th Episode Spectacular" (in its entirety), along with several other Ullman shorts, and is one of the few shorts to ever be released on DVD, being included in the Season 1 DVD set.

Moaning Lisa: "Moaning Lisa" is the sixth episode of "The Simpsons"<nowiki>'</nowiki> first season.  It originally aired on the Fox network in the United States on February 11, 1990.  The episode was written by Al Jean and Mike Reiss, and was directed by Wes Archer.  Ron Taylor guest stars in the episode as Bleeding Gums Murphy.  The episode deals with Lisa's depression and her attempts to sublimate it by playing her saxophone.  It received positive reviews from television critics.

The Yellow Album: The Yellow Album is "The Simpsons" second album of originally recorded songs, released as a follow-up to the 1990 album "The Simpsons Sing the Blues".  Though it was released in 1998, it had been recorded years earlier, after the success of the first album.  The title is a play on the name of The Beatles' highly popular self-titled 1968 album, commonly known as ""The White Album"", with the skin color of the characters of "The Simpsons".  In addition, the cover is a parody of The Beatles' 1967 album, "Sgt. Pepper's Lonely Hearts Club Band".

Question: The Simpsons Sing the Blues is the first album released as an offshoot of "The Simpsons", the album contains originally recorded music, the first verse of the track "Moaning Lisa Blues" which was first featured in which episode, the sixth episode of "The Simpsons"' first season, and originally aired on the Fox network in the United States on February 11, 1990?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "track_name": {
      "type": "string",
      "description": "The name of the track from the album."
    },
    "episode_details": {
      "type": "object",
      "properties": {
        "episode_title": {
          "type": "string",
          "description": "The title of the episode."
        },
        "season_number": {
          "type": "integer",
          "description": "The season number of the episode."
        },
        "episode_number_in_season": {
          "type": "integer",
          "description": "The episode number within its season."
        },
        "original_air_date": {
          "type": "string",
          "description": "The original air date of the episode."
        },
        "network": {
          "type": "string",
          "description": "The network on which the episode originally aired."
        },
        "country_of_airing": {
          "type": "string",
          "description": "The country where the episode originally aired."
        }
      },
      "required": [
        "episode_title",
        "season_number",
        "episode_number_in_season",
        "original_air_date",
        "network",
        "country_of_airing"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "Description of the relationship between the track and the episode."
    }
  },
  "required": [
    "album_name",
    "track_name",
    "episode_details",
    "relationship_description"
  ],
  "additionalProperties": false
}
