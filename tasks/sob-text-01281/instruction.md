{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPraise (band): Praise were an English new-age music group formed in London in 1991, comprising Geoff MacCormack, Simon Goldenberg and Miriam Stockley.  The group was considered to be foundational in the genre of ethnic electronica.\n\nValley Entertainment: Valley Entertainment is an American music distributor and independent record label based in New York City, United States.  The company was founded in 1994 by Barney Cohen and Jon Birge.  In 2001, it acquired the prestigious back catalogue of space, ambient, and new-age music from Hearts of Space Records.  s of 2017 , it has a catalogue of about 375 releases.\n\nMannheim Steamroller: Mannheim Steamroller is an American Neoclassical new-age music group founded by Chip Davis, that is known primarily for its \"Fresh Aire\" series of albums, which blend classical music with elements of new age and rock, and for its modern recordings of Christmas music.  The group has sold 28 million albums in the U.S. alone.\n\nNeoclassical new-age music: Within the broad movement of new-age music, neoclassical new-age music is influenced by and sometimes also based upon early, baroque or classical music, especially in terms of melody and composition.  The artist may offer a modern arrangement of a work by an established composer or combine elements from classical styles with modern elements to produce original compositions.  Many artists within this subgenre are classically trained musicians.  Although there is a wide variety of individual styles, neoclassical new-age music is generally melodic, harmonic, and instrumental, using both traditional musical instruments as well as electronic instruments.  Similar neoclassical elements can often be found within other genres besides new-age music, including electronic music, minimalist music, post-rock music and neoclassical dark wave music.\n\nZingaia: Zingaia is a musical group in the genres of contemporary world music, new-age music and Ethnic electronica.  They have released three albums and have appeared on six compilations, including the Billboard charting album \"Buddha-Lounge 3\".\n\nInside (Paul Horn album): Inside is a 1968 album by jazz flautist Paul Horn, considered one of the earliest new-age music and world fusion records.  The album was recorded inside the Taj Mahal on 25 April 1968, while Horn was with the Beatles in India, and released on the Epic Records label.  It has sold over one million copies.  The album has been reissued under the name Inside the Taj Mahal.\n\nThe Most Relaxing New Age Music in the Universe: The Most Relaxing New Age Music in the Universe is a two-disk album of new-age music produced by Kin-Kou Music under Savoy Label Group and first released on January 11, 2005.  Each disk contains 12 tracks arranged and performed by various artists.  The album reached number six in top New Age album charts in 2005, and was on the Billboard charts in that genre for 40 weeks.  It was followed by several more albums: \"More of the Most Relaxing New Age Music in the Universe\" (July 2005), \"The Ultimate Most Relaxing New Age Music in the Universe\" (June 2006), and \"The Best of the Most Relaxing New Age Music in the Universe\" (October 2012).  Each contained music by many of the same artists and was produced under the same label.\n\nSummer Song (album): Summer Song is part of Mannheim Steamroller's \"Ambience\" collection.  It was released in 2001 on CD by American Gramaphone and features 7 summer-themed tracks.\n\nNorihiro Tsuru: Norihiro Tsuru (都留教博)is a Japanese violinist and composer.  He has composed the scores to several anime series, including \"The Heroic Legend of Arslan\", \"Mermaid's Forest\" and \"Mermaid's Scar\".  He released his first album \"月をつくった男\" in 1989.  He also organized the New-age music group Acoustic Cafe in 1990 (not related to the American radio programme Acoustic Café).\n\nNarada Productions: Narada is a record label formed in 1983 as an independent new-age music label and distributed by MCA Records.  Now a fully owned subsidiary of Universal Music Group and distributed by Capitol Music Group's Blue Note Records, the label evolved through an expansion of formats to include world music, jazz, Celtic music, new flamenco, acoustic guitar and piano genre releases.\n\nQuestion: What is the name of the American Neoclassical new-age music group that released the \"Ambience\" collection in 2001?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"group_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the music group.\"\n    },\n    \"group_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin of the music group.\"\n    },\n    \"group_genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres associated with the music group.\"\n    },\n    \"album_collection_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album collection mentioned in the context.\"\n    },\n    \"collection_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the album collection (or part of it) was released.\"\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the American Neoclassical new-age music group that released the 'Ambience' collection in 2001.\"\n    }\n  },\n  \"required\": [\n    \"group_name\",\n    \"group_origin\",\n    \"group_genres\",\n    \"album_collection_name\",\n    \"collection_release_year\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "group_name": {
        "type": "string",
        "description": "The name of the music group."
      },
      "group_origin": {
        "type": "string",
        "description": "The country of origin of the music group."
      },
      "group_genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres associated with the music group."
      },
      "album_collection_name": {
        "type": "string",
        "description": "The name of the album collection mentioned in the context."
      },
      "collection_release_year": {
        "type": "integer",
        "description": "The year the album collection (or part of it) was released."
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the American Neoclassical new-age music group that released the 'Ambience' collection in 2001."
      }
    },
    "required": [
      "group_name",
      "group_origin",
      "group_genres",
      "album_collection_name",
      "collection_release_year",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
