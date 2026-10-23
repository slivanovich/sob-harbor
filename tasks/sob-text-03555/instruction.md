{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDzeko &amp; Torres: Dzeko & Torres is a Canadian production and DJ duo based in Toronto, Ontario, Canada.  Founded around 2008 by teenagers Julian Dzeko and Luis Torres, the duo has released a number of singles in conjunction with labels such as Mixmash Records, Monstercat, and Musical Freedom Records.  They released the EP \"Hey\" on Dim Mak Records in 2012, and have had airplay on radio stations including Tiesto’s \"Club Life\", Paul Oakenfold’s \"Planet Perfecto\", David Guetta's radio show \"Radio DJ Mix\", and Steve Aoki's BBC Radio 1 \"Essential Mix 2012\".\n\nPhone Down: \"Phone Down\" is a song recorded by American DJs Lost Kings and singer Emily Warren.  It was released as a single on October 7, 2016, via Disruptor Records and RCA Records.\n\nThe Funk Hunters: The Funk Hunters are a Canadian electronic music act and DJ duo based in Vancouver, British Columbia.  Composed of members Nick Middleton and Duncan Smith, The Funk Hunters are recognized on the international dance scene for their future funk sound, which is a mix of old school soul, disco, funk and classic hip hop, deeply cross-pollinated with contemporary electronic dance music.\n\nNew York City (The Chainsmokers song): \"New York City\" is a song by American DJ duo The Chainsmokers.  It features uncredited vocals from American singer Victoria Zaro.  It is the fifth, and last, single from the duo's first EP \"Bouquet EP\".  The song peaked at number 25 on the \"Billboard\" Dance/Electronic Songs chart and number 80 on the 2016 Dance/Electronic Songs year-end chart.\n\nDuck Sauce: Duck Sauce is an American–Canadian DJ duo, formed during 2009 in New York, New York.  The duo consists of American DJ Armand Van Helden and Canadian DJ A-Trak.\n\nLost Kings: Lost Kings is an American DJ duo consisting of Robert Abisi and Nick Shanholtz, based in Los Angeles.  The duo gained popularity beginning in 2014 through their official remixes for artists such as Imagine Dragons, Krewella, Halsey, Vance Joy, Echosmith, Rihanna, and Tori Kelly, and through their original EDM/progressive house music.  Managed by Disruptor Management, a joint venture at Sony Music Entertainment, they signed to Disruptor Records/RCA Records in October 2016.\n\nDzeko &amp; Torres discography: Dzeko & Torres is a Canadian DJ duo based in Toronto, Canada.  They released the EP \"Hey\" on Dim Mak Records in 2012, and have had airplay on radio stations including Tiesto's \"Club Life\", Paul Oakenfold's \"Planet Perfecto\", David Guetta's radio show \"Radio DJ Mix\", and Steve Aoki's BBC Radio 1 \"Essential Mix 2012\".\n\nSetting Fires (song): \"Setting Fires\" is a song by American DJ duo The Chainsmokers, released as a promotional single from the duo's second extended play, \"Collage\" (2016).  It features the vocal collaboration of American electronic music duo XYLØ.  The song was written by Melanie Fontana, Jon Asher and Andrew Taggart.  \"Setting Fires\" was released on November 4, 2016, through Disruptor Records and Columbia Records.\n\nQueens of Noize: Queens of Noize were a DJ duo based in London, consisting of Mairead Nash and Tabitha Denholm, during their time as a duo they presented for MTV2 and BBC 6 Music and performed at a number of international festivals.\n\nRiley &amp; Durrant: Riley & Durrant are an electronic music production and DJ duo based in Leeds, UK.\n\nQuestion: Phone Down was a song recorded by an American DJ duo based out of where?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"recording_artists\": {\n      \"type\": \"array\",\n      \"description\": \"A list of artists who recorded the song.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"dj_duo_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the DJ duo involved in recording the song.\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the DJ duo.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the DJ duo.\"\n        },\n        \"base_location\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the DJ duo is based.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"base_location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"recording_artists\",\n    \"dj_duo_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "recording_artists": {
        "type": "array",
        "description": "A list of artists who recorded the song.",
        "items": {
          "type": "string"
        }
      },
      "dj_duo_details": {
        "type": "object",
        "description": "Details about the DJ duo involved in recording the song.",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the DJ duo."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the DJ duo."
          },
          "base_location": {
            "type": "string",
            "description": "The city where the DJ duo is based."
          }
        },
        "required": [
          "name",
          "nationality",
          "base_location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "recording_artists",
      "dj_duo_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
