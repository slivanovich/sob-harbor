{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIndia's Raw Star: India's Raw Star was an Indian singing competition series created by Gajendra Singh of Saibaba Telefilms which began airing on Star Plus from 24 August 2014.  It was hosted by model-actress Gauahar Khan and mentored by singer-rapper Yo Yo Honey Singh.  Rituraj Mohanty won the first season on 30 November 2014 with Darshan Raval and Mohit Gaur finishing second and third respectively.  The other contestants were Sagar Bhatia, Akasa Singh, pardeep singh sran etc.  Arjun Kapoor and Himesh Reshammiya made guest appearances in the show.  \"India's Raw Star\"' witnessed singers like Kailash Kher, Mohit Chauhan and Shaan perform in the final episode with finalists Rituraj, Mohit and Darshan.  The finalists sang the final face off song composed by Sachin and Jigar on the occasion, while Arjun Kapoor, promoted his film \"Tevar\".\n\nKal Ho Naa Ho: Kal Ho Naa Ho (English: \"Tomorrow May Never Come\"), abbreviated as KHNH, is a 2003 Indian romantic drama, directed by debutant director Nikkhil Advani.  The film was written by Niranjan Iyengar and Karan Johar and produced by Yash Johar and Karan Johar under their Dharma Productions banner.  The soundtrack for the film was composed by Shankar-Ehsaan-Loy, with lyrics written by Javed Akhtar.\n\nRhea Kapoor: Rhea Kapoor is an Indian film producer.  The younger daughter of actor Anil Kapoor and his wife Sunita, she is the sister of actors Sonam Kapoor and Harshvardhan Kapoor, granddaughter of filmmaker Surinder Kapoor, niece of filmmaker Boney Kapoor and his wives, producer Mona Shourie Kapoor and actress Sridevi, and actor Sanjay Kapoor.  Her cousins are actors Arjun Kapoor and Mohit Marwah.  She produced Rajshree Ojha's film \"Aisha\", which starred her sister Sonam and Abhay Deol in leading roles.  She has also produced \"Khoobsurat\", directed by Shashanka Ghosh, which is an official remake of Hrishikesh Mukherjee directed film by the same name.\n\nAbhi Nahi Toh Kabhi Nahi: Abhi Nahi Toh Kabhi Nahi is a upcoming Bollywood movie is directed by Jyoti Kapur Das produce by Virender K.Arora and Arjun Kapoor.  The film features Pankaj Kapoor, Lara Dutta, Kay Kay Menon, Rajeev Khandelwal, Sanjay Kapoor, Pooja Chopra, Sanah Kapoor and Himansh Kohli.\n\nTevar: Tevar (English: \"Attitude\") is a 2015 Indian action film directed by Amit Sharma and written by Gunasekhar.  The film stars Arjun Kapoor and Sonakshi Sinha and in lead roles while Manoj Bajpayee plays and crucial role.  It is an official remake of Telugu film \"Okkadu\" (2003).  Shruti Haasan made a special appearance in the song \"Madamiyan\".\n\nAurangzeb (film): Aurangzeb is an Indian action thriller film written and directed by Atul Sabharwal.  The film stars Arjun Kapoor in the lead role, along with Prithviraj Sukumaran, Sashaa Agha, Swara Bhaskar in pivotal roles, while Jackie Shroff, Rishi Kapoor, Amrita Singh, Sikander Kher and Kavi Shastri play supporting characters.  The film is produced and distributed by Aditya Chopra under his studio Yash Raj Films.  The theatrical trailer was unveiled on 3 April 2013, and the film released on 17 May 2013.  The film was commercially successful.\n\nPhir Bhi Tumko Chaahunga: \"Phir Bhi Tumko Chaahunga\" (English: \"I will still love you\") is a song from the Indian film \"Half Girlfriend\".  Picturised on Shraddha Kapoor and Arjun Kapoor, the song has been sung by Arijit Singh and Shashaa Tirupati.  The music of the song is composed by Mithoon and the lyrics are penned by Manoj Muntashir.  Reprise version of the track is sung by Arijit Singh titled, \"Pal Bhar (Chaahunga Reprise)\", and also another version titled, \"Phir Bhi Tumko Chaahungi\" is sung by Shraddha Kapoor along with the instrumental \"Half Girlfriend (Love Theme)\".\n\nHalf Girlfriend (film): Half Girlfriend is an Indian romantic drama film based on the novel of the same name written by Chetan Bhagat.  The film is directed by Mohit Suri and features Arjun Kapoor and Shraddha Kapoor in the lead roles.\n\nArjun Kapoor: Arjun Kapoor (] ; born 26 June 1985) is an Indian actor who appears in Bollywood films.  He is the son of film producers Boney Kapoor and Mona Shourie Kapoor.  After working as an assistant director and associate producer on several films, including \"Kal Ho Naa Ho\" (2003) and \"Wanted\" (2009), he made his acting debut with Habib Faisal's romantic drama \"Ishaqzaade\" (2012), for which he was nominated for the Filmfare Award for Best Male Debut.\n\nBoney Kapoor: Boney Kapoor (born Achal Kapoor on 11 November 1953) is an Indian film producer who has produced numerous Bollywood films like \"Mr. India\", \"No Entry\", \"Judaai\" and \"Wanted\" to his credit.  He is the elder brother of actors Anil Kapoor and Sanjay Kapoor and father of popular actor Arjun Kapoor.\n\nQuestion: Arjun Kapoor worked on a 2003 film directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film Arjun Kapoor worked on.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"arjun_kapoor_role\": {\n      \"type\": \"string\",\n      \"description\": \"Arjun Kapoor's role in the film.\"\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the director of the film.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"arjun_kapoor_role\",\n    \"director\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film Arjun Kapoor worked on."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "arjun_kapoor_role": {
        "type": "string",
        "description": "Arjun Kapoor's role in the film."
      },
      "director": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the director of the film."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "arjun_kapoor_role",
      "director"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
