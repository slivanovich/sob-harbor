{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMary Frann: Mary Frann (born Mary Frances Luecke, February 27, 1943 – September 23, 1998) was an American stage, film and television actress.  Frann is best known for her role as Bob Newhart's wife, Joanna Loudon, on the CBS sitcom \"Newhart\", which aired from 1982 to 1990.\n\nRose in Paradise: \"Rose in Paradise\" is a song written by Stewart Harris and Jim McBride, and recorded by American country music artist Waylon Jennings.  It was released in January 1987 as the first single from the album \"Hangin' Tough\".  \"Rose in Paradise\" was Waylon Jennings' twelfth number one country single.  The single went to number one for one week and spent a total of nineteen weeks on the country chart.  Recording country artist Chris Young has a remake of the song as a duet with Willie Nelson from the album \"The Man I Want to Be\".\n\nOl' Waylon Sings Ol' Hank: Ol' Waylon Sings Ol' Hank is an album by Waylon Jennings, released independently on WJ Records, the singer's own label, in 1992.  As the title suggests, it features Jennings' performances of songs written or made famous by Hank Williams.  The recordings were made in 1985 and very few copies of the release were pressed; in effect, the original album is extremely rare today.  In 2006, the record was reissued on YMC Records as Waylon Sings Hank Williams with a new cover and a bonus track featuring Jennings reminiscing on his past.\n\nNashville Rebel (box set): Nashville Rebel is a box set by Waylon Jennings, released on RCA Records through Legacy Recordings in 2006.  According to Allmusic's Stephen Thomas Erlewine, it is \"\"the first comprehensive, multi-label Waylon Jennings retrospective ever assembled\", comprising ninety-two songs recorded between 1958 and 1994, with selections from the majority of the singer's recording career.  The first track of the box set is the Buddy Holly-produced \"Jole Blon,\" released in 1958, while the last is \"I Do Believe,\" a song produced by Don Was that was included on The Highwaymen's 1995 release, \"The Road Goes on Forever\".  The other material on the box set covers Jennings' career chronologically, with songs ranging from his years on RCA's roster to later compositions from his short-lived stay at Epic Records; it ignores, however, the tracks from Jennings albums released on independent labels.  The majority of the singer's charting singles are included in the package, as are collaborations such as \"Mamas Don't Let Your Babies Grow Up to Be Cowboys\" with Willie Nelson and \"Highwayman\" with The Highwaymen.  A notable addition is the previously unreleased \"The Greatest Cowboy of Them All,\" a 1978 duet with Johnny Cash which was later recorded by Cash alone for \"A Believer Sings the Truth\" (1979) and \"The Mystery of Life\" (1991); two others, \"It's Sure Been Fun\" and \"People in Dallas Got Hair,\" had never been released in the United States.  \"Nashville Rebel\" was released on four CDs, with a 140-page booklet and liner notes by Rich Keinzle and Lenny Kaye.\n\nThe Best of Waylon Jennings: The Best of Waylon Jennings is a 1970 album by Waylon Jennings released on RCA Records.\n\nThe Best of Waylon: The Best of Waylon is a compilation album by Waylon Jennings, released on RCA Records in 1986, following the singer's departure from the label.  It consists primarily of material from Jennings' last years at RCA, including \"Lucille (You Won't Do Your Daddy's Will)\" and \"Never Could Toe the Mark\".  It is also notable for including two previously unreleased Jennings recordings: \"I Don't Have Anymore Love Songs\" and \"Money Cannot Make the Man\".  \"The Best of Waylon\" failed to chart and was Jennings' final release on RCA.\n\nNashville Rebel (film): Nashville Rebel is a 1966 motion picture starring Waylon Jennings, Mary Frann, Gordon Oas-Heim, and CeCe Whitney.  This should not be confused with a 2006 compilation DVD of TV performances released by RCA Records to accompany the four-disc \"Nashville Rebel\" anthology.\n\nIf Ole Hank Could Only See Us Now: \"If Ole Hank Could Only See Us Now\" is a song co-written and recorded by American country music artist Waylon Jennings.  It was released in January 1988 as the second single from the album \"A Man Called Hoss\".  The song reached number 16 on the \"Billboard\" Hot Country Singles & Tracks chart.  The song was written by Waylon Jennings, his son Shooter Jennings and Roger Murrah.\n\nThe Days of Sand and Shovels: \"The Days of Sand and Shovels\" is a song written by Doyle Marsh and George Reneau, and recorded by American country music artist Waylon Jennings.  It was released in April 1969 as the second single from his album \"The Best of Waylon Jennings\".  The song peaked at number 20 on the \"Billboard\" Hot Country Singles chart.  It also reached number 1 on the \"RPM\" Country Tracks chart in Canada.\n\nCome with Me (Waylon Jennings song): \"Come with Me\" is a song written by Chuck Howard and recorded by American country music artist Waylon Jennings.  It was released in August 1979 as the first single from the album, \"What Goes Around Comes Around\".  \"Come with Me\" was Waylon Jennings' eighth No. 1 on the Country chart as a solo artist.  The single stayed at No. 1 for two weeks and spent a total of thirteen weeks on the Country chart.\n\nQuestion: The actress that played Joanna Loudon on \"Newhart\" also co-stared with Waylon Jennings in a film released in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"known_for_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role the actress is best known for.\"\n        },\n        \"known_for_show\": {\n          \"type\": \"string\",\n          \"description\": \"The TV show associated with the known role.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"known_for_role\",\n        \"known_for_show\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_co_starring_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film where the actress co-starred with Waylon Jennings.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"other_main_star\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the other main star in the film, as per the question.\"\n        }\n      },\n      \"required\": [\n        \"film_title\",\n        \"release_year\",\n        \"other_main_star\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released, which is the answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"actress_information\",\n    \"film_co_starring_details\",\n    \"answer_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_information": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "known_for_role": {
            "type": "string",
            "description": "The role the actress is best known for."
          },
          "known_for_show": {
            "type": "string",
            "description": "The TV show associated with the known role."
          }
        },
        "required": [
          "name",
          "known_for_role",
          "known_for_show"
        ],
        "additionalProperties": false
      },
      "film_co_starring_details": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film where the actress co-starred with Waylon Jennings."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "other_main_star": {
            "type": "string",
            "description": "The name of the other main star in the film, as per the question."
          }
        },
        "required": [
          "film_title",
          "release_year",
          "other_main_star"
        ],
        "additionalProperties": false
      },
      "answer_year": {
        "type": "integer",
        "description": "The year the film was released, which is the answer to the question."
      }
    },
    "required": [
      "actress_information",
      "film_co_starring_details",
      "answer_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
