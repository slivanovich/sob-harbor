{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlfred Hitchcock's Anthology – Volume 2: Alfred Hitchcock's Anthology – Volume 2 is the second installment in the \"Alfred Hitchcock's Anthology\" series.  Originally published in hardcover as \"Alfred Hitchcock's Tales to Take Your Breath Away\" in 1977, this issue contains 29 stories from \"Alfred Hitchcock's Mystery Magazine\" that, by the editors, were believed to be the best published the preceding year (1977).\n\nList of Alfred Hitchcock Presents guest stars: The following is a list of guest stars and other actors who appeared on the television series \"Alfred Hitchcock Presents\", which started in 1955 as a half-hour show, changed its name to \"The Alfred Hitchcock Hour\" when it expanded to an hour, and returned as \"The New Alfred Hitchcock Presents\" in the 1980s as an hour-long show.\n\nThe Birds II: Land's End: The Birds II: Land's End is a 1994 American made-for-television horror film and a sequel to Alfred Hitchcock's 1963 classic \"The Birds\" starring Brad Johnson, Chelsea Field, James Naughton and Tippi Hedren in a minor role different from the one she played in the original Hitchcock film.  The original music score was composed by Ron Ramin.  \"The Birds II: Land's End\" premiered on Showtime on March 14, 1994.\n\nList of The Alfred Hitchcock Hour episodes: The following is a list of the 93 episodes of the television program The Alfred Hitchcock Hour, which is a continuation of the program \"Alfred Hitchcock Presents\" (1955–60).  \"The Alfred Hitchcock Hour\", like its predecessor, is an anthology series in the thriller genre.  NBC renamed the program when they extended its running-time from about 25 minutes to about 50 minutes.  Both programs were hosted by Alfred Hitchcock, whose directorial work in thriller films is extremely influential.  Hitchcock directed only one episode of \"The Alfred Hitchcock Hour\": \"I Saw The Whole Thing\" (Season 1, episode 4).\n\nAlfred Hitchcock's Anthology – Volume 4: Alfred Hitchcock's Anthology – Volume 4 is the fourth installment of \"Alfred Hitchcock's Anthology\", one of the many Alfred Hitchcock story collection books; edited by Eleanor Sullivan.  Originally published in hardcover as \"Alfred Hitchcock's Tales to Scare You Stiff\" in 1978, the book includes 26 short stories and a short novel called \"The Graveyard Shift\" by William P. McGivern.  Also, within the 26 short stories is \"The Green Heart\" by Jack Ritchie which was made into the 1971 film \"A New Leaf\".\n\nAlfred Hitchcock's Anthology – Volume 5: Alfred Hitchcock's Anthology – Volume 5 is the fifth installment of \"Alfred Hitchcock's Anthology\", one of the many Alfred Hitchcock story collection books; edited by Eleanor Sullivan.  Originally published in hardcover as \"Alfred Hitchcock's Tales to Send Chills Down Your Spine\" in 1979, the book contains 29 short stories by many well-known crime fiction novelists.\n\nAlfred Hitchcock's Mystery Magazine: \"AHMM\" was founded in 1956 by HSD Publications, which licensed the use of the director's name.  Though there was no formal connection with the television show, stories published in the magazine were sometimes adapted by the producers of \"Alfred Hitchcock Presents\" (and later, \"The Alfred Hitchcock Hour)\".  A few writers, such as Henry Slesar, wrote for both.  Other contributors during the magazine’s early years included Evan Hunter/Ed McBain, Ed Lacy, Bill Pronzini, Jim Thompson, Donald E. Westlake and Charles Willeford (who briefly worked for the magazine, as did Patricia Hitchcock.  Alfred's daughter).\n\nUnder Capricorn: Under Capricorn is a 1949 British historical thriller film directed by Alfred Hitchcock about a couple in Australia who started out as lady and stable boy in Ireland, and who are now bound together by a horrible secret.  The film was based on the novel \"Under Capricorn\" (1937) by Helen Simpson, with a screenplay by James Bridie.  It was adapted to the screen by Hume Cronyn.  This was Hitchcock's second film in Technicolor, and like the preceding color film \"Rope\" (1948), it also featured 10-minute takes.\n\nRope (film): Rope is a 1948 American psychological crime thriller film noir directed by Alfred Hitchcock, based on the 1929 play of the same name by Patrick Hamilton, adapted by Hume Cronyn and with a screenplay by Arthur Laurents.\n\nAlfred Hitchcock's Anthology – Volume 1: Alfred Hitchcock's Anthology – Volume 1 is the first installment of \"Alfred Hitchcock's Anthology\", one of the many Alfred Hitchcock story collection books; edited by Eleanor Sullivan.  Originally published in hardcover in 1976 as \"Alfred Hitchcock's Tales to Keep You Spellbound\", the book is a collection of 30 stories originally published in \"Alfred Hitchcock's Mystery Magazine\".\n\nQuestion: Alfred Hitchcock film Under Capricorn, which was preceeded by Rope, was adapted to the screen by which person?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in question.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"screen_adapter\": {\n      \"type\": \"string\",\n      \"description\": \"The person who adapted the film to the screen.\"\n    },\n    \"preceding_film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film that preceded it.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the preceding film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_release_year\",\n    \"film_director\",\n    \"screen_adapter\",\n    \"preceding_film\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film in question."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the film."
      },
      "screen_adapter": {
        "type": "string",
        "description": "The person who adapted the film to the screen."
      },
      "preceding_film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film that preceded it."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the preceding film."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_release_year",
      "film_director",
      "screen_adapter",
      "preceding_film"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
