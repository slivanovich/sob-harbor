{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFarewell Song: Farewell Song is a 1982 collection of nine previously unreleased recordings of Janis Joplin with Big Brother and the Holding Company, the Kozmic Blues Band, and Full Tilt Boogie.  Tracks include \"Cheap Thrills\"-era outtakes and live performances; \"Misery 'N\", \"Farewell Song\", and \"Catch Me Daddy\".\n\nI Got Dem Ol' Kozmic Blues Again Mama!: I Got Dem Ol' Kozmic Blues Again Mama!  is a 1969 studio album by Janis Joplin.  It was the first solo studio album Joplin recorded after leaving her former band, Big Brother and the Holding Company, and the only one released in her lifetime (\"Pearl\" was released 3 months after Joplin's death).\n\nRare Pearls: Rare Pearls is a 1999 collection of rare Janis Joplin Studio recordings with Big Brother and the Holding Company and live performances with The Kozmic Blues Band.  It was released only as part of the box set \"Box of Pearls\" (1999), which contained reissues of all of Joplin's albums with added bonus tracks, and this compilation.\n\nKacee Clanton: Kacee Clanton (born Kellie Kristine Clanton) is a Los Angeles–based singer, songwriter, stage actress and performance coach who has worked as a background vocalist for recording artists Beth Hart, Joe Cocker, and Luis Miguel and toured as lead vocalist with Big Brother and the Holding Company.  She has played Janis Joplin in the musical \"Love, Janis\" and was the alternate lead on Broadway in the Tony-nominated musical \"A Night With Janis Joplin.\"  She is also a vocal and performance instructor at Los Angeles College of Music.  Both her music and vocals have been used in a variety of films, TV shows, and video games.\n\nJanis Joplin: Janis Lyn Joplin ( ; January 19, 1943 – October 4, 1970) was an American rock singer and songwriter.  She was one of the biggest female rock stars of her era.  After releasing three albums, she died of a heroin overdose at age 27.  A fourth album, \"Pearl\", was released in January 1971, just over three months after her death.  It reached number one on the \"Billboard\" charts.\n\nMary Bridget Davies: Mary Bridget Davies (born August 30, 1978) is an American singer and actress.  She performs with her own band, \"The Mary Bridget Davies Group\", and is also an interpreter of Janis Joplin's music.  She received a Tony Award nomination for Best Lead Actress in a Musical for her performance as Janis in \"A Night with Janis Joplin\".  Her band \"The Mary Bridget Davies Group\" released an album with original songs in 2012 titled \"Wanna Feel Somethin\".\n\nGrant Lyons: Grant Lyons (born 1941) is an American writer.  He was born in Butler, Pennsylvania, but grew up in Port Arthur, Texas.  While attending Thomas Jefferson High School in Port Arthur, Lyons and a group of male friends befriended Janis Joplin, who was otherwise an outcast in school.  As documented in all biographies of Janis Joplin, he was the person who played Janis her first Lead Belly record, which is considered a formative influence on her style of singing.  He attended Tulane University on a football scholarship, and he has a master's degree in Library Science as well as in History.  Lyons is also the grandson of Captain Ulysses Grant Lyons, who ran and was briefly pronounced winner of a U.S. house of Representatives seat, before Earl Beshlin was eventually named the winner.\n\nKozmic Blues: \"Kozmic Blues\" is a song from Janis Joplin's \"I Got Dem Ol' Kozmic Blues Again Mama! \" album, her first after departing Big Brother and the Holding Company.  It was a part of Joplin's set at Woodstock Festival in 1969.  Although the concert as a whole is not regarded as Joplin at her best, that specific performance became very popular and was released on \"The Essential Janis Joplin\".\n\nJanis (1975 album): Janis is a collection of performances by Janis Joplin, issued in 1975 as a compilation album containing film soundtrack and live recordings.  Disc one is subtitled \"From the soundtrack of the motion picture \"Janis\" (with substituted performances of 'Piece of my Heart' and 'Cry Baby')\".  In addition to concert recordings from Toronto and Frankfurt, there are several short TV-interviews.  Disc two contains recordings from Austin, Texas (1963 and 1964), plus four recordings from San Francisco (1965).  The album booklet contains a photo documentary, with 22 pictures from Janis Joplin's life and career.\n\nMove Over!: Move Over!  is an album by Janis Joplin released for Record Store Day 2011.  The album contains unreleased, rare and alternate songs from all three of Joplin's backing bands, Big Brother and the Holding Company, Kozmic Blues Band and Full Tilt Boogie Band.\n\nQuestion: Kozmic Blues was performed by Janis Joplin as part of which iconic festival set?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song performed.\"\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who performed the song.\"\n    },\n    \"festival_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the iconic festival where the song was performed.\"\n    },\n    \"performance_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the performance took place at the festival.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"artist_name\",\n    \"festival_name\",\n    \"performance_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song performed."
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who performed the song."
      },
      "festival_name": {
        "type": "string",
        "description": "The name of the iconic festival where the song was performed."
      },
      "performance_year": {
        "type": "integer",
        "description": "The year the performance took place at the festival."
      }
    },
    "required": [
      "song_title",
      "artist_name",
      "festival_name",
      "performance_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
