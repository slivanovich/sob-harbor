{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nYou Must Love Me: \"You Must Love Me\" is a song recorded by American singer and songwriter Madonna.  It was written by Andrew Lloyd Webber and Tim Rice, for the 1996 film adaptation of the musical, \"Evita\", based on the life of Argentinian leader Eva Perón.  The song was released on October 27, 1996, by Warner Bros. as the lead single from the film's soundtrack.  After years of not working together due to their individual projects, Webber and Rice collaborated on creating a new track for the film, with the hopes of obtaining an Academy Award nomination for Best Original Song.  According to Webber, the song's main inspiration was to showcase Perón's emotional state at the time as well as her relationship with husband Juan Perón.\n\nEvita (soundtrack): Evita is the third soundtrack album by American singer Madonna.  It was released on November 12, 1996, by Warner Bros.  Records to promote the 1996 American musical drama film, \"Evita\".  The film was based on Tim Rice and Andrew Lloyd Webber's 1978 musical of the same name, about First Lady of Argentina, Eva Perón.  Additional performers on \"Evita\" include Antonio Banderas, Jonathan Pryce and Jimmy Nail, but it is considered a Madonna album since she sang majority of the songs.  After securing the title role in \"Evita\", Madonna underwent vocal training in order to enhance her singing abilities.  Director Alan Parker worked with Rice and Lloyd Webber to compose the soundtrack, reworking the original songs as well as write a new song, \"You Must Love Me\", for the film.\n\nEvita (1996 film): Evita is a 1996 American musical drama film based on the 1976 concept album of the same name produced by Tim Rice and Andrew Lloyd Webber, which also inspired a 1978 musical.  The film depicts the life of Eva Perón, detailing her beginnings, rise to fame, political career and death at the age of 33.  Directed by Alan Parker, and written by Parker and Oliver Stone, \"Evita\" stars Madonna as Eva, Jonathan Pryce as Eva's husband Juan Perón, and Antonio Banderas as Ché, an everyman who acts as the film's narrator.\n\nEvita (musical): Evita is a musical with music by Andrew Lloyd Webber and lyrics by Tim Rice.  It concentrates on the life of Argentine political leader Eva Perón, the second wife of Argentine president Juan Perón.  The story follows Evita's early life, rise to power, charity work, and eventual death.\n\nDon't Cry for Me Argentina: \"Don't Cry for Me Argentina\" is a song recorded by Julie Covington for the 1976 concept album, \"Evita\", and was later included in the 1978 musical of the same name.  The song was written and composed by Andrew Lloyd Webber and Tim Rice while they were researching the life of Argentinian leader Eva Perón.  It appeared at the opening and near the end of the show, initially as the spirit of the dead Eva exhorting the people of Argentina not to mourn her, and finally during Eva's speech from the balcony of Casa Rosada.  Covington was signed by the songwriters for the track, based on her previous work in musicals.\n\nList of accolades received by Evita (1996 film): \"Evita\" is a 1996 American musical drama film based on Tim Rice and Andrew Lloyd Webber's musical of the same name about First Lady of Argentina, Eva Perón.  Directed by Alan Parker and written by Parker and Oliver Stone, the film starred Madonna, Antonio Banderas, and Jonathan Pryce in the leading roles of Eva, Ché and Juan Perón respectively.  Rice and Webber composed the film's musical score, while Darius Khondji was the cinematographer.  Vincent Paterson created the choreography for the film and Gerry Hambling was responsible for editing.  Penny Rose designed and created the period costumes for the film, and Brian Morris was the set designer.\n\nThe Woman with the Whip: The Woman with the Whip is a 1952 biography of political leader Eva Perón, the late First Lady and Spiritual Leader of the Nation of Argentina.  Published in England and the United States shortly after Eva Perón's death, it was the first hostile biography of Eva Perón to be published and, despite the criticism that it is lacking in historical value, has therefore been used by her detractors ever since.  This book is thought to be the basis for the Andrew Lloyd Webber and Tim Rice musical \"Evita\".  However, the book was never officially credited as such, and Rice incorporated many other historical materials as background.\n\nEvita (album): Evita is a concept album released in 1976 and produced by Andrew Lloyd Webber and Tim Rice.  Having successfully launched their previous show, \"Jesus Christ Superstar\", on record in 1970, Lloyd Webber and Rice returned to the format for \"Evita\".  The album was recorded at Olympic Studios in London from April to September 1976 and released in the United Kingdom on 19 November 1976.\n\nAnother Suitcase in Another Hall: \"Another Suitcase in Another Hall\" is a song recorded by Scottish singer Barbara Dickson, for the 1976 concept album, \"Evita\", the basis of the musical of the same name.  The musical was based on the life of Argentinian leader Eva Perón.  Written by Tim Rice and Andrew Lloyd Webber, the song is presented during a sequence where Eva throws out her husband's mistress on the streets.  The latter sings the track, wondering about her future and coming to the conclusion that she would be fine.  Dickson was enlisted by the songwriters to record the track after hearing her previous work.\n\nOh What a Circus: \"Oh What a Circus\" is a song from the 1976 musical \"Evita\", written by Andrew Lloyd Webber and Tim Rice, and music composed by Webber.  It was recorded by English singer David Essex and released as a single on August 19, 1978, by Mercury Records.  Essex had played the character of Che in the musical based on Che Guevara, and the song is sung from Che's point-of-view.  Produced and arranged by Mike Batt, \"Oh What a Circus\" is a mid-tempo song, comparing the musical's title character Eva Perón's life with a circus, and calling her actions fraudulent.  The song is a contrafactum, and shares its tune with the better known \"Don't Cry for Me Argentina\" from the same show.\n\nQuestion: What 1996 American musical drama film based on a concept album released in 1976 and produced by Andrew Lloyd Webber and Tim Rice,  depicts the life of Eva Perón?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the film was released.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        },\n        \"director\": {\n          \"type\": \"string\",\n          \"description\": \"The director of the film.\"\n        },\n        \"main_subject\": {\n          \"type\": \"string\",\n          \"description\": \"The historical figure whose life the film depicts.\"\n        }\n      },\n      \"required\": [\n        \"release_year\",\n        \"genre\",\n        \"director\",\n        \"main_subject\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"source_material\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"source_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of source material the film is based on.\"\n        },\n        \"album_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the concept album.\"\n        },\n        \"album_release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the concept album.\"\n        },\n        \"album_producers\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The producers of the concept album.\"\n        }\n      },\n      \"required\": [\n        \"source_type\",\n        \"album_title\",\n        \"album_release_year\",\n        \"album_producers\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_details\",\n    \"source_material\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "release_year": {
            "type": "integer",
            "description": "The year the film was released."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          },
          "director": {
            "type": "string",
            "description": "The director of the film."
          },
          "main_subject": {
            "type": "string",
            "description": "The historical figure whose life the film depicts."
          }
        },
        "required": [
          "release_year",
          "genre",
          "director",
          "main_subject"
        ],
        "additionalProperties": false
      },
      "source_material": {
        "type": "object",
        "properties": {
          "source_type": {
            "type": "string",
            "description": "The type of source material the film is based on."
          },
          "album_title": {
            "type": "string",
            "description": "The title of the concept album."
          },
          "album_release_year": {
            "type": "integer",
            "description": "The release year of the concept album."
          },
          "album_producers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The producers of the concept album."
          }
        },
        "required": [
          "source_type",
          "album_title",
          "album_release_year",
          "album_producers"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_details",
      "source_material"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
