{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlessandra Negrini: Alessandra Vidal de Negreiros Negrini (born 29 August 1970) is a Brazilian actress.  She is renowned internationally for her roles in Brazilian telenovelas and films.  She began her television career after starring in \"Olho no Olho\" (1993) playing the role of Clara.  In film, her first role was Lília in the \"Four Days in September\" movie.  This opened up gates for her as she has starred in over a dozen telenovelas and in television series since then.  In telenovelas she is known for her roles in \"Desejos de Mulher\" (2002), \"Paraíso Tropical\" (2007), \"Lado a Lado\" (2012), \"Boogie Oogie\" (2014).\n\nBoogie Oogie Oogie: \"Boogie Oogie Oogie\" is a song by American R&B band A Taste of Honey from their 1978 self-titled debut album.  Released as their debut single in the summer of 1978, the song became an extremely popular \"crossover\" disco song.  The lyrics urge listeners to \"boogie oogie oogie till you just can't boogie no more\".\n\nMashed (album): Mashed is a compilation album released on EMI on 12 February 2007.  It is one of the first fully legal mashup albums.  Giles Harris was responsible for the album's concept, track listing, title as well as the laborious work involved in clearing each piece of music that featured on the album.  Most of the tracks were produced by Mark Vidler aka Go Home Productions.  \"Boogie Oogie Music\" and \"Horny as a Dandy\" were produced by Loo and Placido.\n\nThe Nightmare Before Christmas: Oogie's Revenge: The Nightmare Before Christmas: Oogie's Revenge (ナイトメアービフォアクリスマス ブギーの逆襲 , Naitomeā Bifoa Kurisumasu: Bugī no Gyakushū , \"Nightmare Before Christmas: Boogie's Revenge) is a video game for the PlayStation 2 and Xbox platforms.  The Xbox version is not compatible with Xbox 360.  It is set after the events of the 1993 American stop motion musical fantasy film \"The Nightmare Before Christmas\".  A GameCube version was planned, but was cancelled.\n\nA Taste of Honey (album): A Taste of Honey is the debut album by the American rhythm and blues group A Taste of Honey.  It was produced by Fonce Mizell & Larry Mizell for Sky High Productions and included the number one pop, soul and disco classic \"Boogie Oogie Oogie\".\n\nSete Vidas: Sete Vidas (Literally English: Seven Lives, International title: English: Parts of Me ) is a Brazilian telenovela produced and broadcast by Rede Globo from March 9 to July 10, 2015 replacing \"Boogie Oogie\".\n\nKen Page: Ken Page (born January 20, 1954) is an American cabaret singer, actor and voice actor from St. Louis, Missouri.  Page is best known as the voice of \"Oogie Boogie\", the main antagonist of Tim Burton's \"The Nightmare Before Christmas\", creating the eponymous role of \"Ken\" in the original Broadway production of \"Ain't Misbehavin'\" and playing the role of \"Old Deuteronomy\" in both the original Broadway and filmed stage productions of \"Cats, the Musical.\n\nDrowning on Dry Land/Fish Soup: \"Drowning on Dry Land/Fish Soup\" is the second track from Manfred Mann's Earth Band's 1978 album \"Watch\" and is a medley of two songs.  The first song \"Drowning on Dry Land\" is a slow-paced pop rock song that follows on the heels of an acoustic guitar/vocal intro.  \"Fish soup\" cuts in with a clever instrumental break and, leading up to the reprise of \"Drowning on dry land\", a lengthy guitar solo performed by Dave Flett.  The first section was deleted on the single release, and the title was changed to Bouillabaisse, which is French for \"Fish Soup\".  The instrumental part of the track, \"Fish Soup\", bears a resemblance to A Taste of Honey's \"Boogie Oogie Oogie\" given that it has the same funky disco beat and bass line.\n\nA Taste of Honey (band): A Taste of Honey was an American recording act, formed in 1971 by associates Janice–Marie Johnson and Perry Kibble.  In 1978, they had one of the best known chart-toppers of the disco era, \"Boogie Oogie Oogie\".  After their popularity waned during the 1980s, Johnson went on to record as a solo artist and released the album \"One Taste of Honey\" which produced numerous minor hits.  In 2004, singers Hazel Payne (guitar) and Janice–Marie Johnson (bass) reunited for the first time in over 20 years to perform on the PBS specials \"\" and \"My Music: Funky Soul Superstars\".\n\nThe Nightmare Before Christmas: The Nightmare Before Christmas (also known as Tim Burton's The Nightmare Before Christmas) is a 1993 American stop-motion animated musical dark fantasy film directed by Henry Selick, and produced and conceived by Tim Burton.  It tells the story of Jack Skellington, a resident from \"Halloween Town\" who stumbles through a portal to \"Christmas Town\" and decides to celebrate the holiday, with some dastardly and comical consequences.  Danny Elfman wrote the songs and score, and provided the singing voice of Jack.  The principal voice cast also includes Chris Sarandon, Catherine O'Hara, William Hickey, Ken Page, Paul Reubens and Glenn Shadix.\n\nQuestion: Which voice artist from The Nightmare Before Christmas voiced \"Oogie Boogie\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"voice_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the voice actor.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the voice actor.\"\n        },\n        \"origin\": {\n          \"type\": \"string\",\n          \"description\": \"The city and state of origin for the voice actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\",\n        \"origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"character_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character voiced.\"\n        },\n        \"is_main_antagonist\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the character is the main antagonist.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"is_main_antagonist\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    }\n  },\n  \"required\": [\n    \"voice_actor\",\n    \"character_details\",\n    \"film_title\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "voice_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the voice actor."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the voice actor."
          },
          "origin": {
            "type": "string",
            "description": "The city and state of origin for the voice actor."
          }
        },
        "required": [
          "name",
          "birth_date",
          "origin"
        ],
        "additionalProperties": false
      },
      "character_details": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character voiced."
          },
          "is_main_antagonist": {
            "type": "boolean",
            "description": "Indicates if the character is the main antagonist."
          }
        },
        "required": [
          "character_name",
          "is_main_antagonist"
        ],
        "additionalProperties": false
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      }
    },
    "required": [
      "voice_actor",
      "character_details",
      "film_title"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
