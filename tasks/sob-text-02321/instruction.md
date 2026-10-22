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
Born in '58: "Born in '58" is the last single from Bruce Dickinson's debut solo album, "Tattooed Millionaire", released on March 25 1991.  The song is about Bruce Dickinson's early life, growing up with his Grandparents in Worksop (Dickinson was born in 1958).

Eddie Vedder: Eddie Vedder (born Edward Louis Severson; December 23, 1964) is an American musician, singer and songwriter best known as a member of the rock band Pearl Jam, with whom he performs lead vocals and is one of three guitarists.  He is known for his powerful baritone vocals.  He also appeared as a guest vocalist in Temple of the Dog, the one-off tribute band dedicated to the late singer Andrew Wood.

The Wicker Man (song): "The Wicker Man" is a song by Iron Maiden, released as the first single and opening track from their album "Brave New World" in April 2000.  It is also the first single by the band since the returns of vocalist Bruce Dickinson and guitarist Adrian Smith in 1999.  It was co-written by Smith, Dickinson and Steve Harris.  It was co-produced by Kevin Shirley and Harris.  The title is inspired by the British cult film of the same name.  The song should not be confused with "Wicker Man" from Dickinson's solo career, the lyrics of which are more closely themed around the film.  The latter song can be found on the 2 disc edition of "The Best of Bruce Dickinson".

The Book of Souls World Tour: The Book of Souls World Tour was a concert tour by Iron Maiden, held in support of their sixteenth studio album, "The Book of Souls".  The first leg of the tour saw the band play shows in 36 countries across six continents, which included their debut performances in El Salvador, Lithuania and China.  With 117 shows, it was the longest tour with Bruce Dickinson on vocals since the "Somewhere on Tour" in 1986-87.  The group, their crew and equipment were transported on a customised Boeing 747-400, nicknamed "Ed Force One", which was piloted by vocalist Bruce Dickinson.

The Best of Bruce Dickinson: The Best of Bruce Dickinson is a compilation album released in 2001 by Bruce Dickinson.  Two versions were released; a single disc version and a bonus disc version.  On the front cover, the album title is imposed upon the seal of the demon Astaroth.

Bruce Dickinson: Paul Bruce Dickinson (born 7 August 1958), known professionally as Bruce Dickinson, is an English singer, songwriter, musician, airline pilot, entrepreneur, author and broadcaster.  He is the lead singer of the heavy metal band Iron Maiden and is renowned for his wide-ranging operatic vocal style and energetic stage presence.

List of songs recorded by Iron Maiden: Iron Maiden are an English heavy metal band formed by bassist Steve Harris in 1975.  The band's first album, 1980's "Iron Maiden", was written primarily by Harris, with vocalist Paul Di'Anno co-writing two tracks and guitarist Dave Murray contributing "Charlotte the Harlot".  The 1981 follow-up, "Killers", was written almost entirely by the bassist, with frontman Di'Anno contributing only to the title track, "Killers" (the North American bonus track "Twilight Zone" was credited to Harris and Murray).  Bruce Dickinson replaced Di'Anno after the release of "Killers", although he did not contribute any songwriting to "The Number of the Beast", released in 1982, which featured three songs co-written by guitarist Adrian Smith.  "The Number of the Beast" also spawned Iron Maiden's first UK Singles Chart top ten in the form of "Run to the Hills", which charted at number seven on its release.  It was not until 1983's "Piece of Mind" that the songwriting process became a more varied and collaborative approach, with just four of its nine tracks being credited solely to Harris, two to Dickinson and Smith, one to Harris and Murray, one to Dickinson alone, and one to Harris, Dickinson, and Smith.  The Dickinson and Smith-penned "Flight of Icarus" was the first Iron Maiden single to chart in the United States, reaching number eight on the "Billboard" Mainstream Rock chart.

Black (Pearl Jam song): "Black" is a power ballad by the American rock band Pearl Jam.  The song is the fifth track on the band's debut album, "Ten" (1991).  Featuring lyrics written by vocalist Eddie Vedder and music written by guitarist Stone Gossard, "Black" is said to be about first relationships, though Vedder showed strong emotion while performing the song live in early years.  (In relationship with Beth Liebling from 1983-2000) Notably, Vedder now renders the added lyric "We belong together" as "I've been healed" or "We didn't belong together" indicating his moving on from the relationship and being content with how it ended.

Water on the Road: Water on the Road is a film released on DVD and Blu-ray by American singer and Pearl Jam frontman Eddie Vedder.  It documents Vedder's 2008 solo tour, during which he performed Pearl Jam songs, numerous covers, and solo works including songs from the "Into the Wild Soundtrack".  The film features mostly performances from two shows Vedder performed on August 16 and 17, 2008, at Warner Theatre in Washington, D.C. It was released on May 31, 2011.

Man of Sorrows (Bruce Dickinson song): Man of Sorrows is the second single from Bruce Dickinson's fourth solo album, "Accident of Birth", released on 3 June 1997.  The song was originally written for a film called Chemical Wedding, which existed only as a script at the time (it was eventually filmed and released in May 2008).  The original version of the song is included on the Best Of Bruce Dickinson album and was recorded in 1990, engineered by André Jacquemin (who is better known for his sound-engineer work for Monty Python) and with Janick Gers on guitar.

Question: Which musician is known for their baritone vocals, Eddie Vedder or Bruce Dickinson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the musician known for baritone vocals."
    },
    "known_vocal_style": {
      "type": "string",
      "description": "The specific vocal style attributed to the musician in the context."
    },
    "is_baritone_vocalist": {
      "type": "boolean",
      "description": "True if the musician is known for baritone vocals, false otherwise."
    },
    "associated_band": {
      "type": "string",
      "description": "The primary band the musician is best known for."
    }
  },
  "required": [
    "musician_name",
    "known_vocal_style",
    "is_baritone_vocalist",
    "associated_band"
  ],
  "additionalProperties": false
}
