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
Multiply (ASAP Rocky song): "Multiply" is a song recorded by American rapper ASAP Rocky, which was made available for online streaming on October 3, 2014.  Four days later, it was released as a digital single by RCA Records.  The song features Juicy J and was produced by Curtis Heron.  A music video for the track was co-directed by ASAP Rocky and Shomi Patwary.  The single serves as a promotional single for Rocky's third studio album "At.  Long.  Last.  ASAP"

M's (song): "M's" (stylized "M'$") is a song by American rapper ASAP Rocky, taken from Rocky's second studio album "At.  Long.  Last.  ASAP" (2015).  The song, produced by Honorable C.N.O.T.E. alongside Mike Dean, features a guest appearance from fellow American rapper Lil Wayne on the album version.  The song was originally released as a promotional single without Lil Wayne on April 10, 2015.  Upon the release of the album, high downloads resulted in the song peaking at number 6 on the US "Billboard" Bubbling Under Hot 100 Singles chart.

No Limit (G-Eazy song): "No Limit" is a song by American rapper G-Eazy, featuring American rapper ASAP Rocky and American hip hop recording artist Cardi B.  It was written by G-Eazy, ASAP Rocky, Cardi B, Allen Ritter and Boi-1da, with production handled by the latter two.  The song was released through RCA Records on September 8, 2017, as the lead single from G-Eazy's upcoming fifth studio album, "The Beautiful and Damned" (2017).

Long. Live. ASAP: Long.  Live.  ASAP (stylized as LONG.LIVE.A$AP) is the debut studio album by American rapper ASAP Rocky.  It was released on January 15, 2013, by ASAP Worldwide, Polo Grounds Music and RCA Records.  The album features guest appearances from Kendrick Lamar, Schoolboy Q, 2 Chainz, Drake, Big K.R.I.T., Santigold, Overdoz, Yelawolf, Florence Welch, Danny Brown, Action Bronson, Joey Badass, Gunplay and ASAP Ferg.  The album's production was handled by Rocky himself (under the pseudonym LORD FLACKO), Hector Delgado, Hit-Boy, Clams Casino, Jim Jonsin, T-Minus, Danger Mouse, 40, Skrillex and Emile Haynie, among other high-profile producers.

12 (ASAP Twelvyy album): 12 is the debut studio album by American rapper ASAP Twelvyy.  It was released on August 4, 2017, by ASAP Worldwide, Polo Grounds Music and RCA Records.  The album features guest appearances from Joey Badass, Telana, Flatbush Zombies, Fredro Starr, ASAP Rocky, ASAP Ferg, ASAP Ant and ASAP Nast.  It also lists production from Finatik N Zac, Harry Fraud, Hector Delgado, Jim Jonsin, Maaly Raw, P on the Boards, Ricci Riera, among others.

At. Long. Last. ASAP: At.  Long.  Last.  ASAP (stylized as AT.LONG.LAST.A$AP) is the second studio album by American rapper ASAP Rocky .  It was released on May 26, 2015, by A$AP Worldwide, Polo Grounds Music, and RCA Records.  The record serves as a sequel from Rocky's previous studio effort "Long.  Live.  ASAP" (2013).  In 2013, the recording sessions first took place, during a release of "Long.  Live.  A$AP".  The album's executive production was provided by Danger Mouse, mentor ASAP Yams and Rocky himself, featuring production by Rocky and Danger Mouse, as well as a variety of several high-profile producers, including co-executive producers Hector Delgado and Juicy J, Jim Jonsin, FNZ, Frans Mernick, Kanye West, Thelonious Martin and Mark Ronson, among others.

Wild for the Night: "Wild for the Night" is a song by American hip hop recording artist ASAP Rocky and primarily produced by Skrillex.  It was released on March 26, 2013, as the third single from his debut studio album "Long.  Live.  ASAP".  On March 26, 2013 the song was officially released to rhythmic crossover radio as the third single and the music video was released.  The song has since peaked at #80 on the Billboard Hot 100.

PMW (All I Really Need): "PMW (All I Really Need)" is a song by American hip hop recording artist ASAP Rocky, taken from Rocky's debut studio album "Long.  Live.  ASAP" (2013).  The song, produced by T-Minus alongside Nikhil Seetharam, features a guest appearance from Rocky's frequent collaborator and fellow American rapper Schoolboy Q.  The song marks their third collaboration, with the first being "Brand New Guy", from Rocky's 2011 mixtape "Live.  Love.  ASAP", followed by "Hands on the Wheel", featured on Q's 2012 project "Habits & Contradictions".  Upon the release of the album, high downloads resulted in the song peaking at number 14 on the US "Billboard" Bubbling Under Hot 100 Singles chart.

Train discography: American pop rock band Train has released ten studio albums, two live albums, one video album, four extended plays, 30 singles, four promotional singles, and 26 music videos.  The band independently released their eponymous debut studio album in 1996, two years after their formation.  In February 1998, the band signed to Aware Records and Columbia Records and re-released the album under the two labels.  Three singles were released from "Train"; the album's second single, "Meet Virginia", peaked at number 20 on the US "Billboard" Hot 100.  The album peaked at number 76 on the US "Billboard" 200 and was certified platinum by the Recording Industry Association of America (RIAA).  In the period following the release of "Train", producer Brendan O'Brien started working with the band in a partnership that would last for three albums.  The band released their second studio album "Drops of Jupiter" in March 2001; it was preceded by the release of its lead single, "Drops of Jupiter (Tell Me)".  The single became a commercial success, peaking at number five on the US "Billboard" Hot 100 and also becoming a top ten hit in Australia, the Netherlands and the United Kingdom.  "Drops of Jupiter (Tell Me)" also won an award for Best Rock Song at the 44th Grammy Awards.  The album peaked at number six on the "Billboard" 200, earning a double platinum certification from the RIAA. " She's on Fire", the third single from "Drops of Jupiter", achieved moderate success in Australia and the UK.  Train's third studio album, "My Private Nation", was released in June 2003.  It peaked at number six on the "Billboard" 200 and was certified platinum by the RIAA.  The album's first two singles, "Calling All Angels" and "When I Look to the Sky", peaked at numbers 19 and 74 respectively on the "Billboard" Hot 100.  The band released their fourth studio album "For Me, It's You" in January 2006.  The album peaked at number 10 on the "Billboard" 200 and spawned three singles.

Trap Lord: Trap Lord is the debut studio album by American rapper ASAP Ferg.  The album was released on August 20, 2013, by ASAP Worldwide, Polo Grounds Music, and RCA Records.  The album features guest appearances from ASAP Rocky, Bone Thugs-n-Harmony, French Montana, Trinidad James, Schoolboy Q, Waka Flocka Flame, Aston Matthews, B-Real and Onyx.

Question: What debut studio album by American rapper ASAP Rocky released on January 15, 2013, that had a third single peaked at #80 on the Billboard Hot 100?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "album_artist": {
      "type": "string",
      "description": "The artist who released the album."
    },
    "album_type": {
      "type": "string",
      "description": "The type of album, e.g., 'debut studio album'."
    },
    "album_release_date": {
      "type": "string",
      "description": "The release date of the album."
    },
    "related_single": {
      "type": "object",
      "properties": {
        "single_name": {
          "type": "string",
          "description": "The name of the single."
        },
        "single_number": {
          "type": "integer",
          "description": "The sequential number of the single from the album."
        },
        "chart_peak_position": {
          "type": "integer",
          "description": "The highest position the single reached on the specified chart."
        },
        "chart_name": {
          "type": "string",
          "description": "The name of the music chart."
        }
      },
      "required": [
        "single_name",
        "single_number",
        "chart_peak_position",
        "chart_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "album_name",
    "album_artist",
    "album_type",
    "album_release_date",
    "related_single"
  ],
  "additionalProperties": false
}
