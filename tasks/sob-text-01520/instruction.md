{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSpellbinder (album): Spellbinder is an album by Hungarian guitarist Gábor Szabó featuring performances recorded in 1966 for the Impulse!  label.  The album contains \"Gypsy Queen\" which was covered together with Fleetwood Mac's \"Black Magic Woman\" by Santana on his 1970 \"Abraxas\" album.\n\nThe Best of Peter Green's Fleetwood Mac: The Best of Peter Green's Fleetwood Mac is a compilation album by British blues rock band Fleetwood Mac focussing on the Peter Green years.  Only two tracks do not feature Green; \"Dragonfly\" was recorded by Fleetwood Mac after Green left, and \"I'd Rather Go Blind\" is not by Fleetwood Mac but is a recording by Chicken Shack featuring future Fleetwood Mac member Christine McVie.  The album serves as a digitally remastered replacement for the band's \"Greatest Hits\", with the remastering and cover art taken from the 1999 box set \"The Complete Blue Horizon Sessions 1967–1969\".\n\nBlack Magic Woman: \"Black Magic Woman\" is a song written by Peter Green that first appeared as a Fleetwood Mac single in various countries in 1968, subsequently appearing on the 1969 Fleetwood Mac compilation albums \"English Rose\" (US) and \"The Pious Bird of Good Omen\" (UK), as well as \"Vintage Years\".  In 1970, it became a hit by Santana, as sung by Gregg Rolie, reaching No. 4 in the U.S. and Canadian charts, after appearing on their \"Abraxas\" album.  In 2005 the song was covered by ex-Thin Lizzy guitarist Snowy White on his album \"The Way It Is\".  In 1996, the song was also covered by Gary Hoey on his album \"Bug Alley\".\n\nTime (Fleetwood Mac album): Time is the 16th studio album by British-American rock band Fleetwood Mac, released in 1995.  This album features a unique line-up for the band featuring the addition of former Traffic guitarist Dave Mason and country vocalist Bekka Bramlett (daughter of Delaney and Bonnie).  Lindsey Buckingham, who had left Fleetwood Mac in 1987, makes an appearance as a backing vocalist on one track, but \"Time\" is the first and only Fleetwood Mac album since 1974's \"Heroes Are Hard to Find\" not to feature any contribution from Stevie Nicks.  The album also featured drummer Mick Fleetwood's first lead vocal on the seven-minute \"These Strange Times\", produced by Duran Duran producer John Jones, and written with Beach Boys co-writer Ray Kennedy.  The band did not tour following the album's release in October 1995, but had (without Christine McVie) toured from July to December 1994, and again from April to September 1995.\n\nFleetwood Mac (1975 album): Fleetwood Mac is the tenth studio album by British-American rock band Fleetwood Mac, released in July 1975 by Reprise Records.  It was the band's second eponymous album; the first was their 1968 debut album.  Among Fleetwood Mac fans, the album is often referred to as the White Album.  This is the first Fleetwood Mac album to feature Lindsey Buckingham as guitarist and Stevie Nicks as vocalist, after Bob Welch departed the band in late 1974.  The album was also the band's last to be released on the Reprise label until 1997's \"The Dance\" (the band's subsequent albums until then were released through Warner Bros.  Records, Reprise's parent company).\n\nFuture Games: Future Games is the fifth studio album by British-American rock band Fleetwood Mac, released on 3 September 1971.  It was their first album to feature Christine McVie as a full member.  This album was also the first of five albums to feature American guitarist Bob Welch .  “He was totally different background – R&B, sort of jazzy.  He brought his personality,” Mick Fleetwood said of Welch in a 1995 BBC interview.  “He was a member of Fleetwood Mac before we’d even played a note.”\n\nShape Shifter (album): Shape Shifter is the twenty-first studio album (thirty-sixth album overall) by Santana.  It was released on May 14, 2012.  This album is the first from his new record label Starfaith Records, which is distributed by Sony Music Entertainment, owners of most of Santana's albums (except those recorded for Polydor Records which are owned by Universal Music Group).  It is also the first album since 1992's \"Milagro\" that does not feature guest singers in any of the songs, a style that characterized Santana's albums since \"Supernatural\".  The album contains only one song with vocals (\"Eres La Luz\").  The track \"Mr. Szabo\" is a homage to the Hungarian guitarist Gábor Szabó, who released a series of 8 albums for Impulse Records between 1966 and 1967, and one of Carlos Santana's early idols, and features a similar rhythmical and harmonic structure to \"Gypsy Queen\", a Szabó hit from 1966 covered by Santana in 1970 as a medley with Fleetwood Mac's \"Black Magic Woman\".\n\nSay You Will (album): Say You Will is the seventeenth studio album by British-American rock band Fleetwood Mac, released on 15 April 2003.  It was the first Fleetwood Mac album since \"Kiln House\" in 1970 that did not include tracks written by vocalist/keyboardist Christine McVie, who had left the band in 1998.  It was however the band's first studio album since \"Time\" was released in 1995.  Members Lindsey Buckingham, Stevie Nicks and John McVie shared keyboard duties for the album, though Christine McVie is featured on two songs which had been originally recorded for an unreleased Lindsey Buckingham solo album (tracks 13 and 14).  It also marks the first album in 16 years to feature Buckingham as a full time member.\n\nBlack Magic Woman (album): Black Magic Woman is a compilation album by British blues rock band Fleetwood Mac, released in 1971.  It is a double album, composed of songs from two Peter Green-era albums, \"Peter Green's Fleetwood Mac\" and \"English Rose\", as well as several non-album tracks.\n\nFleetwood Mac: Fleetwood Mac are a British-American rock band, formed in London in 1967.  The band have sold more than 100 million records worldwide, making them one of the world's best-selling bands of all time.  In 1998, selected members of Fleetwood Mac were inducted into the Rock and Roll Hall of Fame, and received the Brit Award for Outstanding Contribution to Music.\n\nQuestion: Shape Shifter is the twenty-first studio album (thirty-sixth album overall) by who, \"Gypsy Queen\", a Szabó hit from 1966 covered by Santana in 1970 as a medley with Fleetwood Mac's \"Black Magic Woman\", Fleetwood Mac are a British-American rock band, formed in London in 1967?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the album.\"\n        },\n        \"artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist who released the album.\"\n        },\n        \"studio_album_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The sequential number of the album as a studio album.\"\n        },\n        \"overall_album_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The sequential number of the album overall.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"artist\",\n        \"studio_album_number\",\n        \"overall_album_number\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"related_music_info\": {\n      \"type\": \"array\",\n      \"description\": \"Information about songs related to the album or artists mentioned.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"song_title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the song.\"\n          },\n          \"original_artist\": {\n            \"type\": \"string\",\n            \"description\": \"The original artist of the song.\"\n          },\n          \"original_release_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the song was originally released.\"\n          },\n          \"covered_by\": {\n            \"type\": \"string\",\n            \"description\": \"The artist who covered the song.\"\n          },\n          \"cover_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year the song was covered.\"\n          },\n          \"medley_partner_song\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the song it was covered in a medley with.\"\n          }\n        },\n        \"required\": [\n          \"song_title\",\n          \"original_artist\",\n          \"original_release_year\",\n          \"covered_by\",\n          \"cover_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"band_formation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band.\"\n        },\n        \"formation_location\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the band was formed.\"\n        },\n        \"formation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the band was formed.\"\n        },\n        \"band_type\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the band's origin and genre.\"\n        }\n      },\n      \"required\": [\n        \"band_name\",\n        \"formation_location\",\n        \"formation_year\",\n        \"band_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_details\",\n    \"related_music_info\",\n    \"band_formation_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the album."
          },
          "artist": {
            "type": "string",
            "description": "The artist who released the album."
          },
          "studio_album_number": {
            "type": "integer",
            "description": "The sequential number of the album as a studio album."
          },
          "overall_album_number": {
            "type": "integer",
            "description": "The sequential number of the album overall."
          }
        },
        "required": [
          "title",
          "artist",
          "studio_album_number",
          "overall_album_number"
        ],
        "additionalProperties": false
      },
      "related_music_info": {
        "type": "array",
        "description": "Information about songs related to the album or artists mentioned.",
        "items": {
          "type": "object",
          "properties": {
            "song_title": {
              "type": "string",
              "description": "The title of the song."
            },
            "original_artist": {
              "type": "string",
              "description": "The original artist of the song."
            },
            "original_release_year": {
              "type": "integer",
              "description": "The year the song was originally released."
            },
            "covered_by": {
              "type": "string",
              "description": "The artist who covered the song."
            },
            "cover_year": {
              "type": "integer",
              "description": "The year the song was covered."
            },
            "medley_partner_song": {
              "type": "string",
              "description": "The title of the song it was covered in a medley with."
            }
          },
          "required": [
            "song_title",
            "original_artist",
            "original_release_year",
            "covered_by",
            "cover_year"
          ],
          "additionalProperties": false
        }
      },
      "band_formation_details": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "formation_location": {
            "type": "string",
            "description": "The city where the band was formed."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          },
          "band_type": {
            "type": "string",
            "description": "Description of the band's origin and genre."
          }
        },
        "required": [
          "band_name",
          "formation_location",
          "formation_year",
          "band_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_details",
      "related_music_info",
      "band_formation_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
