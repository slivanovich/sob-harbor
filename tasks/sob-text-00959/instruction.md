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
Wendell Gee: "Wendell Gee" is a song by the American alternative rock band R.E.M., released as the third and final single from the group's third studio album "Fables of the Reconstruction" in 1985.  It was released in Europe only, in two 7" and two 12" formats.

Stand (R.E.M. song): "Stand" is a song by the American alternative rock band R.E.M., released as the second single from the album "Green" in 1989.  The song peaked at number six on the "Billboard" Hot 100, becoming R.E.M.'s second top 10 hit in the United States.  The song reached number 48 on the UK Singles Chart and number 16 in Canada.  It was placed on R.E.M.'s Warner Bros.  Records "best of" album "" in 2003.

Out of Time (album): Out of Time is the seventh studio album by American alternative rock band R.E.M., released on March 12, 1991 by Warner Bros.  Records.  With "Out of Time", R.E.M.'s status grew from that of a cult band to a massive international act.  The record topped the album sales charts in both the U.S. and the United Kingdom, spending 109 weeks on American album charts and enjoying two separate spells at the summit, and spending 183 weeks on the British charts and a single week at the top.  The album has sold over four and a half million copies in the U.S. and over 18 million copies worldwide.  The album won three Grammy Awards in 1992: one as Best Alternative Music Album, and two for the first single, "Losing My Religion."

Finest Worksong: "Finest Worksong" is the third and final single released from R.E.M.'s fifth studio album "Document".  It peaked at number 50 on the UK Singles Chart in April 1988, at the time the group's highest-charting single in the UK.

The Breeders discography: The discography of American alternative rock band The Breeders consists of four studio albums, one live album, three extended plays, ten singles and twelve music videos. Kim Deal, then-bassist of American alternative rock band the Pixies, formed The Breeders as a side-project with Tanya Donelly, guitarist of American alternative rock band Throwing Muses.  After recording a demo tape, The Breeders signed to the English independent record label 4AD in 1989.  Their debut studio album "Pod" was released in May 1990, but was not commercially successful.  After the revival of the Pixies and Throwing Muses in 1990, The Breeders became mostly inactive until the Pixies' breakup in 1993.  With a new lineup, The Breeders released their "Safari" EP in 1992, followed by their second studio album "Last Splash" in 1993.  "Last Splash" was The Breeders' most successful album; it peaked at number 33 on the United States "Billboard" 200 and was certified platinum by the Recording Industry Association of America in 1994.  The album spawned the band's most successful single, "Cannonball".  The single peaked at number 44 on the US "Billboard" Hot 100 and at number two on the "Billboard" Alternative Songs chart.

Drive (R.E.M. song): "Drive" is the lead single and first track from American alternative rock band R.E.M.'s eighth studio album "Automatic for the People" in 1992.  Although it was not as commercially successful as previous lead singles "Losing My Religion," "Stand," or "The One I Love" in the United States, it became R.E.M.'s then second biggest hit on the UK Singles Charts, peaking at #11.  It managed a peak of #28 on the "Billboard" Hot 100.  The song did hit number one on the Modern Rock Tracks and number two on the Mainstream Rock Tracks.

Reckoning (R.E.M. album): Reckoning is the second studio album by the American alternative rock band R.E.M., released on April 9, 1984 by I.R.S. Records.  Produced by Mitch Easter and Don Dixon, the album was recorded at Reflection Sound Studio in Charlotte, North Carolina, over 16 days in December 1983 and January 1984.  Dixon and Easter intended to capture the sound of R.E.M.'s live performances, and used binaural recording on several tracks.  Singer Michael Stipe dealt with darker subject matter in his lyrics, and water imagery is a recurring theme on the record.  Released to critical acclaim, "Reckoning" reached number 27 in the United States—where it was certified gold by the Recording Industry Association of America in 1991—and peaked at number 91 in the United Kingdom.

Document (album): Document is the fifth studio album by American alternative rock band R.E.M. It was released on September 1, 1987 a few months after their rarities collection "Dead Letter Office" appeared and is the last album of new material by the band released on the I.R.S. Records label.  It is the first album on which the band worked with producer Scott Litt.

Überlin: "Überlin" is a song by American alternative rock band R.E.M..  It was released as the second single from their fifteenth and final studio album "Collapse into Now" on January 25, 2011.

We All Go Back to Where We Belong: "We All Go Back to Where We Belong" is the final single from American alternative rock band R.E.M., released in 2011.  The song is the lead single from the band's final album, the career-spanning greatest hits compilation "Part Lies, Part Heart, Part Truth, Part Garbage 1982–2011".  The song was made available over the Internet on October 17, 2011.

Question: "Finest Worksong" is the third and final single, released from American alternative rock band R.E.M., and its fifth studio album, released on September 1, 1987?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_name": {
      "type": "string",
      "description": "The name of the song."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the album from which the song was released."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the album."
        },
        "studio_album_number": {
          "type": "integer",
          "description": "The sequential number of the studio album by the band."
        }
      },
      "required": [
        "album_title",
        "release_date",
        "studio_album_number"
      ],
      "additionalProperties": false
    },
    "single_details": {
      "type": "object",
      "properties": {
        "single_number": {
          "type": "integer",
          "description": "The sequential number of the single released from the album."
        },
        "is_final_single": {
          "type": "boolean",
          "description": "Indicates if this was the final single released from the album."
        }
      },
      "required": [
        "single_number",
        "is_final_single"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_name",
    "album_details",
    "single_details"
  ],
  "additionalProperties": false
}
