{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Return of East Atlanta Santa: The Return of East Atlanta Santa is the tenth studio album by American rapper Gucci Mane.  It was released on December 16, 2016, exclusively to Apple Music and iTunes Store, by GUWOP Enterprises and Atlantic Records.  The record serves as Gucci Mane's third commercial release of the year, following his release from prison, after \"Everybody Looking\" (2016) and \"Woptober\" (2016).  The album features guest appearances from rappers Drake and Travis Scott, alongside American singer-songwriter Bryson Tiller, while the production was handled by Metro Boomin, Southside, Bangladesh, Zaytoven, Mike Will Made It and Murda Beatz, among others.\n\nTone It Down: \"Tone It Down\" is a song by American rapper Gucci Mane, featuring American singer Chris Brown.  It was released on June 20, 2017 as the second single from Gucci Mane's album \"Mr. Davis\" (2017).  The song was written by Mane and Brown, and produced by Cardiak and Hitmaka.\n\nMr. Davis: Mr. Davis is the eleventh studio album by American rapper Gucci Mane.  It will be released on October 13, 2017, by GUWOP Enterprises and Atlantic Records.  It is Gucci Mane's second commercial project of the year following the \"Droptopwop\" (2017) mixtape.  The album features guest appearances from Nicki Minaj, Monica, Chris Brown, Migos, The Weeknd, ASAP Rocky, Big Sean, Ty Dolla Sign, Schoolboy Q, among others.\n\nThe Return of Mr. Zone 6: The Return of Mr. Zone 6 is the eighth studio album by American rapper Gucci Mane.  It was released on March 22, 2011, by 1017 Brick Squad Records and Asylum Records.  The album features guest appearances from Birdman, Waka Flocka Flame, Master P and Rocko, while the majority of the production was provided by Drumma Boy, except for tracks that were produced by Zaytoven and Southside.\n\nGucci Time: \"Gucci Time\" is a song by American rapper Gucci Mane featuring vocals and production from Swizz Beatz.  The song premiered on Gucci Mane's official MySpace page on August 6, 2010 and was released on August 30, 2010 as the lead single from Gucci Mane's 's third studio album \"\".  The song samples French electronic music duo Justice's song \"Phantom Pt.  II\".\n\nEast Atlanta Santa: East Atlanta Santa is a mixtape by American rapper Gucci Mane.  The mixtape was released on December 25, 2014, by 1017 Records and 101 Distribution.  The album features guest appearances from Shawty Lo, Raury and OJ da Juiceman.  The album features production from DJ Spinz, Metro Boomin, Drumma Boy, Zaytoven, Doughboy Beatz, Honorable C.N.O.T.E. and members from the 808 Mafia.\n\nI Get the Bag: \"I Get the Bag\" is a song by American rapper Gucci Mane, featuring American rappers Quavo and Takeoff from the hip hop group Migos.  It was released on September 5, 2017, as the third single from Gucci Mane's album \"Mr. Davis\" (2017).\n\nEverybody Looking: Everybody Looking is the ninth studio album by American rapper Gucci Mane.  It was released on July 22, 2016, by 1017 Records and Atlantic Records.  The record serves as Gucci's first studio release since \"The Return of Mr. Zone 6\" (2011).  Recording sessions on the album took place in under six days, featuring solely three guest appearances from Drake, Kanye West and Young Thug, while the majority of production was provided by Gucci Mane's longtime collaborators such as Mike Will Made It and Zaytoven, among others.\n\nDroptopwop: Droptopwop is a collaborative commercial mixtape by American rapper Gucci Mane and record producer Metro Boomin.  It was released on May 26, 2017 by Atlantic Records and 1017 Records to celebrate Gucci Mane's one year anniversary since being released from prison.  The entire album is produced by Metro Boomin, along with extra production from Southside, London on da Track, DJ Spinz and Cubeatz.  It features guest appearances from American rappers Offset, 2 Chainz, Young Dolph and Rick Ross.\n\nThe Weeknd: Abel Makkonen Tesfaye (born February 16 1990), known professionally as The Weeknd (pronounced \"the weekend\"), is a Canadian singer, songwriter and record producer.\n\nQuestion: Mr. Davis is the eleventh studio album, by American rapper Gucci Mane, the album features guest appearances from which Canadian singer, songwriter and record producer, known professionally as who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album.\"\n    },\n    \"guest_artist\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"professional_name\": {\n          \"type\": \"string\",\n          \"description\": \"The professional name of the artist.\"\n        },\n        \"real_name\": {\n          \"type\": \"string\",\n          \"description\": \"The real name of the artist.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the artist.\"\n        },\n        \"roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The professional roles of the artist.\"\n        }\n      },\n      \"required\": [\n        \"professional_name\",\n        \"real_name\",\n        \"nationality\",\n        \"roles\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_featured_on_album\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the artist is featured on the specified album.\"\n    }\n  },\n  \"required\": [\n    \"album_name\",\n    \"guest_artist\",\n    \"is_featured_on_album\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_name": {
        "type": "string",
        "description": "The name of the album."
      },
      "guest_artist": {
        "type": "object",
        "properties": {
          "professional_name": {
            "type": "string",
            "description": "The professional name of the artist."
          },
          "real_name": {
            "type": "string",
            "description": "The real name of the artist."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the artist."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The professional roles of the artist."
          }
        },
        "required": [
          "professional_name",
          "real_name",
          "nationality",
          "roles"
        ],
        "additionalProperties": false
      },
      "is_featured_on_album": {
        "type": "boolean",
        "description": "Indicates if the artist is featured on the specified album."
      }
    },
    "required": [
      "album_name",
      "guest_artist",
      "is_featured_on_album"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
