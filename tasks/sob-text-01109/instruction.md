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
Dare (album): Dare (released as Dare!  in the US) is the third studio album by British synthpop band The Human League.  The album was recorded between March and September 1981 and first released in the UK on 16 October 1981, then subsequently in the US in mid-1982.

Tell Me When: "Tell Me When" is a song by the British synthpop group the Human League.  Written jointly by lead singer Philip Oakey and Paul C. Beckett, it was recorded at 'Human League Studios', Sheffield in 1994.  The single and the "Octopus" album were produced by Ian Stanley (formerly of Tears for Fears).

All I Ever Wanted (The Human League song): "All I Ever Wanted" is a song by the British synthpop group The Human League.  It is taken from the "Secrets" album of 2001 and was released as its first single.  It is currently their most recent single released on a major label.  It follows the standard Human League style of baritone lead vocals of Philip Oakey with choruses and incidentals jointly shared between female co-vocalists Joanne Catherall and Susan Ann Sulley (credited for the first time under her married name, Gayle, causing some erroneous comment that 'Susan Sulley' had been replaced).  The meticulous joint production of Q, Kerry Hopwood and Dave Clayton produced a modern sounding electronica track that was critically well received.  It was released in July 2001 and stalled at number 47 in the UK Singles Chart.

The Things That Dreams Are Made Of: "The Things That Dreams Are Made Of" is a song by the English synthpop group The Human League.  It was originally recorded for the "Dare" album of 1981.  It was remixed, remastered and released as a dance EP single in 2008; partly to coincide with the 30th anniversary of the Human League, 26th anniversary of "Dare" and the band's Dare '07 tour.  It reached number two in the official UK Dance Chart in February 2008.

The Human League Video Single (1983): The Human League Video Single is a compilation of music videos by the British synthpop group The Human League, released on VHS and Betamax format tape, and marketed as a "video single," released in the UK in August 1983.

Don't You Want Me: "Don't You Want Me" is a single by British synthpop group The Human League, released on 27 November 1981 as the fourth single from their third studio album "Dare" (1981).

One Man in My Heart: "One Man in My Heart" is a song recorded by British synthpop band The Human League.  It was released as the second single from the band's album "Octopus".  A ballad, the song differs from all previous Human League tracks as the lead vocal is performed by a female member of the band, Susan Ann Sulley, with spoken word refrains from Philip Oakey and contrasting backing from the third Human League member Joanne Catherall.  Released on 6 March 1995 in the UK only, the song received positive reviews from music critics and eventually peaked at number thirteen in the UK Singles Chart, eventually spending 8 weeks in the charts.  In 2001 in "The Guardian" newspaper it was called one of the best love songs of the 1990s.

Love and Dancing: Love and Dancing is a remix album released by British synthpop band The Human League in 1982.  It was released under the name "The League Unlimited Orchestra" as a nod to Barry White's disco-era Love Unlimited Orchestra.  The album was principally the idea and work of producer Martin Rushent and contained remixes of songs from the band's multi-platinum selling album "Dare", along with a version of the track "Hard Times", which had originally been the B-side of the single "Love Action (I Believe in Love)".  It was conceived to take advantage of the unexpected huge success of "Dare" and also designed as a stopgap while the Human League worked on new material.

Octopus (The Human League album): Octopus is the seventh full-length studio album recorded by the British synthpop band The Human League.  It was produced by the former Tears for Fears keyboard player Ian Stanley and released by EastWest Records in 1995.  It was the first new album from The Human League in five years after the termination of their long-term contract with Virgin Records.  "Octopus" was the first Human League album which presented the band as a trio consisting of the singers Philip Oakey, Joanne Catherall and Susan Ann Sulley.  The former Human League member Jo Callis and keyboard player Neil Sutton also contributed to the writing of the album.

The Human League: The Human League are an English synth-pop band formed in Sheffield in 1977.  After signing to Virgin Records in 1979, the band released two albums and a string of singles before attaining widespread commercial success with their third album "Dare" in 1981.  The album contained four hit singles, including the UK/US number one hit "Don't You Want Me".  The band received the Brit Award for Best British Breakthrough Act in 1982.  Further hits followed throughout the 1980s and into the 1990s, including "Being Boiled", "Mirror Man", "Fascination", "The Lebanon", "Human" (a US No. 1) and "Tell Me When".

Question: The Human League are an English synth-pop band formed in Sheffield in 1977, the album contained four hit singles, including which UK/US number one hit, a single by British synthpop group The Human League, released on 27 November 1981 as the fourth single from their third studio album "Dare" (1981)?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_name": {
          "type": "string",
          "description": "The name of the studio album."
        },
        "album_release_year": {
          "type": "integer",
          "description": "The release year of the album."
        },
        "album_studio_position": {
          "type": "integer",
          "description": "The sequential number of the album as a studio album for the band."
        }
      },
      "required": [
        "album_name",
        "album_release_year",
        "album_studio_position"
      ],
      "additionalProperties": false
    },
    "single_details": {
      "type": "object",
      "properties": {
        "single_name": {
          "type": "string",
          "description": "The name of the single."
        },
        "single_release_date": {
          "type": "string",
          "description": "The release date of the single."
        },
        "single_from_album_position": {
          "type": "integer",
          "description": "The sequential number of the single released from the album."
        },
        "chart_performance": {
          "type": "string",
          "description": "The chart performance of the single."
        }
      },
      "required": [
        "single_name",
        "single_release_date",
        "single_from_album_position",
        "chart_performance"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band_name",
    "album_details",
    "single_details"
  ],
  "additionalProperties": false
}
