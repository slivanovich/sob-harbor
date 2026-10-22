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
10 Hronia Mazi: 10 H.M. (Short for 10 Hronia Mazi, Greek: "10 Χρόνια Μαζί"; English: "10 Years Together") is an album released by Greek singer Despina Vandi starting on December 6, 2007.  It is her 12th album from the beginning of her career, and her 10th album with Phoebus.  It is also her first studio album of new material since her 2004 release of "Stin Avli Tou Paradisou".  The album is dedicated to the 10-year collaboration with Phoebus and features a track of the same name.  The album is a triple CD, with the first CD containing pop/rock songs, the second CD containing Modern Laika songs and third CD containing new remixes of older songs.  The album is completely written and produced by Phoebus and released by Heaven Music.  The main sponsor is WIND Hellas.

Forever Jolina: Forever is the 5th album of Jolina Magdangal.  It was her 2nd album released under GMA Records.

Discharge (album): Discharge is the fifth studio album by hardcore punk band Discharge released in 2002 on Sanctuary Records.  It is the final album with classic singer Cal Morris.

20:20 Vision: 20:20 Vision is the 5th live album and 20th album overall by Christian parody band ApologetiX.  The name of the album is a parody of the term "20/20 vision", a result of the album being the band's 20th album released on their 20th anniversary and that it contains 20 songs.

Kawaihae (band): Kawaihae is an island music band formed in the summer 2000 in Japan formed by Tokyo/Yokohama/Nagoya radio personality Vance K who was born and raised on the Big Island of Hawaii.  Since the band formed, they have released three albums and is currently working on a 4th album slated for release in 2009.  The band houses a large fanbase within Japan and Hawaii and has received the Group of the Year award at the 2004 Hawaii Music Awards.

Greatest Hits (Soul City): Greatest Hits is the first compilation album by American pop group The 5th Dimension, released in 1970 by Soul City.  It includes all but two of their charting singles to date: "Go Where You Wanna Go", their first Top 20 record in the USA, would appear on the follow-up compilation, The July 5th Album, released later that year, while "Another Day, Another Heartache" was not included in either compilation.  Greatest Hits and The July 5th Album were the final 2 album releases for Soul City Records' distribution deal with Liberty Records.  The 5th Dimension subsequently signed with Bell Records.

Discharge (band): Discharge are a British rock band formed in 1977 by Terence "Tezz" Roberts and Royston "Rainy" Wainwright.  While the band had substantial line-up changes over its history, the classic line-up from the early 1980s featured bassist Wainwright, drummer Gary Maloney, Anthony "Bones" Roberts playing guitar, and vocalist Kelvin "Cal" Morris.

The July 5th Album: The July 5th Album is the second compilation album by American pop group The 5th Dimension, released in 1970 by Soul City.  It is composed primarily of album tracks from amongst the group's four albums of original material for Soul City Records, many of which were B-sides to charting singles.  It also includes one A-side single: the group's cover of The Mamas & the Papas hit "Go Where You Wanna Go".  The song was originally intended to be the Mamas & the Papas first single but was replaced with the now-iconic "California Dreamin'".  Choosing that single, and seeing it become successful, became something of a mixed blessing for The 5th Dimension, as they were frequently referred to in the media as "The Black Mamas & the Papas", a label the group sought to escape while creating their own unique identity.

More Than Words (Mark 'Oh album): More than Words is the 5th album released by Mark 'Oh, and it was released on February 16, 2004, by Home Records GmbH.

P.O.A: Pop on Arrival: P.O.A.: Pop on Arrival is the 5th album released by Japanese band Beat Crusaders, and the 1st full-length album released under the DefSTAR Records Label.  It was released May 11, 2005.  Upon its release, there were two versions available, the Original Version and Limited Edition (初回生産限定盤; The first production limited board).  The Original features 14 tracks, while the Limited Edition includes Bonus Tracks "Get Up!  Get Up!"  and "Say Good-Night" which differentiate the order of tracks on either CD.

Question: Discharge is the 5th album released by the rock band formed in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album in question."
    },
    "album_number": {
      "type": "integer",
      "description": "The sequential number of the album in the band's discography."
    },
    "band_formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "band_name",
    "album_name",
    "album_number",
    "band_formation_year"
  ],
  "additionalProperties": false
}
