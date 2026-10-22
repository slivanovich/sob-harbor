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
The White Stripes (album): The White Stripes is the debut studio album by American alternative rock duo The White Stripes, released on June 15, 1999.  The album was produced by Jim Diamond and vocalist/guitarist Jack White, recorded in January 1999 at Ghetto Recorders and Third Man Studios in Detroit.  White dedicated the album to deceased blues musician Son House.

Jim Diamond (1988 album): Jim Diamond is Singer/Songwriter Jim Diamond's self-titled and third studio album.  Diamond was assisted by old friends Graham Lyle and Chris Parren, who had worked with him on previous albums.

Siddhartha (American rock band): Siddhartha is an American band formed in 2003, led by singer/songwriter Marlon Hauser continued the tradition of Detroit garage icons such as the MC5, The Stooges, and The Gories.  The group recorded a full-length album with Jim Diamond which was never officially released, however in 2006 some of those recordings surfaced as a bootleg EP titled War Is Tragic.  In 2007, Siddhartha appeared on the compilation album as a digital only download for the Manimal Vinyl label.  Also that same year, Mick Collins of The Dirt Bombs produced the single The Fashion Victims.  In 2008 after a move to San Francisco and a lineup change, Manimal Vinyl would sign the band and issue the single/EP titled The Birth Book which featured the Madonna cover, Holiday as a B-side.

Jim Diamond (singer): James Aaron Diamond (28 September 1951 – 8 October 2015) was a Scottish singer-songwriter, best known for his three Top 5 hits.  The first was "I Won't Let You Down" (1982), as the lead singer in the trio PhD, with Tony Hymas and Simon Phillips.  His solo performance, "I Should Have Known Better", was a United Kingdom No.1 in 1984.  The third track was the theme song from "Boon", "Hi Ho Silver" which reached No.5 in the UK Singles Chart in 1986.  He has also featured as a vocalist on the charity No.1s "You'll Never Walk Alone" with The Crowd and "Let It Be" with Ferry Aid.  His last UK chart success was with "Young Love (Carry Me Away)" in 1986.

Beach Day: Beach Day are a rock band based in Hollywood, Florida.  The duo consists of Kimmy Drake (guitars/vocals) and Skyler Black (drums).  The duo met at a local show and bonded over their love of 60's girl groups and a common desire to be in a band that was purely about fun.  Beach Day released their debut single, "Beach Day," in summer of 2012 and sophomore single "Walking on the Streets" in the fall.  Their debut album, "Trip Trap Attack", was released on June 18, 2013 by Kanine Records.  It was recorded in South Florida and mixed in Detroit by Jim Diamond.  Beach Day covered "Up on the Roof" for a LensCrafters television advertisement.  They also did a cover of Screaming Lord Sutch's "Dracula's Daughter" in 2013 which was produced by Kramer.

Hi Ho Silver: "Hi Ho Silver" is a song by Scottish singer/songwriter Jim Diamond.  It is best known for being the theme song for "Boon".  The song was from Diamond's second solo studio album "Desire for Freedom".  It reached #5 on the UK chart in 1986.

The Best of Jim Diamond: The Best of Jim Diamond is a compilation album of tracks from Scottish singer-songwriter Jim Diamond's first two solo albums "Double Crossed" and "Desire for Freedom", along with B-sides.

Jim Diamond (1993 album): Jim Diamond was Jim Diamond's first studio album in five years (not to be confused with its identically-named 1988 predecessor).  Featuring nine new songs and three re-recordings "Hi Ho Silver", "I Won't Let You Down" and "I Should Have Known Better".

Wolfmother (EP): Wolfmother is the debut extended play (EP) by Australian rock band Wolfmother.  Recorded and mixed at Ghetto Studios in Detroit, Michigan, USA, it was released in Australia on 27 September 2004 and later in the United States and the United Kingdom.  The EP was produced and mastered by Jim Diamond and mixed by bassist and keyboardist Chris Ross; the album cover was designed by drummer Myles Heskett.  All four songs from "Wolfmother" were later re-recorded for the band's self-titled debut studio album; "Dimension", "Woman" and "White Unicorn" were also released as singles from the album.

Double Crossed: Double Crossed was Jim Diamond's solo début album in 1985.  The album featured Diamond's first three solo singles "I Should Have Known Better", "I Sleep Alone at Night" and "Remember I Love You".

Question: What year was Jim Diamond's Double Crossed album released?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who released the album."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    }
  },
  "required": [
    "album_title",
    "artist_name",
    "release_year"
  ],
  "additionalProperties": false
}
