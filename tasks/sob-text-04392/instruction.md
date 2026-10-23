{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nToutes les femmes de ta vie: \"Toutes les femmes de ta vie\" (English: All the girls in your life ) is a 2001 song recorded by French band L5.  It was band's debut single released on November 26, 2001, from its first album \"L5\" on which it features as first track.  The song was also included on the band's 2004 album live \"Le live\".  It was a huge success in France where it was a number-one hit and can be considered as L5's signature song.\n\nOne (Metallica song): \"One\" is a song by American heavy metal band Metallica.  It was released as the third and final single from their fourth studio album, \"...And Justice for All\" (1988).  Written by band members James Hetfield and Lars Ulrich, \"One\" is an anti-war song that portrays a World War I soldier who is severely wounded—Arms and legs blown off from an artillery shell, blind and unable to speak or move—begging God to take his life as he feels constant pain.  His only hope is to devise a way to communicate with the hospital staff.  In the music video, he jolts in the hospital bed, spelling \"Kill me\" in Morse code.  Production of the song was done by the band alongside Flemming Rasmussen.  The song was the band's first top 40 hit single in the U.S., reaching number 35 on the \"Billboard\" Hot 100.  It was also a number-one hit in Finland.\n\nArchangel (Soulfly album): The ensuing \"We Sold Our Souls To Metal\" Tour to promote Archangel's release featured Soulfly playing as many as 7 songs from the album live each night, which is the first time since the Primitive Tour that the band has played the majority of a new album live.\n\nMajesty (album): Majesty is the seventh Christian worship music album recorded by Ron Kenoly.  For this album, Kenoly recorded the album live from Liberty University's Vines Center in Lynchburg.  This was one of two albums to be recorded there (God Is Good – Worship with Don Moen was the other), and was released in 2000 by Integrity/Hosanna!  Music.  The title of the album comes from the Jack Hayford penned song of the same name, which is used to open the album.\n\nLive (Korn DVD): Live is a double DVD live release that was recorded in the Hammerstein Ballroom at Manhattan Center Studios during their 2002 \"Untouchables\" tour.  It also features some live tracks from their self-titled album, and albums \"Life Is Peachy\", \"Follow the Leader\", and \"Issues\", as well as part of their cover of Metallica's \"One\" that was later performed for 2003 Metallica's \"MTV Icon\" special in its entirety.  The second DVD features the same show, but from alternate angles, as well as some behind-the-scenes material.  This release has been certified Gold by RIAA.  \"Live\" was directed by Jim Gable.\n\nOblivion (Mastodon song): Oblivion is the second single from \"Crack the Skye\" by American progressive metal band Mastodon.  It is their second-most successful single and song since the release of their full length Crack the Skye, reaching #30 on the Hot Mainstream Rock Tracks chart; however, it has since been surpassed by \"Curl of the Burl,\" which peaked at #16.  It is the opening track on the band's live album Live At The Aragon.\n\nLive at the Apollo: The Proclamation: Byron Cage's album Live At the Apollo: The Proclamation was recorded live at the Apollo Theater on April 26, 2007 with production by PAJAM and featured guests J Moss, Kim Burrell, & Dave Hollister.  The album was released in 2007.  \"I'm Going Back\", was done by The Prince Of Praise in his notable style.  This is also his third solo and fifth overall album.\n\nBlack Wooden Ceiling Opening: Black Wooden Ceiling Opening is an EP released by Mount Eerie.  The album was released as a 10\" record on white vinyl accompanied by a CD containing the same songs, as well as a 10-song bootleg recording of the same group of musicians featured on the album live in concert at the Department of Safety in Anacortes, WA.\n\nOne Acoustic Night: One Acoustic Night is the third album live by the German hard rock band Bonfire.  It was released in 2005 by E-M-S Music and is a two-disc album that is a live acoustic performance in Germany.  It also features a studio song dedicated to the victims of the tsunami disaster in Thailand, recorded in English, German and Spanish.  Chris Limburg and Thomas Streck were guest musicians that helped with the live performance, which is all in German.  A DVD was released at the same time of the acoustic performance.\n\nIn the Raw (song): \"In the Raw\" is a 2007 single by Swedish glam metal band Crashdïet.  This was the first single to feature the band's new lead singer H. Olliver Twisted on vocals, since their original singer Dave Lepard died in January 2006.  This song appears as the opening track on the band's 2007 album, The Unattractive Revolution.  The song debuted at #35 on the Swedish singles chart.  The song's name and chorus is based on the album Live...In the Raw by the Heavy Metal band W.A.S.P which have been a major influence on the sound of Crashdïet.\n\nQuestion: Who was the writer of the song \"One\" which was featured in the album Live?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song.\"\n    },\n    \"writers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The individuals credited as writers of the song.\"\n    },\n    \"original_artist\": {\n      \"type\": \"string\",\n      \"description\": \"The original artist who performed the song.\"\n    },\n    \"featured_on_release\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"release_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album or DVD where the song was featured.\"\n        },\n        \"release_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of release (e.g., album, DVD).\"\n        },\n        \"feature_details\": {\n          \"type\": \"string\",\n          \"description\": \"Details about how the song was featured on the release (e.g., original, cover, part of).\"\n        }\n      },\n      \"required\": [\n        \"release_title\",\n        \"release_type\",\n        \"feature_details\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"writers\",\n    \"original_artist\",\n    \"featured_on_release\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song."
      },
      "writers": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The individuals credited as writers of the song."
      },
      "original_artist": {
        "type": "string",
        "description": "The original artist who performed the song."
      },
      "featured_on_release": {
        "type": "object",
        "properties": {
          "release_title": {
            "type": "string",
            "description": "The title of the album or DVD where the song was featured."
          },
          "release_type": {
            "type": "string",
            "description": "The type of release (e.g., album, DVD)."
          },
          "feature_details": {
            "type": "string",
            "description": "Details about how the song was featured on the release (e.g., original, cover, part of)."
          }
        },
        "required": [
          "release_title",
          "release_type",
          "feature_details"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_title",
      "writers",
      "original_artist",
      "featured_on_release"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
