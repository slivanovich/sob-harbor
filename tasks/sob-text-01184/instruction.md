{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGolden Balls (film): Golden Balls (Spanish: Huevos de oro) is a 1993 Spanish film directed by Bigas Luna.  It stars Javier Bardem, Maria de Medeiros, Alessandro Gassman, Maribel Verdú and Benicio del Toro.\n\nSeven Billiard Tables: Seven Billiard Tables (original Spanish title: \"Siete mesas de billar francés\") is a 2007 Spanish film by Gracia Querejeta.  She also co-wrote the story with David Planell.  In 2008, this film was nominated for nine Goya Awards, Spain's most prestigious film awards.  It won two awards, including the Best Actress award (for Maribel Verdú).\n\nTetro: Tetro is a 2009 American-Argentine drama film written, directed and produced by Francis Ford Coppola and starring Vincent Gallo, Alden Ehrenreich and Maribel Verdú.  Filming took place in 2008 in Buenos Aires, Patagonia, and Spain.  \"Tetro\" received a limited release in the United States on June 11, 2009.\n\nThe Lucky Star (1997 film): La Buena Estrella (English: The Lucky Star ) is a 1997 Spanish drama film directed by Ricardo Franco and starring Antonio Resines, Jordi Mollá and Maribel Verdú.  Critically acclaimed, the film won five Goya Awards: Best Film, Best Director, Best Actor (Antonio Resines), Best Original script and Best Original Music.  Ricardo Franco made just one more film; he died of a heart attack in 1998.\n\nEden Is West: Eden Is West (French: \"Eden à l'ouest\" ) is a 2009 film by Greek-French director Costa-Gavras about an illegal immigrant called Elias who tries to get to Paris.  The original title in Greek is “Paradissos sti Dysi” (“Paradise in West”) and since it is a Greek-French production, the also original French title is “Eden à l'ouest'.  The nationality of the central hero is not disclosed because Gavras wants to make a point about the odysseys of the illegal immigrants of any nationality, since he himself was an immigrant 50 years ago in France, before he became a well known director.  His hero seems to tolerate the sea, the cold of snowy mountains and the hunger, the rapists and robbers he meets, the cops that are after him all the time, the racists who push him aside, the fellow immigrants who steal his clothes and in the best case the women who see him as a lover they could also take advantage of.  His only comfort is his dream of Paris and, in the complexity of human condition, the good within the evil and vice versa.\n\nMaribel Verdú: María Isabel Verdú Rollán (] ; born 2 October 1970) better known as Maribel Verdú is a Spanish actress.  She is known to English-speaking audiences for playing Luisa in Alfonso Cuarón's 2001 film \"Y tu mamá también\" and Mercedes in Guillermo del Toro's 2006 film \"Pan's Labyrinth\".  In Spain she is known for films such as \"Lovers\" (\"Amantes\"), \"Belle Époque\", \"The Blind Sunflowers\" (\"Los girasoles ciegos\") and \"Blancanieves\".\n\nLovers (1991 film): Lovers (Spanish: Amantes ) is a 1991 Spanish film noir written and directed by Vicente Aranda, starring Victoria Abril, Jorge Sanz and Maribel Verdú.  The film brought Aranda to widespread attention in the English-speaking world.  It won two Goya Awards (Best Film and Best Director) and is considered one of the best Spanish films of the 90s.\n\nYear of Enlightment: Year of Enlightment (Spanish: \"El Año de las Luces\" , and also released as \"The Year of the Awakening\") is a 1986 Spanish film directed by Fernando Trueba, starring Jorge Sanz and Maribel Verdú.  The film is a coming of age story of a sixteen-year-old boy finding love and sex in the aftermath of the Spanish Civil War.  The film was awarded the Silver Bear at the 37th Berlin International Film Festival.\n\nPan's Labyrinth: Pan's Labyrinth (Spanish: El laberinto del fauno , 'The Labyrinth of the Faun' ) is a 2006 Spanish-Mexican dark fantasy film written and directed by Mexican filmmaker Guillermo del Toro.  It was produced and distributed internationally by Esperanto Filmoj and Warner Bros.\n\nThe Blind Sunflowers (film): The Blind Sunflowers (Spanish: \"Los girasoles ciegos\" ) is a 2008 Spanish film directed by José Luis Cuerda and written by Rafael Azcona and Cuerda, based on the novel \"The Blind Sunflowers\" by Alberto Méndez.  The film stars Maribel Verdú, Javier Cámara and Raúl Arévalo.  The plot follows the life of a family, former sympathizers of the Spanish Republic, during the early 1940s.  Their lives are disrupted when a young priest falls in love with the mother.  The film is set in Ourense, 1940 where a disorientated deacon, named Salvador returns to the seminary of Ourense where the Rector delays Salvador's access to priesthood for a year.  Salvador begins teaching in a school where he meets with Lorenzo, the son of Elena, whom of which Salvador thinks is widowed.  This opportunity multiplies with the deacon becoming obsessed with her, abusing her mentally and physically.  We realise that Salvador is threatening Elena's family because of his obsession.  Wounded and beaten by the circumstances, the characters of the Blind Sunflowers hit the wall of repression, impossible romances and emotional defeats, while we realise Elena's family try to search for a glimpse of hope.\n\nQuestion: What nationality is the director of the film, in which Maribel Verdú appeared as Mercedes ? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"role_played\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_played\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer_director_nationality\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"actress_details\",\n    \"film_details\",\n    \"director_details\",\n    \"final_answer_director_nationality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "role_played": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "role_played"
        ],
        "additionalProperties": false
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "release_year"
        ],
        "additionalProperties": false
      },
      "director_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "final_answer_director_nationality": {
        "type": "string"
      }
    },
    "required": [
      "actress_details",
      "film_details",
      "director_details",
      "final_answer_director_nationality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
