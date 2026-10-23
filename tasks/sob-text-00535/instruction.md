{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSecond Hand White Baby Grand: \"Second Hand White Baby Grand\" is an original song introduced in the twelfth episode of the first season of the musical TV series \"Smash\", entitled \"Publicity\".  The song was written by Marc Shaiman and Scott Wittman, but within the show's universe, it is written by songwriting team Julia Houston (Debra Messing) and Tom Levitt (Christian Borle) for their Marilyn Monroe musical \"Bombshell\".\n\nDon't Forget Me (Smash song): \"Don't Forget Me\" is an original song introduced in the fifteenth episode of the first season of the musical TV series \"Smash\", entitled \"Bombshell\".  It was written by Marc Shaiman and Scott Wittman, but in the show's fictional universe, it was written by the songwriting team of Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nOn Lexington &amp; 52nd Street: \"On Lexington & 52nd Street\" (also \"Lexington & 52nd Street\") is an original song introduced in the seventh episode of the first season of the musical TV series \"Smash\", entitled \"The Workshop\".  The song is written by Marc Shaiman and Scott Wittman, but in the show's universe, it is written by the songwriting team of Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nDon't Say Yes Until I Finish Talking: \"Don't Say Yes Until I Finish Talking\" is an original song introduced in the tenth episode of the musical TV series \"Smash\", entitled \"Understudy\".  The song is written by Marc Shaiman and Scott Wittman, but in the show's universe, it is written by the songwriting team of Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nHistory Is Made at Night (song): \"History Is Made at Night\" is an original song introduced in the fourth episode of the first season of the musical TV series \"Smash\", entitled \"The Cost of Art\".  It was written by Marc Shaiman and Scott Wittman, but within the show's universe, it was written by the songwriting team of Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nThe 20th Century Fox Mambo: \"The 20th Century Fox Mambo\" is an original song introduced in the second episode of the first season of the musical TV series \"Smash\", entitled \"The Callback\".  It was written by Marc Shaiman and Scott Wittman, but in the show's universe, it was written by songwriting team Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nI Never Met a Wolf Who Didn't Love to Howl: \"I Never Met a Wolf Who Didn't Love to Howl\" is an original song introduced in the fourth episode of the musical TV series \"Smash\", entitled \"The Cost of Art\".  The song is written by Marc Shaiman and Scott Wittman, but in the show's universe, it was written by the songwriting duo Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nLet Me Be Your Star: \"Let Me Be Your Star\" is an original song introduced in the first episode of the first season of the musical TV series \"Smash\", entitled Pilot.  It was written by Marc Shaiman and Scott Wittman, but in the show's universe, it was written by songwriting duo Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for the Marilyn Monroe musical they are working on, \"Bombshell\".\n\nThe National Pastime: \"The National Pastime\" is an original song introduced in the first episode of the first season of the musical TV series \"Smash\", entitled \"Pilot\".  The song was written by Marc Shaiman and Scott Wittman, but in the show's universe, it was written by songwriting duo Tom Levitt (Christian Borle) and Julia Houston (Debra Messing) for their Marilyn Monroe musical \"Bombshell\".\n\nDebra Messing: Debra Lynn Messing (born August 15, 1968) is an American actress.  She is known for her many television roles, most notably Grace Adler on the NBC sitcom \"Will & Grace\".\n\nQuestion: Along side the American actress known most notably for her role as Grace Adler on the NBC sitcom \"Will & Grace\" who wrote the song \"On Lexington & 52nd Street\" in the show's universe for the Marilyn Monroe musical \"Bombshell\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"song_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the song in question.\"\n    },\n    \"musical_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the musical for which the song was written in the show's universe.\"\n    },\n    \"in_show_writers\": {\n      \"type\": \"array\",\n      \"description\": \"The names of the songwriting team who wrote the song in the show's universe.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"writer_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the writer in the show's universe.\"\n          },\n          \"actor_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the actor portraying the writer.\"\n          }\n        },\n        \"required\": [\n          \"writer_name\",\n          \"actor_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"actress_notable_role\": {\n      \"type\": \"string\",\n      \"description\": \"The notable role of the American actress mentioned in the question.\"\n    },\n    \"co_writer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-writer alongside the specified actress in the show's universe.\"\n    }\n  },\n  \"required\": [\n    \"song_title\",\n    \"musical_title\",\n    \"in_show_writers\",\n    \"actress_notable_role\",\n    \"co_writer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "song_title": {
        "type": "string",
        "description": "The title of the song in question."
      },
      "musical_title": {
        "type": "string",
        "description": "The title of the musical for which the song was written in the show's universe."
      },
      "in_show_writers": {
        "type": "array",
        "description": "The names of the songwriting team who wrote the song in the show's universe.",
        "items": {
          "type": "object",
          "properties": {
            "writer_name": {
              "type": "string",
              "description": "The name of the writer in the show's universe."
            },
            "actor_name": {
              "type": "string",
              "description": "The name of the actor portraying the writer."
            }
          },
          "required": [
            "writer_name",
            "actor_name"
          ],
          "additionalProperties": false
        }
      },
      "actress_notable_role": {
        "type": "string",
        "description": "The notable role of the American actress mentioned in the question."
      },
      "co_writer_name": {
        "type": "string",
        "description": "The name of the co-writer alongside the specified actress in the show's universe."
      }
    },
    "required": [
      "song_title",
      "musical_title",
      "in_show_writers",
      "actress_notable_role",
      "co_writer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
