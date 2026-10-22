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
I Am (Becoming The Archetype album): I Am is the fifth studio album by the heavy metal band Becoming the Archetype.  The album was recorded between May 21 and June 17 and was released on September 18, 2012 through Solid State Records.  This album is a departure from the previous effort, as Seth Hecox says, "gone are the sitars and horns of Celestial Completion.  Instead, we've crafted an album full of the heaviest and most technical songs we've ever written.”  It is the first release by the band to feature Chris McCane on vocals, Codey Watkins on bass, and Chris Heaton on drums.  Guitarist/vocalist Seth Hecox is the only original member from the debut album featured on I Am.  The first single to promote the album was the song "The Time Bender", released on August 28, 2012, as well a lyric video and an official video.

Concrete and Gold: Concrete and Gold is the ninth studio album by American rock band Foo Fighters.  It was released on September 15, 2017.  The album's first single, "Run", was released on June 1, 2017, and topped the US "Billboard" Mainstream Rock Songs chart the following month.  The second single, "The Sky Is a Neighborhood", was released on August 23, 2017.  A third song, "The Line", was released a week prior to the album's release.  The album received positive reviews, and topped the US all-format "Billboard" 200 chart in its debut week of release, selling 120,000 copies.

True Colours (Split Enz album): True Colours, the fifth album released by New Zealand band Split Enz, was their first major commercial success.  Released in 1980, the album featured more mature songwriting from Neil Finn.  Credited to him is the album's New Zealand and Australian #1 single, "I Got You," which also broke them internationally.  The US release of the album featured "Shark Attack" and "I Got You" in reversed positions due to the latter's success on the single charts.

The Seer (Big Country album): The Seer is the third studio album by the Scottish band Big Country, released in 1986.  The album featured very traditional Scottish musical settings, reminiscent of the band's debut album "The Crossing" (1983).  Kate Bush worked on the title song in a duet with lead singer and lyricist Stuart Adamson.  The album's first single, "Look Away", was an Irish number one, and was also the group's biggest hit single in the UK, reaching #7.

Twenty (Boyz II Men album): Twenty is the tenth studio album by American R&B group Boyz II Men.  The album was released in the United States on October 25, 2011.  The first single was "More Than You'll Ever Know" featuring Charlie Wilson.  As of September 2011, the single was the most added song to radio sets on urban adult contemporary radio stations.  The album featured 13 new material songs and nine rerecorded Boyz II Men classics.  It was produced Tim & Bob, Babyface, Jimmy Jam and Terry Lewis, and Teddy Riley.  The album debuted at number 20 on the "Billboard" 200, selling 18,400 copies in its first week.

Biyahe ng Pangarap: Biyahe ng Pangarap (lit.  Journey of Dreams) is the first live album and DVD of Filipino rapper Gloc-9, originally released on November 9, 2014.  The album featured songs from his previous albums (6 tracks), Liham at Lihim (5 tracks) and Talumpati (1 track).  Also, the album has one bonus track (studio recorded) entitled "Businessman" with former Parokya Ni Edgar vocalist Vinci Montaner arranged by Jazz Nicholas of Itchyworms which also serves as the album's first single.

MTV Unplugged (Juanes album): Juanes: MTV Unplugged is the third live album of Colombian singer Juanes.  It was recorded before a live audience at the New World Symphony Center in Miami Beach, Florida, on February 1, 2012 and was released by Universal Music Latino on May 29, 2012.  The album includes featured performances by the Spanish composer Joaquín Sabina and the Brazilian singer Paula Fernandes.  The album features rearranged takes on Juanes' hit songs like "Me Enamora", La Camisa Negra and "A Dios le Pido".  The first single of the live album was released on March 5, 2012 called La Señal, which became a hit in Latin America.  The second single was "Me Enamora", with new instrumental arrangements, and was released two days after of the album's release.  The album featured three new songs, one of which was a collaboration with Joaquín Sabina.  The album debuted at number one on the Billboard Top Latin Albums Chart and won the 2012 Latin Grammy for Album of the Year.  This was the third time he won Album of the Year at the Latin Grammys.

Covert Coup: Covert Coup is the collaboration studio album by rapper Curren$y and producer The Alchemist.  The album featured guest appearances from rappers Prodigy of Mobb Deep, Freddie Gibbs, Smoke DZA and Fiend and contains 10 songs.  "Covert Coup" was created as a retail EP.  Later, the artists decided to release it as a free digital album.  It was still treated as a mixtape, however, since it was given away for free.  On April 7, 2011, the first single from "Covert Coup" titled "Ventilation" was leaked onto the internet.  "Full Metal" was leaked on April 12.  On April 15, the third single entitled "Scottie Pippen" featuring Freddie Gibbs, was leaked.  The album was released by Curren$y on April 20, 2011 via his Twitter.

Run (Foo Fighters song): "Run" is a song by American rock band Foo Fighters.  It was released as a single on June 1, 2017, and is off their ninth studio album, "Concrete and Gold".  The song topped the US "Billboard" Mainstream Rock Songs chart in July 2017.

The Pretender (song): "The Pretender" is a song by the American alternative rock band Foo Fighters.  It was the first single from the group's 2007 album "Echoes, Silence, Patience & Grace".  It is one of Foo Fighters' most successful songs; peaking at number 37 on the US "Billboard" Hot 100 (making it their third top 40 single), only "Learn to Fly" and "Best of You" beat its position on the "Billboard" Hot 100.

Question: Which Foo Fighter album featured "RUN" as its first Single? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the album."
    },
    "album_number": {
      "type": "integer",
      "description": "The sequential number of the studio album for the band."
    },
    "first_single": {
      "type": "object",
      "properties": {
        "single_name": {
          "type": "string",
          "description": "The name of the first single from the album."
        },
        "release_date": {
          "type": "string",
          "description": "The release date of the first single."
        }
      },
      "required": [
        "single_name",
        "release_date"
      ],
      "additionalProperties": false
    },
    "album_release_date": {
      "type": "string",
      "description": "The release date of the album."
    }
  },
  "required": [
    "album_name",
    "band_name",
    "album_number",
    "first_single",
    "album_release_date"
  ],
  "additionalProperties": false
}
