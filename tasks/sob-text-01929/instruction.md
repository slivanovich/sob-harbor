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
Bohemian Like You: "Bohemian Like You" is a song by American alternative rock band The Dandy Warhols.  The song was written by frontman Courtney Taylor-Taylor after seeing a woman pull up in her car to the traffic lights outside his apartment.  It was released as the second single from the band's third studio album, "Thirteen Tales from Urban Bohemia", in August 2000.

One Model Nation: One Model Nation is a graphic novel by Jim Rugg and Dandy Warhols frontman Courtney Taylor-Taylor about a fictional 1970s German krautrock band.  It was released on 11 November 2009.  An accompanying studio album titled "Totalwerks, Vol.  1 (1969–1977)", a fake greatest hits album by the fictional band, was released on 31 January 2012.

Peter Holmström: Peter Holmström is an American rock musician.  He is in the bands The Dandy Warhols, Pete International Airport, Radis Noir and Rebel Drones.  Holmström's first guitar was a Gibson SG.  Holmström is an amateur photographer.  In the past he has also composed music for his sister's theater group.

The Dandy Warhols: The Dandy Warhols are an American alternative rock band, formed in Portland, Oregon in 1994 by singer-guitarist Courtney Taylor-Taylor and guitarist Peter Holmström.  They were joined by keyboardist Zia McCabe and drummer Eric Hedford.  Hedford left in 1998 and was replaced by Taylor-Taylor's cousin Brent DeBoer.  The band's name is a play on the name of American pop artist Andy Warhol.

Mark Englert: Mark Englert is an American musician known as a guitarist for Dramarama since 1982.  He has appeared with Dramarama on "Late Night with David Letterman" and "The Tonight Show".  He has worked with a number of established musicians including Benmont Tench from Tom Petty and The Heartbreakers, and Clem Burke of Blondie.  Mark a.k.a. "Mr. E. Boy", was a founding member of Hatful of Rain, a defunct band established in Portland, Oregon during the mid-1990s, which featured singer/songwriter John Lowery and at one time included Courtney Taylor-Taylor of The Dandy Warhols on drums.  The band went on to receive stellar reviews from critics around the globe, but failed commercially due to their short term run of just a few months prior to their break-up.  Mark has been known to play guitar for many underground artists and has recently put out a few of his own solo records on his own label Phat Boris Records.

Pete International Airport: Pete International Airport is an American neo-psychedelia band from Portland, Oregon, formed in 1997 by Peter Holmström of The Dandy Warhols.  Other band members are Jsun Adams (The Upsidedown) on vocals, Collin Hegna (The Brian Jonestown Massacre) on bass guitar, Jason "Plucky" Anchondo (The Warlocks, Spindrift) on drums and Paulie Pulvirenti, also on drums.

The Dandy Warhols Are Sound: The Dandy Warhols Are Sound is a studio album by American alternative rock band The Dandy Warhols.  It is the original mix of the band's 2003 album "Welcome to the Monkey House", by Grammy Award-winning soul music mixing engineer Russell Elevado.  It was released on July 14, 2009, through the band's own label Beat the World Records.

Zia McCabe: Zia McCabe (born Aimee Springer on June 2, 1975) is a keyboard player, percussionist and bass guitarist, and member of American alternative rock band The Dandy Warhols.  She is also a solo DJ, and part of a six-piece country music band called Brush Prairie.  She graduated from Battle Ground High School in Battle Ground, Washington in 1993.  In 1995, with hardly any prior musical experience, Zia joined The Dandy Warhols.  In an interview, Zia said,

Plan A: "Plan A" is a song by American rock band The Dandy Warhols.  It was released as the third single from their fourth studio album, "Welcome to the Monkey House", on 24 November 2003.  It peaked at No. 66 on the UK Singles Chart.

Courtney Taylor-Taylor: Courtney A. Taylor (born July 20, 1967), known as Courtney Taylor-Taylor, is an American singer-songwriter from Portland, Oregon.  He is the lead singer and guitarist of alternative rock band The Dandy Warhols, a band he co-founded.  Taylor-Taylor has written the majority of the band's songs.

Question: "Plan A" is a song by American rock band The Dandy Warhols, an American alternative rock band, formed in Portland, Oregon in which year, by singer-guitarist Courtney Taylor-Taylor and guitarist Peter Holmström?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song mentioned in the question."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band associated with the song."
    },
    "band_origin": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the band was formed."
        },
        "state": {
          "type": "string",
          "description": "The state where the band was formed."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "formation_year": {
      "type": "integer",
      "description": "The year the band was formed."
    },
    "founding_members": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the founding members of the band."
    }
  },
  "required": [
    "song_title",
    "band_name",
    "band_origin",
    "formation_year",
    "founding_members"
  ],
  "additionalProperties": false
}
