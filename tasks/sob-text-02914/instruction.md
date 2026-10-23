{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSkin Deep (Cher song): \"Skin Deep\" is a rock song performed by American singer-actress Cher from her eighteenth studio album, \"Cher\".  It was written by Mark Goldenberg and Jon Lind, and produced by Lind.  It was released as the album's third single in mid-1988.\n\nJust Like Jesse James: \"Just Like Jesse James\" is a pop rock song by American singer-actress Cher in her nineteenth album \"Heart of Stone\".  It is the third North American and second European official single released in October 1989 by Geffen Records.  The song was written by Desmond Child and Diane Warren.  It is a December 1989 top ten hit.  The song's title is a reference to legendary Wild West bandit Jesse James.\n\nBang Bang (My Baby Shot Me Down): \"Bang Bang (My Baby Shot Me Down)\" is the second single by American singer-actress Cher from her second album, \"The Sonny Side of Chér\".  Written by her then-husband Sonny Bono and released in 1966, the song reached No. 3 in the UK Singles Chart and No. 2 on the \"Billboard\" Hot 100 for a single week (behind \"(You're My) Soul and Inspiration\" by The Righteous Brothers), eventually becoming one of Cher's biggest-selling singles of the 1960s.\n\nDon't Hide Your Love: \"Don't Hide Your Love\" is a song released by American singer-actress Cher as the second single released from the album \"Foxy Lady\".  The song was written by Neil Sedaka and Howard Greenfield.  It hit number 46 on the \"Billboard\" Hot 100, and number 19 on the Adult Contemporary chart.  Allmusic editor Joe Viglione wrote that this song should have been duet with the songwriter itself, because it would bring her back into the public eye.\n\nSong for the Lonely: \"Song for the Lonely\" is a song recorded by American singer-actress Cher for her 24th studio album, \"Living Proof\".  It was released on March 19, 2002, as the second single from the album in Europe while in North America it was released as the lead single, by Warner Bros. and WEA.  The song was performed in some American television programs and in her 2002–2005 .\n\nThe Sonny Side of Chér: The Sonny Side of Chér is the second studio album by American singer-actress Cher, released on April, 1966 by Imperial, as her second album, Cher again collaborated with Sonny Bono and Harold Battiste.  The album is by-and-large a covers album and contains two songs written by Bono.  The title of the album is a pun on the name of Cher's first husband Sonny Bono.  After its release, the album garnered positive reviews from critics.  The album was Cher's second successful album of the sixties.\n\nAlive Again (Cher song): \"Alive Again\" is a song performed by American singer-actress Cher from her twenty-fourth studio album, \"Living Proof\".  It was released as a third and final European single from the album on June 11, 2002 by WEA, while the song remains unreleased in North America.  The song has never been performed live.  The song had received positive reviews from music critics, but its commercial response was limited and quite poor in some European countries.  It managed to chart in Germany and Switzerland.\n\nI Paralyze (song): \"I Paralyze\" is a song written by John Farrar and Steve Kipner.  It was produced for American singer-actress Cher on 1982, as the second single from her seventeenth album of the same name by Columbia Records.\n\nBackflip (song): \"Backflip\" is the second single by American singer-actress Raven-Symoné from her third album, \"This Is My Time\".  It debuted on Radio Disney on July 28, 2004.\n\nRaven-Symoné: Raven-Symoné Christina Pearman ( ; born December 10, 1985), sometimes credited as Raven, is an American actress, singer, songwriter, television personality, and producer.  She first appeared on television in 1989 on \"The Cosby Show\" as Olivia Kendall.  She released her debut album, \"Here's to New Dreams\" in 1993; the single, \"That's What Little Girls Are Made Of\" charted number 68 on the US \"Billboard\" Hot 100.  The next album, \"Undeniable\", was released on May 4, 1999.\n\nQuestion: \"Backflip\" is the second single by American singer-actress Raven-Symoné from her third album, titled what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who performed the song.\"\n    },\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album from which the song was released.\"\n    },\n    \"album_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The sequential number of the album in the artist's discography.\"\n    },\n    \"single_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The sequential number of the single from the album.\"\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"song_title\",\n    \"album_title\",\n    \"album_number\",\n    \"single_number\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who performed the song."
      },
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "album_title": {
        "type": "string",
        "description": "The title of the album from which the song was released."
      },
      "album_number": {
        "type": "integer",
        "description": "The sequential number of the album in the artist's discography."
      },
      "single_number": {
        "type": "integer",
        "description": "The sequential number of the single from the album."
      }
    },
    "required": [
      "artist_name",
      "song_title",
      "album_title",
      "album_number",
      "single_number"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
