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
Werk 80 II: Werk 80 II is the eighth full-length album by German industrial gothic metal band Atrocity, released on February 29, 2008 and their 2nd full-length cover album after the original "Werk 80" album released in 1997.  Burlesque artist Dita Von Teese is the cover model.

We Are All We Have: We Are All We Have is the eighth full-length studio album from American street punk band The Casualties, on the record label SideOneDummy Records.  The band started a headlining tour in support of the album on August 20, 2009.

Reiterate: Reiterate is the eighth full-length album from the Christian hip hop group GRITS.  It was released on September 16, 2008, and is the GRITS first release on their newly formed Revolution Art label.

Handful of Stars: Handful of Stars (Ukrainian: Пригорща Зірок, Pryhorshcha Zirok) is the eighth full-length album by Ukrainian black metal band Drudkh, released in 2010 on Season of Mist's Underground Activists label.

Woodstock (Portugal. The Man album): Woodstock is the eighth full-length album by American rock band Portugal.  The Man, released on June 16, 2017 through Atlantic Records.

Feel It Still: "Feel It Still" is a song by American rock band Portugal.  The Man.  The song was written by the band along with John Hill and Asa Taccone, with the latter two serving as producers.  It serves as the second single and first radio single off their eighth studio album "Woodstock".  The song reached number one on the US Alternative Songs and Russian Tophit airplay chart, and became their first entry on the Hot 100, peaking at number 10 as of October 2017.

Universal (Borknagar album): Universal is the eighth full-length album by the Norwegian metal band Borknagar.  It marks the return of guitarist Jens F. Ryland.  The band's former vocalist ICS Vortex performed vocals on the track "My Domain".  The album was intended to be released in the fall of 2009, but the release date was postponed as a result of a label decision.  It was released on 22 February 2010 in four formats: a regular jewelcase CD, a limited digipack which includes a bonus disc, a CD box with extras, and a gatefold LP with double vinyl.

Night Is the New Day: Night Is the New Day is Katatonia's eighth full-length album.  It was released 2 November 2009, in Europe and 10 November 2009, in North America through Peaceville Records.  Thirteen tracks were recorded, eleven of which made it onto the record.  The band describes the material as "Our most varied, diverse and possibly strongest shit all together on one and the same album".  "Idle Blood" had the working title "Kozelek", named after Mark Kozelek, a member of Red House Painters, which is one Katatonia's influences.  This is the last Katatonia release with the Norrman brothers.

I Am the Portuguese Blues: I Am the Portuguese Blues is the eighth full-length album released by Starflyer 59.  With this album, the band returned to its past in multiple ways.  The band's earlier albums had been characterized by loud guitars, but later albums saw the band progress to a softer sound, incorporating keyboards.  "I Am the Portuguese Blues" saw the return of the sound from earlier albums, as the band was stripped just to Jeff Cloud on bass, Frank Lenz on drums, and Jason Martin, the only person to perform on all of Starflyer 59's albums, handling guitar and vocal duties.  In addition, the album has a monochromatic cover, similar to those of Starflyer 59's first three albums ("Silver", "Gold", and "Americana").  Many of the songs on "I Am the Portuguese Blues" were written years earlier as demos for an album to follow "Americana".  They were eventually scrapped, as the band decided to take a different musical direction for "The Fashion Focus".  The old demos were refined and combined with several new songs for "I Am the Portuguese Blues".  In regards to the title of the album, Martin, the band's frontman said,

Dance of the Headless Bourgeoisie: Dance of the Headless Bourgeoisie is the eighth full-length album released by Canadian punk rock band Nomeansno.  It was initially released on Alternative Tentacles in 1998 as a 10-track CD and 12-track double LP.  The band's own label Wrong Records, along with distributors Southern Records, re-released the 12-track version of the album in 2007, 2010, and 2014 with modified track order and art.

Question: On which record label did the band who released the single Feel It Still release their eighth full-length album Woodstock?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "album_number": {
      "type": "integer",
      "description": "The sequential number of the album in the band's discography."
    },
    "record_label": {
      "type": "string",
      "description": "The record label through which the album was released."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the album was released."
    }
  },
  "required": [
    "album_title",
    "band_name",
    "album_number",
    "record_label",
    "release_year"
  ],
  "additionalProperties": false
}
