{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAkhlaq Ahmed: Akhlaq Ahmed (Urdu: اخلاق احمد‎ ; January 10, 1950 – August 4, 1999) was a Pakistani playback singer.  He was a member of a famous singing group from Karachi with two other artists,film playback singer Masood Rana and film actor Nadeem.  Akhlaq debuted as a singer in the 1973 film, \"Pazaib\" with music by \"Lal Mohammad Iqbal\".  He was unable to get a dominant place in the Pakistan film industry because when he started his singing career, at that time Ahmed Rushdi was the prominent playback singer in the Pakistani film industry.  Even then he remained a somewhat successful singer in the late 1970s and 1980s.\n\nS. P. Balasubrahmanyam discography: Sripathi Panditaradhyula Balasubrahmanyam (   ) is an Indian film playback singer, actor, music director, voice actor and film producer.  He is mostly referred to as S. P. B. or Balu.  He has won the Guinness World Record for recording the highest number of songs.  He won the National Film Award for Best Male Playback Singer six times and the Nandi Awards in Telugu cinema 25 times from the Government of Andhra Pradesh.\n\nUnni Menon: Unni Menon is an Indian film playback singer.  He has sung over 3000 songs in South Indian languages like Malayalam, Tamil, Telugu and Kannada.  In the early part of his career, he spent many years as a low-profile playback singer.  The turning point in his career came when he sang the song \"Pudhu Vellai Mazhai\" from Mani Ratnam's award winning 1992 Tamil film \"Roja\", composed by A. R. Rahman.  He has frequently associated with A. R. Rahman, lending his voice to nearly 25 popular songs from films like \"Karuththamma\" (1994) and \"Minsaara Kanavu\" (1997).\n\nSinov Raj: Sinov Raj is an Indian film playback singer known for his works in Malayalam and Telugu films.  he made his debut as the playback singer in the Malayalam movie \"Camel Safari\" singing the song \"Sayyan\". He works mostly in the Malayalam & Telugu film industry.  He has a background of a band which started before with his few friends.\n\nHarini (singer): Harini is an Indian film playback singer and classical singer, who sings mainly in Tamil films.  She has also sung in Hindi, Malayalam, Telugu and Kannada language films, whilst working with many leading film composers.  She considers legendary singer K. S. Chitra as her inspiration.  She is married to another playback singer Tippu.\n\nRicha Sharma (singer): Richa Sharma (born 29 August 1980) is an Indian film playback singer as well a devotional singer.  In 2006, she sang Bollywood's longest track, the \"bidaai\" song, in film \"Baabul\" (2006).\n\nS. P. Balasubrahmanyam: Sripathi Panditaradhyula Balasubrahmanyam (   ; born 4 June 1946) is an Indian film playback singer, actor, music director, voice actor and film producer.  He is mostly referred to as S. P. B. or Balu.  He has won the Guinness World Record for recording the highest number of songs.  He has garnered six National Film Awards for Best Male Playback Singer, and twenty five Nandi Awards for his works towards Telugu cinema.  In 2012, He received the Andhra Pradesh state NTR National Award for his contributions to Indian cinema.\n\nKavita Krishnamurthy: Kavita Krishnamurthy is an Indian film playback singer.  Trained in classical music, she has sung a wide range of classical-based songs.  In her career, she has worked with a variety of music composers, including Laxmikant–Pyarelal, R. D. Burman, Hamsalekha and A. R. Rahman.  She is also the recipient of four Filmfare Best Female Playback Singer Awards, including three consecutive awards in the period 1994–1996, and the Padmashri which she received in 2005.  In 1999, she married violinist L. Subramaniam.\n\nVani Harikrishna: Vani Harikrishna () is an Indian film playback singer and music director, who works in South Indian films, primarily in Kannada cinema.  She has composed, written and sung several devotional songs before entering into the film playback singing.  She won Karnataka State Award for her rendition of \"Madhuvana Karedare\" song from the film \"Inthi Ninna Preethiya\".  Vani debuted as a film composer with the 2013 film \"Loosegalu\".\n\nCollaborations 3: Collaborations 3 is album in the series of Collaborations albums by Sukshinder Shinda.  Featured in this album are Jazzy B, Diljit Dosanjh, Kamal Khan, Shazia Manzoor, Surinder Shinda, Richa Sharma, Abrar-Ul-Haq and Don Revo.  The Album is on MovieBox (UK) Music Waves (Canada) and T-Series (India).\n\nQuestion: Collaborations 3 features an Indian film playback singer who sang the bidaai song in what film?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"singer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Indian film playback singer.\"\n    },\n    \"album_collaboration\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the album in which the singer was featured.\"\n    },\n    \"film_performance\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film where the singer performed the specified song.\"\n        },\n        \"song_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the song sung by the artist in the film.\"\n        },\n        \"song_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the song, if available.\"\n        },\n        \"film_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"film_title\",\n        \"song_name\",\n        \"film_release_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"singer_name\",\n    \"album_collaboration\",\n    \"film_performance\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "singer_name": {
        "type": "string",
        "description": "The name of the Indian film playback singer."
      },
      "album_collaboration": {
        "type": "string",
        "description": "The name of the album in which the singer was featured."
      },
      "film_performance": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the film where the singer performed the specified song."
          },
          "song_name": {
            "type": "string",
            "description": "The name of the song sung by the artist in the film."
          },
          "song_description": {
            "type": "string",
            "description": "A description of the song, if available."
          },
          "film_release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "film_title",
          "song_name",
          "film_release_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "singer_name",
      "album_collaboration",
      "film_performance"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
