{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDeath Cult Armageddon: Death Cult Armageddon is the sixth studio album by Norwegian symphonic black metal band Dimmu Borgir, released on 9 September 2003.  It has since sold over 100,000 copies in the United States; the first album under Nuclear Blast to do so; and debuted on the \"Billboard\" 200 chart at number 169.  The song \"Progenies of the Great Apocalypse\" is released as single with accompanying music video.  Parts of the album were recorded with the Prague Philharmonic Orchestra.  This would also be the last album to have Nicholas Barker on drums.  It also features guest vocals by Abbath Doom Occulta.\n\nImmortal (band): Immortal is a black metal band from Bergen, Norway, founded in 1991 by frontman and bassist Abbath Doom Occulta (Olve Eikemo) and guitarist Demonaz Doom Occulta (Harald Nævdal).  The pair worked with various drummers (including Grim, Armagedda and Hellhammer), and were later joined by current drummer Horgh (Reidar Horghagen) in 1996.\n\nIvar Bjørnson: Ivar Bjørnson (born November 27, 1977 in Etne) is a Norwegian composer/guitarist for the progressive black/viking metal band Enslaved.  He is, along with Grutle Kjellson, one of only two founding members left in the current line-up, being only 13 years old at the time of the band's formation in 1991.  Bjørnson and Grutle Kjellson performed in a death metal band called Phobia in 1989.  The two decided that they wanted to form a new band in a more black metal style, and after discovering their shared fascination with Norse mythology, this set the groundwork for Enslaved.  Beyond his duties on guitar, he writes almost all of the music for Enslaved as well as much of the lyrics.  He has said that \"When we started Enslaved we wanted to have the same level of commitment to something spiritual as our contemporaries in black metal [have with] the Satanic side.  The dark destructive part of black metal didn't seem right because we didn't have any commitment to any Satanic ideology.\"  He contributed keyboard/synth work to Borknagar's first three albums and synth/piano work on the Gorgoroth albums \"Incipit Satan\" and \"Destroyer\" under the name \"Daimonion\"; and also produced the first demo from black metal band Orcustus.\n\nAll Shall Fall: All Shall Fall is the eighth studio album by Norwegian black metal band Immortal.  The album was released in Europe on September 25, 2009, and in the US on October 6, 2009.  The only album to feature bassist Apollyon and the last to feature vocalist/guitarist Abbath Doom Occulta.\n\nSigurd Wongraven: Satyr (born Sigurd Wongraven on 28 November 1975) is the vocalist, lead and rhythm guitarist, bassist, and keyboardist for the Norwegian black metal band Satyricon.  He was a founding member of Satyricon (although the band had been around for a short length of time as Eczema without him) and have so far released eight albums, two demos, and a live DVD.  He has also contributed to other bands such as Darkthrone, Eibon, Storm, Thorns, Black Diamond Brigade and Wongraven.  About black metal, he stated \"It, black metal, doesn't necessarily have to be all satanic as long as it's dark.\"  He has recently been endorsed by ESP Guitars.\n\nMarcin Rygiel: Marcin \"Martin\" Rygiel, (born 30 April 1983 in Krosno, Poland), is a Polish musician, best known as the former bass guitarist of the technical death metal band Decapitated from 1997 to 2007, leaving several months before their hiatus.  He was also a member of the avant-garde metal/black metal band Lux Occulta from 1998 until their hiatus in 2002.  In June 2008, Rygiel toured with the death metal band Vader as a session musician.  In 2010, Rygiel joined California-based death metal band Annihilated as their bassist until 2013.  He was the bassist for the Egyptian-American death metal band Nader Sadek from 2014 to 2015.\n\nThe Seventh Date of Blashyrkh: The Seventh Date of Blashyrkh is black metal band Immortal's first live DVD.  All content is from the Wacken Open Air set they performed in 2007, as part of their comeback tour, The Seventh Date of Blashyrkh.\n\nOlve Eikemo: Olve Eikemo (born 27 June 1973), better known by his stage name Abbath Doom Occulta or simply Abbath, is a Norwegian musician best known as a founding member of the black metal band Immortal.  Before founding Immortal, Abbath performed with Old Funeral alongside future Immortal member Demonaz.  While working with Old Funeral, he also joined Demonaz's band Amputation which later became Immortal.  He also plays bass in Demonaz's eponymous project.\n\nThe Older Ones: The Older Ones is the first compilation album by Norwegian blackened death metal band Old Funeral, which was made up by key players in the Norwegian black metal scene, including bassist/vocalist Olve \"Abbath\" Eikemo (Immortal), guitarist Harald \"Demonaz\" Nævdal (Immortal) and guitarist Kristian \"Varg\" Vikernes (Burzum).  By the time this album was released, the members had already gone their separate ways, with Immortal a going concern for Abbath and Varg in jail.\n\nAbbath (band): Abbath (stylized as ABBATH) is a black metal band formed in 2015 by former Immortal guitarist and vocalist Abbath Doom Occulta after departing from Immortal earlier in 2015.  The band released their first album, \"Abbath\", on January 22, 2016, and played live for the first time at Tuska Open Air 2015.\n\nQuestion: The Seventh Date of Blashyrkh is black metal band, and which black metal band from Bergen, Norway, founded in 1991 by frontman and bassist Abbath Doom Occulta (Olve Eikemo), first live DVD?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the black metal band.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The musical genre of the band.\"\n    },\n    \"origin\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the band was founded.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the band was founded.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the band was founded.\"\n    },\n    \"founding_members\": {\n      \"type\": \"array\",\n      \"description\": \"A list of the band's founding members.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"stage_name\": {\n            \"type\": \"string\",\n            \"description\": \"The stage name of the founding member.\"\n          },\n          \"real_name\": {\n            \"type\": \"string\",\n            \"description\": \"The real name of the founding member.\"\n          },\n          \"roles\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"The roles of the founding member in the band.\"\n          }\n        },\n        \"required\": [\n          \"stage_name\",\n          \"roles\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"first_live_dvd\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the band's first live DVD.\"\n        }\n      },\n      \"required\": [\n        \"title\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"genre\",\n    \"origin\",\n    \"founding_year\",\n    \"founding_members\",\n    \"first_live_dvd\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the black metal band."
      },
      "genre": {
        "type": "string",
        "description": "The musical genre of the band."
      },
      "origin": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the band was founded."
          },
          "country": {
            "type": "string",
            "description": "The country where the band was founded."
          }
        },
        "required": [
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the band was founded."
      },
      "founding_members": {
        "type": "array",
        "description": "A list of the band's founding members.",
        "items": {
          "type": "object",
          "properties": {
            "stage_name": {
              "type": "string",
              "description": "The stage name of the founding member."
            },
            "real_name": {
              "type": "string",
              "description": "The real name of the founding member."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "The roles of the founding member in the band."
            }
          },
          "required": [
            "stage_name",
            "roles"
          ],
          "additionalProperties": false
        }
      },
      "first_live_dvd": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the band's first live DVD."
          }
        },
        "required": [
          "title"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "band_name",
      "genre",
      "origin",
      "founding_year",
      "founding_members",
      "first_live_dvd"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
