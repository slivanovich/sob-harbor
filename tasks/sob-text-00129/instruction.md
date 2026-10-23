{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Band Geek Mafia: The Band Geek Mafia is Voodoo Glow Skulls' fourth full-length album.  It was released on July 14, 1998 on Epitaph Records.  All songs were written by Voodoo Glow Skulls except \"Stranded in the Jungle\", written by James Johnson and Ernestine Smith.  The song \"Stranded in the Jungle\" appears on punk compilation album \"Punk-O-Rama 5\", \"They Always Come Back\" appears on \"Punk-O-Rama 4\", and \"Delinquent Song\" appears on Punk-O-Rama 3.  The song \"Symptomatic\" was in ESPN X Games \"Pro Boarder\" for the PS1.\n\nRasta Mis Huevos: Rasta Mis Huevos is the second EP from Californian ska punk band Voodoo Glow Skulls.  It was released in 1992 through Signal Sound Systems Records as a 7\" vinyl EP, including a limited edition pressing of 1,000 on white vinyl and 500 on red vinyl that were sold in Japan only.  The sleeve credits \"Greg McDeath\" as Executive Producer.\n\nAdicción, Tradición, Revolución: Adicción, Tradición, Revolución is the Voodoo Glow Skulls' seventh full-length album.  It was released on November 2, 2004 on Victory Records.  The song \"Used to Love Her\" is a cover song of the original by Guns N' Roses.\n\nSymbolic (Voodoo Glow Skulls album): Symbolic is the Voodoo Glow Skulls' fifth full-length album.  It was released on September 12, 2000 on Epitaph Records.  This album marks the last appearance of the creator of the VGS horn style, Helios J Hernandez.  Track 14 is a cover of the song \"I Shot the Sheriff\" from Bob Marley.  The song \"Say Goodnight\" appears on punk compilation album \"Punk-O-Rama 6\".\n\nWe're Coloring Fun: We're Coloring Fun is the third EP from Californian ska punk band Voodoo Glow Skulls.  Released in 1993 on Signal Sound Systems Records, it contains songs from their 1989 demo tape plus tracks previously featured on various compilations.\n\nVoodoo Glow Skulls: Voodoo Glow Skulls is an American ska punk band formed in 1988 in Riverside, California by brothers Frank, Eddie, and Jorge Casillas and their longtime friend Jerry O'Neill.  Voodoo Glow Skulls first played at backyard parties and later at Spanky's Café in their hometown of Riverside, where they played shows with the Angry Samoans, The Mighty Mighty Bosstones, Firehose, Murphy's Law, and The Dickies.\n\nThe Old of Tomorrow: The Old of Tomorrow is the debut EP from Californian ska punk band Voodoo Glow Skulls.  It was released in 1990 on 7\" vinyl through Goon Records.  It was produced by Voodoo Glow Skulls with the help of local band Public Humiliation.\n\nFirme: Firme is the second studio album by Voodoo Glow Skulls.  Released on October 10, 1995, it is the band's first release on Epitaph Records.  \"Firme\" is Chicano slang meaning \"cool\" or \"hot\".  All the songs were written by Voodoo Glow Skulls, except \"Charlie Brown\" which is a traditional song played by The Coasters.\n\nSouthern California Street Music: Southern California Street Music is Voodoo Glow Skulls' eighth full-length album released on September 18, 2007 on Victory Records (VR 348).  This album, unlike most of the band's other albums, doesn't contain any cover songs.  All the songs are written by Voodoo Glow Skulls.\n\nI Shot the Sheriff: \"I Shot the Sheriff\" is a song written by Bob Marley and released in 1973 by The Wailers.\n\nQuestion: What song on the fifth full-length album of the band Voodoo Glow Skulls was originally released in 1973 by The Wailers?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the Voodoo Glow Skulls album.\"\n        },\n        \"album_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The sequential number of the full-length album.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the album was released.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"album_number\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"song_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song.\"\n        },\n        \"original_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist who originally released the song.\"\n        },\n        \"original_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the original song was released.\"\n        }\n      },\n      \"required\": [\n        \"song_title\",\n        \"original_artist\",\n        \"original_release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_cover_song\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the song on the album is a cover version.\"\n    }\n  },\n  \"required\": [\n    \"album_details\",\n    \"song_details\",\n    \"is_cover_song\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the Voodoo Glow Skulls album."
          },
          "album_number": {
            "type": "integer",
            "description": "The sequential number of the full-length album."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the album was released."
          }
        },
        "required": [
          "album_title",
          "album_number",
          "release_year"
        ],
        "additionalProperties": false
      },
      "song_details": {
        "type": "object",
        "properties": {
          "song_title": {
            "type": "string",
            "description": "The title of the song."
          },
          "original_artist": {
            "type": "string",
            "description": "The artist who originally released the song."
          },
          "original_release_year": {
            "type": "integer",
            "description": "The year the original song was released."
          }
        },
        "required": [
          "song_title",
          "original_artist",
          "original_release_year"
        ],
        "additionalProperties": false
      },
      "is_cover_song": {
        "type": "boolean",
        "description": "Indicates if the song on the album is a cover version."
      }
    },
    "required": [
      "album_details",
      "song_details",
      "is_cover_song"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
