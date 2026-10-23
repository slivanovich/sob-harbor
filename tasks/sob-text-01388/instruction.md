{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTrust Nobody: \"Trust Nobody\" is a song by Norwegian DJ and record producer Cashmere Cat, featuring vocals by American singer Selena Gomez and Canadian rapper Tory Lanez.  It was released on September 30, 2016, as the second single from Cashmere's debut studio album, \"9\" (2017).  The track was written by Cashmere Cat, Gomez, Lanez, Benny Blanco, Frank Dukes and Starrah.  It was produced by Cashmere Cat, Benny Blanco and Frank Dukes.\n\nAfterski: \"Afterski\" is the debut single from Norwegian DJ and electronic music duo Broiler.  It was released in Norway on 15 November 2012 for digital download.  The song peaked at number 3 on the Norwegian Singles Chart.  The song is included on their debut studio album \"The Beginning\" (2013)\n\nEn gang til (song): \"En gang til\" is a single from Norwegian DJ and electronic music duo Broiler and Norwegian band Sirkus Eliassen.  It was released in Norway on 20 June 2013 for digital download.  The song peaked at number 8 on the Norwegian Singles Chart.  The song is included on Broiler's debut studio album \"The Beginning\" (2013).\n\nVannski: \"Vannski\" is a single from Norwegian DJ and electronic music duo Broiler.  It was released in Norway on 16 May 2013 for digital download.  The song peaked at number 1 on the Norwegian Singles Chart, making it their first number one single in Norway.  The song is included on their debut studio album \"The Beginning\" (2013)\n\nCashmere Cat: Magnus August Høiberg (born 29 November 1987), known professionally as Cashmere Cat, is a Norwegian DJ, record producer, musician and turntablist.  He is best known for producing songs for various artists, as well as remixing and editing songs from those respective artists as well.  He also represented Norway in the DMC World DJ Championships as DJ Final from 2006 to 2009.  His debut EP, \"Mirror Maru\", released in October 2012, gained recognition from several other producers.\n\nTungevaag &amp; Raaban: Tungevaag & Raaban is a dance music producer duo consisting of the Norwegian DJ Martin Tungevaag from Stadlandet in Norway, and the Swedish DJ and producer Robbin Söderlund (better known by his artistic name Raaban) from Borås in Sweden.  Sharing a common interest for the EDM genre, they have both collaborated and separately produced music within the genre for many years.\n\nStay (Kygo song): \"Stay\" is a song by Norwegian DJ and record producer Kygo, featuring American singer Maty Noyes.  The song was produced by Kygo with fellow Norwegian, William Wiik Larsen, who also wrote it with Noyes.  It was released as the fourth single from Kygo's debut studio album, \"Cloud Nine\" (2016).  An official music video for the song was released on 18 February 2016.\n\nFeeling Right (Everything Is Nice): \"Feeling Right (Everything Is Nice)\" is the debut single by Norwegian DJ and producer Matoma, featuring rapper Wale and Jamaican dancehall artist Popcaan.  It was released on October 16, 2015, by Parlophone Records.  The song is produced by Matoma and contains choruses, one bridge, and one verse from Popcaan´s Everything Nice.  The remaining verses are performed by Wale.\n\nID (song): \"ID\" is a song by Norwegian DJ and record producer Kygo.  The song was released on 10 February 2015 and reached number 31 on the Norwegian Singles Chart.  \"ID\" was also included on the \"FIFA 16\" soundtrack.  It was the official anthem of the 2015 Ultra Music Festival.\n\nLA Confidential (song): \"LA Confidential\" is a song by Canadian rapper Tory Lanez.  The song was released on January 29, 2016 by EMI Records, Mad Love Records, Interscope Records and Virgin Records.  The song is produced by Benny Blanco, Cashmere Cat, Pop and Toro.\n\nQuestion: What is the name of the rapper who created a song produced by a Norwegian DJ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"rapper_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the rapper.\"\n    },\n    \"norwegian_dj_producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Norwegian DJ or producer who produced songs for this rapper.\"\n    },\n    \"songs_produced\": {\n      \"type\": \"array\",\n      \"description\": \"A list of songs by the rapper that were produced by the specified Norwegian DJ/producer.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"song_title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the song.\"\n          },\n          \"release_date\": {\n            \"type\": \"string\",\n            \"description\": \"The release date of the song.\"\n          },\n          \"other_producers\": {\n            \"type\": \"array\",\n            \"description\": \"Other producers involved in the song, besides the Norwegian DJ/producer.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          },\n          \"album_details\": {\n            \"type\": \"object\",\n            \"description\": \"Details about the album the song is included on, if available.\",\n            \"properties\": {\n              \"album_name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of the album.\"\n              },\n              \"album_artist\": {\n                \"type\": \"string\",\n                \"description\": \"The artist of the album.\"\n              }\n            },\n            \"required\": [\n              \"album_name\",\n              \"album_artist\"\n            ],\n            \"additionalProperties\": false\n          }\n        },\n        \"required\": [\n          \"song_title\",\n          \"release_date\",\n          \"other_producers\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"rapper_name\",\n    \"norwegian_dj_producer_name\",\n    \"songs_produced\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "rapper_name": {
        "type": "string",
        "description": "The name of the rapper."
      },
      "norwegian_dj_producer_name": {
        "type": "string",
        "description": "The name of the Norwegian DJ or producer who produced songs for this rapper."
      },
      "songs_produced": {
        "type": "array",
        "description": "A list of songs by the rapper that were produced by the specified Norwegian DJ/producer.",
        "items": {
          "type": "object",
          "properties": {
            "song_title": {
              "type": "string",
              "description": "The title of the song."
            },
            "release_date": {
              "type": "string",
              "description": "The release date of the song."
            },
            "other_producers": {
              "type": "array",
              "description": "Other producers involved in the song, besides the Norwegian DJ/producer.",
              "items": {
                "type": "string"
              }
            },
            "album_details": {
              "type": "object",
              "description": "Details about the album the song is included on, if available.",
              "properties": {
                "album_name": {
                  "type": "string",
                  "description": "The name of the album."
                },
                "album_artist": {
                  "type": "string",
                  "description": "The artist of the album."
                }
              },
              "required": [
                "album_name",
                "album_artist"
              ],
              "additionalProperties": false
            }
          },
          "required": [
            "song_title",
            "release_date",
            "other_producers"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "rapper_name",
      "norwegian_dj_producer_name",
      "songs_produced"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
