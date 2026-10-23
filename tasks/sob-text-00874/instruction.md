{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCloud Nine (Kygo album): Cloud Nine (Cloud IX) is the debut studio album by Norwegian DJ and record producer Kygo and features the likes of Maty Noyes, Conrad, Parson James, Tom Odell, Foxes, Matt Corby, RHODES, Will Heard, Julia Michaels, James Vincent McMorrow, Kodaline, Labrinth, John Legend and Angus & Julia Stone.  It was released on 13 May 2016 by Sony Music and Ultra Music.\n\nCloud Nine (George Harrison album): Cloud Nine is the eleventh studio album by English musician George Harrison.  The album was recorded and released in 1987 after Harrison had taken a five-year hiatus from his career as a solo artist.  The hit single \"Got My Mind Set on You\" from this album re-established Harrison as a critically acclaimed and commercially significant recording artist.  \"Cloud Nine\" was the last studio solo album of Harrison's released during his lifetime.\n\nFragile (Kygo and Labrinth song): \"Fragile\" is a 2016 song by Norwegian DJ and record producer Kygo and British singer Labrinth.  It was released as the first promotional single from Kygo's debut studio album, \"Cloud Nine\".\n\nTrust Nobody: \"Trust Nobody\" is a song by Norwegian DJ and record producer Cashmere Cat, featuring vocals by American singer Selena Gomez and Canadian rapper Tory Lanez.  It was released on September 30, 2016, as the second single from Cashmere's debut studio album, \"9\" (2017).  The track was written by Cashmere Cat, Gomez, Lanez, Benny Blanco, Frank Dukes and Starrah.  It was produced by Cashmere Cat, Benny Blanco and Frank Dukes.\n\nIt's Album Time: It's Album Time is the debut studio album by Norwegian DJ and record producer Todd Terje, released on 8 April 2014 by Olsen Records.  The album was self-produced by Terje and was recorded in a span of three years.  It was met with generally positive reviews from music critics upon release.  The album debuted at number 2 in Terje's home country of Norway, number 4 on the \"Billboard\" Dance/Electronic Albums chart, number 23 on the UK Albums Chart, and number 6 on the UK Dance Albums chart.\n\nCarry Me (song): \"Carry Me\" is a 2016 song by Norwegian DJ and record producer Kygo from his debut studio album, \"Cloud Nine\".  It was released as the sixth single from the album on 12 August 2016.  The song features American singer Julia Michaels.  The song was performed in the 2016 Summer Olympics closing ceremony in the Maracanã Stadium on 21 August 2016.\n\n9 (Cashmere Cat album): 9 (originally announced under the working title Wild Love) is the debut studio album by Norwegian DJ and record producer Cashmere Cat, released on 28 April 2017 through Interscope and Mad Love.\n\nStay (Kygo song): \"Stay\" is a song by Norwegian DJ and record producer Kygo, featuring American singer Maty Noyes.  The song was produced by Kygo with fellow Norwegian, William Wiik Larsen, who also wrote it with Noyes.  It was released as the fourth single from Kygo's debut studio album, \"Cloud Nine\" (2016).  An official music video for the song was released on 18 February 2016.\n\nRaging (song): \"Raging\" is a 2016 song by Norwegian DJ and record producer Kygo from his debut studio album, \"Cloud Nine\".  It was released as the second promotional single from the album on 1 April 2016, becoming later the fifth single from the album.  The song features Irish rock band Kodaline.  \"Raging\" also includes writing credits from James Bay.\n\nEn gang til (song): \"En gang til\" is a single from Norwegian DJ and electronic music duo Broiler and Norwegian band Sirkus Eliassen.  It was released in Norway on 20 June 2013 for digital download.  The song peaked at number 8 on the Norwegian Singles Chart.  The song is included on Broiler's debut studio album \"The Beginning\" (2013).\n\nQuestion: Both the single \"Stay\" and the debut studio album \"Cloud Nine\" were developed by which Norwegian DJ and record producer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Norwegian DJ and record producer.\"\n    },\n    \"artist_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the artist.\"\n    },\n    \"artist_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Roles of the artist, such as DJ or record producer.\"\n    },\n    \"associated_album\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the associated album.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the album (e.g., debut studio album).\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"associated_single\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the associated single.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the single (e.g., single).\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"artist_nationality\",\n    \"artist_roles\",\n    \"associated_album\",\n    \"associated_single\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the Norwegian DJ and record producer."
      },
      "artist_nationality": {
        "type": "string",
        "description": "The nationality of the artist."
      },
      "artist_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Roles of the artist, such as DJ or record producer."
      },
      "associated_album": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the associated album."
          },
          "type": {
            "type": "string",
            "description": "The type of the album (e.g., debut studio album)."
          }
        },
        "required": [
          "title",
          "type"
        ],
        "additionalProperties": false
      },
      "associated_single": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the associated single."
          },
          "type": {
            "type": "string",
            "description": "The type of the single (e.g., single)."
          }
        },
        "required": [
          "title",
          "type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "artist_name",
      "artist_nationality",
      "artist_roles",
      "associated_album",
      "associated_single"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
