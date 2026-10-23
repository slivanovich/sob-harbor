{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n42nd Primetime Emmy Awards: The 42nd Primetime Emmy Awards were held on Sunday, September 16, 1990.  The ceremony was broadcast on Fox from the Pasadena Civic Auditorium in Pasadena, California.  Two networks, The Family Channel and The Disney Channel received their first major nominations.\n\nMarty McFly: Martin \"Marty\" Seamus McFly is a fictional character and the main protagonist of the \"Back to the Future\" trilogy.  He is portrayed by actor Michael J. Fox.  Marty also appears in the , where he was voiced by David Kaufman.  In by Telltale Games, he is voiced by A.J. Locascio; in addition, Fox voiced Marty's future counterparts at the end of the game.  In 2008, Marty McFly was selected by \"Empire\" magazine as the 12th Greatest Movie Character of All Time.\n\n54th Primetime Emmy Awards: The 54th Primetime Emmy Awards were held on Sunday, September 22, 2002.  Nominations were announced July 22, 2002.  The ceremony was hosted by Conan O'Brien and was broadcast on NBC.  Two networks, FX and VH1, received their first major nominations this year.  The program \"\" was simulcast on every major network, and therefore, is not designated with one below.\n\n41st Primetime Emmy Awards: The 41st Primetime Emmy Awards were held on Sunday, September 17, 1989.  The ceremony was broadcast on Fox from the Pasadena Civic Auditorium in Pasadena, California.  The ceremony saw the guest acting categories double, as they were now based on gender as well as genre.  Two networks, Lifetime, and USA, received their first major nominations this year.\n\nBack to the Future: The Game: Back to the Future: The Game is an episodic graphic adventure based on the \"Back to the Future\" film franchise.  The game was developed and published by Telltale Games as part of a licensing deal with Universal Pictures.  Bob Gale, co-creator, co-writer and co-producer of the film trilogy, assisted Telltale in writing the game's story.  Original actors Michael J. Fox and Christopher Lloyd allowed the developers to use their likenesses in the game for the lead characters Marty McFly and Doc Brown, respectively.  Lloyd also provides the voice for Doc, while A.J. Locascio plays the role of Marty; Fox later appeared to voice two cameo roles in the final episode, reprising his role as future versions of Marty McFly in addition to playing his forefather William.\n\n52nd Primetime Emmy Awards: The 52nd Primetime Emmy Awards were held on Sunday, September 10, 2000.  The ceremony was hosted by Garry Shandling and was broadcast on ABC.  Two networks, Bravo and The WB, received their first major nominations.  This remains the only year in which a show from The WB or its descendants received a major nomination.\n\nBack to the Future Part II: Back to the Future Part II is a 1989 American science-fiction adventure comedy film directed by Robert Zemeckis and written by Bob Gale.  It is the sequel to the 1985 film \"Back to the Future\" and the second installment in the \"Back to the Future\" trilogy.  The film stars Michael J. Fox, Christopher Lloyd, Thomas F. Wilson, and Lea Thompson and continues immediately following the original film.  After repairing the damage to history done by his previous time travel adventures, Marty McFly (Fox) and his friend Dr. Emmett \"Doc\" Brown (Lloyd) travel to 2015 to prevent McFly's future son from ending up imprisoned.  However, their presence allows Biff Tannen (Wilson) to steal Doc's DeLorean time machine and travel to 1955, where he alters history by making his younger self wealthy.\n\nBack to the Future Part III: Back to the Future Part III is a 1990 American Science fiction Western comedy film and the third and final installment of the \"Back to the Future\" trilogy.  The film was directed by Robert Zemeckis, and stars Michael J. Fox, Christopher Lloyd, Mary Steenburgen, Thomas F. Wilson and Lea Thompson.  The film continues immediately following \"Back to the Future Part II\" (1989); while stranded in 1955 during his time travel adventures, Marty McFly (Fox) discovers that his friend Dr. Emmett \"Doc\" Brown, trapped in 1885, was killed by Biff Tannen's great-grandfather Buford.  Marty decides to travel to 1885 to rescue Doc.\n\nMichael J. Fox: Michael Andrew Fox, OC (born June 9, 1961), known professionally as Michael J. Fox, is a Canadian-American actor, author, producer, and activist.  With a film and television career spanning from the 1970s, Fox starred in the \"Back to the Future\" trilogy, where he portrayed Marty McFly.  Other notable roles have included Mike Flaherty on the ABC sitcom \"Spin City\" (1996–2000), for which he won five Emmys, four Golden Globes, and two Screen Actors Guild Awards and his portrayal of Alex P. Keaton on the American sitcom \"Family Ties\".\n\n48th Primetime Emmy Awards: The 48th Primetime Emmy Awards were held at the Pasadena Civic Auditorium in Pasadena, California.  The awards were presented over two ceremonies, one untelevised on September 7, 1996, and other televised on September 8, 1996.  It was hosted by Michael J. Fox, Paul Reiser, and Oprah Winfrey.  Two networks, A&E and AMC, received their first major nominations this year.\n\nQuestion: What actor who starred in the \"Back to the Future\" trilogy, where he portrayed Marty McFly., hosted an awards show where two networks, A&E and AMC, received their first major nominations that year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the actor.\"\n    },\n    \"role_in_trilogy\": {\n      \"type\": \"string\",\n      \"description\": \"The character portrayed by the actor in the film trilogy.\"\n    },\n    \"trilogy_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film trilogy.\"\n    },\n    \"awards_show_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"awards_show_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the awards show hosted by the actor.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the awards show was held.\"\n        },\n        \"hosted_by_actor\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the actor was a host of this specific awards show.\"\n        },\n        \"first_time_nominated_networks\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of networks that received their first major nominations at this awards show.\"\n        }\n      },\n      \"required\": [\n        \"awards_show_name\",\n        \"year\",\n        \"hosted_by_actor\",\n        \"first_time_nominated_networks\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_in_trilogy\",\n    \"trilogy_name\",\n    \"awards_show_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The full name of the actor."
      },
      "role_in_trilogy": {
        "type": "string",
        "description": "The character portrayed by the actor in the film trilogy."
      },
      "trilogy_name": {
        "type": "string",
        "description": "The name of the film trilogy."
      },
      "awards_show_details": {
        "type": "object",
        "properties": {
          "awards_show_name": {
            "type": "string",
            "description": "The name of the awards show hosted by the actor."
          },
          "year": {
            "type": "integer",
            "description": "The year the awards show was held."
          },
          "hosted_by_actor": {
            "type": "boolean",
            "description": "Indicates if the actor was a host of this specific awards show."
          },
          "first_time_nominated_networks": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of networks that received their first major nominations at this awards show."
          }
        },
        "required": [
          "awards_show_name",
          "year",
          "hosted_by_actor",
          "first_time_nominated_networks"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "role_in_trilogy",
      "trilogy_name",
      "awards_show_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
