{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNewport Jazz Festival: Live at Carnegie Hall: Ella Fitzgerald at the Newport Jazz Festival: Live at Carnegie Hall is a 1973 live album by the American jazz singer Ella Fitzgerald, accompanied by a reconstructed Chick Webb Band, the pianist Ellis Larkins, and for the second half of the album, the Tommy Flanagan Quartet (featuring Joe Pass).\n\nElla Fitzgerald and Billie Holiday at Newport: Ella Fitzgerald and Billie Holiday at Newport is a 1958 live album by Ella Fitzgerald and Billie Holiday, recorded at the 1957 Newport Jazz Festival.\n\nElla in Japan: 'S Wonderful: Ella in Japan: 'S Wonderful is a 1964 live album by the American jazz singer Ella Fitzgerald, recorded in Tokyo, Japan.  Norman Granz sold the Verve label to MGM Records in 1961, but continued to manage her career and produce Ella Fitzgerald's recordings.  Granz supervised frequently live concert tours, planning several live projects for release on record.  In late January 1964 work began on an album, called \"Ella In Nippon\", the album did not reach past the post-production stage, remaining uncompleted and unreleased for 47 years.  Tracks 1 to 12 on this 2011 release are the tracks Norman Granz mixed for the unreleased album \"Ella In Nippon\".\n\nAt the Opera House: At the Opera House is a 1958 live album by Ella Fitzgerald.  The album presents a recording of the 1957 Jazz at the Philharmonic Concerts.  This series of live jazz concerts was devised by Fitzgerald's manager Norman Granz, they ran from 1944 to 1983.  Featured on this occasion, in 1957, are Fitzgerald and the leading jazz players of the day in an onstage jam session.  The first half of the 1990 CD edition includes a performance that was recorded on September 29, 1957 at the Chicago Opera House, whilst the second half highlights the concert recorded on October 7, 1957 at the Shrine Auditorium, in Los Angeles.  The original LP obviously included only the mono tracks (#10-18).\n\nShrine Auditorium: The Shrine Auditorium is a landmark large-event venue in Los Angeles, California.  It is also the headquarters of the Al Malaikah Temple, a division of the Shriners.  It was designated a Los Angeles Historic-Cultural Monument (No. 139) in 1975.\n\nElla Fitzgerald Live at Mister Kelly's: Ella Fitzgerald Live at Mister Kelly's is a live album of a 1958 Ella Fitzgerald performance at Mister Kelly's, and released in 2007.\n\nElla Fitzgerald Sings the Johnny Mercer Song Book: Ella Fitzgerald Sings the Johnny Mercer Song Book is a 1964 studio album by the American jazz singer Ella Fitzgerald, with the Nelson Riddle Orchestra, focusing on the songs of Johnny Mercer.  It was recorded in Los Angeles, California.  This is Fitzgerald's fifth and final collaboration with Riddle during her years on the Verve label.\n\nSonic Boom (Lee Morgan album): Sonic Boom is an album by jazz trumpeter Lee Morgan, recorded on April 14 and 28, 1967 but not released on the Blue Note label until 1979.  The 2003 CD reissue added seven tracks recorded on September 12 & October 10, 1969 which were first released on the original double LP edition of \"The Procrastinator\".  Therefore, the CD edition includes performances by Morgan with two line-ups: the first one with David Newman, Cedar Walton, Ron Carter and Billy Higgins, whilst the second features Julian Priester, George Coleman, Harold Mabern, Walter Booker and Mickey Roker.\n\nTodd Gordon: Todd Gordon is a singer and entertainer from Scotland, United Kingdom.  He was a Beatles fan until the age of eleven when he first listened to Frank Sinatra's seminal \"Songs for Swingin' Lovers\".  Gordon's first-ever visit to a major jazz concert was in 1973 to see Duke Ellington performing at the Usher Hall in Edinburgh.  His second was on April 11, 1974 to see Ella Fitzgerald at The Apollo in Glasgow.  Recently, the \"Ella Fitzgerald Charitable Foundation\" included Gordon's off- and on- stage encounters with Ella Fitzgerald.\n\nLive in Japan (John Coltrane album): Live in Japan is a four-disc box set by American saxophonist John Coltrane and his last group, featuring the quintet of Coltrane, his wife/pianist Alice, saxophonist/bass clarinetist Pharoah Sanders, bassist Jimmy Garrison and drummer Rashied Ali.  The 4-CD set compiles all the music issued as three albums in the seventies by Impulse! ; \"Concert In Japan\" (1973, US 2-LP, electronically processed for compatible quadrophonic/stereo), \"Coltrane In Japan\" (1974, Japan 3-LP (side six is blank), mono) and \"Second Night In Tokyo\" (1976, Japan 3-LP (side six contains an interview, mono).  (Some of this material was also reissued as two 2-LP sets in 1980 by MCA under the titles \"Coltrane In Tokyo Vol.  1\" and \"Coltrane In Tokyo Vol.  2\") The first CD issues were by Impulse!  Japan as two 2-CD sets: \"Live In Japan Vol.  1\" (same as \"Coltrane In Japan\") and \"Live In Japan Vol.  2\" (same as \"Second Night In Tokyo\").  The US 4-CD edition includes both of these volumes, with identical mastering from the original mono tapes.  The side six interview from \"Second Night In Tokyo\" has never been reissued on any CD edition.\n\nQuestion: At the Opera House is a 1958 live album by Ella Fitzgerald, the first half of the 1990 CD edition includes a performance, whilst the second half highlights the concert recorded on October 7, 1957 at which andmark large-event venue in Los Angeles, California?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the album being discussed.\"\n    },\n    \"recording_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date of the concert highlighted in the second half of the album.\"\n    },\n    \"venue\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the venue where the concert was recorded.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The city and state where the venue is located.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the venue from the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\",\n        \"description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_title\",\n    \"recording_date\",\n    \"venue\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_title": {
        "type": "string",
        "description": "The title of the album being discussed."
      },
      "recording_date": {
        "type": "string",
        "description": "The date of the concert highlighted in the second half of the album."
      },
      "venue": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the venue where the concert was recorded."
          },
          "location": {
            "type": "string",
            "description": "The city and state where the venue is located."
          },
          "description": {
            "type": "string",
            "description": "A description of the venue from the context."
          }
        },
        "required": [
          "name",
          "location",
          "description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_title",
      "recording_date",
      "venue"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
