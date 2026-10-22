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
Till Death Do Us Part (Geto Boys album): Till Death Do Us Part is the fourth studio album by the Houston gangsta rap group the Geto Boys, released in March 1993 on Rap-A-Lot Records.  Rapper Willie D had left the group in 1992 temporarily to pursue a solo career.  In his position, fellow Rap-A-Lot member Big Mike joined Scarface and Bushwick Bill for this album.  "Till Death Do Us Part" became the group's first #1 on the R&B/hip hop charts, and also included the group's second top 40 "Billboard" Hot 100 single, "Six Feet Deep" (which used a sample from The Commodores' 1977 hit single "Easy").  Other singles released from the album were "Crooked Officer" and "Straight Gangstaism".

L.T.D. (band): L.T.D. is an American R&B/funk band best known for their 1977 hit single, "(Every Time I Turn Around) Back in Love Again" and "Holding On (When Love Is Gone)", as well as their many ballads, such as "Love Ballad", "We Both Deserve Each Other's Love", and "Where Did We Go Wrong?" .

Swayin' to the Music (Slow Dancing): "Swayin' to the Music (Slow Dancin')" or "Slow Dancin' (Swayin' to the Music)" is a 1977 hit single by Johnny Rivers.  It was his last Top 40 hit in the United States, and became his second Gold record.

Yes Sir, I Can Boogie: "Yes Sir, I Can Boogie" is a 1977 hit single by the Spanish vocal duo Baccara.

Atlanta Rhythm Section: Atlanta Rhythm Section (or ARS) is an American southern rock band, formed in 1971 by Rodney Justo (singer), Barry Bailey (guitar), Paul Goddard (bass), Dean Daughtry (keyboards), Robert Nix (drums) and J.R. Cobb (guitar).  The band's current lineup consists of Daughtry and Justo, along with guitarists David Anderson and Steve Stone, bassist Justin Senker and drummer Rodger Stephan.

Swingtown (song): "Swingtown" is a 1977 hit song by the Steve Miller Band.  It was their third and final single release from their "Book of Dreams" album, and became the second biggest hit from the LP.

Don't Stop (Fleetwood Mac song): "Don't Stop" is a song by the British-American rock band Fleetwood Mac, written by vocalist and keyboard player Christine McVie.  Sung by guitarist Lindsey Buckingham and McVie, it was a single taken from the band's 1977 hit album, "Rumours".  It is one of the band's most enduring hits, peaking at No. 3 on the "Billboard" singles chart.  In the UK market, "Don't Stop" followed "Go Your Own Way" as the second single from "Rumours" and peaked at No. 32.  In the US, it was the third single released, and peaked at No. 3 in October 1977.

So in to You: "So in to You" is a 1977 hit single by the Atlanta Rhythm Section.  It was the first release from their sixth studio LP, "A Rock and Roll Alternative".

Heaven On The 7th Floor: "Heaven on the 7th Floor" is a 1977 hit single by British singer Paul Nicholas.  It was his greatest hit, a track from his eponymous debut LP.  The song spent three weeks at number 6 on the U.S. "Billboard" Hot 100.  during November and December of that year.  "Heaven On The 7th Floor" became a Gold record.  It reached number 49 in Canada.

Alessi Brothers: The Alessi Brothers (also known as simply 'Alessi') are an American pop rock singer-songwriter duo who first came to international prominence with their 1977 hit single "Oh Lori".  The duo are identical twin brothers, Billy and Bobby Alessi (born 12 July 1953, West Hempstead, New York).

Question: "So in to You" is a 1977 hit single by a band formed in whichyear ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the hit song."
    },
    "artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band or artist."
        },
        "formation_year": {
          "type": "integer",
          "description": "The year the band was formed."
        }
      },
      "required": [
        "name",
        "formation_year"
      ],
      "additionalProperties": false
    },
    "hit_year": {
      "type": "integer",
      "description": "The year the song was a hit single."
    }
  },
  "required": [
    "song_title",
    "artist",
    "hit_year"
  ],
  "additionalProperties": false
}
