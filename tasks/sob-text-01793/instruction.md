{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSoul Assassin: Soul Assassin is a 2001 thriller film starring Rena Owen, Kristy Swanson and Skeet Ulrich.  The film is about a young security agent, Kevin Burke, who is employed by a multinational banking firm.  He intends to ask his girlfriend Rosalind to marry him.  His girlfriend, however, is brutally murdered by a hitman.  Kevin then swears to avenge Rosalind's death.\n\nBrittany Murphy: Brittany Murphy-Monjack (born Brittany Anne Bertolotti; November 10, 1977 – December 20, 2009), known professionally as Brittany Murphy, was an American actress and singer.  A native of Atlanta, Murphy moved to Los Angeles as a teenager and pursued a career in acting.  Her breakthrough role was as Tai Frasier in \"Clueless\" (1995), followed by supporting roles in independent films such as \"Freeway\" (1996) and \"Bongwater\" (1998).  She made her stage debut in a Broadway production of Arthur Miller's \"A View from the Bridge\" in 1997, before appearing as Daisy Randone in \"Girl, Interrupted\" (1999) and as Lisa Swenson in \"Drop Dead Gorgeous\" (1999).\n\nDisclosure (film): Disclosure is a 1994 American erotic thriller film directed by Barry Levinson, starring Michael Douglas and Demi Moore.  It is based on Michael Crichton's novel of the same name.  The cast also includes Donald Sutherland, Rosemary Forsyth and Dennis Miller.  The film is a combination thriller and slight mystery in an office setting within the computer industry in the mid-1990s.  The main focus of the story, from which the film and book take their titles, is the issue of sexual harassment and its power structure.\n\nSanctuary (2002 film): Sanctuary is a 2001 thriller film written and directed by Katt Shea from a book by Nora Roberts.  It stars Melissa Gilbert and Costas Mandylor.\n\nAntitrust (film): Antitrust (also titled Conspiracy.com and Startup) is a 2001 thriller film written by Howard Franklin and directed by Peter Howitt.\n\nThy Neighbor's Wife (film): Thy Neighbour's Wife is a 2001 thriller film directed by Jim Wynorski.\n\nThe China Syndrome: The China Syndrome is a 1979 American thriller film directed by James Bridges and written by Bridges, Mike Gray, and T. S. Cook.  It tells the story of a television reporter and her cameraman who discover safety coverups at a nuclear power plant.  It stars Jane Fonda, Jack Lemmon, and Michael Douglas, with Douglas also serving as the film's producer.  The cast also features Scott Brady, James Hampton, Peter Donat, Richard Herd, and Wilford Brimley.\n\nDon't Say a Word: Don't Say a Word is a 2001 American psychological thriller film starring Michael Douglas, Brittany Murphy and Sean Bean based on the novel of the same title by Andrew Klavan.  \"Don't Say a Word\" was directed by Gary Fleder and written by Anthony Peckham and Patrick Smith Kelly.\n\nProtection (film): Protection is a 2001 thriller film directed by John Flynn.  In this movie, a former mobster, now in the Witness Protection Program, finds himself unable to change his ways.  Filming took place in Canada.  It was Flynn's last movie.\n\nPicture Claire: Picture Claire is a 2001 thriller film directed by Bruce McDonald of a screenplay by Semi Chellas.  The film stars Juliette Lewis, Gina Gershon, Callum Keith Rennie, Kelly Harms, Camilla Rutherford, Peter Stebbings, and Mickey Rourke.  The film premiered at the Toronto International Film Festival, and also appeared at Cinéfest in Sudbury, where the film received Best Ontario Feature Award.\n\nQuestion: The actress that played Tai Frasier in \"Clueless\" also stars with Michael Douglas in a 2001 thriller film based on a novel by what author?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actress.\"\n        },\n        \"breakthrough_role\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"film_title\": {\n              \"type\": \"string\",\n              \"description\": \"The title of the film where the actress had her breakthrough role.\"\n            },\n            \"character_name\": {\n              \"type\": \"string\",\n              \"description\": \"The name of the character played by the actress in her breakthrough role.\"\n            }\n          },\n          \"required\": [\n            \"film_title\",\n            \"character_name\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"breakthrough_role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"related_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the 2001 thriller film starring the actress and Michael Douglas.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        },\n        \"co_star_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the co-star mentioned in the question (Michael Douglas).\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"genre\",\n        \"co_star_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"novel_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_based_on_novel\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the film is based on a novel.\"\n        },\n        \"author_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the author of the novel the film is based on.\"\n        }\n      },\n      \"required\": [\n        \"is_based_on_novel\",\n        \"author_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The final answer to the question: the author's name.\"\n    }\n  },\n  \"required\": [\n    \"actress_details\",\n    \"related_film_details\",\n    \"novel_details\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the actress."
          },
          "breakthrough_role": {
            "type": "object",
            "properties": {
              "film_title": {
                "type": "string",
                "description": "The title of the film where the actress had her breakthrough role."
              },
              "character_name": {
                "type": "string",
                "description": "The name of the character played by the actress in her breakthrough role."
              }
            },
            "required": [
              "film_title",
              "character_name"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "breakthrough_role"
        ],
        "additionalProperties": false
      },
      "related_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the 2001 thriller film starring the actress and Michael Douglas."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          },
          "co_star_name": {
            "type": "string",
            "description": "The name of the co-star mentioned in the question (Michael Douglas)."
          }
        },
        "required": [
          "title",
          "release_year",
          "genre",
          "co_star_name"
        ],
        "additionalProperties": false
      },
      "novel_details": {
        "type": "object",
        "properties": {
          "is_based_on_novel": {
            "type": "boolean",
            "description": "Indicates if the film is based on a novel."
          },
          "author_name": {
            "type": "string",
            "description": "The name of the author of the novel the film is based on."
          }
        },
        "required": [
          "is_based_on_novel",
          "author_name"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "string",
        "description": "The final answer to the question: the author's name."
      }
    },
    "required": [
      "actress_details",
      "related_film_details",
      "novel_details",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
