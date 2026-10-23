{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAngelo Montrone: Angelo Montrone is an American record producer, songwriter, and talent scout (A&R).  Montrone has played a key role as producer and A&R man for Grammy-winning acts including Matisyahu and Los Lonely Boys, as well as producing acts such as jam band favorite Railroad Earth, and discovering a young Jennifer Love Hewitt.  Over the course of his nearly 30-year career, he has worked as an independent record producer as well as being a staff producer and A&R man for Sony, Elektra Entertainment, Atlantic Records, Or Music, Razor & Tie, and Majestic Music.  Montrone had a #4 song on the Billboard Dance Charts with \"Break Me\".  Also, his song \"Free to Be a Woman\" was the theme song for the Style Network's show \"The Modern Girl\".  He is the founder and CEO of the Majestic Music record label based in Hampton Falls, New Hampshire.\n\nCharlie Puth: Charles Otto Puth Jr. ( ) (born December 2, 1991) is an American singer, songwriter and record producer.  He is known for his 2015 song \"See You Again\", which he wrote, co-produced, and performed with Wiz Khalifa for the \"Furious 7\" soundtrack as a tribute to Paul Walker.\n\nCulpa al Corazón: \"Culpa al Corazón\" (English: \"Blame the Heart\") is a 2015 song by American singer Prince Royce.  The song was released on November 13, 2015 as the lead single taken from Royce's fifth studio album, \"Five\" (2017).  It received a Lo Nuestro nomination for Tropical Song of the Year.\n\nShow You Love (Kato and Sigala song): \"Show You Love\" is a song by Danish DJ Kato and British DJ Sigala.  It features the vocals of American singer Hailee Steinfeld.  The song is a re-release of the 2015 song \"Show You Love\" Kato vs. Sigala featuring Grace Tither.\n\nTrees Dallas: Trees first opened its doors as a venue in May 1990.  Named for its trunk-like support beams, Trees hosted bands including Nirvana, Radiohead, Mazzy Star, and The Afghan Whigs during its initial run as a venue before the club closed in May 2005.  It was reopened on August 14, 2009 by Clint Barlow, former drummer for Vanilla Ice and spouse Whitney Barlow.  Since its resurrection, the venue has seen acts including Hiatus Kaiyote, Matt Corby, Charlie Puth, Robert DeLong, Charli XCX, and Jess Glynne.\n\nNicholas Furlong (musician): Nicholas Furlong (born September 16, 1986), professionally known as RAS, is an American singer, songwriter, and record producer.  His work is noted to cross many musical genres, ranging from rock, dance, and pop, to hip-hop.  Furlong has had many chart successes, both in America and internationally.  He has worked with many acts including Avicii, WALK THE MOON, All Time Low, Steve Aoki, blink-182, 5 Seconds of Summer, Krewella, Papa Roach, Skylar Grey, Machine Gun Kelly, Diplo, Onyx, Waka Flocka Flame, The Front Bottoms, and Logan Henderson.\n\nUnda K9 Records: Unda K9 Records is an independent Australian record label founded by a female hip-hop record producer Lui.  Since the formation, the label has represented a number of hip-hop acts including Figgkidd a.k.a. Lee Monro, Bishop a.k.a. Michael Sison, DJ Eko, Bukkcity a.k.a. Andre Knight, DJ Denno, DJ Funk (Melbourne), Big Dave (Distribution Only), Tycotic, 13th Son, Syntax (from Trace Elements), DirtBox Kings, Herb (from Basic Equipment) and DJ Crusador.  Even though the company had seen some very positive times, it folded its recording studio, label and management division in 2009.  Unda K9 Records has since re-branded dropping the \"records\" to only Unda K9 and concentrates on selected musical releases, artist meet and greets, publicity, touring and MMA events.\n\nBack It Up (Prince Royce song): \"Back It Up\" is a 2015 song by American singer Prince Royce, featuring Jennifer Lopez and Pitbull.  The song was released on May 4, 2015 as the second single taken from Royce's fourth studio album, \"Double Vision\".\n\nCool (Alesso song): \"Cool\" is a 2015 song by a Swedish electronic musician Alesso featuring vocals from American singer Roy English (also known by his real name Brandon Wronski), the frontman of the former American rock band Eye Alaska.  It premiered on February 13, 2015 on BBC Radio 1.  The track, which samples Kylie Minogue's \"Get Outta My Way\", was officially released in Europe on 16 February 2015 and in North America on 17 February 2015.  The song was released on 26 April 2015 in the UK.\n\nNicol Sponberg: Nicol Sponberg (1970) is an American Christian singer.  She was formerly a member of her brother's band Selah under the maiden name Nicol Smith.  She is best known for her 2004 album \"Resurrection\" and the title song \"Resurrection\".  The third single from her solo album \"Resurrection,\" \"Crazy In Love\", crossed over to peak at No. 13 on the \"Billboard\" Adult Contemporary chart and was one of the Top 30 most played adult contemporary songs of 2006.\n\nQuestion: Since its resurrection Trees has seen acts including an American singer known for what 2015 song?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"venue_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music venue.\"\n    },\n    \"resurrection_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date the venue reopened or was resurrected.\"\n    },\n    \"performer_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"singer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the American singer who performed at the venue.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the singer.\"\n        },\n        \"known_for_song\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"song_title\": {\n              \"type\": \"string\",\n              \"description\": \"The title of the 2015 song the singer is known for.\"\n            },\n            \"release_year\": {\n              \"type\": \"integer\",\n              \"description\": \"The release year of the song.\"\n            },\n            \"song_description\": {\n              \"type\": \"string\",\n              \"description\": \"A brief description of the song's context or significance.\"\n            }\n          },\n          \"required\": [\n            \"song_title\",\n            \"release_year\",\n            \"song_description\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"singer_name\",\n        \"nationality\",\n        \"known_for_song\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"venue_name\",\n    \"resurrection_date\",\n    \"performer_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "venue_name": {
        "type": "string",
        "description": "The name of the music venue."
      },
      "resurrection_date": {
        "type": "string",
        "description": "The date the venue reopened or was resurrected."
      },
      "performer_details": {
        "type": "object",
        "properties": {
          "singer_name": {
            "type": "string",
            "description": "The name of the American singer who performed at the venue."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the singer."
          },
          "known_for_song": {
            "type": "object",
            "properties": {
              "song_title": {
                "type": "string",
                "description": "The title of the 2015 song the singer is known for."
              },
              "release_year": {
                "type": "integer",
                "description": "The release year of the song."
              },
              "song_description": {
                "type": "string",
                "description": "A brief description of the song's context or significance."
              }
            },
            "required": [
              "song_title",
              "release_year",
              "song_description"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "singer_name",
          "nationality",
          "known_for_song"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "venue_name",
      "resurrection_date",
      "performer_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
