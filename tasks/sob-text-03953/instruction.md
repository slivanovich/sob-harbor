{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWest Is West (2010 film): West Is West is a 2010 British comedy-drama film, which is a sequel to the 1999 comedy \"East Is East\".  It stars Om Puri, Linda Bassett, Aqib Khan, Ila Arun and Jimi Mistry, is written by Ayub Khan-Din, directed by Andy DeEmmony, and produced by Leslee Udwin for Assassin Films and BBC Films.\n\nA Room for Romeo Brass: A Room for Romeo Brass is a 1999 British comedy-drama film directed and written by Shane Meadows.  It was co-written by frequent Meadows collaborator Paul Fraser.  Filming began in September 1998.\n\nJimmi Harkishin: Jimmi Harkishin (born Rajan Harkinshindas, March 1965) is a French-born British actor best known for his role as shopkeeper Dev Alahan in \"Coronation Street\", which he has played since November 1999.  He's also been featured in the film \"East is East\" as well as \"Bhaji on the Beach\".  He played Gary Dunn in the \"Jonathan Creek\" episode \"Danse Macabre\".\n\nIdiot (1992 film): Idiot is a 1992 Hindi film based on Fyodor Dostoevsky's novel, \"The Idiot\".  It was directed by Mani Kaul and starred Shah Rukh Khan and Ayub Khan-Din.  The film debuted at the New York Film Festival in October 1992.  In this version of the tale, placed in contemporary Mumbai, Prince Miskin (Khan-Din) is a man whose epilepsy is mistaken for idiocy.\n\nAmar Akbar &amp; Tony: Amar Akbar & Tony is a 2015 British comedy-drama film written and directed by Atul Malhotra.  \"Amar Akbar & Tony\" is an independent British feature film.  The film will feature Rez Kempton, Sam Vincenti and Martin Delaney in the lead roles.\n\nDev Alahan: Devendra \"Dev\" Alahan is a fictional character from the British ITV soap opera, \"Coronation Street\".  Portrayed by Jimmi Harkishin, the character first appeared onscreen during the episode airing on 10 November 1999.  He is the ex-husband of Sunita (Shobna Gulati), and father to Amber Kalirai (Nikki Patel), Aadi Alahan (Zennon Ditchett) and Asha Alahan (Tanisha Gorey), though Amber is not Sunita's daughter.  Dev departed on 13 February 2015, after Harkishin asked for an extended break from the show, Dev returned on 1 June 2015.\n\nMansfield Park (film): Mansfield Park is a 1999 British romantic comedy-drama film based on Jane Austen's novel of the same name, written and directed by Patricia Rozema.  The film departs from the original novel in several respects.  For example, the life of Jane Austen is incorporated into the film, as well as the issues of slavery and plantation life.  The majority of the film was made at Kirby Hall in Northamptonshire.\n\nEast Is East (1999 film): East Is East is a 1999 British comedy-drama film written by Ayub Khan-Din and directed by Damien O'Donnell.  It is set in Salford, Lancashire, in 1971, in a mixed-ethnicity British household headed by Pakistani father George (Om Puri) and an English mother, Ella (Linda Bassett).\n\nAnother Year (film): Another Year is a 2010 British comedy-drama film written and directed by Mike Leigh, starring Lesley Manville, Jim Broadbent, and Ruth Sheen.  It premiered at the 2010 Cannes Film Festival in competition for the Palme d'Or.  The film was shown at the 54th London Film Festival before its general British release date on 5 November 2010.  At the 83rd Academy Awards, Mike Leigh was nominated for an Academy Award for Best Original Screenplay.\n\nAll in Good Time (film): All in Good Time is a British film directed by Nigel Cole.  It is based on Ayub Khan-Din's 2007 play \"Rafta, Rafta,\" which itself was based on a 1963 play and 1966 film by Bill Naughton, \"All in Good Time\" and \"The Family Way.\"\n\nQuestion: Which of the film in which Jimmi Harkishin was featured is a 1999 British comedy-drama film written by Ayub Khan-Din and directed by Damien O'Donnell?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"film_type\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the film's type, e.g., 'British comedy-drama film'.\"\n    },\n    \"writer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the film's writer.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the film's director.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"featured_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor featured in the film, specifically Jimmi Harkishin.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"film_type\",\n    \"writer\",\n    \"director\",\n    \"featured_actor\"\n  ],\n  \"additionalProperties\": false\n}"
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
        "description": "The year the film was released."
      },
      "film_type": {
        "type": "string",
        "description": "A description of the film's type, e.g., 'British comedy-drama film'."
      },
      "writer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the film's writer."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "director": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the film's director."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "featured_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actor featured in the film, specifically Jimmi Harkishin."
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
      "film_type",
      "writer",
      "director",
      "featured_actor"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
