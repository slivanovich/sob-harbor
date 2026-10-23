{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDon't Love You No More (I'm Sorry): \"Don't Love You No More (I'm Sorry)\" is the second single from British singer Craig David's third album \"The Story Goes...\".  \"Don't Love You No More (I'm Sorry)\" gave David his second top ten hit from \"The Story Goes...\" and one of his biggest hits to date, tying with number-one single \"7 Days\" for longest-running single in the UK top 75, spending fifteen weeks on the chart.  However, \"Don't Love You No More (I'm Sorry)\" is his biggest for most consecutive weeks inside the top 75 as \"7 Days\" had fourteen, before it re-entered for a week.  The song was his biggest hit from \"The Story Goes\", peaking at number 4, one place lower than \"All the Way\", which only spent six weeks inside the top 75.\n\nThe Time Is Now (album): The Time Is Now is the upcoming seventh studio album by British singer Craig David, scheduled for release on 26 January 2018.  The album will feature guests JP Cooper, Bastille, AJ Tracey, Ella Mai, Kaytranada and GoldLink.  The first single from the album, titled \"Heartline\", was released on 14 September 2017, through Craig David's official YouTube account.\n\nAll the Way (Craig David song): \"All the Way\" is the first single released by the British singer Craig David from his third album \"The Story Goes...\".  It was the first single he released with new label Warner Bros.  Records after Wildstar Records went bankrupt.  After missing the top ten with previous singles \"World Filled with Love\" and \"You Don't Miss Your Water ('Til the Well Runs Dry)\", \"All The Way\" returned David to the top three.  It was the highest-charting single from \"The Story Goes...\" but not the biggest-selling as \"Don't Love You No More (I'm Sorry)\" spent over double the amount of weeks inside the UK top 75.  The music video became the sixth Craig David video directed by Max & Dania.\n\nWhen the Bassline Drops: \"When the Bassline Drops\" is a song by British singer Craig David and British rapper Big Narstie.  It is David's first single in six years, it was released on 27 November 2015 by Insanity and Speakerbox Media as the lead single from his sixth studio album, \"Following My Intuition\" (2016).  The song was written by David, Scott Wild and Tyrone Lindo, and peaked at number ten on the UK Singles Chart.\n\nHot Stuff (Let's Dance): \"Hot Stuff (Let's Dance)\" is a song by British singer Craig David.  It was released in November 2007 as the second single from his fourth album \"Trust Me\", following the single \"This Is the Girl\" with rapper Kano.  It samples David Bowie's 1983 number-one single \"Let's Dance\".\n\nKano (rapper): Kane Robinson (born 21 May 1985), better known as Kano, is an English rapper and actor from East Ham, London.  He is a significant contributor to grime.  In 2004, Kano released his debut single \"P's and Q's\", which was an underground hit within the grime community.  After signing to 679 Recordings, Kano released his debut studio album \"Home Sweet Home\" (2005), which peaked at number 36 on the UK Albums Chart and featured the top 30 singles \"Typical Me\" and \"Nite Nite\".  This was followed by the album \"London Town\" (2007), featuring Kano's highest-charting single \"This is the Girl\" featuring Craig David.  Through Bigger Picture Music, Kano released his third and fourth albums, \"140 Grime St\" (2008) and \"Method to the Maadness\" (2010), both which charted in the top 50.\n\nHeartline: \"Heartline\" is a song by British singer Craig David, from his upcoming studio album \"The Time Is Now\", set to be released in 2018, this is the first single from the album.  The single was released on 14 September 2017, on Craig David's official YouTube account.\n\nThis Is the Girl: \"This is the Girl\" was the first single from British rapper Kano's second studio album \"London Town\" and the first from British singer Craig David's fourth studio album \"Trust Me\".  The song was released in 2007 and reached its peak of number 18 in the UK charts on 18 September 2007.\n\nShutdown (Skepta song): \"Shutdown\" is a song by English rapper Skepta.  It was released as the second single from Skepta's fourth album \"Konnichiwa\" (2016) on 26 April 2015 through Boy Better Know.  A music video for the song was uploaded to YouTube on the day of the song's release.  \"Shutdown\" peaked at number 39 on the UK Singles Chart.  The song samples speech from a Vine video created by Canadian rapper Drake.  The song was covered by English rock band Slaves in the BBC Radio 1 Live Lounge.  The song is featured in \"NBA 2K17\".\n\nTrust Me (album): Trust Me is the fourth studio album by the English singer Craig David.  It was released on 12 November 2007 in the United Kingdom and on 6 May 2008 in the United States.  The album entered the UK Albums Chart at number 18, but failed to make any impact on the \"Billboard\" 200, although it did manage to peak at number 58 on the Top R&B/Hip-Hop Albums chart.\n\nQuestion: \"Hot Stuff (Let's Dance)\" is a song by British singer Craig David, it was released in November 2007 as the second single from his fourth album \"Trust Me\", following the single \"This Is the Girl\" with which English rapper and actor from East Ham, London, better know as?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"main_song_context\": {\n      \"type\": \"object\",\n      \"description\": \"Contextual information about the main song mentioned in the question.\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"Title of the main song.\"\n        },\n        \"artist\": {\n          \"type\": \"string\",\n          \"description\": \"Main artist of the song.\"\n        },\n        \"album\": {\n          \"type\": \"string\",\n          \"description\": \"Album the song is from.\"\n        },\n        \"release_month\": {\n          \"type\": \"string\",\n          \"description\": \"Month of the song's release as a single.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"Year of the song's release as a single.\"\n        },\n        \"single_order\": {\n          \"type\": \"integer\",\n          \"description\": \"Order of the single from the album.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"artist\",\n        \"album\",\n        \"release_month\",\n        \"release_year\",\n        \"single_order\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"preceding_single_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the single that preceded the main song.\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"Title of the preceding single.\"\n        },\n        \"collaborating_artist_type\": {\n          \"type\": \"string\",\n          \"description\": \"Type of artist collaborating on the preceding single.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"collaborating_artist_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"collaborating_artist_identity\": {\n      \"type\": \"object\",\n      \"description\": \"Identity details of the collaborating artist on the preceding single.\",\n      \"properties\": {\n        \"stage_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name the artist is better known as.\"\n        },\n        \"real_name\": {\n          \"type\": \"string\",\n          \"description\": \"The real name of the artist.\"\n        },\n        \"origin_location\": {\n          \"type\": \"string\",\n          \"description\": \"The origin city/area of the artist.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"List of professions of the artist.\"\n        }\n      },\n      \"required\": [\n        \"stage_name\",\n        \"real_name\",\n        \"origin_location\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"main_song_context\",\n    \"preceding_single_details\",\n    \"collaborating_artist_identity\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "main_song_context": {
        "type": "object",
        "description": "Contextual information about the main song mentioned in the question.",
        "properties": {
          "title": {
            "type": "string",
            "description": "Title of the main song."
          },
          "artist": {
            "type": "string",
            "description": "Main artist of the song."
          },
          "album": {
            "type": "string",
            "description": "Album the song is from."
          },
          "release_month": {
            "type": "string",
            "description": "Month of the song's release as a single."
          },
          "release_year": {
            "type": "integer",
            "description": "Year of the song's release as a single."
          },
          "single_order": {
            "type": "integer",
            "description": "Order of the single from the album."
          }
        },
        "required": [
          "title",
          "artist",
          "album",
          "release_month",
          "release_year",
          "single_order"
        ],
        "additionalProperties": false
      },
      "preceding_single_details": {
        "type": "object",
        "description": "Details about the single that preceded the main song.",
        "properties": {
          "title": {
            "type": "string",
            "description": "Title of the preceding single."
          },
          "collaborating_artist_type": {
            "type": "string",
            "description": "Type of artist collaborating on the preceding single."
          }
        },
        "required": [
          "title",
          "collaborating_artist_type"
        ],
        "additionalProperties": false
      },
      "collaborating_artist_identity": {
        "type": "object",
        "description": "Identity details of the collaborating artist on the preceding single.",
        "properties": {
          "stage_name": {
            "type": "string",
            "description": "The name the artist is better known as."
          },
          "real_name": {
            "type": "string",
            "description": "The real name of the artist."
          },
          "origin_location": {
            "type": "string",
            "description": "The origin city/area of the artist."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of professions of the artist."
          }
        },
        "required": [
          "stage_name",
          "real_name",
          "origin_location",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "main_song_context",
      "preceding_single_details",
      "collaborating_artist_identity"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
