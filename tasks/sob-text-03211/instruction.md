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
Bourne baronets: The Bourne Baronetcy, of Hackinsall Hall in the parish of Stalmine, and of Heathfield in the parish of Childwell, both in the County Palatine of Lancaster, was a title in the Baronetage of the United Kingdom.  It was created on 10 May 1880 for the Conservative Party politician James Bourne.  The title became extinct on the early death of his son, the second Baronet, in 1883.

Richard Ashcroft: Richard Paul Ashcroft (born 11 September 1971) is an English singer and songwriter.  He was the lead singer and occasional rhythm guitarist of the alternative rock band The Verve from their formation in 1990 until their original split in 1999.  He became a successful solo artist in his own right, releasing three UK top three solo albums.  The Verve reformed in 2007 but again broke up by summer 2009.  Ashcroft then founded a new band, RPA & The United Nations of Sound, and released a new album on 19 July 2010.  On 22 February 2016 Ashcroft announced his fourth solo album, "These People", set for release 20 May 2016.  Chris Martin of Coldplay has described Ashcroft as "the best singer in the world".

United Nations of Sound (album): United Nations of Sound is the debut album by British alternative rock band RPA & The United Nations of Sound (pseudonym of Richard Ashcroft, arrived at his fourth solo album), released on 19 July 2010 through Parlophone (see 2010 in British music).  The album was released in the United States on 22 March 2011 under the name "Richard Ashcroft" through the record company Razor & Tie.

James Bourne: James Elliot Bourne (born 13 September 1983 in Rochford, Essex, England) is an English singer-songwriter and co-founder of pop rock bands Busted and Son of Dork as well as a solo electronic project, Future Boy.  From 2013-2015 he was a member of supergroup McBusted, which consisted of himself, Busted bandmate Matt Willis, and McFly.

Keys to the World: Keys to the World is the third studio album by English singer-songwriter Richard Ashcroft.  It was released 23 January 2006, reaching number 2 in the UK Albums Chart (see 2006 in British music).  Ashcroft worked on the album at State of the Ark studios and Julian Kershaw wrote string arrangements for some of the songs later recorded by London Metropolitan Orchestra.  Strings are featured on 8 songs on the album which also features electric viola on some tracks – played by Bruce White.  The engineer/producer was Chris Potter.

A Song for the Lovers: "A Song for the Lovers" is a song by English singer-songwriter Richard Ashcroft and is the opening track on his 2000 album, "Alone with Everybody".  The song was also released on April 3, 2000 as the first single from that album in the United Kingdom (see 2000 in British music).  The single peaked at #3 in the UK Singles Chart, a position that would be matched by Ashcroft's 2006 single "Break the Night with Colour".

Rather Be (The Verve song): "Rather Be" is a song by English alternative rock band The Verve.  It is the third track on their fourth studio album, "Forth".  The song was released as the second single from the album on 17 November 2008, following summer hit "Love Is Noise".  Richard Ashcroft is credited for being the sole composer of the track, although as stated by band members the song has changed a lot since the initial version brought over by Ashcroft thanks to his companions' aid.

James Bourne discography: The discography of James Bourne, an English singer-songwriter.  He released three albums as a part of Busted, one with Son of Dork and has three forthcoming studio albums - one under his stage name Future Boy, another with new band Call Me When I'm 18 and now a new Busted album has been announced following their reunion announcement.  Bourne also worked for a while under the name Future Boy.

RPA &amp; The United Nations of Sound: RPA & The United Nations of Sound are a British alternative rock band formed by vocalist Richard Ashcroft, former lead singer of The Verve.  Ashcroft announced the formation of the band (which is a pseudonym more than a real band) and presented the video of the first single, "Are You Ready?" , on 18 January 2010 in an exclusive premiere on the "NME" website.  "Are You Ready?"  was released only in the UK on 1 April 2010 in a limited edition 12" vinyl.  On 9 April 2010 the band released a fanclub-only track, "Third Eye (Colombus Circle)".  In the first two weeks of June Ashcroft and his musicians completed a European tour (Ancona, Paris, Berlin, Cologne, Amsterdam, Manchester and London), then they played in Tokyo and Osaka on 7–8 August 2010 during the Summer Sonic Festival 2010 and also in Melbourne and Sydney respectively on 30 July and 31 July.  The band played in Australia also during the Splendour in the Grass Festival in late July.  The band's debut album as Richard's backing lineup, entitled "United Nations of Sound", was released on 19 July 2010.  "Born Again", the first proper single, was officially released the same day of the album as a digital download.

Volume 1 (Future Boy album): Volume 1 is the debut solo album from ex-Busted and Son of Dork band member James Bourne, under the name Future Boy.  The complete album was officially released via digital download on 3 June 2010.  Produced and mixed by Tommy Henriksen and James Bourne, Bourne describes the album as "100% electronic - and not a rock album".  The album had been previously released in two halves - with 'Side A' being released on 3 May, and 'Side B' being released on 1 June.  The album's artwork was designed and painted by Paul Karslake.  Bourne claims that the album will be released on CD at 'some point', but it will depend on 'when he has the cash'.  Bourne has promoted the album by being the supporting act for Twenty Twenty during their 2010 Clubs & Pubs Tour.

Question: Which singer has been part of more bands, Richard Ashcroft or James Bourne?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "singer_with_more_bands": {
      "type": "string",
      "description": "The name of the singer who has been part of more bands."
    },
    "singer_comparison": {
      "type": "array",
      "description": "Details for each singer, including their band count and band names.",
      "items": {
        "type": "object",
        "properties": {
          "singer_name": {
            "type": "string",
            "description": "The name of the singer."
          },
          "number_of_bands": {
            "type": "integer",
            "description": "The total number of bands the singer was a part of."
          },
          "band_names": {
            "type": "array",
            "description": "A list of names of the bands the singer was a part of.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "singer_name",
          "number_of_bands",
          "band_names"
        ],
        "additionalProperties": false
      }
    },
    "comparison_summary": {
      "type": "string",
      "description": "A summary statement comparing the number of bands for both singers."
    }
  },
  "required": [
    "singer_with_more_bands",
    "singer_comparison",
    "comparison_summary"
  ],
  "additionalProperties": false
}
