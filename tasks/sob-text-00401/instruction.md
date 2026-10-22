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
Arthur's Club-Geneve 1995: Arthur's Club-Geneve 1995 was a 75-minute performance in Geneva by blues guitarist Mick Taylor, featuring Snowy White, recorded for a television special and a promotional album.  It consists of a collections of blues classics, a Jimi Hendrix song and a Rolling Stones song with long jams.

The Rolling Stones No. 2: The Rolling Stones No. 2 is the second UK album by the Rolling Stones released in 1965 following the massive success of 1964's debut "The Rolling Stones".  It followed its predecessor's tendency to largely feature R&B covers.  However, it does contain three compositions from the still-developing Mick Jagger/Keith Richards songwriting team.  On Dutch and German pressings of the album, the title is listed as "The Rolling Stones Vol.  2" on the front cover, although the back of the album cover lists the title as "The Rolling Stones No. 2".

Amazing Atomic Activity: Amazing Atomic Activity is the eighth studio album by Polish thrash metal band Acid Drinkers.  It was released on May 17, 1999.  The promotional single of the album was the song "Satisfaction", which is a cover of The Rolling Stones song "(I Can't Get No) Satisfaction".  It is the first album to feature rhythm guitarist Przemek "Perła" Wejmann.

Coca-Cola C2: Coca-Cola C2 (also referred to as Coke C2, C2 Cola, or simply C2) was a cola-flavored beverage introduced by The Coca-Cola Company first in Japan, then later on June 7, 2004 in the United States (and shortly thereafter, Canada), in response to the low-carbohydrate diet trend.  This Coke product was marketed as having half the carbohydrates, sugars and calories compared to standard Coca-Cola.  It contains aspartame, acesulfame potassium, and sucralose in addition to the high fructose corn syrup typically found in cola beverages distributed in America.  Aside from the high fructose corn syrup, one 12-ounce can of Coca Cola C2 contains 19 mg of aspartame, 4 mg of sucralose and 19 mg of acesulfame potassium.  The packaging design differs from other Coke products in that the logos are printed in black.  For marketing on radio and television, and movie theaters the Queen song "I Want to Break Free" was used.  When it was first introduced, though, The Rolling Stones song "You Can't Always Get What You Want" was used.

Beatles and Rolling Stones rivalry: "The Beatles" and "The Rolling Stones" were arguably the biggest bands of the 1960s.  Both bands started their careers in the early 1960s in the United Kingdom and rose to fame as part of the British invasion.  The Beatles rose to fame in the UK in 1963 with their singles "Please Please Me" and 'Love Me Do".  After a successful album contract the band decided to leave Liverpool and move to London.  The Rolling Stones were a struggling band at the time and the Beatles had become famous as a self contained Rock Band.  Original song content was getting tougher to acquire in the United Kingdom so the Rolling Stones were a Rock and Roll Blues cover group.  On meeting the Beatles at a London Pub; John Lennon and Paul McCartney agreed to write an original single for the Rolling Stones called "I Wanna Be Your Man".  The song gave the Stones their first commercial success and Mick Jagger and Keith Richards began writing as well.

Sympathy for the Devil (album): Sympathy for the Devil is a compilation album by Laibach and follows on from their Beatles cover album Let It Be.  "Sympathy for the Devil" features seven cover versions of the Rolling Stones song "Sympathy for the Devil" and one original Laibach track.  The tracks are recorded both by Laibach and a variety of side projects with Laibach members (including Dreihunderttausend Verschiedene Krawalle and Germania).

Sympathy for the Devil: "Sympathy for the Devil" is a samba rock song by the Rolling Stones, written by Mick Jagger and Keith Richards.  Sung by Jagger, the song is an homage to the Devil, written in the first-person narrative from his point of view, recounting atrocities committed throughout the history of humanity.  It is performed in a rock arrangement with a samba rhythm.  It first appeared as the opening track on their 1968 album "Beggars Banquet". " Rolling Stone" magazine placed it at number 32 in its list of the "500 Greatest Songs of All Time".

VH1 Presents: The Corrs, Live in Dublin: VH1 Presents: The Corrs, Live In Dublin is an album which is a live performance performed by the Irish pop rock band, The Corrs in Dublin, Ireland who are accompanied by the Irish Film Orchestra.  The Corrs have performed previous released songs with a slight remix into it.  Also, this album highlights include two duets with Bono of U2 — performing Ryan Adams' "When the Stars Go Blue", and the Lee Hazlewood/Nancy Sinatra song "Summer Wine".  The Corrs also perform Jimi Hendrix's "Little Wing", featuring a guitar solo by Ronnie Wood who later also performs alongside them for the Rolling Stones song "Ruby Tuesday".

Science &amp; Nature (Inkubus Sukkubus album): Science & Nature is a full-length album released by the British Goth rock band Inkubus Sukkubus on September 24, 2007.  Sympathy for the Devil is a cover of a Rolling Stones song.

Taste of Conium: Taste of Conium is the second album by Greek progressive/Blues rock group, Socrates Drank the Conium.  The album was released in 1973.  It features a thirteen-minute cover of The Rolling Stones song (I Can't Get No) Satisfaction, retitled "Wild Satisfaction".  The album was followed by On the Wings.

Question: Science & Nature includes a cover of a Rolling Stones song written by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album that includes the cover song."
    },
    "covered_song_title": {
      "type": "string",
      "description": "The title of the Rolling Stones song that was covered."
    },
    "original_artist": {
      "type": "string",
      "description": "The original artist of the covered song."
    },
    "songwriters": {
      "type": "array",
      "description": "A list of the individuals who wrote the covered song.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the songwriter."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "album_name",
    "covered_song_title",
    "original_artist",
    "songwriters"
  ],
  "additionalProperties": false
}
