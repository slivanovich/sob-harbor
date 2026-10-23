{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGeorge Harrison (album): George Harrison is the eighth studio album by English musician George Harrison, released in February 1979.  It was written and recorded through much of 1978, a period of domestic contentment for Harrison, during which he married Olivia Trinidad Arias and became a father for the first time, to son Dhani.  Harrison wrote several of the songs in Hawaii, while the track \"Faster\" reflected his year away from music-making, when he and Arias attended many of the races in the 1977 Formula 1 World Championship.  The album also includes the hit single \"Blow Away\" and \"Not Guilty\", a song that Harrison originally recorded in 1968 for the Beatles' White Album.\n\nSomewhere in England: Somewhere in England is the ninth studio album by George Harrison, released in 1981.  The album was recorded as Harrison was becoming increasingly frustrated with the music industry.  The album's making was a long one, during which conflicts with Warner Bros.  Records arose.  \"Somewhere in England\" was the first Harrison album to be released after the death of his former Beatles bandmate John Lennon; the lyrics of its first single, \"All Those Years Ago\", pay tribute to Lennon.\n\nIf You Believe (George Harrison song): \"If You Believe\" is a song by English musician George Harrison from his 1979 album \"George Harrison\".  Harrison began writing the song with Gary Wright on New Year's Day 1978 and finished the lyrics a month later while in Hawaii.  The song appears as the final track on \"George Harrison\".  Its lyrics are a statement on the power of faith to bring about a desired outcome.\n\nSoft Touch: \"Soft Touch\" is a song by English musician George Harrison from his 1979 album \"George Harrison\".  It was also issued as the B-side of the album's lead single, \"Blow Away\", apart from in North America, where it was the B-side of the second single, \"Love Comes to Everyone\".  Harrison wrote the song while in the Virgin Islands with his future wife, Olivia Arias, shortly before recording his 1976 album \"Thirty Three & 1/3\".  The song is a love song in which Harrison also conveys his wonder at the idyllic island setting.\n\nWhat Is Life: \"What Is Life\" is a song by the English musician George Harrison, released on his 1970 triple album \"All Things Must Pass\".  In many countries, it was issued as the second single from the album, in February 1971, becoming a top-ten hit in the United States, Canada and elsewhere, and topping singles charts in Australia and Switzerland.  In the United Kingdom, \"What Is Life\" appeared as the B-side to \"My Sweet Lord\", which was the best-selling single there of 1971.  Harrison's backing musicians on the song include Eric Clapton and the entire Delaney & Bonnie Friends band, with whom he had toured during the final months of the Beatles.  Harrison co-produced the recording with Phil Spector, whose Wall of Sound production also employed a prominent string arrangement by John Barham and multiple acoustic rhythm guitars, played by Harrison's fellow Apple Records signings Badfinger.\n\nDark Horse (George Harrison song): \"Dark Horse\" is a song by English musician George Harrison, released as the title track to his 1974 solo album on Apple Records.  The song was the album's lead single in North America, becoming a top-twenty hit in the United States, but it was Harrison's first single not to chart in Britain when issued there in February 1975.  While the term \"dark horse\" had long been applied to Harrison due to his success as a solo artist following the Beatles' break-up in 1970, commentators recognise the song as Harrison's rebuttal to a number of possible detractors: those reviewers who criticised the spiritual content of his 1973 album \"Living in the Material World\"; his first wife, Pattie Boyd; and his former bandmates John Lennon and Paul McCartney.  Harrison also used the title for that of his record label, and his 1974 North American tour with Ravi Shankar would come to be known as the Dark Horse Tour.\n\nDing Dong, Ding Dong: \"Ding Dong, Ding Dong\" is a song by English musician George Harrison, written as a New Year's Eve singalong and released in December 1974 on his album \"Dark Horse\".  It was the album's lead single in Britain and some other European countries, and the second single, after \"Dark Horse\", in North America.  A large-scale production, the song incorporates aspects of Phil Spector's Wall of Sound technique, particularly his Christmas recordings from 1963.  In addition, some Harrison biographers view \"Ding Dong\" as an attempt to emulate the success of two glam rock anthems from the 1973–74 holiday season: \"Merry Xmas Everybody\" by Slade, and Wizzard's \"I Wish It Could Be Christmas Everyday\".  The song became only a minor hit in Britain and the United States, although it was a top-twenty hit elsewhere in the world.\n\nWriting's on the Wall (George Harrison song): \"Writing's on the Wall\" is a song by English musician George Harrison from his 1981 album \"Somewhere in England\".  It was also the B-side of the album's lead single, \"All Those Years Ago\", which Harrison wrote as a tribute to his former Beatles bandmate John Lennon.  In his lyrics, Harrison sings of the transient nature of life and the importance of recognising a spiritual purpose.  Although the song was written long before Lennon's murder in New York in December 1980, the lyrics' reference to how easily friends can be shot down and killed led listeners to interpret it as a further comment on Lennon's death.\n\nThe Heart Gently Weeps: \"The Heart Gently Weeps\" is the first single from the 2007 album \"8 Diagrams\" by the Wu-Tang Clan.  The song features a sample of The Beatles' song \"While My Guitar Gently Weeps\".  It features guest appearances from three other musicians: R&B singer Erykah Badu sings the song's chorus; Dhani Harrison, son of Beatles member George Harrison, plays acoustic guitar; and John Frusciante of the Red Hot Chili Peppers is featured on lead guitar.  This song was made using a cover version of the George Harrison song played by the blues guitarist Jimmy Ponder.\n\nBlow Away: \"Blow Away\" is a song by English musician George Harrison that was released in February 1979 on his album \"George Harrison\".  It was also the lead single from the album.  The song is one of Harrison's most popular recordings from his solo career and has appeared on the compilations \"Best of Dark Horse 1976–1989\" and \"\".\n\nQuestion: Writing's on the Wall is from a George Harrison album with which song as its first single?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"requested_song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song mentioned in the question.\"\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album the song is from.\"\n        },\n        \"album_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the album.\"\n        },\n        \"lead_single_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the lead single from the album.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"album_release_year\",\n        \"lead_single_title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist.\"\n    }\n  },\n  \"required\": [\n    \"requested_song_title\",\n    \"album_details\",\n    \"artist_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "requested_song_title": {
        "type": "string",
        "description": "The title of the song mentioned in the question."
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album the song is from."
          },
          "album_release_year": {
            "type": "integer",
            "description": "The release year of the album."
          },
          "lead_single_title": {
            "type": "string",
            "description": "The title of the lead single from the album."
          }
        },
        "required": [
          "album_title",
          "album_release_year",
          "lead_single_title"
        ],
        "additionalProperties": false
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the artist."
      }
    },
    "required": [
      "requested_song_title",
      "album_details",
      "artist_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
