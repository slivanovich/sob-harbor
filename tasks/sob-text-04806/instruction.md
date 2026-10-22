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
David Allan Coe discography: This is a detailed discography for American country music artist David Allan Coe.  Coe started his career in 1970 on SSS International Records before signing with Columbia Records and staying with the label for 15 years.  In the 1990s, he released albums through several independent labels such as his own DAC Records.  Most of these releases have been reissued under different names and/or cannibalized for various compilations.  Overall, Coe's discography consists of 42 studio albums, 4 live albums, 1 collaboration album and 1 audiobook, in addition to many compilation albums.  Given the obscure nature of Coe's '90s albums and the limited information available, sources have been included for each album after his split with Columbia.

Danny Sheridan: Danny Sheridan (October 11, 1950 – May 24, 2016) was an American musician, songwriter, producer, actor, and entertainment manager.  In 2006 he also became a radio personality on 97.1 KLSX Free FM (CBS Los Angeles).  He is credited as an influential electric bass player, and as the founder of the Eli Radish Band, pioneers of the so-called outlaw country music genre.  This is a style that Sheridan's former band-mate/vocalist David Allan Coe continues to perform today, with a string of hit songs like “Would You Lay with Me (In a Field of Stone)” and the anti-labor tune, “Take This Job And Shove It”.  Still in his teens, Sheridan's Eli Radish toured with such notable acts as The Who and The Doors.  The lyrics of Coe's "Longhaired Redneck" forever memorialized the concerts he performed with Sheridan while fronting the Eli Radish Band.  In 2014 Sheridan began managing Coe and co-produced his new CD "Just As I Am", with Boris Menart.

David Allan Coe: David Allan Coe (born September 6, 1939) is an American songwriter, outlaw country music singer, and guitarist who achieved popularity in the 1970s and 1980s.  As a singer, his biggest hits were "Mona Lisa Lost Her Smile", "The Ride", "You Never Even Called Me by My Name", "She Used to Love Me a Lot", and "Longhaired Redneck".  His best-known compositions are the No. 1 successes "Would You Lay With Me (In a Field of Stone)" and "Take This Job and Shove It", the latter of which inspired the movie of the same name.

She Used to Love Me a Lot: "She Used to Love Me a Lot" is a song recorded by American country music artist David Allan Coe.  It was released in December 1984 as the lead single from Coe's album "Darlin', Darlin".  The song peaked at number 11 on both the U.S. "Billboard" Hot Country Singles chart and the Canadian "RPM" Country Tracks chart.  It was written by Dennis Morgan, Charles Quillen, and Kye Fleming.  A version of the song by Johnny Cash was recorded in the early 1980s, but remained unreleased until 2014.

Confederate Railroad: Confederate Railroad is an American country rock–Southern rock band founded in 1987 in Marietta, Georgia, by Danny Shirley (lead vocals, rhythm guitar), Michael Lamb (lead guitar), Mark Dufresne (drums), Chris McDaniel (keyboards), Warren "Gates" Nichols (steel guitar) and Wayne Secrest (bass guitar).  After serving as a backing band for outlaw country acts David Allan Coe and Johnny Paycheck, the band signed to a recording contract with Atlantic Records, releasing their self-titled debut album that year.  In the 1990s, they released four more albums for Atlantic.

Tennessee Whiskey (song): "Tennessee Whiskey" is the title of a country song written by Dean Dillon and Linda Hargrove.  It was originally recorded by American country music artist David Allan Coe for his album of the same name "Tennessee Whiskey", whose version peaked at number 77 on the "Billboard" Hot Country Singles chart in 1981.  George Jones' 1983 version of the song was included on his album "Shine On", and reached number 2 on the Hot Country Singles chart.  The song has been covered by several artists, including Chris Stapleton, whose version was performed at the 2015 Country Music Association (CMA) Awards with Justin Timberlake, and was certified platinum by the Recording Industry Association of America (RIAA).

Longhaired Redneck (song): "Longhaired Redneck" is a song co-written and recorded by American country music artist David Allan Coe.  It was released in January 1976 as the lead single from Coe's album of the same name.  The song is notable for its direct reference to the "outlaw" movement in country music during the 1970s, with which Coe was associated, as well as the chorus which features Coe impersonating classic country artists Ernest Tubb, "Whisperin'" Bill Anderson, and Merle Haggard.  The song peaked at number 17 on the U.S. "Billboard" Hot Country Singles chart and at number 23 on the Canadian "RPM" Country Tracks chart.  It was written by Coe with Jimmy Rabbitt, who is also a popular radio DJ in Texas.

You Never Even Called Me by My Name: "You Never Even Called Me by My Name" is a song written and recorded by Steve Goodman and John Prine, and recorded by country music singer David Allan Coe.  It was the third single release of Coe's career, included on his album "Once Upon a Rhyme".  The song was Coe's first Top Ten hit, reaching a peak of number eight on the "Billboard" country singles charts.  The song, over five minutes long, is known for its humorous self-description as "the perfect country and western song."

Johnny Paycheck: Johnny Paycheck (born Donald Eugene Lytle; May 31, 1938 – February 19, 2003) was an American country music singer-songwriter, multi-instrumentalist, and Grand Ole Opry member notable for recording the David Allan Coe song "Take This Job and Shove It".  He achieved his greatest success in the 1970s as a force in country music's "Outlaw Movement" popularized by artists Coe, Waylon Jennings, Willie Nelson, Billy Joe Shaver, and Merle Haggard.  In the 1980s, his music career slowed due to drug, alcohol and legal problems.  He served a prison sentence in the early 1990s and his declining health effectively ended his career in early 2000.  In 1980, Paycheck appeared on the PBS music program "Austin City Limits" (season 5).

Longhaired Redneck: Longhaired Redneck is an album released by country musician David Allan Coe.  It was released in 1976 on Columbia.

Question: "Longhaired Redneck" is a song co-written and recorded by American country music artist David Allan Coe, an American songwriter, outlaw country music singer, and guitarist who achieved popularity in the 1970s and 1980s, born on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist."
        },
        "birth_date": {
          "type": "string",
          "description": "The birth date of the artist in YYYY-MM-DD format."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles or professions of the artist."
        },
        "popularity_period": {
          "type": "string",
          "description": "The period during which the artist achieved popularity."
        }
      },
      "required": [
        "name",
        "birth_date",
        "roles",
        "popularity_period"
      ],
      "additionalProperties": false
    },
    "song_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the song mentioned in the context."
        },
        "artist_contribution": {
          "type": "string",
          "description": "How the artist contributed to the song (e.g., 'co-written and recorded by')."
        }
      },
      "required": [
        "title",
        "artist_contribution"
      ],
      "additionalProperties": false
    },
    "question_focus": {
      "type": "string",
      "description": "The specific piece of information the question is asking for."
    }
  },
  "required": [
    "artist",
    "song_details",
    "question_focus"
  ],
  "additionalProperties": false
}
