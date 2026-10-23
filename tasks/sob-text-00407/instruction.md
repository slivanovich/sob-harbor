{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJailbreak (AC/DC song): \"Jailbreak\" is a song by Australian hard rock band AC/DC.  It is the ninth and final track of their third Australian album \"Dirty Deeds Done Dirt Cheap\", released in September 1976.  The song was not released in North America until 1984.  It was written by Angus Young, Malcolm Young, and Bon Scott.\n\nLessons in Violence: The Best Of Exodus: Lessons in Violence is a compilation album by thrash metal band Exodus.  Even though this compilation album was released after \"Impact Is Imminent\", it contains no tracks from that album as Exodus had switched record labels by that time.  The AC/DC cover \"Dirty Deeds Done Dirt Cheap\" was recorded live on July 14th, 1989 at the Fillmore in San Francisco, CA.  It was recorded during Exodus' \"Fabulous Disaster\" tour and can be found on their 1991 live album \"Good Friendly Violent Fun\".  \"Another Lesson In Violence\" was recorded live at the Astoria in London, England on March 8th, 1989 during the \"Headbanger's Ball Tour\".\n\nDirty Deeds Done Dirt Cheap: Dirty Deeds Done Dirt Cheap is an album by Australian hard rock band AC/DC.  It was the band's third LP released in Australia and in Europe in 1976 but was not released in the US until 1981, more than one year after Bon Scott's death.  All songs were written by Angus Young, Malcolm Young and Bon Scott.\n\nRide On (AC/DC song): \"Ride On\" is a song and single by Australian hard rock band AC/DC originally released on the album \"Dirty Deeds Done Dirt Cheap\" and later re-released on the album \"Who Made Who\".  In both versions, the song is sung by Bon Scott.  Atypically for an AC/DC song, it has a sad, slow blues, almost ballad-like feel to it.  The lyrics concern a man reflecting on mistakes he has made in a relationship while drinking alcohol.  It has frequently been cited as one of AC/DC's best songs.\n\nAngus Young: Angus McKinnon Young (born 31 March 1955) is an Australian guitarist, best known as the co-founder, lead guitarist, songwriter and sole constant original member of the Australian hard rock band AC/DC.  He is known for his energetic performances, schoolboy-uniform stage outfits and his own version of Chuck Berry's duckwalk.  Young was ranked 24th in \"Rolling Stone\" magazine's 100 greatest guitarists of all-time list.\n\nDirty Deeds Done Dirt Cheap (song): \"Dirty Deeds Done Dirt Cheap\" is a song by Australian hard rock band AC/DC.  It is the title track and first track of their album \"Dirty Deeds Done Dirt Cheap\", released in September 1976, and was written by Angus Young, Malcolm Young, and Bon Scott.\n\nVanda &amp; Young: Vanda & Young were a songwriting/producing duo composed of Harry Vanda and George Young.  They performed as members of 1960s Australian rock group The Easybeats where Vanda was their lead guitarist and backing singer and Young was their rhythm guitarist and backing singer.  Vanda & Young co-wrote most of The Easybeats later hits including their international hit \"Friday on My Mind\" and they were the record producers for the group from 1967.  Young is the older brother of Malcolm and Angus Young of the hard rock band AC/DC, being the record producer behind several of the band's biggest albums (such as 1976's \"Dirty Deeds Done Dirt Cheap\").\n\nMark Evans (musician): Mark Whitmore Evans (born 2 March 1956) is an Australian bass guitarist for the Australian rock band Rose Tattoo who was an early member of hard rock band AC/DC from March 1975 to June 1977.  His playing featured on their albums \"T.N.T\", \"High Voltage\", \"Dirty Deeds Done Dirt Cheap\", \"Let There Be Rock\" and \"'74 Jailbreak\".  Evans has played for numerous other groups, sometimes on lead guitar, including Finch (a.k.a. Contraband), Cheetah, Swanee, Heaven and The Party Boys.  Evans' autobiography, \"Dirty Deeds: My Life Inside/Outside of AC/DC\" was released in December 2011.\n\nFuse Box (album): Fuse Box was an AC/DC tribute album released in Australia in 1995 by BMG.  The album compiled a selection of the country's more prominent alternative rock artists from the period.  Most of these songs only appear on this album, with the exception of Ed Kuepper's \"Highway to Hell\", which he also recorded for his album \"A King in the Kindness Room\".  A live version of \"Dirty Deeds Done Dirt Cheap\" was included on Nitocris' 1995 \"Epic Voyage\" EP.  The Meanies' version of \"It's a Long Way to the Top\" was released as a single, with a promotional video featuring the band playing on the back of a truck driving through the Melbourne CBD, an homage to the original clip.\n\n'74 Jailbreak: The first track is from the Australian version of \"Dirty Deeds Done Dirt Cheap\" (1976), while the rest are from the Australian version of the band's debut album, \"High Voltage\", recorded in 1974 and released early the following year.\n\nQuestion: In what year was the main writer of Dirty Deeds Done Dirt Cheap born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"writer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"writer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the main writer identified.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the writer.\"\n        },\n        \"band_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the writer in the band.\"\n        }\n      },\n      \"required\": [\n        \"writer_name\",\n        \"birth_year\",\n        \"band_role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the band that performed the song.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"writer_details\",\n    \"band_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "writer_details": {
        "type": "object",
        "properties": {
          "writer_name": {
            "type": "string",
            "description": "The name of the main writer identified."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the writer."
          },
          "band_role": {
            "type": "string",
            "description": "The role of the writer in the band."
          }
        },
        "required": [
          "writer_name",
          "birth_year",
          "band_role"
        ],
        "additionalProperties": false
      },
      "band_name": {
        "type": "string",
        "description": "The name of the band that performed the song."
      }
    },
    "required": [
      "song_title",
      "writer_details",
      "band_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
