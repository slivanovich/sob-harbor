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
Homework (Daft Punk album): Homework is the debut studio album by the French electronic music duo Daft Punk, released on 20 January 1997 by Virgin Records and Soma Quality Recordings.  The duo produced the tracks without plans to release an album.  After working on projects that were intended to be separate singles over five months, they considered the material good enough for an album.

Electricity (The Avalanches song): "Electricity" is a song by Australian electronic music group The Avalanches.  Produced by group members Robbie Chater and Darren Seltmann, it was issued as a single on 13 September 1999 as the group's first release for Modular Recordings.  "Electricity" was later remixed and remastered for inclusion on the group's debut album "Since I Left You" (2000).  The song features prominent samples of "Rapp Dirty" by American musician Blowfly, as well as guest vocals from Australian singers Sally Russell and Antoinette Halloran.  Several critics' reviews of the song noted its disco sound and likened it to the work of French electronic music duo Daft Punk.  "Electricity" was later re-released as a single on 3 December 2001, with single releases containing remixes of the song by DJ Harvey and DJ Sneak.

Contact (Daft Punk song): "Contact" is a song by French electronic music duo Daft Punk.  It is the thirteenth and final track from the duo's fourth studio album "Random Access Memories", released on 17 May 2013.  The track was written and produced by the duo, with additional writing and co-production by DJ Falcon.  Daryl Braithwaite, Tony Mitchell, and Garth Porter are also credited as writers due to the song containing a sample of "We Ride Tonight" by Australian rock band The Sherbs.  The song includes audio from the Apollo 17 mission, courtesy of NASA and Captain Eugene Cernan.  Due to digital downloads of "Random Access Memories", the song charted at number 46 on the French Singles Chart and at number 24 on the "Billboard" Dance/Electronic Songs chart.

Daft Punk discography: French electronic music duo Daft Punk has released four studio albums, two live albums, one compilation album, one soundtrack album, three remix albums, one video album, 22 singles and 18 music videos. Group members Thomas Bangalter and Guy-Manuel de Homem-Christo met in 1987 while studying at the Lycée Carnot secondary school.  They subsequently recorded several demo tracks with each other, forming Daft Punk in 1993.  Their debut single "The New Wave" was released the following year on the Soma Quality Recordings label.  Daft Punk first found commercial success with the release of their second single "Da Funk", which peaked at number seven in France and topped the United States "Billboard" Hot Dance Club Play chart.

Face to Face (Daft Punk song): "Face to Face" is a song by French electronic music duo Daft Punk, featuring vocals and co-production by American house music producer Todd Edwards.  It was released as the fifth single from their 2001 album "Discovery".  Promotional 12" singles were released for those who pre-ordered the 2003 remix album "Daft Club", and a CD single containing a remix of the song by French producer Demon was released commercially.  As part of "Discovery", the song appears in the film "", and the section of the film in which the song appears serves as its music video.  The song topped the "Billboard" Hot Dance Club Play chart in 2004.

Around the World (Daft Punk song): "Around the World" is a song by the French electronic music duo Daft Punk.  The song was written by the duo and appeared on their debut album "Homework" in 1997 and was released as a single the same year.  It became a major club hit around the world and reached number one in the dance charts.  The song's only lyrics are the title.  The music video was directed by Michel Gondry and choreographed by Blanca Li.  In October 2011, "NME" placed it at number 21 on its list "150 Best Tracks of the Past 15 Years".

Paradis (duo): Paradis is a French electronic music duo consisting of Simon Mény and Pierre Rousseau.  The duo is currently signed to Universal label Maison Barclay.  They grew to fame after releasing their first 12" single on Beats In Space titled Parfait Tirage featuring a cover of Alain Souchon's "La Ballade de Jim".  The duo have appeared on the French DJ scene with sets at Nuits Sonores and Rex Club.

Discovery (Daft Punk album): Discovery is the second studio album by French electronic music duo Daft Punk, released on 26 February 2001 by Virgin Records.  It marks a shift from the Chicago house sound prevalent on their first studio record, "Homework" (1997), to a house style more heavily inspired by disco, post-disco, garage house, and synthpop.  Comparing their stylistic approach to their previous album, band member Thomas Bangalter described "Discovery" as an exploration of song structures and musical forms whereas "Homework" was "raw" electronic music.  He also described "Discovery" as a reflection of the duo's childhood memories, when they would listen to music with a more playful and innocent viewpoint.

Air (French band) discography: The discography of French electronic music duo AIR consists of seven studio albums (including one collaborative album), one remix album, one soundtrack album, one mix album, two video albums, one extended play, twenty-two singles and sixteen music videos.  The band's first release was the 1995 single "Modular Mix", which peaked at number 177 in the United Kingdom.  Their debut extended play, "Premiers Symptômes", was released in July 1997; it peaked at number 12 in the UK and was certified silver by the British Phonographic Industry (BPI). " Moon Safari", AIR's debut studio album, was released in January 1998.  It peaked at number 21 in France and was certified gold by the Syndicat National de l'Édition Phonographique (SNEP).  "Moon Safari" reached the top ten in countries such as Ireland and the UK and produced three singles: "Sexy Boy", "Kelly Watch the Stars" and "All I Need".  All three singles reached the top 40 in the UK; "Sexy Boy" and "All I Need" reached the top 25 in Finland and the Netherlands respectively.

Indo Silver Club: "Indo Silver Club" is a single by French electronic music duo Daft Punk.  It was released as a 12-inch single on 26 February 1996 by Soma Quality Recordings with no artist listed on the record.  "Indo Silver Club" (Part Two) was later released as the 14th track on their debut album "Homework" in 1997.

Question: Which record company released an album which included the single 'Indo Silver Club' by this French electronic music duo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_duo": {
      "type": "string",
      "description": "The name of the electronic music duo."
    },
    "album_name": {
      "type": "string",
      "description": "The name of the album that included the single."
    },
    "included_single_name": {
      "type": "string",
      "description": "The name of the single included in the album."
    },
    "record_companies": {
      "type": "array",
      "description": "A list of record companies that released the album.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "artist_duo",
    "album_name",
    "included_single_name",
    "record_companies"
  ],
  "additionalProperties": false
}
