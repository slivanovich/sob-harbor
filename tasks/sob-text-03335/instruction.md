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
More Songs from Pooh Corner: More Songs from Pooh Corner is a children's music album released in 2000 by Kenny Loggins.  The follow-up to his 1994 album Return to Pooh Corner, it includes the theme song from the recent Disney Winnie the Pooh film "The Tigger Movie", "Your Heart Will Lead You Home", which he also performed for that film's soundtrack, as well as several classic film songs and duets with Olivia Newton-John and Alison Krauss.  "Always in All Ways" was based on Loggins' wife's letters and response to his children leaving the nest while "Hana Aluna Lullabye" featuring lyrics in Hawaiian and English was written for his fifth child Hana named after a town on the Hawaiian island of Maui he and second wife Julia fell in love on in 1991.  It was jointly released by Loggins' label Columbia Records, Sony Wonder, and Walt Disney Records.  It was revealed on The Tonight Show with Jimmy Fallon March 15th, 2016 that the girl on the cover's left is Zoe Kravitz.

I Hum to Myself: "I Hum to Myself" is a song from the "Welcome to Pooh Corner" Cable TV series which premiered in 1983 on the Disney Channel (which was also that channel's inaugural season).  The song was written by the Academy Award-winning songwriting duo of Richard M. Sherman and Robert B. Sherman.  The Sherman Brothers also wrote the majority of the well known Winnie the Pooh songs, including "The Wonderful Thing about Tiggers" and "Heffalumps and Woozles" from the 1960s, and in 2000 wrote the score to "The Tigger Movie".

Pollyanna (1960 film): Pollyanna is a 1960 Walt Disney Productions feature film, starring child actress Hayley Mills, Jane Wyman, Karl Malden, and Richard Egan, in a story about a cheerful orphan changing the outlook of a small town.  Based on the novel "Pollyanna" (1913) by Eleanor Porter, the film was written and directed by David Swift.  The film marks Mills's first of six films for Disney, and it won the actress an Academy Juvenile Award.

The Right Side: "The Right Side" is a song from the "Welcome to Pooh Corner" Cable TV series which premiered in 1983 during the Disney Channel's inaugural season.  The song was written by the Academy Award-winning songwriting duo Richard M. Sherman and Robert B. Sherman.  The Sherman Brothers also wrote the majority of the well known Winnie the Pooh songs, including "The Wonderful Thing About Tiggers" and "Heffalumps and Woozles" from the 1960s, and in 2000 wrote the score to "The Tigger Movie".

The Tigger Movie: The Tigger Movie is a 2000 American animated musical comedy-drama film written and directed by Jun Falkenstein from a story by Eddie Guzelian.  Part of the "Winnie-the-Pooh" series, this film features Pooh's friend Tigger searching for his family tree and other Tiggers like himself.

Return to Pooh Corner: Return to Pooh Corner is a children's music album by soft rock singer Kenny Loggins.  Released in 1994, it features songs written by John Lennon, Rickie Lee Jones, Paul Simon and Jimmy Webb, along with several other traditional children's songs.  It was a successful album for Loggins, selling over 500,000 copies, and was nominated for a Grammy.  Loggins returned to Pooh Corner several years later with 2000's "More Songs from Pooh Corner".  The songs are described as "music for parents and children to enjoy together".  Loggins's album More Songs from Pooh Corner contains the song that he helped the Sherman Brothers to write for The Tigger Movie, which was called Your Heart Will Lead You Home.  Guest appearances are made by David Crosby and Graham Nash on "All the Pretty Little Ponies", Patti Austin on the "Neverland Medley" and Amy Grant and Gary Chapman on the title track (a rewritten version of "House at Pooh Corner", a song Loggins wrote in high school and had previously recorded with Jim Messina for their 1971 album "Sittin' In").

Piglet's Big Movie: Piglet's Big Movie is a 2003 American animated musical comedy-drama adventure film produced by Walt Disney Feature Animation and animated by Walt Disney Animation (Japan).  It was released by Walt Disney Pictures on March 21, 2003.  The film is based upon the characters in the "Winnie-the-Pooh" books written by A. A. Milne.  It is the second in a recent series of theatrically released "Winnie the Pooh" films, preceded by "The Tigger Movie" (2000) and followed by "Pooh's Heffalump Movie" (2005).  In the film, Piglet is ashamed of being small and wanders off into the Hundred Acre Woods, leading his friends to form a search party to find him.

Just Say, 'Yes I Can': "Just Say, 'Yes I Can'" is a song from the "Welcome to Pooh Corner" Cable TV series which premiered in the Disney Channel's inaugural season in 1983.  The song was written by the Academy Award-winning song-writing duo of Richard M. Sherman and Robert B. Sherman.  The Sherman Brothers also wrote the majority of the well known Winnie the Pooh songs, such as "The Wonderful Thing about Tiggers" and "Heffalumps and Woozles" from the 1960s, and in 2000 wrote the score to "The Tigger Movie".

You're the Only You: You're the Only You is a song from the "Welcome to Pooh Corner" Cable TV series which premiered in 1983 on the Disney Channel (which was also that channel's inaugural season).  The song was written by the Academy Award-winning songwriting duo of Richard M. Sherman and Robert B. Sherman.  The Sherman Brothers also wrote most of the well known Winnie the Pooh songs, including "The Wonderful Thing about Tiggers" and "Heffalumps and Woozles" from the 1960s, and in 2000 wrote the score to "The Tigger Movie".

The Wonderful Thing About Tiggers: "The Wonderful Thing About Tiggers" is the theme song and personal anthem of Tigger, a fictional tiger from the children's book series Winnie-the-Pooh.  Although Tigger's birthday is believed to be in October 1928, the year that "The House at Pooh Corner" was first published, on Tigger-related merchandise, Disney often indicates Tigger's birth year as 1968, a reference to the first year that Tigger appeared in a Disney production, "Winnie the Pooh and the Blustery Day".  That was also the same instance when Tigger first sang this song.  The song is repeated in Disney's 1974 release "Winnie the Pooh and Tigger Too! ", The Many Adventures of Winnie the Pooh ride and then again in the 1977 release "The Many Adventures of Winnie the Pooh".  "The Wonderful Thing About Tiggers" opens up the 2000 release of "The Tigger Movie".  In 1974, Paul Winchell earned a Grammy for his rendition of the song.

Question: Which movie premiered in 2000, Pollyanna or The Tigger Movie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_comparison": {
      "type": "object",
      "properties": {
        "question_movie_1": {
          "type": "string",
          "description": "The first movie mentioned in the question."
        },
        "question_movie_1_release_year": {
          "type": "integer",
          "description": "The release year of the first movie."
        },
        "question_movie_2": {
          "type": "string",
          "description": "The second movie mentioned in the question."
        },
        "question_movie_2_release_year": {
          "type": "integer",
          "description": "The release year of the second movie."
        }
      },
      "required": [
        "question_movie_1",
        "question_movie_1_release_year",
        "question_movie_2",
        "question_movie_2_release_year"
      ],
      "additionalProperties": false
    },
    "movie_premiered_in_2000": {
      "type": "string",
      "description": "The movie from the question that premiered in 2000."
    },
    "answer_found": {
      "type": "boolean",
      "description": "Indicates if a definitive answer was found in the context."
    }
  },
  "required": [
    "movie_comparison",
    "movie_premiered_in_2000",
    "answer_found"
  ],
  "additionalProperties": false
}
