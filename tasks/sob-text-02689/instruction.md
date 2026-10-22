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
Guns and Roses (disambiguation): Guns N' Roses is an American hard rock band.  It is also the name of the band's second EP Guns N' Roses (EP), and a pinball game named after them, Guns N' Roses (pinball).

Use Your Illusion II: Use Your Illusion II is the fourth studio album by the American hard rock band Guns N' Roses.  The album was released on September 17, 1991, the same day as its counterpart album "Use Your Illusion I".  Both of the albums were released in conjunction with the Use Your Illusion Tour.  Bolstered by the lead single "You Could Be Mine," "Use Your Illusion II" was the slightly more popular of the two albums, selling 770,000 copies its first week and debuting at No. 1 on the U.S. charts, ahead of "Use Your Illusion I"'s first week sales of 685,000.  As of 2010, "Use Your Illusion II" has sold 5,587,000 units in the U.S., according to Nielsen SoundScan.  Both albums have since been certified 7× Platinum by the RIAA.  It was also No. 1 on the UK Albums Chart for a single week.  It is the last Guns N' Roses album to feature rhythm guitarist Izzy Stradlin.  It also included the last Guns N' Roses song to feature drummer Steven Adler, who played on "Civil War."

The Days of Our Nights: The Days of Our Nights is the fifth album by American alternative rock band Luna, currently out of print in the United States.  It includes a cover of the Guns N' Roses hit "Sweet Child o' Mine".

One in a Million (Guns N' Roses song): "One in a Million" is a song by American rock band Guns N' Roses.  It is the eighth track on the album "G N' R Lies" and was released in 1988.  The lyrics describe Guns N' Roses singer Axl Rose's experience of getting hustled in the Greyhound bus station upon first arriving in Los Angeles.  The song is notable not only for its controversy, but also for being one of the first Guns N' Roses songs that Axl Rose wrote solo.  According to interviews, Rose wrote "One in a Million" on guitar (with which he was not proficient at the time), using only the bottom two strings.  This differs from other Rose-written Guns N' Roses songs, which Rose composed on piano or keyboards.  This is the first Guns N' Roses song to feature piano, played by Rose on the outro.

Guns N' Roses/Metallica Stadium Tour: The Guns N' Roses/Metallica Stadium Tour was a co-headlining concert tour by American rock bands Guns N' Roses and Metallica during 1992.  It took place in the middle of Guns N' Roses' "Use Your Illusion Tour," promoting their "Use Your Illusion I" & "II" albums, and between Metallica's "Wherever We May Roam Tour" and "Nowhere Else to Roam," promoting their eponymous fifth album "Metallica (The Black Album)".  The tour's opening act was Faith No More.  Axl Rose had wanted Seattle rock band Nirvana to be the opening act, but frontman Kurt Cobain refused.

&quot;The Spaghetti Incident?&quot;: "The Spaghetti Incident?"  is the fifth studio album by the American hard rock band Guns N' Roses.  The album is composed of covers of older punk rock and hard rock songs. " "The Spaghetti Incident?""  is the only studio album to feature rhythm guitarist Gilby Clarke, who replaced original Guns N' Roses member Izzy Stradlin during the band's "Use Your Illusion" tour in 1991, as well as the last album to feature guitarist Slash, bassist Duff McKagan and drummer Matt Sorum.  It is also the only Guns N' Roses album not to be accompanied by a supporting tour.

Babylon A.D. (album): Babylon A.D. is the debut album by the American hard rock band of the same name, released in 1989.  It contains the metal hits "Bang Go The Bells", "Hammer Swings Down" and "The Kid Goes Wild" which was also featured in the film "RoboCop 2".  In the music video for "The Kid Goes Wild", Robo-Cop is featured targeting the band, much like in the video for the Guns N' Roses song "You Could Be Mine", in which the Terminator is targeting Guns N' Roses.

Slash (musician): Saul Hudson (born July 23, 1965), better known by his stage name Slash, is a British-American musician and songwriter.  He is best known as the lead guitarist of the American hard rock band Guns N' Roses, with whom he achieved worldwide success in the late 1980s and early 1990s.  During his later years with Guns N' Roses, Slash formed the side project Slash's Snakepit.  After leaving Guns N' Roses in 1996, he co-founded the supergroup Velvet Revolver, which re-established him as a mainstream performer in the mid to late 2000s.  Slash has since released three solo albums: "Slash" (2010), featuring an array of famous guest musicians, and "Apocalyptic Love" (2012) and "World on Fire" (2014), recorded with his band, Myles Kennedy and the Conspirators.  He returned to Guns N' Roses in 2016, nearly 20 years after he had left.

Steven Adler: Steven Adler (born Michael Coletti; January 22, 1965) is an American musician.  He is best known as the former drummer and co-songwriter of the hard rock band Guns N' Roses, with whom he achieved worldwide success in the late 1980s.  Adler was fired from Guns N' Roses over his heroin addiction in 1990, following which he reformed his old band Road Crew and briefly joined BulletBoys, which both proved unsuccessful.  During the 2000s, Adler was the drummer of the band Adler's Appetite, and from 2012, he had held the same position in the band Adler.  In early 2017, Steven Adler declared that he has no intention to continue with the band, and that the band has now dissolved, and the reason is his lack of interest in performing during poorly attended concerts.  He appeared on the second and fifth seasons of the reality TV show "Celebrity Rehab with Dr. Drew", as well as on the first season of its spin-off "Sober House".  He was inducted into the Rock and Roll Hall of Fame in 2012 as a member of Guns N' Roses.

Sweet Child o' Mine: "Sweet Child o' Mine" is a song by the American rock band Guns N' Roses, featured on their debut album, "Appetite for Destruction" (1987).  Released in August 1988 as the album's third single, the song topped the "Billboard" Hot 100 chart, becoming the band's first and only number-one single in the U.S..  "Billboard" ranked it as the No. 5 song for 1988.  It reached number six on the UK Singles Chart, when re-released in 1989.

Question: Which Guns N'Roses song, known for being their only number-one single in the U.S., is covered by the American alternative rock band Luna?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_name": {
      "type": "string",
      "description": "The name of the Guns N' Roses song."
    },
    "chart_performance": {
      "type": "object",
      "properties": {
        "us_number_one_single": {
          "type": "boolean",
          "description": "Indicates if the song was a number one single in the U.S."
        },
        "only_us_number_one": {
          "type": "boolean",
          "description": "Indicates if the song was the band's only number one single in the U.S."
        }
      },
      "required": [
        "us_number_one_single",
        "only_us_number_one"
      ],
      "additionalProperties": false
    },
    "covered_by": {
      "type": "object",
      "properties": {
        "band_name": {
          "type": "string",
          "description": "The name of the band that covered the song."
        },
        "band_genre": {
          "type": "string",
          "description": "The genre of the band that covered the song."
        },
        "album_name": {
          "type": "string",
          "description": "The name of the album on which the cover appeared."
        }
      },
      "required": [
        "band_name",
        "band_genre",
        "album_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_name",
    "chart_performance",
    "covered_by"
  ],
  "additionalProperties": false
}
