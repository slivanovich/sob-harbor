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
Six Queens: "Six Queens" was Larrikin Love's debut single, released on Young and Lost Club Records in September 2005.  Although billed as a double A side with "Little Boy Lost", the greater popularity of the former among both fans and the band, and the fact that it had a music video made for it means that the release is usually simply referred to as just 'Six Queens'.

Tiny Dancers: Tiny Dancers were an English band from South Elmsall, West Yorkshire.  They are David William Kay (vocals, acoustic guitar), Chris Etherington (lead guitar, keyboards), Dale Wathey (bass guitar), Duncan Morrison (drums) and David Glover (keyboards, glockenspiel, percussion, guitar).  Based in Sheffield, they signed to Parlophone in early 2006 and supported acts as diverse as The Spinto Band, Babyshambles, Richard Ashcroft, Larrikin Love, Bob Dylan, as well as a co-headlining tour with Ghosts and their own headline tour.

Downing Street Kindling: "Downing Street Kindling" was the second single to be taken from Larrikin Love's debut album, "The Freedom Spark", and their first release to enter the UK Top 40, charting at number 35.

Micko Larkin: Michael "Micko" Joseph Larkin (born 13 October 1986) is an English musician, most notable as the lead guitarist of the indie rock band Larrikin Love and reformed Hole.

Larrikin Love: Larrikin Love were an English four piece indie rock band from London.

Happy as Annie: "Happy as Annie" was originally released in 2005 as the limited edition second single by Larrikin Love on London indie label Transgressive Records (TRANS 010).  Re-recorded and re-mixed by Ian Gore for the band's 2006 debut album "The Freedom Spark", a new version of the song was released on 11 September 2006 through Warner.

Edwould: "Edwould" was the third single from Larrikin Love, and the first to be taken from their debut album "The Freedom Spark".  It was also the band's first major label release and the first to receive full distribution, and subsequently reached number 49 on the UK charts.

List of Rock Band Network songs: The "Rock Band" Network in the music video games "Rock Band 2" and "Rock Band 3" supports downloadable songs for the Xbox 360, PlayStation 3, and Wii veins throughout the consoles' respective online services.  The Rock Band Network Store became publicly available on March 4, 2010 for all Xbox 360 players in selected countries (US, Canada, UK, France, Italy, Germany, Spain, Sweden, and Singapore).  Rock Band Network songs became available on the PlayStation 3 in five song intervals through their own Rock Band Network Store on April 22, 2010.  Starting on April 12, 2011, up to 10 songs were added weekly to the PlayStation 3 platform until June 14, 2011 when it reverted to five song intervals.  Also, starting on June 14, 2011, PlayStation 3 Rock Band Network songs will only be compatible with Rock Band 3.  Rock Band Network became available on the Wii in six to 10 song intervals from September 7, 2010 to January 18, 2011.  Rock Band Network songs will be exclusive to the Xbox 360 for 30 days, after which a selection of songs will be made available on the PlayStation 3 and Wii.  As of January 18, 2011, no further Rock Band Network songs will be released on the Wii platform due to Nintendo's small online install base, limited demand for the songs and the significant amount of work each song needs to convert to the Wii.

In Here We Fall: In Here We Fall is the second album by British rock band Electrasy, released on September 26, 2000 to capitalize on interest in the single "Morning Afterglow" in the United States.  It was later released in Japan on February 7, 2001, with the song "Renegades" released as a promo single in early January the same year.  It was produced by Matthew Wilder and engineered by Chris Brown.

Electrasy: Electrasy were an English rock band.  Formed in 1994 in Dorset, UK, the band consisted of vocalist Alisdair (Ali) McKinnell, guitarists Nigel Nisbet and Steve Atkins, bassist Alex Meadows (who joined the band before they recorded "In Here We Fall"), drummer Paul Pridmore and keyboardist Jim Hayden (who left the band by May 2001).  The band were active until 2002, although several members of the band still based in the UK after this time continued to perform occasional gigs.  Nigel Nisbet has subsequently released three solo-albums, "Calling All The Dreamers" in 2007, "Musicians are Different" in 2015 and "Mainstream Panic" in 2016.  Alex Meadows has also released recent solo material under the name "The Inexperienced", and is also a regular performer with various other acts (Tom Jones, Il Divo).

Question: Which rock band, Larrikin Love or Electrasy,.came out of Dorset, UK?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "bands_evaluated": {
      "type": "array",
      "description": "A list of bands considered in the question, with their relevant attributes.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "origin_location": {
            "type": "string",
            "description": "The location where the band was formed."
          }
        },
        "required": [
          "band_name",
          "origin_location"
        ],
        "additionalProperties": false
      }
    },
    "answer_band_name": {
      "type": "string",
      "description": "The name of the band that is the correct answer to the question."
    },
    "answer_origin_location": {
      "type": "string",
      "description": "The origin location of the answer band."
    }
  },
  "required": [
    "question_asked",
    "bands_evaluated",
    "answer_band_name",
    "answer_origin_location"
  ],
  "additionalProperties": false
}
