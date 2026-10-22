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
Soldier of Love (Sade song): "Soldier of Love" is the first single and title track from the album Soldier of Love by the English band Sade.  It premiered worldwide on 8 December 2009, and it was released on iTunes digitally on 12 January 2010.  It was also the band's first new material in almost ten years, preceding their long-awaited sixth studio album of the same name which was released worldwide on 8 February 2010.  The song was number-one on the "Billboard" Adult R&B.  The song debuted at #58 on the "Billboard" Hot 100 becoming the band's highest debut on the chart.  It has peaked at number 52, making it the band's highest-peaking single on that chart since 1992's "No Ordinary Love".

Jaya (1989 album): Jaya was the first album by Filipino-Jamaican singer actress and tv host Jaya.  The album was produced by Stevie B and Don Glenn Gutierrez under LMR Records.  She was offered an opportunity to finish an album that had already been started by another artist.  In February 1989, she signed a record deal with LMR Records (New York).  Later that year, her first self-titled debut album was released in the U.S.  The first single, "If You Leave Me Now", was a hit in the dance clubs and was subsequently released to Top 40 radio.  The single entered the "Billboard" Hot 100 chart in October 1989.  It eventually peaked at number 44 in February 1990 and remained in the Top 100 pop singles chart for 26 weeks, an unusually long chart run for a single that peaked outside the Top 40.  According to playlists submitted to "Billboard" magazine by American radio stations at the time, the song was a top 20 hit on dance-pop stations in various large markets, such as New York City, Los Angeles, Chicago and San Francisco.  The song features a strong vocal performance by Jaya as well as many elements associated with freestyle music, which in the late 1980s was beginning to reach a wider audience in the U.S. "If You Leave Me Now" also gave Jaya the opportunity to work across the US with top artists like Stevie B, MC Hammer, Milli Vanilli, James Ingram, The Jets, and many more.

Let It Be (song): "Let It Be" is a song by the English rock band the Beatles, released in March 1970 as a single, and (in an alternate mix) as the title track of their album "Let It Be".  At the time, it had the highest debut on the "Billboard" Hot 100, beginning its chart run at number 6.  It was written and sung by Paul McCartney.  It was their final single before McCartney announced his departure from the band.  Both the "Let It Be" album and the US single "The Long and Winding Road" were released after McCartney's announced departure from and the subsequent break-up of the group.

Instant Karma!: "Instant Karma!"  – sometimes referred to as "Instant Karma!  (We All Shine On)" – is a song written by English musician John Lennon, released as a single on Apple Records in February 1970.  In the UK, the single was credited to "Lennon/Ono with the Plastic Ono Band".  The song reached the top five in the British and American singles charts, competing with the Beatles' "Let It Be" in America, where it became the first solo single by a member of the band to sell a million copies.

I Don't Want to Wait: "I Don't Want to Wait" is a song written, performed and produced by Paula Cole.  It was Cole's second single from her album "This Fire" and later served as the opening theme for the TV series "Dawson's Creek".  Cole originally wrote the song and recorded a demo of the song in April 1991 but did not officially record and release it until 1996.  The single ranked #10 on the 1998 "Billboard" Hot 100 singles chart year-end summary.  The single spent the most consecutive weeks in the top 50 without cracking the top 10, just missing out at #11.  The single, with a 56-week-long run, is among the list of the 32 songs in the history of the "Billboard" Hot 100 to have had a chart run longer than 50 weeks.

(Marie's the Name) His Latest Flame: "(Marie's the Name) His Latest Flame" is a song recorded in a hit version by Elvis Presley and published by Elvis Presley Music in 1961.  It was written by Doc Pomus and Mort Shuman and originally recorded by Del Shannon on the album "Runaway With Del Shannon", which was released in June 1961.  The more famous and successful recording by Presley was released in August 1961.  The relatively intense tune, featuring a Bo Diddley beat, performed well on both pop and easy listening stations, reaching No. 4 on the "Billboard" Hot 100, and No. 2 on the Easy Listening chart, based (at the time) on the Top 100.  However, the single's Hot 100 chart run was atypical of a Top Ten hit.  In the autumn of 1961 it shot from 22 to 4, then dropped to 10, then 26, all within the space of four weeks.  The single (a double A-side with "Little Sister", as in the States) spent four weeks at No. 1 in the UK Singles Chart — one of Presley's nine UK chart-toppers between 1960 and 1962.

Karma (Alicia Keys song): "Karma" is a song by American singer and songwriter Alicia Keys, taken from her second studio album, "The Diary of Alicia Keys" (2003).  Written by Keys, Kerry Brothers, Jr., and Taneisha Smith, the track takes influence from hip hop and classical music, and was released as the album's fourth and final single in November 2004, peaking at number twenty on the U.S. "Billboard" Hot 100 and number seventeen on the U.S. "Billboard" Hot R&B/Hip-Hop Songs chart—the album's only single not to top a "Billboard" chart.  A mashup of "Karma" with Stevie Wonder's 1972 hit "Superstition" titled "Karmastition", produced by Go Home Productions, exists.

Here Come Those Tears Again: "Here Come Those Tears Again" is a song written and performed by American singer-songwriter Jackson Browne and included on his 1976 album "The Pretender".  Released as a single, it reached #23 one year to the week after the death of Browne's wife, Phyllis Major, spending nine weeks on the chart, after entering the Billboard Hot 100 on February 5, 1977 at position #64, the highest debut of the week.  It also reached #15 on the Billboard Adult Contemporary chart.  The single was the eighth-highest charting of his Hot 100 career.  It was also released as a single in the United Kingdom, Germany and Japan.

Midnight Madness (album): Midnight Madness is the second studio album from rock band Night Ranger released in 1983.  Their second album produced three charting singles and contains the band's best known hit, "Sister Christian."  It remains their highest selling album at over a million copies sold in the US.  The first single/video, "(You Can Still) Rock in America" peaked at #51 in early 1984 on Billboard's Hot 100 chart and also reached #15 on Billboard's Mainstream Rock Tracks chart.  "Sister Christian" peaked at #5 on Billboard's Hot 100 and was one of the most played videos of 1984.  The song also has been featured in several films including "Boogie Nights" and "Rock of Ages" among others.  "When You Close Your Eyes" was the third single/video and reached #14 on Billboard's Hot 100 chart and #7 on Billboard's Mainstream Rock Tracks Chart.  The 1984 CD release contains a slightly different recording of the track.  "Rumours In The Air" also charted on the Billboard Mainstream Rock chart peaking at #26 in the spring of 1984.

Let U Go (Ashley Parker Angel song): "Let U Go" is the first single from Ashley Parker Angel's debut solo album "Soundtrack to Your Life".  In the U.S., the song debuted at #17 on the "Billboard" Hot 100 singles chart, the third highest debut of the year.  The song moved up to its peak of #12 in its second week, while reaching the top 10 of the Pop 100 companion chart at #9.  The song was written about Angel's relationship with his now-ex-fiancee Tiffany Lynn.  Angel has said that the relationship has, at times, been rough, but that he and Tiffany are meant to be together.  Dr. Luke and Max Martin produced the song.

Question: In America "Instant Karma!" competed with a song that had the highest debut on the "Billboard" Hot 100, beginning its chart run at what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "competing_song_title": {
      "type": "string",
      "description": "The title of the song that competed with 'Instant Karma!'."
    },
    "chart_name": {
      "type": "string",
      "description": "The name of the Billboard chart."
    },
    "debut_position": {
      "type": "integer",
      "description": "The position at which the song debuted on the chart."
    },
    "was_highest_debut_at_time": {
      "type": "boolean",
      "description": "Indicates if the song had the highest debut on the chart at that time."
    }
  },
  "required": [
    "competing_song_title",
    "chart_name",
    "debut_position",
    "was_highest_debut_at_time"
  ],
  "additionalProperties": false
}
