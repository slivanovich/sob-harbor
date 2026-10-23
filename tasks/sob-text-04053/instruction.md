{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWorld Tour 1980: WORLD TOUR 1980 is a live album by Yellow Magic Orchestra.  It was recorded during the band's 1980 international tour (their second after the 1979 Trans Atlantic Tour).  This is the only YMO live album to include songs originally released on \"X∞Multiplies\"; it also features six songs from YMO members made for other projects and two covers.  It was released, with a book with photographs taken during the tour, as both a 2-CD set and a 3-LP set (with 3-5 songs spread over 5 sides), which had a bonus track.  \"Jiseiki Hirake Kokoro\" was originally made for a Fujifilm cassette commercial.  It was included in Snakeman Show's self-titled album in mono so that the lyrics, which reference Fujifilm cassettes, could not be understood properly; it was presented here in stereo, and was included in the \"\" compilation.\n\nIntimacy (Bloc Party album): Intimacy is the third studio album by British indie rock band Bloc Party.  It was recorded in two weeks at several locations in London and Kent during 2008 and was produced by Jacknife Lee and Paul Epworth.  Inspired by the release options available in the Internet age, the band members made the album available for purchase on their website as a digital download on 21 August 2008.  Minimal promotion was undertaken in the UK.  The record was released in compact disc form on 24 October 2008, with Wichita Recordings as the primary label.  It peaked at number 8 on the UK Albums Chart and entered the \"Billboard\" 200 in the United States at number 18.\n\nShut Your Eyes: \"Shut Your Eyes\" is a song by the Northern Irish-Scottish band Snow Patrol.  Initially a track on their 2006 album \"Eyes Open\", it was released as a single in several countries in 2007.\n\nIn the End (Snow Patrol song): \"In the End\" is a song by Northern Irish-Scottish alternative rock group Snow Patrol.  The track is the fourth single from the band's sixth studio album, \"Fallen Empires\", it was released as a digital download on 13 February 2012.\n\nSnow Patrol: Snow Patrol are a Northern Irish-Scottish rock band formed in 1993, consisting of Gary Lightbody (vocals, guitar), Nathan Connolly (guitar, backing vocals), Paul Wilson (bass guitar, backing vocals), Jonny Quinn (drums), and Johnny McDaid (piano, guitar, backing vocals).  Initially an indie rock band, the band rose to prominence in the early-mid 2000s as part of the post-Britpop movement.\n\nBloodstream (song): \"Bloodstream\" is a song recorded by English singer-songwriter, Ed Sheeran for his second studio album, \"×\" (2014).  It was written by Sheeran, Rudimental, and Snow Patrol members – Johnny McDaid and Gary Lightbody.  Production was handled by Rick Rubin.\n\nA Drug Against War: \"A Drug Against War\" is a song by industrial rock band KMFDM, taken from their 1993 album \"Angst\".  It was released as a single prior to the album.  A music video, featuring animated depictions of the band's previous album covers and singles, was made for the single, and was subsequently shown on the MTV cartoon \"Beavis and Butt-head\" on July 11, 1994.  It was re-released as a 7\" in 2009.  The song was featured in the video game \"Brütal Legend\" and, on December 16, 2010, it was made available as a downloadable song for the game \"Rock Band\".  In late 2011, the band released a new version of the song called \"A Drug Against Wall Street\", with lyrics in support of the Occupy Wall Street movement, and made it available for free download from their site.\n\nEyes Open (album): Eyes Open is the fourth studio album by Northern Irish-Scottish alternative rock band Snow Patrol.  Produced by Jacknife Lee, it was released in the UK on 1 May 2006, and 9 May 2006 in the US.  It was the band's first album without bassist Mark McClelland and the first to feature bassist Paul Wilson and keyboardist Tom Simpson.  Recording for the album took place between October and December 2005 at Grouse Lodge Studios in Ireland, The Garage in Kent, and The Garden and Angel Studios, both in London.\n\nThis Isn't Everything You Are: \"This Isn't Everything You Are\" is a song by Northern Irish-Scottish alternative rock group Snow Patrol.  The track is the second single from the band's sixth studio album, \"Fallen Empires\", it was released as a digital download on 14 October 2011.\n\nGary Lightbody: Gary Lightbody (born 15 June 1976) is a Northern Irish singer, songwriter, guitarist and multi-instrumentalist, best known as the lead singer and rhythm guitarist of the Northern Irish-Scottish rock band Snow Patrol.\n\nQuestion: What 2 Northern Irish-Scottish rock band members made a song called \"Bloodstream\" in 2014?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the song was released or featured on an album.\"\n    },\n    \"band_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band.\"\n        },\n        \"origin\": {\n          \"type\": \"string\",\n          \"description\": \"The origin of the band (e.g., Northern Irish-Scottish).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"origin\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"band_members_who_wrote_song\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Names of the band members who wrote the song.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"release_year\",\n    \"band_info\",\n    \"band_members_who_wrote_song\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the song was released or featured on an album."
      },
      "band_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the band."
          },
          "origin": {
            "type": "string",
            "description": "The origin of the band (e.g., Northern Irish-Scottish)."
          }
        },
        "required": [
          "name",
          "origin"
        ],
        "additionalProperties": false
      },
      "band_members_who_wrote_song": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Names of the band members who wrote the song."
      }
    },
    "required": [
      "song_title",
      "release_year",
      "band_info",
      "band_members_who_wrote_song"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
