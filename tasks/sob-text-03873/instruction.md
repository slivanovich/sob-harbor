{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Dance of Reality: The Dance of Reality (Spanish: \"La danza de la realidad\" ) is a 2013 Chilean-French autobiographical musical fantasy drama film written, produced, and directed by Alejandro Jodorowsky, starring Brontis Jodorowsky, Pamela Flores, and Jeremias Herskovits.  It is Alejandro Jodorowsky's first film in 23 years.  The film screened at Directors' Fortnight during the 2013 Cannes Film Festival.  The film is based on an earlier work by Jodorowsky first published in Spanish under the title \"La danza de la realidad: Psicomagia y psicochamanismo\" (2001).\n\nFando y Lis: Fando y Lis is a film adaptation of a Fernando Arrabal play by the same name, and it is Alejandro Jodorowsky's first feature-length film.  Arrabal was working with Jodorowsky on performance art at the time.  The film was shot in high-contrast black-and-white on the week-ends with a small budget and was first shown at the Acapulco Film Festival in 1968.\n\nJodorowsky's Dune: Jodorowsky's Dune is a 2013 American-French documentary film directed by Frank Pavich.  The film explores cult film director Alejandro Jodorowsky's unsuccessful attempt to adapt and film Frank Herbert's 1965 science fiction novel \"Dune\" in the mid-1970s.\n\nAbel Cain: Abel Cain (formerly known as Sons of El Topo) is a stalled film project written and directed by Alejandro Jodorowsky and the sequel to Jodorowsky's classic acid Western film \"El Topo\".  It was to be produced and financed by Parallel Media.  In a 2010 interview, Jodorowsky said that the film had \"dragged a long time\" and suggested that Abel Cain will not feature any \"stars\", adding that he would cast his son Axel Jodorowsky in the lead role just as he did in his 1989 cult classic film \"Santa Sangre\".\n\nAlejandro Jodorowsky: Alejandro Jodorowsky Prullansky (] ; born 17 February 1929) is a Chilean-French film and theatre director, screenwriter, playwright, actor, author, poet, producer, composer, musician, comics writer, and spiritual guru.  Best known for his avant-garde films, he has been \"venerated by cult cinema enthusiasts\" for his work which \"is filled with violently surreal images and a hybrid blend of mysticism and religious provocation\".\n\nThe Holy Mountain (1973 film): La montaña sagrada (The Holy Mountain, reissued as The Sacred Mountain) is a 1973 Mexican surrealist fantasy film directed, written, produced, co-scored, co-edited by and starring Alejandro Jodorowsky, who also participated as a set designer and costume designer on the film.  The film was produced by Beatles manager Allen Klein of ABKCO Music and Records, after Jodorowsky scored an underground phenomenon with \"El Topo\" and the acclaim of both John Lennon and George Harrison (Lennon and Yoko Ono put up production money).  It was shown at various international film festivals in 1973, including Cannes, and limited screenings in New York and San Francisco.\n\nLes têtes interverties: Les têtes interverties (also known as \"La cravate\", \"The Transposed Heads\" and \"The Severed Heads\") is a 1957 French short film written and directed by Alejandro Jodorowsky.  Shot between 1953 and 1957, the film is a mime adaptation of Thomas Mann's 1940 novella \"The Transposed Heads\" (\"Die vertauschten Köpfe\").  The film stars surreal humorist Raymond Devos as well as Jodorowsky himself.\n\nJerry Belson: Jerry Belson (July 8, 1938 – October 10, 2006) was a writer, director, and producer of Hollywood films for over forty years.\n\nAxel Jodorowsky: Axel Cristóbal Jodorowsky (born 24 July 1965), also known as Cristóbal Jodorowsky, is a Chilean-French actor, writer, painter, playwright, trainer, tarologist, and psychologist.  He is the son of the Chilean-French film and theater director Alejandro Jodorowsky and Mexican actress Valerie Trumblay, brother to Brontis Jodorowsky and Adan Jodorowsky, and the uncle of Alma Jodorowsky.\n\nSanta Sangre: Santa Sangre (Holy Blood) is a 1989 Mexican-Italian avant-garde horror film directed by Alejandro Jodorowsky and written by Jodorowsky along with Claudio Argento and Roberto Leoni.  It stars Axel Jodorowsky, Adan Jodorowsky, Teo Jodorowsky, Blanca Guerra, Thelma Tixou and Guy Stockwell.  Divided into both a flashback and a flash-forward, the film, which is set in Mexico, tells the story of Fenix, a boy who grew up in a circus, and his life through both adolescence and early adulthood.\n\nQuestion: Were both Jerry Belson and Alejandro Jodorowsky actors in Hollywood films?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"The boolean answer to the question: Were both individuals actors in Hollywood films?\"\n    },\n    \"individuals_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"is_actor\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is identified as an actor in the context, false otherwise.\"\n          },\n          \"acted_in_hollywood_films\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is identified as having acted in Hollywood films, false otherwise.\"\n          },\n          \"known_roles_in_hollywood_films\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"Specific roles the individual held in Hollywood films, if any, other than acting.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_actor\",\n          \"acted_in_hollywood_films\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"answer\",\n    \"individuals_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "answer": {
        "type": "boolean",
        "description": "The boolean answer to the question: Were both individuals actors in Hollywood films?"
      },
      "individuals_involved": {
        "type": "array",
        "description": "Details about each individual mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "is_actor": {
              "type": "boolean",
              "description": "True if the individual is identified as an actor in the context, false otherwise."
            },
            "acted_in_hollywood_films": {
              "type": "boolean",
              "description": "True if the individual is identified as having acted in Hollywood films, false otherwise."
            },
            "known_roles_in_hollywood_films": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Specific roles the individual held in Hollywood films, if any, other than acting."
            }
          },
          "required": [
            "name",
            "is_actor",
            "acted_in_hollywood_films"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "question_asked",
      "answer",
      "individuals_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
