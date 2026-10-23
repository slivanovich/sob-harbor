{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSteven E. de Souza: Steven E. de Souza (born November 17, 1947) is an American screenwriter, producer, and director of film and television widely known for writing blockbuster action films like \"Commando\", \"Die Hard\", \"Hudson Hawk\", and \"Judge Dredd\".  He is among a handful of screenwriters whose films have earned over US$2 billion at the worldwide box office.\n\nJohn Singleton: John Daniel Singleton (born January 6, 1968) is an American film director, screenwriter, and producer best known for directing \"Boyz n the Hood\" (1991).  For the film, he was nominated for the Academy Award for Best Director, becoming the first African American and youngest person to have ever been nominated for the award.  Singleton is a native of South Los Angeles and many of his early films, such as \"Poetic Justice\" (1993), \"Higher Learning\" (1995), and \"Baby Boy\" (2001), consider the implications of inner-city violence.  Some of his other films include dramas such as \"Rosewood\" (1997) in addition to action films such as \"Shaft\" (2000), \"2 Fast 2 Furious\" (2003), and \"Four Brothers\" (2005).\n\nJeb Stuart (writer): Jeb Stuart (born 1956) is an American screenwriter, film director, and producer best known for writing blockbuster action films like \"Die Hard, Lock Up,\" and \"The Fugitive.\"\n\nSantosh Mishra: Santosh Mishra (born 24 August 1978) is a Bhojpuri film director, writer and music composer, known for his works in Hindi, Bhojpuri and Gujarati films.  He is known for directing blockbuster Bhojpuri movies, Patna Se Pakistan, Bam Bam Bol Raha Hai Kashi, Mokama 0 km, Nehlle Pe Dehlla, Nirahua Rickshawala 2 and more than 40 films.\n\nPeter Menzies Jr.: Peter Menzies Jr., A.C.S. is an Australian cinematographer best known for his work on blockbuster action films such as \"Die Hard with a Vengeance\", \"\", \"The Incredible Hulk,\" and \"Clash of the Titans.\"\n\nWhen a Stranger Calls (2006 film): When a Stranger Calls is a 2006 American horror film directed by Simon West and written by Jake Wade Wall.  The film stars Camilla Belle, Brian Geraghty, Katie Cassidy and Clark Gregg.  Camilla Belle plays a babysitter who starts to receive threatening phone calls from an unidentified stranger, played by both Tommy Flanagan and Lance Henriksen.  The film is a remake of Fred Walton's 1979 horror film of the same name which became a cult classic for its legendary opening 20 minutes which this remake extended to a feature length film.\n\nThe Expendables (film series): The Expendables is an American series of action films written by and starring Sylvester Stallone and originally created by David Callaham.  The film series itself was created to pay homage to the blockbuster action films of the 1980s and 90s and also pays gratitude to the action stars of those decades, as well as more recent stars in action.  The series consists of three films: \"The Expendables\" (2010), \"The Expendables 2\" (2012) and \"The Expendables 3\" (2014), with a final fourth film scheduled to be released in 2018.  The series has received mixed critical reception, in regard to its plots and dialogue between the characters; however, many critics praised the use of humor and action scenes.  The films have been box office successes.\n\nAmir Mokri: Amir M. Mokri (Persian: امیر مکری‎ ‎ ; born June 11, 1956) is an Iranian-born American cinematographer known for his work on blockbuster action films such films as \"Bad Boys II\", \"Fast & Furious\", \"Man of Steel\" and \",\" collaborating with directors like Michael Bay, Andrew Niccol, and Zack Snyder.\n\nThe babysitter and the man upstairs: The babysitter and the killer upstairs — also known as the babysitter or the sitter — is an urban legend that dates back to the 1960s about a teenage girl babysitting children who receives telephone calls from a man who continually asks her to \"check the children\".  The basic storyline has been adapted a number of times, including in \"Foster's Release\" (1971), \"O Anjo da Noite\" (1974), \"The Sitter\" (1977), \"When a Stranger Calls\" (1979), \"When a Stranger Calls Back\" (1993), \"When a Stranger Calls\" (2006) and \"Amusement\" (2008).  (\"The Sitter\", \"When a Stranger Calls\", and \"When a Stranger Calls Back\" are all the work of director Fred Walton.)\n\nSimon West: Simon West (born 1961) is an English film director and producer best known for directing blockbuster action films like \"Con Air, ,\" and \"The Expendables 2\".\n\nQuestion: What is the birth year of this English film director and producer best known for directing blockbuster action films, including When a Stranger Calls?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film director.\"\n    },\n    \"birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the director.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the director.\"\n    },\n    \"known_for_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of films the director is best known for.\"\n    }\n  },\n  \"required\": [\n    \"director_name\",\n    \"birth_year\",\n    \"nationality\",\n    \"known_for_genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_name": {
        "type": "string",
        "description": "The name of the film director."
      },
      "birth_year": {
        "type": "integer",
        "description": "The birth year of the director."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the director."
      },
      "known_for_genre": {
        "type": "string",
        "description": "The genre of films the director is best known for."
      }
    },
    "required": [
      "director_name",
      "birth_year",
      "nationality",
      "known_for_genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
