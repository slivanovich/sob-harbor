{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Visitors (1972 film): The Visitors is a 1972 American drama film directed by Elia Kazan.  It was entered into the 1972 Cannes Film Festival.  Kazan used Daniel Lang's \"Casualties of War\" story as a jumping-off point for this film.\n\nThe Last Detail: The Last Detail is a 1973 American comedy-drama film directed by Hal Ashby and starring Jack Nicholson, Randy Quaid, Otis Young, with a screenplay adapted by Robert Towne from a 1970 novel of the same name by Darryl Ponicsan.  The film became known for its frequent use of profanity.  It was nominated for three Academy Awards, Best Actor in a Leading Role, Jack Nicholson; Best Actor in a Supporting Role, Randy Quaid; and Best Writing, Screenplay Based on Material from Another Medium, Robert Towne.\n\nFive Easy Pieces: Five Easy Pieces is a 1970 American drama film written by Carole Eastman (as Adrien Joyce) and Bob Rafelson, and directed by Rafelson.  The film stars Jack Nicholson, with Karen Black, Susan Anspach, Ralph Waite, and Sally Struthers in supporting roles.\n\nThe Last Tycoon (1976 film): The Last Tycoon is a 1976 American drama film directed by Elia Kazan and produced by Sam Spiegel, based upon Harold Pinter's screenplay adaptation of F. Scott Fitzgerald's \"The Last Tycoon\".  It stars Robert De Niro, Tony Curtis, Robert Mitchum, Jack Nicholson, Donald Pleasence, Jeanne Moreau, Theresa Russell and Ingrid Boulting.\n\nThe Crossing Guard: The Crossing Guard is a 1995 American independent thriller drama film co-produced, written and directed by American actor Sean Penn.  The film tells the story of Freddy Gale, a man who has been tormented for over five years following his daughter's death in a car accident.  Since, he became an alcoholic despite being a husband, and when he finds out that the man who was responsible for the death of his daughter is released from prison, he decides to set out for personal vendetta against him.  The film stars Jack Nicholson, David Morse, Robin Wright and Anjelica Huston.\n\nTheresa Russell: Theresa Lynn Russell (born March 20, 1957) is an American actress.  Russell made her film debut in \"The Last Tycoon\" (1976) directed by Elia Kazan, followed by a lead role opposite Dustin Hoffman in \"Straight Time\" (1978).  She was then cast in Nicolas Roeg's controversial thriller \"Bad Timing\" (1980), which earned her critical praise.  After marrying Roeg in 1982, she appeared in multiple films directed by him, mainly arthouse and experimental films, including \"Eureka\" (1983), \"Insignificance\" (1985), and \"Cold Heaven\" (1991).\n\nIronweed (film): Ironweed is a 1987 American drama film directed by Héctor Babenco.  It is based on the Pulitzer Prize-winning novel of the same name by William Kennedy, who also wrote the screenplay.  It stars Jack Nicholson and Meryl Streep, with Carroll Baker, Michael O'Keefe, Diane Venora, Fred Gwynne, Nathan Lane and Tom Waits in supporting roles.  The story concerns the relationship of a homeless couple: Francis, an alcoholic, and Helen, a terminally ill woman during the Great Depression.  Major portions of the film were shot on location in Albany, New York, including Jay Street at Lark Street, Albany Rural Cemetery and the Miss Albany Diner on North Broadway.\n\nIngrid Boulting: Ingrid Boulting was born in Transvaal in 1947 – step-daughter of English film-maker Roy Boulting and niece of John Boulting and Sydney Boulting a.k.a. Peter Cotes.  She was a ballerina and model, before embarking on an acting career.  In 1976, Ingrid starred in \"The Last Tycoon\", the last film directed by famed director Elia Kazan, written by Harold Pinter based on F. Scott Fitzgerald's Hollywood novel \"The Last Tycoon\", and produced by Sam Spiegel.\n\nThe King of Marvin Gardens: The King of Marvin Gardens is a 1972 American drama film.  It stars Jack Nicholson, Bruce Dern, Ellen Burstyn and Scatman Crothers.  It is one of several collaborations between Nicholson and director Bob Rafelson.  The majority of the film is set in a wintry Atlantic City, New Jersey, with cinematography by László Kovács.\n\nJack Nicholson: John Joseph Nicholson (born April 22, 1937) is an American actor and filmmaker, who has performed for over 60 years.  Nicholson is known for playing a wide range of starring or supporting roles, including satirical comedy, romance and dark portrayals of antiheroes and psychopathic characters.  In many of his films, he has played the \"eternal outsider, the sardonic drifter,\" someone who rebels against the social structure.\n\nQuestion: The Last Tycoon is a 1976 American drama film directed by Elia Kazan, it stars Jack Nicholson, born John Joseph Nicholson, an American actor and filmmaker, who has performed for over 60 years, born on which date?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film mentioned in the question.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actor.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the actor in 'Month Day, Year' format.\"\n        },\n        \"professions\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of professions of the actor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\",\n        \"professions\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"film_director\",\n    \"actor_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film mentioned in the question."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_director": {
        "type": "string",
        "description": "The director of the film."
      },
      "actor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the actor."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the actor in 'Month Day, Year' format."
          },
          "professions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of professions of the actor."
          }
        },
        "required": [
          "name",
          "birth_date",
          "professions"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_year",
      "film_director",
      "actor_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
