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
Jim Couza: Jim Couza was an American hammered dulcimer player born in New Bedford, Massachusetts, April 27, 1945 and resident in England since 1982; he died in 2009.  In addition to the hammered dulcimer, Couza also played Appalachian dulcimer and guitar.  He made several recordings, both solo and with the D'Uberville Ramblers.  He also worked with Björk on the album Post, and with Peter Gabriel on OVO (Couza is featured on a track called "The Time Of The Turning (reprise) / Weavers Reel").  He also worked with Celtic singer songwriter Jim Fox, performing at many venues and festivals around the UK.  Couza suffered a number of health problems in recent years resulting in amputation of both his legs.  He died on 2 August 2009.

Brenda Hunter: Brenda J. Hunter is an American musician and composer best known as a hammered dulcimer player.  She also plays Irish fiddle, Celtic harp, and classical piano, with the latter influence evident in her particular style on the dulcimer and harp.  She won the National Championship in 1995 at the Walnut Valley Festival in Winfield, Kansas, receiving as her prize a Masterworks hammered dulcimer built by Russell Cook.  She has also played a Rick Thum instrument, and currently uses a Nick Blanton Compact model on stage.  She performs and teaches nationally on hammered dulcimer, also performs on solo Celtic harp, plays fiddle and hammered dulcimer with Celtic trio Banshee in the Kitchen, and was previously with Celtic duo Briar Rose.

Contemporary folk music: Contemporary folk music refers to a wide variety of genres that emerged in the mid 20th century and afterwards which were associated with traditional folk music.  Starting in the mid-20th century a new form of popular folk music evolved from traditional folk music.  This process and period is called the (second) folk revival and reached a zenith in the 1960s.  The most common name for this new form of music is also "folk music", but is often called "contemporary folk music" or "folk revival music" to make the distinction.  The transition was somewhat centered in the US and is also called the American folk music revival.  Fusion genres such as folk rock, folktronica, and others also evolved within this phenomenon.  While contemporary folk music is a genre generally distinct from traditional folk music, it often shares the same English name, performers and venues as traditional folk music; even individual songs may be a blend of the two.

Jean Ritchie: Jean Ritchie (December 8, 1922 – June 1, 2015) was an American folk music singer, songwriter, and Appalachian dulcimer player.  Her career formed a kind of bridge between the traditional and modern forms of folk music: in her youth she learned folksongs in the traditional way (orally, from her family and members of her community); and in adulthood she became a successful modern folksinger, promulgating songs in public through concerts and recordings.  She was called by some the "Mother of Folk".

Andrew Rowan Summers: Andrew Rowan Summers (December 15, 1912– March 1968) was an American folk singer and player of the Appalachian dulcimer.  He is credited with a large role in preserving Appalachian music from extinction.  Summers was among the earliest musicians to draw attention to the dulcimer to a wider audience outside the Appalachians, with John Jacob Niles being one of the few earlier.

Kevin Roth: Kevin Roth (born 1957 in Philadelphia, Pennsylvania) is an American folk singer and Appalachian dulcimer player who has released forty-five albums.

Stephen Seifert: Stephen Seifert (born September 29, 1973) is an American folk musician and virtuoso of the Appalachian dulcimer.  He has released many educational DVDs and videos on the subject of dulcimer playing.

David Massengill: David Massengill (born 1951, Bristol, Tennessee) is an American folk singer-songwriter, guitar and appalachian dulcimer player.  His best-known songs include: "On The Road to Fairfax County", recorded by The Roches and by Joan Baez; "The Great American Dream"; and "My Name Joe", about an illegal immigrant restaurant worker.  For some years after he began recording, Massengill maintained a day job as a restaurant dishwasher.  He also contributed his poignant dulcimer-centered version of "The Crucifixion" to 2001's multi-artist double-disc tribute to Phil Ochs, "What's That I Hear".

Joemy Wilson: Joemy Wilson is a hammered dulcimer player from New Haven, Connecticut.  Her first instruments were the piano and violin.  She also took voice lessons in high school.  She started playing Appalachian dulcimer while attending Barnard College, and started playing hammered dulcimer in 1979.

Brightest and Best: "Brightest and Best" (occasionally rendered by its first line, "Brightest and Best of the Sons of the Morning") is a Christian hymn written in 1811 by the Anglican bishop Reginald Heber to be sung at the feast of Epiphany.  It appeared in Heber's widow's compilation of hymns entitled "Hymns Written and Adapted to the Weekly Service of the Church Year" in 1827.  It can be sung to a number of tunes, including "Morning Star" by James P. Harding, "Epiphany" by Joseph Thrupp, and "Star in the East" by William Walker.  It appears in "The Lutheran Hymnal", and appeared in the 1966 Methodist hymnal.  It has been recorded by a number of artists, including Glen Campbell, Joanne Hogg and Kathy Mattea (on her album "Good News").  The Kentucky traditional singer Jean Ritchie often sang this and told of her childhood memory of her grandmother sitting by the fire and singing it quietly to herself on Twelfth Night; the Library of Congress collected it from her in 1951.

Question: What American folk music singer, songwriter, and Appalachian dulcimer player, often sang the Christian hymn Brightest and Best?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the American folk musician."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the musician."
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of roles the musician held."
    },
    "primary_instrument": {
      "type": "string",
      "description": "The primary instrument the musician played, as specified in the question."
    },
    "hymn_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the hymn."
        },
        "genre": {
          "type": "string",
          "description": "The genre or type of the hymn."
        },
        "writer": {
          "type": "string",
          "description": "The writer of the hymn."
        }
      },
      "required": [
        "title",
        "genre",
        "writer"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "musician_name",
    "nationality",
    "roles",
    "primary_instrument",
    "hymn_details"
  ],
  "additionalProperties": false
}
