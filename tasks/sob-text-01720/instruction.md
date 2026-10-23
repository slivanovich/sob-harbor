{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSee You in the Morning (film): See You in the Morning is a 1989 American romantic comedy film written and directed by Alan J. Pakula, and starring Jeff Bridges, Alice Krige and Farrah Fawcett.  It features music by Nat King Cole and Cherri Red.  The film's music was composed by Michael Small.\n\nLove and Pain and the Whole Damn Thing: Love and Pain and the Whole Damn Thing is a 1973 American comedy-drama film directed by Alan J. Pakula.  It is often categorized as a drama, but contains many comic elements.  Maggie Smith and Timothy Bottoms star.\n\nAlan J. Pakula: Alan Jay Pakula ( ; April 7, 1928 – November 19, 1998) was an American film director, writer and producer.  He was nominated for three Academy Awards: Best Picture for \"To Kill a Mockingbird\" (1962), Best Director for \"All the President's Men\" (1976) and Best Adapted Screenplay for \"Sophie's Choice\" (1982).\n\nComes a Horseman: Comes a Horseman is a 1978 American western drama film starring Jane Fonda, James Caan, Jason Robards, and Richard Farnsworth, directed by Alan J. Pakula.\n\nRobert Mulligan: Robert Patrick Mulligan (August 23, 1925 – December 20, 2008) was an American film and television director best known as the director of humanistic American dramas, including \"To Kill a Mockingbird\" (1962), \"Summer of '42\" (1971), \"The Other\" (1972), \"Same Time, Next Year\" (1978) and \"The Man in the Moon\" (1991).  He was also known in the 1960s for his extensive collaborations with producer Alan J. Pakula.  He was the elder brother of actor Richard Mulligan.\n\nPresumed Innocent (film): Presumed Innocent is a 1990 American legal drama film based on the 1987 novel of the same name by Scott Turow.  Directed by Alan J. Pakula, and written by Pakula and Frank Pierson, it stars Harrison Ford, Brian Dennehy, Raúl Juliá, Bonnie Bedelia, Paul Winfield and Greta Scacchi.  \"Presumed Innocent\" follows Rusty Sabich (Ford), a prosecutor who is charged with the murder of his colleague and mistress Carolyn Polhemus (Scacchi).\n\nThe Pelican Brief (film): The Pelican Brief is a 1993 American legal political thriller based on the novel of the same name by John Grisham.  Directed by Alan J. Pakula, the film stars Julia Roberts in the role of young law student Darby Shaw and Denzel Washington as \"Washington Herald\" reporter Gray Grantham.  The film, which features music composed by James Horner, was the last film that featured Pakula as a writer or producer before his death.\n\nSam Mendes: Samuel Alexander Mendes, {'1': \", '2': \", '3': \", '4': \"} (born 1 August 1965) is an English stage and film director.  He is best known for directing the drama film \"American Beauty\" (1999), which earned him the Academy Award and Golden Globe Award for Best Director, the crime film \"Road to Perdition\" (2002), and the \"James Bond\" films \"Skyfall\" (2012) and \"Spectre\" (2015).\n\nOrphans (1987 film): Orphans is a 1987 American drama film directed by Alan J. Pakula.  It was written by Lyle Kessler, based on his play of the same name. \n\nNeal Street Productions: Neal Street Productions is a British film, television and theatre production company.  The company was set up in 2003 by Sam Mendes, Pippa Harris and Caro Newling.  Nicolas Brown joined in 2013 to work across the film and TV portfolio.  The company's movies include \"Revolutionary Road\", \"Jarhead\" and \"Starter for 10\".  Their TV dramas include the award-winning \"Stuart: A Life Backwards\" with Tom Hardy and Benedict Cumberbatch, \"Penny Dreadful\" and \"Call the Midwife\".  In theatre Neal Street has produced \"The Bridge Project\", \"Shrek the Musical\" and the London West End musical of \"Charlie and the Chocolate Factory\", directed by Sam Mendes.\n\nQuestion: Alan J. Pakula and Sam Mendes, have which occupation in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person.\"\n    },\n    \"person_1_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations for the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person.\"\n    },\n    \"person_2_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations for the second person.\"\n    },\n    \"common_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The occupation shared by both individuals.\"\n    },\n    \"occupation_category\": {\n      \"type\": \"string\",\n      \"description\": \"The category of the common occupation (e.g., 'film', 'stage').\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_1_occupations\",\n    \"person_2_name\",\n    \"person_2_occupations\",\n    \"common_occupation\",\n    \"occupation_category\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person."
      },
      "person_1_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations for the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person."
      },
      "person_2_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations for the second person."
      },
      "common_occupation": {
        "type": "string",
        "description": "The occupation shared by both individuals."
      },
      "occupation_category": {
        "type": "string",
        "description": "The category of the common occupation (e.g., 'film', 'stage')."
      }
    },
    "required": [
      "person_1_name",
      "person_1_occupations",
      "person_2_name",
      "person_2_occupations",
      "common_occupation",
      "occupation_category"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
