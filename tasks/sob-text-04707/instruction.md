{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Package (Lost): \"The Package\" is the tenth television episode of the American Broadcasting Company's sixth season of the serial drama television series \"Lost\" and 113th episode overall.  The episode was aired on March 30, 2010, on ABC in the United States.  The episode was written by producer Paul Zbyszewski and story editor Graham Roland.  The episode is centered on Sun-Hwa Kwon and Jin-Soo Kwon.\n\nThe Fight (Star Trek: Voyager): \"The Fight\" is the 113th episode of the science fiction television series \"\", the 19th episode of the .\n\n113th Ohio Infantry: The 113th Ohio Volunteer Infantry (or 113th OVI) was an infantry regiment in the Union Army during the American Civil War.\n\nSpanky (film): Spanky is a 1932 \"Our Gang\" short comedy film directed by Robert F. McGowan.  It was the 113th (25th talking episode) \"Our Gang\" short that was released.  The film was based on \"Our Gang\" co-star George \"Spanky\" McFarland.\n\nThe Masterpiece Society: \"The Masterpiece Society\" is the 113th episode of the American science fiction television series \"\", the 13th episode of the .  In this episode, while the crew of the USS \"Enterprise\" saves an isolated genetically engineered society from immediate destruction, the cultural contamination resulting from their interaction may still ultimately doom the colony.\n\nRobot Wrecks: Robot Wrecks is a 1941 \"Our Gang\" short comedy film directed by Edward Cahn.  It was the 200th \"Our Gang\" short (201st episode, 112th talking short, 113th talking episode, and 32nd MGM produced episode) that was released.\n\nGeorge McFarland: George \"Spanky\" McFarland (October 2, 1928 – June 30, 1993) was an American actor most famous for his appearances as a child in the \"Our Gang\" series of short-subject comedies of the 1930s and 1940s.  The \"Our Gang\" shorts were later syndicated to television as \"The Little Rascals\".\n\nSecret Santa (The Office): \"Secret Santa\" is the 13th episode of the sixth season of the U.S. comedy series \"The Office\" and the show's 113th episode overall.  It was written by Mindy Kaling and directed by Randall Einhorn.  The night the episode premiered, it was immediately followed by an episode of \"30 Rock\" with the same title.\n\nBy Inferno's Light: \"By Inferno's Light\" is the 113th episode of the television series \"\", the 15th episode of the .\n\nHelping Hands (film): Helping Hands is a 1941 \"Our Gang\" short comedy film directed by Edward Cahn.  It was the 201st \"Our Gang\" short (202nd episode, 113th talking short, 114th talking episode, and 33rd MGM produced episode) that was released.\n\nQuestion: What American actor was the inspiration for the 113th episode of \"Our Gang\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"inspired_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the American actor who inspired the episode.\"\n        },\n        \"nickname\": {\n          \"type\": \"string\",\n          \"description\": \"The common nickname of the actor, if available.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ]\n    },\n    \"inspired_episode\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the 'Our Gang' episode.\"\n        },\n        \"episode_number\": {\n          \"type\": \"integer\",\n          \"description\": \"The overall episode number of the 'Our Gang' short.\"\n        },\n        \"series_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the series the episode belongs to.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"episode_number\",\n        \"series_name\"\n      ]\n    },\n    \"inspiration_type\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the nature of the inspiration (e.g., 'based on').\"\n    }\n  },\n  \"required\": [\n    \"inspired_actor\",\n    \"inspired_episode\",\n    \"inspiration_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "inspired_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the American actor who inspired the episode."
          },
          "nickname": {
            "type": "string",
            "description": "The common nickname of the actor, if available."
          }
        },
        "required": [
          "name"
        ]
      },
      "inspired_episode": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the 'Our Gang' episode."
          },
          "episode_number": {
            "type": "integer",
            "description": "The overall episode number of the 'Our Gang' short."
          },
          "series_name": {
            "type": "string",
            "description": "The name of the series the episode belongs to."
          }
        },
        "required": [
          "title",
          "episode_number",
          "series_name"
        ]
      },
      "inspiration_type": {
        "type": "string",
        "description": "Describes the nature of the inspiration (e.g., 'based on')."
      }
    },
    "required": [
      "inspired_actor",
      "inspired_episode",
      "inspiration_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
