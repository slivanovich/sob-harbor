{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTori Amos discography: Tori Amos is an American pianist and singer-songwriter whose musical career began in 1980, at the age of seventeen, when she and her brother co-wrote the song \"Baltimore\".  The song was selected as the winning song in a contest for the Baltimore Orioles and was recorded and pressed locally as a 7\" single.  From 1984–89, Amos fronted the synthpop band Y Kant Tori Read, which released one self-titled album with Atlantic Records in 1988 before breaking up.  Shortly thereafter, Amos began writing and recording material that would serve as the debut of her solo career.  Still signed with Atlantic, and its UK counterpart East West, Amos' initial solo material was rejected by the label in 1990.  Under the guidance of co-producers Eric Rosse, Davitt Sigerson and Ian Stanley, a second version of the album was created and accepted by the label the following year.\n\nFade to Red: Fade to Red: Tori Amos Video Collection is a double DVD set from recording artist and musician Tori Amos and was released by Rhino Entertainment on February 14, 2006.  It featured music videos spanning 1992 to 2005, including the singles \"Silent All These Years,\" \"Crucify,\" \"Cornflake Girl,\" and \"A Sorta Fairytale\", which co-stars Oscar winner Adrien Brody.  The DVD features digitally re-mastered 5.1 audio and included a comprehensive audio commentary by Amos herself on each video.  The collection omits the following music videos: \"Glory of the 80's,\" \"Strange Little Girl,\" and \"Mary (Tales Version).\"\n\nMidwinter Graces: Midwinter Graces is the eleventh solo studio album by singer-songwriter Tori Amos released on November 10, 2009 (November 16, 2009 in the UK), through Universal Republic Records.  It is the first seasonal album by Amos, and is also notable for marking her return to a more classical, stripped-down, baroque sound with various synths, string-instruments, the harpsichord and Amos's own signature \"Bösendorfer\" piano at center stage, once more.  The album, like previous releases from Amos, is available in a single form CD or a Deluxe edition which includes 3 bonus tracks, a 20-page photo book, and a DVD containing an interview with Amos.  The standard edition was not released in the US or Canada.\n\nTori Amos: Live from New York: Tori Amos: Live from New York is a benefit concert performed by American singer and songwriter Tori Amos on January 23, 1997.  The concert was performed at the Madison Square Garden Theater in New York to launch \"Unlock the Silence\", a year-long promotional and fund-raising campaign sponsored by cK Calvin Klein to raise awareness of the work undertaken by RAINN, the Rape, Abuse and Incest National Network, a non-profit organization offering support and counseling to survivors of sexual assault.  The performance included compositions from her first three albums, including \"Silent All These Years\" from her debut album \"Little Earthquakes\" (1992), which served as the touchstone track for the \"Unlock the Silence\" campaign.\n\nDatura (song): \"Dātura\" or \"Datura\" is a song written and recorded by American singer Tori Amos.  It is the ninth song of Amos's fifth record \"To Venus and Back\", which was released in September 1999.  It is included in the first disc of the double album subtitled \"Orbiting\" that contains eleven original studio recordings.  The song lists the names of the plants found in Amos's garden and was created during the recording sessions of \"To Venus and Back\".  The song's title refers to datura, a plant known for its toxic and hallucinogenic properties.  Amos has never performed the song live due to its complex structure and time signatures which makes it hard to reproduce with a live band.  However, in 2011 Amos incorporated the \"room in my heart\" bridge when performing \"Take to the Sky\" during her concert in Brussels on October 29, 2011 Video on YouTube .  She also performed the song in a similar fashion throughout the Unrepentant Geraldines Tour.\n\nTori Amos: Complete Videos 1991–1998: Tori Amos: The Complete Videos 1991–1998 is a VHS cassette of all of Tori Amos's videos from \"Little Earthquakes\" through \"From the Choirgirl Hotel\", with the exception of \"Professional Widow\".  The video collection was released in a standard-size hard plastic VHS case and a large soft plastic VHS case (with the same catalogue number).  The video collection runs approximately 75 minutes and was released by Atlantic Records\n\nTori Amos: Tori Amos (born Myra Ellen Amos, August 22, 1963 ) is an American singer-songwriter, pianist and composer.  She is a classically trained musician with a mezzo-soprano vocal range.\n\nEric Clapton: Eric Patrick Clapton, {'1': \", '2': \", '3': \", '4': \"} (born 30 March 1945), is an English rock and blues guitarist, singer, and songwriter.  He is the only three-time inductee to the Rock and Roll Hall of Fame: once as a solo artist and separately as a member of the Yardbirds and Cream.  Clapton has been referred to as one of the most important and influential guitarists of all time.  Clapton ranked second in \"Rolling Stone\" magazine's list of the \"100 Greatest Guitarists of All Time\" and fourth in Gibson's \"Top 50 Guitarists of All Time\".  He was also named number five in \"Time\" magazine's list of \"The 10 Best Electric Guitar Players\" in 2009.\n\nTales of a Librarian: Tales of a Librarian (complete title: \"A Tori Amos Collection: Tales of a Librarian\") is the first retrospective compilation album by singer/songwriter Tori Amos.  Given the option to be involved in the project, Amos elected to take a central role in the production of the collection, released in 2003 on her former label Atlantic Records.\n\nY Kant Tori Read: Y Kant Tori Read was a 1980s synthpop band, fronted by singer-songwriter Tori Amos.  The band released one album, also called \"Y Kant Tori Read\", which was largely unsuccessful; Atlantic Records abandoned promoting the record completely after only two months of release.  The band originally consisted of Amos, Steve Caton, Matt Sorum (later of Guns N' Roses), and bassist Brad Cobb.  They worked with record producer Joe Chiccarelli, and Kim Bullard, later of Kajagoogoo.  The name comes from an incident in Amos's childhood where she was asked to leave the Peabody Conservatory because she refused to read sheet music.\n\nQuestion: Are Tori Amos and Eric Clapton from the same country?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"artist_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"are_from_same_country\": {\n      \"type\": \"boolean\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"artist_1\",\n    \"artist_2\",\n    \"are_from_same_country\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "artist_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "are_from_same_country": {
        "type": "boolean"
      },
      "reasoning": {
        "type": "string"
      }
    },
    "required": [
      "artist_1",
      "artist_2",
      "are_from_same_country",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
