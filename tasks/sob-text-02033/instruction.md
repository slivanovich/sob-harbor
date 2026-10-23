{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nStorm World Tour: Storm World Tour (or simply \"Storm Tour\") was the first world tour by Finnish singer Tarja Turunen to support her second studio album, \"My Winter Storm\", released on November 19, 2007, by Universal Music; it was Tarja's first world tour since her dismissal from Nightwish in 2005, playing for the first time in several countries like Luxembourg, Serbia, Israel, Ukraine, Bulgaria and Belarus.\n\nNever Enough (Tarja song): \"Never Enough'\" is a song released by Finnish singer Tarja Turunen from her fourth studio album \"Colours in the Dark\".  The song was released on May 31, 2013 as a lyrical video-teaser song.  The track is only available as a digital version.  The song, although from the \"Colours in the Dark\" album, was previously featured on the \"\" live album, as the song was first played at the end of the \"What Lies Beneath World Tour\".\n\nWhat Lies Beneath World Tour: What Lies Beneath World Tour is the second world tour by Finnish soprano Tarja Turunen to promote her third album, \"What Lies Beneath\", released by Universal Music on September 1, 2010.\n\nMy Winter Storm: My Winter Storm is the second solo album by Finnish singer Tarja Turunen, and the first to consist mainly of new and original songs specifically written by or for Turunen.  The album was released by Universal Music on 19 November 2007 in Finland, on 2 January 2008 in South America and on February 26 in North America and in the United Kingdom was also released a special version limited in 300 copies.\n\nColours in the Dark (album): Colours in the Dark is the fourth studio album released by Finnish vocalist Tarja Turunen.  The record was released on 30 August 2013, in Austria, Brazil, Finland, Germany, Portugal, Spain, and Switzerland; 2 September in Norway, Poland, and the Czech Republic; 3 September in the United States and Canada; and 4 September in Belgium, Denmark, the Netherlands, Sweden, and the UK.  Mixing was done by Tim Palmer in Austin, Texas in the United States.  Tarja will start the Colours in the Dark World Tour on 17 October 2013, to promote the album.  The name of the album, as the cover image, came as a metaphor from the idea that life has a large range of colors and the dark absorbs all of them, containing every color.\n\nTarja Turunen: Tarja Soile Susanna Turunen-Cabuli (born 17 August 1977), known professionally as Tarja Turunen or simply Tarja, is a Finnish singer-songwriter.  She is a full lyric soprano and has a vocal range of three octaves.\n\nUnderneath (Tarja song): \"Underneath\" is the fourth single by Finnish singer Tarja Turunen from her third album \"What Lies Beneath\".  It was released on 22 April 2011 only as a digital version.  The release has been confirmed for Austria, Switzerland, Russia, Poland, Finland, Sweden, Ukraine, France and UK.  It includes two unreleased versions of the song, plus a non-album track in Spanish.  An exclusive limited edition 7 inches 2 track vinyl single was released in America on May 24, 2013.\n\nWhat Lies Beneath (Tarja album): What Lies Beneath is the third album by the Finnish singer Tarja Turunen, which was released on 1 September 2010 in Finland, on 3 September in Germany, Switzerland and Austria and on 14 September in Latin and North America.  It is the first of Tarja's albums in which she is credited for composition on every track.The album was mixed at '62 Studios in Austin Texas by Tim Palmer\n\nI Feel Immortal: \"I Feel Immortal\" is a song by Finnish singer-songwriter Tarja, featuring Canadian guitarist Jason Hook.  It was written by Tarja, Toby Gad, Kerli Kõiv, and Lindy Robbins, and was produced by Tarja and \"Mic\".  It was released as the second single from her second album \"What Lies Beneath\" on August 27, 2010.\n\nIn Concert – Live at Sibelius Hall: \"Tarja Turunen & Harus - Live at Sibelius Hall\" is a collaboration album by Finnish soprano Tarja Turunen with musicians Kalevi Kiviniemi, Marzi Nyman and Markku Khron record at the Sibelius Hall, Finland and released on 25 November 2011.\n\nQuestion: Tarja Turunen, whose third album What Lies Beneath, was released on September 1, 2010 by Universal Music, was born when?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist.\"\n    },\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album mentioned in the question.\"\n        },\n        \"release_date\": {\n          \"type\": \"string\",\n          \"description\": \"The release date of the album.\"\n        },\n        \"record_label\": {\n          \"type\": \"string\",\n          \"description\": \"The record label that released the album.\"\n        }\n      },\n      \"required\": [\n        \"album_title\",\n        \"release_date\",\n        \"record_label\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the artist.\"\n    }\n  },\n  \"required\": [\n    \"artist_name\",\n    \"album_details\",\n    \"birth_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "artist_name": {
        "type": "string",
        "description": "The name of the artist."
      },
      "album_details": {
        "type": "object",
        "properties": {
          "album_title": {
            "type": "string",
            "description": "The title of the album mentioned in the question."
          },
          "release_date": {
            "type": "string",
            "description": "The release date of the album."
          },
          "record_label": {
            "type": "string",
            "description": "The record label that released the album."
          }
        },
        "required": [
          "album_title",
          "release_date",
          "record_label"
        ],
        "additionalProperties": false
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the artist."
      }
    },
    "required": [
      "artist_name",
      "album_details",
      "birth_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
