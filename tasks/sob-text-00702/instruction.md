{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTakkabur: Takabbur is a Pakistani drama serial being telecast on A-Plus Entertainment TV channel in Pakistan.  It is written by Shahzad Javed and Nooran Makhdoom and produced by Six Sigma Entertainment.\n\nDaddy (drama): Daddy is a Pakistani drama serial which premiered on ARY Digital on 13 November 2010 and ended on 5 February in the following year.  The serial is produced by Samina Humayun Saeed's Production house Six Sigma Productions, written by Ali Imran, directed by Misbah Khalid.\n\nPyarey Afzal: Pyarey Afzal or Pyaare Afzal (Urdu: ‎ ) ( English: \"Dear Afzal\" ) is a Pakistani romantic drama serial that aired on ARY Digital, directed by Nadeem Baig, written by Khalil-ur-Rehman Qamar and production of Six Sigma Entertainment.  The drama starred Hamza Ali Abbasi and Ayeza Khan in lead roles.\n\nDurr-e-Shehwar: Durr-e-Shehwar (Urdu: ‎ ) is a Urdu language Pakistani telenovela written by Umera Ahmed and directed by Haissam Hussain.  First broadcast in Pakistan by Hum TV, \"Durr-e-Shehwar\", which premiered in Pakistan on 10 March 2012, has been produced by Momina Duraid and Six Sigma Entertainment.  The telenovela, which featured actors Sanam Baloch, Qavi Khan, Samina Peerzada, Noman Ejaz, and Nadia Jamil, in the lead roles, ended its run in Pakistan on 16 June 2012, after airing 15 episodes.\n\nJawani Phir Nahi Ani: Jawani Phir Nahi Ani is a 2015 Pakistani adventure and comedy film directed by Nadeem Beyg.  It was co-produced by Humayun Saeed, Salman Iqbal and Shahzad Nasib at Saeed's production house, Six Sigma Plus.  The film stars Humayun Saeed, Hamza Ali Abbasi, Ahmad Ali Butt, Vasay Chaudhry, Mehwish Hayat and Sohai Ali Abro.  The supporting cast includes Javed Sheikh, Ismail Tara, Bushra Ansari, Ayesha Khan, Sarwat Gillani and Uzma Khan.  The film is about a single man who is a divorce lawyer.  He takes his three married friends on a trip to help them escape their wives.\n\nInteha (1999 film): Inteha (Urdu: ‎ ) is a Pakistani Urdu film which was released in 1999 across theaters in Pakistan.  The movie was Samina Peerzada's debut directorial attempt and established the careers of its two leading men Humayun Saeed and Zeeshan Sikander.  The actors, incidentally, made their debuts with \"Inteha\".\n\nSix Sigma Entertainment: Six Sigma Entertainment is a Pakistani film and television production house which is owned by Shahzad Nasib and his friend and well known actor Humayun Saeed.  On 9 December 2015; Humayun Saeed announced that the Company will be collaborating with the renowned Play writer Khalil-ur-Rehman Qamar, where the writer will be exclusively writing for Six Sigma Productions.  Khalil will be writing for the production company's upcoming film Punjab Nahi Jaungi, Nadeem Beyg is expected to direct the film.\n\nYNH Films: Yasir-Nida-Hassan Films stylized as YNH Films is a Pakistani film production house founded by actors, Yasir Nawaz, Nida Yasir and Hassan Zia.  In 2015, YNH Films released its debut picture, \"Wrong No. \", that became a commercial and financial success and went onto become the 8th highest-grossing Pakistani film of all time.  directed by Yasir Nawaz it was also produced by Yasir Nawaz\n\nHumayun Saeed: Humayun Saeed (born Humayun Saeed Ansari: 27 July 1971) is a Pakistani film/television actor and producer.  Saeed is also a co-founder of the media production house Six Sigma Entertainment Plus which produces television drama serials and commercial movies.  He has appeared in dozens of Pakistani television dramas and limited number of films, and earned numerous accolades, including Lux Style Awards and ARY Film Awards Saeed Enjoys substantial fan following in Pakistan since the beginning of his career and was often ranked amongst the highest paid TV actors of his time.\n\nKhalil-ur-Rehman Qamar: Khalil-ur-Rehman Qamar (Urdu: خلیل الرحمان قمر‎ ) is a playwright for Pakistani television.  His notable work includes \"Boota from Toba Tek Singh\", aired from PTV World, and \"Landa Bazar\", aired on PTV.  His recent work \"Pyarey Afzal\" and \"Sadqay Tumhare\" are among his dramas.  On 9th December 2015, Humayun Saeed, one of the co-founders of Six Sigma Entertainment, announced that Khalil will be exclusively writing for his production company.\n\nQuestion: Inteha established the career of what Pakistani film/television actor who is the co-founder of the media production house Six Sigma Entertainment Plus?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Pakistani film/television actor.\"\n    },\n    \"career_established_by_film\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film that established the actor's career.\"\n    },\n    \"is_co_founder_of_six_sigma_entertainment_plus\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the actor is a co-founder of Six Sigma Entertainment Plus.\"\n    },\n    \"production_house_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the production house co-founded by the actor.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"career_established_by_film\",\n    \"is_co_founder_of_six_sigma_entertainment_plus\",\n    \"production_house_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the Pakistani film/television actor."
      },
      "career_established_by_film": {
        "type": "string",
        "description": "The name of the film that established the actor's career."
      },
      "is_co_founder_of_six_sigma_entertainment_plus": {
        "type": "boolean",
        "description": "Indicates if the actor is a co-founder of Six Sigma Entertainment Plus."
      },
      "production_house_name": {
        "type": "string",
        "description": "The name of the production house co-founded by the actor."
      }
    },
    "required": [
      "actor_name",
      "career_established_by_film",
      "is_co_founder_of_six_sigma_entertainment_plus",
      "production_house_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
