{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAsawari Joshi: Asawari Joshi (born 6 May 1965) is a popular Indian actress.  She has acted in many Marathi language films and serials.  She is famous for her role in Hindi TV series, Office Office.  She has acted as Lovely Kapoor in \"Om Shanti Om\", a movie which starred Shahrukh Khan.  She is also best known for her role in Hindi serial \"\" aired on Disney Channel which is the Indian version of American serial Shake It Up.\n\nKabhi Alvida Naa Kehna: Kabhi Alvida Naa Kehna (English: \"Never Say Good Bye\"), also known as KANK, is a 2006 Indian musical romantic drama film directed by Karan Johar and produced under the Dharma Productions banner.  Released on 11 August 2006 in India and North America, it stars Shah Rukh Khan, Rani Mukherji, Abhishek Bachchan and Preity Zinta in the lead roles, while Amitabh Bachchan and Kirron Kher play pivotal supporting roles.  Arjun Rampal also makes a special appearance in the film.\n\nBewafaa (2005 film): Bewafaa (English: Unfaithful ) is a 2005 Indian musical romantic drama film starring Akshay kumar, Anil Kapoor, Kareena Kapoor, Manoj Bajpayee, Sushmita Sen, Shamita Shetty and Kabir Bedi.  The film is directed by Dharmesh Darshan who had earlier directed films like \"Raja Hindustani\" (1996) and \"Dhadkan\" (2000).  \"Bewafaa\" tells the story of changing morals and values in a fast-changing world, with the tagline \"When cultures meet.\"  \"Bewafaa\" was produced by Boney Kapoor, with music composed by Nadeem-Shravan.  It borrows a lot of elements from the 1963 film \"Gumrah\", and the Telugu hit Abhinandana.  The movie was presented by Sahara Group.\n\nOm Shanti Om: Om Shanti Om is a 2007 Indian musical romantic drama thriller film co-written, choreographed and directed by Farah Khan.  It stars Shah Rukh Khan and debutant Deepika Padukone in the lead roles while Arjun Rampal, Shreyas Talpade, and Kirron Kher feature in supporting roles.  More than forty-two well-known Hindi movie stars appear in the course of the film, including thirty of them (not including the stars of the film) in one song alone.  The film is set in the 1970s and 2000s; it pays tribute to, and pokes fun at, the Indian film industry of both these eras.\n\nMohabbatein: Mohabbatein (English: \"Love Stories\" ) is a 2000 Indian musical romantic drama film directed by Aditya Chopra.  It was Chopra's second directorial venture after \"Dilwale Dulhania Le Jayenge\" and was filmed at India and the United Kingdom.  The film stars Amitabh Bachchan and Shah Rukh Khan in pivotal roles, along with six young debutantes.  Aishwarya Rai appeared in flashbacks as Khan's lover.  The film's soundtrack was composed by Jatin-Lalit, while the lyrics were penned by Anand Bakshi.  The film is notable for being the first time that Bachchan and Khan appeared on-screen together.\n\nTaal (film): Taal (English: \"Rhythm\") is a 1999 Indian musical romantic drama film co written, edited, produced and directed by Subhash Ghai.  \"Taal\" was an official selection for the 2005 .  Taal was screened retrospectively, during the 2014 International Film Festival of India in the \"Celebrating Dance in Indian cinema\" section.\n\nRosa Kale: Rosa Kale (Rose Forest) (Sinhalese: \"රෝස කැලේ\" ) is a 2008 Sri Lankan Sinhala drama mystery film directed by Nishantha Weerasingha and produced by Dhammika Siriwardena for Alankulama Films.  It stars Indian actress Monika Maruthiraj and Roshan Ranawana in lead roles along with Sanath Gunathilake and Iranganie Serasinghe.  Music co-composed by Rohana Weerasinghe and Bathiya and Santhush.  It is the 1106th Sri Lankan film in the Sinhala cinema.\n\nKabhi Ajnabi The: Kabhi Ajnabi The is an 1985 Indian musical romantic drama film directed and produced by Vijay Singh. The film stars Debashree Roy, Poonam Dhillon, Sandeep Patil and Iftekhar in lead.\n\nRockstar (2011 film): Rockstar is a 2011 Indian musical romantic drama film directed by Imtiaz Ali, starring Ranbir Kapoor and Nargis Fakhri, with music composed by A. R. Rahman.  The film also stars Moufid Aziz, Aditi Rao Hydari, Piyush Mishra, Shernaz Patel, Kumud Mishra in supporting roles, and also Shammi Kapoor, who makes his last silver screen appearance.  The film was produced by Eros International Ltd. along with Shree Ashtavinayak Cine Vision Ltd.  It follows Janardhan Jakhar a.k.a. JJ or Jordan, who dreams of becoming a rockstar like his inspiration, Jim Morrison.  Yet, eventually on attaining all that he dreamt of, Jordan ends up anguished and despondent without Heer Kaul, whom he so fiercely, passionately loved.\n\nParineeta (2005 film): Parineeta (\"The Married Woman\") is a 2005 Indian musical romantic drama film adaptation of the 1914 Bengali novella, \"Parineeta\" by Sarat Chandra Chattopadhyay.  Directed by debutant Pradeep Sarkar, it was based upon a screenplay by the film's producer, Vidhu Vinod Chopra.  The film featured Vidya Balan (In her Bollywood Debut), Saif Ali Khan and Sanjay Dutt in the lead roles.  Raima Sen plays the supporting role of Lalita's chirpy cousin.  Sabyasachi Chakrabarty plays the pivotal role of Shekhar's father.  Diya Mirza, with a cameo appearance as Shekhar's fiancé and Rekha, with a cameo performance of a night club (Moulin Rouge) singer, are other notable performances.\n\nQuestion: What Indian musical romantic drama thriller film stars Indian actress Asawari Joshi?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres the film belongs to.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"asawari_joshi_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role played by Asawari Joshi in the film.\"\n    },\n    \"lead_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of lead actors in the film.\"\n    },\n    \"supporting_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of supporting actors in the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genres\",\n    \"director\",\n    \"asawari_joshi_role\",\n    \"lead_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres the film belongs to."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "asawari_joshi_role": {
        "type": "string",
        "description": "The role played by Asawari Joshi in the film."
      },
      "lead_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of lead actors in the film."
      },
      "supporting_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of supporting actors in the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genres",
      "director",
      "asawari_joshi_role",
      "lead_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
