{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCyrano de Bergerac (1946 film): Cyrano de Bergerac is a 1946 French romantic comedy film directed by Fernand Rivers and starring Claude Dauphin, Ellen Bernsen and Pierre Bertin.  It is based on the 1897 play \"Cyrano de Bergerac\" by Edmond Rostand.\n\nCyrano de Bergerac (play): Cyrano de Bergerac is a play written in 1897 by Edmond Rostand.  Although there was a real Cyrano de Bergerac, the play is a fictionalization of his life that follows the broad outlines of it.\n\nChantecler (play): Chantecler is a verse play in four acts written by Edmond Rostand.  The play is notable in that all the characters are farmyard animals including the main protagonist, a chanticleer, or rooster.  The play centers on the theme of idealism and spiritual sincerity, as contrasted with cynicism and artificiality.  Much of the play satirizes modernist artistic doctrines from Rostand's romanticist perspective.\n\nCyrano de Bergerac (1990 film): Cyrano de Bergerac is a 1990 French comedy drama film directed by Jean-Paul Rappeneau and based on the 1897 play of the same name by Edmond Rostand, adapted by Jean-Claude Carrière and Rappeneau.  It stars Gérard Depardieu, Anne Brochet and Vincent Pérez.  The film was a co-production between companies in France and Hungary.\n\nSway (book): Sway is a 2014 young adult fiction book by American author Kat Spears and her debut novel.  The work was first published on 16 September 2014 through St. Martin's Griffin and is a modern take on the story of Cyrano de Bergerac.\n\nSarah Bernhardt: Sarah Bernhardt (] ; 22 or 23 October 1844 – 26 March 1923) was a French stage actress who starred in some of the most popular French plays of the late 19th and early 20th centuries, including \"La Dame Aux Camelias\" by Alexandre Dumas, \"fils\", \"Ruy Blas\" by Victor Hugo, \"Fédora\" and \"La Tosca\" by Victorien Sardou, and \"L'Aiglon\" by Edmond Rostand.  She also played male roles, including Shakespeare's Hamlet.  Rostand called her \"the queen of the pose and the princess of the gesture\", while Hugo praised her \"golden voice\".  She made several theatrical tours around the world, and was one of the first prominent actresses to make sound recordings and to act in motion pictures.\n\nRoxanne (film): Roxanne is a 1987 American romantic comedy film directed by Fred Schepisi and starring Steve Martin and Daryl Hannah.  It is a modern retelling of Edmond Rostand's 1897 verse play \"Cyrano de Bergerac\", adapted by Steve Martin.\n\nCyrano Agency: Cyrano Agency (; lit.  \"Cyrano Dating Agency\") is a 2010 South Korean romantic comedy starring Uhm Tae-woong, Park Shin-hye, Choi Daniel, Park Chul-min and Lee Min-jung.  It is a modern take on Edmond Rostand's 1897 play \"Cyrano de Bergerac\", which focuses on a dating agency that helps its customers win the hearts of the people they desire.  Produced by Myung Films and distributed by Lotte Entertainment, the film was released on September 16, 2010 and ran for 121 minutes.  The film was later remade into the Tamil-language as Idhu Enna Maayam.\n\nCyrano de Bergerac (1950 film): Cyrano de Bergerac is a 1950 drama romance film based on the 1897 French Alexandrine verse drama \"Cyrano de Bergerac\" by Edmond Rostand.  It uses poet Brian Hooker's 1923 English blank verse translation as the basis for its screenplay.  The film was the first motion picture version in English of Rostand's play, though there were several earlier adaptations in different languages.\n\nMaurice Rostand: Maurice Rostand (26 May 1891 – 21 February 1968) was a French author, the son of the noted poet and dramatist Edmond Rostand and the poet Rosemonde Gérard, and brother of the biologist Jean Rostand.\n\nQuestion: What adult fiction book by Kat Spears in based on a play 1897 by Edmond Rostand?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"book_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the book.\"\n    },\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the book's author.\"\n    },\n    \"book_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the book as described in the context.\"\n    },\n    \"source_play_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"play_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the play the book is based on.\"\n        },\n        \"play_author\": {\n          \"type\": \"string\",\n          \"description\": \"The author of the play.\"\n        },\n        \"play_publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The publication year of the play.\"\n        }\n      },\n      \"required\": [\n        \"play_title\",\n        \"play_author\",\n        \"play_publication_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"book_title\",\n    \"author_name\",\n    \"book_genre\",\n    \"source_play_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "book_title": {
        "type": "string",
        "description": "The title of the book."
      },
      "author_name": {
        "type": "string",
        "description": "The name of the book's author."
      },
      "book_genre": {
        "type": "string",
        "description": "The genre of the book as described in the context."
      },
      "source_play_details": {
        "type": "object",
        "properties": {
          "play_title": {
            "type": "string",
            "description": "The title of the play the book is based on."
          },
          "play_author": {
            "type": "string",
            "description": "The author of the play."
          },
          "play_publication_year": {
            "type": "integer",
            "description": "The publication year of the play."
          }
        },
        "required": [
          "play_title",
          "play_author",
          "play_publication_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "book_title",
      "author_name",
      "book_genre",
      "source_play_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
