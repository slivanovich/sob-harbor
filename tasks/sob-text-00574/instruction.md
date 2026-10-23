{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFukrey: Fukrey (English: 'slacker' or 'worthless' ) is a 2013 Hindi coming of age comedy film directed by Mrighdeep Singh Lamba and starring Pulkit Samrat, Varun Sharma, Ali Fazal, Manjot Singh, Richa Chadda, Vishakha Singh, and Priya Anand in the lead roles.  The story and dialogues are written by Vipul Vig and the screenplay is written by Vig and Lamba.  Produced under the Excel Entertainment banner, the film was released on 14 June 2013.  Becoming a cult classic with time, the film went on to become a sleeper hit.\n\nJal (film): Jal (English: \"Water\") is a 2013 Hindi film which is set in the Rann of Kutch, India about an overconfident water diviner named Bakka, who tries to solve the drought problems in his village, but faces unforeseen circumstances when he tries to help a female bird watcher save flamingos.  The film is directed by Girish Malik and is his debut film as a director.\n\nAli Fazal: Ali Fazal (pronounced ] ; born 15 October 1986) is an Indian actor.  Born in Lucknow, he made his screen debut with a small role in the English language film \"The Other End of the Line\" (2008) before appearing in the American television miniseries \"Bollywood Hero\" (2009).\n\nMai (2013 film): Mai, meaning mother in Marathi, is a 2013 Hindi film which marks the debut of veteran singer Asha Bhosle as a lead actress.  The film is a family drama of how children abandon their ailing old parents.  The film is also debut directorial venture of Mahesh Kodiyal.\n\nMain Krishna Hoon: Main Krishna Hoon is a 2013 Hindi partly animated film directed by Rajiv S. Ruia which stars Juhi Chawla, Paresh Ganatra, and child artist Namit Shah as the primary cast and features real-life Hindi film superstars Hrithik Roshan and Katrina Kaif in guest appearances as themselves.  The Hindu god Lord Krishna appears as an animated character in this story, to help an orphaned boy also named Krishna.\n\nBhaag Milkha Bhaag (soundtrack): Bhaag Milkha Bhaag is the soundtrack album, by Shankar-Ehsaan-Loy, to the 2013 Hindi film of the same name, directed by Rakeysh Omprakash Mehra that stars Farhan Akhtar and Sonam Kapoor in the lead roles.  The album features eight tracks, and was released digitally on 14 June 2013.\n\nHuff! It's Too Much: Huff!  It's Too Much is a 2013 Hindi film.  It stars Pushkar Jog and Pakistani actress Armeena Khan.  The film was directed by Pushkar Jog himself and it released on 8 November 2013.\n\nShikha Joshi: Shikha Joshi was an Indian model turned actress who is known for her role in the 2013 Hindi film \"B.A. Pass\".\n\nRaanjhanaa (soundtrack): Raanjhanaa is the soundtrack album, composed by A. R. Rahman of the 2013 Hindi film of the same name, directed by Anand L. Rai and starring Dhanush, Sonam Kapoor and Abhay Deol in the lead roles.  The film is produced by Krishika Lulla under the banner Eros International.  The lyrics of the original version were written by Irshad Kamil whereas the Tamil lyrics were written by poet Vairamuthu.  The soundtrack album features nine original tracks.  The music of the original version of the soundtrack was released on the co-branded record labels Sony Music and Eros Music on 11 June 2013 and the Tamil version on 24 June 2013.\n\nSooper Se Ooper: Sooper Se Ooper is a 2013 Hindi film written & directed by Shekhar Ghosh under the banner of Reliance Entertainment and Jigsaw Pictures Pvt. Ltd.  The trailer of this movie was released on 27 September and the movie on 25 October.  The movie was a total washout.\n\nQuestion: What actor, born in Lucknow, starred in the 2013 Hindi film Fukrey?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"birthplace\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the actor was born.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actor starred in.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"birthplace\",\n    \"film_title\",\n    \"film_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "birthplace": {
        "type": "string",
        "description": "The city where the actor was born."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film the actor starred in."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "actor_name",
      "birthplace",
      "film_title",
      "film_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
