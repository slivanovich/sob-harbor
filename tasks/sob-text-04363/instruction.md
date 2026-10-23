{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGene Brewer: Gene Brewer (born Eugene N. Brewer, 4 July 1937) is an American writer, the author of the K-PAX series of novels, about a man who claims to be a visiting extraterrestrial from a planet called K-PAX: \"K-PAX\" (1995), \"On a Beam of Light\" (2001), \"K-PAX III: The Worlds of Prot\" (2002), \"\" (2007) and \"Prot's Report\", a brief natural history of the Earth, which appears in \"K-PAX: The Trilogy\", an omnibus edition of the first three K-PAX books.  The first book in the series was made into a Universal Pictures film in 2001; it stars Kevin Spacey and Jeff Bridges.\n\nL'Inhumaine: L'Inhumaine (\"the inhuman woman\") is a 1924 French drama-science fiction film directed by Marcel L'Herbier; it has the subtitle histoire féerique (\"fairy story\", \"story of enchantment\").  It was notable for its experimental techniques and for the collaboration of many leading practitioners in the decorative arts, architecture and music.  The film gave rise to much controversy on its release.\n\nMan Facing Southeast: Man Facing Southeast (Spanish: Hombre mirando al sudeste ) is a 1986 Argentine drama-science fiction film written and directed by Eliseo Subiela and starring Lorenzo Quinteros and Hugo Soto.\n\nStar Trek: Star Trek is an American science fiction media franchise based on the television series created by Gene Roddenberry.  The first television series, simply called \"Star Trek\" and now referred to as \"\", debuted in 1966 and aired for three seasons on the television network NBC.  It followed the interstellar adventures of Captain James T Kirk (William Shatner) and his crew aboard the starship USS \"Enterprise\", a space exploration vessel, built by the interstellar federal republic United Federation of Planets in the twenty-third century.  The \"Star Trek\" canon of the franchise includes \"The Original Series\", an animated series, five spin-off television series, and its film franchise in addition to further adaptations made in several media since the original.\n\nK-PAX (film): K-PAX is a 2001 American science fiction-mystery film based on Gene Brewer's 1995 novel of the same name, directed by Iain Softley, starring Kevin Spacey, Jeff Bridges, Mary McCormack and Alfre Woodard.  Brewer's novel and the subsequent film are uncredited adaptations of the 1986 Argentinian film \"Man Facing Southeast\" by director, Eliseo Subiela.  The film is about a psychiatric patient who claims to be an alien from the planet K-PAX.  During his treatment, the patient demonstrates an outlook on life that ultimately proves inspirational for his fellow patients and especially for his psychiatrist.\n\nScarecrow &amp; Other Anomalies: Scarecrow & Other Anomalies, by Oliverio Girondo, is a collection of short prose poems written originally in Spanish.  \"Scarecrow\" inspired the feature film \"The Dark Side of the Heart\" (1994), directed by Eliseo Subiela.\n\nThe Effect of Love: The Effect of Love (Spanish: El resultado del amor) is a 2007 Argentinian drama film, written and directed by Eliseo Subiela, an Argentinian film director.  The film was shot in Buenos Aires and San Luis in Argentina.\n\nK-PAX: K-PAX is an American science fiction novel by Gene Brewer, the first in the K-PAX series.\n\nThe Dark Side of the Heart: The Dark Side of the Heart (Spanish: El lado oscuro del corazón ) is a 1992 Argentine drama film directed by Eliseo Subiela.  The film was selected as the Argentine entry for the Best Foreign Language Film at the 65th Academy Awards, but was not accepted as a nominee.\n\nThe Adventures of God: The Adventures of God (Spanish: \"Las Aventuras de Dios\" ) is a 2000 Argentine fantasy drama film directed and written by Eliseo Subiela.\n\nQuestion: What is a 1986 Argentine drama-science fiction film written and directed by Eliseo Subiela, that has uncredited adaptations made from it to  a 2001 American science fiction-mystery film based on Gene Brewer's 1995 novel ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the film was released.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the film was produced.\"\n    },\n    \"genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres the film belongs to.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"writer\": {\n      \"type\": \"string\",\n      \"description\": \"The writer of the film.\"\n    },\n    \"uncredited_adaptations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"adaptation_title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the uncredited adaptation.\"\n          },\n          \"adaptation_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of the adaptation (e.g., 'film', 'novel').\"\n          },\n          \"adaptation_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The release year of the adaptation.\"\n          },\n          \"source_material_author\": {\n            \"type\": \"string\",\n            \"description\": \"The author of the source material for the adaptation.\"\n          },\n          \"source_material_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The release year of the source material for the adaptation.\"\n          }\n        },\n        \"required\": [\n          \"adaptation_title\",\n          \"adaptation_type\",\n          \"adaptation_year\",\n          \"source_material_author\",\n          \"source_material_year\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of works that are uncredited adaptations of this film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"release_year\",\n    \"country_of_origin\",\n    \"genres\",\n    \"director\",\n    \"writer\",\n    \"uncredited_adaptations\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "country_of_origin": {
        "type": "string",
        "description": "The country where the film was produced."
      },
      "genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres the film belongs to."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "writer": {
        "type": "string",
        "description": "The writer of the film."
      },
      "uncredited_adaptations": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "adaptation_title": {
              "type": "string",
              "description": "The title of the uncredited adaptation."
            },
            "adaptation_type": {
              "type": "string",
              "description": "The type of the adaptation (e.g., 'film', 'novel')."
            },
            "adaptation_year": {
              "type": "integer",
              "description": "The release year of the adaptation."
            },
            "source_material_author": {
              "type": "string",
              "description": "The author of the source material for the adaptation."
            },
            "source_material_year": {
              "type": "integer",
              "description": "The release year of the source material for the adaptation."
            }
          },
          "required": [
            "adaptation_title",
            "adaptation_type",
            "adaptation_year",
            "source_material_author",
            "source_material_year"
          ],
          "additionalProperties": false
        },
        "description": "A list of works that are uncredited adaptations of this film."
      }
    },
    "required": [
      "film_title",
      "release_year",
      "country_of_origin",
      "genres",
      "director",
      "writer",
      "uncredited_adaptations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
