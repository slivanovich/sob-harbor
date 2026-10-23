{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2008 French Open – Boys' Singles: The 2008 French Open – Boys' Singles tournament was an event during the 2008 French Open tennis tournament.  Vladimir Ignatic was the defending champion, but did not compete in the Juniors in this year.\n\nAsterix at the Olympic Games (film): Asterix at the Olympic Games (French: \"Astérix aux Jeux Olympiques\" ) is a 2008 French fantasy comedy film directed by Frédéric Forestier and Thomas Langmann, and written by Langmann, Alexandre Charlot, and Frank Magnier, based on characters from René Goscinny and Albert Uderzo's Astérix comic series.  It was filmed primarily in Spain over the course of the year 2006.\n\nThe Beautiful Person: The Beautiful Person (French: La Belle Personne ) is a 2008 French film directed by Christophe Honoré.  It is a modernized adaptation of the seventeeth-century French novel \"La Princesse de Clèves\".\n\nAsterix and Obelix: God Save Britannia: Asterix and Obelix: God Save Britannia (French: Astérix & Obélix: Au service de Sa Majesté ; translated as \"Asterix & Obelix: In The Service of Her Majesty\"), directed by Laurent Tirard, is the fourth film adaptation of the adventures of Astérix after \"Asterix & Obelix vs Caesar\" (1999), \"\" (2002), and \"Asterix at the Olympic Games\" (2008).  The film is adapted into 3D and had its World Premiere in September 2012.  It is a live-action film from Fidélité Films and is based on \"Asterix in Britain\" (1965) and \"Asterix and the Normans\" (1966).\n\nMesrine (2008 film): Mesrine is a two-part (Mesrine: Killer Instinct and Mesrine: Public Enemy Number One) 2008 French film directed by Jean-François Richet and written by Abdel Raouf Dafri and Richet.  The first part's script was based on the autobiographical book \"L'instinct de mort\" by French gangster Jacques Mesrine, while the second part detailed Mesrine's criminal career.  The film has been referred to as the French version of the American film \"Scarface\" which starred Al Pacino.\n\nBeauties at War: Beauties at War is a 2008 French film.  Originally titled La guerre des Miss in French, the film aired in France on 9 January 2009, directed by Patrice Leconte.  It was also shown at the Seattle International Film Festival 2009.\n\nUn Lac: Un Lac is a 2008 French film directed by Philippe Grandrieux, starring Dmitriy Kubasov, Natálie Rehorová and Alexei Solonchev.  The film won a Special Mention in the Orizzonti Section at the 2008 Venice Film Festival.\n\nA Man and His Dog: A Man and His Dog (\"Un Homme et Son Chien\") is a 2008 French film directed by French director Francis Huster, starring Jean-Paul Belmondo, based on the 1952 film Umberto D. directed by Vittorio De Sica, and written by Cesare Zavattini.\n\nThe First Day of the Rest of Your Life: The First Day of the Rest of Your Life (French: \"Le Premier Jour du reste de ta vie\" ) is a 2008 French film written and directed by Rémi Bezançon.  The film received 9 César Award nominations, winning three (Best Editing, Most Promising Actor and Most Promising Actress).\n\nParis (2008 film): Paris is a 2008 French film by Cédric Klapisch concerning a diverse group of people living in Paris.  The film began shooting in November 2006 and was released in February 2008.  Its UK release was in July 2008.  Commentators have noted the similarity in style of this film to Woody Allen's \"Manhattan\" and Robert Altman's \"Short Cuts\".\n\nQuestion: Which 2008 French film was the third of a four-film adaptation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"is_adaptation\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is an adaptation of another work.\"\n    },\n    \"adaptation_source\": {\n      \"type\": \"string\",\n      \"description\": \"The source material the film is adapted from.\"\n    },\n    \"series_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"film_number_in_series\": {\n          \"type\": \"integer\",\n          \"description\": \"The position of this film within its adaptation series.\"\n        },\n        \"total_films_in_series\": {\n          \"type\": \"integer\",\n          \"description\": \"The total number of films in the adaptation series mentioned in the context.\"\n        },\n        \"other_films_in_series\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"title\": {\n                \"type\": \"string\",\n                \"description\": \"The title of another film in the series.\"\n              },\n              \"year\": {\n                \"type\": \"integer\",\n                \"description\": \"The release year of another film in the series.\"\n              }\n            },\n            \"required\": [\n              \"title\",\n              \"year\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of other films mentioned as part of the same adaptation series.\"\n        }\n      },\n      \"required\": [\n        \"film_number_in_series\",\n        \"total_films_in_series\",\n        \"other_films_in_series\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"is_adaptation\",\n    \"adaptation_source\",\n    \"series_information\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "is_adaptation": {
        "type": "boolean",
        "description": "Indicates if the film is an adaptation of another work."
      },
      "adaptation_source": {
        "type": "string",
        "description": "The source material the film is adapted from."
      },
      "series_information": {
        "type": "object",
        "properties": {
          "film_number_in_series": {
            "type": "integer",
            "description": "The position of this film within its adaptation series."
          },
          "total_films_in_series": {
            "type": "integer",
            "description": "The total number of films in the adaptation series mentioned in the context."
          },
          "other_films_in_series": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "title": {
                  "type": "string",
                  "description": "The title of another film in the series."
                },
                "year": {
                  "type": "integer",
                  "description": "The release year of another film in the series."
                }
              },
              "required": [
                "title",
                "year"
              ],
              "additionalProperties": false
            },
            "description": "A list of other films mentioned as part of the same adaptation series."
          }
        },
        "required": [
          "film_number_in_series",
          "total_films_in_series",
          "other_films_in_series"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "release_year",
      "is_adaptation",
      "adaptation_source",
      "series_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
