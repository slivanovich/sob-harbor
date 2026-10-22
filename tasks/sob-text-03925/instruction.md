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
Daydreaming (Radiohead song): "Daydreaming" is a song by the English rock band Radiohead and produced by Radiohead's longtime producer Nigel Godrich.  It is a piano ballad with ambient, electronic and orchestral elements, including strings arranged by Radiohead guitarist Jonny Greenwood.  Radiohead released it as download on 6 May 2016 as the second single from their ninth studio album "A Moon Shaped Pool", accompanied by a music video directed by Paul Thomas Anderson.

OK Computer: OK Computer is the third studio album by English alternative rock band Radiohead, released in 1997 on EMI subsidiaries Parlophone and Capitol Records.  The members of Radiohead self-produced the album with Nigel Godrich, an arrangement they have used for their subsequent albums.  Other than the song "Lucky", which was recorded in 1995, Radiohead recorded the album in Oxfordshire and Bath between 1996 and early 1997, mostly in the historic mansion St Catherine's Court.  The band made a deliberate attempt to distance themselves from the guitar-oriented, lyrically introspective style of their previous album, "The Bends".  "OK Computer"' s abstract lyrics, densely layered sound and eclectic range of influences laid the groundwork for Radiohead's later, more experimental work.

Ticker Tape: Ticker Tape Ltd. is an English record distribution vanity label, founded in 2011 by the English alternative rock band Radiohead to distribute all of their releases from "The King of Limbs" onwards.  Ticker Tape is a subsidiary of XL Recordings, the label Radiohead is signed to.  Radiohead are the only artists who will have music released on Ticker Tape, similar in style to Trent Reznor's label The Null Corporation.  The label's first release was Radiohead's "The King of Limbs", which has been certified Gold in England.  Ticker Tape releases are licensed to XL Recordings in the UK, TBD Records in the US and Hostess Entertainment in Japan.

Radiohead: The Best Of: Radiohead: The Best Of is the first compilation album by the English rock band Radiohead, released on 2 June 2008 by Parlophone Records in the United Kingdom and by Capitol Records in the United States.  The album contains various songs from their first six studio albums, recorded under Radiohead's record contract with EMI subsidiary labels Parlophone and Capitol.  The compilation only contains songs for which EMI held the publishing rights, and so contains no songs recorded after Radiohead's final studio album with EMI, "Hail to the Thief" (2003).

Kid A: Kid A is the fourth studio album by the English rock band Radiohead, released on 2 October 2000 by Parlophone.  On the verge of a breakdown after promoting Radiohead's 1997 album "OK Computer", songwriter Thom Yorke envisioned a radical change in direction.  Radiohead replaced their rock sound with synthesisers, drum machines, the ondes Martenot, string orchestras and brass instruments.  They incorporated influences from genres such as electronic music, krautrock, jazz, and 20th-century classical music.  They recorded "Kid A" with "OK Computer" producer Nigel Godrich in Paris, Copenhagen, Gloucestershire and their hometown Oxford, England.  The sessions produced over 20 tracks, and Radiohead split the work in two albums: "Kid A" and "Amnesiac".  The latter was released the following year.

Nigel Godrich: Nigel Timothy Godrich (born 28 February 1971) is an English record producer, recording engineer and musician.  He is best known for his work with the English rock band Radiohead, having produced all of their studio albums since "OK Computer" (1997); he has been dubbed the "sixth member" of the band, in an allusion to George Martin being called the "Fifth Beatle".  Godrich has also worked extensively with Radiohead singer Thom Yorke on his solo material, and is a member of the bands Atoms for Peace (with Yorke) and Ultraísta.  Other acts Godrich has worked with include Beck, Paul McCartney, U2, R.E.M. and Roger Waters.  He is the creator of the music webseries "From the Basement".

The Eraser: The Eraser is the debut solo album by Thom Yorke of the English alternative rock band Radiohead, released on 10 July 2006 on the independent label XL Recordings.  It was produced by longtime Radiohead producer Nigel Godrich.  The album comprises electronic music Yorke recorded during Radiohead's 2004 hiatus and between their 2005 rehearsals, and makes heavy use of original samples.

Radio Rewrite: Radio Rewrite is a 2012 work for instrumental ensemble by American composer Steve Reich (born 1936), inspired by two songs by British rock band Radiohead: "Jigsaw Falling into Place" and "Everything in Its Right Place".  The piece represents the first time that Reich has reworked material from western pop/rock music.  It has five movements, alternating fast and slow, and is scored for clarinet, flute, two violins, viola, cello, two vibraphones, two pianos and electric bass.  The work premiered in London, UK in 2013, performed by the London Sinfonietta, to a generally positive reception.  Much attention focused on the Radiohead material, with some reviewers praising how completely it is integrated, while others question whether Radiohead's style is suited to Reich's work.  Alarm Will Sound made the first recording of the piece for an album of the same name released on Nonesuch Records in 2014.

The National Anthem (Radiohead song): "The National Anthem" is a song by the English rock band Radiohead, and the third track from their fourth studio album, "Kid A".  The song is moored to a repetitive bassline, has a processed electronic production and develops in a direction influenced by jazz.  The song was written by Radiohead, who co-produced it with Nigel Godrich.  It has been played frequently at Radiohead concerts since the release of "Kid A" in 2000.  It received polarised reviews by critics.

Burn the Witch (Radiohead song): "Burn the Witch" is a song by the English rock band Radiohead, released on 3 May 2016 as the lead single from their ninth studio album "A Moon Shaped Pool" (2016).  Radiohead developed the song for over a decade, first working on it during the sessions for their fourth album, "Kid A" (2000).  It features a string section playing "col legno battuto", producing a percussive sound, arranged by Radiohead guitarist Jonny Greenwood.

Question: Who is best know for his work with the English rock band Radiohead and produced by Radiohead?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "primary_role": {
      "type": "string",
      "description": "The primary professional role of the person."
    },
    "associated_band": {
      "type": "string",
      "description": "The band the person is best known for working with."
    },
    "production_details": {
      "type": "string",
      "description": "Details about their production work for the associated band."
    },
    "notable_fact": {
      "type": "string",
      "description": "A notable fact or nickname associated with the person's work with the band."
    }
  },
  "required": [
    "person_name",
    "primary_role",
    "associated_band",
    "production_details",
    "notable_fact"
  ],
  "additionalProperties": false
}
