{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPhir Se...: Phir Se (English: \"Once Again\") is an upcoming Indian romance film, directed by Kunal Kohli and Ajay Bhuyan.  The film stars Kunal Kohli, Jennifer Winget and Sumona Chakravarti.  Rajit Kapoor, Dalip Tahil, Kanwaljeet Singh and Sushmita Mukherjee are in supporting roles.  This is the first film of director Kunal Kohli as an actor and also the debut film of Jennifer Winget.  The tagline of the film is \"I'm not 40—I'm 18 with 22 years experience.\"  The trailer was released on 7 April 2015.  Prior to \"Phir Se\", Kohli had directed \"Fanaa\", \"Hum Tum\", \"Mujhse Dosti Karoge! \" and \"Teri Meri Kahaani\".\n\nDamia Farooq: Damia Farooq is a Pakistani singer-songwriter and musician.  Starting her career at the age of thirteen in 2012, she released her debut album \"Damia Debut\" which consisted eight tracks including three music videos.  Later that year, she released her hit duet single \"Jana i miss you\" along with her elder sister, Parisa Farooq.  She appeared on many TV shows and interviews on various channels.  Since then, she has performed across the country and has done playback singing in drama serials such as \" Sun Yara \" (ARY Digital), \"Phir Se Meri Qismat Likh De\" (Hum Sitaray), \"Dil Mohalay Ki Haveli\" (Geo TV), \"Zindagi Mujhe Tera Pata Chahiye\" (PTV), \"Kis Se Kahoon\" (PTV) and many more.  Sang in films such as \"Ishq Positive\" , \"Blind Love\" (2016), \"Punjab Nahi Jaungi\" and many more.  In 2015, Damia launched her single \"Rab Janay\" and performed with the famous Romanian band Ex-Akcent TWO.  In 2016, Damia released her duet single \"Jhoomo\" with Parisa Farooq and months later marked her \"Coke Studio\" debut as the youngest featured artist in season 9, as a part team Faakhir.  Her latest hit, ARY digital's drama serial OST Sun Yara was nominated in the 16th Lux style awards 2017.\n\nSalman Iqbal: Salman Iqbal (Urdu: ‎ ) is a Pakistani media mogul.  He became the CEO of ARY Digital Network in 2014 after the death of Abdul Razzak Yaqoob.  In addition, Iqbal is the owner of the ARY Group, that was started by his Uncle Abdul Razzak Yaqoob and publisher of the Newsweek Middle East.\n\nARY News: ARY News (Urdu: ‎ ) is a Pakistani news channel launched on 26 September 2004.  A bilingual news channel in English and Urdu, it is a part of the ARY Digital Network, which is a subsidiary of ARY Group.  ARY is an acronym of Abdul Razzak Yaqoob, who was the owner of ARY Group.\n\nARY Films: ARY Films (Urdu: ‎ ) is a film distribution & production company in Pakistan, part of ARY Digital Network.  Thirty five films including 11 Urdu, 6 Punjabi and 17 Pashto films were released by ARY Films in 2013.  Among them, \"Waar\", \"Jawani Phir Nahi Ani\", \"Wrong No. \", \"Jalaibee\", \"3 Bahadur\" tops the charts in industry.\n\n2nd ARY Film Awards: The 2nd ARY Film Awards or AFA'16 ceremony, presented by the ARY Digital Network and Entertainment Channel, sponsored by Tang and L'Oréal, honored the best Pakistani films of 2015 and took place on April 16, 2016, at the Madinat Jumeirah, in Dubai, UAE, beginning at 7:30 UAE Standard Time.  The ceremony was held recorded and televised on May 7, 2016.  During the ceremony, the ARY Digital Network and Entertainment Channel presented ARY Film Awards (commonly referred to as AFAs) in 28 categories.  The ceremony was televised in the Pakistan by ARY Digital, and produced by Salma Iqbal and Jarjees Seja.\n\nARY Zauq: ARY Zauq was a 24-hour cooking channel from Pakistan.  It was part of the ARY Digital Network and was owned by ARY Group.  It featured programming about food and cooking including programmes about Pakistani cuisine and international cuisine.  ARY Zauq launched in 2009 and was available on Paksat 1 satellite at 38.0°E, free to air.  In its final years it also aired reruns of popular Pakistani programs from the ARY Digital vault.\n\nDobara Phir Se: Dobara Phir Se is a 2016 Pakistani romantic drama film directed by Mehreen Jabbar and a production of ARY Films.  The film is produced by Salman Iqbal and co-produced by Mohammad Jerjees Seja.  The film stars Ali Kazmi, Hareem Farooq, Adeel Hussain, Tooba Siddiqui, Sanam Saeed, Atiqa Odho, Shaz Khan, and child actor, Musa Khan.  The film was released on 25 November 2016.\n\n1st ARY Film Awards: The 1st ARY Film Awards or AFA'14 ceremony, presented by ARY Digital Network and Entertainment Channel, sponsored by Nokia, powered by ZONG and L'Oréal and took place on April 27, 2014 at the Golf Club, DHA Phase VIII, Karachi.  The ceremony was held recorded and televised on May 24, 2014.  During the ceremony ARY Digital Network and Entertainment Channel presented ARY Film Awards (commonly referred to as AFA's) in 29 categories and 4 special awards honoring the actors, technical achievements and films of 2013.  The ceremony, televised in Pakistan by ARY Digital and was produced by ARY Digital Network chairman Salman Iqbal.  ARY Film Awards became the most expensive event held in Pakistan.\n\nARY Film Award for Best Director: The ARY Film Award for Best Director (officially known as the ARY Film Award for Best Directing) is an award presented annually by the ARY Digital Network and Entertainment Channel.  It is given in honor of a film director who has exhibited outstanding directing while working in the film industry.  The 1st ARY Film Awards were held in 2014 and Bilal Lashari was given this award for his direction for \"Waar\".  Currently, nominees are determined by single transferable vote within the directors branch of ARY Digital Network while winners are selected by a public voting.\n\nQuestion: Who co-produced Dobara Phir se with the CEO of ARY Digital Network?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"main_producer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the main producer.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role or title of the main producer.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"co_producer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-producer.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"main_producer\",\n    \"co_producer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "main_producer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the main producer."
          },
          "role": {
            "type": "string",
            "description": "The role or title of the main producer."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "co_producer_name": {
        "type": "string",
        "description": "The name of the co-producer."
      }
    },
    "required": [
      "film_title",
      "main_producer",
      "co_producer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
