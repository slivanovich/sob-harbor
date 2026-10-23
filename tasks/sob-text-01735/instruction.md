{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDead Presidents (soundtrack): Dead Presidents is the first of two soundtracks to the 1995 film, \"Dead Presidents\".  It was released on September 26, 1995, by Capitol Records and consists of 1970s R&B, funk and soul music.  The soundtrack was very successful, reaching #14 on the \"Billboard\" 200 and #1 on the Top R&B/Hip-Hop Albums charts, and was certified gold on December 1, 1995.  The soundtrack's success led Capitol Records to release a second volume the following year.\n\nRush Hour (instrumental): \"Rush Hour\" is an instrumental composition by American DJ Christopher Lawrence.  It was released as a 12-inch single in 2000, featuring the song \"Ride the Light\" as a B-side.  A shorter version of \"Rush Hour\" later appeared on Lawrence's debut studio album, \"All or Nothing\", which was released in 2004.  The track peaked at number 118 on the UK Singles Chart.  It was also featured on the soundtrack for the video game \"\".\n\nChris Tucker: Christopher Tucker (born August 31, 1971) is an American actor and stand-up comedian.  He is known for playing the role of Smokey in \"Friday\" and as Detective James Carter in the \"Rush Hour\" film series.  Tucker became a frequent stand up performer on Def Comedy Jam in the 1990s.  He also appeared in Luc Besson's \"The Fifth Element\", Quentin Tarantino's \"Jackie Brown\", and David O. Russell's \"Silver Linings Playbook\" and \"Money Talks\".\n\nDead Presidents, Vol. 2: Dead Presidents, Vol.  2 is the second soundtrack released for the film, \"Dead Presidents\".  It was released on April 2, 1996, through Capitol Records.  After the success of the first soundtrack, Capitol Records decided to release a second soundtrack.  However, this one failed to match the success of the first, only reaching #45 on the Top R&B/Hip-Hop Albums chart.  Like the first, it consists of 1970s era funk and soul music.\n\nRush Hour (1998 film): Rush Hour is a 1998 American buddy action comedy film directed by Brett Ratner and starring Jackie Chan and Chris Tucker as mismatched cops who must rescue the Chinese consul's kidnapped daughter.  Released on September 18, 1998, the film grossed over $244 million worldwide.  The film's success led to two sequels, \"Rush Hour 2\" (2001) and \"Rush Hour 3\" (2007).\n\nDead Presidents: Dead Presidents is a 1995 American crime thriller film co-written by Michael Henry Brown and the Hughes brothers, Albert and Allen, who also produced and directed.  It stars Larenz Tate, Keith David, Chris Tucker, Freddy Rodriguez, N'Bushe Wright, and Bokeem Woodbine.  The film chronicles the life of Anthony Curtis, focusing on his teenage years as a high school graduate and his experiences during the Vietnam War.  As he returns to his hometown in The Bronx, Curtis finds himself struggling to support himself and his family, eventually turning to a life of crime.\n\nLess Than an Hour: \"Less Than an Hour (Theme from Rush Hour 3)\" is a 2007 song by rapper Nas and singer Cee-Lo.  It was first heard in the final credits of the film \"Rush Hour 3\" on August 10, before being released on iTunes in September.  It is featured on Nas' \"Greatest Hits\" album.  It is produced by Salaam Remi, who arranged the track's rhythm section.  Lalo Schifrin also received a writing credit for arranging the song's orchestra.\n\nRush Hour 3: Rush Hour 3 is a 2007 American martial arts/buddy action comedy film and the third and final film in the \"Rush Hour\" series, starring Jackie Chan and Chris Tucker.  The film was officially announced on May 7, 2006, and filming began on July 4, 2006.  The film is set in Paris and Los Angeles.  \"Rush Hour 3\" was released on August 10, 2007, in the United States.\n\nDead Presidents (song): \"Dead Presidents\" is a 1996 song by rapper Jay-Z.  It was released as the first promotional single for Jay-Z's debut album \"Reasonable Doubt\", although it did not directly appear on the album: a different version, with the same backing track and chorus but different lyrics, called \"Dead Presidents II\", appeared on \"Reasonable Doubt\" instead.  The single was a commercial success, and was certified as an RIAA certification gold single in June 1996.  Both versions of the song are regarded as some of the greatest hip-hop songs ever recorded, and \"Dead Presidents II\" was voted #16 in About.com's Top 100 Rap Songs.\n\nRush Hour 2: Rush Hour 2 is a 2001 American martial arts buddy cop action comedy film.  It is the sequel to the 1998 film \"Rush Hour\" and the second installment in the \"Rush Hour\" film series.  The film stars Jackie Chan and Chris Tucker who respectively reprise their roles as Inspector Lee and Detective Carter.  The film finds Lee and Carter embroiled in a counterfeit scam involving the Triads.\n\nQuestion: Which actor from Dead Presidents also appeared in the Rush Hour film series?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who appeared in both film series.\"\n    },\n    \"film_appearances\": {\n      \"type\": \"array\",\n      \"description\": \"List of film series or films the actor appeared in, relevant to the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film or film series.\"\n          },\n          \"type\": {\n            \"type\": \"string\",\n            \"enum\": [\n              \"film\",\n              \"film_series\"\n            ],\n            \"description\": \"The type of appearance (single film or a series).\"\n          },\n          \"character_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the character played by the actor in this film/series.\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"type\",\n          \"character_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_film_series_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of distinct film series/films the actor appeared in, as per the question.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"film_appearances\",\n    \"common_film_series_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who appeared in both film series."
      },
      "film_appearances": {
        "type": "array",
        "description": "List of film series or films the actor appeared in, relevant to the question.",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the film or film series."
            },
            "type": {
              "type": "string",
              "enum": [
                "film",
                "film_series"
              ],
              "description": "The type of appearance (single film or a series)."
            },
            "character_name": {
              "type": "string",
              "description": "The name of the character played by the actor in this film/series."
            }
          },
          "required": [
            "title",
            "type",
            "character_name"
          ],
          "additionalProperties": false
        }
      },
      "common_film_series_count": {
        "type": "integer",
        "description": "The number of distinct film series/films the actor appeared in, as per the question."
      }
    },
    "required": [
      "actor_name",
      "film_appearances",
      "common_film_series_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
