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
Mark Farrow: Mark Farrow was named Designer of the Year in the Creative Review Peer Poll in 2004, voting him ‘the most important graphic designer working today’.  His career began in the early 1980s designing experimental sleeves and posters for Factory Records, and The Haçienda, which placed him at the forefront of contemporary music graphic design.  This has since continued with a longstanding creative partnership with Pet Shop Boys, and other bands such as Spiritualized.  He designed the cover for "Everything Must Go" (1996), the breakthrough album by the Manic Street Preachers.  His minimalist approach, and a rigorous, highly precise attention to detail defines his aesthetic, and appeals to a broad spectrum of clients, from museums and galleries to pop music and retail, product designers and architects, to restaurateurs and artists.  In 2009 he was given the honour of Royal Designer for Industry (RDI) by the RSA.

Take the Skinheads Bowling: "Take the Skinheads Bowling" is the signature song of Santa Cruz, California alternative rock band Camper Van Beethoven, written by David Lowery and released on their 1985 album "Telephone Free Landslide Victory".  The song (as covered by the band Teenage Fanclub) was notably featured in the Michael Moore documentary "Bowling for Columbine", and received substantial airplay on KROQ, and BBC Radio 2, as well as The Dr. Demento Show.  The song was also recorded by Welsh rock band Manic Street Preachers as a B-side to their 1996 single "Australia" and subsequently included on their B-side compilation album "Lipstick Traces (A Secret History of Manic Street Preachers)".

Music of the Gran Turismo series: "Gran Turismo" featured two different opening songs.  For the North American and PAL versions is a Chemical Brothers remix of the Manic Street Preachers song Everything Must Go.  The opening music for the Japanese version is "Moon Over The Castle", composed by Masahiro Andoh; this music is used for the opening movie in the Japanese version of every "Gran Turismo" primary game to date (as well as the Asian version of Gran Turismo 4).  The North American and PAL versions of the game featured a soundtrack composed of instrumentals and famous bands, whereas the Japanese version used the "Gran Turismo Original Soundtrack", a completely original score.

Journal for Plague Lovers: Journal for Plague Lovers is the ninth studio album by Welsh alternative rock band Manic Street Preachers, released in May 2009 by record label Columbia.  Recorded between October 2008 and February 2009 and produced by Steve Albini and Dave Eringa, it features exclusively posthumous lyrics by Richey Edwards, who disappeared on 1 February 1995 and was presumed deceased in 2008.  It is the only Manic Street Preachers album in which the lyrics for every song were written solely by Edwards.

Manic Street Preachers: Manic Street Preachers are a Welsh alternative rock band, formed in 1986 in Blackwood, Caerphilly and consisting of James Dean Bradfield (lead vocals, lead guitar), Nicky Wire (bass guitar, lyrics) and Sean Moore (drums, percussion).  They are often colloquially known as the Manics.  Following the release of their first single, "Suicide Alley", the band was joined by Richey Edwards as co-lyricist and rhythm guitarist.  The band's early albums were in a punk vein, eventually broadening to a greater alternative rock sound, whilst retaining a leftist politicisation.  Their early combination of androgynous glam imagery and lyrics about "culture, alienation, boredom and despair" has gained them a loyal following and cult status.

Leaving the 20th Century: Leaving the 20th Century is a recording of the Manic Millennium concert by the Welsh rock band Manic Street Preachers, released 2000.  The concert, which also celebrated the 10th anniversary of the band, was performed on the New Year's Eve night 1999-2000 at the Millennium Stadium in Cardiff, in front of more than 57,000 fans.  The event became international as the final song of the event was broadcast live all over the world through satellites.

Heineken Music Festival: In the early to mid-1990s the Heineken Brewery sponsored a number of free live music festivals each year in the United Kingdom.  Taking place in venues such as Avenham Park in Preston and Roundhay Park in Leeds, the Heineken Music Festival featured Britpop acts such as Oasis, Pulp, Manic Street Preachers, Blur, Inspiral Carpets, The Boo Radleys and Catatonia.  Also long-established bands including The Stranglers, Jools Holland, The Pogues, Saw Doctors, Tom Robinson Band and Mike + The Mechanics.  In total there were thirty events over six years, all of four days duration.  The last event was in Leeds in July 1995, which attracted 110,000 fans on the Saturday, and 300,000 over four days after which Heineken withdrew their sponsorship.  Various events still continue under different names.

Malfunkshun: Malfunkshun is an alternative rock band formed on Easter Sunday in 1980 by Andrew Wood and his brother Kevin Wood and is often recognized as one of the "Founding Fathers of the grunge scene" or the "Godfathers of Grunge".  They formed around the same time bands such as The U-Men (1981), Melvins (1983), Green River (1984) and Soundgarden (1984).

National Treasures – The Complete Singles: National Treasures – The Complete Singles is a compilation album by the Welsh alternative rock band Manic Street Preachers, released on 31 October 2011.  It is the band's third compilation album, after "Forever Delayed: Manic Street Preachers, The Greatest Hits" (2002), and the B-sides/rarities collection "Lipstick Traces (A Secret History of Manic Street Preachers)" (2003).  The compilation features one new recording, a cover of The The's "This is the Day", which was issued as a single on 18 September 2011.  The compilation reached number 10 on the UK Album Chart in November 2011.

Craig Pruess: Craig Pruess (born 1950) is an American composer, musician, arranger and gold & platinum record producer who has been living in Britain since 1973.  His career has covered diverse areas including: record production for international stars such as Anu Malik, Sir Cliff Richard, Sarah Brightman, Sheila Walsh (whose first album, "War of Love" was produced and arranged by Craig and was nominated for a Grammy Award in 1983); musical arrangements for Massive Attack, Def Leppard, Bond; feature film soundtrack music ("Bride & Prejudice", "Bend It Like Beckham", "It's a Wonderful Afterlife", "What's Cooking? ", "Bhaji on the Beach"); world music producing, performing (sitar, keyboards and African percussion) and arranging for international acts such as Massive Attack, Katie Melua, Manic Street Preachers, Def Leppard and Pascal Obispo; television music ("Peak Practice", Sue Lawley Show, Rich Deceiver, ZigZag Kenya, Samson Superslug) and also arranging, sitar and sound design work (for such well known composers as Danny Elfman, Gabriel Yared, Patrick Doyle, Carl Davis, John Altman, Rachel Portman, and George Fenton); television and film advertising/corporate music (over 300 commercials to date); lecturing and teaching; concert performing (solo and with his own ensembles but also with Mike Oldfield for the world premiere of "Tubular Bells II", September 1992, at the Edinburgh Castle); sound engineering, synthesizer and computer music programming, sound design and music technology innovations.

Question: Are Malfunkshun and Manic Street Preachers both in the same genre of music?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "genre"
      ],
      "additionalProperties": false
    },
    "band_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "genre": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "genre"
      ],
      "additionalProperties": false
    },
    "share_genre": {
      "type": "boolean"
    },
    "shared_genre_name": {
      "type": "string"
    }
  },
  "required": [
    "band_1",
    "band_2",
    "share_genre",
    "shared_genre_name"
  ],
  "additionalProperties": false
}
