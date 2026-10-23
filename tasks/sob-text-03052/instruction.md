{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOn the Silver Globe (film): On the Silver Globe (Polish: \"Na srebrnym globie\" ) is a Polish film premiered in 1988, directed by Andrzej Żuławski and adapted from a novel by Jerzy Żuławski.\n\nRosebud (film): Rosebud is a 1975 film directed by Otto Preminger, and starring Peter O'Toole, Richard Attenborough, and Peter Lawford.  The script was by Otto's son, Erik Lee Preminger, based on the novel by Joan Hemingway and .  Originally the film was set to star Robert Mitchum, but he left after disagreements with Preminger.  Kim Cattrall made her film début as a teenager.  Barbara Emerson, who had been cast as one of the girls, was replaced during production.\n\nIngo Preminger: Ingwald \"Ingo\" Preminger (25 February 1911 in Czernowitz, Austria-Hungary (now Chernivtsi, Ukraine) – 7 June 2006 in Pacific Palisades, California) was a film producer.  He was also the literary agent for several writers, including Dalton Trumbo and Ring Lardner Jr., both of whom were blacklisted in the McCarthy era.  He was brother of actor-director-producer Otto Preminger.\n\nAndrzej Żuławski: Andrzej Żuławski (] ; 22 November 1940 – 17 February 2016) was a Polish film director and writer.  He was born in Lwów, Poland (now Ukraine).  Żuławski often went against mainstream commercialism in his films, and enjoyed success mostly with European art-house audiences.\n\nPossession (1981 film): Possession is a 1981 French-German psychological horror drama film co-written and directed by Andrzej Żuławski and starring Isabelle Adjani and Sam Neill.  The plot obliquely follows the relationship between an international spy and his wife, who begins exhibiting increasingly disturbing behavior after asking him for a divorce.  Filmed in Berlin in 1980, the film debuted at the Cannes Film Festival, where Isabelle Adjani won the award for Best Actress for her performance.  \"Possession\" was Żuławski's only English-language film.  In recent years, the film has developed a cult following.\n\nMirosław Żuławski: Mirosław Żuławski (January 16, 1913 – February 17, 1995) was a Polish writer, prosaist, diplomatist and screenwriter.  He is father of film director, Andrzej Żuławski.\n\nCosmos (2015 film): Cosmos is a 2015 French-Portuguese thriller film directed by Andrzej Żuławski.  The screenplay by Żuławski is based on the novel of the same name by Witold Gombrowicz.  It tells the story of two friends who spend time at a countryside guesthouse where they discover mysterious and frightening signs.  The filmmakers label it as a \"metaphysical noir thriller\".\n\nOtto Preminger: Otto Ludwig Preminger ( , ] ; 5 December 1905 – 23 April 1986) was an American theatre and film director, originally from Austria-Hungary.\n\nAndrzej Korzyński: Andrzej Korzyński is a Polish composer who has worked with film directors Andrzej Wajda (\"The Birch Wood\", \"Man of Marble\") and Andrzej Żuławski.\n\nFidelity (film): Fidelity () is a 2000 French drama film written and directed by Andrzej Żuławski and starring Sophie Marceau, Pascal Greggory, and Guillaume Canet.  Based on Madame de La Fayette's seventeenth century novel \"La Princesse de Clèves\", the film is about a talented photographer who lands a lucrative job in Paris with a scandal-mongering tabloid and becomes romantically involved with an eccentric children's book publisher while resisting the sexual advances of another photographer.  Filmed on location in Paris, \"Fidelity\" received the Cabourg Romantic Film Festival Award for Best Actress (Sophie Marceau) and the Golden Swann Award (Andrzej Zulawski).\n\nQuestion: Who was an American theatre and film director, originally from Austria-Hungary, Otto Preminger or Andrzej Żuławski ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person who matches the description.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the person.\"\n    },\n    \"origin_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the person was originally from.\"\n    },\n    \"professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions held by the person.\"\n    },\n    \"is_american_director\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the person was an American theatre and film director, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"nationality\",\n    \"origin_country\",\n    \"professions\",\n    \"is_american_director\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person who matches the description."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the person."
      },
      "origin_country": {
        "type": "string",
        "description": "The country where the person was originally from."
      },
      "professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions held by the person."
      },
      "is_american_director": {
        "type": "boolean",
        "description": "True if the person was an American theatre and film director, false otherwise."
      }
    },
    "required": [
      "person_name",
      "nationality",
      "origin_country",
      "professions",
      "is_american_director"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
