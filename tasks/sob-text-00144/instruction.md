{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPachaikili Muthucharam: Pachaikili Muthucharam is a 2007 Tamil romantic thriller directed by Gautham Vasudev Menon which is strongly based on 2005 British-American thriller film Derailed.  The film stars R. Sarathkumar, Jyothika, Andrea Jeremiah and Milind Soman.  The film's score and soundtrack were composed by Harris Jayaraj.  The soundtrack was released on 20 January 2007 to positive reviews.  The film was released on 13 February 2007.  This is available in Telugu under name Drohi.  This film was inspired by the English film Derail and the same film was released in Hindi, The Train starring Emran hashmi and Geetha Basra.\n\nBlinded (1997 film): Blinded (original French title: A ciegas) is a 1997 romantic thriller directed and written by Daniel Calparsoro.  The film's director Daniel Calparsoro was nominated for the Golden Lion award at the 1997 Venice International Film Festival, but lost to Takeshi Kitano's romantic film Hana-bi.\n\nNakash Aziz: Nakash Aziz (born February 24, 1985), also known as Nakash, is an Indian playback singer and music composer.  He has assisted the legendary composer A. R. Rahman on films like \"Highway\", \"Raanjhanaa\", \"Rockstar\", \"Delhi 6\" and \"I\" in Hindi.  He is popularly known for playback of songs like \"Jabra Fan\" from \"Fan\",<ref name=\"http://www.deccanchronicle.com/ 2016\"> </ref> \"Sari Ke Fall Sa\" and \"Gandi Baat\" from the film \"R.. .  Rajkumar\" (2013) and \"Dhating Nach\" from film \"Phata Poster Nikhla Hero\" (2013); the latter two films of which were picturized on Shahid Kapoor.\n\nGangster (2016 film): Gangster (Bengali: গ্যাংস্টার ) is an Indian Bengali language romantic thriller film directed by Birsa Dasgupta under the banner of Shree Venkatesh Films.  The film stars debutant Yash Dasgupta with Mimi Chakraborty in leading roles.  The film is a romantic thriller where Yash plays the role of a gangster.  This is an Intense romantic thriller with few twists and turns to keep the audience glued to their seats.  The film has been shot in Istanbul, Turkey.  The music by Arindam Chatterjee is captivating.  The film released on 7 October 2016.\n\nJahan Jaaeyega Hamen Paaeyega: Jahan Jaaeyega Hamen Paaeyega is a Bollywood romantic thriller directed by Janmendra Ahuja and produced by Dr Lakhan Sinhaa.  The film stars Govinda, Sakshi Shivanand, Sharat Saxena, Kader Khan and Mukesh Rishi in the main casts.  It was released on 6 July 2007 although it was filmed many years back.\n\nI (film): I (also known as \"Shankar's I \") is a 2015 Indian Tamil-language romantic thriller film written and directed by Shankar and co-written by Subha.  Produced and distributed by V. Ravichandran under his production company, Aascar Films, the film features Vikram, Amy Jackson and Suresh Gopi in lead roles while Upen Patel, Santhanam and Ramkumar Ganesan portray pivotal roles.  The soundtrack and film score were composed by A. R. Rahman.  Production design was handled by T. Muthuraj.  P. C. Sreeram was the film's cinematographer and editing was done by Anthony.\n\nKalabha Kadhalan: Kalabha Kadhalan is a 2006 Tamil romantic thriller directed by debutant Igore, starring Arya and Renuka Menon.  This film was a low-budget production and the soundtrack was composed by Niru.  Akshaya also appeared in this family based psycho thriller.  It enjoyed relatively quiet success.  It shared a similar storyline to a great thriller S.J. Suryah’s Vaali and another 2006 film called Uyir.  The film’s censors demanded it an \"Adults Only\" rating.\n\nEk Villain: Ek Villain (English: \"One Villain\") is a 2014 Indian romantic thriller directed by Mohit Suri.  The film stars Sidharth Malhotra, Shraddha Kapoor and Riteish Deshmukh in lead roles, and tells the story of a hardened criminal whose terminally ill wife is murdered by a serial killer.  The film was produced by Ekta Kapoor and Shobha Kapoor under Balaji Motion Pictures and ALT Entertainment.  The film is an unofficial remake of the 2010 South Korean action thriller film \"I Saw the Devil\".  Upon its release on 27 June 2014, the film received mixed to positive reviews from the critics, and was a commercial success.\n\nYeh Saali Zindagi: Yeh Saali Zindagi (\"This bloody life\") is a 2011 Hindi romantic thriller directed by Sudhir Mishra.  The film stars Irrfan Khan, Chitrangada Singh, Arunoday Singh and Aditi Rao Hydari in the lead roles.  The film was released on 4 February 2011 to positive critical acclaim and was moderately successful at the box office.\n\nPolam Pol: Polam Pol features songs sung by Farhad Bhiwandiwala, Nakash Aziz, Palak Muchhal, Shree Dayal, Ash King.  Music and Background Score for the film is composed by Paresh-Bhavesh.  The soundtrack was launched on 19 January.\n\nQuestion: Nakash Aziz performed music for what Tamll-language romantic thriller directed by Shankar?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        },\n        \"language\": {\n          \"type\": \"string\",\n          \"description\": \"The primary language of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        }\n      },\n      \"required\": [\n        \"director\",\n        \"language\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"music_contribution\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"contributor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the music contributor.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the contributor in the film's music production, as described in the context.\"\n        },\n        \"main_composer\": {\n          \"type\": \"string\",\n          \"description\": \"The main composer whom the contributor assisted.\"\n        },\n        \"notes\": {\n          \"type\": \"string\",\n          \"description\": \"Additional details about the specific context of the contribution.\"\n        }\n      },\n      \"required\": [\n        \"contributor_name\",\n        \"role\",\n        \"main_composer\",\n        \"notes\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_details\",\n    \"music_contribution\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "director": {
            "type": "string",
            "description": "The director of the film."
          },
          "language": {
            "type": "string",
            "description": "The primary language of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          }
        },
        "required": [
          "director",
          "language",
          "genre"
        ],
        "additionalProperties": false
      },
      "music_contribution": {
        "type": "object",
        "properties": {
          "contributor_name": {
            "type": "string",
            "description": "The name of the music contributor."
          },
          "role": {
            "type": "string",
            "description": "The role of the contributor in the film's music production, as described in the context."
          },
          "main_composer": {
            "type": "string",
            "description": "The main composer whom the contributor assisted."
          },
          "notes": {
            "type": "string",
            "description": "Additional details about the specific context of the contribution."
          }
        },
        "required": [
          "contributor_name",
          "role",
          "main_composer",
          "notes"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_details",
      "music_contribution"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
