{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Shadow Between (1931 film): The Shadow Between is a 1931 British romantic drama film directed by Norman Walker and starring Godfrey Tearle, Kathleen O'Regan, Olga Lindo and Ann Casson.\n\nSybil Thorndike: Dame Agnes Sybil Thorndike (24 October 18829 June 1976) was an English actress who toured internationally in Shakespearean productions, often appearing with her husband Lewis Casson.  Bernard Shaw wrote \"Saint Joan\" specially for her, and she starred in it with great success.  She was made Dame Commander of the Order of the British Empire in 1931, and Companion of Honour in 1970.\n\nBenedict Campbell: Benedict \"Ben\" Campbell (born June 12, 1957) is a Canadian actor and voice actor whose work has consisted primarily of providing voices for television cartoons and video games. Early in his career, Campbell also appeared in a number of live action works.  Campbell comes from an acting family; his parents are Douglas Campbell and Ann Casson, and he is the brother of Dirk Campbell.  Campbell's maternal grandparents are Sir Lewis Casson and Dame Sybil Thorndike.\n\nThe Prince Chap: The Prince Chap is a 1920 American silent drama film directed by William C. deMille and written by Olga Printzlau based upon the play of the same name by Edward Peple.  The film stars Thomas Meighan, Charles Ogle, Kathlyn Williams, Casson Ferguson, Ann Forrest, Peaches Jackson, and Mae Giraci.  The film was released in August 1920, by Paramount Pictures.\n\nCrime on the Hill: Crime on the Hill is a 1933 British mystery film directed by Bernard Vorhaus and starring Sally Blane, Nigel Playfair and Lewis Casson.  The plot was based on a successful play by Jack de Leon and Jack Celestin.  It was made by British International Pictures at Welwyn Studios in autumn 1933.\n\nDance Pretty Lady: Dance Pretty Lady is a 1932 British drama film directed by Anthony Asquith and starring Ann Casson, Carl Harbord, Michael Hogan, Moore Marriott and Flora Robson.  It was based on a novel by Compton Mackenzie.\n\nAnn Casson: Ann Casson (6 November 1915 – 2 May 1990) was an English stage and film actress.  She was the daughter of acting couple Sir Lewis Casson and Dame Sybil Thorndike.  She was married to actor Douglas Campbell.  The couple had four children.  She was the younger sister of Christopher Casson.\n\nBachelor's Baby: Bachelor's Baby is a 1932 British comedy film directed by Harry Hughes and starring Ann Casson, William Freshman and Henry Wenman.  It was made by British International Pictures at Elstree Studios.\n\nI Have Been Here Before: I Have Been Here Before is a play by J. B. Priestley, first produced by Lewis Casson at the Royalty Theatre, London, on 22 September 1937.\n\nLewis Casson: Sir Lewis Thomas Casson MC (26 October 187516 May 1969) was a British actor and theatre director, and the husband of actress Dame Sybil Thorndike.\n\nQuestion: What made Ann Casson similar to Lewis Casson?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"shared_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession shared by both individuals.\"\n    },\n    \"relationship_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of relationship between the two individuals, e.g., 'family'.\"\n    },\n    \"individual_a\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first individual.\"\n        },\n        \"role_in_relationship\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the first individual in the family relationship to the second.\"\n        },\n        \"occupation\": {\n          \"type\": \"string\",\n          \"description\": \"The primary occupation of the first individual.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_relationship\",\n        \"occupation\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"individual_b\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second individual.\"\n        },\n        \"role_in_relationship\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the second individual in the family relationship to the first.\"\n        },\n        \"occupation\": {\n          \"type\": \"string\",\n          \"description\": \"The primary occupation of the second individual.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role_in_relationship\",\n        \"occupation\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"common_ground_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the commonality between the two individuals.\"\n    }\n  },\n  \"required\": [\n    \"shared_profession\",\n    \"relationship_type\",\n    \"individual_a\",\n    \"individual_b\",\n    \"common_ground_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "shared_profession": {
        "type": "string",
        "description": "The profession shared by both individuals."
      },
      "relationship_type": {
        "type": "string",
        "description": "The type of relationship between the two individuals, e.g., 'family'."
      },
      "individual_a": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first individual."
          },
          "role_in_relationship": {
            "type": "string",
            "description": "The role of the first individual in the family relationship to the second."
          },
          "occupation": {
            "type": "string",
            "description": "The primary occupation of the first individual."
          }
        },
        "required": [
          "name",
          "role_in_relationship",
          "occupation"
        ],
        "additionalProperties": false
      },
      "individual_b": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second individual."
          },
          "role_in_relationship": {
            "type": "string",
            "description": "The role of the second individual in the family relationship to the first."
          },
          "occupation": {
            "type": "string",
            "description": "The primary occupation of the second individual."
          }
        },
        "required": [
          "name",
          "role_in_relationship",
          "occupation"
        ],
        "additionalProperties": false
      },
      "common_ground_description": {
        "type": "string",
        "description": "A brief description of the commonality between the two individuals."
      }
    },
    "required": [
      "shared_profession",
      "relationship_type",
      "individual_a",
      "individual_b",
      "common_ground_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
