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
Rose in Paradise: "Rose in Paradise" is a song written by Stewart Harris and Jim McBride, and recorded by American country music artist Waylon Jennings.  It was released in January 1987 as the first single from the album "Hangin' Tough".  "Rose in Paradise" was Waylon Jennings' twelfth number one country single.  The single went to number one for one week and spent a total of nineteen weeks on the country chart.  Recording country artist Chris Young has a remake of the song as a duet with Willie Nelson from the album "The Man I Want to Be".

The Conversation (song): "The Conversation" is a single by American country music artists Waylon Jennings and Hank Williams Jr. Originally, the song was one of the tracks featured on Hank Williams Jr.'s 1979 Platinum selling album "Whiskey Bent and Hell Bound".  The track was included on Jennings' 1983 album "Waylon and Company", which consisted almost entirely of duets, and was released as the album's second radio single.  A music video was made to promote the single, a rarity for country music at the time.  It was the first for Jennings and the second for Williams, with his first being "Queen of My Heart".  The song was a moderately successful hit and reached number 15 on the "Billboard" Hot Country Singles & Tracks chart.

Ladies Love Outlaws (Waylon Jennings album): Ladies Love Outlaws is a country music album by Waylon Jennings, released on RCA Records in 1972.  Together with Jennings' previous album "Good Hearted Woman", it marks his transition toward his Outlaw Country image and style.  "Ladies Love Outlaws" coined the use of the term "Outlaw" to refer to the country music subgenre, which was developing at the time of its release.

Are You Sure Hank Done It This Way: "Are You Sure Hank Done It This Way" is a song written and performed by American country music artist Waylon Jennings.  It was released in August 1975 as the first single from the album "Dreaming My Dreams".  The song was Waylon Jennings' fourth number one on the country chart as a solo artist.  The single stayed at number one for one week and spent a total of sixteen weeks on the country chart.

The Days of Sand and Shovels: "The Days of Sand and Shovels" is a song written by Doyle Marsh and George Reneau, and recorded by American country music artist Waylon Jennings.  It was released in April 1969 as the second single from his album "The Best of Waylon Jennings".  The song peaked at number 20 on the "Billboard" Hot Country Singles chart.  It also reached number 1 on the "RPM" Country Tracks chart in Canada.

If Ole Hank Could Only See Us Now: "If Ole Hank Could Only See Us Now" is a song co-written and recorded by American country music artist Waylon Jennings.  It was released in January 1988 as the second single from the album "A Man Called Hoss".  The song reached number 16 on the "Billboard" Hot Country Singles & Tracks chart.  The song was written by Waylon Jennings, his son Shooter Jennings and Roger Murrah.

We Had It All (song): "We Had It All" is a song written by Troy Seals and Donnie Fritts and originally recorded by Waylon Jennings on his 1973 album, "Honky Tonk Heroes".  It has since been covered by many artists, including Rita Coolidge, Dobie Gray, Susan Jacks, Willie Nelson, Dolly Parton, the Rolling Stones, Bob Dylan (32 live performances in 1986), Rod Stewart, Tina Turner, Conway Twitty, Ray Charles, and Dottie West.

Out of the Ashes (Jessi Colter album): Out of the Ashes is the 11th and last studio album by American country music artist Jessi Colter, released 2006 on Shout!  Factory Records.  It was Colter's first album in 10 years, and her first country music album in 22 years since 1984's "Rock and Roll Lullaby."  It was also her first release since 1981 to chart on the Top Country Albums chart, where it reached #61.  It was the first album by Colter to be released following the death of her husband and country artist, Waylon Jennings.  The title of the album, "Out of the Ashes," explains the message that she has remained an artist without the help of Jennings.

Come with Me (Waylon Jennings song): "Come with Me" is a song written by Chuck Howard and recorded by American country music artist Waylon Jennings.  It was released in August 1979 as the first single from the album, "What Goes Around Comes Around".  "Come with Me" was Waylon Jennings' eighth No. 1 on the Country chart as a solo artist.  The single stayed at No. 1 for two weeks and spent a total of thirteen weeks on the Country chart.

Honky Tonk Heroes: Honky Tonk Heroes is a country music album by Waylon Jennings, released in 1973 on RCA Victor.  With the exception of "We Had It All", all of the songs on the album were written or co-written by Billy Joe Shaver.  The album is considered an important piece in the development of the outlaw subgenre in country music as it helped revive the honky tonk music of Nashville by injecting a rock and roll attitude.

Question: What was the country music album by Waylon Jennings, released in 1973 that had the song WE Had It All that was since covered by Rita Coolidge?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the country music album."
    },
    "artist": {
      "type": "string",
      "description": "The primary artist of the album."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    },
    "featured_song": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song featured on the album."
        },
        "original_album": {
          "type": "string",
          "description": "The album where the song was originally recorded."
        },
        "covered_by_artists": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of artists who have covered the song."
        }
      },
      "required": [
        "song_title",
        "original_album",
        "covered_by_artists"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_name",
    "artist",
    "release_year",
    "featured_song"
  ],
  "additionalProperties": false
}
