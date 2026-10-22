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
The Who Tour 1966: The Who Tour 1966 was a series of performances and tours by The Who, supporting releases such as "My Generation" (album and single), "Substitute", "I'm a Boy", and "A Quick One".

Pete Townshend: Peter Dennis Blandford Townshend (born 19 May 1945) is an English musician, singer, songwriter, and multi-instrumentalist, best known as the lead guitarist, backing vocalist, and main songwriter for the rock band the Who.  His career with the Who spans over 50 years, during which time the band grew to be considered one of the most influential bands of the 20th century.

Louise Karlsson: Louise Karlsson (born April 26, 1974) is a former Swedish breaststroke and medley swimmer who competed in the 1992 and 1996 Summer Olympics.  She finished 8th on 200 m medley in the 1996 Summer Olympics.  She also held the world record on 100 m medley for about one year, with the time 1:01.03 in January 1997.

Boris the Spider: "Boris the Spider" is a song written by The Who's bass guitarist, John Entwistle.  It appears as the second track of their 1966 album "A Quick One".  This song is claimed to be Entwistle's first composition, and became a staple of live shows.  This song, along with "My Wife", "Heaven and Hell" and "The Quiet One", were Entwistle's biggest songs to perform live.  "The Quiet One" was written to replace this song and "My Wife", which Entwistle had become quite tired of singing.  Though this song was popular, it was not released as a single in the US and the UK.  In Japan, "Boris the Spider" was released as the B-side to "Whiskey Man" in 1967.

A Quick One: A Quick One is the second studio album by the English rock band The Who, released on 9 December 1966.  The album was also released under the title Happy Jack on Decca Records in April 1967 in the United States, where the song "Happy Jack" was a top 40 hit.

Happy Jack (song): "Happy Jack" is a song by the British rock band The Who.  It was released as a single in December 1966 in the UK, peaking at No. 3 in the charts.  It peaked at No. 1 in Canada.  It was also their first top 40 hit in the United States, where it was released in March 1967 and peaked at No. 24.  It was included on the American version of their second album, "Happy Jack", originally titled "A Quick One" in the UK.

The Who Tour 1967: The Who Tour 1967 was a series of performances and tours by The Who, supporting releases such as "A Quick One", "Pictures of Lily", and "The Who Sell Out".  1967 was the first year the group performed in North America.

Jan Jiskoot: Johannes "Jan" Jiskoot (born 3 March 1940 in Dordrecht) is a retired Dutch swimmer who won two medals in medley events at the 1962 European Aquatics Championships.  He also participated in the 1960 and 1964 Summer Olympics and was sixth in the 400 m medley.  He started as a backstroke swimmer, but then leaned more to butterfly and medley.  On 18 September 1962 he set the European 100 m batterfly record at 0:59:50, becoming the first European to swim 100 m butterfly within one minute.  Between 1960 and 1966 he was 14 times national champion and set more than 20 national records in various backstroke, butterfly and medley events.

A Quick One, While He's Away: "A Quick One, While He's Away" is a 1966 medley written by Pete Townshend and recorded by The Who for their second album "A Quick One".  The song also appears on the album "BBC Sessions".  In the performance on their "Live at Leeds" album Townshend calls the nine-minute "epic" track a "mini-opera" and introduces it as ""Tommy's" parents".

So Sad About Us: "So Sad About Us" is a 1966 song by British rock band The Who, first released on the band's second album "A Quick One".  Originally written for The Merseys, "So Sad About Us" has likely been covered more frequently than any other song on the album; according to the All Music Guide, it is "one of the Who's most covered songs".  Shaun Cassidy, Primal Scream, The Breeders, and most notably The Jam and Dexter Romweber Duo (with backup vocal by Mary Huff of Southern Culture on the Skids) are among the many artists who have recorded studio versions of the song.

Question: "A Quick One, While He's Away" is a 1966 medley written a musician who was born in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song in question."
    },
    "writer_details": {
      "type": "object",
      "properties": {
        "writer_name": {
          "type": "string",
          "description": "The name of the musician who wrote the song."
        },
        "writer_birth_year": {
          "type": "integer",
          "description": "The birth year of the musician."
        }
      },
      "required": [
        "writer_name",
        "writer_birth_year"
      ],
      "additionalProperties": false
    },
    "query_answer": {
      "type": "integer",
      "description": "The birth year of the musician who wrote the song, which is the answer to the question."
    }
  },
  "required": [
    "song_title",
    "writer_details",
    "query_answer"
  ],
  "additionalProperties": false
}
