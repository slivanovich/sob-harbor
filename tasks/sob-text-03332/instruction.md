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
Sedated (song): "Sedated" is a song written and performed by Irish musician Hozier.  It was released on 20 May 2014 as the third single from his debut studio album "Hozier" (2014) and peaked at number three on the Irish Singles Chart.

The Wanted discography: British-Irish boy band The Wanted have released three studio albums, two extended plays and ten singles.  The band's debut album, "The Wanted", was released by Geffen Records in the United Kingdom in October 2010.  It reached number four on the UK Album Chart and number eleven on the Irish Albums Chart.  The album's first single, "All Time Low", was released in July 2010 and peaked at number one on the UK Singles Chart and number thirteen on the Irish Singles Chart.  This was followed by "Heart Vacancy", which reached two in the UK and eighteen in Ireland. " Lose My Mind", was the third and last single from the album and was less successful than its predecessors, reaching number 19 in the UK and number 30 in Ireland.

Gold Dust (DJ Fresh song): "Gold Dust" is a song by British-based DJ and record producer DJ Fresh.  Originally put out as a 12" in 2008, it was re-released in 2010 featuring vocals from Ce' Cile although there is a version of the song on his album "Nextlevelism" which features Ms. Dynamite.  It is the third single released from his second album "Kryptonite".  The 2010 version of the song peaked at number 24 on the UK Singles Chart.  The music video was directed by Ben Newman and edited by Jacek Zajkowski.  In 2012, Shy FX made a 're-edit' of the song that was re-released to radio.  This version reached number 22 on the UK Singles Chart and number 39 on the Irish Singles Chart.  The sales of all versions are combined together enabling it to have sold in excess of 600,000 copies, receiving a Platinum certification, despite never reaching the top twenty of the UK Singles Chart.

Someone New (Hozier song): "Someone New" is a song written and performed by Irish musician Hozier.  It was released on May 11, 2015 as the fifth single from his debut studio album "Hozier" (2014) and peaked at number 13 on the Irish Singles Chart.

Kodaline discography: The discography of Kodaline, a Dublin-based Irish alternative rock quartet, consists of two studio albums, three extended plays, ten singles and seven music videos. Originally known as 21 Demands, the band made chart history in March 2007, when their debut single "Give Me a Minute" topped the Irish Singles Chart, becoming the first independently released track to achieve the feat.  In June 2013 Kodaline released their debut studio album "In a Perfect World", peaking to number 1 on the Irish Albums Chart. " High Hopes" was released as the lead single from the album in March 2013, peaking at number 1 on the Irish Singles Chart. " Love Like This" was released as the second single from the album in May 2013, peaking at number 8 on the Irish Singles Chart.  Their second album "Coming Up for Air" reached the number 1 on the Irish Albums Chart.

The Steady Song: "The Steady Song" is a 2008 single by the Irish musical ensemble Republic of Loose featuring Isabel Reyes-Feeney.  It features on the album "".  When released as a single on 20 June.  it spent a total of thirteen weeks in the Irish Singles Chart, climbing as far as number 12 (the band's highest placed entry in the Irish Singles Chart thus far) and receiving steady airplay throughout the summer.  amongst the songs live performances have been an appearance on "The View" and also at Oxegen 2008.

Barbados (Typically Tropical song): "Barbados" was a UK Number 1 single released in May 1975 by Typically Tropical.  "Barbados" entered the UK Singles Chart at number 37 in late June 1975, and five weeks later was at Number 1 for a week.  In total, "Barbados" spent eleven weeks on the chart.  The track also reached Number 1 on the Irish Singles Chart, Number 1 on the South African Singles Chart, and 20 on the Australian Singles Chart (Kent Music Report).  The track was later released on an album in 1975 by Gull Records.  The album was named "Barbados Sky".

Hozier (musician): Andrew Hozier-Byrne (born 17 March 1990), known professionally by the mononym Hozier, is an Irish musician, singer and songwriter from County Wicklow.  He released his debut EP, featuring the hit single "Take Me to Church", in 2013 and his second EP, "From Eden", in 2014.  His debut studio album, "Hozier", was released in Ireland in September 2014 and globally in October 2014.

From Eden: "From Eden" is a song written and performed by Irish musician Hozier.  It was released as the second single from his debut studio album "Hozier" (2014).  "From Eden" peaked at number two on the Irish Singles Chart and has also charted in Belgium.  A "From Eden" EP was released digitally on 9 March 2014.

Country Grammar: Country Grammar is the debut studio album by American rapper Nelly.  It was released on June 27, 2000, by Universal Records (who released the album after listening to demos by Nelly, before signing a record deal with the rapper in 1999).  The production on the album was handled by Jason "Jay E" Epperson, with additional production by C-Love, Kevin Law, City Spud, Steve "Blast" Wills and Basement Beats.  Nelly contributed to all lyrics on the album, with Epperson and City Spud also contributing.  The album introduced a unique Saint Louis, Midwestern sound, and introduces Nelly's vocal style of pop-rap singalongs and Midwestern, Missouri twang.  It was supported four successful singles: "Country Grammar (Hot Shit)", "E.I.", "Ride wit Me" and "Batter Up".  Its lead single, "Country Grammar (Hot Shit)", peaked at number 7 on the "Billboard" Hot 100 and UK Singles Chart.  "E.I." charted at number 16, number 12 and number 11 on the Hot 100, UK Singles Chart and ARIA Singles Chart, respectively.  "Ride wit Me" peaked within the top five on the Hot 100, ARIA Singles Chart, Irish Singles Chart and UK Singles Chart.  The album's fourth and final single, "Batter Up" featuring Murphy Lee and Ali, achieved moderate chart success.

Question: When was the Hozier album containing a song that reached #2 on the Irish Singles Chart released globally?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_name": {
      "type": "string",
      "description": "The name of the artist."
    },
    "album_title": {
      "type": "string",
      "description": "The title of the album."
    },
    "song_details": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song from the album that reached number 2 on the Irish Singles Chart."
        },
        "irish_singles_chart_peak_position": {
          "type": "integer",
          "description": "The peak position of the song on the Irish Singles Chart."
        }
      },
      "required": [
        "song_title",
        "irish_singles_chart_peak_position"
      ],
      "additionalProperties": false
    },
    "album_global_release_date": {
      "type": "string",
      "description": "The global release date of the album."
    }
  },
  "required": [
    "artist_name",
    "album_title",
    "song_details",
    "album_global_release_date"
  ],
  "additionalProperties": false
}
