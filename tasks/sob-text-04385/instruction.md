{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFor Hope: For Hope is a 1996 ABC TV movie starring Dana Delany and directed by Bob Saget.  Based on Saget's sister Gay, the movie showed the experience of a young woman fatally afflicted with the disease \"scleroderma\".  Other cast members included Tracy Nelson and Chris Demetral.\n\nA Nameless Band: A Nameless Band (Bulgarian: Оркестър без име ) is a comedy movie released in Bulgaria in 1982.  It was directed by Lyudmil Kirkov and written by Stanislav Stratiev.  The movie describes the life of the young generation in Bulgaria in the late seventies and early eighties.  It is about dreams and reality, friendship, love… \"and something else\" (the favorite expression of Reni in the movie).\n\nLyudmil Kirkov: Lyudmil Kirkov (Bulgarian: Людмил Кирков , 14 December 1933 – 12 December 1995) was a Bulgarian film director and actor.\n\nA Peasant on a Bicycle: A Peasant on a Bicycle (Bulgarian: \"Селянинът с Колелото\" / \"Selyaninat s Koleloto\") is a Bulgarian drama film released in 1974, directed by Lyudmil Kirkov, starring Georgi Georgiev - Gets, Diana Chelebieva, Georgi Rusev and Evstati Stratev.\n\nBalance (1983 film): Balance (Bulgarian: Равновесие , translit.  Ravnovesie) is a 1983 Bulgarian drama film directed by Lyudmil Kirkov.  It was entered into the 13th Moscow International Film Festival where it won the Silver Prize.\n\nThe Boy Turns Man: The Boy Turns Man (Bulgarian: \"Момчето си отива\" / \"Momcheto si otiva\") is a Bulgarian comedy-drama film released in 1972, directed by Lyudmil Kirkov, starring Nevena Kokanova, Philip Trifonov, Kiril Gospodinov and Sashka Bratanova.\n\nFarce of the Penguins: Farce of the Penguins is a 2007 American direct-to-video parody directed by Bob Saget.  It is a parody of the 2005 French feature length nature documentary \"March of the Penguins\" directed and co-written by Luc Jacquet.  The film features Samuel L. Jackson as narrator, with the two main characters voiced by Bob Saget and Lewis Black.  Five of Saget's former \"Full House\" co-stars also lent their voices to the film.  Other additional voices were provided by Tracy Morgan, Christina Applegate, James Belushi, Whoopi Goldberg, Dane Cook, Abe Vigoda, Mo'Nique, and others.\n\nThe Swedish Kings: The Swedish Kings (Bulgarian: \"Шведските крале\" / \"Shvedskite krale\") is a Bulgarian comedy film released in 1968, directed by Lyudmil Kirkov, starring Kiril Gospodinov, Tsvetana Maneva, Asen Georgiev, Evstati Stratev and Konstantin Kotsev.\n\nBob Saget: Robert Lane \"Bob\" Saget (born May 17, 1956) is an American stand-up comedian, actor, and television host.  His television roles include Danny Tanner on the ABC sitcom \"Full House\" (1987–95) and its Netflix sequel \"Fuller House\", and hosting \"America's Funniest Home Videos\" from 1989 to 1997.  Saget is also known for his adult-oriented stand-up routine.  He also provided the voice of the future Ted Mosby on the CBS sitcom \"How I Met Your Mother\" from 2005 to 2014.\n\nRollin' with Saget: \"Rollin' with Saget\" is a comedic rap song composed by Stu Stone & D-Sisive and featuring vocals from Jamie Kennedy & Stu Stone with Bob Saget.  Much of its humor is derived from showing Saget in a profane and violent light (which actually corresponds with his stand-up act), as opposed to his most famous role, Danny Tanner, the squeaky clean widowed father of three on the American sitcom \"Full House\", or the wholesome host of \"America's Funniest Home Videos\".  Saget himself has since adopted it as a pseudo theme song, streaming it on his official website and playing during his stand-up acts.\n\nQuestion: Are Lyudmil Kirkov and Bob Saget both film or TV stars?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"are_both_stars\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals are identified as film or TV stars, false otherwise.\"\n    },\n    \"number_of_stars_identified\": {\n      \"type\": \"integer\",\n      \"description\": \"The count of individuals identified as film or TV stars from the context.\"\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"Details for each individual mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"is_film_or_tv_star\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual is a film or TV star based on the context.\"\n          },\n          \"roles\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"Specific roles (e.g., actor, voice actor, television host) that qualify the individual as a star.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_film_or_tv_star\",\n          \"roles\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"are_both_stars\",\n    \"number_of_stars_identified\",\n    \"individuals\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "are_both_stars": {
        "type": "boolean",
        "description": "True if both individuals are identified as film or TV stars, false otherwise."
      },
      "number_of_stars_identified": {
        "type": "integer",
        "description": "The count of individuals identified as film or TV stars from the context."
      },
      "individuals": {
        "type": "array",
        "description": "Details for each individual mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "is_film_or_tv_star": {
              "type": "boolean",
              "description": "True if the individual is a film or TV star based on the context."
            },
            "roles": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Specific roles (e.g., actor, voice actor, television host) that qualify the individual as a star."
            }
          },
          "required": [
            "name",
            "is_film_or_tv_star",
            "roles"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "are_both_stars",
      "number_of_stars_identified",
      "individuals"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
