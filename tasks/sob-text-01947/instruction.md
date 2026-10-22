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
You Belong with Me: "You Belong with Me" is a song performed by American singer-songwriter Taylor Swift.  The song was co-written by Swift and Liz Rose and produced by Nathan Chapman with Swift's aid.  It was released on April 18, 2009, by Big Machine Records as the third single from Swift's second studio album, "Fearless" (2008).  Swift was inspired to write "You Belong with Me" after overhearing a male friend of hers arguing with his girlfriend through a phone call; she continued to develop a story line afterward.  The song contains many pop music elements and its lyrics have Swift desiring an out-of-reach love interest.

Teardrops on My Guitar: "Teardrops on My Guitar" is a song by American singer-songwriter Taylor Swift.  The song was co-written by Swift, alongside Liz Rose and produced by Nathan Chapman with Swift's aid.  "Teardrops on My Guitar" was released on February 19, 2007 by Big Machine Records, as the second single from Swift's eponymous debut album (2006).  The song was later included on the international release of Swift's second studio album, "Fearless" (2008), and released as the second pop single from the album in the United Kingdom.  It was inspired by Swift's experience with Drew Hardwick, a classmate of hers for whom she had feelings.  He was completely unaware and continually spoke about his girlfriend to Swift, something she pretended to be endeared by.  Years afterwards, Hardwick appeared at Swift's house, but Swift rejected him.  Musically, the track is soft and is primarily guided by a gentle acoustic guitar.  Critics have queried the song's classification as country music, with those in agreement (such as Grady Smith of "Rolling Stone") citing the themes and narrative style as country-influenced and those opposed (such as Roger Holland of "PopMatters") indicating the pop music production and instrumentation lack traditional country elements.

Picture to Burn: "Picture to Burn" is a song recorded by American singer-songwriter Taylor Swift.  It was co-written by Swift and Liz Rose, and produced by Nathan Chapman.  It was released on February 3, 2008 by Big Machine Records as the fourth single from Swift's eponymous studio album, "Taylor Swift" (2006).  It was inspired by the narcissistic and cocky nature of her former high school classmate and ex-boyfriend Jordan Alford with whom Swift never established a formal relationship.  In retrospect, Swift has stated that she has evolved on a personal level and as a songwriter, claiming she processed emotions differently since "Picture to Burn".  The song was chosen as a single based on the audience's reaction to it in concert.  Musically, the track is of the country rock genre with prominent usage of guitar, banjo, and drums.  The lyrics concern setting fire to photographs of a former boyfriend.

Fearless (Taylor Swift song): "Fearless" is a country pop song performed by American singer-songwriter Taylor Swift.  The song was co-written by Swift in collaboration with Liz Rose and Hillary Lindsey and produced by Nathan Chapman and Swift.  "Fearless" was released on January 3, 2010 by Big Machine Records as the fifth and final single from Swift's second studio album of the same name (2008).  Swift composed the song while traveling on tour to promote her eponymous debut album, "Taylor Swift" (2006).  She wrote "Fearless" in regard to the fearlessness of falling in love and eventually titled her second studio album after the song.  Musically, it contains qualities commonly found in country pop music and, lyrically, is about a perfect first date.

Liz Rose: Liz Rose (born in Dallas, Texas) is an American country music songwriter best known for her work with Taylor Swift.  She has co-written twenty of Swift's officially-released songs and singles, including "White Horse," "Teardrops on My Guitar," and "You Belong with Me," which won her and Swift a Grammy Award in 2010.

Fearless (Taylor Swift album): Fearless is the second studio album by the American singer-songwriter Taylor Swift.  The album was released on November 11, 2008, by Big Machine Records.  As with her first album, "Taylor Swift", Swift wrote or co-wrote all thirteen tracks on "Fearless".  Most of the songs were written as the singer promoted her first album as the opening act for numerous country artists.  Due to the unavailability of collaborators on the road, eight songs were written by Swift.  Other songs were co-written with Liz Rose, Hillary Lindsey, Colbie Caillat, and John Rich.  Swift also made her debut as a record producer, co-producing all songs on the album with Nathan Chapman.

Taylor Swift (album): Taylor Swift is the debut studio album by American singer-songwriter Taylor Swift, released on October 24, 2006, by Big Machine Records.  Swift was 16 years old at the time of the album's release and wrote its songs during her freshman year of high school.  Swift has writing credits on all of the album's songs, including those co-written with Liz Rose.  Swift experimented with several producers, ultimately choosing Nathan Chapman, who had produced her demo album.  Musically, the album is country music styled, and lyrically it speaks of romantic relationships, a couple of which Swift wrote from observing relationships before being in one.  Lyrics also touch on Swift's personal struggles in high school.

Tim McGraw (song): "Tim McGraw" is the debut single and first published song recorded by American singer-songwriter Taylor Swift.  The song was written by Swift and Liz Rose, and produced by Nathan Chapman.  It was released on June 19, 2006 by Big Machine Records as Swift's debut single and the lead single from Swift's eponymous debut album.  Swift wrote "Tim McGraw" during her freshman year of high school, knowing that she and her senior boyfriend would break up at the end of the year when he left for college.  The song was written about all the different things that would remind the subject of Swift and their time spent together, once he departed.  "Tim McGraw" is a musical interconnection of traditional and modern country music.  Lyrically, the track lists items in order to associate a past relationship, one of them being country artist Tim McGraw's music.

Our Song (Taylor Swift song): "Our Song" is a country song performed by American singer-songwriter Taylor Swift.  The song was written by Swift and produced by Nathan Chapman.  It was released on September 9, 2007 by Big Machine Records as the third single from Swift's eponymous debut album, "Taylor Swift" (2006).  Swift solely composed "Our Song" for the talent show of her freshman year in high school, about a boyfriend who she did not have a song with.  It was included on "Taylor Swift" as she recalled its popularity with her classmates.  The uptempo track is musically driven mainly by banjo and lyrically describes a young couple who use the events in their lives in place of a regular song.

White Horse (Taylor Swift song): "White Horse" is a song performed by American singer-songwriter Taylor Swift.  The song was written by Swift and Liz Rose and produced by Nathan Chapman, with Swift's aid.  The song was released on December 7, 2008 by Big Machine Records, as the second single from Swift's second studio album "Fearless" (2008).  Swift and Rose composed the song about one of Swift's ex-boyfriends, when Swift discovered he was not what she had perceived of him.  It focused on the moment where Swift accepted that the relationship was over.  "White Horse" is, musically, a country song and uses sparse production to emphasize vocals.  Lyrically, the track speaks of disillusionment and pain in a relationship, drawing references to fairytales.

Question: Liz Rose, is an American country music songwriter best known for her work with Taylor Swift, and  has co-written twenty of Swift's officially-released songs and singles, including which song was written by Swift and Liz Rose and produced by Nathan Chapman, with Swift's aid?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_name": {
      "type": "string",
      "description": "The title of the song."
    },
    "writers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of individuals credited as songwriters."
    },
    "producers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of individuals credited as producers."
    },
    "swift_production_aid": {
      "type": "boolean",
      "description": "Indicates if Taylor Swift aided in the production of the song."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album the song is from."
    },
    "record_label": {
      "type": "string",
      "description": "The record label that released the song."
    }
  },
  "required": [
    "song_name",
    "writers",
    "producers",
    "swift_production_aid",
    "album_title",
    "record_label"
  ],
  "additionalProperties": false
}
