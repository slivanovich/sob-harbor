{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPierre Womé: Pierre Nlend Womé (born 26 March 1979) is a Cameroonian retired footballer who played as a defender.  A journeyman, Womé was a versatile and skillful left wingback who played for 14 clubs in six countries, being only one of eleven players to have played in the top divisions in Italy, Spain, England and Germany respectively (the others are Jon Dahl Tomasson, Abel Xavier, Gheorghe Popescu, Florin Răducioiu, Pepe Reina, Christian Poulsen, Maniche, Marko Marin, Eduardo Vargas and Obafemi Martins).\n\nSaša Zdjelar: Saša Zdjelar (Serbian Cyrillic: Саша Здјелар; born 20 March 1995) is a Serbian professional footballer who plays for Greek club Olympiacos as a midfielder.\n\nOlympiacos B.C.: Olympiacos B.C. (Greek: ΚΑΕ Ολυμπιακός Σ.Φ.Π. ) , also known simply as Olympiacos or Olympiacos Piraeus, is a Greek professional basketball club, part of the major multi-sport club Olympiacos CFP, based in Piraeus.  The basketball club, founded in 1931, is one of the most successful clubs in European basketball, having won three EuroLeague Championships, one Triple Crown, one Intercontinental Cup, twelve Greek Championships and nine Greek Cups.  They play their home matches at the Peace and Friendship Stadium.\n\nMarko Marin: Marko Marin (Cyrillic: Марко Марин); born 13 March 1989) is a German professional footballer who plays for Greek club Olympiacos as an attacking midfielder and left winger.  He is known for his acceleration, dribbling, agility, creativity, versatility, technical skill and playmaking ability.\n\nDiogo Figueiras: Diogo José Rosário Gomes Figueiras (born 1 July 1991) is a Portuguese professional footballer who plays for Greek club Olympiacos F.C. as a right back.\n\nQazim Laçi: Qazim Laçi (born 19 January 1996) is an Albanian professional footballer who plays as a midfielder for French club Ajaccio on loan from Greek club Olympiacos and the Albania national under-21 football team.\n\nAndré Martins: André Renato Soares Martins (born 21 January 1990 in Santa Maria da Feira, Aveiro District) is a Portuguese professional footballer who plays for Greek club Olympiacos F.C. as a central midfielder.\n\nUroš Đurđević: Uroš Đurđević (Serbian Cyrillic: Урош Ђурђевић; born 2 March 1994) is a Serbian professional footballer who plays as a striker for Greek club Olympiacos.\n\nAlberto Botía: Alberto Tomás Botía Rabasco (] ; born 27 January 1989) is a Spanish professional footballer who plays for Greek club Olympiacos F.C. as a central defender.\n\nOmar Elabdellaoui: Omar Elabdellaoui (born 5 December 1991) is a Norwegian professional footballer who plays for Greek club Olympiacos.  He plays primarily as a right back but can also play as a right midfielder.\n\nQuestion: Pierre Nlend Womé is a Cameroonian retired footballer, who played as a defender, is only one of eleven players to have played in the top divisions in Italy, Spain, England and Germany respectively, who is this German professional footballer, who plays for Greek club Olympiacos?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the professional footballer.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the footballer.\"\n    },\n    \"current_club\": {\n      \"type\": \"string\",\n      \"description\": \"The current club the footballer plays for.\"\n    },\n    \"club_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country of the current club.\"\n    },\n    \"is_one_of_eleven_players\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the player is one of the eleven players who played in the top divisions of Italy, Spain, England, and Germany.\"\n    },\n    \"top_division_countries\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"List of countries whose top divisions the player has played in.\"\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"nationality\",\n    \"current_club\",\n    \"club_country\",\n    \"is_one_of_eleven_players\",\n    \"top_division_countries\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the professional footballer."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the footballer."
      },
      "current_club": {
        "type": "string",
        "description": "The current club the footballer plays for."
      },
      "club_country": {
        "type": "string",
        "description": "The country of the current club."
      },
      "is_one_of_eleven_players": {
        "type": "boolean",
        "description": "Indicates if the player is one of the eleven players who played in the top divisions of Italy, Spain, England, and Germany."
      },
      "top_division_countries": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of countries whose top divisions the player has played in."
      }
    },
    "required": [
      "player_name",
      "nationality",
      "current_club",
      "club_country",
      "is_one_of_eleven_players",
      "top_division_countries"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
