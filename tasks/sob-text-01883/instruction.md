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
Sinner (Drowning Pool album): Sinner is the debut studio album by American rock band Drowning Pool.  The album is the band's most popular album, being certified platinum in the same year that it was released in.  This was due at least in part to "Bodies" which remains the band's most well-known song.  This is the only studio album by the band to feature original lead singer Dave Williams.  While touring in support of "Sinner", he died on August 14, 2002 from cardiomyopathy.  The album debuted at #14 on the "Billboard" 200 chart.  Drowning Pool released a reissue of the album called the "Unlucky 13th Anniversary Edition" in 2014.  The album was put at no. 25 on Metal Descent's list "The 25 Best Alternative Metal Albums".

Oracular Spectacular: Oracular Spectacular is the debut album by American psychedelic rock band MGMT, released on October 2, 2007 by RED Ink and physically on January 22, 2008 by Columbia.  It was produced by Dave Fridmann and is the band's first release of new content, being recorded from March to April 2007.  The album was promoted with three singles: "Time to Pretend", "Electric Feel" and "Kids".  Both "Time to Pretend" and "Kids" were re-recorded for the album songs from the band's previous release "Time to Pretend" (2005), with the opening track serving as a "mission statement" and the theme continued through the album's subsequent tracks.

Time to Pretend (EP): Time to Pretend is the second EP by the American rock band MGMT, released on August 30, 2005 by Cantora Records and made available on iTunes.  New versions of the tracks "Time to Pretend" and "Kids" were later released on MGMT's debut album "Oracular Spectacular" (2007–2008).  At the time this was recorded they were still known as "The Management".

We (Don't) Care: We (Don't) Care is the first release by the American rock band The Management (now known as MGMT).  Newer versions of the tracks "Love Always Remains" and "Kids" were later released on MGMT's Cantora Records release "Time to Pretend" EP (2005) and additional versions of "Kids" appear on both their major-label debut "Oracular Spectacular" (2007–2008) and their demo album "Climbing to New Lows" (2005) recorded shortly after this EP.  Additionally, "We Care", "We Don't Care" and "Grutu (Just Becuz)" were also included on "Climbing to New Lows".

Congratulations (album): Congratulations is the second studio album by American rock band MGMT, first self-released through MGMT's website on March 20, 2010 with a general release following on April 13, 2010 by Columbia Records.  The album marks a departure from the synthpop style that first brought the band acclaim on their debut studio album "Oracular Spectacular" and features a more psychedelic, progressive and guitar-driven sound.  MGMT began writing the tracks that would ultimately appear on "Congratulations" in early 2009.  They eventually headed to a Malibu studio to work on the album, with producer Peter Kember (Sonic Boom), an ex-member of Spacemen 3, where vocal contributions from Royal Trux singer Jennifer Herrema were also recorded for the album.  VanWyngarden has stated that the album is influenced by the band's massive rise in popularity since "Oracular Spectacular'"s release.  "It's us trying to deal with all the craziness that's been going on since our last album took off.  Sometimes it just doesn't feel natural".

Kids (MGMT song): "Kids" is a song by the American rock band MGMT, released as the third and final single from their debut studio album "Oracular Spectacular" (2007) on October 13, 2008.  The version of the song that appears on "Oracular Spectacular" is updated from earlier versions that appear on the band's EPs "Time to Pretend" (2005) and "We (Don't) Care" (2004).  A track entitled "Kids (Afterschool Dance Megamix)" appears on the album "Climbing to New Lows" (2005).  On December 1, 2009, the track was announced as a nominee at the 52nd Grammy Awards in the category Best Pop Performance by a Duo or Group with Vocals.

Electric Feel: "Electric Feel" is a song by the American rock band MGMT, released as the second single from their debut studio album "Oracular Spectacular" (2007) on June 23, 2008.  The single was released as a 7" and CD single, and later on 12" vinyl.  "Electric Feel" was released to radio on July 29, 2008.  The song's second video features The Rock-afire Explosion.  The song is primarily in 6/4, with an instrumental bridge in 4/4.

Time to Pretend: "Time to Pretend" is a song by the American indie band MGMT, released as the lead single from their debut studio album "Oracular Spectacular" (2007) on March 3, 2008.  An earlier version had been released on their "Time to Pretend" EP.  The single was released as a 7" and CD single featuring the B-sides "Weekend Wars" (BBC Radio 1 Session) and "Metanoia", respectively.  In early 2009, the song was re-released in the UK.  The song was ranked at number 493 on "Rolling Stone"' s list of The 500 Greatest Songs of All Time.  The song was ranked at number 90 on "NME"' s list of The 500 Greatest Songs of All Time.

Andrew VanWyngarden: Andrew Wells VanWyngarden (born February 1, 1983) is an American musician.  He is the lead vocalist, guitar player and songwriter for the band MGMT, praised for (according to "Interview Magazine") "an uncanny knack for producing pop music that sounds as if it were filtered through a kaleidoscope."  One of his (and MGMT cofounder Benjamin Goldwasser's) songs "Kids" (from the "Oracular Spectacular" album) received a nomination for the Grammy Award for Best Pop Performance by a Duo or Group with Vocals, while the duo was nominated in the Best New Artist category.

MGMT: MGMT is an American psychedelic rock band formed in 2002 at Wesleyan University.  It currently consists of Andrew VanWyngarden (lead vocals, guitar, keyboards, bass guitar, drums, percussion) and Ben Goldwasser (vocals, keyboards, guitar, percussion).  In the live lineup it consists of VanWyngarden, Goldwasser, Will Berman (drums, percussion, harmonica, backing vocals), Matt Asti (bass guitar, backing vocals), James Richardson (lead guitar, keyboards, backing vocals) and Hank Sullivant (guitar, keyboards).

Question: Who is the lead singer of a rock band that created an album called "Oracular Spectacular?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album mentioned in the question."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that created the album."
    },
    "band_genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "lead_singer_name": {
      "type": "string",
      "description": "The name of the lead singer of the band."
    }
  },
  "required": [
    "album_name",
    "band_name",
    "band_genre",
    "lead_singer_name"
  ],
  "additionalProperties": false
}
