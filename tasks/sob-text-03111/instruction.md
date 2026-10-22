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
Make Me Smile: "Make Me Smile" is a song written by James Pankow for the rock band Chicago with the band's guitarist, Terry Kath, on lead vocals.  Part 1 of Pankow's 7-part "Ballet for a Girl in Buchannon" song cycle/suite, it was recorded for their second album, "Chicago" (often called "Chicago II"), which was released in 1970.

Feelin' Stronger Every Day: "Feelin' Stronger Every Day" is a song written by Peter Cetera and James Pankow for the group Chicago and recorded for their album "Chicago VI" (1973).  The first single released from that album, it reached #10 on the U.S. "Billboard" Hot 100.  Cetera played bass and sang lead vocals and keyboardist Robert Lamm played Hohner Pianet as well as acoustic piano.

Brand New Love Affair (song): "Brand New Love Affair," sometimes alternatively listed as "Brand New Love Affair (Parts I and II)", is a song written by James Pankow for the group Chicago and recorded for their album Chicago VIII.  The song peaked at #61 on the charts.  Guitarist Terry Kath sings the first half while bassist Peter Cetera sings the second half.  Keyboardist Robert Lamm played the distinctive Fender Rhodes electric piano on the song—the intro particularly showcases its lush vibrato bell-like sound.

Feelin' Satisfied: "Feelin' Satisfied" is a 1978 song written by Tom Scholz for the Boston band album "Don't Look Back".  Paul Grein of "Billboard" described the song as "an affectionate tribute to the power of music."  The same magazine later described the song as an "upbeat track which is totally rock 'n' roll," praising the "clear singing" and "fresh sounds."  Terry Hazlett of The "Observer-Reporter" described the song as an "innocent little [ditty]" which comes across like a "rock 'n' roll anthem." .  AXS contributor Bill Craig describes the lyrics as being about "the wonders of rock music."  Pete Bishop of "The Pittsburgh Press" claimed that it has "an infectious happy feel."  "Ultimate Classic Rock" critic Michael Gallucci described it as a "simple" song that, in common with many Boston songs, "celebrates rock 'n' roll."  Gallucci rated it Boston's 8th greatest song, particularly praising the effect from the hand claps during the refrain.  Paul Elliott rated it their 7th greatest song, commenting on its "sense of fun" as Scholz lets go of some of his usual control.

Old Days: "Old Days" is a song written by James Pankow for the group Chicago and recorded for their album "Chicago VIII" (1975), with lead vocals by Peter Cetera.  The second single released from that album, it reached #5 on the U.S. "Billboard" Hot 100 and #3 on the Easy Listening chart.

(I've Been) Searchin' So Long: "(I've Been) Searchin' So Long" is a song written by James Pankow for the group Chicago and recorded for their album "Chicago VII" (1974).  The first single released from that album, it reached number 9 on the U.S. "Billboard" Hot 100.  It also hit number 8 on the Adult Contemporary chart.  In Canada, the song peaked as high as number 5.

Just You 'n' Me: "Just You 'n' Me" is a song written by James Pankow for the group Chicago and recorded for their album "Chicago VI" (1973).  The lead vocals are sung by bassist Peter Cetera.

Colour My World (Chicago song): "Colour My World" is a song written by American musician James Pankow, one of the founding members of the rock/jazz fusion band Chicago.  Part of Pankow's "Ballet for a Girl in Buchannon" song cycle/suite, it was recorded for their second album "Chicago", also called "Chicago II" (1970).  Terry Kath sings the lead vocal, and Walter Parazaider performs the highly recognizable flute solo.

Chicago (band): Chicago is an American rock band formed in 1967 in Chicago, Illinois.  The self-described "rock and roll band with horns" began as a politically charged, sometimes experimental, rock band and later moved to a predominantly softer sound, generating several hit ballads.  The group had a steady stream of hits throughout the 1970s and 1980s.  Since at least 2008, "Billboard" has shown Chicago to be the "greatest of all time" American band in singles chart success, and since 2015, the "greatest of all time" American band in album chart success as well.  Chicago is one of the longest-running and most successful rock groups, and one of the world's best-selling groups of all time, having sold more than 100 million records.

Alive Again (Chicago song): "Alive Again" is a song written by James Pankow for the group Chicago and recorded for their album "Hot Streets" (1978), with Peter Cetera singing lead vocals.  The first single released from that album, it reached #14 on the U.S. "Billboard" Hot 100 chart.  In Canada, "Alive Again" spent two weeks at number 11.

Question: "Just You 'n' Me" is a song written by James Pankow for an American rock band that has sold more than how many records?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "writer_name": {
      "type": "string",
      "description": "The name of the person who wrote the song."
    },
    "band_info": {
      "type": "object",
      "properties": {
        "band_name": {
          "type": "string",
          "description": "The name of the band."
        },
        "is_american_band": {
          "type": "boolean",
          "description": "Indicates if the band is American."
        },
        "records_sold_millions": {
          "type": "integer",
          "description": "The number of records sold by the band, in millions."
        }
      },
      "required": [
        "band_name",
        "is_american_band",
        "records_sold_millions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "writer_name",
    "band_info"
  ],
  "additionalProperties": false
}
