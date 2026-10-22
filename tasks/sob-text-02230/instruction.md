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
The Wrong Girl: "The Wrong Girl" is a song written by Liz Rose and Pat McLaughlin, and recorded by American country music artist Lee Ann Womack.  It was released in February 2004 as the first and only single from her "Greatest Hits" album.  The song peaked at number 24 on the "Billboard" Hot Country Singles & Tracks.

Teardrops on My Guitar: "Teardrops on My Guitar" is a song by American singer-songwriter Taylor Swift.  The song was co-written by Swift, alongside Liz Rose and produced by Nathan Chapman with Swift's aid.  "Teardrops on My Guitar" was released on February 19, 2007 by Big Machine Records, as the second single from Swift's eponymous debut album (2006).  The song was later included on the international release of Swift's second studio album, "Fearless" (2008), and released as the second pop single from the album in the United Kingdom.  It was inspired by Swift's experience with Drew Hardwick, a classmate of hers for whom she had feelings.  He was completely unaware and continually spoke about his girlfriend to Swift, something she pretended to be endeared by.  Years afterwards, Hardwick appeared at Swift's house, but Swift rejected him.  Musically, the track is soft and is primarily guided by a gentle acoustic guitar.  Critics have queried the song's classification as country music, with those in agreement (such as Grady Smith of "Rolling Stone") citing the themes and narrative style as country-influenced and those opposed (such as Roger Holland of "PopMatters") indicating the pop music production and instrumentation lack traditional country elements.

Taylor Swift (album): Taylor Swift is the debut studio album by American singer-songwriter Taylor Swift, released on October 24, 2006, by Big Machine Records.  Swift was 16 years old at the time of the album's release and wrote its songs during her freshman year of high school.  Swift has writing credits on all of the album's songs, including those co-written with Liz Rose.  Swift experimented with several producers, ultimately choosing Nathan Chapman, who had produced her demo album.  Musically, the album is country music styled, and lyrically it speaks of romantic relationships, a couple of which Swift wrote from observing relationships before being in one.  Lyrics also touch on Swift's personal struggles in high school.

Picture to Burn: "Picture to Burn" is a song recorded by American singer-songwriter Taylor Swift.  It was co-written by Swift and Liz Rose, and produced by Nathan Chapman.  It was released on February 3, 2008 by Big Machine Records as the fourth single from Swift's eponymous studio album, "Taylor Swift" (2006).  It was inspired by the narcissistic and cocky nature of her former high school classmate and ex-boyfriend Jordan Alford with whom Swift never established a formal relationship.  In retrospect, Swift has stated that she has evolved on a personal level and as a songwriter, claiming she processed emotions differently since "Picture to Burn".  The song was chosen as a single based on the audience's reaction to it in concert.  Musically, the track is of the country rock genre with prominent usage of guitar, banjo, and drums.  The lyrics concern setting fire to photographs of a former boyfriend.

Like My Mother Does: "Like My Mother Does" is a song written by Nathan Chapman, Liz Rose, and Nikki Williams.  It was first recorded by American country artist Kristy Lee Cook from her 2008 album, "Why Wait".  It was later recorded and released as a single by country music singers Jesse Lee and Lauren Alaina in 2010 and 2011, respectively.  Alaina's recording became the first version of the song to chart; it debuted at number 49 on the U.S. "Billboard" Hot Country Songs chart, and later reached a peak of number 36 on the chart in October 2011.

Pam Rose: Pam Rose is an American country music songwriter.  In her career, she has been a member of the groups Calamity Jane and Kennedy Rose, both times pairing with fellow songwriter Mary Ann Kennedy.  Rose's co-writing credits include the Grammy Award-nominated songs "Ring on Her Finger, Time on Her Hands" by Lee Greenwood and "I'll Still Be Loving You" by Restless Heart.  Other songs that she has written include "Safe in the Arms of Love" by Martina McBride and "You Will" by Patty Loveless.

Liz Rose: Liz Rose (born in Dallas, Texas) is an American country music songwriter best known for her work with Taylor Swift.  She has co-written twenty of Swift's officially-released songs and singles, including "White Horse," "Teardrops on My Guitar," and "You Belong with Me," which won her and Swift a Grammy Award in 2010.

Songs About Rain: "Songs About Rain" is a song written by Pat McLaughlin and Liz Rose, and recorded by American country music artist Gary Allan.  It was released in November 2003 as the second single from his album "See If I Care".  The song peaked at number 12 on the U.S. "Billboard" Hot Country Singles & Tracks chart and at number 71 on the U.S. "Billboard" Hot 100 chart.

Jen Foster: Jennifer Kate Foster is an American singer-songwriter, musician, performer, record producer, and owner of her own record label, "Fosterchild Records."  Her music incorporates elements of rock, pop, r&b, folk, country and dance.  She has released 3 studio albums, 3 EP's and has contributed to various film, television and multi-media soundtracks and exceeded sales of 50, 000 units as an independent artist.  Foster has garnered a number of awards for her songwriting skills and has written with a number Nashville, Tennessee Music Row hit songwriter's including Pam Tillis ("Mi Vida Loca", "Spilled Perfume"),Jeffrey Steele ("What Hurts The Most", "My Wish"), Natalie Hemby ("Only Prettier", "White Liar"), Liz Rose ("Teardrops on My Guitar"), Mike Reid ("I Can't Make You Love Me"), Kristen Hall of Sugarland ("Baby Girl", "Stay"), Greg Barnhill ("Walkaway Joe"), Keith Follese ("Smile",“Lookin For a Good Time",“I Love You"),Rob Giles (The Rescues), Emily West ("I Hate You, I Love You", "Blue Sky")

Tim McGraw (song): "Tim McGraw" is the debut single and first published song recorded by American singer-songwriter Taylor Swift.  The song was written by Swift and Liz Rose, and produced by Nathan Chapman.  It was released on June 19, 2006 by Big Machine Records as Swift's debut single and the lead single from Swift's eponymous debut album.  Swift wrote "Tim McGraw" during her freshman year of high school, knowing that she and her senior boyfriend would break up at the end of the year when he left for college.  The song was written about all the different things that would remind the subject of Swift and their time spent together, once he departed.  "Tim McGraw" is a musical interconnection of traditional and modern country music.  Lyrically, the track lists items in order to associate a past relationship, one of them being country artist Tim McGraw's music.

Question: American country music songwriter Liz Rose, worked extensively with what singer-songwriter, on songs like Teardrops on My Guitar, release February 19, 2007?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "primary_artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the primary artist for the song."
        },
        "artist_type": {
          "type": "string",
          "description": "The type of artist, e.g., singer-songwriter."
        }
      },
      "required": [
        "name",
        "artist_type"
      ],
      "additionalProperties": false
    },
    "song_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the song."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the song."
        }
      },
      "required": [
        "title",
        "release_date"
      ],
      "additionalProperties": false
    },
    "songwriter_collaboration": {
      "type": "object",
      "properties": {
        "songwriter_name": {
          "type": "string",
          "description": "The name of the collaborating songwriter."
        },
        "collaboration_role": {
          "type": "string",
          "description": "The role of the songwriter in the collaboration, e.g., co-writer."
        },
        "total_songs_co_written_with_artist": {
          "type": "integer",
          "description": "The total number of songs co-written by the songwriter with the primary artist."
        }
      },
      "required": [
        "songwriter_name",
        "collaboration_role",
        "total_songs_co_written_with_artist"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "primary_artist",
    "song_details",
    "songwriter_collaboration"
  ],
  "additionalProperties": false
}
