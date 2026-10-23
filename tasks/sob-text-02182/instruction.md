{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMy Own Worst Enemy (song): \"My Own Worst Enemy\" is a song by the American rock band Lit.  It was released in March 1999 as the lead single from Lit's second album, \"A Place in the Sun\", which was also released that year.  The song was only moderately successful at first, reaching number 17 on the Modern Rock Tracks chart on February 27, 1999.  It later achieved mainstream success, peaking at number 51 on the \"Billboard\" Hot 100 chart and number one on the Modern Rock Tracks (also known as Alternative Songs) chart.  The song's success helped \"A Place in the Sun\" to be certified platinum by the Recording Industry Association of America (RIAA) on October 27, 1999 for sales of 1,300,000 copies in the United States.  At the 1999 \"Billboard\" Music Awards, \"My Own Worst Enemy\" won the Modern Rock Track of the Year award.  Its music video was filmed by Gavin Bowden in a Las Vegas bowling alley.\n\nAstro Lounge: Astro Lounge, released in 1999, is the second full length album from the Californian rock band Smash Mouth.  It includes the single \"All Star\", arguably the group's most well-known song, which reached number four on the U.S. \"Billboard\" Hot 100.  Several other singles were released from the album, including \"Waste\" and \"Then the Morning Comes\".\n\n...To Be Loved: The Best of Papa Roach: ...To Be Loved: The Best of Papa Roach is the first compilation album by Californian rock band Papa Roach.  It was released on June 29, 2010.  It was the band's final album with Geffen Records, after the band left for Eleven Seven Music.  The album omits one of the band's biggest singles, \"Between Angels and Insects\", which was a top 20 hit in the UK.  The band members themselves asked their fans not to buy this CD (as well as expressed their resentment towards Geffen Records) because they do not endorse this release, nor would they receive royalties for its sales.\n\nA Place in the Sun (Lit album): A Place in the Sun is the second studio album by the American rock band Lit.\n\nZip-Lock (song): \"Zip-Lock\" is a song by the American pop punk band Lit, released as the follow-up single to their number one rock hit \"My Own Worst Enemy\" from their second album, \"A Place in the Sun\" in 1999.  While not as successful as its previous single, it was able to reach number 11 on the Modern Rock Tracks and number 34 on the Mainstream Rock Tracks.\n\nLifeline (Papa Roach song): \"Lifeline\" is the second single from Californian rock band Papa Roach's fifth album, \"Metamorphosis\", and eleventh released single in total.  The song was originally titled \"Hanging On\", and was changed to \"Lifeline\" after lead singer Jacoby Shaddix decided to alter the lyrics of the chorus.  It was released to iTunes on January 27, 2009 and as a Hot Topic exclusive CD single on February 10.  An accompanying music video was released on March 6, 2009.  To launch this song in its truest form, the band filmed \"Lifeline\" live during \"Crüe Fest\".\n\nLit (album): Lit is the fourth studio album by the American rock band Lit.  The album was recorded at World Class Audio in Anaheim and The Pool House in Fullerton, California.\n\nBetween Angels and Insects: \"Between Angels and Insects\", also known by its working title of \"Obsession\", is the third single from Californian rock band Papa Roach's first album, \"Infest\", and third released single in total.  It is also one of the band's most well known songs.\n\nLit (band): Lit is an American rock band, formed in 1995 in Fullerton, California.  They are best known for their hit song \"My Own Worst Enemy\".\n\nTime Is Running Out (Papa Roach song): \"Time Is Running Out\" is the seventh track from Californian rock band Papa Roach's fifth album, \"The Paramour Sessions\".  The song is also available as a downloadable track for the \"Rock Band\" games.\n\nQuestion: Californian rock band Lit recorded A Place in the Sun in 1995, but what's their best known song?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the rock band.\"\n    },\n    \"best_known_song\": {\n      \"type\": \"string\",\n      \"description\": \"The band's most well-known song.\"\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the album mentioned in the question.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the album was released.\"\n        }\n      },\n      \"required\": [\n        \"album_name\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"question_recording_year_correct\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the recording year mentioned in the question for the album is correct based on the context.\"\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"best_known_song\",\n    \"album_details\",\n    \"question_recording_year_correct\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the rock band."
      },
      "best_known_song": {
        "type": "string",
        "description": "The band's most well-known song."
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_name": {
            "type": "string",
            "description": "The name of the album mentioned in the question."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the album was released."
          }
        },
        "required": [
          "album_name",
          "release_year"
        ],
        "additionalProperties": false
      },
      "question_recording_year_correct": {
        "type": "boolean",
        "description": "Indicates if the recording year mentioned in the question for the album is correct based on the context."
      }
    },
    "required": [
      "band_name",
      "best_known_song",
      "album_details",
      "question_recording_year_correct"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
