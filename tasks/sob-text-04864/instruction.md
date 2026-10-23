{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBobby Fuller Died for Your Sins: Bobby Fuller Died for Your Sins is an album by recording artist and singer/songwriter Chuck Prophet.  It was released on February 10, 2017 on Yep Roc Records.  Chuck Prophet has described the album as :California Noir\", elaborating: \"the state has always represented the Golden Dream, and it's the tension between romance and reality that lurks underneath the surface in all noir films and paperbacks, and that connects these songs.  Doomed love, inconsolable loneliness, rags to riches to rags again, and fast-paced violence are always on the menu on the Left Coast.\"  The title of the album refers to the mystery long surrounding Bobby Fuller, a well regarded musician in the mid-1960s.  Found dead in his car at 23 years old, his death was ruled a suicide but still the topic of controversy, doubt and speculation.\n\nThe Bobby Fuller Four: The Bobby Fuller Four (sometimes stylized as Bobby Fuller 4) was a popular mid-1960s American rock & roll band started by Bobby Fuller.  With its first incarnation formed in 1962 in El Paso, Texas, the group went on to produce some of its most memorable hits under Mustang Records in Hollywood, California.  The band's most successful songs include \"Let Her Dance\", \"I Fought the Law\", and \"Love's Made a Fool of You.\"\n\nRandy Fuller (musician): Randall \"Randy\" Fuller (January 29, 1944) is an American rock singer, songwriter, and bass player best known for his work in the popular 60s rock group the Bobby Fuller Four with his older brother, Bobby Fuller.\n\nBobby Fuller: Robert Gaston Fuller (October 22, 1942 – July 18, 1966) was an American rock singer, songwriter, and guitarist best known for \"Love's Made a Fool of You\" and his cover of \"I Fought the Law\", recorded with his mid-1960s group The Bobby Fuller Four.\n\nJim Reese (musician): James Gordon Reese, Jr., simply known as Jim Reese, (7 December 1941 – 26 October 1991) was a longtime member of the famed rock and roll band, The Bobby Fuller Four.  Being virtuosic at a variety of instruments, he is perhaps best known for his guitar work (both lead and rhythm).  He provided backing vocals and rhythm guitar to the Bobby Fuller Four's greatest hit, \"I Fought the Law.\"\n\nTrash Box: Trash Box is a 5-CD box set of mid-1960s garage rock and psychedelic rock recordings, primarily by American bands.  This box set is similar to the earlier \"Pebbles Box\" (a 5-LP box set) and includes almost all of the same recordings in that box set (and in the same order), along with numerous bonus tracks at the end of each disc.  Supposedly, \"the Trash Box\" collects the first five volumes of the CDs in the Pebbles series (i.e., those released by AIP Records, not to be confused with the 4 earlier CDs that were issued by ESD Records).  However, as is generally true of the CD reissues of these five volumes (though not nearly to the same extent), the tracks differ significantly on all five discs as compared to both the original Pebbles LPs and the later Pebbles CDs in the corresponding volumes; and the surf rock rarities on \"Pebbles, Volume 4\" have been eschewed entirely.  Overall, there are 109 tracks in the box set (excluding the introduction and ending cuts) as compared to 101 songs on the individual CDs and 72 tracks in the \"Pebbles Box\".  Although most of the recordings on \"the Trash Box\" were released at some point on one of the individual Pebbles albums, several of the songs have not appeared elsewhere in the Pebbles series.  Inexplicably, one of these songs is the well-known hit \"I Fought the Law (but the Law Won)\" by the Bobby Fuller Four (on Disc Four) – which is also included in the \"Pebbles Box\" – in place of the much rarer \"Wine Wine Wine\" by Bobby Fuller that appears on \"Pebbles, Volume 2\".\n\nShivaree (TV series): Shivaree was a Los Angeles-based music variety show that ran in syndication from 1965 to 1966.  It was created and hosted by KFWB-AM personality Gene Weed, LA's top nighttime DJ at the time, and who in later years became a producer for Dick Clark Productions.  In its brief run, the show featured numerous well-known acts, including the Supremes, the Rolling Stones, Jackie Wilson, Marvin Gaye, Ronnie Dove, James Brown, Stevie Wonder, The Ronettes, Cher, Simon and Garfunkel, the Byrds, The Toys, the Bobby Fuller Four, Allan Sherman, Lesley Gore, and Gary Lewis, and was taped at KABC-TV's studios in LA.  It began in syndication in April 1965 and ran through May 1966 in more than 150 markets in the U.S. and seven countries internationally.  Although it was a syndicated series, Shivaree was produced and owned by the ABC network. \n\nShakedown! The Texas Tapes Revisited: Shakedown!  The Texas Tapes Revisited is a grammy nominated compilation of the work of Bobby Fuller and his recording band in El Paso, Texas before signing to Bob Keane's Del-Fi Records 1964.  The two CDs compile Fuller's hit local singles, and a wealth of outtakes and other recordings over its 50 tracks.\n\nStorm Large: Storm Large (born Susan Storm Large, June 25, 1969) is a singer, songwriter, actress and author.  She attracted national attention as a contestant on the CBS reality television show \"\".  For many years solely a rock artist, in recent years she has branched out into the theater and cabaret world.  A resident of Portland, Oregon, she currently balances performing with her own band in venues around the country and touring with the Portland-based band Pink Martini around the world.\n\nI Fought the Law: \"I Fought the Law\" is a song written by Sonny Curtis of the Crickets and popularized by a cover by the Bobby Fuller Four, which went on to become a top-ten hit for the band in 1966 and was also recorded by the Clash in 1979.  The Bobby Fuller Four version of this song was ranked No. 175 on the \"Rolling Stone\" list of The 500 Greatest Songs of All Time in 2004, and the same year was named one of the 500 \"Songs that Shaped Rock\" by the Rock and Roll Hall of Fame.\n\nQuestion: Is Bobby Fuller or Storm Large an author?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_a\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first person queried.\"\n        },\n        \"is_author\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the person is identified as an author in the context, false otherwise.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions attributed to the person in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_author\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_b\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second person queried.\"\n        },\n        \"is_author\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the person is identified as an author in the context, false otherwise.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions attributed to the person in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"is_author\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"at_least_one_is_author\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if at least one of the queried individuals is identified as an author.\"\n    },\n    \"author_identified\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified as an author, if any. Empty string if none.\"\n    }\n  },\n  \"required\": [\n    \"person_a\",\n    \"person_b\",\n    \"at_least_one_is_author\",\n    \"author_identified\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_a": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first person queried."
          },
          "is_author": {
            "type": "boolean",
            "description": "True if the person is identified as an author in the context, false otherwise."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions attributed to the person in the context."
          }
        },
        "required": [
          "name",
          "is_author",
          "professions"
        ],
        "additionalProperties": false
      },
      "person_b": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second person queried."
          },
          "is_author": {
            "type": "boolean",
            "description": "True if the person is identified as an author in the context, false otherwise."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions attributed to the person in the context."
          }
        },
        "required": [
          "name",
          "is_author",
          "professions"
        ],
        "additionalProperties": false
      },
      "at_least_one_is_author": {
        "type": "boolean",
        "description": "True if at least one of the queried individuals is identified as an author."
      },
      "author_identified": {
        "type": "string",
        "description": "The name of the person identified as an author, if any. Empty string if none."
      }
    },
    "required": [
      "person_a",
      "person_b",
      "at_least_one_is_author",
      "author_identified"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
