{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCrazy Loka: Crazy Loka is a 2012 Kannada film starring V. Ravichandran and Daisy Bopanna in the lead roles.  The film is directed by Kavita Lankesh and produced by Confident Group and Shanti Pictures.  Manikanth Kadri is the music director for the film.\n\nUdhayan (film): Udhayan is an Indian Tamil action-romance film directed by debutant Chaplin.  Starring Arulnithi, in his second film, alongside newcomer Pranitha, the film features musical score by saxophone player Kadri Gopalnath's son Manikanth Kadri.  A Muthamizh Padaippagam production, it was started during Pongal 2011 and released on 24 June 2011 with mixed reviews.\n\nBurhan Asaf Belge: Burhan Asaf Belge (February 1, 1899 – January 12, 1967) was a figure among the young intellectuals during the early periods of Republic of Turkey and served as the representative of Muğla province during the 11th term of Turkish National Assembly.  He was a regular contributor to \"Kadro\", a left-wing journal dedicated to \"discussions on ideology and economic-development strategy.\"  Burhan Asaf Belge is the father of the prominent Turkish intellectual Murat Belge and the first husband of the actress Zsa Zsa Gabor (in 1935-41).  He was the brother-in-law of Yakup Kadri Karaosmanoğlu.\n\nPrithvi (2010 film): Prithvi is an 2010 Indian Kannada language film directed by Jacob Varghese, produced by N.S Rajkumar, starring Puneeth Rajkumar and Parvathi in lead roles.  Manikanth Kadri composed the music of the film.\n\nMadeleine Robinson: Madeleine Robinson (born Madeleine Svoboda; 1916–2004) was a French actress.  She was born to a French mother and Czech father near Paris.  She was orphaned at the age of 14, and worked to support herself and her two younger brothers, but enjoyed watching plays.  She then studied under Charles Dullin.  Her first lead role was in \"Forty Little Mothers\" (1936).  During the Occupation of France, she had a prominent role in \"Love Story\" and \"Lumière d'été\" (both 1943), and \"The Bellman\" (1945).  Because she had acted during the Occupation, Robinson found it difficult to get work afterwards, but again came to prominence in Une si jolie petite plage (1949).  Madeleine Robinson won the Volpi Cup for Best Actress in 1959 for her role in \"À double tour\".  In 2001, she was awarded a for her contribution to the field.\n\nRun Anthony: Run Antony (Kannada: ರನ್ ಅಂತೋನಿ ) is a 2016 Indian Kannada Action thriller film written and directed by Raghu Shastri, making his debut.  Produced by Parvathamma Rajkumar, Raghavendra Rajkumar and Guru Rajkumar under Vajreshwari Hospitality banner, the film stars Vinay Rajkumar and debutants Sushmita Joshi and Rukhsar Mir in the lead roles.  The film's score and soundtrack is composed by Manikanth Kadri whilst the cinematography is by Manohar Joshi.\n\nManikanth Kadri: Manikanth Kadri is an Indian film score and soundtrack composer and singer.  He has predominantly scored music for Kannada as well as several Telugu,Tamil,Tulu and Malayalam films.  He is the son of legendary saxophonist Kadri Gopalnath.\n\nKadri Gopalnath: Dr. Kadri Gopalnath (Kannada: ಕದ್ರಿ ಗೋಪಾಲನಾಥ್) (born 11 December 1949) is an Indian saxophonist and one of the pioneers of Carnatic music on the saxophone.\n\nRadhan Ganda: Radhan Ganda () is a 2013 Kannada comedy - action film written and directed by Murugan.  It is produced by Confident Group along with Shanta Pictures.  Komal Kumar and Poorna are in the lead roles.  Manikanth Kadri has composed the soundtrack and film score.  The storyline is similar to 2011 Malayalam movie Makeup Man and the 2001 French movie My Wife Is an Actress.\n\nMaduve Mane: Maduve Mane () (English : \"Wedding House\") is a 2011 Indian Kannada language film in the romantic comedy genre starring Ganesh and Shradha Arya in the lead roles.  The film was directed by Sunil Kumar Singh and produced by H. A. Rahman under the banner J. J. International.  The music of the film was composed by Manikanth Kadri.\n\nQuestion: What was the occupation of Manikanth Kadri's father?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person whose father's occupation is being queried.\"\n    },\n    \"father_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the father.\"\n    },\n    \"father_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The primary occupation of the father.\"\n    },\n    \"father_notable_attributes\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Notable attributes or descriptions of the father.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"father_name\",\n    \"father_occupation\",\n    \"father_notable_attributes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person whose father's occupation is being queried."
      },
      "father_name": {
        "type": "string",
        "description": "The name of the father."
      },
      "father_occupation": {
        "type": "string",
        "description": "The primary occupation of the father."
      },
      "father_notable_attributes": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Notable attributes or descriptions of the father."
      }
    },
    "required": [
      "person_name",
      "father_name",
      "father_occupation",
      "father_notable_attributes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
