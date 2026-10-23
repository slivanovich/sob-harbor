{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTony Bennett's &quot;Something&quot;: Tony Bennett's \"Something\" is a 1970 studio album by Tony Bennett.  As with Bennett's previous album, \"Tony Sings the Great Hits of Today! \", it contains renditions of contemporary pop songs, including \"Something\", which had appeared on the earlier release.\n\nOrchid and Hound: Orchid and Hound is a pop duo composed of John Constantine and Lawrence Alarcon.  Their music has been described as pop music paired with lush arrangements and strong vocal harmonies with influences of Björk, Jacques Brel and Queen.\n\nShapes and Patterns: Shapes and Patterns is a 1997 album by the British pop group Swing Out Sister.  It was first released in Japan in March 1997, and then in Europe and USA the year after.  Producer Paul Staveley O'Duffy, who co-wrote half of the songs, was back at the helm.  As an orchestra was once again employed (led by Gavyn Wright), the lush arrangements characteristic of \"Kaleidoscope World\" resurfaced.  The album features the track \"Now You're Not Here\" which was used as the theme to the Japanese programme \"Mahiru No Tsuki\", as well as a reworked version of \"Better Make It Better\" which had featured on their previous studio album, \"The Living Return\".\n\nRags to Riches (song): \"Rags to Riches\" is a 1953 popular song by Richard Adler and Jerry Ross.  The best-known version of the song, recorded by Tony Bennett with Percy Faith and his orchestra, was number one for eight weeks on the Billboard chart in 1953 and became a gold record.  In the same year, a version by David Whitfield reached number three in the British charts and one by Billy Ward and his Dominoes with Jackie Wilson singing lead made number two on Billboard's R&B chart.  Later recordings by Sunny & the Sunliners (#45 in 1963) and Elvis Presley (#33 in 1971) also made the Billboard charts.\n\nLife Is Beautiful (Tony Bennett album): Life Is Beautiful is an album released by Tony Bennett in 1975.  It was named after the song written by Fred Astaire.  The album was the first project of Bennett's own Improv label.  The album was Bennett's tribute to the American songbook featuring songs of Cole Porter, Richard Rodgers, Irving Berlin and others.  The pianist, Torrie Zito, wrote new arrangements for Bennett's large session orchestra.  The album was reissued by Concord with the addition of a separately recorded 13-minute Cole Porter medley.\n\nSnowfall: The Tony Bennett Christmas Album: Snowfall: The Tony Bennett Christmas Album is a 1968 studio album by Tony Bennett, his first Christmas album.  It was arranged and conducted by Robert Farnon.\n\nPercy Faith: Percy Faith (April 7, 1908 – February 9, 1976) was a Canadian bandleader, orchestrator, composer and conductor, known for his lush arrangements of pop and Christmas standards.  He is often credited with popularizing the \"easy listening\" or \"mood music\" format.  Faith became a staple of American popular music in the 1950s and continued well into the 1960s.  Though his professional orchestra-leading career began at the height of the swing era, Faith refined and rethought orchestration techniques, including use of large string sections, to soften and fill out the brass-dominated popular music of the 1940s.\n\nAlone Together (Tony Bennett album): Alone Together is an album by American singer Tony Bennett.  It was originally released in 1960 on Columbia as CL 1471.  It almost exclusively features string arrangements of standards, with a choir, harp accompaniment and sparse percussion in places.  It is among the most obscure Bennett recordings.  So far, it has been released on CD only in Japan by Sony/CBS.\n\nA Weather: A Weather is an indie band from Portland, Oregon, fronted by Aaron Gerber and Sarah Winchester.  Other members include Zach Boyle, Aaron Krenkel and Louis Thomas.  Their debut album, \"Cove\" (2008), was described as \"tenderly crafted chamber pop\" and \"bursting with intricately plotted melodies and lush arrangements\", and was released to favourable reviews.In 2007, the band toured in the U.S. with Bright Eyes.\n\nTony Bennett at the Talk of the Town: Tony Bennett at the Talk of the Town was a British television series hosted by American pop standards and jazz singer Tony Bennett that aired during 1972.  It was staged in London from the Talk of the Town nightclub in conjunction with Thames Television.  In the United States and Canada, the programme was known as This Is Music, and was aired in 1974 and 1976, respectively.\n\nQuestion: What Canadian bandleader known for his lush arrangements of pop and Christmas standards also recorded a version of the 1953 song Rags to Riches with Tony Bennett?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"bandleader_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Canadian bandleader.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the bandleader.\"\n    },\n    \"known_for_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of what the bandleader is known for.\"\n    },\n    \"collaboration_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"song_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song recorded in collaboration.\"\n        },\n        \"collaborating_artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist who collaborated on the song.\"\n        },\n        \"song_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the song was released or recorded.\"\n        },\n        \"chart_performance\": {\n          \"type\": \"string\",\n          \"description\": \"Details about the song's performance on music charts.\"\n        },\n        \"record_certification\": {\n          \"type\": \"string\",\n          \"description\": \"Any certification the record received (e.g., gold, platinum).\"\n        }\n      },\n      \"required\": [\n        \"song_title\",\n        \"collaborating_artist\",\n        \"song_release_year\",\n        \"chart_performance\",\n        \"record_certification\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"bandleader_name\",\n    \"nationality\",\n    \"known_for_description\",\n    \"collaboration_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "bandleader_name": {
        "type": "string",
        "description": "The name of the Canadian bandleader."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the bandleader."
      },
      "known_for_description": {
        "type": "string",
        "description": "A description of what the bandleader is known for."
      },
      "collaboration_details": {
        "type": "object",
        "properties": {
          "song_title": {
            "type": "string",
            "description": "The title of the song recorded in collaboration."
          },
          "collaborating_artist": {
            "type": "string",
            "description": "The artist who collaborated on the song."
          },
          "song_release_year": {
            "type": "integer",
            "description": "The year the song was released or recorded."
          },
          "chart_performance": {
            "type": "string",
            "description": "Details about the song's performance on music charts."
          },
          "record_certification": {
            "type": "string",
            "description": "Any certification the record received (e.g., gold, platinum)."
          }
        },
        "required": [
          "song_title",
          "collaborating_artist",
          "song_release_year",
          "chart_performance",
          "record_certification"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "bandleader_name",
      "nationality",
      "known_for_description",
      "collaboration_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
