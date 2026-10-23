{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Best of Glen Campbell: After Glen Campbell's Greatest Hits (1971), The Best of Glen Campbell was the second of official Capitol compilation albums by Glen Campbell and was released in 1976.\n\nGlen Campbell videos: American country music singer Glen Campbell released fifteen video albums and was featured in twenty-one music videos in his lifetime.  His first two music videos, \"By the Time I Get to Phoenix\" and \"Wichita Lineman\", were directed by Gene Weed in 1967 and 1968 respectively.  Campbell released his final music video, \"I'm Not Gonna Miss You\", in 2014 to coincide with the release of the documentary \"\".\n\nBy the Time I Get to Phoenix: \"By the Time I Get to Phoenix\" is a song written by Jimmy Webb.  Originally recorded by Johnny Rivers in 1965, it was covered by American country music singer Glen Campbell on his album of the same name.  Released on Capitol Records in 1967, Campbell's version topped \"RPM\"'s Canada Country Tracks, reached number two on \"Billboard\"'s Hot Country Singles chart, and won two awards at the 10th Annual Grammys.  Broadcast Music, Inc. (BMI) named it the third most performed song from 1940 to 1990.  The song was ranked number 20 on BMI's Top 100 Songs of the Century.  Frank Sinatra called it \"the greatest torch song ever written.\"\n\nThe Essential Glen Campbell Volume One: The Essential Glen Campbell Volume One is the first of a series of three albums which cover Glen Campbell's recordings for Capitol Records between 1962 and 1979.  The tracks are presented in a non-chronological order.  All three Essential CDs contain, next to single and albums tracks, previously unreleased recordings.  On The Essential Glen Campbell Volume One, these are \"Twelve Blues\", \"I Walk the Line\" (a jazz version of the Johnny Cash hit) and \"Blue Sky Shining\", from a 1979 recording session led by Nelson Riddle.  The Essential albums are also notable for containing some of the songs from The Artistry of Glen Campbell, the only original studio album by Glen Campbell that has not been released on CD or as a digital download.  Included here are \"Banjo Garden\" and \"Shenandoah\".\n\nThe Essential Glen Campbell Volume Two: The Essential Glen Campbell Volume Two is the second of a series of three albums which cover Glen Campbell's recordings for Capitol Records between 1962 and 1979.  The tracks are presented in a non-chronological order.  All three Essential CDs contain, next to single and albums tracks, previously unreleased recordings.  On The Essential Glen Campbell Volume Two, these are \"My Special Angel\", an uptempo version of \"Last Thing on My Mind\", \"Oh Boy\" and \"Don't It Make You Want To Go Home\".  The Essential albums are also notable for containing some of the songs from The Artistry of Glen Campbell, the only original studio album by Glen Campbell that has not been released on CD or as a digital download.  Included here is \"Greensleeves\".\n\nThe Essential Glen Campbell Volume Three: The Essential Glen Campbell Volume Three is the third of a series of three albums which cover Glen Campbell's recordings for Capitol Records from 1962-79.  The tracks are presented in a non-chronological order.  All three \"Essential\" CDs contain, next to single and albums tracks, previously unreleased recordings.  On The Essential Glen Campbell Volume Three, these are \"Beautiful Brown Eyes\", \"They'll Never Take Her Love from Me\", \"All the Way\" and \"Learnin' the Blues\".  The last two songs are from a 1979 recording session led by Nelson Riddle.  The \"Essential\" albums are also notable for containing some of the songs from The Artistry of Glen Campbell, the only original studio album by Campbell that has not been released on CD or as a digital download.  Included here is \"Tequila\".\n\nGlen Campbell's Greatest Hits: Glen Campbell's Greatest Hits was the first official Capitol compilation album by Glen Campbell and was released in 1971.  The Best of Glen Campbell followed in 1976, covering his later hits in addition to five on this compilation.\n\nUnited We Stand (Debby and Glen Campbell album): United We Stand is a release by Glen Campbell's eldest daughter Debby.  Debby Campbell has been performing with her father since 1987.  She was a featured vocalist on the Glen Campbell Goodtime Theater shows in Branson, MO during the mid 90s.  United We Stand was released as a cassette only.  It was sold in record stores and the Goodtime Theatre in Branson and after concerts during tours.  Next to solo recordings, it contains four duets with Glen Campbell, two of which were recorded live at the shows.\n\nWalls (Circus): \"Walls (Circus)\" is a song written by Tom Petty and recorded by Tom Petty and the Heartbreakers.  It was released in July 1996 as the only single from their soundtrack album \"Songs and Music from \"She's the One\"\".  The song features Lindsey Buckingham on background vocals in a sheer Fleetwood Mac style.  The song peaked at number 69 on the U.S. \"Billboard\" Hot 100 chart.  The song was recorded at Sound City Studios by engineer Sylvia Massy.  An alternate arrangement of the song, played at a faster tempo, was included on the soundtrack under the title \"Walls (No. 3)\".  The song was later covered by Glen Campbell on his 2008 album \"Meet Glen Campbell\".\n\nI Wanna Live: \"I Wanna Live\" is a song written by John D. Loudermilk and recorded by American country music singer Glen Campbell.  It was released in March 1968 as the lead single from the album, \"Hey Little One\".  The song was Glen Campbell's sixth release on the country charts and his first of five number ones on the country chart.  The song spent three non-consecutive weeks at number one and a total of fifteen weeks on the country charts.  The song was also Glen Campbell's third Top 40 release peaking at number thirty-six.\n\nQuestion: Who was the original artist of the song covered in Glen Campbell's 1967 video?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song featured in Glen Campbell's video.\"\n    },\n    \"glen_campbell_video_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year Glen Campbell's music video for the song was released.\"\n    },\n    \"original_artist\": {\n      \"type\": \"string\",\n      \"description\": \"The artist who originally recorded the song.\"\n    },\n    \"original_recording_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was originally recorded by the original artist.\"\n    },\n    \"songwriter\": {\n      \"type\": \"string\",\n      \"description\": \"The writer of the song.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"glen_campbell_video_year\",\n    \"original_artist\",\n    \"original_recording_year\",\n    \"songwriter\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song featured in Glen Campbell's video."
      },
      "glen_campbell_video_year": {
        "type": "integer",
        "description": "The year Glen Campbell's music video for the song was released."
      },
      "original_artist": {
        "type": "string",
        "description": "The artist who originally recorded the song."
      },
      "original_recording_year": {
        "type": "integer",
        "description": "The year the song was originally recorded by the original artist."
      },
      "songwriter": {
        "type": "string",
        "description": "The writer of the song."
      }
    },
    "required": [
      "song_title",
      "glen_campbell_video_year",
      "original_artist",
      "original_recording_year",
      "songwriter"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
