{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBang Masters: Bang Masters is a compilation album by Van Morrison released by Columbia's Legacy Records imprint in 1991.  The tracks were remixed from the original multi-tracks and were given a wider stereo spread with less compression.  The alternate version of \"Brown Eyed Girl\" included on this album was according to Bill Flannagan take six out of the twenty-two takes before the final form released in 1967 on \"Blowin' Your Mind! \".\n\nNew York Sessions '67: New York Sessions '67 is a two-disc retrospective album of recordings made by Van Morrison in 1967 for Bang Records that were later released in the 1990s.  Other album releases with the same recordings have been called \"Payin' Dues\" and \"The Complete Bang Sessions\".  The first disc presents material already available on \"Blowin' Your Mind! \" and on the previous Bang compilation albums \"T.B. Sheets\" and \"Bang Masters\".  The second disc contains the notorious \"Contractual Obligation\" session – thirty-one improvised nonsense songs Morrison recorded in order to fulfill his contract with Bang Records.  The song \"Thirty Two\" takes a swipe at Berns's production style and \"Brown Eyed Girl\": Morrison sings \"we'll get three guitars . .  and we'll do the sha, sha-la-la bit.\"  Tracks from this album would be officially released on the compilation album \"The Authorized Bang Collection\".\n\nT.B. Sheets (album): T.B. Sheets is a retrospective album of recordings made in 1967 by Northern Irish musician Van Morrison, released in 1973 on Bang Records.  It contains songs that had appeared on Morrison's debut album, \"Blowin' Your Mind! \", including his first hit, \"Brown Eyed Girl\".  It also features early versions of two songs that appeared in 1968 on Morrison's acclaimed album \"Astral Weeks\" — \"Beside You\" and \"Astral Weeks\"' centerpiece, \"Madame George\".\n\nClassics: The Early Years: Classics: The Early Years is a compilation album by Neil Diamond released in 1983 featuring the early recordings he made for Bang Records in 1966 and 1967.  After CBS acquired the Bang Records catalogue, the twelve best recordings were reissued on this album.  Columbia gave Diamond control of the Bang masters of his recordings.  The original copyright notice of this album read \"(C) and (P)1983 Neil Diamond and CBS Inc.\" This compilation has a different track lineup compared to the 1968 Bang compilation album titled \"Neil Diamond's Greatest Hits\" which contains two cover songs. All the songs in this album are original Diamond compositions and substitutes \"I'm A Believer\" (which The Monkees covered) and \"Shilo\" in place of the Gary U.S. Bonds hit \"New Orleans\" and the Tommy James and the Shondells hit \"Hanky Panky.\"\n\nBlowin' Your Mind!: Blowin' Your Mind!  is the debut album by Northern Irish musician Van Morrison, released in 1967.  It was recorded 28–29 March 1967 and contained his first solo pop hit \"Brown Eyed Girl\".  It was included by \"Rolling Stone\" as one of the \"40 Essential Albums of 1967\".\n\nT.B. Sheets: \"T.B. Sheets\" is a blues-influenced song written and recorded by Northern Irish singer-lyricist Van Morrison, recorded for the Bang Records label in 1967 and included on his first solo album, \"Blowin' Your Mind! \".  It later appeared on the Bang compilation, \"T.B. Sheets\".\n\nThe Best of Van Morrison Volume 3: The Best of Van Morrison Volume 3 is a compilation album by Northern Irish singer-songwriter Van Morrison, that was released on 11 June 2007 in the UK with a digital version released in the U.S. on iTunes Store, on 12 June 2007.  Manhattan/EMI Music Catalog Marketing released the CD version of the album on 19 June 2007 in the United States.  This new two-disc collection of 31 tracks has been compiled by Morrison himself.  It offers an overview of his large volume of material since the release of \"The Best of Van Morrison Volume Two\" in 1993.  The album's thirty-one tracks include previously unreleased collaborations with Tom Jones (\"Cry For Home\") and Bobby Bland (\"Tupelo Honey\") as well as duets with John Lee Hooker, B.B. King and Ray Charles.  The 2003 duet with Ray Charles is \"Crazy Love\" a song originally recorded on Morrison's 1970 album \"Moondance\".  \"Blue and Green\" was previously donated to be used on the charity album \"\", which raised money for relief efforts intended for Gulf Coast victims devastated by hurricane Katrina.  The duet with Tom Jones, \"Cry For Home\" was taken from the same recording sessions that produced the \"Sometimes We Cry\" duet between the two artists, which featured on Jones' successful album \"Reload\".  \"Cry for Home\" was released as a single on 4 June 2007 in the UK, and was followed by \"Blue and Green\" on 27 August.\n\nNo Prima Donna: The Songs of Van Morrison: No Prima Donna: The Songs of Van Morrison released in October 1994 is the first tribute album for the songs of singer-songwriter Van Morrison.  The album was produced by Van Morrison and his friend for many years, Phil Coulter.  Morrison's longtime girlfriend, Michelle Rocca was the model on the cover of the album.  Morrison was actively involved in choosing the songs and the artists who performed them, which is unusual for most tribute albums.\n\nBrown Eyed Girl: \"Brown Eyed Girl\" is a song by Northern Irish singer and songwriter Van Morrison.  Written by Morrison and recorded in March 1967 for Bang Records owner and producer Bert Berns, it was released as a single in June 1967 on the Bang label, peaking at No. 10 on the \"Billboard\" Hot 100.  It featured The Sweet Inspirations singing back-up vocals and is considered to be Van Morrison's signature song.  \"Brown Eyed Girl\" has remained a staple on classic rock radio, and has been covered by hundreds of bands over the decades.\n\nTakin' the Country Back: Takin' the Country Back is the seventeenth studio album of country music artist John Anderson.  It was released in 1997 under the Mercury Records label.  The album produced the singles: \"Somebody Slap Me\", which peaked at 22 on Country charts, \"Small Town\", which peaked at 44 and the title track, which peaked at 41.  Also included on the album was a cover of the Van Morrison's 1967 hit \"Brown Eyed Girl\" from his album Blowin' Your Mind! .\n\nQuestion: Bang Masters contains an alternate version of which first solo pop hit by Van Morrison, originally released on Blowin' Your Mind in 1967?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"original_album\": {\n      \"type\": \"string\",\n      \"description\": \"The album on which the song was originally released.\"\n    },\n    \"original_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was originally released.\"\n    },\n    \"is_first_solo_pop_hit\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the song was Van Morrison's first solo pop hit.\"\n    },\n    \"compilation_album_with_alternate_version\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the compilation album that contains the alternate version of the song.\"\n    },\n    \"alternate_version_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"take_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The take number of the alternate version included on the compilation album.\"\n        },\n        \"total_takes_before_final\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of takes recorded before the final version was released.\"\n        }\n      },\n      \"required\": [\n        \"take_number\",\n        \"total_takes_before_final\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"original_album\",\n    \"original_release_year\",\n    \"is_first_solo_pop_hit\",\n    \"compilation_album_with_alternate_version\",\n    \"alternate_version_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "original_album": {
        "type": "string",
        "description": "The album on which the song was originally released."
      },
      "original_release_year": {
        "type": "integer",
        "description": "The year the song was originally released."
      },
      "is_first_solo_pop_hit": {
        "type": "boolean",
        "description": "Indicates if the song was Van Morrison's first solo pop hit."
      },
      "compilation_album_with_alternate_version": {
        "type": "string",
        "description": "The name of the compilation album that contains the alternate version of the song."
      },
      "alternate_version_details": {
        "type": "object",
        "properties": {
          "take_number": {
            "type": "integer",
            "description": "The take number of the alternate version included on the compilation album."
          },
          "total_takes_before_final": {
            "type": "integer",
            "description": "The total number of takes recorded before the final version was released."
          }
        },
        "required": [
          "take_number",
          "total_takes_before_final"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "original_album",
      "original_release_year",
      "is_first_solo_pop_hit",
      "compilation_album_with_alternate_version",
      "alternate_version_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
