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
(God Must Have Spent) A Little More Time on You: "(God Must Have Spent) A Little More Time on You" is the a song by American boy band NSYNC.  It was released as the third single from their self-titled debut album in the U.S.  While some of the previous singles were released in Europe, this one was not, and subsequently only charted in Australia and the U.S., reaching number 46 and number 8 respectively.  The single included a live version of Christopher Cross song "Sailing", as well as a limited edition postcard.  Some versions of the single included the track's video.  The radio version of this song was featured on both their first and third compilation albums: "Greatest Hits" (2005) and "The Essential *NSYNC" (2014).

Greatest Hits (NSYNC album): Greatest Hits is the first compilation album by American boy band NSYNC.  Released on October 25, 2005, the album debuted at #47 on the "Billboard" 200 albums chart.  It didn't chart in the UK on release, but debuted at #96 on the UK Albums Chart dated September 7, 2013 in the wake of NSYNC's brief reunion performance at the 2013 MTV Video Music Awards.  It features hits like "Bye Bye Bye", "It's Gonna Be Me", "I Want You Back", "Tearin' Up My Heart" and "Pop".  This album also marks the third and final overall release under Jive Records.  To date, the album has sold less than half a million copies worldwide and sold 325,000 copies in the US according to Nielsen SoundScan.

Bye Bye Baby (Madonna song): "Bye Bye Baby" is a song recorded by American singer and songwriter Madonna, for her fifth studio album "Erotica" (1992).  It was released on November 15, 1993, as the sixth and final single from the album.  "Bye Bye Baby" was written by Madonna, Shep Pettibone, and Anthony Shimkin and was produced by Madonna and Pettibone.  The song is inspired by Madonna's emotions of that time and her S&M thoughts.  Musically, it is a hip hop song, sampling a hook from LL Cool J's track "Jingling Baby", released in 1990.  Madonna's vocals were filtered to make them appear as sound coming out from an antique radio.  "Bye Bye Baby" features instrumentation from keyboard and lyrically finds Madonna asking questions to a lover she is about to abandon.

Bye Bye Boy: "Bye Bye Boy" was a single released in 2004, by Jennifer Ellison.  It is her second, and so far, final single.  It is a cover of Japanese rock/pop song "Bye Bye."  by Nanase Aikawa.  It reached number 13 on the UK charts.

Bye Bye Bye: "Bye Bye Bye" is a song by American boy band NSYNC.  It was released on January 11, 2000 as the first single from their second studio album "No Strings Attached".  The song was written and produced by Kristian Lundin and Jake Schulze, with additional writing by Andreas Carlsson.  Its lyrics describe the end of a romantic relationship; it was reported to also reference the group's separation from their manager Lou Pearlman and their record label RCA Records.  This song was also featured on the 2001 American compilation album "Now That's What I Call Music!  6".

NSYNC discography: American boy band NSYNC has released three studio albums and 18 singles.  The band first charted in 1996 and released its self-titled debut album in 1998.  Although their 2000 single "It's Gonna Be Me" reached number one on the "Billboard" Hot 100 and internationally, they are perhaps better known for their single released in the same year, "Bye Bye Bye".

NSYNC: NSYNC (sometimes stylized as *NSYNC or 'N Sync) was an American boy band formed in Orlando, Florida in 1995 and launched in Germany by BMG Ariola Munich.  NSYNC consisted of Justin Timberlake, JC Chasez, Chris Kirkpatrick, Joey Fatone, and Lance Bass.  After heavily publicized legal battles with their former manager Lou Pearlman and former record label Bertelsmann Music Group, the group's second album, "No Strings Attached", sold over one million copies in one day and 2.42 million copies in one week, which was a record for over fifteen years.  Among the group's singles, "Bye Bye Bye", "This I Promise You", "Girlfriend" and "It's Gonna Be Me" reached the top 10 in several national charts, with the latter being a US "Billboard" Hot 100 number one.  In addition to a host of Grammy Award nominations, NSYNC has performed at the World Series, the Super Bowl and the Olympic Games, and sang or recorded with Elton John, Stevie Wonder, Michael Jackson, Phil Collins, Celine Dion, Aerosmith, Nelly, Left Eye, Mary J. Blige, country music supergroup Alabama, and Gloria Estefan.

It's Gonna Be Me: "It's Gonna Be Me" is a song by American boy band NSYNC.  It was released on June 13, 2000 as the second single in the United States and third in Europe from their second studio album "No Strings Attached".  The song was NSYNC's only "Billboard" Hot 100 number-one hit, making it their highest-charting single.  It topped the chart for two consecutive weeks and has been certified Gold by the RIAA.  The song serves as the opening track of the 2000 compilation album "Now That's What I Call Music!  5".

Monday Kiz: Monday Kiz (Korean: 먼데이 키즈) is a South Korean male band formed in 2005.  Their members consist of Lee Jin-sung, Han Seung-hee and Im Han-byeol.  Monday Kiz is currently signed to Rainbow Bridge World.  Monday Kiz released their first album, "Bye Bye Bye" on October 6, 2005.

Fred Hamm: Fred Hamm was a Chicago jazz orchestra leader and co-author of the song "Bye Bye Blues."  In 1925 he took over the leadership of the Benson Orchestra (founded by Edgar Benson).  He sang and played the cornet.  Among the members of his band were Dave Bennett (who played clarinet and alto saxophone), Chauncey Gray (piano), and Bert Lown (violin).  With Bennett, Gray, and Lown, he co-wrote "Bye Bye Blues" in early 1925.

Question: "Bye Bye Bye" is a song by American boy band NSYNC, formed in Orlando, Florida in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song mentioned in the question."
    },
    "artist_name": {
      "type": "string",
      "description": "The name of the band that performs the song."
    },
    "band_details": {
      "type": "object",
      "properties": {
        "formation_year": {
          "type": "integer",
          "description": "The year the band was formed."
        },
        "origin_city": {
          "type": "string",
          "description": "The city where the band was formed."
        },
        "origin_country": {
          "type": "string",
          "description": "The country where the band was formed."
        }
      },
      "required": [
        "formation_year",
        "origin_city",
        "origin_country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "artist_name",
    "band_details"
  ],
  "additionalProperties": false
}
