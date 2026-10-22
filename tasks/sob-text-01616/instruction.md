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
Come On Over (Shania Twain song): "Come On Over" is a song co-written and recorded by Canadian country music singer Shania Twain.  It was the ninth single to country radio and title track from her third studio album "Come On Over" (1997).  It was written by Twain and her then-husband, Robert John "Mutt" Lange.  "Come On Over" was originally released to North American country radio stations in September 1999.  The song went on to win a Grammy Award for Best Country Song in 2000.  "Come On Over" was included in the setlist of the Come On Over Tour, and in a medley during the Up!  Tour; it was also performed at the CMAs on September 29, 1999.  The song was later included in Twain's 2004 "Greatest Hits" album.

Superchunk: Superchunk is an American indie rock band from Chapel Hill, North Carolina, consisting of singer-guitarist Mac McCaughan, guitarist Jim Wilbur, bassist Laura Ballance, and drummer Jon Wurster.  Formed in 1989, they were one of the bands that helped define the Chapel Hill music scene of the 1990s.  Their energetic, high-velocity style and do-it-yourself ethics were influenced by punk rock.

Team (Lorde song): "Team" is a song by New Zealand singer Lorde, taken from her debut studio album, "Pure Heroine" (2013).  The song was released on 13 September 2013 as the album's third single in Australia and New Zealand by Universal Music New Zealand, and the second in the United States and the United Kingdom by Lava and Republic Records.  The track was written by Lorde and Joel Little and produced by Little, with additional production from Lorde herself.  "Team" is a hybrid of alternative pop and electro-hop featuring synthesiser, bass and snare drum instrumentation over a handclap-based beat.  Lyrically, the track is a "tribute to her friends and country".

Music of New Zealand: The music of New Zealand has been influenced by blues, jazz, country, rock and roll and hip hop, with many of these genres given a unique New Zealand interpretation.  A number of popular artists have gone on to achieve international success including Lorde, Split Enz, Crowded House, OMC, Bic Runga, Kimbra, Ladyhawke, The Naked and Famous, Fat Freddy's Drop, Savage, Flight of the Conchords, and Brooke Fraser.

I Was Totally Destroying It: I Was Totally Destroying It is a five-piece powerpop band from Chapel Hill, North Carolina, featuring current and former members of Saddle Creek band Sorry About Dresden.  After self-releasing and touring the country behind their first full-length album, the band signed with Portland-based indie label Greyday Records.  Since forming in 2007, the band has toured much of the country, playing with artists such as Conor Oberst and the Mystic Valley Band, Motion City Soundtrack, Cursive, Superchunk, Portastatic, Ryan Ferguson (formerly of No Knife), Dear and the Headlights, Margot & the Nuclear So and So's, Snowden, Billy Bragg, Annuals, Joan Jett, The Actual, Ozma, Polvo, Birds of Avalon and Blankface.  Their next full-length, Horror Vacui, was released by Greyday in October 2009, and was co-produced by Josh Cain of Motion City Soundtrack.

Come Pick Me Up: Come Pick Me Up is the seventh studio album by American indie rock band Superchunk, released in 1999.  It is marked by the presence of co-producer Jim O'Rourke, a well-known figure in underground circles.  Superchunk drummer Jon Wurster said that O'Rourke was selected because the band wanted someone "coming from a different head-space."  O'Rourke helped the band decorate the album with string and horn touches that were not typical of their guitar-based sound.  One of the horn players who appeared on the album is another well-known figure in underground circles, Shellac's Bob Weston.

Lorde: Ella Marija Lani Yelich-O'Connor (born 7 November 1996), better known by her stage name Lorde ( ), is a New Zealand singer-songwriter and record producer.  Born in Takapuna and raised in Devonport, Auckland, she became interested in performing as a child.  In her early teens, she signed with Universal Music Group and was later paired with songwriter and record producer Joel Little.  At the age of sixteen, she released her first extended play, "The Love Club EP" (2012), reaching number two on the national record charts in both New Zealand and Australia.

Clara Villarosa: Clara Villarosa is an American entrepreneur, author, publisher and motivational speaker.  She is the co-founder of Villarosa Media and was the founder of Hue-Man Bookstores in Denver, Colorado and Harlem, New York, one of the highest earning African-American bookstores in the country from the 1980s to the 2010s.  Her book, "Down to Business: The First 10 Steps to Entrepreneurship for Women" was nominated for a NAACP Image Award.  Villarosa founded the African American Booksellers Association.  In January 2016, she co-founded Villarosa Media with her daughters, Linda and Alicia Villarosa.  The company focuses on publishing new books from established black authors and classic books reissued in digital formats with print on demand (POD) capability.  Its first published book was "The Wind Is Spirit: The Life, Love and Legacy of Audre Lorde".  In 2016, she was featured in the film, "Dream, Girl".

Here's Where the Strings Come In: Here's Where the Strings Come In is the fifth studio album by American indie rock band Superchunk.  It was recorded at Fort Apache Studios from May 25 to June 4, 1995.  The album was released by Merge Records on September 19, 1995.

Swingin Party: "Swingin Party" is a song written by Paul Westerberg and recorded by his band The Replacements for their fourth studio album "Tim" (1985).  The song is an indie rock and rock and roll ballad with influences from jazz, country and new wave.  Lyrically, it portrays the protagonist's "feigned nonchalance".  It was well received by music critics, who praised Westerberg's songwriting talent.  The song has been covered by other artists, notably Kindness in 2009 and Lorde in 2013.

Question: Do Superchunk and Lorde come from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artists": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the artist or band."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin for the artist or band."
          }
        },
        "required": [
          "name",
          "origin_country"
        ],
        "additionalProperties": false
      },
      "description": "A list of artists and their respective origin countries."
    },
    "are_from_same_country": {
      "type": "boolean",
      "description": "True if both artists are from the same country, false otherwise."
    },
    "comparison_reasoning": {
      "type": "string",
      "description": "Explanation of why the artists are or are not from the same country."
    }
  },
  "required": [
    "artists",
    "are_from_same_country",
    "comparison_reasoning"
  ],
  "additionalProperties": false
}
