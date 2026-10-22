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
Our Bright Future: Our Bright Future is Tracy Chapman's eighth studio album and was released on November 11, 2008.  The album was co-produced by Larry Klein.  The album's first single "Sing For You" was released digitally on October 31.  In promotion for this album, Chapman appeared on radio stations across Europe with interviews and sessions.  Chapman also performed "Sing for You" on "The Tonight Show with Jay Leno".  A European tour in support of the disc took place through November and December 2008.  A U.S. tour was planned for January 2009 but was postponed.  Chapman toured Europe again in the Summer of 2009.  "Our Bright Future" was certified Gold in France for sales in excess of 100,000 copies.  The album was nominated for the Grammy Award for Best Contemporary Folk Album.  To date, it is Chapman's latest record.

The Long Way Home (Terri Clark album): The Long Way Home is the seventh studio album by Canadian country music artist Terri Clark.  The album was released on September 1, 2009 in Canada and through digital retailers in United States and was released to other American retailers on October 20.  It produced four singles: "Gypsy Boots," "If You Want Fire," "A Million Ways to Run" and "You Tell Me."  Additionally, "The One You Love" was originally released on her fifth studio album, "Pain to Kill", but was re-recorded for "The Long Way Home" to include Vince Gill on background vocals.

Deniz Koyu: KO:YU aka Deniz Koyu (born as Deniz Akcakoyunlu in Bochum, Germany) is a Turkish/German DJ and electronic dance music producer who specializes in progressive house and electro house.  He has received worldwide support from acclaimed DJs such as Avicii, Swedish House Mafia, Tiësto, Dada Life and Fedde le Grand and was named an EDM artist to watch in 2012 by MTV.  Getting into EDM(at age 18), he previously enjoyed pop music and indie pop.  He lists Daft Punk, disco house and later on progressive and electro house as influences.  His track "Tung!"  is the most worldwide known from his Discography.  He now produces under the name "KO:YU".  His latest release under this alias is "A Way Home" with Don Palm on Spinnin' Records.

Take the Floor (Scottish radio programme): Take the Floor is the name of a radio programme airing on BBC Radio Scotland.  It is the longest-running radio programme in Scotland, dating back to the 1930s when it was called Scottish Dance Music and broadcast by the Scottish Home Service.  The programme was given its present name of Take the Floor in 1978 by Chris Worrall, a Music Producer with BBC Radio Scotland (1978-82), who introduced 'live sessions' and 'programme road shows' touring Scotland, together with player interviews, an events diary and reviews of latest record/CD releases.  The original programme was presented by David Findlay until his death in 1981 and then by Robbie Shepherd until he stepped down in 2016.  In keeping with its predecessor, the current programme also features live sessions from top dance bands, individual musicians and vocalists from across the country.  The host of the programme is Gary Innes.  The programme airs on Saturday evenings and is repeated on Sunday afternoons.  Its theme music is traditional Scottish reel "Kate Dalrymple".

Benediction (band): Benediction are a British death metal band formed in 1989.  In October 2001 they released with Nuclear Blast the album "Organised Chaos".  This is the first album with the new vocalist Dave Hunt.  Their latest record is "Killing Music", released in 2008.

The Datsuns: The Datsuns are a hard rock band from Cambridge, New Zealand, formed in 2000.  To date they have released six albums and several singles, most of which have charted in New Zealand and/or the United Kingdom.  "Deep Sleep", their latest record was released in October 2014.

Picture Perfect (Sevendust song): "Picture Perfect" is a song by the American alternative metal band Sevendust.  It was released as the second single from their ninth studio album, Black Out the Sun on August 6, 2013.  The song has not been performed at the band's concerts, yet.  Also this was one of the earliest riffs that the band worked on their latest record.

No Lucifer: "No Lucifer" is a 10" single released by rock band British Sea Power on 10 March 2008.  It was the second single released from their critically acclaimed third album, "Do You Like Rock Music? ".  The song was written by Hamilton, who also sings on the track.  It is the first track written and fronted by Hamilton to be officially released as an A-side single in the UK, although during promotion for "Open Season", the track "How Will I Find My Way Home" was intended for single release before being cancelled by the band's record label.

Benjamin B: Guitar rock band Benjamin B was founded in 1994 in Winschoten, the Netherlands.  After releasing two albums on Excelsior Recordings, the band released its latest record "Tired of the Moon" on Living Room Records.

Spinnin' Records: Spinnin' Records is a Dutch record label, founded in 1999 by Eelko van Kooten and Roger de Graaf.

Question: What is the ethnicity of the record label which released Deniz Koyu's latest record, "A Way Home"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "record_title": {
      "type": "string",
      "description": "The title of the record."
    },
    "record_label": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the record label."
        },
        "origin_country": {
          "type": "string",
          "description": "The country of origin of the record label."
        }
      },
      "required": [
        "name",
        "origin_country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_name",
    "record_title",
    "record_label"
  ],
  "additionalProperties": false
}
