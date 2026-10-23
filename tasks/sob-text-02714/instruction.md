{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMichael Crichton: John Michael Crichton ( ; October 23, 1942 – November 4, 2008) was an American best-selling author, screenwriter, film director and producer best known for his work in the science fiction, medical fiction and thriller genres.  His books have sold over 200 million copies worldwide, and many have been adapted into films.\n\nThe Man Who Loved Women (1983 film): The Man Who Loved Women is a 1983 American comedy film directed by Blake Edwards and starring Burt Reynolds, Julie Andrews and Kim Basinger.  It is a remake of the 1977 French film \"L'Homme qui aimait les femmes\".\n\nCloud 9 (2006 film): Cloud 9 is a 2006 American sports comedy film starring Burt Reynolds that was written and produced by Brett Hudson, Burt Kearns and Academy Award-winning producer (\"The Godfather\", \"Million Dollar Baby\") Albert S. Ruddy.  It was the last comedy in which Reynolds reprised and updated his role as the charming rascal made legendary in films like \"The Longest Yard\" and \"Smokey and the Bandit\".\n\nW.W. and the Dixie Dancekings: W.W. and the Dixie Dancekings is a 1975 American comedy film directed by John G. Avildsen, starring Burt Reynolds, and written by Thomas Rickman.  The 20th Century Fox film features the acting debut of Jerry Reed.\n\nRent-a-Cop (film): Rent-a-Cop is a 1987 American comedy crime film starring Burt Reynolds and Liza Minnelli.  Reynolds plays a disgraced police officer, now working as a security guard, who falls in love with Minnelli, who plays a prostitute.\n\nShark!: Shark!  (also known as \"Caine \"and\" Maneater\") is a 1969 American action film directed by Samuel Fuller and starring Burt Reynolds.  The film was based on the Victor Canning novel \"His Bones are Coral\" with the original screenplay written by Ken Hughes.  When Fuller joined the project, he rewrote the script and retitled it \"Caine\".\n\nPhysical Evidence: Physical Evidence is a 1989 American crime thriller film directed by Michael Crichton (in his final film as a director), and stars Burt Reynolds, Theresa Russell and Ned Beatty.  It follows an ex-police officer who is incriminated by the evidence, but insists on his innocence.\n\nThe Last Producer: The Last Producer is a 2000 American drama film directed by and starring Burt Reynolds.  It also featured Sean Astin, Ann-Margret, Lauren Holly, Rod Steiger, and Benjamin Bratt.  It was also referred to as \"The Final Hit\" in final packaging and promotional materials.\n\nLarry L. King: Larry L. King (January 1, 1929 –December 20, 2012) was an American playwright, journalist, and novelist, best remembered for his 1978 Tony Award-nominated play \"The Best Little Whorehouse in Texas\", which became a long-running production on Broadway and was later turned into a feature film starring Burt Reynolds, Charles Durning and Dolly Parton.\n\nHawk (TV series): Hawk is a crime drama series starring Burt Reynolds, which aired on ABC from September 8, 1966 to December 29, 1966.  The series was Reynolds' first starring role in a television series since leaving \"Gunsmoke\" the previous year.\n\nQuestion: Physical Evidence starring Burt Reynolds was the last film directed by which celebrated thriller and sci-fi novelist?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in question.\"\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the director.\"\n        },\n        \"genres_known_for\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Genres the director is known for as an author/filmmaker.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"genres_known_for\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_starring\": {\n      \"type\": \"string\",\n      \"description\": \"The main actor mentioned in the question.\"\n    },\n    \"director_specific_role\": {\n      \"type\": \"string\",\n      \"description\": \"A specific detail about the director's role related to this film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director\",\n    \"actor_starring\",\n    \"director_specific_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film in question."
      },
      "director": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the director."
          },
          "genres_known_for": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Genres the director is known for as an author/filmmaker."
          }
        },
        "required": [
          "name",
          "genres_known_for"
        ],
        "additionalProperties": false
      },
      "actor_starring": {
        "type": "string",
        "description": "The main actor mentioned in the question."
      },
      "director_specific_role": {
        "type": "string",
        "description": "A specific detail about the director's role related to this film."
      }
    },
    "required": [
      "film_title",
      "director",
      "actor_starring",
      "director_specific_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
