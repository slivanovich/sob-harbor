{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFriend Request: Friend Request (released overseas as Unfriend) is a 2016 English-language German supernatural-psychological horror film directed by Simon Verhoeven and written by Verhoeven, Matthew Ballen, and Philip Koch.  The film stars Alycia Debnam-Carey, William Moseley, Connor Paolo, Brit Morgan, Brooke Markham, Sean Marquette, Liesl Ahlers, and Shashawnee Hall.  It was released by Warner Bros.  Pictures on 7 January 2016 in Germany and 22 September 2017 in the United States by Entertainment Studios Motion Picutres.\n\nRosalie Goes Shopping: Rosalie Goes Shopping is a 1989 English-language German film directed by Percy Adlon and starring Marianne Sägebrecht, Brad Davis, and Judge Reinhold.\n\nAlycia Debnam-Carey: Alycia Jasmin Debnam-Carey (born 20 July 1993) is an Australian actress, best known for her role as Commander Lexa in The CW series \"The 100\" and her portrayal of Alicia Clark on the AMC series \"Fear the Walking Dead\" (the companion series to \"The Walking Dead).\"  Debnam-Carey has also starred in the 2014 films \"Into the Storm\" and \"The Devil's Hand\", and appeared in the television series \"McLeod's Daughters\", \"Dream Life\", and \"Next Stop Hollywood\".  In 2016, she starred in the German film \"Friend Request\".\n\nThe Last Station: The Last Station is a 2009 English-language German biographical drama film written and directed by Michael Hoffman, and based on Jay Parini's 1990 biographical novel of the same name, which chronicled the final months of Leo Tolstoy's life.  The film stars Christopher Plummer as Tolstoy and Helen Mirren as his wife Sofya Tolstaya.  The film is about the battle between Sofya and his disciple Vladimir Chertkov for his legacy and the copyright of his works.  The film premiered at the 2009 Telluride Film Festival.\n\nFremde Haut: Fremde Haut is a 2005 German film.  It was directed by Angelina Maccarone and stars Jasmin Tabatabai, Anneke Kim Sarnau, and Navíd Akhavan.  Its English title is Unveiled.\n\nAditya Om: Aditya Om (born 5 October 1980) is an Indian film actor, writer, lyricist, director and producer and well known star in Telugu movies.  He also did theatre and serials.  He starred in \"Lahiri Lahiri Lahirilo \" (2002) as a main lead.  He has done more than 25 films as a leading actor in Telugu films (South Indian Films).  He has directed critically acclaimed film \"Bandook\" and Silent film \"Mr Lonely Miss lovely\".  His short films \"Maya Mobile\" and \"For my mother\" were widely appreciated.  As an associate producer he was involved in critically acclaimed feature films \"Shudra\" and \"Dozakh, in search of heaven\".  Aditya Om just completed his art film in English language \"The Dead End\" and presently working on \"Friend request\" a bilingual Hindi-Telugu film.  His Next release Film Alif as an Actor.\n\nTarzan (2013 film): Tarzan (also known as Tarzan 3D) is a 2013 English-language German 3D computer-animated motion capture action-adventure film written, directed and produced by German producer Reinhard Klooss which was released on October 17, 2013 in Russia.  The film was released across early 2014 in other countries.  The film stars the voices of Kellan Lutz, Spencer Locke, Anton Zetterholm, Mark Deklin, Joe Cappelletti, and Jaime Ray Newman.  The screenplay was written by Reinhard Klooss, Jessica Postigo and Yoni Brenner.  The film is based on the classic book \"Tarzan of the Apes\" (1912) by Edgar Rice Burroughs, and is one of many adaptations.  The film received predominantly negative reviews from critics, who panned the film's storyline and animation and grossed $44 million worldwide.  \"Tarzan\" was released on DVD and Blu-ray on August 5, 2014 by Highlight Film.\n\nKokowääh 2: Kokowääh 2 is a 2013 German film directed by Til Schweiger.  It is a sequel to the 2011 film \"Kokowääh\".  It was released in German–speaking countries (Germany, Austria and Switzerland) on 7 February 2013.  The film stars Til Schweiger, his daughter Emma Tiger Schweiger, Jasmin Gerat and Samuel Finzi reprising their roles from the first film.\n\nKokowääh: Kokowääh is a 2011 German film directed by Til Schweiger.  It was released in German–speaking countries (Germany, Austria and Switzerland) on 3 February 2011.  The film stars Til Schweiger, his daughter Emma Tiger Schweiger, Jasmin Gerat and Samuel Finzi.  Another of Schweiger's daughters, Luna Schweiger, makes a small appearance in the film.  \"Kokowääh\" is an onomatopoetic depiction of the French pronunciation of coq au vin.  A sequel, \"Kokowääh 2\", was released on 7 February 2013 with Schweiger having returned as director, co-writer and producer.\n\nFriend Request Pending: Friend Request Pending is a 2011 short comedy drama film written and produced by Chris Croucher and directed by Chris Foggin.  It stars Judi Dench, Tom Hiddleston, and Philip Jackson.  It was included in the feature film \"Stars in Shorts\".\n\nQuestion: Alycia Jasmin Debnam-Carey, is an Australian actress, in 2016, she starred in the German film \"Friend Request\", an English-language German supernatural-psychological horror film, directed by who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the film was released.\"\n        },\n        \"language\": {\n          \"type\": \"string\",\n          \"description\": \"The primary language(s) of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"language\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"starring_actress\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress mentioned in the question.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actress.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"director_name\",\n    \"starring_actress\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          },
          "language": {
            "type": "string",
            "description": "The primary language(s) of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "language",
          "genre"
        ],
        "additionalProperties": false
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "starring_actress": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress mentioned in the question."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actress."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_details",
      "director_name",
      "starring_actress"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
