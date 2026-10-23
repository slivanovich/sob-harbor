{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Pappas: John Pappas (born November 11, 1951) is an American actor, playwright and former comic who has appeared on television and in film since the 1970s.  Pappas is best known for his recurring role as \"Pappas\" on the television series Hardball (NBC 1989-1990).  Pappas is also known for his recurring role of Leo Sullivan on the NBC Soap Opera \"Days of Our Lives\" (NBC1994).  In 2001 Pappas returned to \"Days of Our Lives\" in another recurring role of a convict named \"Buddy\".  Pappas is an award-winning actor receiving a 1990 best actor award from the L.A. Weekly, for his performance in Gilbert Girion’s BAD COUNTRY.  He received 2 Drama-Logue awards, one in 1989 and another in 1988.\n\n+1 (film): +1 (also known as Plus One and Shadow Walkers) is a 2013 American science fiction-horror film directed by Dennis Iliadis.  It premiered on March 10, 2013, at SXSW and stars Ashley Hinshaw, Rhys Wakefield, and Natalie Hall. \" +1\" was released in theaters, iTunes, and VOD on September 20, 2013.  For the VOD release Iliadis worked on fine-tuning elements of the film, as he felt that the SXSW release was too \"rushed\".\n\nThe Return of Doctor X: The Return of Doctor X (also billed as The Return of Dr. X) is a 1939 American science fiction-horror film directed by Vincent Sherman and starring Wayne Morris, Rosemary Lane, and Humphrey Bogart as the title character.  It was based on the short story \"The Doctor's Secret\" by William J. Makin.  Despite supposedly being a sequel to \"Doctor X\" (1933), also produced by Warner Bros., the films are unrelated.\n\nRob Morgan (actor): Rob Morgan is an American actor best known for his roles in Netflix series, most notably Turk Barrett in \"Daredevil\" and \"Luke Cage\", as well as his recurring roles in \"Stranger Things\" and the upcoming limited series \"Godless\" in 2017.\n\nZaat: Zaat (also known as The Blood Waters of Dr. Z, Hydra, and Attack of the Swamp Creatures) is a 1971 American science fiction-horror film that was written, produced, and directed by Don Barton.  It gained significant exposure when it was used in an episode of movie-mocking television series \"Mystery Science Theater 3000\" in May 1999.\n\nThe Mist (TV series): The Mist is an American science fiction-horror thriller television series developed by Christian Torpe for Spike.  It is based on the horror novella of the same name by author Stephen King.  The first season, consisting of ten episodes, premiered on June 22, 2017.  On September 27, 2017, Spike cancelled the series after one season.\n\nThe Frankenstein Syndrome: The Frankenstein Syndrome (originally titled The Prometheus Project) is a 2011 American science fiction-horror film written and directed by Sean Tretta.  Scott Anthony Leet stars as a murdered security guard who is reanimated by a research institute in the tradition of Mary Shelley's novel \"Frankenstein\".  It was released directly to DVD.\n\nThe Fly (1958 film): The Fly is a 1958 American science fiction-horror film produced and directed by Kurt Neumann.  The screenplay by James Clavell was based on the 1957 short story of the same name by George Langelaan.  The film stars David Hedison, Patricia Owens, Vincent Price and Herbert Marshall.\n\nStranger Things: Stranger Things is an American science fiction-horror web television series created, written, directed and co-executive produced by the Duffer Brothers, as well as co-executive-produced by Shawn Levy and Dan Cohen.  The first season stars Winona Ryder, David Harbour, Finn Wolfhard, Millie Bobby Brown, Gaten Matarazzo, Caleb McLaughlin, Natalia Dyer, Charlie Heaton, Cara Buono, and Matthew Modine, with Noah Schnapp and Joe Keery in recurring roles.  The second season will see Schnapp and Keery promoted to series regulars, along with the addition of Sadie Sink and Dacre Montgomery.\n\nLexa Doig: Alexandra Lecciones \"Lexa\" Doig (born June 8, 1973) is a Canadian actress.  She portrayed the title role in the 2000–05 Canadian-American science fiction-adventure television series \"Andromeda\".  She also portrayed the female lead role of Rowan in the science fiction-horror movie \"Jason X\" (2001), the 10th installment of the \"Friday the 13th\" film series.\n\nQuestion: Rob Morgan is best known for his recurring role in an American science fiction-horror web television series reated, written, directed and co-executive produced by who? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the television series.\"\n    },\n    \"series_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the television series.\"\n    },\n    \"creators\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The individuals or groups credited with creating, writing, directing, and co-executive producing the series.\"\n    },\n    \"production_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The specific production roles held by the creators for the series.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"series_name\",\n    \"series_genre\",\n    \"creators\",\n    \"production_roles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "series_name": {
        "type": "string",
        "description": "The name of the television series."
      },
      "series_genre": {
        "type": "string",
        "description": "The genre of the television series."
      },
      "creators": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The individuals or groups credited with creating, writing, directing, and co-executive producing the series."
      },
      "production_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The specific production roles held by the creators for the series."
      }
    },
    "required": [
      "actor_name",
      "series_name",
      "series_genre",
      "creators",
      "production_roles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
