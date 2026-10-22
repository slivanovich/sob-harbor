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
Paul Waaktaar-Savoy: Paul Waaktaar-Savoy (born Pål Waaktaar Gamst, 6 September 1961) is a Norwegian musician and songwriter.  He was named Knights First Class of the Order of St. Olav by King Harald for his services to Norwegian music and his international success.  Pål Savoy is best known for his work as the main songwriter and guitarist in the Norwegian pop band A-ha.  He has written or co-written most of the band's biggest hits, including "The Sun Always Shines on T.V.", "Hunting High and Low", "Take On Me", the James Bond theme "The Living Daylights" and the ballad "Summer Moved On".  In addition, Waaktaar-Savoy is also a painter.  The band A-ha has sold more than 50 million albums worldwide.

A Dot of Black in the Blue of Your Bliss: A Dot Of Black In The Blue Of Your Bliss is the second solo album of Norwegian band a-ha's Magne Furuholmen as Magne F.

A-ha: A-ha (usually stylized as a"-h"a; ] ) is a Norwegian band formed in Oslo in 1982.  The band was founded by Morten Harket (vocals), Magne Furuholmen (keyboards) and Pål Waaktaar-Savoy (guitars).  The group rose to fame during the mid-1980s after being discovered by musician and producer John Ratcliff, and continued global success in the 1990s and 2000s.

Morten Harket: Morten Harket (born 14 September 1960) is a Norwegian musician, best known as the lead singer of the synthpop/rock band A-ha, which released ten studio albums and topped the charts internationally after their breakthrough hit "Take on Me" in 1985.  A-ha disbanded in 2010 after they played their last gig in Oslo.  In 2015, after each member pursued his own artistic path, a-ha reunited to produce a new album, "Cast In Steel", and perform a world tour, kicking off at Rock in Rio in Rio de Janeiro, Brazil on 27 September 2015.  Harket has also released six solo albums.  Before joining A-ha in 1982, Harket had appeared on the Oslo club scene as the singer for blues outfit Souldier Blue.

Analogue (album): Analogue is the eighth studio album by the Norwegian band A-ha, released in 2005.  It is aha's first album on Polydor Records (Universal), having previously been signed to Warner Music.  Four singles were also released from this record.  The album's second single, "Analogue (All I Want)" became the group's first top 10 hit on the UK Singles Chart since "Stay on These Roads" (1988).  The album reached #24 in the UK and got silver certification there.

List of awards and nominations received by A-ha: This is a comprehensive list of major music awards received by A-ha, a Norwegian new wave band.  Formed in 1982 by Morten Harket, Magne Furuholmen, and Paul Waaktaar-Savoy, A-ha have been one of the most popular European acts in the world since the mid-1980s.  The band has sold more than 100 million albums and singles worldwide, and has been nominated for one Grammy Award, more than any other Norwegian rock band.

Celice (song): "Celice" is a song by Norwegian band A-ha.  Written by Magne Furuholmen and Martin Terefe, it was released as the first single from the album, "Analogue", throughout Europe.  It was released on 7 October 2005 in Germany and Norway, and 24 October in Sweden.  It was not released in the UK.  It reached worldwide sales of over 300,000 units.  For a while the song was under consideration to be included on the Da Vinci Code movie soundtrack.

Magne Furuholmen: Magne Furuholmen (born 1 November 1962) is a Norwegian musician and visual artist.  Furuholmen, better known to music fans by his stage name Mags, is the keyboardist of the synthpop/rock band A-ha, and co-wrote many of the band's hits including "Take on Me", "Stay on These Roads", "Manhattan Skyline", "Cry Wolf", "Forever Not Yours", "Analogue (All I Want)", and "Foot of the Mountain".

Apparatjik: Apparatjik ( ) are a multi-national band formed in 2008.  The band is a supergroup that consists of bassist Guy Berryman from Coldplay, guitarist/keyboardist Magne Furuholmen from A-ha, singer/guitarist Jonas Bjerre of Mew and drummer/producer Martin Terefe.  The band's name literal translation is "agent of the apparatus".  Apparatjik is based on apparatchik, which is a word of Russian origin and is used to describe "an official or bureaucrat in any organization" but has in the past had other meanings, including "Communist agent or spy".

Past Perfect Future Tense: Past Perfect Future Tense is the first solo album of Norwegian band a-ha's Magne Furuholmen as Magne F. Magne worked in this album with Coldplay members, Will Champion and Guy Berryman, also Travis member, Andy Dunlop.

Question: Past Perfect Future Tense is the first solo album of Norwegian band a-ha's Magne Furuholmen,  better known to music fans by what stage name?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The full name of the musician."
    },
    "stage_name": {
      "type": "string",
      "description": "The stage name by which the musician is better known."
    },
    "album_details": {
      "type": "object",
      "properties": {
        "album_title": {
          "type": "string",
          "description": "The title of the album mentioned."
        },
        "album_type": {
          "type": "string",
          "description": "The type of album (e.g., solo album)."
        }
      },
      "required": [
        "album_title",
        "album_type"
      ],
      "additionalProperties": false
    },
    "band_affiliation": {
      "type": "string",
      "description": "The band the musician is associated with."
    }
  },
  "required": [
    "musician_name",
    "stage_name",
    "album_details",
    "band_affiliation"
  ],
  "additionalProperties": false
}
