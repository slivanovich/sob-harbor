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
Livin' on the Fault Line: Livin' on the Fault Line is the seventh studio album by the American rock band The Doobie Brothers, released in 1977.  It is one of the few Doobie Brothers albums which did not produce a hit (although "You Belong to Me" was a hit as recorded by co-author Carly Simon).  Still, the album received modest critical acclaim.  Tom Johnston (guitar, vocals) left the band early in the sessions.  He is listed as part of the band (appearing in the inside group photo) but appears on little or none of the actual album; despite writing and singing five songs during the sessions for the album, they were not included on the final release.  Much of this consistently mellow album has a jazz tinge, and the influences of R&B are palpable throughout.  The track "Little Darling (I Need You)" is a remake of the Marvin Gaye 1966 hit.

Rockin' down the Highway: The Wildlife Concert: Rockin’ Down the Highway: The Wildlife Concert is the second double live album by American rock band The Doobie Brothers, released in 1996.  (see 1996 in music).  The concerts were performed to benefit the Wildlife Conservation Society, hence the album's title.

Farewell Tour (album): Farewell Tour is the first live album by American rock band The Doobie Brothers, released in 1983.  (See 1983 in music.)  It documents the group's 1982 Farewell Tour and is a double album set.

The Doobie Brothers: The Doobie Brothers are an American rock band from San Jose, California.  The group has sold more than 40 million albums worldwide throughout its career.  The band has been active for five decades, with their biggest success occurring in the 1970s.

Live at Wolf Trap: Live at Wolf Trap is the third live album by US rock band The Doobie Brothers, released in 2004.

Brotherhood (The Doobie Brothers album): Brotherhood is the eleventh studio album by American rock band The Doobie Brothers, released in 1991 (see 1991 in music).  It was their second and final album for Capitol.  It also marked the final appearances on a Doobie Brothers album by bassist Tiran Porter and original drummer John Hartman.

Hampton Comes Alive: Hampton Comes Alive is a six-disc live album by the American rock band Phish, released on November 23, 1999, by Elektra Records.  It is the band's third live album and the first time complete live Phish concerts were released in their entirety (though fan recordings of most Phish shows are widely circulated).  "Hampton Comes Alive" consists of two full concerts recorded on November 20 and 21, 1998, at the Hampton Coliseum in Hampton, Virginia.  The album title is a play on Peter Frampton's classic live album "Frampton Comes Alive! ".

The Doobie Brothers (album): The Doobie Brothers is the debut album by American rock band The Doobie Brothers, released in 1971 (see 1971 in music).  It is their only official studio album to feature original bass player Dave Shogren on all tracks, who left during the recording of their second album.  The album was re-released in 1974 on the Midi record label with colourised album artwork.

Minute by Minute: Minute by Minute is the eighth studio album by American rock band The Doobie Brothers, released in 1978.  The album contains their biggest hit, the Grammy-winning "What a Fool Believes," which was co-written by Kenny Loggins and simultaneously released on his 1978 album "Nightwatch".  "Depending on You" and the title track were also released as singles.  The album would be the last to include members Jeff "Skunk" Baxter and John Hartman.  It is also the most-honored Doobie Brothers album, having won four Grammys at the 22nd Grammy Awards, more than any other album.

You Belong to Me (Carly Simon song): "You Belong to Me" is a song written by American singer-songwriters Carly Simon and Michael McDonald.  Originally recorded by McDonald's rock group The Doobie Brothers for their seventh studio album, "Livin' on the Fault Line" (1977), the song was made famous by Simon herself when she recorded it for her seventh studio album, "Boys in the Trees" (1978).  Released as the album's lead single, her version reached the top ten of the "Billboard" Pop Singles chart, peaking at #6, and remained on the chart for 18 weeks.  Simon received a Grammy Award nomination for Best Pop Female Vocalist in 1979.  A live version of the song from The Doobie Brothers' 1983 album "Farewell Tour" would later chart on the Pop Singles chart at #79 in August 1983.

Question: Live at Wolf Trap, released in 2004, is the third live album by US rock band The Doobie Brothers, an American rock band from San Jose, in which US state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the rock band."
    },
    "band_origin": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the band originated."
        },
        "state": {
          "type": "string",
          "description": "The US state where the band originated."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "album_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the album mentioned in the question."
        },
        "release_year": {
          "type": "integer",
          "description": "The year the album was released."
        },
        "album_type": {
          "type": "string",
          "description": "The type of album (e.g., live album, studio album)."
        },
        "live_album_sequence_number": {
          "type": "integer",
          "description": "The sequential number of this live album for the band."
        }
      },
      "required": [
        "title",
        "release_year",
        "album_type",
        "live_album_sequence_number"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "band_origin",
    "album_details"
  ],
  "additionalProperties": false
}
