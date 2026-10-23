{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLucio Dalla (1978 album): Lucio Dalla (1978) is an album by the Italian singer-songwriter Lucio Dalla.\n\n17 Songs (Maria Farantouri album): 17 Songs is a 1990 album by Maria Farantouri.  The album includes 17 songs on the album in Greek, Portuguese, Spanish, including covers of Caruso (song) by Leo Brouwer and Once Upon a Summertime.  The album also includes 3 songs from 1989-1990 collaboration with Vangelis, to Greek lyrics by Michalis Bourboulis.\n\nCom'è profondo il mare: Come è profondo il mare is an album by Italian singer-songwriter Lucio Dalla, released in 1977 by RCA Italiana.  It was the first work in which Dalla wrote both the music and lyrics, after three albums in which the latter had been provided by poet Roberto Roversi.\n\nBienvenue chez moi: Bienvenue chez moi is a 1995 album recorded by French singer Florent Pagny.  It can be considered a compilation because it contains the singer's previous hit singles, plus some new songs.  It was his fourth album overall and was released on September 26, 1995.  It achieved huge success in France and Belgium (Wallonia), where it remained charted respectively for 81 and 73 weeks, including several weeks atop.  There are three duets on this album : \"I Don't Know\", with Noa, \"Jamais\", with Johnny Hallyday and \"Oh Happy Day\", with La Chorale des Cherubins de Sarcelles.  The cover version of Lucio Dalla's song, \"Caruso\", was released as single and became a success (#2 in France, #3 in Belgium).\n\nCaruso (song): \"Caruso\" is a song written by Italian singer-songwriter Lucio Dalla in 1986.  It is dedicated to Enrico Caruso, an Italian tenor.  Following Lucio Dalla's death, the song entered the Italian Singles Chart, peaking at number two for two consecutive weeks.  The single was also certified platinum by the Federation of the Italian Music Industry.\n\nAutomobili: Automobili is an album by Italian singer-songwriter Lucio Dalla, released in 1976 by RCA Italiana.  It was the last work in collaboration with poet Roberto Roversi: the following LP, \"Com'è profondo il mare\", was entirely (not only the music) written by Dalla.\n\nSpaccacuore: \"Spaccacuore\" is a song written by Italian singer-songwriters Samuele Bersani and Lucio Dalla, together with Giuseppe D'Onghia.  The song was recorded by Bersani for his 1995's second studio set \"Freak\", and it was released as the album's second single in 1995.  The song later became one of his best-known songs in Italy.\n\nTutta la vita: \"Tutta la Vita\" (\"All Life Long\") is a song written and first performed by Italian singer-songwriter Lucio Dalla.  It was released in 1984 as the first single from his studio album \"Viaggi Organizzati\", produced by Mauro Malavasi.  This song is about a man searching for freedom all his life, trying not to fall in love, only to have a good time.  For the Spanish-language market, two cover versions were released, and both peaked at number-one in the \"Billboard\" Hot Latin Tracks chart, the first by Cuban singer Franco and another by Mexican performer Emmanuel, spending three weeks each at the top position, being the first time (and only) in the Hot Latin Tracks chart history that two versions of the same song succeeded one another at the top.  To date, it is uncertain who released the first cover version of the single.\n\nAthens Concert: Athens Concert is a live album by jazz saxophonist Charles Lloyd and the Greek singer Maria Farantouri.  Recorded in 2010 by the Charles Lloyd Quartet with Maria Farantouri and released on the ECM label.\n\nIskra Menarini: Iskra Menarini (San Felice sul Panaro, 5 May 1946) is an Italian singer, known for video and vocal interpretation of The Big Bad Wolf, single from the album Change of Lucio Dalla 1990, and participation in the Sanremo Festival 2009 with the song Quasi amore.\n\nQuestion: What is the name of the song that was written by Lucio Dalla and was covered on Maria Farantouri's album titled 17 Songs?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"original_writer\": {\n      \"type\": \"string\",\n      \"description\": \"The original writer of the song.\"\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album where the song was covered.\"\n        },\n        \"album_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist of the album.\"\n        },\n        \"cover_version_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist who performed the cover version on the album.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"album_artist\",\n        \"cover_version_artist\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"original_writer\",\n    \"album_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "original_writer": {
        "type": "string",
        "description": "The original writer of the song."
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album where the song was covered."
          },
          "album_artist": {
            "type": "string",
            "description": "The artist of the album."
          },
          "cover_version_artist": {
            "type": "string",
            "description": "The artist who performed the cover version on the album."
          }
        },
        "required": [
          "album_title",
          "album_artist",
          "cover_version_artist"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "original_writer",
      "album_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
