{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKalakar: Kalakar (\"Artist\") is a 1983 Indian Hindi-language film directed by P. Sambasiva Rao.  Produced by P. Anand Rao, it stars Kunal Goswami and Sridevi. The basic plot of this film is based on the Tamil film \"Payanangal Mudivathillai\".\n\nToilet: Ek Prem Katha: Toilet: Ek Prem Katha (English - Toilet: A Love Story) is a 2017 Indian Hindi-language film directed by Shree Narayan Singh.  Co-produced by Akshay Kumar and Neeraj Pandey, the film stars Akshay Kumar and Bhumi Pednekar in the lead roles, with Anupam Kher, Sudhir Pandey and Divyendu Sharma in supporting roles.  The film was released on August 11, 2017.  The film is a satirical comedy in support of governmental campaigns to improve the sanitation conditions, with an emphasis on the eradication of open defecation, especially in rural areas.  The film was financially successful in India.\n\nLife's Good (film): Life's Good is an upcoming Bollywood drama film produced by Anand Shukla under his banner EktAnand Pictures directed by Ananth Mahadevan.  The film stars Jackie Shroff, Rajit Kapur, Mohan Kapoor, Anannaya Vij, Saniya Anklesaria and Ankita Shrivastav in the lead roles, whilst Sunita Sen Gupta, Nakul Sahdev and Saanand Verma appear in supporting roles.  The film is inspired by the personal diary of screenwriter Sujit Sen about his stay in a Mumbai hospital.  The film slated for 2018 release.\n\nAurat (1967 film): Aurat (\"Woman\") is a 1967 Indian Hindi-language film produced and directed by S. S. Balan and S. S. Vasan.  It is a remake of 1966 Tamil film \"Chitthi\".  The film stars Padmini, Pran, Rajesh Khanna, Feroz Khan, Kanhaiyalal, David, O. P. Ralhan, Nazima, Lalita Pawar and Leela Chitnis.  The films music is by Ravi. The film is totally revolving around the character of Parvati's life played by Padmini.  The film deals with how Parvati (played by Padmini), who is in true love with character played by Feroz Khan, is forced by circumstances to marry Manoharilal (played by Pran) against wishes of her brother (played by Rajesh Khanna) and later is tested by life to show whether after marriage to Manoharilal, she is truly affectionate to Manoharilal or is she having an affair with her ex-boyfriend.\n\nAugust 2 (film): August 2 is an Indian Hindi-language film directed by P V Krishnan.  It was claimed to be a true independent mainstream film made within its budget.  Producers of the film claims that the film is made on the micro budget of Rs. 300,000.  The film had got selected for the Red Carpet Premier in The Indian Independent Film Festival 2013.\n\nSaanand Verma: Saanand Verma is an Indian film and TV actor.  He has appeared in a number of serials as well as advertising films.  He is currently playing the role of Anokhe Lal Saxena in the serial \"Bhabhi Ji Ghar Par Hain! \" which airs on &TV.\n\nBhabi Ji Ghar Par Hai!: Bhabhi Ji Ghar Par Hai!  (English:\" Sister-in-law is at home!\")  is an Indian Hindi-language comedy television series that premiered on March 02, 2015 and airs weeknights at 10:30 p.m. on &TV.  The show is inspired by the 1995 Hindi serial Shrimaan Shrimati.  In November 2016, The show, has been extended by one more day, named “Bhabiji Ghar Par Hai Shanivaar Special” in which celebrities visit the sets.  The show is being shot at Artisian and Nirman Studio, Vasai(A Tribeni Group venture).\n\nGundagardi: Gundagardi (English: Hooliganism or rowdism) is a 1997 Indian Hindi-language film directed by V.Sai Prasad and produced by MC Bokadia starring Vijayashanti in the lead role.  Dharmendra is featured in a supporting role and Raj Babbar and Gulshan Grover star as the antagonists.  Aditya Pancholi, Ayub Khan and Simran make dynamic appearances in the film.  It didn't do well at the box office but its songs especially \"Bahar Baras Raha Hai Pani\" composed by Jatin Lalit were huge hits.  The film was dubbed in Telugu as \"Gunda Darbar\" and in Tamil as \"Thalaivi\".\n\nAnokhelal Mishra: Anokhelal Mishra (Hindi: अनोखेलाल मिश्रा ; 1914 10 March 1958) also spelled as Anokhe Lal Misra and commonly known as Pandit Anokhelalji was an Indian Tablā Artist who belonged to the Banaras Gharana of Hindustani classical music.\n\nShibban Lal Saxena: Shibban Lal Saxena (हिन्दी:- शिब्बन लाल सक्सेना) was a former Indian politician and Freedom Fighter.  He was son of late Shri Chhotey Lal Saxena.  He was born on 13 July 1906 to a wealthy Kayastha Family at Agra.\n\nQuestion: What is the premier date of the Indian Hindi-language film in which Saanand Verma plays the role of Anokhe Lal Saxena?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"production_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the production (e.g., film, serial).\"\n    },\n    \"production_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the production.\"\n    },\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"premier_date\": {\n      \"type\": \"string\",\n      \"description\": \"The date when the production premiered, in YYYY-MM-DD format if possible, otherwise as found in text.\"\n    }\n  },\n  \"required\": [\n    \"production_type\",\n    \"production_title\",\n    \"actor_name\",\n    \"character_name\",\n    \"premier_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "production_type": {
        "type": "string",
        "description": "The type of the production (e.g., film, serial)."
      },
      "production_title": {
        "type": "string",
        "description": "The title of the production."
      },
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "premier_date": {
        "type": "string",
        "description": "The date when the production premiered, in YYYY-MM-DD format if possible, otherwise as found in text."
      }
    },
    "required": [
      "production_type",
      "production_title",
      "actor_name",
      "character_name",
      "premier_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
