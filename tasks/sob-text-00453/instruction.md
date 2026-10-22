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
Wings at the Speed of Sound: Wings at the Speed of Sound is the fifth studio album by Wings, released on 25 March 1976 as a follow-up to their previous album "Venus and Mars".  Issued at the height of the band's popularity, it reached the top spot on the US album chart and peaked at number 2 on the UK album chart.  Both singles from the album also reached the top 5 of the UK and US singles charts, with 'Silly Love Songs' reaching number 1 in the US.

G4 Love Songs: G4 Love Songs is the fifth album released by "X Factor" runners-up G4.  The album of love songs features Lesley Garrett, Merrill Osmond, Oli Nez and The City of Prague Philharmonic Orchestra.  "G4 Love Songs" was funded by fans through PledgeMusic, where the funding reached 112%.  Part of the pledge money was donated to Breast Cancer Care.

Love Songs (Ayumi Hamasaki album): Love Songs (stylized as Love songs) is the twelfth studio album by Japanese singer-songwriter Ayumi Hamasaki.  The album was released on December 22, 2010 through Avex Trax, eight months after her eleventh studio album "Rock 'n' Roll Circus".  A stylistic return to the aesthetic of her albums before "Secret", "Love Songs" contains pop songs with lyrics primarily revolving around love, many of them ballads.

Silly Love Songs: "Silly Love Songs" is a song written by Paul McCartney and Linda McCartney and performed by Wings.  The song appears on the 1976 album "Wings at the Speed of Sound."  It was also released as a single in 1976, backed with "Cook of the House".  The song, written in response to music critics accusing him of writing only "silly love songs", also features disco overtones.

Love Songs (Michael Jackson album): Love Songs is a compilation album by American recording artist Michael Jackson.  It was released on January 15, 2002 by Motown Records as a part of "Motown's Love Songs" line.  The album contains 14 love songs and ballads Michael Jackson recorded, either by himself or with The Jackson 5, during his time on Motown in the early '70s.  In this case there are many hits of Michael (such as "Got to Be There"), or The Jackson 5 hits, such as "Who's Lovin' You,".  It also includes an unreleased version of The Jackson 5 hit, "I'll Be There", and the original mix of Michael's "Call on Me".

Cook of the House: "Cook of the House" is a song written by Paul and Linda McCartney that was first released on Wings' 1976 album "Wings at the Speed of Sound".  It was also released as the B-side to the number 1 single "Silly Love Songs."  The song was included on Linda McCartney's posthumous 1998 solo album "Wide Prairie".

Jūnigatsu no Love Song: Complete Box: Jūnigatsu no Love Songs ~Complete Box~ (December Love Songs ~Complete Box~) is a limited edition box set album released by Gackt on December 13, 2006.  It contains nine different versions of the previously released single Jūnigatsu no Love Song, including the Chinese version duet with Leehom Wang, and four new versions.  The box set also contained an aromatherapy diffuser and gold & silver foil postcards of the CD covers.

Silly Love Songs (Glee): "Silly Love Songs" is the twelfth episode of the second season of the American musical television series "Glee", and the thirty-fourth overall.  The Valentine's Day-themed episode was written by series creator Ryan Murphy, directed by Tate Donovan, and premiered on Fox on February 8, 2011.  In this episode, Director Will Schuester (Matthew Morrison) assigns the McKinley High School glee club to perform love songs in honor of Valentine's Day.  Club member Finn Hudson (Cory Monteith) sets up a kissing booth for the occasion, to take advantage of his rising popularity and raise money for the club.  At the Dalton Academy, Blaine Anderson (Darren Criss) and the Dalton Academy Warblers make plans to perform a musical number outside of the campus, and Kurt Hummel (Chris Colfer) confesses his love for Blaine.

Songs for a Blue Guitar: Songs for a Blue Guitar is an album by Red House Painters, released on July 22, 1996 in the UK, and a day later in the US.  It is effectively a Mark Kozelek solo album, since no other members of the band are listed in the liner notes.  The album introduced heavier, electric guitar driven rock to their sound in songs like "Make Like Paper", and Kozelek's cover of Paul McCartney & Wings' "Silly Love Songs".

Love Songs (Glen Campbell album): Love Songs, released on the Gold Label in 2000, contains a selection of songs from the "Love Songs" disc from the 1999 My Hits and Love Songs album.

Question: "Silly Love Songs" is a song on an album released on which date ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album on which the song appears."
    },
    "album_artist": {
      "type": "string",
      "description": "The artist who released the album."
    },
    "album_release_date": {
      "type": "string",
      "format": "date",
      "description": "The release date of the album."
    }
  },
  "required": [
    "song_title",
    "album_title",
    "album_artist",
    "album_release_date"
  ],
  "additionalProperties": false
}
