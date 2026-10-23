{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRobert Rodriguez: Robert Anthony Rodriguez (born June 20, 1968) is an American filmmaker, screenwriter, and musician.  He shoots and produces many of his films in Mexico and his home state, Texas.  Rodriguez directed the 1992 action film \"El Mariachi\", which was a commercial success after grossing $2 million against a budget of $7,000.  The film spawned two sequels known collectively as the \"Mexico Trilogy\": \"Desperado\" and \"Once Upon a Time in Mexico\".  He directed \"From Dusk till Dawn\" in 1996 and developed its (2014–present).  Rodriguez co-directed the 2005 neo-noir crime thriller anthology \"Sin City\" (adapted from the graphic novel of the same name) and the 2014 sequel, \"\".  Rodriguez also directed the \"Spy Kids\" films, \"The Faculty\", as well as \"The Adventures of Sharkboy and Lavagirl\", \"Planet Terror\", and \"Machete\".  He is a friend and frequent collaborator of filmmaker Quentin Tarantino, who founded the production company A Band Apart, which Rodriguez was a member of.  In December 2013, Rodriguez launched his own cable television channel, El Rey.\n\nGuimba the Tyrant: Guimba the Tyrant (French: \"Guimba, un tyran, une époque\" ) is a 1995 Malian comedy drama film in the Bambara language (with some Fula language components), directed by noted Malian director Cheick Oumar Sissoko.  The movie shows the rise and fall of a cruel and despotic village chief \"Guimba\", and his son \"Jangine\" in a fictional village in the Sahel of Mali.  Some of the storytelling was done through the medium of the village griot, and with the film being placed in an old setting, lends an epic touch to the movie.  The exact chronological setting of the movie is difficult to ascertain, being set in an isolated village, but the commonly used weaponry shown is the blunderbuss (however one scene outside the village features a neem tree, a species introduced to Africa during the colonial period).  The film depicts some magical components, including a solar eclipse brought on by magic.  Casting was only partially done from among professional actors.\n\nCheick Oumar Dabo: Cheick Oumar Dabo (born 12 January 1981 in Bamako) is a Malian football player.\n\nDesperado (film): Desperado is a 1995 American contemporary Western action film written, produced, and directed by Robert Rodriguez.  A sequel to the 1992 film \"El Mariachi\", it is the second installment in Robert Rodriguez's \"Mexico Trilogy\".  It stars Antonio Banderas as the mariachi who seeks revenge on the drug lord who killed his lover.  The film was screened out of competition at the 1995 Cannes Film Festival. \" Once Upon a Time in Mexico\", the final part of the trilogy, was released in 2003.  \"Desperado\" grossed $25.4 million in the United States.\n\nOumar Sissoko: Oumar Sissoko (born 13 September 1987 in Montreuil France) is a Malian footballer who currently plays as a goalkeeper for Le Havre.  His cousin Mohamed Sissoko is also a professional footballer and was also capped for Mali.\n\nGenesis (1999 film): Genesis (French: La genèse ) is a 1999 French-Malian drama film directed by Cheick Oumar Sissoko.  It covers chapters 23 to 37 of the biblical Book of Genesis, but with only African actors.  It was screened in the Un Certain Regard section at the 1999 Cannes Film Festival.\n\nBalla Moussa Keïta: Balla Moussa Keïta (1934 – March 6, 2001) was a Malian actor and comedian, and a West African cinema pioneer who was well known in the West (especially France).  Born in the Ségou Region of Mali, he was originally a radio producer.  He later turned to acting and acted in a number of movies by notable Mali directors like Cheick Oumar Sissoko, Souleymane Cissé and Abdoulaye Ascofaré.  Among his critically acclaimed roles are those of the tribal king \"Rouma Boll\" in \"Yeelen\" and as Mambi in \"Guimba, un tyrant, une époque\".  He received the Best Male Interpretation award at the FESPACO for his role in the Guinean film \"Séré, le témoin\".\n\nAfrican Solidarity for Democracy and Independence: African Solidarity for Democracy and Independence (French: \"Solidarité Africaine pour la Démocratie et l'Indépendance\" ) is a left-wing political party in Mali.  It was founded by Cheick Oumar Sissoko and Oumar Mariko in 1996; Sissoko is the party's President and Mariko is its Secretary-General, the top post in the party.  The party is Pan-Africanist in ideology, is affiliated internationally with the International Communist Seminar, a grouping organised by the Workers Party of Belgium, and is in part an outgrowth of the 1991 demonstrations against the military rule of President Moussa Traoré.  Mariko was head of the Association of Students and Pupils of Mali (AEEM) during the 1991 protest movement which overthrew the government.\n\nCheick Bathily: Cheick Oumar Bathily (born 10 October 1982) is a Malian football player who currently plays for CS Duguwolofila.\n\nCheick Oumar Sissoko: Cheick Oumar Sissoko (born 1945 in San, Mali) is a Malian film director and politician.\n\nQuestion: Who is older, Cheick Oumar Sissoko or Robert Rodriguez?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the first person being compared.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the first person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the second person being compared.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the second person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"age_comparison_result\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"older_person_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who is older.\"\n        },\n        \"younger_person_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who is younger.\"\n        },\n        \"age_difference_years\": {\n          \"type\": \"integer\",\n          \"description\": \"The difference in birth years between the two people.\"\n        }\n      },\n      \"required\": [\n        \"older_person_name\",\n        \"younger_person_name\",\n        \"age_difference_years\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_1\",\n    \"person_2\",\n    \"age_comparison_result\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the first person being compared."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the first person."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the second person being compared."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the second person."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "age_comparison_result": {
        "type": "object",
        "properties": {
          "older_person_name": {
            "type": "string",
            "description": "The name of the person who is older."
          },
          "younger_person_name": {
            "type": "string",
            "description": "The name of the person who is younger."
          },
          "age_difference_years": {
            "type": "integer",
            "description": "The difference in birth years between the two people."
          }
        },
        "required": [
          "older_person_name",
          "younger_person_name",
          "age_difference_years"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_1",
      "person_2",
      "age_comparison_result"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
