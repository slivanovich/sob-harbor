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
Miracles in December: Miracles in December (Korean: 12월의 기적 ; ) is the overall second EP by South Korean-Chinese boy band Exo.  It was released by S.M. Entertainment on December 9, 2013.  Presented as a special winter album, "Miracles in December" is a follow-up to the group's first studio album "XOXO", which was released in June 2013.  Like all of the group's music, the EP has Korean and Chinese versions.  The EP is also the group's second release as well as first EP to be promoted extensively being as a combined group.  Its singles were "Miracles in December" and "Christmas Day".

Kim Jong-hyun (singer): Kim Jong-hyun (born April 8, 1990), better known by the mononym Jonghyun, is a South Korean singer-songwriter, and radio host.  He is a vocalist of the South Korean boy group Shinee, and has further participated in S.M. Entertainment's project group S.M.  The Ballad.  Jonghyun debuted as a solo artist on January 12, 2015, with his first EP, titled "Base".  In the same year, on September 17, Jonghyun released a compilation album, "Story Op.1".  On May 24, 2016, Jonghyun released his first studio album, "She Is", followed by his second compilation album, "Story Op.2" on April 24, 2017.

Base (EP): Base is the first EP of Korean boy band Shinee member Jonghyun, released on January 12, 2015 by S.M. Entertainment.

Anthem Lights (EP): Anthem Lights is the second EP by the American Christian boy band Anthem Lights.  It is the first EP released under the group's current name.  In addition to notable mentions, "Anthem Lights" has received very positive reviews.  "Can't Shut Up", the first track from "Anthem Lights", peaked at No. 42 on "Billboard"'s Christian Songs chart and at No. 27 on the CHR radio charts.

Cooking? Cooking!: Cooking?  Cooking!  (Korean: 요리왕 ), is the first EP by South Korean boy band Super Junior-H, sub-unit of Super Junior.  It was released on 5 June 2008 by SM Entertainment.  The mini album sold close to 2,000 copies within one day of release.  It was also released in Taiwan by Avex Taiwan on 11 July 2008.

Alive (Adler's Appetite EP): Alive is an EP released by American Hard Rock band Adler's Appetite on April 2, 2012.  It is a sequel to the band's first EP, the self-titled "Adler's Appetite" that was released in February 2005.  In 2010 the band released their single “Alive" on iTunes from their upcoming "Alive" EP that was slated to be released in 2011.  Also a radio edit of the Alder's Appetite's album's single "Alive" was released on July 29, 2010 in conjunction with Steven Adler's tell-all autobiography, "My Appetite for Destruction: Sex, and Drugs, and Guns N' Roses", and the band began recording the album in November 2011 in North Hollywood, California, and unlike the bands first EP which the band produced itself, "Alive" was produced by Cinderella band member and drummer Fred Coury, and was also recorded in a different studio as well.  The album was mixed by Adler's long time friend Anthony Focx, and was released under the record label "Down Boys Records".  There is a digital as well as a limited-edition physical release, as "Alive" is available in both CD and digital music formats.

Hō: Hō (鳳 , Phoenix ) is the first EP from Japanese nu metal/hardcore punk band Maximum the Hormone.  This was the second record and first EP of the band to feature the current lineup.  The EP also commonly goes by the title "Ootori".

DoraDora: DORADORA is the sixth extended play released by South Korean boy band U-KISS.  It is the first EP to be released after their 8 months hiatus due to their activities in Japan.  It was released on April 25, 2012.

Boy Band (TV series): Boy Band is an American television music competition series that premiered on June 22, 2017 on ABC.  The 10-episode first season features young male vocalists competing to become a member of a new five-piece boy band.  The final five boys who form the boy band receive a recording contract with Hollywood Records and perform the band's debut single during the finale.  On August 24, 2017, it was announced on the live show that Brady Tutton, Chance Perez, Drew Ramos, Sergio Calderon, and Michael Conor were the new members of the boy band, In Real Life.  They performed for the very first time their first single, "Eyes Closed".

Maktesløs: Maktesløs is the first EP by the Norwegian unblack metal band Frosthardr released in 2004.  The EP mixes the rawness of punkish old school black metal and the complicated song structures of progressive black metal.  "Death - My Relief" is often cited as the highlight of the EP.  The title track is an industrial music style intro, and the last song "Vandret" is an outro of the same style.  The cover art was designed by Samuel Durling, depicting a negative of a black and white graveyard photo, and a logo that contains a crossbow element.  Morten Magerøy of Vaakevandring and Antestor fame contributed some keyboards for the EP.  Collin of "Metal Storm" wrote about the album that "This first EP (that's also their first official release ever) proves that contrary to all expectations [that they were just another black metal band from Norway], Frosthardr is one of the most innovative and inventive bands I've heard this year (2005)."

Question: Base was the first EP by the singer-songwriter from which boy band?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ep_name": {
      "type": "string",
      "description": "The name of the Extended Play (EP)."
    },
    "artist_name": {
      "type": "string",
      "description": "The name of the artist who released the EP."
    },
    "artist_type": {
      "type": "string",
      "description": "The type of artist (e.g., singer-songwriter)."
    },
    "boy_band_name": {
      "type": "string",
      "description": "The name of the boy band the artist is a member of."
    },
    "release_date": {
      "type": "string",
      "format": "date",
      "description": "The release date of the EP."
    },
    "record_label": {
      "type": "string",
      "description": "The record label that released the EP."
    }
  },
  "required": [
    "ep_name",
    "artist_name",
    "artist_type",
    "boy_band_name",
    "release_date",
    "record_label"
  ],
  "additionalProperties": false
}
