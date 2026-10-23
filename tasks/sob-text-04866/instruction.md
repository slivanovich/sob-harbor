{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHenry V (play): Henry V is a history play by William Shakespeare, believed to have been written around 1599.  It tells the story of King Henry V of England, focusing on events immediately before and after the Battle of Agincourt (1415) during the Hundred Years' War.  In the First Quarto text, it was entitled \"The Cronicle History of Henry the fift\", which became \"The Life of Henry the Fifth\" in the First Folio text.\n\nJohn of Lancaster, 1st Duke of Bedford: John of Lancaster, 1st Duke of Bedford, KG (20 June 138914 September 1435) was the third surviving son of King Henry IV of England by Mary de Bohun, brother to King Henry V, and acted as regent of France for his nephew, King Henry VI.\n\nSuite from Henry V: Suite from Henry V is a 1963 orchestral arrangement of William Walton's musical score from the 1944 film \"Henry V\".  The suite, arranged by Muir Mathieson, is in five movements, although the second and fourth movements had already appeared in string arrangement form in Walton's own Two Pieces for Strings from Henry V.\n\nMontjoy: Montjoy is a herald, or royal messenger, of the French King in William Shakespeare's play \"Henry V\".  His job is to convey the King of France (King \"Charles VI\" )'s messages, including the constable 's harsh message to King Henry.  However, he conveys them in such a polite and respectable way that King Henry thinks on him favourably; an example of this can be seen when King Henry tips him when he has conveyed a message.\n\nLaurence Olivier: Laurence Kerr Olivier, Baron Olivier, {'1': \", '2': \", '3': \", '4': \"} ( ; 22 May 1907 – 11 July 1989) was an English actor and director who, along with his contemporaries Ralph Richardson and John Gielgud, dominated the British stage of the mid-20th century.  He also worked in films throughout his career, playing more than fifty cinema roles.  Late in his career, he had considerable success in television roles.\n\nThomas Erpingham: Sir Thomas Erpingham KG (  1355 –1428) was an English knight who became famous as the commander of King Henry V's longbow wielding archers at the Battle of Agincourt.  He was immortalised as a character in the play \"Henry V\" by William Shakespeare.  It is, however, his lengthy and loyal service to John of Gaunt, Henry IV and Henry V, which contributed significantly to the establishment of the House of Lancaster upon the English throne, that is his true legacy.\n\nHenry V (1989 film): Henry V is a 1989 British historical drama film adapted for the screen and directed by Kenneth Branagh, based on William Shakespeare's play of the same name about King Henry V of England.  The film stars Branagh in the title role with Paul Scofield, Derek Jacobi, Ian Holm, Emma Thompson, Alec McCowen, Judi Dench, Robbie Coltrane, Brian Blessed, and Christian Bale in supporting roles.\n\nRevival of the Heresy Acts: In November 1554, the Revival of the Heresy Acts (1 & 2 Ph. & M. c.6) revived three former Acts against heresy; the letters patent of 1382 of King Richard II, an Act of 1401 of King Henry IV, and an Act of 1414 of King Henry V.  All three of these laws had been repealed under King Henry VIII and King Edward VI. \n\nHenry V (1944 film): Henry V is a 1944 British Technicolor film adaptation of William Shakespeare's play of the same name.  The on-screen title is The Chronicle History of King Henry the Fift with His Battell Fought at Agin Court in France (the title of the 1600 quarto edition of the play).  It stars Laurence Olivier, who also directed.  The play was adapted for the screen by Olivier, Dallas Bower, and Alan Dent.  The score is by William Walton.\n\nDual monarchy of England and France: The dual monarchy of England and France existed during the latter phase of the Hundred Years' War when Charles VII of France and Henry VI of England disputed the succession to the throne of France.  It commenced on 21 October 1422 upon the death of King Charles VI of France, who had signed the Treaty of Troyes which gave the French crown to his son-in-law Henry V of England and Henry's heirs.  It excluded King Charles's son, the Dauphin Charles, who by right of primogeniture was the heir to the Kingdom of France.  Although the Treaty was ratified by the Estates-General of France, the act was a contravention of the French law of succession which decreed that the French crown could not be alienated.  Henry VI, son of Henry V, became king of both England and France and was recognized only by the English and Burgundians until 1435 as King Henry II of France.  He was crowned King of France on 16 December 1431.\n\nQuestion: Who wrote the original play which was later turn into a 1944 film about King Henry V and starred and was directed by an English actor born in 1907?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"play_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the original play.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the original play.\"\n        },\n        \"writing_year_approx\": {\n          \"type\": \"integer\",\n          \"description\": \"The approximate year the play was written.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"author\",\n        \"writing_year_approx\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_adaptation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film adaptation.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film adaptation.\"\n        },\n        \"star_actor\": {\n          \"type\": \"string\",\n          \"description\": \"The main actor starring in the film adaptation.\"\n        }\n      },\n      \"required\": [\n        \"film_year\",\n        \"director\",\n        \"star_actor\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author of the original play.\"\n    }\n  },\n  \"required\": [\n    \"play_details\",\n    \"film_adaptation_details\",\n    \"actor_details\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "play_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the original play."
          },
          "author": {
            "type": "string",
            "description": "The author of the original play."
          },
          "writing_year_approx": {
            "type": "integer",
            "description": "The approximate year the play was written."
          }
        },
        "required": [
          "title",
          "author",
          "writing_year_approx"
        ],
        "additionalProperties": false
      },
      "film_adaptation_details": {
        "type": "object",
        "properties": {
          "film_year": {
            "type": "integer",
            "description": "The release year of the film adaptation."
          },
          "director": {
            "type": "string",
            "description": "The director of the film adaptation."
          },
          "star_actor": {
            "type": "string",
            "description": "The main actor starring in the film adaptation."
          }
        },
        "required": [
          "film_year",
          "director",
          "star_actor"
        ],
        "additionalProperties": false
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the actor."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The name of the author of the original play."
      }
    },
    "required": [
      "play_details",
      "film_adaptation_details",
      "actor_details",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
