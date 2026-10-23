{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPaco Plaza: Paco Plaza is a Spanish film director best known for writing and directing \"REC\" and \"REC 2\" with Jaume Balagueró.  He then went on to direct the \"REC\" parallel sequel \"\" by himself while Jaume Balagueró directed the follow-up, \"REC 4: Apocalypse\".  He speaks Spanish, English and French.\n\nFragile (film): Fragile (Spanish: Frágiles ) is a 2005 Spanish-British horror film directed by Jaume Balagueró.\n\nMuse (2017 film): Muse (Spanish: \"Musa\" ) is an upcoming English-language Spanish supernatural thriller film directed by Jaume Balagueró.  The screenplay, written by Balagueró and Fernando Navarro, is based on the Spanish novel \"The Lady Number Thirteen\" by José Carlos Somoza.  The film stars Elliot Cowan, Franka Potente, Ana Ularu, Joanne Whalley, Christopher Lloyd and Leonor Watling.  It is scheduled to be released in Spain on 1 December 2017.\n\nREC (film): REC (stylized as [•REC]) is a 2007 Spanish zombie horror film, co-written and directed by Jaume Balagueró and Paco Plaza.  The film was shot in Barcelona, Spain and the title is an abbreviation of the word \"record\", as it appears on a video camera.\n\nJaume Balagueró: Jaume Balagueró i Bernat (] ; born 2 November 1968) is a Spanish film director widely known for his horror films, most notably the acclaimed \"REC\" series.\n\nREC 4: Apocalypse: REC 4 (stylized as [•REC]⁴, subtitled in some countries as \"Apocalypse\") is a 2014 Spanish horror film, and the fourth and final installment of the \"REC\" franchise.  The film is a direct sequel to \"REC 2\", taking place immediately after the events of the second film.  Jaume Balagueró, the director of the first two installments, returns alongside actress Manuela Velasco, who reprises her role of the imperiled reporter Ángela Vidal.  The film premiered at the Toronto International Film Festival on 9 September 2014 and screened at the 2014 Sitges Film Festival on 3 October, before being released in Spain on the 31st of October.\n\nThe Nameless (film): The Nameless (Spanish: Los Sin Nombre ; Catalan: Els sense nom ) is a 1999 independent Spanish horror film directed by Jaume Balagueró.  It is based on the 1981 horror novel by English writer Ramsey Campbell which mingled psychological suspense with supernatural horror.\n\nTristana Medeiros: Tristana Medeiros Da Souza, known in Spanish as La Niña Medeiros is a fictional character and main antagonist of the \"REC film series\".  Created by Jaume Balagueró and Paco Plaza, Medeiros Girl was introduced in the first film and had an expanded role in \"REC 2\".  In \"\", she has a cameo that reveals she is the root cause of the demonic outbreak.  Her origins are told by the character itself in the comic book \"REC: Historias Ineditas\", released in 2012 alongside \"Genesis\".\n\nDarkness (2002 film): Darkness is a 2002 English-language horror film, directed by Jaume Balagueró and starring Anna Paquin, Lena Olin, Iain Glen, Giancarlo Giannini and Fele Martínez.  The film was produced by Julio Fernández and Brian Yuzna.  The film's plot follows an American family who move into a house in the Spanish countryside, where six children disappeared during an occult ritual forty years before; the teenage daughter and young son of the family are subjected to increasing disturbances in the house.\n\nREC 2: REC 2 (stylized as [•REC]²) is a 2009 Spanish horror film sequel to 2007's \"REC\" and the second installment of the REC film series.  The film was written and directed by Jaume Balagueró and Paco Plaza, both of whom returned from the previous film.  The story takes place immediately after the events of the first film.  The film was followed by \"\".\n\nQuestion: Jaume Balagueró i Bernat, is a Spanish film director widely known for his horror films, most notably REC, a Spanish zombie horror film, co-written and directed by Jaume Balagueró and Paco Plaza, released in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"directors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of directors for the film.\"\n    },\n    \"genre\": {\n      \"type\": \"string\",\n      \"description\": \"The primary genre of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"directors\",\n    \"genre\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "directors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of directors for the film."
      },
      "genre": {
        "type": "string",
        "description": "The primary genre of the film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "directors",
      "genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
