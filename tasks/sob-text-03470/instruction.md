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
Metaphysical Graffiti: Metaphysical Graffiti is the fifth studio album by The Dead Milkmen, released by Enigma Records in 1990.  The album title and cover art parody the 1975 album "Physical Graffiti" by Led Zeppelin.  Two tracks ("Do the Brown Nose" and "If You Love Somebody, Set Them on Fire") appeared on "Death Rides a Pale Cow".

Kashmir (song): "Kashmir" is a song by the English rock band Led Zeppelin.  Included on their sixth album "Physical Graffiti" (1975), it was written by Jimmy Page and Robert Plant (with contributions from John Bonham) over a period of three years with lyrics dating to 1973.  The song became a concert staple, performed by the band at almost every concert after its release.  The song has been described as one of Led Zeppelin's two most overtly progressive epics.

Physical Graffiti: Physical Graffiti is the sixth studio album by the English rock band Led Zeppelin, released as a double album on 24 February 1975 by their newly founded imprint label Swan Song Records.  The band wrote and recorded eight new songs for the album at Headley Grange, which stretched the total time of the record beyond the typical length of a single LP, so the band decided to make "Physical Graffiti" a double album by including unreleased tracks from earlier recording sessions: one outtake from "Led Zeppelin III," three from "Led Zeppelin IV," and three from "Houses of the Holy", including the unused title track from the latter album.

Led Zeppelin IV: The untitled fourth studio album by English rock band Led Zeppelin, commonly known as Led Zeppelin IV, was released on 8 November 1971 by Atlantic Records.  Produced by guitarist Jimmy Page, it was recorded between November 1970 and January 1971 at several locations, most prominently the Victorian house Headley Grange.

Black Country Woman: "Black Country Woman" is the fourteenth song on English rock band Led Zeppelin's 1975 album "Physical Graffiti".  It was originally intended to be part of the "Houses of the Holy" album, which had been released two years earlier.

The Firm (album): The Firm is the first studio album by the British rock band The Firm, released by Atlantic Records on 11 February 1985.  Tracks ranged from the epic "Midnight Moonlight" based on a previously unreleased song by Led Zeppelin called "Swan Song", first tinkered with during the "Physical Graffiti" sessions, to the commercially successful "Radioactive".  "Closer" employs a horn section to subtle effect.  It also includes the Righteous Brothers' hit "You've Lost That Lovin' Feelin'" with the fretless bass sound of Tony Franklin.

Trampled Under Foot: "Trampled Under Foot" is a song by English rock group Led Zeppelin, featured on their 1975 album "Physical Graffiti".

Ass (album): Ass is the fourth studio album by British rock band Badfinger, and their last album released on Apple Records.  The opening track, "Apple of My Eye", refers to the band leaving the label to begin its new contract with Warner Bros.  Records.  The cover artwork, showing a donkey chasing a distant carrot, alludes to Badfinger's feelings that they had been misled by Apple over the years.  The cover was painted by Grammy Award-winning artist Peter Corriston, who would later create album covers for Led Zeppelin ("Physical Graffiti") and the Rolling Stones ("Some Girls", "Tattoo You").

Custard Pie: "Custard Pie" is the opening track on the English rock band Led Zeppelin's sixth album, "Physical Graffiti", released in 1975.

The Little Red Record: The Little Red Record is a EP by the country rock band the Ozark Mountain Daredevils.  The 33⅓ rpm record was packaged and included with "The Car Over the Lake Album".  It contains three outtakes from the prolific "It'll Shine When It Shines" sessions.

Question:  Physical Graffiti included three outtakes the album released on what date in 1971?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "source_album_name": {
      "type": "string",
      "description": "The name of the album from which outtakes were included."
    },
    "source_album_release_date": {
      "type": "object",
      "properties": {
        "day": {
          "type": "integer",
          "description": "The day of release for the source album."
        },
        "month": {
          "type": "string",
          "description": "The month of release for the source album."
        },
        "year": {
          "type": "integer",
          "description": "The year of release for the source album."
        }
      },
      "required": [
        "day",
        "month",
        "year"
      ],
      "additionalProperties": false
    },
    "number_of_outtakes": {
      "type": "integer",
      "description": "The number of outtakes from the source album included in the destination album."
    },
    "destination_album_name": {
      "type": "string",
      "description": "The name of the album that included the outtakes."
    }
  },
  "required": [
    "source_album_name",
    "source_album_release_date",
    "number_of_outtakes",
    "destination_album_name"
  ],
  "additionalProperties": false
}
