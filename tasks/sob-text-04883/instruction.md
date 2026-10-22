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
Beheaded (album): Beheaded is the second studio album by Texas-based indie rock band Bedhead, which was released on October 24, 1996 through Trance Syndicate.  The album was released in the United Kingdom through Rough Trade, and was reissued on compact disc format through Touch & Go Records on February 20, 2001 along with the band's other two albums "WhatFunLifeWas" and "Transaction de Novo".  The album was included in the Numero Group's 2014 boxset "Bedhead: 1992–1998" and was also released separately on LP format.

Bedhead (band): Bedhead was an American, Texas-based indie rock band, active from 1991 to 1998.  Members consisted of Matt and Bubba Kadane (vocals and guitar), Tench Coxe (guitar), Kris Wheat (bass), and Trini Martinez (drums).  The band released several EPs and three LPs on Trance Syndicate, touring intermittently.  Bedhead's music was generally subdued, with three electric guitars and one electric bass guitar over sung or spoken vocals.  Allmusic dubbed the group "the quintessential indie rock band," and "Tiny Mix Tapes" gave their final album "Transaction de Novo" a perfect 5/5 score.

Use Me (Hinder song): "Use Me" is the first single from the American rock band Hinder's 2008 album, "Take It to the Limit".  It was released as a digital download through the band's website on July 15, 2008, and made available on iTunes on July 29, 2008.  It is one of the songs that marked a change in direction in Hinder's music, transitioning from post-grunge to more of a glam metal sound, while still retaining the post-grunge and hard rock influences that were used on Hinder's previous album, "Extreme Behavior". The song was put on as downloadable content for the video games and Rock Band 2.

Demons (band): Demons are a punk rock/garage punk band from Sweden.  The band includes quotation marks in their name to differentiate themselves from other bands with a similar name.  Their music has been described as "punk 'n' roll", but the band claims it should only be described as high-energy rock.  Their musical style relies heavily on the energy derived from punk rock.  Influences include 1960s garage rock bands such as The Sonics, The Standells and Shadows of Knight, The Velvet Underground, The Stooges and New York Dolls; and punk rock bands such as The Damned, The Heartbreakers and The Saints; and early hardcore punk bands such as Black Flag, Bad Brains and Dead Kennedys.  "Demons" has often been compared to contemporary groups like New Bomb Turks, The Hellacopters and Electric Frankenstein.

Hinder: Hinder is an American rock band from Oklahoma that was formed in 2001 by lead singer Austin Winkler, lead guitarist Joe "Blower" Garvey, and drummer Cody Hanson.  The band released four studio albums with Winkler; "Extreme Behavior" (2005), "Take It to the Limit" (2008), "All American Nightmare" (2010) and "Welcome to the Freakshow" (2012).  Winkler left the band in 2013, and "When The Smoke Clears" (2015) was Hinder's first album featuring new lead vocalist Marshal Dutton.

Haitian rock: Haitian rock, or rock kreyòl, started as rock n roll in Haiti in the early 1960s.  It was played by rock bands called "yeye" bands.  The name "yeye" derives from the Beatles lyrical verse, "yeah, yeah, yeah", which took off in the United States and was listened to by upper class Haitian families who had access to the radio.  Young Haitians formed small electric guitar-based bands.  These "yeye" rock bands were short-lived, as the addition of "compas" to their repertoires resulted in a sound was called mini-jazz, or "mini-djaz" in creole.

Austin John: Austin John Winkler (born October 25, 1981) is an American singer-songwriter best known for being the former lead singer of the American rock band Hinder.  Winkler was one of the founding members of Hinder and recorded a total of one EP, four studio albums and released twenty-four singles to radio while with them during his 12-year tenure with the band.  Since his departure from Hinder, Winkler has continued his career, but as a solo artist.

G.a.s. Drummers: G.a.s. Drummers was a melodic hardcore band formed in Jerez de la Frontera, Spain at the end of 1997 by three teenagers who stood out from their other students due to their colourful hair dies and their taste in the california punk rock bands such as Bad Religion, Operation Ivy, NOFX, Lagwagon, The Descendents etc.  Original members from other small local bands Dani Llamas (guitar and vocals), Pakomoto (Bass and vocals) and Rafa Camison (Drums) started playing together and composing their own music and after one year of sending demos around the country they got put as the opening act for Swedish Punk Rock band Randy on their Spanish tour.  A tour that took the band through the whole country helping a lot of Spanish kids discover that there were actually Spanish bands capable of sounding as good as some of their favorite American bands.  This lead immediately the band to sign to a young record label called Slide Chorus Records a young emerging record label from Madrid which would start releasing albums for other Spanish Punk Rock bands.  This first release titled Proud To Be Nothing hit the streets at the end of 1999 and was presented on their first European tour which covered Spain, Great Britain, France and the Netherlands amongst Spanish punk rock legend[P.P.M.

Vandarth: Vandarth (born Nathan Snyder; September 15, 1986) is a solo musician from Indianapolis, Indiana.  He is also the lead vocalist and guitarist in the band Project Hero.  His music is influenced by a variety of bands including Avenged Sevenfold, Foo Fighters, Weezer, Against Me! , and Coldplay.  Vandarth is primarily an original artist.  He has released several solo albums, most notably 2009's "The Escape", but he has also released a series of covers.  He has opened for rock bands such as Hinder, Disciple, Three Days Grace, and many more.

Matt and Bubba Kadane: Matt and Bubba Kadane is an American musical duo that consists of two brothers, Matt Kadane and Bubba Kadane.  They have founded three indie rock bands, serving as producers, songwriters, vocalists, and guitarists in all of them.  The first, Bedhead, released three well-received studio LPs before it was disbanded.  The brothers reformed as The New Year in 2001, and in 2012 they formed the group Overseas with David Bazan and Will Johnson.

Question: Were Bedhead and Hinder both rock bands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "band_names": {
      "type": "array",
      "description": "List of band names mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "band_details": {
      "type": "array",
      "description": "Details for each band mentioned, including their genre.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "is_rock_band": {
            "type": "boolean",
            "description": "True if the band is described as a rock band or a subgenre of rock."
          },
          "genre_description": {
            "type": "string",
            "description": "The specific genre description from the context."
          }
        },
        "required": [
          "band_name",
          "is_rock_band",
          "genre_description"
        ],
        "additionalProperties": false
      }
    },
    "all_are_rock_bands": {
      "type": "boolean",
      "description": "True if all bands in the question are identified as rock bands."
    }
  },
  "required": [
    "question_asked",
    "band_names",
    "band_details",
    "all_are_rock_bands"
  ],
  "additionalProperties": false
}
