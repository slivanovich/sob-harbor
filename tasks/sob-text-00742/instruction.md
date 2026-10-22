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
Kaizers Orchestra: Kaizers Orchestra was a Norwegian alternative rock band formed on 1 January 2000.  They are notable for being among the first non-black metal Norwegian artists singing in their native language to become popular beyond Scandinavia.  To other Norwegians, the band is instantly recognizable both because of their unique, unpredictable style, and because of vocalist Ottesen's distinctive Jæren dialect, shared by four of the other band members.

Geir Zahl: Geir Zahl (born 19 May 1975) is a Norwegian musician.  He is known for playing guitar in the Norwegian rock group Kaizers Orchestra.  The band was founded by Geir Zahl and Janove Ottesen who had both played together in some other bands, namely Blod, snått & juling and gnom.  Geir Zahl is the composer and main vocalist on several songs, both on the recordings and live at concerts.

Rock music in Norway: Norway has produced a number of famous rock bands, including Titanic, a-ha and Kaizers Orchestra.

Fake Problems: Fake Problems is a four-piece indie rock from Naples, Florida.  They released their first full-length album, "How Far Our Bodies Go", on Sabot Productions on April 27, 2007.  Their second record, "It's Great to Be Alive", was released through Side One Dummy Records on February 17, 2009.  Their third record "Real Ghosts Caught On Tape" was released September 21, 2010, also on Sideonedummy.  They are currently on an indefinite hiatus.

Våre demoner: Våre demoner (English: Our Demons ) is the fifth studio album by Norwegian alternative rock group Kaizers Orchestra.  Recorded during early 2009, it was released in limited quantities on 27 April 2009.  Unlike their four previous albums, the material on "Våre demoner" consists of re-recorded versions of old material that was never released officially for various reasons.  The album's liner notes contain information about how the lyrics relate to one another within the "universe" of the band's songs as well as lyrics.

Øyvind Storesund: Øyvind Storesund (born March 9, 1975 in Bø i Telemark, Norway) is a Norwegian Rock and jazz musician (upright bass) known from playing in the Norwegian bands Cloroform and Kaizers Orchestra.

Live i Oslo Spektrum: Live i Oslo Spektrum is a live album released on CD, DVD and Blu-ray featuring Norwegian alternative rock band Kaizers Orchestra.  It features their concert at Oslo Spektrum in Oslo, Norway on 9 April 2011, the official celebration of Kaizers Orchestra's tenth anniversary.  The album is expected to be released on 11 November 2011 (coinciding with the release date of their eighth studio album, "Violeta Violeta Vol.  II", and the stage premiere of their musical, "Sonny").  The live CD of the same concert, bundled with both releases, omits a certain number of songs due to capacity constraints.

Janove Ottesen: Janove Ottesen (born Jan Ove Ottesen, 1975) is a Norwegian musician, born in Stord, Hordaland, Norway.  He specializes in vocals, guitar and barrels, and is a leading member of the Norwegian band Kaizers Orchestra.

Viva la Vega: Viva La Vega is a Live DVD featuring the Norwegian alternative rock band Kaizers Orchestra produced by the Norwegian company Amazon Film.  It features their concert at Vega in Copenhagen, Denmark on 6 October 2005, as well as documentaries, music videos, a biography, and stills.  The DVD features all the songs Kaizers recorded in 2005, whether as part of the concert itself or as background music for the extras.

Erlend Skomsvoll: Erlend Fredrik Skomsvoll (born 12 May 1969 in Bærum, Norway) is a Norwegian jazz musician (piano, keyboards, accordion, and tuba), band leader, composer and arranger, known from his own band Skomsork and the band Wibutee with Live Maria Roggen, Madrugada, and Kaizers Orchestra.  He has also cooperated with Nils Petter Molvær, Chick Corea and Pat Metheny.

Question: Are Fake Problems and Kaizers Orchestra from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bands_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string"
          },
          "origin_country": {
            "type": "string"
          }
        },
        "required": [
          "band_name",
          "origin_country"
        ],
        "additionalProperties": false
      }
    },
    "are_from_same_country": {
      "type": "boolean"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "bands_compared",
    "are_from_same_country",
    "reasoning"
  ],
  "additionalProperties": false
}
