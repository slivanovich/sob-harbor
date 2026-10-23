{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTitanic: The Complete Story: Titanic: The Complete Story is an American documentary chronicling the story of the ocean liner RMS Titanic which sank on its maiden voyage in 1912.  This is a compilation of a four-hour documentary special produced by A&E Television Networks in 1994.  A&E Home Video originally sold the entire documentary in a 4-tape VHS set.  It is considered by many critics and historians to be the definitive documentary regarding the \"Titanic\".\n\nAlice Cleaver: Alice Catherine Cleaver was a survivor of the \"RMS Titanic\" and nursemaid for the Allison family, wealthy insurance moguls from Canada during the early 20th century.  She is best known for rescuing the youngest Allison child, Trevor, from the \"Titanic\".  Little is known about her later life, as she refused to give interviews after surviving the shipwreck.  She was the subject of books and movies that misidentified her as Alice Mary Cleaver, a woman who was infamous for murdering her own infant.\n\nJames Joseph Brown: James Joseph \"J.J.\" Brown (September 27, 1854 – September 5, 1922), was an American mining engineer, inventor, and self-made member of fashionable \"society\".  His wife was \"RMS Titanic\" survivor Molly Brown.\n\nThe Legend of the Titanic: The Legend of the Titanic (Spanish: La leyenda del Titanic , Italian: La leggenda del Titanic ) is a 1999 Italian animated film directed by Orlando Corradi and Kim J. Ok.  The film is a very loose adaptation of the RMS Titanic sinking and featured several fantasy elements such as anthropomorphic animals.\n\nTitanic Canyon: Titanic Canyon is a submarine canyon located south of the Grand Banks of Newfoundland, Canada.  Its name was proposed in 1991 by marine geologist Alan Ruffman for the remembrance of British passenger liner RMS Titanic, the wreck of which lies about 34 km south of the head of Titanic Canyon on its eastern slope.\n\nMartin Bayerle: Captain Martin Gerard Bayerle (born April 23, 1951) is an American treasure hunter and author, best known for finding the 1909 shipwreck of the White Star Liner RMS Republic.  He is also star of the History Channel show \"Billion Dollar Wreck.\"  The \"Republic\" was the largest ship to sink in history to her day, only to be eclipsed by the loss of RMS Titanic in 1912.  Capt. Bayerle and his company, Martha's Vineyard Scuba Headquarters, Inc. (\"MAVIS\") were referred to as \"modern day pirates\" by Judge Nancy Gertner of the United States District Court, District of Massachusetts in a 2005 opinion granting exclusive salvage rights to the \"Republic\" to MAVIS.  MAVIS subsequently acquired legal title to the RMS Republic shipwreck and her contents in August 2011, with the U.S. District Court of Boston also barring all future claims.\n\nEdward Kamuda: Edward Stephen Kamuda (November 10, 1939 – April 13, 2014) was an American historian who specialized in the study of the RMS Titanic.  The Titanic sank on April 14, 1912, after striking an iceberg in the north Atlantic Ocean.  Kamuda devoted much of his life to the preservation of the Titanic's legacy as the founder and president of the Titanic Historical Society.  Much of his research focused on the biographies of the crew and passengers of the RMS Titanic.\n\nThe Titanic (song): \"The Titanic\" (also known as \"It Was Sad When That Great Ship Went Down\" and \"Titanic (Husbands and Wives)\") is a folk song and children's song most known for being sung in the United States at summer camp.  \"The Titanic\" is about the sinking of the RMS Titanic which sank on April 15, 1912 after striking an iceberg.\n\nAvoca Lodge: Avoca Lodge, known as The Molly Brown Summer House, is a Registered Historic Place in southwest Denver, Colorado near Bear Creek.  The home served as a summer retreat for philanthropist, socialite, and activist Margaret Brown and her husband James Joseph Brown.  It is open to the public rental and for tours.\n\nDistant Waves: Distant Waves is a novel using the RMS Titanic as much of its setting.  It is not a story completely of the Titanic, it mixes fiction with real people that were alive during the Titanic era.\n\nQuestion: In which persons name the Avoca Lodge is known who is the wife of James Joseph Brown and \"RMS Titanic\" survivor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person by whom the Avoca Lodge is known.\"\n    },\n    \"person_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the person.\"\n        },\n        \"other_known_names\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other names or aliases the person is known by.\"\n        },\n        \"is_rms_titanic_survivor\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the person was a survivor of the RMS Titanic.\"\n        },\n        \"is_wife_of_james_joseph_brown\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the person is the wife of James Joseph Brown.\"\n        },\n        \"roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Key roles or descriptions of the person.\"\n        }\n      },\n      \"required\": [\n        \"full_name\",\n        \"is_rms_titanic_survivor\",\n        \"is_wife_of_james_joseph_brown\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"lodge_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The official name of the lodge.\"\n        },\n        \"known_as_alternative\": {\n          \"type\": \"string\",\n          \"description\": \"The alternative name by which the lodge is known, incorporating the person's name.\"\n        },\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the lodge's location.\"\n        },\n        \"purpose\": {\n          \"type\": \"string\",\n          \"description\": \"The primary purpose or function of the lodge.\"\n        },\n        \"is_registered_historic_place\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the lodge is a Registered Historic Place.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"known_as_alternative\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_attributes\",\n    \"lodge_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person by whom the Avoca Lodge is known."
      },
      "person_attributes": {
        "type": "object",
        "properties": {
          "full_name": {
            "type": "string",
            "description": "The full name of the person."
          },
          "other_known_names": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other names or aliases the person is known by."
          },
          "is_rms_titanic_survivor": {
            "type": "boolean",
            "description": "Indicates if the person was a survivor of the RMS Titanic."
          },
          "is_wife_of_james_joseph_brown": {
            "type": "boolean",
            "description": "Indicates if the person is the wife of James Joseph Brown."
          },
          "roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Key roles or descriptions of the person."
          }
        },
        "required": [
          "full_name",
          "is_rms_titanic_survivor",
          "is_wife_of_james_joseph_brown"
        ],
        "additionalProperties": false
      },
      "lodge_information": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The official name of the lodge."
          },
          "known_as_alternative": {
            "type": "string",
            "description": "The alternative name by which the lodge is known, incorporating the person's name."
          },
          "location_description": {
            "type": "string",
            "description": "A description of the lodge's location."
          },
          "purpose": {
            "type": "string",
            "description": "The primary purpose or function of the lodge."
          },
          "is_registered_historic_place": {
            "type": "boolean",
            "description": "Indicates if the lodge is a Registered Historic Place."
          }
        },
        "required": [
          "name",
          "known_as_alternative"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "person_name",
      "person_attributes",
      "lodge_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
