{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUmrika: Umrika is a 2015 Indian Hindi comedy-drama film written and directed by Prashant Nair, and produced by Swati Shetty and Manish Mundra.  It features Suraj Sharma, Tony Revolori, Smita Tambe, Rajesh Tailang, Pramod Pathak, Adil Hussain, Amit Sial, Sauraseni Maitra and Prateik Babbar.\n\nAnshai Lal: Anshai Lal is an Indian film director working in Hindi films since 2006.  His directorial debut Phillauri, starring Anushka Sharma, Diljit Dosanjh and Suraj Sharma released on 24 March 2017.\n\nBurn Your Maps: Burn Your Maps is a 2016 American adventure comedy-drama film written and directed by Jordan Roberts, based on the short story of the same name by Robyn Joy Leff.  The film stars Vera Farmiga, Jacob Tremblay, Suraj Sharma, Ramón Rodríguez, Virginia Madsen, and Marton Csokas.\n\nPrashant Nair: Prashant Nair is an Indian-born October 4 , 1973 French film director, screenwriter and producer best known for his 2015 feature film \"Umrika\", starring Suraj Sharma and Tony Revolori.\n\nList of accolades received by Life of Pi: \"Life of Pi\" is a 2012 American 3D adventure drama film based on Yann Martel's 2001 novel of the same name.  Directed by Ang Lee, the film is based on an adapted screenplay by David Magee, and stars Suraj Sharma, Irrfan Khan, Gérard Depardieu, Tabu, and Adil Hussain.\n\nLife of Pi: Life of Pi is a Canadian fantasy adventure novel by Yann Martel published in 2001.  The protagonist is Piscine Molitor \"Pi\" Patel, an Indian boy from Pondicherry who explores issues of spirituality and practicality from an early age.  He survives 227 days after a shipwreck while stranded on a lifeboat in the Pacific Ocean with a Bengal tiger named Richard Parker.\n\nPhillauri (film): Phillauri is a 2017 Indian Hindi fantasy comedy film directed by Anshai Lal and produced by Fox Star Studios with Anushka Sharma and her brother Karnesh Sharma under their banner of Clean Slate Films.  Director Navdeep Singh and writer Sudip Sharma are associated with the film as Creative Producers.  The film stars Anushka Sharma, Diljit Dosanjh, Suraj Sharma & Mehreen Pirzada in the lead roles.  The film's first official poster was released on February 3, 2017.  The film released on March 24, 2017.\n\nSuraj Sharma: Suraj Sharma (born 21 March 1993) is an Indian actor, who made his debut with 2012 film \"Life of Pi\".  Directed by Ang Lee, \"Life of Pi\" was adapted from the novel of the same nameand earned him critical acclaim as well as the BAFTA Rising Star Award nomination.  In 2014, he portrayed Aayan Ibrahim in season 4 of the Showtime series \"Homeland\".\n\nLife of Pi (film): Life of Pi is a 2012 American survival drama film based on Yann Martel's 2001 novel of the same name.  Directed by Ang Lee, the film's adapted screenplay was written by David Magee, and it stars Suraj Sharma, Irrfan Khan, Rafe Spall, Tabu, Adil Hussain, and Gérard Depardieu.  The storyline revolves around an Indian man named \"Pi\" Patel, telling a novelist about his life story, and how at 16 he survives a shipwreck in which his family dies, and is adrift in the Pacific Ocean on a lifeboat with a Bengal tiger.  The film had its worldwide premiere as the opening film of the 51st New York Film Festival at both the Walter Reade Theater and Alice Tully Hall in New York City on September 28, 2012.\n\nBeragee Bomb: Beragee Bomb is a 2013 comedy Meitei film directed by Oinam Gautam and written by Laishram Santosh.  It stars Gurumayum Bonny, Leishangthem Tonthoi, Loya, Suraj Sharma Laimayum and Edwin Soibam.  \"Beragee Bomb\" was released on 31 August 2013 at MFDC with a Red Carpet Event, hosted by WOL Media for the first time in Meitei cinema.  The official trailer of the film was released by WOL Media on 18 August 2013.  A sequel to the film titled \"Moreh Maru\" was produced by RT Motion Pictures and released in 2016.\n\nQuestion: Suraj Sharma was an actor in the movie that comes from a novel published in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"movie_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the movie.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the movie.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"novel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel the movie is based on.\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The publication year of the novel.\"\n        },\n        \"author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the novel.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publication_year\",\n        \"author\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"movie_details\",\n    \"novel_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "movie_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the movie."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the movie."
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "novel_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the novel the movie is based on."
          },
          "publication_year": {
            "type": "integer",
            "description": "The publication year of the novel."
          },
          "author": {
            "type": "string",
            "description": "The author of the novel."
          }
        },
        "required": [
          "title",
          "publication_year",
          "author"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "movie_details",
      "novel_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
