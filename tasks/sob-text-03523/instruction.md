{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGulshan Kumar Mehta: Gulshan Kumar Mehta, popularly known by his pen name Gulshan Bawra (literally: \"Gulshan the madman\") (12 April 1937 – 7 August 2009), was an Indian songwriter and actor in Hindi cinema.  In a career spanning 42 years, he has to his credit about 240 songs, he collaborated with noted music directors like Kalyanji Anandji, Shankar Jaikishan, and R D Burman composed almost half of songs in films like \"Khel Khel Mein\" (1975), \"Kasme Vaade\" (1976) and \"Satte Pe Satta\" (1982).  Apart from R.D. Burman hits, he is most remembered for his songs like, \"Mere Desh Ki Dharti\" in \"Upkaar\" (1968), and \"Yaari Hai Imaan Mera\", \"Zanjeer\" (1974), both of which got him the Filmfare Best Lyricist Award.  The latter also top the Binaca Geetmala annual list of 1973.  As a character actor, he also appeared in a small number of Hindi films.\n\nAashiqui 2 (soundtrack): Aashiqui 2 is the soundtrack to the 2013 Bollywood romance film of the same name, directed by Mohit Suri and starring Aditya Roy Kapoor and Shraddha Kapoor in the lead roles.  The album was produced by Bhushan Kumar and Mahesh Bhatt under the banner T-Series and Vishesh Films.  the songs of the film were mostly composed by Jeet Gannguli, although Mithoon and Ankit Tiwari composed two songs each (including both versions) as guest composers.  Irshad Kamil wrote lyrics for most of songs on the album.  Sandeep Nath wrote both versions of \"Sunn Raha Hai\", while Mithoon wrote \"Tum Hi Ho\" and Sanjay Masoom wrote \"Bhula Dena\".  Arijit Singh sang six of the songs on the album.  The music became very popular after its release on 8 April 2013, with songs \"Tum Hi Ho\" and \"Sunn Raha Hai\" topping the charts across various platforms in India.  Jeet Gannguli reused the tune from his own Bengali composition \"Mon Hariye Beghorey\" for \"Milne Hai Mujhse Aayi\".\n\nDesi Kalakaar: \"Desi Kalakaar\" is the title track song from the album \"Desi Kalaakar\" by Honey Singh produced by Gulshan Kumar, story and screen play is by Yo Yo Honey Singh.  The song features Sonakshi Sinha, Yo Yo Honey Singh, Gulshan Grover in the music video.  The video was filmed in various locations around suburbs of Los Angeles, California including Culver City and Palmdale.  The video has received over forty-two million views on T-Series official channel of YouTube.\n\nGaon Hamara Shaher Tumhara: Gaon Hamara Shaher Tumhara is a 1972 Bollywood romance film directed by Naresh Kumar.  The film stars Rajendra Kumar and Rekha .\n\nGulshan Kumar: Gulshan Kumar (born Gulshan Kumar Dua, 5 May 1951 – 12 August 1997) was the founder of the T-Series music label (Super Cassettes Industries Ltd.), and a Bollywood movie producer.  T-Series is now run by his younger brother Krishan Kumar Dua and son Bhushan Kumar.  His daughter Tulsi Kumar is a playback singer.\n\nPehchan (1970 film): Pehchan is a 1970 Filmfare Award winning Bollywood romance film produced & directed by Sohanlal Kanwar, & the story is by Sachin Bhowmick.  The film stars Manoj Kumar, Babita, and Balraj Sahni.  Music is by Shankar Jaikishan.\n\nT-Series: T-Series is an Indian music company founded by Gulshan Kumar which is also engaged in film production and distribution.\n\nMogul (film): Mogul - The Gulshan Kumar Story is an upcoming 2018 Indian biographical film written and directed by Subhash Kapoor and produced by Bhushan Kumar.  The film is based on the life of Gulshan Kumar who was founder of the T-Series music label (Super Cassettes Industries Ltd.), and a Bollywood movie producer.  The film is set to release in 2018.\n\nBewafa Sanam: Bewafa Sanam is a 1993 Hindi film directed by Gulshan Kumar.  It stars Krishan Kumar(Brother of Gulshan Kumar), Shilpa Shirodkar, Aruna Irani, Shakti Kapoor and Kiran Kumar.  The screenplay was written by Sachin Bhowmick, dialogue by Madan Joshi, and story by Gulshan Kumar.  It was produced by Gulshan Kumar.\n\nZindagi Zindagi: Zindagi Zindagi (English: Life, Life) is a 1972 Bollywood romance film directed by Tapan Sinha.  The film stars Deb Mukherjee, Waheeda Rehman, Farida Jalal and Ashok Kumar .  The film revolves around life in a village hospital and has casteism as an issue at its core.  It had excellent music by S. D. Burman which fetched him a National Award for Best Music.  It is a remake of Tapan Sinha's Bengali hit \"Khoniker Atithi\".\n\nQuestion: Who directed the 2013 Bollywood romance film that was produced by an Indian music company founded by Gulshan Kumar ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Bollywood film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"production_company\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the production company.\"\n        },\n        \"founder\": {\n          \"type\": \"string\",\n          \"description\": \"The founder of the production company.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founder\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre\",\n    \"director\",\n    \"production_company\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the Bollywood film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "production_company": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the production company."
          },
          "founder": {
            "type": "string",
            "description": "The founder of the production company."
          }
        },
        "required": [
          "name",
          "founder"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre",
      "director",
      "production_company"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
