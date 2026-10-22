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
A Different Ship: A Different Ship is the third album from Brooklyn-based indie rock band Here We Go Magic and was released by Secretly Canadian in May 2012.  As he did on the band's first two albums ("Here We Go Magic" and "Pigeons"), Luke Temple filled the dual role of singer and songwriter.  The band also teamed with producer Nigel Godrich (Radiohead, Pavement) for the first time.

Pavement (band): Pavement was an American indie rock band that formed in Stockton, California in 1989.  The group mainly consisted of Stephen Malkmus (vocals and guitar), Scott Kannberg (guitar and vocals), Mark Ibold (bass), Steve West (drums) and Bob Nastanovich (percussion and vocals).  Initially conceived as a recording project, the band at first avoided press or live performances, while attracting considerable underground attention with their early releases.  Gradually evolving into a more polished band, Pavement recorded five full-length albums and nine EPs over the course of their decade-long career, though they disbanded with some acrimony in 1999 as the members moved on to other projects.  In 2010, they undertook a well-received reunion tour.

The Bends: The Bends (stylised as the bends) is the second studio album by the English alternative rock band Radiohead, released on 13 March 1995 by Parlophone Records in the United Kingdom and by Capitol Records in the United States.  The album was produced by John Leckie and engineered by Nigel Godrich, who would go on to co-produce all future albums by the band.  "The Bends" marked the beginning of a shift in aesthetics and themes for the band, with greater use of keyboards and more abrasive guitar tracks, while balancing them with subtler ones.  The introspective grunge-influenced style of their debut album "Pablo Honey" (1993) evolved into more multi-layered rock with cryptic lyrics and larger ideas, as the band and its lead singer and songwriter Thom Yorke reacted against the rigours of their near-constant world tours.

Slay Tracks (1933–1969): Slay Tracks (1933–1969) (usually referred to as Slay Tracks) is American indie rock band Pavement's debut extended play (EP).  Pavement—at that time, a duo of just its two founding members Stephen Malkmus (guitar, vocals) and Scott Kannberg (guitar)—recorded "Slay Tracks" with producer and future member Gary Young (drums) during a four-hour session.  Pavement self-released the EP as a 7" vinyl record on the band's own record label Treble Kicker in 1989.  The music of "Slay Tracks" was influenced by indie and punk rock bands such as Swell Maps and The Fall, and many of the lyrics were inspired by life in the band's hometown of Stockton, California.

Ultraísta: Ultraísta is an experimental rock band, formed in 2008.  The band consists of Atoms for Peace members Nigel Godrich and Joey Waronker, alongside Laura Bettinson.  The band's self-titled debut album was released on October 2, 2012.  The band's biography notes that it was "conceived from a love of afrobeat, electronica, art and inspired by tequila.

Kid A: Kid A is the fourth studio album by the English rock band Radiohead, released on 2 October 2000 by Parlophone.  On the verge of a breakdown after promoting Radiohead's 1997 album "OK Computer", songwriter Thom Yorke envisioned a radical change in direction.  Radiohead replaced their rock sound with synthesisers, drum machines, the ondes Martenot, string orchestras and brass instruments.  They incorporated influences from genres such as electronic music, krautrock, jazz, and 20th-century classical music.  They recorded "Kid A" with "OK Computer" producer Nigel Godrich in Paris, Copenhagen, Gloucestershire and their hometown Oxford, England.  The sessions produced over 20 tracks, and Radiohead split the work in two albums: "Kid A" and "Amnesiac".  The latter was released the following year.

All I Need (Radiohead song): "All I Need" is a song by English alternative rock band Radiohead, produced by Nigel Godrich, and released on their seventh studio album "In Rainbows" (2007).  One of the band's most direct love songs, "All I Need" is a downbeat track which sees frontman Thom Yorke singing of obsession and unrequited love.

Nigel Godrich: Nigel Timothy Godrich (born 28 February 1971) is an English record producer, recording engineer and musician.  He is best known for his work with the English rock band Radiohead, having produced all of their studio albums since "OK Computer" (1997); he has been dubbed the "sixth member" of the band, in an allusion to George Martin being called the "Fifth Beatle".  Godrich has also worked extensively with Radiohead singer Thom Yorke on his solo material, and is a member of the bands Atoms for Peace (with Yorke) and Ultraísta.  Other acts Godrich has worked with include Beck, Paul McCartney, U2, R.E.M. and Roger Waters.  He is the creator of the music webseries "From the Basement".

Radiohead: Radiohead are an English rock band from Abingdon, Oxfordshire, formed in 1985.  The band consists of Thom Yorke (lead vocals, guitar, piano, keyboards), Jonny Greenwood (lead guitar, keyboards, other instruments), Ed O'Brien (guitar, backing vocals), Colin Greenwood (bass), and Phil Selway (drums, percussion, backing vocals).  They have worked with producer Nigel Godrich and cover artist Stanley Donwood since 1994.

Terror Twilight: Terror Twilight is the fifth and final studio album by American indie rock band Pavement, released on June 8, 1999 on Matador Records in the US and Domino Records in the UK.  It was produced by Nigel Godrich.

Question: What is the forming year of this American indie rock band that formed in Stockton, California, and was produced by Nigel Godrich?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_name": {
      "type": "string",
      "description": "The name of the band."
    },
    "genre": {
      "type": "string",
      "description": "The musical genre of the band."
    },
    "origin_city": {
      "type": "string",
      "description": "The city where the band formed."
    },
    "origin_country": {
      "type": "string",
      "description": "The country where the band formed."
    },
    "producer_name": {
      "type": "string",
      "description": "The name of the producer associated with the band."
    },
    "forming_year": {
      "type": "integer",
      "description": "The year the band was formed."
    }
  },
  "required": [
    "band_name",
    "genre",
    "origin_city",
    "origin_country",
    "producer_name",
    "forming_year"
  ],
  "additionalProperties": false
}
