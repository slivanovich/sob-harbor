{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nManiac Cop 2: Maniac Cop 2 is a 1990 American action horror film directed by William Lustig and written by Larry Cohen.  It is the second installment in the \"Maniac Cop\" series.  it stars Robert Davi, Claudia Christian, Michael Lerner, and Bruce Campbell.  Robert Z'Dar returns as Matthew Cordell, an undead cop-turned-serial killer following his own murder.\n\nTracy Morgan: Tracy Jamal Morgan (born November 10, 1968) is an American actor and comedian best known for his seven seasons as a cast member on \"Saturday Night Live\" (1996–2003), \"30 Rock\" (2006–2013) and his 2010 buddy cop film \"Cop Out\" and hosting \"Scare Tactics\".  He was nominated for an Emmy Award in 2009 for his work on \"30 Rock\".  He has appeared in numerous films as an actor and voice actor.\n\nBruce Campbell: Bruce Lorne Campbell (born June 22, 1958) is an American actor, producer, writer, comedian and director.  One of his best-known roles is portraying Ash Williams in Sam Raimi's \"Evil Dead\" franchise, from the 1978 short film \"Within the Woods\" to the ongoing TV series \"Ash vs Evil Dead\".  He has starred in many low-budget cult films such as \"Crimewave\" (1985), \"Maniac Cop\" (1988), \"\" (1989), and \"Bubba Ho-Tep\" (2002).\n\nRobert R. Shafer: Robert Ray \"Bobby\" Shafer (born April 10, 1958) is an American actor who has amassed a substantial cult-following for having played Officer Ted Warnicky (more commonly known as Joe Vickers) in the 1989 horror-comedy \"Psycho Cop\" and the sequel \"Psycho Cop 2\".  Shafer, sometimes credited as Bobby Ray Shafer, is best known for playing Bob Vance on \"The Office\".  Born in Charleston, West Virginia, Shafer has appeared in film, television, commercials, voice-over and theater.  According to Amazon.com, Shafer has appeared in at least 18 movies.\n\nLeo Rossi: Leo Rossi (born June 26, 1946) is an American actor, writer and producer.  A highly prolific character actor with over 100 credits to his name, he is known for his role as foul-mouthed EMT Vincent \"Budd\" Scarlotti in the 1981 horror film \"Halloween II\", as the serial killer Turkell from the 1990 horror sequel \"Maniac Cop 2\", and as Detective Sam Dietz in the \"Relentless\" franchise.  His other films include \"Heart Like a Wheel\" (1983), \"River's Edge\" (1986), \"The Accused\" (1988), \"Analyze This\" (1999), \"One Night at McCool's\" (2001), and \"10th & Wolf\" (2006).\n\nRobert Z'Dar: Robert J. Zdarsky (June 3, 1950 – March 30, 2015), better known by his stage name Robert Z'Dar, was an American actor and film producer, best known for his role as officer Matt Cordell in the cult horror film \"Maniac Cop\" and its two sequels.\n\nLaurene Landon: Laurene Landon (born March 17, 1957 as Laurene Landon Coughlin) is an American film and television actress.  Laurene first began appearing in movies in the 1980s.  She is best known for her roles in \"Maniac Cop\" and \"Maniac Cop 2\", \"Hundra\", \"\", and \"...All the Marbles\" with Peter Falk.  She is half Irish and half Polish and describes herself as being \"bi-Polish\".\n\nManiac Cop: Maniac Cop is a 1988 American action horror film directed by William Lustig and written by Larry Cohen.  It stars Tom Atkins, Bruce Campbell, Laurene Landon, Richard Roundtree, William Smith, Robert Z'Dar, and Sheree North.  Z'Dar plays the title character, a murderous ex-cop returned from the dead, who is pursued by his former co-workers.  It was released on May 13, 1988, and grossed $671,382 from a budget of $1.1 million.  Despite negative reviews on release, \"Maniac Cop\" has become a cult film.  It was followed by two sequels, \"Maniac Cop 2\" (1990) and \"\" (1993).\n\nPsycho Cop: Psycho Cop is a 1989 American slasher film written and directed by Wallace Potts, noted for its similarities to the previous year's \"Maniac Cop\" by William Lustig and Larry Cohen.  It was followed by a 1993 sequel entitled \"Psycho Cop 2\".\n\nTimothy Carhart: Timothy Carhart (born December 24, 1953) is an American actor.  He starred in the CBS drama \"Island Son\" (1989–90) and has had recurring roles in \"\" (2000–03) and \"24\" (2002).  He also starred in the 1992 Broadway revival of \"A Streetcar Named Desire\".  His film appearances include \"Pink Cadillac\" (1989), \"Thelma & Louise\" (1991), and \"Beverly Hills Cop III\" (1994).\n\nQuestion: Who was the American actor who starred in \"Maniac Cop\" and \"Bubba Ho Tep\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actor.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actor.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the actor in YYYY-MM-DD format.\"\n        },\n        \"occupations\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of the actor's known occupations.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"birth_date\",\n        \"occupations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"films_matching_criteria\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film.\"\n          },\n          \"year\": {\n            \"type\": \"integer\",\n            \"description\": \"The release year of the film.\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"year\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of films the actor starred in that match the question's criteria.\"\n    },\n    \"final_answer_actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who is the final answer to the question.\"\n    }\n  },\n  \"required\": [\n    \"actor_details\",\n    \"films_matching_criteria\",\n    \"final_answer_actor_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the actor."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actor."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the actor in YYYY-MM-DD format."
          },
          "occupations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of the actor's known occupations."
          }
        },
        "required": [
          "name",
          "nationality",
          "birth_date",
          "occupations"
        ],
        "additionalProperties": false
      },
      "films_matching_criteria": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the film."
            },
            "year": {
              "type": "integer",
              "description": "The release year of the film."
            }
          },
          "required": [
            "title",
            "year"
          ],
          "additionalProperties": false
        },
        "description": "A list of films the actor starred in that match the question's criteria."
      },
      "final_answer_actor_name": {
        "type": "string",
        "description": "The name of the actor who is the final answer to the question."
      }
    },
    "required": [
      "actor_details",
      "films_matching_criteria",
      "final_answer_actor_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
