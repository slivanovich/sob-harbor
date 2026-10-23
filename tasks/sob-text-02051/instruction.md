{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJeffrey Walker: Jeffrey Walker (born 25 March 1969) is a bass guitarist, vocalist from Windle, St Helens, UK.  He is best known for his work with death metal band Carcass for which he is also the main lyricist.  Before Carcass, he played in the hardcore punk band Electro Hippies.  After the demise of Carcass, he went on to form hard rock band Blackstar with two former Carcass bandmates.  In some territories the band was called Blackstar Rising.\n\nJeffrey Walker (actor): Jeffrey Walker (born 10 July 1982, in Melbourne) is an Australian television actor and director, best known to the Australian public for his appearances as a child actor in \"Ocean Girl\" and \"Round the Twist\".  He moved on to direct episodes of Australian soaps \"Neighbours\", \"Home and Away\", and \"\".  He is married to American born Australian actress Brooke Harman-Walker; together they have two sons, Boston Scott Walker (b. 24 June 2013) and Ace Jackson Walker (b. 24 June 2015)\n\nLiberal Animation: Liberal Animation is the debut album by the American punk rock band NOFX.  It was originally released in 1988 through Wassail Records, which was Fat Mike's label before Fat Wreck Chords.  Brett Gurewitz produced the record, and even offered to release it on his label, Epitaph Records.  The band decided to self-release it instead.  It was re-released through Epitaph Records in 1991 with all new artwork.  The title is a spoonerism of \"animal liberation\" and the cover artwork is a reflection of that.  Bassist/Singer, Fat Mike has stated many times that he thinks it's the worst NOFX album.  He wrote the majority of the album on a guitar he bought from Lynn Strait of Snot.  The track \"Shut Up Already\" borrows a riff from the Led Zeppelin song \"Black Dog\".  It is the only full length album by NOFX to feature Dave Cassilas on guitar.  Amateur style music videos were made for the tracks \"Shut Up Already\" and \"Mr. Jones.\" [1][3]\n\nCool to Be You: Cool to Be You is the sixth studio album by the American punk rock band the Descendents, released in 2004 through Fat Wreck Chords.  It was their first album of new studio material since 1996's \"Everything Sucks\", which had been released through Epitaph Records.  Following \"Everything Sucks\", singer Milo Aukerman had returned to his biochemistry career while the other members—bassist Karl Alvarez, guitarist Stephen Egerton, and drummer Bill Stevenson—had continued with their other band All, releasing two more studio albums and a live album through Epitaph between 1998 and 2001 with singer Chad Price.  \"Cool to Be You\" was recorded with Aukerman in 2002, but its release was delayed until 2004.  The band switched from Epitaph to Fat Wreck Chords partly due to the enthusiasm of label head Fat Mike, who cited the Descendents as one of his favorite bands.  \"Cool to Be You\" became the fourth Descendents release to chart, reaching #143 on the \"Billboard\" 200 and #6 amongst independent albums.\n\nFat Wreck Chords: Fat Wreck Chords (pronounced as if spelled \"Fat Records\", ) is a San Francisco, California-based independent record label, focused on punk rock.  It was started by NOFX lead singer Michael Burkett (better known as Fat Mike) and his girlfriend at the time, Erin Burkett, in 1991.\n\nPizza of Death Records: Pizza of Death is a Japanese record label based in Tokyo, Japan, and was founded by Hi-Standard front man Ken Yokoyama.  It was created in 1994 as a record label inside a record label (Fat Wreck Chords), and officially established itself as fully independent in 1999 with the release of Hi-Standard's \"Making the Road\".  The label currently holds 19 bands, 5 of which are based in The United States and Europe.  One of these is \"Me First and the Gimme Gimmes\", which is associated with several well-known American punk musicians from the United States, including producer and bassist Fat Mike of NOFX.\n\nFat Mike: Michael John Burkett (born January 31, 1967), also known as Fat Mike, is an American musician and producer.  He is the bassist and lead vocalist for the punk rock band NOFX and the bassist for the punk rock supergroup cover band Me First and the Gimme Gimmes.  He was also a temporary bassist for the band Against Me! \n\nCognicide: Cognicide is Western Addiction's first full-length album.  It was released on Fat Wreck Chords on November 1, 2005.  The album is known for featuring a sound heavily inspired by Hardcore punk acts of the 1980's.  Fat Mike has often listed Cognicide as one of the greatest releases on his label, Fat Wreck Chords, calling it one of the best hardcore albums he's ever heard.  Joey Cape of Lagwagon has also stated that it is his favorite album released on Fat Wreck Chords.\n\nPink and Black Records: Pink and Black Records is an imprint record label of Fat Wreck Chords created to distribute albums from female-fronted bands.  The first record released on this label was the Dance Hall Crashers album \"Purr\" in 1999.  Pink & Black is named for the two favorite colors of Erin Burkett, ex-wife of Fat Mike, and one of the founders of Fat Wreck Chords.\n\nApathy and Exhaustion: Apathy and Exhaustion is the third album by the Chicago, Illinois punk rock band The Lawrence Arms, released in 2002 by Fat Wreck Chords.  It was the band's first album to be released on Fat Wreck Chords, and with this release, the band formed a close relationship with the label and its founder Fat Mike, for whom they released their next two albums with.  It's also their first full length album they recorded with producer, Matt Allison, who they would go on to record all of their full length albums with.  Apathy and Exhaustion shows the band experimenting with verse/chorus structures, and infectious pop melodies.  It's often considered to be one of their finest efforts.  Fat Mike included this album on a list of the 25 best albums released on his label, Fat Wreck Chords.  An independent music video was filmed for the song \"Porno and Snuff Films.\"\n\nQuestion: Jeffrey Walker and Fat Mike, share which mutual occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the individuals mentioned in the question.\"\n    },\n    \"mutual_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The occupation shared by both individuals.\"\n    },\n    \"individual_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"occupations\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"A list of occupations for this individual.\"\n          },\n          \"primary_band\": {\n            \"type\": \"string\",\n            \"description\": \"The primary band associated with this individual's musical career.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"occupations\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Details of each individual's occupations.\"\n    }\n  },\n  \"required\": [\n    \"person_names\",\n    \"mutual_occupation\",\n    \"individual_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the individuals mentioned in the question."
      },
      "mutual_occupation": {
        "type": "string",
        "description": "The occupation shared by both individuals."
      },
      "individual_occupations": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "occupations": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of occupations for this individual."
            },
            "primary_band": {
              "type": "string",
              "description": "The primary band associated with this individual's musical career."
            }
          },
          "required": [
            "name",
            "occupations"
          ],
          "additionalProperties": false
        },
        "description": "Details of each individual's occupations."
      }
    },
    "required": [
      "person_names",
      "mutual_occupation",
      "individual_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
