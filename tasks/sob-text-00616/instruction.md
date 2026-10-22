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
The Happening (song): "The Happening" is a 1967 song recorded by Motown artists The Supremes.  The song served as the theme song of the 1967 Columbia Pictures film "The Happening", and was released as a single by Motown at the time of the film's release that spring.  While the movie flopped, the song peaked at number-one on the "Billboard" Hot 100 pop singles chart in May, becoming The Supremes' tenth number-one single in the United States, peaking in the top 10 on the UK Pop Chart at number six, and in the top 5 in the Australian Pop Chart and in the Dutch Pop Chart.

Come Spy with Me (The Miracles song): "Come Spy With Me" (T54145) was a 1967 song recorded by Motown Records R&B group The Miracles, recorded on its Tamla Records subsidiary label.  The B-side of the group's Top 20 hit single "The Love I Saw in You Was Just a Mirage", It was written by Miracles lead singer Smokey Robinson, and was the original titular theme song from the 1967 20th Century Fox feature film of the same name, starring Troy Donahue and Andrea Dromm.

The First Cut Is the Deepest: "The First Cut Is the Deepest" is a 1967 song written by Cat Stevens, originally released by P. P. Arnold in May 1967.  Stevens' own version originally appeared on his album "New Masters" in December 1967.

Happy Together (song): "Happy Together" is a 1967 song from the Turtles' album of the same name.  Released as a single in February 1967, the song knocked The Beatles' "Penny Lane" out of the number one slot for three weeks on the "Billboard" Hot 100.  It was the group's only chart-topper in the United States.  "Happy Together" reached number 12 on the UK Singles Chart in April 1967 and number 13 on Top 100 Singles of 1967 in Canada The song was written by Garry Bonner and Alan Gordon, former members of a band known as The Magicians.  The song had been rejected a dozen times before it was offered to the Turtles, and the demo acetate was worn out."

Stop! And Think It Over: "Stop!  And Think it Over" is a 1967 song written by Sid Tepper and Roy C. Bennett and performed by Perry Como.  Released as a single, it was the first of three number ones for Como on the Easy Listening chart, spending a single week at the top in June 1967.  On the "Billboard" Hot 100, it reached number ninety-two.

Ode to Billie Joe: "Ode to Billie Joe" is a 1967 song written and recorded by Bobbie Gentry, a singer-songwriter from Chickasaw County, Mississippi.  The single, released in late July, was a number-one hit in the United States, and became a big international seller.  "Billboard" ranked the record as the No. 3 song for 1967 (the other two were #2 "The Letter" by the Box Tops and #1 "To Sir With Love" by Lulu).  The song is ranked #412 on "Rolling Stone"<nowiki>'</nowiki>s list of "the 500 Greatest Songs of All Time".  The recording of "Ode to Billie Joe" generated eight Grammy nominations, resulting in three wins for Gentry and one win for arranger Jimmie Haskell.

If This World Were Mine: "If This World Were Mine" is a 1967 song by soul music duo Marvin Gaye and Tammi Terrell from their album "United".  Written solely by Gaye, it was one of the few songs they recorded without Ashford & Simpson writing or producing.  When it was released as a single in November 1967 as the B-side to the duo's "If I Could Build My Whole World Around You", it hit the "Billboard" pop singles chart, peaking at number sixty-eight, and peaked at number twenty-seven on the "Billboard" R&B singles chart.  Gaye would later put the song into his set list during his last tours in the early-1980s as he performed a medley of his hits with Terrell.  The song was covered a year later by Joe Bataan on the 1968 Fania Allstars LP "Live at the Red Garter, Vol.  2", and in 1969 by Ambrose Slade (pre-Slade) on their album "Beginnings".

I Think We're Alone Now (disambiguation): "I Think We're Alone Now" is a 1967 song originally recorded by Tommy James and the Shondells and covered by Tiffany.

Western Union (Five Americans song): "Western Union" is a 1967 song by the American rock band the Five Americans.  The single peaked at number 5 on the "Billboard" Hot 100 in April 1967, where it remained for one week.  It also reached number 7 on the "Cash Box" Top 100 Singles chart in the same month, where it remained for two weeks. <ref name="Cash Box Top 100 4/22/67">Cash Box Top 100 Singles, April 22, 1967</ref>

Perry Como: Pierino Ronald "Perry" Como (May 18, 1912 – May 12, 2001) was an American singer and television personality.  During a career spanning more than half a century, he recorded exclusively for RCA Victor for 44 years after signing with the label in 1943.  "Mr. C.", as he was nicknamed, sold millions of records for RCA and pioneered a musical variety television show.  Como was seen weekly on television from 1948 to 1963, then continued hosting the "Kraft Music Hall" variety program monthly until 1967.  His television shows and seasonal specials were broadcast throughout the world.  Also a popular recording artist, Perry Como released numerous hit records from the 1940s through the 1970s.  Como's appeal spanned generations and he was universally respected for both his professional standards and the conduct in his personal life.

Question: Who sang the 1967 song "Stop and Think it Over"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the song was released."
    },
    "artist_info": {
      "type": "object",
      "properties": {
        "artist_name": {
          "type": "string",
          "description": "The name of the artist who performed the song."
        },
        "artist_type": {
          "type": "string",
          "description": "The type of artist (e.g., singer, group)."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the artist."
        }
      },
      "required": [
        "artist_name",
        "artist_type",
        "nationality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "release_year",
    "artist_info"
  ],
  "additionalProperties": false
}
