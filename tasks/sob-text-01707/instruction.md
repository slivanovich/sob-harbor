{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCéleste (film): Céleste is a 1982 German film by Percy Adlon about the life of the French writer Marcel Proust as he lay in his bed from 1912 to 1922; the story is told through the eyes of his real life maid, Céleste Albaret.  She waited decades before writing her own book about the experience which was adapted for the screen by Percy Adlon.\n\nYounger and Younger: Younger And Younger is 1993 American comedy film directed by Percy Adlon.\n\nMax Marcin: Max Marcin (5 May 1879 – 30 March 1948) was a Polish screenwriter and film director.  He wrote for 47 films between 1916 and 1949.  He also directed six films between 1931 and 1936.  His stage work includes \"See My Lawyer\" (1915), directed by Frank M. Stammers; he wrote and/or produced almost 20 plays for Broadway from 1916-38.  Marcin wrote for and produced \"The FBI in Peace and War\" and created, produced and wrote for the \"Crime Doctor\" radio program, which became the basis for a series of 10 \"Crime Doctor\" films.\n\nSalmonberries: Salmonberries is a 1991 drama film directed by Percy Adlon and written by Adlon and his son Felix.  It stars k.d. lang as Kotzebue, a young woman of androgynous appearance who works as a (male) miner in Alaska, and Rosel Zech as Roswitha, an East German immigrant and librarian.  The film takes place in Kotzebue, Alaska and Berlin, Germany, shortly after reunification; the dialog is mostly English but includes some German with English subtitles.\n\nMahler on the Couch: Mahler on the Couch (German: Mahler auf der Couch ) is a 2010 German film directed by Percy Adlon and Felix Adlon.  It is an historical drama depicting an affair between Alma Mahler and Walter Gropius, and the subsequent psychoanalysis of Mahler's husband Gustav Mahler by Sigmund Freud.\n\nKing of the Jungle (1933 film): King of the Jungle is a 1933 American Pre-Code adventure film directed by H. Bruce Humberstone and Max Marcin and written by Charles Thurley Stoneham, Max Marcin, Fred Niblo, Jr. and Philip Wylie.  The film stars Buster Crabbe, Frances Dee, Sidney Toler, Nydia Westman, Robert Barrat, Irving Pichel and Douglass Dumbrille.  The film was released on March 10, 1933, by Paramount Pictures.\n\nThe Lawyer's Secret: The Lawyer's Secret is a 1931 American Pre-Code crime film directed by Louis J. Gasnier and Max Marcin and written by Lloyd Corrigan, James Hilary Finn and Max Marcin.  The film stars Clive Brook, Charles 'Buddy' Rogers, Richard Arlen, Fay Wray, Jean Arthur, Francis McDonald and Harold Goodwin.  The film was released on June 6, 1931, by Paramount Pictures.\n\nPercy Adlon: Paul Rudolf Parsifal \"Percy\" Adlon (] ; born 1 June 1935) is a German director, screenwriter, and producer.  He is best known for his film \"Bagdad Café\".  He is associated with the New German Cinema movement, whose \"members\" also include Werner Herzog and the illustrious Rainer Werner Fassbinder.\n\nThe Strange Case of Clara Deane: The Strange Case of Clara Deane is a 1932 American Pre-Code drama film directed by Louis J. Gasnier and Max Marcin and written by Max Marcin.  The film stars Wynne Gibson, Pat O'Brien, Dudley Digges, Frances Dee, George Barbier, Russell Gleason and Lee Kohlmar.  The film was released on May 6, 1932, by Paramount Pictures.\n\nSilence (1931 film): Silence is a 1931 American Pre-Code crime film directed by Louis J. Gasnier and Max Marcin and written by Max Marcin.  The film stars Clive Brook, Marjorie Rambeau, Peggy Shannon, Charles Starrett, Willard Robertson, John Wray and Frank Sheridan.  It was released on August 29, 1931, by Paramount Pictures.\n\nQuestion: What job did both Percy Adlon and Max Marcin have?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_names\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The names of the individuals being compared.\"\n    },\n    \"common_job_title\": {\n      \"type\": \"string\",\n      \"description\": \"The job title that both individuals held.\"\n    },\n    \"job_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"percy_adlon_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"All known job roles for Percy Adlon.\"\n        },\n        \"max_marcin_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"All known job roles for Max Marcin.\"\n        }\n      },\n      \"required\": [\n        \"percy_adlon_roles\",\n        \"max_marcin_roles\"\n      ],\n      \"additionalProperties\": false,\n      \"description\": \"Detailed breakdown of job roles for each person.\"\n    }\n  },\n  \"required\": [\n    \"person_names\",\n    \"common_job_title\",\n    \"job_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_names": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The names of the individuals being compared."
      },
      "common_job_title": {
        "type": "string",
        "description": "The job title that both individuals held."
      },
      "job_details": {
        "type": "object",
        "properties": {
          "percy_adlon_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All known job roles for Percy Adlon."
          },
          "max_marcin_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "All known job roles for Max Marcin."
          }
        },
        "required": [
          "percy_adlon_roles",
          "max_marcin_roles"
        ],
        "additionalProperties": false,
        "description": "Detailed breakdown of job roles for each person."
      }
    },
    "required": [
      "person_names",
      "common_job_title",
      "job_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
