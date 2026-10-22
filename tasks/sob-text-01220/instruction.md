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
The Nostalgia Factory: The Nostalgia Factory, subtitled "...and other tips for amateur golfers", is the second album to be released by Steven Wilson under the name 'Porcupine Tree'.  It was the second full-length cassette produced for his 'joke' project with friend Malcom Stocks.  The album was issued by Delerium in 1991 (despite the Porcupine Tree website stating 1990) in a limited edition of 300 copies.  Like its predecessor, the tracks from "The Nostalgia Factory" were subsequently released in the band's first studio album "On the Sunday of Life", and the compilation album "Yellow Hedgerow Dreamscape".  Some tracks have been renamed and/or rearranged in later albums and performances.

Atlanta (album): Atlanta is a download only double-live album by British progressive rock band Porcupine Tree recorded at the Roxy Theatre, Atlanta, United States on 29 October 2007.  The show recording was initially intended for a prospective Porcupine Tree live album, but this decision was later turned down as development of the "Anesthetize" DVD project began.  In the wake of the news regarding Mick Karn's advanced stage cancer, the band decided to put it out as a downloadable item from the Burning Shed online store at a very cheap cost, as a . RAR file split in two parts, all in MP3 format at 320kbit/s with completely printable artwork designed by Carl Glover.  The profits from the "Atlanta" downloads are intended to help Mick pay his treatment.  A 24-bit FLAC version was released in August 2010; profits from this version go to the Teenage Cancer Trust.  Since the album's artwork and mix is set up for two CDs it is widely considered to be a double album.  The album has a somewhat similar track listing to the "Anesthetize" DVD but includes the first official live recording of the track "A Smart Kid" and some of the songs that were performed at the shows for the Anesthetize shoot, but left out as they were already available on previous live releases (Open Car and Blackest Eyes).

Tarquin's Seaweed Farm: Tarquin's Seaweed Farm, subtitled "Words from a Hessian Sack", is the first album to be released by Steven Wilson under the name "Porcupine Tree".  It was originally a compiled cassette of experimental music made by Steven Wilson for his joke band he formed with his friend Malcom Stocks.  The cassette was only sent out to a few people, but was enough to give the band a bit of fame in the UK underground music scene of the time, being picked up by the underground magazine Freakbeat.  It was later released under Delerium Records in 1991 in a limited edition of 300 copies.  Eventually, the tracks from this and the later Porcupine Tree album "The Nostalgia Factory" were compiled into what are considered Porcupine Tree's first true studio albums, "On the Sunday of Life" and "Yellow Hedgerow Dreamscape".

We Lost the Skyline: We Lost the Skyline (also known as Transmission 7.1) is a live recording by Porcupine Tree, recorded during an in-store performance at Park Avenue CDs in Orlando, Florida, with 200 fans in attendance.  Although it was originally planned that the full band would play, lack of space dictated that only the two guitarists/singers Steven Wilson and John Wesley did.  This one-off performance was captured by a remote recording facility and the complete 8 song, 33 minute show is now being released in a mail order only CD, but the band are currently negotiating a low-key release for the CD through a number of independent stores in the USA that have supported Porcupine Tree over the last few years (including Park Avenue CDs itself).  However, the CD was released in Poland in small quantity.

XM (album): XM (also known as Transmission 1.1 and Transmission 1.2) is a live-in-studio album recorded by British band Porcupine Tree in early 2003 as a live album of mostly "In Absentia" tracks.  This was taken from a session at XM Satellite Radio in Washington D.C. on 12th November 2002, and was originally released as a limited edition tour album.  It was later released online on the Porcupine Tree store.

The Accidentals: The Accidentals are an American musical band, formed in Traverse City, Michigan, United States in 2012, by Savannah Buist and Katie Larson.  Currently the band includes the founders and musician Michael Dause, added in 2014.  The group features an eclectic blend of indie folk, pop, jazz, bluegrass, rock, classical and other genres, utilizing a wide variety of instruments that reflect the group's orchestral roots and electronic influences.

Anesthetize (Porcupine Tree): Anesthetize is the second live DVD by progressive rock band Porcupine Tree, released on 20 May 2010.  The Blu-ray edition was released on 15 June.  It is filmed in high definition and taken from two concerts given by Porcupine Tree at Tilburg, Netherlands on 15 and 16 October, at the end of the "Fear of a Blank Planet" tour in 2008.  The film is directed and edited by Lasse Hoile and the audio track is mixed in stereo and 5.1 Surround by Steven Wilson.

Porcupine Tree: Porcupine Tree were an English rock band formed by musician Steven Wilson in 1987.  The band began essentially as a solo project for Wilson, who created all of the band's music.  However, by 1993, Wilson desired to work in a band environment, and so brought on frequent collaborators Richard Barbieri on keyboards, Colin Edwin on bass and Chris Maitland on drums as permanent band members.  With Wilson still in charge of guitar and lead vocals, this would remain the lineup until 2001, when the band recruited Gavin Harrison to replace Maitland on drums.

Time Flies (song): Time Flies is a single from Porcupine Tree's 2009 studio album "The Incident".  Written by bandleader Steven Wilson, "Time Flies" is the centrepiece of the 55 minute movement that comprises the first disc of the album.  The track deals with the passage of time and the phenomenon that as one gets older, time seems to pass even more quickly, with the lyrics making reference to Wilson's life so far.  The song was edited down from its album length of 11:40 for both the single and video releases.  The music video was directed by longtime Porcupine Tree collaborator Lasse Hoile.  Due to an error in the mixing stage, the promo CD single edit has a strange drum mix, making it different from the full-length album mix.

XMII: XMII (also known as Transmission 4.1) is a live-in-studio album by British progressive rock band Porcupine Tree, released in June 2005.  It is the band's second session for XM Satellite Radio and was recorded on 21 July 2003.  Unlike its predecessor, "XM", "XMII" contains mostly tracks from the "Lightbulb Sun" album.  The album was issued on the band's own "Transmission" label and sold only at shows and through Porcupine Tree's online store, Burning Shed.  An interesting feature of the album is the song "Fadeaway" sung by guest guitarist John Wesley.

Question: Which band was formed first The Accidentals or Porcupine Tree?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "formation_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "formation_year"
      ],
      "additionalProperties": false
    },
    "band_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "formation_year": {
          "type": "integer"
        }
      },
      "required": [
        "name",
        "formation_year"
      ],
      "additionalProperties": false
    },
    "earliest_formed_band_name": {
      "type": "string"
    },
    "earliest_formation_year": {
      "type": "integer"
    }
  },
  "required": [
    "band_one",
    "band_two",
    "earliest_formed_band_name",
    "earliest_formation_year"
  ],
  "additionalProperties": false
}
