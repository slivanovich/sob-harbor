{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSombrero (film): Sombrero is a 1953 film starring Ricardo Montalbán, Pier Angeli, Vittorio Gassman and Cyd Charisse.\n\nOn an Island with You: On an Island with You is a 1948 musical Technicolor romantic comedy film directed by Richard Thorpe.  It stars Esther Williams, Peter Lawford, Ricardo Montalbán, Cyd Charisse, Kathryn Beaumont and Jimmy Durante.\n\nMeet Me in Las Vegas: Meet Me in Las Vegas (1956) is an MGM musical comedy produced by Joe Pasternak, directed by Roy Rowland, filmed in Eastman Color (credited as Metrocolor) and CinemaScope, and starring Dan Dailey and Cyd Charisse.  The film has a running time of 112 minutes.\n\nFiesta (1947 film): Fiesta is an American Technicolor musical-drama film released by Metro-Goldwyn-Mayer in 1947, starring Esther Williams, Ricardo Montalbán, Mary Astor and Cyd Charisse.  The film was directed by Richard Thorpe and written by George Bruce and Lester Cole.\n\nTony Martin (American singer): Tony Martin (born Alvin Morris; December 25, 1913 – July 27, 2012) was an American actor, best known for his film roles and popular singer.  His career spanned over seven decades, and he scored dozens of hits between the late-1930s and mid-1950s with songs such as \"Walk Hand in Hand\" and \"Stranger in Paradise\".  He was married to actress and dancer Cyd Charisse for 60 years until her death in 2008.\n\nThe Kissing Bandit (film): The Kissing Bandit is a 1949 film starring Frank Sinatra and Kathryn Grayson.  The supporting cast includes Ricardo Montalban, Ann Miller, and Cyd Charisse.  The movie was directed by Laslo Benedek.\n\nSally, Irene and Mary (1938 film): Sally, Irene and Mary is a 1938 American comedy film directed by William A. Seiter and written by Harry Tugend and Jack Yellen.  The film stars Alice Faye, Tony Martin, Fred Allen, Joan Davis, Marjorie Weaver and Gregory Ratoff.  The film was released on March 4, 1938, by 20th Century Fox.\n\nFive Golden Hours: Five Golden Hours is a 1961 Italian-British comedy film directed by Mario Zampi and written by Hans Wilhelm, starring Ernie Kovacs, Cyd Charisse and George Sanders, and featuring Dennis Price and John Le Mesurier.\n\nSomething's Got to Give: Something's Got to Give is an unfinished 1962 American feature film, directed by George Cukor for Twentieth Century-Fox and starring Marilyn Monroe, Dean Martin and Cyd Charisse.  A remake of \"My Favorite Wife\" (1940), a screwball comedy starring Cary Grant and Irene Dunne, it was Monroe's last work, but from the beginning its production was disrupted by her personal troubles, and after her death on August 5, 1962, the film was abandoned.  Most of its completed footage remained unseen for many years.\n\nThe Band Wagon: The Band Wagon is a 1953 musical comedy film directed by Vincente Minnelli, starring Fred Astaire and Cyd Charisse.   Fred Astaire was contemplating retirement just like his character.  It tells the story of an aging musical star who hopes a Broadway show will restart his career.  However, the play's director wants to make it a pretentious retelling of \"Faust\", and brings in a prima ballerina who clashes with the star.  Along with \"Singin' in the Rain\", it is regarded as one of the finest of the Metro-Goldwyn-Mayer musicals, although it was only a modest box-office success on first release.\n\nQuestion: Who directed a 1938 American comedy film starring the husband of Cyd Charisse?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director of the film.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor who is Cyd Charisse's husband.\"\n        },\n        \"relationship_to_cyd_charisse\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the actor's relationship to Cyd Charisse.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"relationship_to_cyd_charisse\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"director_name\",\n    \"film_details\",\n    \"actor_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "director_name": {
        "type": "string",
        "description": "The name of the director of the film."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "genre"
        ],
        "additionalProperties": false
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor who is Cyd Charisse's husband."
          },
          "relationship_to_cyd_charisse": {
            "type": "string",
            "description": "Description of the actor's relationship to Cyd Charisse."
          }
        },
        "required": [
          "actor_name",
          "relationship_to_cyd_charisse"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "director_name",
      "film_details",
      "actor_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
