{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJean-Patrick Manchette: Jean-Patrick Manchette (19 December 1942, Marseille – 3 June 1995, Paris) was a French crime novelist credited with reinventing and reinvigorating the genre.  He wrote ten short novels in the seventies and early eighties, and is widely recognized as the foremost French crime fiction author of the 1970s - 1980s.  His stories are violent, existentialist explorations of the human condition and French society.  Manchette was politically to the left and his writing reflects this through his analysis of social positions and culture.  His books are reminiscent of the \"nouvelle vague\" crime films of Jean-Pierre Melville, employing a similarly cool, existential style on a typically American genre (film noir for Melville and pulp novels for Manchette).\n\nEk Hasina Thi (TV series): Ek Hasina Thi (English: \"There was a beautiful woman\") is a Crime thriller television series created by Cinevistaas Limited for the channel Star Plus from 14 April 2014 to 20 December 2014.  Produced by Prem Krishen, \"Ek Hasina Thi\" is loosely based on the American series \"Revenge\".  The series has Sanjeeda Sheikh and Vatsal Sheth as leads, and, Simone Singh and Ayub Khan in supportive roles.  The show is set in Kolkata, but is filmed in Mumbai.  The series was earlier titled \"Daag\". The show was acclaimed by critics and viewer and it was one of the most successful show of Star Plus at that time. Simone Singh's performance has been lauded.\n\nCrime Scenes: Crime Scenes (French: \"Scènes de crimes\" ) is a 2000 French crime film directed by Frédéric Schoendoerffer.\n\nThe Informant (2013 film): The Informant (French: Gibraltar , also known as Border Informant) is a 2013 French crime thriller film written and directed by Julien Leclercq.\n\nDominique Manotti: Dominique Manotti (born 1942, in Paris) is a French crime writer and economic historian.  She has written more than a dozen books, many of which have been translated.  Among her many prizes is the 2011 Grand Prix de Littérature Policière, the most prestigious award in French crime fiction.\n\nLe choc: Le choc (English: \"The Shock\" ) is a 1982 French crime thriller film directed by Robin Davis and starring Alain Delon, Catherine Deneuve, and Philippe Léotard.  Based on the novel \"The Prone Gunman\" (\"La position du tireur couché\") by Jean-Patrick Manchette, the film is about a hitman who wants to retire from his life in organized crime and flees to the country where he meets and falls in love with a beautiful woman.\n\nFlic Story: Flic Story French: \"Il était une fois un flic\" is a French crime thriller released on October 1, 1975, based on the autobiography of the same name written by French police detective Roger Borniche.  Both film and book portray Borniche's nine-year pursuit of French gangster and murderer Emile Buisson, who was executed on February 28, 1956.  Directed by Jacques Deray, the film stars Alain Delon and Jean-Louis Trintignant as Borniche and Buisson respectively, supported by Claudine Auger and André Pousse.\n\nCoralie Trinh Thi: Coralie Trinh Thi (born April 11, 1976) is a former pornographic actress and French author, also known for writing and directing with Virginie Despentes the film \"Baise-moi\" (2000).  During her career as a porn performer, she was generally just credited as Coralie.  She won a Hot d'Or Award for Best European Actress in 1996, and she received a Hot d'Or Honorary Award in 2009.\n\nThe Blue Villa: The Blue Villa (French title: Un bruit qui rend fou, \"A noise that renders one crazy\") is a 1995 French crime thriller film, directed by Alain Robbe-Grillet and starring Fred Ward.  It was entered into the 45th Berlin International Film Festival.\n\nBaise-moi: Baise-moi (\"Fuck me \") is a 2000 French crime thriller film with elements of a rape and revenge film written and directed by Virginie Despentes and Coralie Trinh Thi and starring Karen Lancaume and Raffaëla Anderson.  It is based on the novel by Despentes, first published in 1993.  The film received intense media coverage because of its graphic mix of violence and explicit sex scenes.  Consequently, it is sometimes considered an example of the \"New French Extremity.\"\n\nQuestion: The 2000 French crime thriller film starred what writer and director besides Coralie Trinh Thi?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"co_director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-director mentioned in the question.\"\n    },\n    \"other_writer_director\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other writer and director of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_genre\",\n    \"co_director_name\",\n    \"other_writer_director\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "co_director_name": {
        "type": "string",
        "description": "The name of the co-director mentioned in the question."
      },
      "other_writer_director": {
        "type": "string",
        "description": "The name of the other writer and director of the film."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_genre",
      "co_director_name",
      "other_writer_director"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
