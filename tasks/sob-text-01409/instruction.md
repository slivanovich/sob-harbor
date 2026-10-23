{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHonor Bound (film): Honor Bound (also known as Red End) is a 1988 film directed by Jeannot Szwarc.\n\nEnigma (1982 film): Enigma is a 1982 Anglo-American thriller film directed by Jeannot Szwarc and starring Martin Sheen, Sam Neill, Brigitte Fossey, and Kevin McNally.  Based on Michael Barak's novel \"Enigma Sacrifice\", the film centers on a CIA agent that tries to infiltrate Soviet intelligence in order to stop a murderous plot.\n\nLes Soeurs Soleil: Les Soeurs Soleil is a 1997 French comedy film directed by Jeannot Szwarc, starring and co-written by Marie-Anne Chazel.\n\nMaureen Teefy: Maureen Jane Teefy (born October 26, 1953) is an American actress.  Her films include \"Fame\" (1980), \"Grease 2\" (1982) and\" Supergirl\" (1984).\n\nSupergirl (film): Supergirl is a 1984 British superhero film directed by Jeannot Szwarc and written by David Odell, based on the DC Comics character of the same name and serves as a spin-off to Alexander and Ilya Salkind's \"Superman\" film series.  The film stars Helen Slater as Supergirl, along with Faye Dunaway, Mia Farrow and Peter O'Toole, with Marc McClure reprising his role as Jimmy Olsen from the \"Superman\" films.  He was the only actor to do so.  \"Supergirl\" was the first superhero film to feature a woman in the lead role.\n\nSomewhere in Time (film): Somewhere in Time is a 1980 American romantic science fiction drama film directed by Jeannot Szwarc.  It is a film adaptation of the 1975 novel \"Bid Time Return\" by Richard Matheson, who also wrote the screenplay.  The film stars Christopher Reeve, Jane Seymour, and Christopher Plummer.\n\nBug (1975 film): Bug is a 1975 American horror film in Panavision, directed by Jeannot Szwarc and written by William Castle and Thomas Page, from Page's 1973 novel \"The Hephaestus Plague\".  It was the last film Castle was involved in before his death.  The film starred Bradford Dillman, Joanna Miles and Richard Gilliland.\n\nThe Great Air Race (miniseries): Half a World Away (aka The Great Air Race) is a 1991 Australian television miniseries directed by Marcus Cole from an original story by Ross Dimsey, who served as the producer of the series.  The international cast included Helen Slater, Robert Reynolds, Caroline Goodall, Helen Slater, Tim Hughes and Barry Bostwick.  The film was based on the 1934 MacRobertson Air Race.  The film was also known as \"The Great Air Race\" in video and international versions.\n\nLa Vengeance d'une blonde: La Vengeance d'une blonde is a 1994 French comedy film directed by Jeannot Szwarc.\n\nHalf a World Away (TV miniseries): Half a World Away (aka The Great Air Race) is a 1991 Australian television miniseries directed by Marcus Cole from an original story by Ross Dimsey, who served as the producer of the series.  The international cast included Helen Slater, Robert Reynolds, Caroline Goodall, Helen Slater, Tim Hughes and Barry Bostwick.  The film was based on the 1934 MacRobertson Air Race.  The film was also known as \"The Great Air Race\" in video and international versions.\n\nQuestion: Maureen Jane Teefy and Helen Slater both starred in what 1984 film directed by Jeannot Szwarc? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of actors who starred in the film and were mentioned in the question.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"is_spin_off\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is a spin-off of another series.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"director_name\",\n    \"starring_actors\",\n    \"film_genre\",\n    \"is_spin_off\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The year the film was released."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of actors who starred in the film and were mentioned in the question."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "is_spin_off": {
        "type": "boolean",
        "description": "Indicates if the film is a spin-off of another series."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "director_name",
      "starring_actors",
      "film_genre",
      "is_spin_off"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
