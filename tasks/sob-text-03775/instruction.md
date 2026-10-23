{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThérèse Desqueyroux (1962 film): Thérèse Desqueyroux is a 1962 French film directed by Georges Franju, based on the novel of the same name by François Mauriac.  Written by Franju and François Mauriac and Claude Mauriac, it stars Emmanuelle Riva and Philippe Noiret.  Riva won Best Actress at the Venice Film Festival, the Étoile de Cristal award for Best Actress, and the Silver Goddess Award from the Mexican Cinema Journalists for her performance.\n\nGeorges Franju: Georges Franju (] ; 12 April 1912 – 5 November 1987) was a French filmmaker.  He was born in Fougères, Ille-et-Vilaine.\n\nThomas the Impostor: Thomas the Impostor (French: \"Thomas l'imposteur\" ) is a 1964 French film directed by Georges Franju and starring Emmanuelle Riva, Fabrice Rouleau, Sophie Dares, Jean Marais and Charles Aznavour.  It is based on a novel of the same name by Jean Cocteau, which had first been published in French in 1923 and had been inspired by Cocteau's experiences in the first World War.  An American edition of the novel, translated into English by Lewis Galentiere, was published in 1925 under the title \"Thomas the Impostor\", and another English translation by Dorothy Williams was subsequently published in 1957 under the title \"The Impostor\".  The film was entered into the 15th Berlin International Film Festival.\n\nChristian Matras (cinematographer): Christian Matras (29 December 1903, Valence, Drôme, France - 4 May 1977, Paris) was a French cinematographer who worked on more than 100 feature films, including \"Grand Illusion\" (1937), directed by Jean Renoir; \"The Milky Way\" (1969), directed by Luis Buñuel; and \"Thérèse Desqueyroux\" (1962), directed by Georges Franju; \"Lola Montès\" (1955), \"The Earrings of Madame De...\" (1953), and \"Le Plaisir\" (1952), all directed by Max Ophüls; and \"L'Aigle à deux têtes\" (1948) directed by Jean Cocteau.\n\nLe Grand Méliès: Le Grand Méliès is a 1952 French short documentary film directed by Georges Franju about the life of the film pioneer Georges Méliès.\n\nJami (director): Jamshed Mahmood Raza (born March 1972), popularly known as Jami, is a film director from Pakistan.\n\nBlood of the Beasts: Blood of the Beasts (\"Le Sang des bêtes\") is a 1949 short French documentary film written and directed by Georges Franju.  It is Franju's first film and is narrated by Georges Hubert and Nicole Ladmiral.\n\nThe Demise of Father Mouret: The Demise of Father Mouret (French: \"La Faute de l'Abbé Mouret\" , \"The Mistake of Father Mouret\") is a 1970 French film directed by Georges Franju, based on the 1875 novel \"La Faute de l'Abbé Mouret\" by Émile Zola.  Like the novel, the film is about Father Mouret, a young priest (played by Francis Huster) who is sent to a remote village in Provence, then has a nervous breakdown and develops amnesia.  While recuperating, he meets and falls in love with a beautiful young woman, Albine (Gillian Hills), with whom he begins an idyllic relationship meant to recall the story of Adam and Eve.  When he regains his memory, though, he is wracked with guilt, and ends the relationship, leading to tragedy for both.\n\nLa Vampire Nue: La Vampire Nue (English title: \"The Nude Vampire\") is a 1970 film directed by Jean Rollin.  It concerns a suicide cult led by a mysterious man known as \"The Master\".  The film was influenced by the 1963 Georges Franju classic \"Judex\".\n\nHôtel des Invalides (film): Hôtel des Invalides is a 1952 French short documentary film directed by Georges Franju.\n\nQuestion: Which filmaker is from Pakistan, Georges Franju or Jami?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"filmmaker_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the filmmaker from Pakistan.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin for the identified filmmaker.\"\n    },\n    \"other_filmmaker_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other filmmaker mentioned in the question.\"\n    },\n    \"other_filmmaker_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin for the other filmmaker.\"\n    },\n    \"question_answered\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the question about the filmmaker's origin was successfully answered.\"\n    }\n  },\n  \"required\": [\n    \"filmmaker_name\",\n    \"country_of_origin\",\n    \"other_filmmaker_name\",\n    \"other_filmmaker_country\",\n    \"question_answered\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "filmmaker_name": {
        "type": "string",
        "description": "The name of the filmmaker from Pakistan."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country of origin for the identified filmmaker."
      },
      "other_filmmaker_name": {
        "type": "string",
        "description": "The name of the other filmmaker mentioned in the question."
      },
      "other_filmmaker_country": {
        "type": "string",
        "description": "The country of origin for the other filmmaker."
      },
      "question_answered": {
        "type": "boolean",
        "description": "Indicates if the question about the filmmaker's origin was successfully answered."
      }
    },
    "required": [
      "filmmaker_name",
      "country_of_origin",
      "other_filmmaker_name",
      "other_filmmaker_country",
      "question_answered"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
