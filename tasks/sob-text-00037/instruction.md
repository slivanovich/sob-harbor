{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJoshua Lynn: Joshua Lynn (born December 14, 1969, in Santa Barbara, California) was the Chief Trial Deputy of Santa Barbara County, Santa Barbara, California from 2008 to 2010.  He was the lead prosecuting attorney in the trial of Jesse James Hollywood, who was convicted and sentenced to Life in Prison on February 5, 2010.\n\nSantana Andrade: Santana Andrade is a fictional character from the American soap opera \"Santa Barbara\".  She was first portrayed by actress Ava Lazar from July 30 to December 5, 1984.  Margaret Michaels portrayed the role from April 26 to October 2, 1985 and was soon replaced by actress Gina Gallego, who portrayed the role the longest out of four actresses.  She played the role from October 3, 1985 to April 10, 1987 and returned for a short stint from November 13 to November 20, 1989.  Wanda De Jesus was the final actress to play the role, from July 19, 1991 to May 28, 1992.\n\nWilbur Jacobs: Wilbur R. Jacobs (June 30, 1918 – June 15, 1998) was an American historian, with a special interest in Native American, Western, and Environmental history.  Born in Chicago, Illinois in 1918, Jacobs moved west at a young age and settled in the Los Angeles area.  He started college at Pasadena City College, then earned his B.A. (1940) and M.A. (1942) in History at the University of California, Los Angeles.  After military service during World War II, Jacobs started doctoral study at Johns Hopkins University, but decided to return to UCLA to pursue Western Frontier history under the direction of Lewis Knott Koontz.  He finished his doctorate in 1947 and then taught Western Civilization at Stanford University for two years, before accepting a call to the History program at the University of California, Santa Barbara (known at that time as the University of California, Santa Barbara College).  At the University of California, Santa Barbara, Jacobs served as a founding member of the History Department and also served as Department Chair from 1961-1964.\n\nMark McCormick: Dr. Marcus \"Mark\" Aurelius McCormick is a fictional character from the American soap opera \"Santa Barbara\", portrayed by American actor Jon Lindstrom from November 14, 1985 to July 30, 1986.  Even though he didn't reappear later, his character's death was an instrumental storyline during 1988.\n\nJon Lindstrom: Jon Lindstrom (born October 18, 1957) is an American actor, writer, director, producer, and musician.  He is well known for his role as Kevin Collins on the ABC Daytime soap opera \"General Hospital\" and its spin-off \"Port Charles\".\n\nDimitrije Đorđević (historian): Dimitrije \"Mita\" Đorđević (Serbian: Димитрије Ђорђевић ; 27 February 1922 – 5 March 2009) was a widely published historian of Modern European history, especially of the Balkans.  Đorđević was born in Belgrade to a prominent Serbian family.  When he was a law student, the Germans invaded Yugoslavia during World War II and he joined the resistance movement of Dragoljub Mihailovic.  Đorđević was captured by the Germans and was imprisoned, ultimately in Mauthausen-Gusen concentration camp in Austria.  He survived the war, but was in turn imprisoned by the communist regime in post World War II Yugoslavia.  After he was pardoned and released, Đorđević was eventually allowed to commence study at the University of Belgrade, where he was a student of Vaso Čubrilović (one of the members of the Young Bosnia who conspired to assassinate Franz Ferdinand which led to the outbreak of World War I).  Đorđević was awarded his doctorate in 1962.  In 1970, Đorđević took up a position as a Full Professor of History at the University of California, Santa Barbara, joining a strong faculty in European History including Joachim Remak, Leonard Marsak, and C. Warren Hollister.  He was elected a member of the Serbian Academy of Science and Arts in 1985.  A popular undergraduate lecturer and graduate mentor at the University of California, Santa Barbara, in 1992 many of his former students contributed to his \"Festschrift\" entitled \"Scholar, Patriot, Mentor: Historical Essays in Honor of Dimitrije Djordjevic\".  In retirement, Đorđević published his autobiography, \"Scars and Memory: Four Lives in One Lifetime\", describing his World War II and post World War II experiences.  Professor Đorđević died in Santa Barbara on March 5, 2009.\n\nMichael Brainard: Michael Brainard (born November 23, 1965 in Hollywood, California, United States) is an American actor most notable for his role as the second Ted Capwell on NBC's soap opera \"Santa Barbara\".  He portrayed the role from 1991 to 1993.  He also portrayed Dr. Jake Martin on an ABC soap, \"All My Children\", from 1988 to 1991, prior to joining \"Santa Barbara\".\n\nSanta Barbara (TV series): Santa Barbara is an American television soap opera that aired on NBC from July 30, 1984 to January 15, 1993.  The show revolves around the eventful lives of the wealthy Capwell family of Santa Barbara, California.  Other prominent families featured on the soap were the rival Lockridge family, and the more modest Andrade and Perkins families.\n\nPeter Flint: Peter Flint is a fictional character from the American soap opera \"Santa Barbara\".  He was portrayed by American actor Stephen Meadows from July 30, 1984 to February 28, 1985.  Meadows returned in a cameo on April 11, 1986.\n\nRaghavan N. Iyer: Raghavan Narasimhan Iyer (born 10 March 1930) was an Indian academic, political theorist and philosopher.  Educated at Oxford, he was professor of political science at the University of California, Santa Barbara from 1965 to 1986, when he retired as professor emeritus.  A founder member of the Santa Barbara branch of the United Lodge of Theosophists, he co-founded the Institute of World Culture in Santa Barbara in 1976, and remained its president until 1986.\n\nQuestion: In what year was the actor who portrayed Mark McCormick in \"Santa Barbara\" from November 14, 1985 to July 30, 1986 born?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"character\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the fictional character.\"\n        },\n        \"tv_series\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the TV series the character appeared in.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"tv_series\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who portrayed the character.\"\n        },\n        \"role_start_date\": {\n          \"type\": \"string\",\n          \"description\": \"The start date of the actor's portrayal of the character.\"\n        },\n        \"role_end_date\": {\n          \"type\": \"string\",\n          \"description\": \"The end date of the actor's portrayal of the character.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_start_date\",\n        \"role_end_date\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the actor who portrayed the character.\"\n    }\n  },\n  \"required\": [\n    \"character\",\n    \"actor\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "character": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the fictional character."
          },
          "tv_series": {
            "type": "string",
            "description": "The name of the TV series the character appeared in."
          }
        },
        "required": [
          "name",
          "tv_series"
        ],
        "additionalProperties": false
      },
      "actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor who portrayed the character."
          },
          "role_start_date": {
            "type": "string",
            "description": "The start date of the actor's portrayal of the character."
          },
          "role_end_date": {
            "type": "string",
            "description": "The end date of the actor's portrayal of the character."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the actor."
          }
        },
        "required": [
          "name",
          "role_start_date",
          "role_end_date",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "integer",
        "description": "The birth year of the actor who portrayed the character."
      }
    },
    "required": [
      "character",
      "actor",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
