{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlice in Verse: The Lost Rhymes of Wonderland: Alice in Verse: The Lost Rhymes of Wonderland (2010) is a reimagining of Lewis Carroll's \"Alice in Wonderland\" written by British-American author J.T. Holden.  It tells the story of \"Alice's Adventures in Wonderland\" (with a \"Slight Detour \"Through the Looking-Glass\"\") in 19 rhyming poems, each written in the same style as Lewis Carroll's original verse.  The book includes 36 illustrations by American artist Andrew Johnson.\n\nAlice (Avril Lavigne song): \"Alice\" is a song written and performed by Avril Lavigne for \"Almost Alice\", the soundtrack to the 2010 film \"Alice in Wonderland\".  An extended version was released as a hidden track on Lavigne's fourth studio album, \"Goodbye Lullaby\".\n\nAlice in Wonderland (1949 film): Alice in Wonderland (French: Alice au pays des merveilles ) is a 1949 French film based on Lewis Carroll's fantasy novel \"Alice's Adventures in Wonderland\".  Directed by Dallas Bower, the film stars Carol Marsh as Alice, Stephen Murray as Lewis Carroll, and Raymond Bussières as The Tailor.  Most of the Wonderland characters are portrayed by stop-motion animated puppets created by Lou Bunin.\n\nAlmost Alice: Almost Alice is a concept album of various artists' music inspired by Tim Burton's film, \"Alice in Wonderland\".  The album is also notable for featuring songs that were inspired from quotes directly from Lewis Carroll's original novel \"Alice's Adventures in Wonderland\".  For example, both \"The Lobster Quadrille\" (by Franz Ferdinand) and \"You Are Old, Father William\" (by They Might Be Giants) are both word-for-word performances of poems from the original \"Alice\" as quoted by The Mock-Turtle (the former) and Alice herself to the Caterpillar (the latter).  Furthermore, \"Very Good Advice\" by Robert Smith is a cover of Kathryn Beaumont's \"Very Good Advice\" from Disney's 1951 animated adaptation of \"Alice in Wonderland\".\n\nTea Party (song): \"Tea Party\" is a song by Estonian recording artist Kerli.  It is featured on the album \"Almost Alice\", a multi-artist compilation album which features music that is inspired by the 2010 film \"Alice in Wonderland\" released on March 2, 2010.  \"Almost Alice\" debuted at number five on the \"Billboard\" 200 and topping \"Billboard\"' s Digital Albums and Soundtracks charts.\n\nThe Game of Alice in Wonderland: The Game of Alice in Wonderland is a traditional card game published in 1882 by Selchow and Righter.  It is the first game, based on the book Alice’s Adventures in Wonderland by Lewis Carroll.  The cards feature colorized illustrations based on the original Sir John Tenniel illustrations.\n\nAlice in Wonderland (1976 film): Alice in Wonderland (sometimes listed as Alice in Wonderland: An X-Rated Musical Comedy) is a 1976 American musical fantasy adult film, loosely based on Lewis Carroll's book \"Alice's Adventures in Wonderland\".  It was directed by Bud Townsend and starred Kristine De Bell as Alice.  The film was favorably reviewed by film critic Roger Ebert in 1976.\n\nWonderland (musical): Wonderland: A New Alice, formerly called Wonderland: Alice's New Musical Adventure, is a musical with a book by Jack Murphy and Gregory Boyd, lyrics by Murphy, and music by Frank Wildhorn.  The story, a contemporary version of \"Alice's Adventures in Wonderland\" and \"Through the Looking-Glass\" by Lewis Carroll, is set in New York City and focuses on writer Alice Cornwinkle and her 10-year-old daughter Chloe.\n\nAlice in Wonderland (1988 film): Alice in Wonderland is an Australian 51-minute direct-to-video animated film from Burbank Films Australia.  It was originally released in 1988.  The film is based on Lewis Carroll's classic English novel, \"Alice's Adventures in Wonderland\", first published in 1865, and was adapted by Paul Leadon.  Unlike many other adaptations of the novel, this one did not borrow elements from its sequel, \"Through the Looking-Glass\" (1871), combined into one film.  The production company produced a 73-minute adaptation of the second novel the year before, in 1987, entitled \"Alice: Through the Looking-Glass\".  The 1988 film was produced by Roz Phillips and directed by Rich Trueblood.  Quite uncommon among Burbank Films Australia's adaptations of classic literary works, \"Alice in Wonderland\" featured one original theme song, composed by Mark Isaacs.  The copyright in this film is now owned by Pulse Distribution and Entertainment and administered by digital rights management firm NuTech Digital.\n\nCaterpillar (Alice's Adventures in Wonderland): The Caterpillar (also known as the Hookah-Smoking Caterpillar) is a fictional character appearing in Lewis Carroll's book \"Alice's Adventures in Wonderland\".\n\nQuestion: What is one song from Almost Alice that was based on a Hookah-Smoking being from Lewis Carrolls book Alice's Adventures in Wonderland?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album.\"\n    },\n    \"inspired_by_character\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character from the book.\"\n        },\n        \"character_alias\": {\n          \"type\": \"string\",\n          \"description\": \"An alternative name or description for the character.\"\n        },\n        \"source_book\": {\n          \"type\": \"string\",\n          \"description\": \"The book from which the character originates.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"character_alias\",\n        \"source_book\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"song_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the song.\"\n        },\n        \"artist\": {\n          \"type\": \"string\",\n          \"description\": \"The artist who performed the song.\"\n        },\n        \"inspiration_type\": {\n          \"type\": \"string\",\n          \"description\": \"How the song was inspired by the character or source material.\"\n        }\n      },\n      \"required\": [\n        \"song_title\",\n        \"artist\",\n        \"inspiration_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"album_name\",\n    \"inspired_by_character\",\n    \"song_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_name": {
        "type": "string",
        "description": "The name of the album."
      },
      "inspired_by_character": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character from the book."
          },
          "character_alias": {
            "type": "string",
            "description": "An alternative name or description for the character."
          },
          "source_book": {
            "type": "string",
            "description": "The book from which the character originates."
          }
        },
        "required": [
          "character_name",
          "character_alias",
          "source_book"
        ],
        "additionalProperties": false
      },
      "song_details": {
        "type": "object",
        "properties": {
          "song_title": {
            "type": "string",
            "description": "The title of the song."
          },
          "artist": {
            "type": "string",
            "description": "The artist who performed the song."
          },
          "inspiration_type": {
            "type": "string",
            "description": "How the song was inspired by the character or source material."
          }
        },
        "required": [
          "song_title",
          "artist",
          "inspiration_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "album_name",
      "inspired_by_character",
      "song_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
