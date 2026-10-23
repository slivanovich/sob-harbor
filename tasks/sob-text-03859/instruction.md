{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLet Me Be Clear: Let Me Be Clear is the debut extended play by Australian alternative band Gang of Youths.  The EP features 5 original tracks and a cover of Joni Mitchell's \"Both Sides Now\".  It was released on 29 July 2016 and debuted at number 2 on the ARIA Charts.\n\nClient Liaison (EP): Client Liaison is the self-titled debut extended play (EP) by Australian indie pop duo Client Liaison, released independently on 5 September 2014.\n\nLet Me Down Easy (Sheppard song): \"Let Me Down Easy\" is a song by Australian indie pop band Sheppard.  It was included on their debut extended play \"Sheppard\" in 2012 and their debut album \"Bombs Away\" in 2014.  The song was not released as a single in Australia, but used to promote the extended play, which went on to achieve double platinum accreditation.  The song received APRA and ARIA award nominations.  \"Let Me Down Easy\" was released as an international single in January 2015.\n\nFifth Harmony discography: The discography of American girl group Fifth Harmony consists of three studio albums, six extended plays, ten singles and thirteen music videos.  After finishing third on the second season of the American televised singing competition \"The X Factor\" the group was signed to Epic Records though Syco Music.  Less than a year later, Fifth Harmony released their debut single from their debut extended play, \"Miss Movin' On\".  The single charted on the Mainstream Top 40 and New Zealand, peaking at 27 in both countries.  It was certified gold in the United States for selling combined sales and track-equivalent streams units of 500,000.  The group's extended play, \"Better Together\" peaked at number six on the \"Billboard\" 200 and number 18 in New Zealand, charting in both countries similar to the group's lead single.  As part of the promotion for \"Better Together\", four other versions were released of the extended play, including an acoustic release, a Spanish-language acoustic and a standard Spanish-language translated version as well as a remix edition.\n\nSame Kind of Different: Same Kind of Different is the debut extended play (EP) by Australian indie pop artist Dean Lewis.  It was released on 12 May 2017.\n\nRatcat: Ratcat are an Australian indie rock band which were formed in 1985 and are fronted by mainstay vocalist and guitarist, Simon Day.  Their combination of indie pop song writing and energetic punk-style guitar won them fans from both the indie and skate-punk communities.  They found mainstream success with their extended play, \"Tingles\" (October 1990), album \"Blind Love\" (June 1991) and the single, \"Don't Go Now\" (April), which all reached No. 1 on the ARIA Charts during 1991.  The band released two subsequent albums, however they did not match the earlier chart success.  Ratcat ceased regular live shows in the late 1990s, however they have continued to play sporadic shows since that time.\n\nSheppard (EP): Sheppard is the self-titled debut extended play (EP) by Australian indie pop band Sheppard, released independently on 17 August 2012.  It was produced by Stuart Stuart at Analog Heart Studios.\n\nGang of Youths: Gang of Youths are an Australian indie rock group consisting of principal songwriter David Le'aupepe (lead vocals/guitar/piano), Max Dunn (bass guitar), Jung Kim (keyboards/guitar), Joji Malani (lead guitar) and Donnie Borzestowski (drums).  Their debut album, \"The Positions\", peaked at No. 5 on the ARIA Albums Chart in May 2015 and was nominated for multiple ARIA Awards.\n\nMegMac: MegMac (also stylised as \"MEGMAC\") is the self-titled debut extended play (EP) by Australian indie pop artist Meg Mac.  It was released on 12 September 2014.  The EP contains four original songs and a cover of Bill Withers' “Grandma's Hands”.\n\nThe Missy Higgins EP: The Missy Higgins EP is the debut extended play (EP) by Australian indie pop singer songwriter, Missy Higgins.\n\nQuestion: What is the name of this Australian indie rock group, whose debut album was \"The Positions\" and debut extended play was \"Let Me Be Clear\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"band_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Australian indie rock group.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the band.\"\n    },\n    \"debut_album\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of their debut album.\"\n        },\n        \"chart_peak_position\": {\n          \"type\": \"integer\",\n          \"description\": \"The highest position the debut album reached on the charts.\"\n        },\n        \"chart_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the chart where the album peaked.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the debut album was released.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"chart_peak_position\",\n        \"chart_name\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"debut_extended_play\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of their debut extended play (EP).\"\n        },\n        \"number_of_original_tracks\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of original tracks on the EP.\"\n        },\n        \"cover_song_details\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"title\": {\n              \"type\": \"string\",\n              \"description\": \"The title of the cover song on the EP.\"\n            },\n            \"original_artist\": {\n              \"type\": \"string\",\n              \"description\": \"The original artist of the cover song.\"\n            }\n          },\n          \"required\": [\n            \"title\",\n            \"original_artist\"\n          ],\n          \"additionalProperties\": false\n        },\n        \"release_date\": {\n          \"type\": \"string\",\n          \"description\": \"The release date of the debut EP.\"\n        },\n        \"chart_peak_position\": {\n          \"type\": \"integer\",\n          \"description\": \"The highest position the debut EP reached on the charts.\"\n        },\n        \"chart_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the chart where the EP peaked.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"number_of_original_tracks\",\n        \"cover_song_details\",\n        \"release_date\",\n        \"chart_peak_position\",\n        \"chart_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"band_name\",\n    \"genre\",\n    \"debut_album\",\n    \"debut_extended_play\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "band_name": {
        "type": "string",
        "description": "The name of the Australian indie rock group."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the band."
      },
      "debut_album": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of their debut album."
          },
          "chart_peak_position": {
            "type": "integer",
            "description": "The highest position the debut album reached on the charts."
          },
          "chart_name": {
            "type": "string",
            "description": "The name of the chart where the album peaked."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the debut album was released."
          }
        },
        "required": [
          "title",
          "chart_peak_position",
          "chart_name",
          "release_year"
        ],
        "additionalProperties": false
      },
      "debut_extended_play": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of their debut extended play (EP)."
          },
          "number_of_original_tracks": {
            "type": "integer",
            "description": "The number of original tracks on the EP."
          },
          "cover_song_details": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string",
                "description": "The title of the cover song on the EP."
              },
              "original_artist": {
                "type": "string",
                "description": "The original artist of the cover song."
              }
            },
            "required": [
              "title",
              "original_artist"
            ],
            "additionalProperties": false
          },
          "release_date": {
            "type": "string",
            "description": "The release date of the debut EP."
          },
          "chart_peak_position": {
            "type": "integer",
            "description": "The highest position the debut EP reached on the charts."
          },
          "chart_name": {
            "type": "string",
            "description": "The name of the chart where the EP peaked."
          }
        },
        "required": [
          "title",
          "number_of_original_tracks",
          "cover_song_details",
          "release_date",
          "chart_peak_position",
          "chart_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "band_name",
      "genre",
      "debut_album",
      "debut_extended_play"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
