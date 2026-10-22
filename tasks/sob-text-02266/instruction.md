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
Madder Rose: Madder Rose was a New York City-based alternative rock band who recorded in the 1990s.  The band was fronted by Mary Lorson, who shared songwriting duties with guitarist Billy Coté.  The two singer/songwriters continued their collaboration after Madder Rose disbanded, Coté as guest producer on Lorson's three discs with Saint Low, Lorson as guest vocalist on Coté's Jazz Cannon disc.  Lorson and Cote have also created the original scores to several films, notably HBO's documentary of Sally Mann, and in 2008 released a disc with Kathy Ziegler as The Piano Creeps.  The name Madder Rose came from the herb-based paint rose madder.  Many of their songs, including "Panic On" and "Car Song", were featured in John Peel's end-of-year round-up, the Festive Fifty, major feature films, and television shows.  The band released three albums on Atlantic Records, and one on Cooking Vinyl, before breaking up in 1999.

Laßt Jubeltöne laut erklingen: Laßt Jubeltöne laut erklingen (Let exultation sound loudly), WAB 76, is a festive song composed by Anton Bruckner in 1854.

Chitta Kukkad: "Chitta Kukkad" is a wedding-themed Punjabi dance song by Bollywood composer, producer and singer Parichay, with lyrics written by rapper and lyricist The Gunsmith.  The track has been sung by Neha Kakkar and Gippy Grewal and is the 3rd song released from the film Loveshhuda by Tips Industries Limited, starring Girish Kumar and Navneet Kaur Dhillon.  This festive song is based on the classic folk song "Chitta Kukkad Banere Te" by Pakistani singer Musarrat Nazir, but has been revamped with fresh production, composition and new lyrics.

Go to the Mardi Gras: "Go to the Mardi Gras" or "Mardi Gras in New Orleans" is a New Orleans Mardi Gras-themed R&B song that was performed by Professor Longhair (real name Henry Roland Byrd) and recorded several times since 1949.  He co-wrote the song with Theresa Terry.  The song was covered by Fats Domino and released as a single in 1953.  It is now considered an iconic festive song of the New Orleans Carnival season.

Merry Christmas Everyone: "Merry Christmas Everyone" is a festive song by Welsh British singer-songwriter Shakin' Stevens.  Written by Bob Heatlie and produced by Dave Edmunds, it was the fourth number one single from Shakin' Stevens on the UK Singles Chart.

The Seven Joys of Mary (carol): "The Seven Joys of Mary" (Roud # 278) is a traditional carol about Mary's happiness at moments in the life of Jesus, probably inspired by the trope of the Seven Joys of the Virgin in the devotional literature and art of Medieval Europe.  Though not traditionally associated with Christmas, it has become so in the modern era.

Festgesang, WAB 15: The Festgesang (Festive song), WAB 15, is a cantata composed by Anton Bruckner in 1855.

Carol (music): A carol is in Modern English a festive song, generally religious but not necessarily connected with church worship, and often with a dance-like or popular character.

Alright (Kendrick Lamar song): "Alright" is a song by American rapper Kendrick Lamar, taken from his third album "To Pimp a Butterfly" (2015).  Lyrically a festive song about hope, it features uncredited vocals from the song's co-producer Pharrell Williams during the chorus.  "Alright" was released to radio stations as the album's fourth single on June 30, 2015.  Most music publications considered it among the best songs and videos of the year, highlighting their message in the social context of the time.  "Alright" received four nominations at the 58th Grammy Awards: Song of the Year, Best Music Video, Best Rap Performance and Best Rap Song, winning the latter two.

Carnival Time (song): "Carnival Time" is a New Orleans Mardi Gras-themed R&B song that was performed by Al Johnson and recorded in 1960.  The song's composition was originally credited to Al Johnson and Joe Ruffino, though Johnson now holds exclusive rights.  It is now considered an iconic festive song of the New Orleans Carnival season.

Question: What is the name of a festive song with a dance-like character about Mary's happiness?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_name": {
      "type": "string",
      "description": "The name of the festive song."
    },
    "song_type": {
      "type": "string",
      "description": "The genre or type of the song, e.g., carol."
    },
    "is_festive": {
      "type": "boolean",
      "description": "Indicates if the song is considered festive."
    },
    "describes_marys_happiness": {
      "type": "boolean",
      "description": "Indicates if the song is about Mary's happiness."
    },
    "has_dance_like_character": {
      "type": "boolean",
      "description": "Indicates if the song has a dance-like or popular character."
    }
  },
  "required": [
    "song_name",
    "song_type",
    "is_festive",
    "describes_marys_happiness",
    "has_dance_like_character"
  ],
  "additionalProperties": false
}
