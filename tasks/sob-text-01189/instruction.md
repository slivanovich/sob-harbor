{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAll Fired Up (film): All Fired Up (French: Tout feu, tout flamme ) is a 1982 French comedy film directed by Jean-Paul Rappeneau, starring Yves Montand and Isabelle Adjani.  It tells the story of a man who works with shady casino operations abroad.  When he returns to Paris in need of money, he is unaware that his eldest daughter has begun to work for the ministry of finance.  The film premiered on 13 January 1982.  It had 2,279,445 admissions in France.\n\nJean Bouise: Jean Bouise (3 June 1929 in Le Havre – 6 July 1989 in Lyon) was a French actor.  In the 1950s he helped to found Théâtre de la Cité, and was a player in the company.  He entered films in the 1960s, and played a supporting roles in \"The Shameless Old Lady\", \"Z\", \"L'Aveu\", \"Out 1\", \"The Return of the Tall Blond Man with One Black Shoe\", \"Section spéciale\", and \"Monsieur Klein\".  He received César nominations for his roles in \"Le vieux fusil\" and \"Le Juge Fayard dit Le Shériff\", before winning the Best Supporting Actor award for \"Coup de tête\".  Subsequently he appeared in \"Édith et Marcel\", \"Le Dernier Combat\", \"Subway\", \"The Big Blue\" and \"Nikita\".\n\nPossession (1981 film): Possession is a 1981 French-German psychological horror drama film co-written and directed by Andrzej Żuławski and starring Isabelle Adjani and Sam Neill.  The plot obliquely follows the relationship between an international spy and his wife, who begins exhibiting increasingly disturbing behavior after asking him for a divorce.  Filmed in Berlin in 1980, the film debuted at the Cannes Film Festival, where Isabelle Adjani won the award for Best Actress for her performance.  \"Possession\" was Żuławski's only English-language film.  In recent years, the film has developed a cult following.\n\nAdolphe (film): Adolphe is a 2002 French drama film based on the novel \"Adolphe\" by Benjamin Constant.  The film was directed by Benoît Jacquot and starred Isabelle Adjani as Ellénore and Stanislas Merhar as Adolphe.\n\nIsabelle Sadoyan: Isabelle Sadoyan (12 May 1928 – 10 July 2017) was a French-Armenian actress.  She was the wife of actor Jean Bouise.  Her filmography includes films by Jeanne Moreau, Claude Chabrol, Claude Lelouch, Luc Besson, Jean-Luc Godard, Henri Verneuil, Bertrand Tavernier, Robert Kechichian and Krzysztof Kieślowski.\n\nFrench Women (film): French Women (original title: Sous les jupes des filles) is a 2014 French comedy drama film and the directorial debut of Audrey Dana.  The film tells the stories of eleven women in Paris and features an ensemble cast including Isabelle Adjani, Alice Belaïdi, Laetitia Casta, Audrey Dana, Julie Ferrier, Audrey Fleurot, Marina Hands, Géraldine Nakache, Vanessa Paradis, Alice Taglioni and Sylvie Testud.  The French title directly translated is \"\"Under the Skirts of Girls\"\".\n\nOne Deadly Summer: One Deadly Summer (French: L'Été meurtrier ) is a French film directed by Jean Becker.  Isabelle Adjani won a César award for her performance in this film.  The film was a massive hit in France gaining 5,137,040 admissions and was the 2nd highest grossing film of the year.  The film is based on a 1977 novel by Sébastien Japrisot (whose real name is Jean-Baptiste Rossi).\n\nSubway (film): Subway is a 1985 French comedy drama film directed by Luc Besson and starring Isabelle Adjani and Christopher Lambert.  The film is classified as part of the \"cinema du look\" movement.\n\nCamille Claudel (film): Camille Claudel is a 1988 French film about the life of the 19th century female sculptor Camille Claudel.  The movie was based on the book by Reine-Marie Paris, granddaughter of Camille's brother, the poet and diplomat Paul Claudel.  It was directed by Bruno Nuytten, co-produced by Isabelle Adjani, and starred her and Gérard Depardieu.  The film had a total of 2,717,136 admissions in France.  Adjani earned a nomination for Academy Award for Best Actress for her role, the second time in her career she was so honored and the first time a French actress was nominated for the Best Actress Oscar twice.\n\nThe Story of Adele H.: The Story of Adele H. (French: \"L'Histoire d'Adèle H.\" ) is a 1975 French historical drama film directed by François Truffaut and starring Isabelle Adjani, Bruce Robinson, and Sylvia Marriott.  Written by Truffaut, Jean Gruault, and Suzanne Schiffman, the film is about Adèle Hugo, the daughter of writer Victor Hugo, whose obsessive unrequited love for a military officer leads to her downfall.  The story is based on Adèle Hugo's diaries.  It was filmed on location in Guernsey, Barbados, and Senegal.\n\nQuestion: Jean Bouise was a French actor who appeared in a 1985 French comedy drama film directed by Luc Besson, that starred Isabelle Adjani and who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"genre\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The genres of the film.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The names of the main actors starring in the film.\"\n    },\n    \"co_star_identified\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-star identified in the question, in addition to Isabelle Adjani.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director_name\",\n    \"genre\",\n    \"starring_actors\",\n    \"co_star_identified\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "genre": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The genres of the film."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The names of the main actors starring in the film."
      },
      "co_star_identified": {
        "type": "string",
        "description": "The name of the co-star identified in the question, in addition to Isabelle Adjani."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director_name",
      "genre",
      "starring_actors",
      "co_star_identified"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
