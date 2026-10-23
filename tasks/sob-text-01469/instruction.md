{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Incredible Hulk (1982 TV series): The Incredible Hulk is an animated television series based on the Marvel Comics character of the same name.  The series ran for 13 episodes on NBC in 1982, part of a combined hour with \"Spider-Man and His Amazing Friends\" (as The Incredible Hulk and the Amazing Spider-Man).  Compared to the live-action \"The Incredible Hulk\" television series from Universal, this series followed the Hulk comic books much more closely, particularly with regard to the Hulk's origin, the supporting cast (though Rio and his daughter Rita do not appear in the comics), and the heavy use of fantastical elements.  This was the second Hulk animated series: in 1966, the Hulk appeared in 39 seven-minute segments as part of TV's \"The Marvel Super Heroes\".\n\nList of Mr. Bean (animated TV series) episodes: This is the episode list of \"Mr. Bean\", a British animated television series based on the 1990 TV series of the same name.  Characters include Mr. Bean, Irma Gobb and the driver of the Reliant Supervan, with the addition of Mrs. Wicket, Bean's landlady, and her cat Scrapper.  In February 2001, the series was officially announced, with it premièring shortly afterwards.\n\nTimothy Goes to School: Timothy Goes to School is a Canadian children's animated television series based on the series of Yoko and other individual books by Rosemary Wells such as \"\"Shy Charles\"\", \"\"Fritz and the Mess Fairy\"\", and \"\"Noisy Nora\"\", but is titled after the book of the same name.  It primarily features a young enthusiastic raccoon named Timothy (voiced by Austin Di Iulio), who attends a fictional primary school called \"Hilltop School\" along with ten other students (each of which are of different animals), who are mainly friends of him and each other.  The kindergarten class is taught by Mrs. Jenkins, a comforting teacher who enjoys educating and helping her students.\n\nCarol Ann Susi: Carol Ann Susi (February 2, 1952 – November 11, 2014) was an American actress.  She was known for providing the voice of recurring unseen character Mrs. Wolowitz on the television series \"The Big Bang Theory\".\n\nSpongeBob SquarePants (film series): SpongeBob SquarePants is an American animated/live-action comedy film series based on the Nickelodeon animated television program of the same name, created by Stephen Hillenburg.  It began in 2004 with the release of \"The SpongeBob SquarePants Movie\".  The series is distributed and owned by Paramount Pictures, a subsidiary of Nickelodeon's parent company Viacom.  All films feature the regular television voice cast: Tom Kenny, Clancy Brown, Rodger Bumpass, Bill Fagerbakke, Mr. Lawrence, Jill Talley, Carolyn Lawrence, Mary Jo Catlett and Lori Alan.  The first installment was directed by Hillenburg, and all subsequent films were directed by former showrunner Paul Tibbitt.\n\nEscape from Cluster Prime: Escape from Cluster Prime is a one-hour animated television special produced by Frederator Studios on Nickelodeon.  It features the characters from the Nickelodeon animated television series, \"My Life as a Teenage Robot\".  It was nominated for the Emmy Award for Animated Program (For Programming One Hour or More) in 2006.\n\nIron Man (TV series): Iron Man, also known as Iron Man: The Animated Series, is an American animated television series based on Marvel Comics' superhero Iron Man.  The series aired from 1994 to 1996 in syndication as part of \"The Marvel Action Hour\", which packaged \"Iron Man\" with another animated series based on Marvel properties, the \"Fantastic Four\", with one half-hour episode from each series airing back-to-back.  The show was backed by a toy line that featured many armor variants.\n\nPuff and the Incredible Mr. Nobody: Puff and the Incredible Mr. Nobody is a 30-minute animated television film loosely based on the song \"Puff, the Magic Dragon\" by Leonard Lipton and Peter Yarrow.  The title character was voiced by Burgess Meredith, and the film also featured the voice of David Mendenhall.  The special first aired May 17, 1982 on CBS.  This was the last \"Puff the Magic Dragon\" special.\n\nMrs. Puff: Mrs. Puff is a fictional character in the American animated television series \"SpongeBob SquarePants\" and both films based on the franchise.  She is voiced by actress Mary Jo Catlett and debuted in the season one episode \"Boating School\" on August 7, 1999.  Mrs. Puff was created and designed by marine biologist and animator Stephen Hillenburg.  He developed the character in response to a request from Nickelodeon that the show star a schoolteacher.  Hillenburg did not want to write SpongeBob as a school-age child, so Mrs. Puff was introduced as his driving instructor rather than a classroom educator.\n\nKrrish (franchise): Krrish is a franchise of Indian science fiction films, superhero films, television series, comics and video games.  The film series is directed, produced and written by Rakesh Roshan.  It is considered Indian cinema's first such film series.  All three films starred Rakesh's son Hrithik Roshan, and were scored by his brother Rajesh Roshan.  The films are centred, initially, on a mentally handicapped boy who has an encounter with an extraterrestrial being, and later, his son, who grows up to be a reluctant superhero.  The first two films were blockbusters in the Indian market, and hits in the overseas markets.  The third film was released on 1 November 2013 and was declared a blockbuster shattering many box office records grossing over () at the box office.  In 2013, an animated television series based on this \"Krrish\" film series, and named \"Kid Krrish\", aired on Cartoon Network India.  It also spawned a spin-off animation-cum-live-action series titled \"J Bole Toh Jadoo\" that aired on Nickelodeon (India).  \"Krrish 3\" was the first Indian film to launch its own official Facebook Emoticons as part of the promotion.\n\nQuestion: Which animated television series based on the Nickelodeon program of the same name, features the character Mrs. Puff?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the animated television series.\"\n    },\n    \"network\": {\n      \"type\": \"string\",\n      \"description\": \"The television network associated with the series.\"\n    },\n    \"is_animated_series\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the series is an animated television series.\"\n    },\n    \"character_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the featured character.\"\n        },\n        \"voice_actor\": {\n          \"type\": \"string\",\n          \"description\": \"The voice actor for the character.\"\n        },\n        \"debut_episode\": {\n          \"type\": \"string\",\n          \"description\": \"The episode in which the character debuted.\"\n        },\n        \"debut_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the character debuted.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"voice_actor\",\n        \"debut_episode\",\n        \"debut_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"series_name\",\n    \"network\",\n    \"is_animated_series\",\n    \"character_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "series_name": {
        "type": "string",
        "description": "The name of the animated television series."
      },
      "network": {
        "type": "string",
        "description": "The television network associated with the series."
      },
      "is_animated_series": {
        "type": "boolean",
        "description": "Indicates if the series is an animated television series."
      },
      "character_details": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the featured character."
          },
          "voice_actor": {
            "type": "string",
            "description": "The voice actor for the character."
          },
          "debut_episode": {
            "type": "string",
            "description": "The episode in which the character debuted."
          },
          "debut_date": {
            "type": "string",
            "description": "The date the character debuted."
          }
        },
        "required": [
          "character_name",
          "voice_actor",
          "debut_episode",
          "debut_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "series_name",
      "network",
      "is_animated_series",
      "character_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
