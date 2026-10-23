{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChild actor: The term child actor or child actress is generally applied to a child acting on stage or in motion pictures or television, but also to an adult who began his or her acting career as a child; to avoid confusion, the latter is also called a \"former child actor\".  Closely associated is teenage actor or teen actor, an actor who reached popularity as a teenager.\n\nNiño Muhlach: Niño Muhlach (born Angelo Jose Rocha Muhlach, October 27, 1971) is a Filipino actor and former child actor.  He is the father of Filipino child actor Alonzo Muhlach.\n\nSunny Besen Thrasher: Sunny Besen Thrasher (born December 13, 1976 in Toronto, Ontario) is a Canadian former child actor who starred as Paul Edison in Nelvana's live-action series, \"The Edison Twins\", and supplied voices in the first Care Bears movies.  He's the son of Prairie Oyster keyboardist and Canadian songwriter Joan Besen.\n\nJoey Cramer: Deleriyes August Joe Fisher \"Joey\" Cramer (born August 23, 1973) is a Canadian former child actor who had a briefly successful career in Canadian television and Hollywood in the mid-1980s, most notably for his role in the cinema film \"Flight of the Navigator\".\n\nK. C. Martel: Kevin Christopher Martel (born September 14, 1967) is a Canadian former child actor.  He played Mike Seaver's friend Eddie on \"Growing Pains\" from 1985-1992.\n\nMichael Shea (actor): Michael Shea (born November 4, 1952) is an American former child actor.  Beginning a prolific career as a child actor at the age of ten, Shea is perhaps best known for portraying the title role in the NBC children's television series, \"The New Adventures of Huckleberry Finn\", as well as for his feature film roles; as Nick in the Ivan Tors family film, \"Namu, the Killer Whale\", as Jimmy in the MGM western, \"Welcome to Hard Times\", and as \"Cav\" in the Walt Disney drama, \"\".  Although born and raised in New York City, Shea was primarily cast as the wholesome small-town \"country boy\" throughout most of his career as a child star.\n\nTommy Rettig: Thomas Noel Rettig, known as Tommy Rettig (December 10, 1941 – February 15, 1996), was an American child actor, computer software engineer, and author.  Rettig is remembered for portraying the character \"Jeff Miller\" in the first three seasons of CBS's \"Lassie\" television series, from 1954 to 1957, later seen in syndicated re-runs as \"Jeff's Collie\".  He also co-starred with another former child actor, Tony Dow, in the mid-1960s television teen soap opera \"Never Too Young\" and recorded the song by that title with the group The TR-4.\n\nFlight of the Navigator: Flight of the Navigator is a 1986 American science fiction adventure film directed by Randal Kleiser and written by Mark H. Baker, Michael Burton and Matt MacManus.  The film stars Joey Cramer as David Freeman, a 12-year-old boy who is abducted by an alien spaceship and finds himself caught in a world that has changed around him.\n\nXavier Petermann: Xavier Norman Petermann is a Canadian former child actor from Quebec, who garnered a Genie Award nomination for Best Actor at the 6th Genie Awards for his performance as an autistic child in the film \"Mario\".  The film was his first-ever acting role.\n\nSteven Mond: Steven Mond (born May 12, 1971) is a Canadian former child actor best known for playing Robbie Jason on the sitcom \"Diff'rent Strokes.\n\nQuestion:  is a Canadian former child actor\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"query_topic\": {\n      \"type\": \"string\",\n      \"description\": \"The topic of the query.\"\n    },\n    \"number_of_actors_found\": {\n      \"type\": \"integer\",\n      \"description\": \"The total count of Canadian former child actors found in the context.\"\n    },\n    \"canadian_former_child_actors\": {\n      \"type\": \"array\",\n      \"description\": \"A list of Canadian former child actors.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"actor_name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the actor.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the actor.\"\n          },\n          \"is_former_child_actor\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the person is a former child actor.\"\n          },\n          \"birth_date\": {\n            \"type\": \"string\",\n            \"description\": \"The birth date of the actor.\"\n          },\n          \"birth_place\": {\n            \"type\": \"string\",\n            \"description\": \"The birth place of the actor.\"\n          },\n          \"notable_roles\": {\n            \"type\": \"array\",\n            \"description\": \"A list of notable roles or projects the actor was known for.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          },\n          \"awards_nominations\": {\n            \"type\": \"array\",\n            \"description\": \"A list of awards or nominations received by the actor.\",\n            \"items\": {\n              \"type\": \"object\",\n              \"properties\": {\n                \"award_name\": {\n                  \"type\": \"string\",\n                  \"description\": \"The name of the award or nomination.\"\n                },\n                \"category\": {\n                  \"type\": \"string\",\n                  \"description\": \"The category for which the award/nomination was received.\"\n                }\n              },\n              \"required\": [\n                \"award_name\",\n                \"category\"\n              ],\n              \"additionalProperties\": false\n            }\n          }\n        },\n        \"required\": [\n          \"actor_name\",\n          \"nationality\",\n          \"is_former_child_actor\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"query_topic\",\n    \"number_of_actors_found\",\n    \"canadian_former_child_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "query_topic": {
        "type": "string",
        "description": "The topic of the query."
      },
      "number_of_actors_found": {
        "type": "integer",
        "description": "The total count of Canadian former child actors found in the context."
      },
      "canadian_former_child_actors": {
        "type": "array",
        "description": "A list of Canadian former child actors.",
        "items": {
          "type": "object",
          "properties": {
            "actor_name": {
              "type": "string",
              "description": "The full name of the actor."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the actor."
            },
            "is_former_child_actor": {
              "type": "boolean",
              "description": "Indicates if the person is a former child actor."
            },
            "birth_date": {
              "type": "string",
              "description": "The birth date of the actor."
            },
            "birth_place": {
              "type": "string",
              "description": "The birth place of the actor."
            },
            "notable_roles": {
              "type": "array",
              "description": "A list of notable roles or projects the actor was known for.",
              "items": {
                "type": "string"
              }
            },
            "awards_nominations": {
              "type": "array",
              "description": "A list of awards or nominations received by the actor.",
              "items": {
                "type": "object",
                "properties": {
                  "award_name": {
                    "type": "string",
                    "description": "The name of the award or nomination."
                  },
                  "category": {
                    "type": "string",
                    "description": "The category for which the award/nomination was received."
                  }
                },
                "required": [
                  "award_name",
                  "category"
                ],
                "additionalProperties": false
              }
            }
          },
          "required": [
            "actor_name",
            "nationality",
            "is_former_child_actor"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "query_topic",
      "number_of_actors_found",
      "canadian_former_child_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
