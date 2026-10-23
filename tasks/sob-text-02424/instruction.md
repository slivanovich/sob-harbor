{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJag tror på människan: \"Jag tror på människan\" is a rock ballad written by Johan Stentorp, Lasse Andersson and Tommy Nilsson, and performed by Tommy Nilsson at Melodifestivalen 2007.  The song participated in the semifinal inside the Kinnarps Arena in the town of Jönköping, Sweden on 3 February 2007, directly reaching the finals inside the Stockholm Globe Arena on 10 March 2007, where it ended up on 10th place, without any single point.  Tommy Nilsson referred to this as to do a \"shutout\" in the Stockholm Globe Arena.  The previous time he performed at Melodifestivalen was also inside the Stockholm Globe Arena, when his song \"En dag\" won the contest in 1989.\n\nA Little Touch of Schmilsson in the Night: A Little Touch of Schmilsson in the Night is an album of classic 20th-century standards sung by American singer Harry Nilsson.  The album was arranged by Frank Sinatra's arranger Gordon Jenkins, and produced by Derek Taylor.  In 1988, it was reissued as A Touch More Schmilsson in the Night, containing an intro and outro (studio chatter) and six additional songs from the recording sessions.\n\nCoconut (song): \"Coconut\" is a song written and first recorded by American singer-songwriter Harry Nilsson, released as the third single from his 1971 album, \"Nilsson Schmilsson\".  It was on the Billboard charts for 10 weeks, reaching #8, and was ranked by \"Billboard\" as the #66 song for 1972.\n\nYou're Breakin' My Heart: You're Breakin' My Heart is a song written by Harry Nilsson, appearing on his 1972 album \"Son of Schmilsson\".  It is notorious for the opening line, \"You're breakin' my heart / You're tearin' it apart / So fuck you\".\n\nPete Ham: Peter William Ham (27 April 1947 – 24 April 1975) was a Welsh singer, songwriter and guitarist, best known as the lead vocalist/composer of the 1970s rock band Badfinger whose hit songs include \"No Matter What\", \"Day After Day\" and \"Baby Blue.\"  He also co-wrote the ballad \"Without You\", a worldwide Number One hit for Harry Nilsson and it has become a standard song as covered by hundreds of artists consistently throughout the years since.  Ham was granted two Ivor Novello Awards related to the song in 1973.\n\nHerbie Flowers: Brian Keith \"Herbie\" Flowers (born 19 May 1938) is an English musician specialising in electric bass, double bass and tuba.  He is noted as a member of Blue Mink, T. Rex and Sky and as one of Britain's best-known session bass players, having contributed to recordings by Elton John (\"Tumbleweed Connection\", \"Madman Across the Water\"), David Bowie (\"Space Oddity\", \"Diamond Dogs\"), Lou Reed (\"Transformer\", including the prominent bass line of \"Walk on the Wild Side\"), Melanie (\"Candles in the Rain\"), Roy Harper (\"Bullinamingvase\"), David Essex (\"Rock On\"), Allan Clarke, Al Kooper (\"New York City (You're a Woman)\"), Bryan Ferry (\"The Bride Stripped Bare\"), Harry Nilsson (\"Nilsson Schmilsson\", \"Son of Dracula\"), Cat Stevens (\"New Masters\", \"Foreigner\"), Serge Gainsbourg (\"Histoire de Melody Nelson\"), Paul McCartney (\"Give My Regards to Broad Street\"), George Harrison (\"Somewhere in England\", \"Gone Troppo\", \"Brainwashed\") and Ringo Starr (\"Stop and Smell the Roses\").  He also played bass on \"Jeff Wayne's Musical Version of The War of the Worlds\".  By the end of the 1970s, Flowers had played bass on an estimated 500 hit recordings.\n\nSpaceman (Harry Nilsson song): \"Spaceman\" is a song written and recorded by American singer-songwriter Harry Nilsson, released on his 1972 album, Son of Schmilsson.\n\nJump into the Fire: \"Jump into the Fire\" is a song by American singer-songwriter Harry Nilsson, released on his 1971 album \"Nilsson Schmilsson\".  It was also issued as the album's second single, after \"Without You\", and peaked at number 27 on America's \"Billboard\" Hot 100 chart and number 16 in Canada.\n\nSon of Schmilsson: Son of Schmilsson is the eighth album by American singer Harry Nilsson.  Nilsson was being pressured to produce a follow-up album similar to his 1971 breakthrough, \"Nilsson Schmilsson\", but instead, he created a more eccentric work.  The album was produced by Richard Perry and features musical contributions from former Beatles Ringo Starr and George Harrison.  Other musicians on the recording include Nicky Hopkins, Klaus Voormann, Bobby Keys and Peter Frampton.  Among the album's tracks are \"You're Breakin' My Heart\" and the US hit \"Spaceman\".\n\nNilsson Schmilsson: Nilsson Schmilsson is the seventh album by American singer Harry Nilsson, released by RCA Records in November 1971.  It was Nilsson's most commercially successful work, producing three of his best-known songs.  Among these was the number 1 hit \"Without You\", written by Pete Ham and Tom Evans of the group Badfinger.  The album was the first of two Nilsson albums recorded in London and produced by Richard Perry.\n\nQuestion: What award did the man, who wrote \"Without You\" for Nilsson Schmilsson, win?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"album\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"album\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"writer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"role\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"award_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"award_name\": {\n          \"type\": \"string\"\n        },\n        \"number_of_awards\": {\n          \"type\": \"integer\"\n        },\n        \"year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"award_name\",\n        \"number_of_awards\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"song_details\",\n    \"writer\",\n    \"award_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "album": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "album"
        ],
        "additionalProperties": false
      },
      "writer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "award_details": {
        "type": "object",
        "properties": {
          "award_name": {
            "type": "string"
          },
          "number_of_awards": {
            "type": "integer"
          },
          "year": {
            "type": "integer"
          }
        },
        "required": [
          "award_name",
          "number_of_awards",
          "year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "song_details",
      "writer",
      "award_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
