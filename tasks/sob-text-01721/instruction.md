{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBriana Loves Jenna: Briana Loves Jenna is a 2001 pornographic film starring Briana Banks and Jenna Jameson, written and directed by Jay Grdina under the stage name \"Justin Sterling\".\n\nSheila Kennedy: Sheila Kennedy (born April 12, 1962) is a model and actress who was the December 1981 Penthouse Pet of the Month and the 1983 Pet of the Year.\n\nChanel Preston: Chanel Preston (born December 1, 1985) is an American pornographic actress and the \"Penthouse\" magazine Penthouse Pet for March 2012.  She entered the adult film industry in 2010 at the age of 24.\n\nBriana Banks: Briana Banks (born May 21, 1978) is the stage name of a German American pornographic actress and model.  She is the \"Penthouse\" Pet of the Month for June 2001.\n\nNikki Benz: Alla Montchak (Russian: А́лла Монча́к , born December 11, 1981), better known by her stage name Nikki Benz, is a Ukrainian Canadian pornographic actress.  She was also a 2010 Penthouse Pet who was selected as the 2011 Pet of the Year.\n\nSamantha Saint: Samantha Saint (born June 8, 1987) is the stage name of an American pornographic actress, model and Penthouse Pet of the Month for October 2012.\n\nVictoria Zdrok: Victoria Nika Zdrok (Ukrainian: Вікторія Здрок ; born March 3, 1973) is a pornographic performer, author, and model of Ukrainian origin.  She is \"Playboy's\" Playmate for October 1994.  In June 2002 she became \"Penthouse\" magazine's Pet of the Month, later being chosen as their 2004 Penthouse Pet of the Year.  Zdrok is also a non-practicing attorney, a clinical psychologist and sex therapist.\n\nFrankenhooker: Frankenhooker is a 1990 American black comedy horror directed by Frank Henenlotter.  Very loosely inspired by Mary Shelley's novel \"Frankenstein\", the film stars James Lorinz as medical school drop-out Jeffrey Franken and former Penthouse Pet Patty Mullen as the title character (who wears a fatsuit in the beginning of the film).\n\nGina Lynn: Gina Lynn (born February 15, 1974) is a Puerto Rican former pornographic actress, model, and stripper.  She was inducted into the AVN Hall of Fame in 2010 and is the \"Penthouse\" magazine Penthouse Pet for April 2012.\n\nHesketh 308E: The Hesketh 308E is a Formula One racing car model built by the Hesketh Racing team in .  The car was designed by Frank Dernie and Nigel Stroud and was the last car built by the Hesketh team before it folded at the end of .  The 308E was a relatively conservative design, with an aluminium monocoque chassis built around the common Cosworth DFV engine and Hewland gearbox combination.  However, the 308E gained particular notoriety owing to Hesketh's team sponsors in 1977 – Penthouse and Rizla – and the resultant livery which incorporated a large rendering of a scantily-clad Penthouse Pet embracing a Rizla packet.  During this year, driver Rupert Keegan managed to qualify the car at every race entered although its best finish was only seventh place at the Austrian Grand Prix.  For 1978 the team reverted to rather less controversial sponsorship from the Olympus Corporation, although results were less dependable.  Following Hesketh's withdrawal from the F1 World Championship the remaining 308Es were run for various competitors in the British Aurora AFX championship.\n\nQuestion: Who starred in a film with the Penthouse Pet for June 2001?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"penthouse_pet_of_month\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Penthouse Pet for the specified month and year.\"\n    },\n    \"pet_month\": {\n      \"type\": \"string\",\n      \"description\": \"The month of the Penthouse Pet selection.\"\n    },\n    \"pet_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year of the Penthouse Pet selection.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film in which the Penthouse Pet starred.\"\n    },\n    \"co_star\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-star who appeared in the film with the Penthouse Pet.\"\n    }\n  },\n  \"required\": [\n    \"penthouse_pet_of_month\",\n    \"pet_month\",\n    \"pet_year\",\n    \"film_title\",\n    \"co_star\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "penthouse_pet_of_month": {
        "type": "string",
        "description": "The name of the Penthouse Pet for the specified month and year."
      },
      "pet_month": {
        "type": "string",
        "description": "The month of the Penthouse Pet selection."
      },
      "pet_year": {
        "type": "integer",
        "description": "The year of the Penthouse Pet selection."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film in which the Penthouse Pet starred."
      },
      "co_star": {
        "type": "string",
        "description": "The name of the co-star who appeared in the film with the Penthouse Pet."
      }
    },
    "required": [
      "penthouse_pet_of_month",
      "pet_month",
      "pet_year",
      "film_title",
      "co_star"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
