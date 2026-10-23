{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBaise-moi: Baise-moi (\"Fuck me \") is a 2000 French crime thriller film with elements of a rape and revenge film written and directed by Virginie Despentes and Coralie Trinh Thi and starring Karen Lancaume and Raffaëla Anderson.  It is based on the novel by Despentes, first published in 1993.  The film received intense media coverage because of its graphic mix of violence and explicit sex scenes.  Consequently, it is sometimes considered an example of the \"New French Extremity.\"\n\nSecret Things: Secret Things (French: Choses secrètes ) is a 2002 French erotic thriller film directed by Jean-Claude Brisseau, starring Coralie Revel and Sabrina Seyvecou.  The film is sometimes associated with the New French Extremity.  Cahiers du Cinema named \"Secret Things\", jointly along with \"Ten\" by director Abbas Kiarostami, as the best film of 2002.  The film was awarded the 'French Cineaste of the Year' title at the 2003 Cannes Film Festival.  In 2005, the director Jean-Claude Brisseau was found guilty of sexually harassing two actresses between 1999 and 2001 during auditions for the film.\n\nWhale Rider: Whale Rider is a 2002 New Zealand-German family drama film directed by Niki Caro, based on the novel of the same name by Witi Ihimaera.  The film stars Keisha Castle-Hughes as Kahu Paikea Apirana, a twelve-year-old Māori girl whose ambition is to become the chief of the tribe.  Her grandfather Koro believes that this is a role reserved for males only.  The film was a coproduction between New Zealand and Germany.  It was shot on location in Whangara, the setting of the novel.  The world premiere was on 9 September 2002, at the Toronto International Film Festival.  The film received critical acclaim upon its release.  At age 13, Keisha Castle-Hughes became the youngest nominee for the Academy Award for Best Actress before she was surpassed by Quvenzhané Wallis, at age 9, for \"Beasts of the Southern Wild\" less than a decade later.  The film earned $41.4 million on a NZ$9,235,000 budget.\n\nBertrand Bonello: Bertrand Bonello (] ; born 11 September 1968) is a French film director, screenwriter, producer and composer.  His background is in classical music, and he lives between Paris and Montreal.  His work has also been associated with the New French Extremity.\n\nThe Lord of the Rings: The Two Towers: The Lord of the Rings: The Two Towers is a 2002 New Zealand-American epic high fantasy adventure film directed by Peter Jackson and based on the second volume of J. R. R. Tolkien's novel \"The Lord of the Rings\".  It is the second installment in \"The Lord of the Rings\" film series, preceded by \"\" (2001) and concluding with \"\" (2003).\n\nShed Skin Papa: Shed Skin Papa is an upcoming Hong Kong comedy-drama film written by Norihiko Tsukada and Roy Szeto based on Tsuksda's Japanese play \"Nukegara\", and directed by Szeto, who had previously directed an award-winning Hong Kong stage adaptation of the play titled \"Shed Skin\" in 2011.  The film stars Louis Koo as a washed-out, debt-ridden film director who must take care of his seventy nine-year-old dementia-ridden father (Francis Ng), who begins to shed a layer a skin everyday where regains his youth.  \"Shed Skin Papa\" made its world premiere at the 29th Tokyo International Film Festival on 26 October 2016 where it was shown in competition for the Tokyo Grand Prix\n\nNew French Extremity: New French Extremity (or New French Extremism) is a term coined by \"Artforum\" critic James Quandt for a collection of transgressive films by French directors at the turn of the 21st century.  The filmmakers are also discussed by Jonathan Romney of \"The Independent\".\n\nThe Maori Merchant of Venice: The Maori Merchant of Venice (Māori: \"Te Tangata Whai Rawa o Weniti\" ) is a 2002 New Zealand drama film in the Māori language (with English subtitles), directed by Don Selwyn.\n\nIn My Skin: In My Skin (French: \"Dans ma peau\") is a 2002 New French Extremity film written by, directed by, and starring Marina de Van.  It details the downward mental spiral of Esther, a woman (played by Marina de Van) who engages in increasingly destructive acts of self-mutilation following an accident that injures her leg at a party.\n\nThe Skin I Live In: The Skin I Live In (Spanish: La piel que habito ) is a 2011 Spanish psychological horror film written and directed by Pedro Almodóvar, starring Antonio Banderas, Elena Anaya, Marisa Paredes, Jan Cornet, and Roberto Álamo.  \"The Skin I Live In\" is based on Thierry Jonquet's novel \"Mygale\", first published in French and then in English under the title \"Tarantula\".\n\nQuestion: In My Skin, is a 2002 New French Extremity film written by, directed by, and starring who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"genre_association\": {\n      \"type\": \"string\",\n      \"description\": \"The film movement or genre the film is associated with.\"\n    },\n    \"person_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person involved in multiple roles for the film.\"\n        },\n        \"roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The roles this person held for the film (e.g., writer, director, star).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"roles\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"genre_association\",\n    \"person_details\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "genre_association": {
        "type": "string",
        "description": "The film movement or genre the film is associated with."
      },
      "person_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person involved in multiple roles for the film."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The roles this person held for the film (e.g., writer, director, star)."
          }
        },
        "required": [
          "name",
          "roles"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "genre_association",
      "person_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
