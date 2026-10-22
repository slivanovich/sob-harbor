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
Hell Freezes Over: Hell Freezes Over is the second live album by the Eagles, released in 1994.  The album is the first to be released after Eagles had re-formed following a fourteen-year-long break up.  The band's lineup was that of the "Long Run" era: Glenn Frey, Don Henley, Don Felder, Joe Walsh, and Timothy B. Schmit.  It contains four new studio tracks and eleven tracks recorded live in April 1994 for an MTV special.  Two Top 40 Mainstream singles, "Get Over It" and "Love Will Keep Us Alive", were released from the album.  It also features an acoustic version of "Hotel California".  The four new studio recordings are the last to feature Don Felder, who was dismissed from the band in 2001.

Playin' It Cool: Playin' It Cool is the debut studio solo album by Timothy B. Schmit, the bass guitarist and co-lead vocalist for the Eagles.  The album was released in 1984 on Asylum in the United States and Europe.  The album features guest appearances from Don Henley, Joe Walsh, Steve Lukather, Carl Wilson, J.D. Souther and Rita Coolidge.

The Long Run (album): The Long Run is the sixth studio album by American rock group the Eagles.  It was released in 1979, on Asylum in the United States and in the United Kingdom.  This was the first Eagles album to feature Timothy B. Schmit, who had replaced founding member Randy Meisner.  This was the band's final studio album for Asylum Records.

Indian Summer (Poco album): Indian Summer is the twelfth album by the American country rock band Poco, released in 1977.  This was the band's last studio album before both Timothy B. Schmit and George Grantham left the group.

Timothy B.: Timothy B is the second studio solo album by Timothy B. Schmit, the bass guitarist and co-lead vocalist for the Eagles.  The album was released in 1987 on MCA in the United States and Europe, three years after Schmit's debut solo album, "Playin' It Cool" and seven years after the demise of the Eagles.  The album peaked at #106 on the "Billboard" 200 chart, and the single, "Boys Night Out", peaked at #25 on the "Billboard" Hot 100 chart, this song is Schmit's best selling single.  The album was produced by Richard Rudolph, and it was co-produced by Bruce Gaitsch.

Eagles (band): The Eagles are an American rock band formed in Los Angeles in 1971.  The founding members were Glenn Frey (lead guitar, lead vocals), Don Henley (drums, lead vocals), Bernie Leadon (guitars, vocals) and Randy Meisner (bass guitar, vocals).  With five number-one singles, six Grammy Awards, five American Music Awards, and six number one albums, the Eagles were one of the most successful musical acts of the 1970s.  At the end of the 20th century, two of their albums, "Their Greatest Hits (1971–1975)" and "Hotel California", were ranked among the 20 best-selling albums in the United States according to the Recording Industry Association of America.  "Hotel California" is ranked 37th in "Rolling Stone"' s list of "The 500 Greatest Albums of All Time" and the band was ranked number 75 on the magazine's 2004 list of the 100 Greatest Artists of All Time.

I Can't Tell You Why: "I Can't Tell You Why" is a song by the American rock band Eagles which appeared on their 1979 album "The Long Run".  The song was written by band members Timothy B. Schmit, Glenn Frey, and Don Henley.  Recorded in March 1978, it was the first song finished for the album and the first Eagles song to feature Schmit on lead vocals.  The studio version became a "Billboard" Top 10 hit in April 1980, reaching number 8 on the "Billboard" Hot 100 and number 3 on the Adult Contemporary chart.  It is their last Top Ten hit on the Hot 100.  The original key of the song is D major.

Soul Searchin' (Glenn Frey album): Soul Searchin' is the third solo studio album by Glenn Frey, the guitarist and co-lead vocalist for the Eagles.  The album was released in mid 1988 on MCA in the United States and the United Kingdom, four years after Frey's successful album, "The Allnighter" and eight years after the demise of the Eagles.  The album features eight original songs co-written by Frey with Jack Tempchin and the song "Two Hearts" contributed by Frey's friend, Hawk Wolinski.  The album also features contributions from fellow Eagles member Timothy B. Schmit, Max Carl, Robbie Buchanan, Michael Landau, and Bruce Gaitsch.

Airborne (Don Felder album): Airborne is the first solo album by former Eagles guitarist Don Felder recorded during the period that the band was broken up.  It was his only solo album until 2012's "Road to Forever".  It featured Carlos Vega, Joe Vitale, Russ Kunkel, Tris Imboden, Timothy B. Schmit, Jeff Lorber, Paulinho Da Costa, Joe Lala, Kenny Loggins, Dave Mason and Albhy Galuten.

Beat Street (album): Beat Street is the seventh studio album by the Canadian pop rock band Prism.  It was originally released in 1983 on the record label, Capitol, two years after Prism's successful album, "Small Change".  It was the last of two Prism studio albums featuring the lead vocalist Henry Small, who had replaced Ron Tabak after his forced departure in 1981.  It features high-profile guest backing vocalists, including the Eagles' co-lead singer Timothy B. Schmit, Toto's lead singer Bobby Kimball and Chicago's lead singer Bill Champlin.  The album is notably the band's first album not to feature their guitarist and founding member Lindsay Mitchell.  The album was their last recording of original material until they officially reformed in 1987–88.  In that incarnation of the band, Small was replaced by Darcy Deutsch.

Question:  Timothy B is the second studio solo album by Timothy B. Schmit, the bass guitarist and co-lead vocalist for the Eagles, an American rock band formed where in 1971

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band."
        },
        "formation_year": {
          "type": "integer",
          "description": "The year the band was formed."
        },
        "formation_location": {
          "type": "string",
          "description": "The city where the band was formed."
        }
      },
      "required": [
        "name",
        "formation_year",
        "formation_location"
      ],
      "additionalProperties": false
    },
    "member_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the band member."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Roles of the member within the band."
        }
      },
      "required": [
        "name",
        "roles"
      ],
      "additionalProperties": false
    },
    "album_context": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the album mentioned in the context."
        },
        "artist": {
          "type": "string",
          "description": "The artist of the album."
        },
        "type": {
          "type": "string",
          "description": "The type of album (e.g., studio solo album)."
        }
      },
      "required": [
        "title",
        "artist",
        "type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "band",
    "member_details",
    "album_context"
  ],
  "additionalProperties": false
}
