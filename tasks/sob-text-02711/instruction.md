{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBand on the Run: Band on the Run is the third studio album by Paul McCartney and Wings, released in December 1973.  It marked the fifth album by Paul McCartney since his departure from the Beatles in April 1970.  Although sales were modest initially, its commercial performance was aided by two hit singles – \"Jet\" and \"Band on the Run\" – such that it became the top-selling studio album of 1974 in the United Kingdom and Australia; in addition to revitalising McCartney's critical standing.  It remains McCartney's most successful album and the most celebrated of his post-Beatles works.\n\nYou're the One (album): You're the One is the tenth solo studio album by Paul Simon, released in 2000 and his first successful studio album in 10 years.  The album was nominated for a Grammy Award for Album of the Year in 2001, with Simon becoming the first artist to be nominated in that category in five consecutive decades (1960s-2000s).  (In 2006, Paul McCartney became the only other artist to match this feat with \"Chaos and Creation in the Backyard\").\n\nMcCartney (album): McCartney is the debut studio album by English musician Paul McCartney.  It was issued on Apple Records in April 1970 after McCartney had resisted attempts by his fellow Beatles to have the release delayed to allow for Apple's previously scheduled titles, notably the band's \"Let It Be\" album.  McCartney recorded this solo album during a period of depression and confusion, following John Lennon's private announcement on September 20, 1969 that he was leaving the Beatles, and the conflict over its release further estranged McCartney from his bandmates.  A press release in the form of a self-interview, supplied with UK promotional copies of \"McCartney\", led to the announcement of the group's break-up on 10 April 1970.\n\nTemporary Secretary: \"Temporary Secretary\" is a song by Paul McCartney, featured on his 1980 album \"McCartney II\".  In 2013, \"Rolling Stone\" ranked it the #36 all-time McCartney post-Beatles song, calling it a \"cult favorite\" and an \"oddly catchy electro-pop nugget, about a slightly creepy-sounding guy looking to hire a temp.\"  In 2014, \"Temporary Secretary\" was ranked the 167th greatest song of all time by critics of \"NME\" magazine.  They described it as \"wonky electropop that didn't sound so much ahead of its time as out of it altogether.\"\n\nOff the Ground: Off the Ground is the ninth solo studio album by Paul McCartney under his own name (discounting then his Wings-era discography, among other releases), released in 1993.  As his first studio album of the 1990s, it is also the follow-up to the well-received \"Flowers in the Dirt\" (1989).\n\nTug of War (Paul McCartney album): Tug of War is the third solo studio album by Paul McCartney, released in April 1982.  It was McCartney's first album released after the dissolution of Wings in April, 1981 and McCartney's first album after the murder of former songwriting partner John Lennon.  The album was produced by former Beatles producer George Martin and was a number 1 hit in numerous countries.  It was hailed as a return-to-form for McCartney upon release.  Its remastered deluxe edition received a nomination for Best Boxed or Special Limited Edition Package at the 2017 Grammy Awards.\n\nRun Devil Run (album): Run Devil Run is the eleventh solo studio album by Paul McCartney using his own name, released in 1999.  It features mostly covers of both familiar and obscure 1950s rock and roll songs, along with three original McCartney compositions written in the same style, including the title track.  As his first project following first wife Linda's death in 1998, McCartney felt the need to get back to his roots and perform some of the music he loved as a teenager.  On 14 December 1999, McCartney returned to the Cavern Club stage to play a set publicising the new album.\n\nFlaming Pie: Flaming Pie is the tenth solo studio album by Paul McCartney under his own name, first released in 1997.  His first studio album in over four years, it was mostly recorded following McCartney's involvement in the highly successful \"Beatles Anthology\" project.  The album was recorded in several locations over two years, 1995 and 1997, featuring two songs dating from 1992.  The album featured several of McCartney's family members and friends, most notably McCartney's son, James McCartney.  In \"Flaming Pie\"'s liner notes, McCartney said: \"\"[The Beatles Anthology]\" reminded me of The Beatles' standards and the standards that we reached with the songs.  So in a way it was a refresher course that set the framework for this album.\"\n\nMemory Almost Full: Memory Almost Full is the fourteenth solo studio album by Paul McCartney, discounting his Wings-and-Beatles-era discography, his orchestral works and his output as the Fireman.  It was released in the United Kingdom on 4 June 2007 and in the United States a day later.  The album was the first release on Starbucks' Hear Music label.  It was produced by David Kahne and recorded at Abbey Road Studios, Henson Recording Studios, AIR Studios, Hog Hill Mill Studios and RAK Studios between October 2003, and from 2006 to February 2007.  In between the 2003 and 2006 sessions, McCartney was working on another studio album, \"Chaos and Creation in the Backyard\" (2005), with producer Nigel Godrich.\n\nMcCartney II: McCartney II is the second completely solo studio album by Paul McCartney, and the first since the formation of Wings in 1971.  It was released in 1980, a year before the band's dissolution and while their future lay in limbo.  The album is a significant departure for McCartney, as much of it relies heavily on synthesizers and studio experimentation.  It was reissued on 13 June 2011 as part of the \"Paul McCartney Archive Collection\".  The album remains a cult favourite.\n\nQuestion: which solo studio album by Paul McCartney did Temporary Secretary  featured on\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who performed the song.\"\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album the song is featured on.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the album was released.\"\n        },\n        \"album_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of album (e.g., solo studio album).\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"release_year\",\n        \"album_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"artist_name\",\n    \"album_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "artist_name": {
        "type": "string",
        "description": "The name of the artist who performed the song."
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album the song is featured on."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the album was released."
          },
          "album_type": {
            "type": "string",
            "description": "The type of album (e.g., solo studio album)."
          }
        },
        "required": [
          "album_title",
          "release_year",
          "album_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "artist_name",
      "album_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
