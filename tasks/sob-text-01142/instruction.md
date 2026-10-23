{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTogether (1956 film): Together is a 1956 film about two deaf people in the East End of London, directed by , in collaboration with Denis Horne, based on his short story, \"The Glass Marble.\"  The two main characters are played by artists Eduardo Paolozzi and Michael Andrews, who were friends of the filmmaker.  The film, produced by the British Film Institute Experimental Film Fund, was first shown as part of the first Free Cinema programme at the National Film Theatre in London in February 1956, along with Tony Richardson and Karel Reisz's \"Momma Don't Allow\", and Lindsay Anderson's \"O Dreamland\".\n\nMomma Don't Allow: Momma Don't Allow is a short British documentary film about a north London jazz club made in 1955.  It was co-directed by Karel Reisz and Tony Richardson and filmed by Walter Lassally.  It was produced by the British Film Institute Experimental Film Fund.  It was first shown as part of the first Free cinema programme at the National Film Theatre in February 1956.\n\nFree Cinema: Free Cinema was a documentary film movement that emerged in the United Kingdom in the mid-1950s.  The term referred to an absence of propagandised intent or deliberate box office appeal.  Co-founded by Lindsay Anderson, though he later disdained the 'movement' tag, with Karel Reisz, Tony Richardson and Lorenza Mazzetti.  The movement began with a programme of three short films at the National Film Theatre, London, on 5 February 1956.  The programme was such a success that five more programmes appeared under the Free Cinema banner before the founders decided to end the series.  The last event was held in March 1959.  Three of the screenings consisted of work from overseas film makers.\n\nWe Are the Lambeth Boys: We Are the Lambeth Boys (1959) is a British documentary film directed by Karel Reisz.  Filmed in the summer of 1958, it was sponsored by the Ford motor company as part of a 'Look at Britain' series.  \"Lambeth Boys\" was one of the last films to be made by the Free Cinema movement, and offered a sympathetic portrait of the lives of young working class people in South London.\n\nWho'll Stop the Rain: Who'll Stop the Rain is a 1978 psychological drama film released by United Artists starring Nick Nolte.  It was directed by Karel Reisz and produced by Herb Jaffe and Gabriel Katzka with Sheldon Schrager and Roger Spottiswoode as executive producers.  The screenplay was by Judith Rascoe and Robert Stone from Stone's novel \"Dog Soldiers\".  The music score was by Laurence Rosenthal and the cinematography by Richard H. Kline.\n\nEverybody Wins (film): Everybody Wins is a 1990 American mystery-thriller film directed by Karel Reisz, starring Debra Winger and Nick Nolte.  The screenplay was written by Arthur Miller, based on his one-act play \"Some Kind of Love Story\" (1984).  It is loosely inspired by an actual 1970s murder case in Canaan, Connecticut which was the subject of the television film \"A Death in Canaan\" (1978) directed by Tony Richardson.\n\nSaturday Night and Sunday Morning (film): Saturday Night and Sunday Morning is a 1960 British drama film directed by Karel Reisz and produced by Tony Richardson.  It is an adaptation of the 1958 novel of the same name by Alan Sillitoe, who also wrote the screenplay adaptation.  The film is about a young machinist who spends his weekends drinking and partying, all the while having an affair with a married woman.\n\nKarel Reisz: Karel Reisz (21 July 1926 – 25 November 2002) was a British filmmaker who was active in post–World War II Britain, and one of the pioneers of the new realist strain in British cinema during the 1950s and 1960s.\n\nNight Must Fall (1964 film): Night Must Fall is a remake of the 1937 film of the same name, which was in turn based on the 1935 play by Emlyn Williams.  It was directed by Karel Reisz from a script by Clive Exton and starred Albert Finney, Mona Washbourne, and Susan Hampshire, but was not as successful as the original film.  The film was entered into the 14th Berlin International Film Festival.\n\nCindy Baer: Cindy Baer is an American actress, director, producer, and entrepreneur.  She helms the production company Free Dream Pictures, located in Burbank, California.\n\nQuestion: Cindy Baer and Karel Reisz, work in the film related industry?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_text\": {\n      \"type\": \"string\",\n      \"description\": \"The original question asked.\"\n    },\n    \"answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"The boolean answer to the question (true for yes, false for no).\"\n    },\n    \"individuals_involved\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"is_film_professional\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the individual works in the film-related industry.\"\n          },\n          \"film_roles\": {\n            \"type\": \"array\",\n            \"description\": \"A list of film-related roles or professions of the individual.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          },\n          \"associated_film_entities\": {\n            \"type\": \"array\",\n            \"description\": \"Companies, movements, or projects the individual is associated with in the film industry.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_film_professional\",\n          \"film_roles\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"question_text\",\n    \"answer\",\n    \"individuals_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_text": {
        "type": "string",
        "description": "The original question asked."
      },
      "answer": {
        "type": "boolean",
        "description": "The boolean answer to the question (true for yes, false for no)."
      },
      "individuals_involved": {
        "type": "array",
        "description": "Details about each individual mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "is_film_professional": {
              "type": "boolean",
              "description": "Indicates if the individual works in the film-related industry."
            },
            "film_roles": {
              "type": "array",
              "description": "A list of film-related roles or professions of the individual.",
              "items": {
                "type": "string"
              }
            },
            "associated_film_entities": {
              "type": "array",
              "description": "Companies, movements, or projects the individual is associated with in the film industry.",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "name",
            "is_film_professional",
            "film_roles"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "question_text",
      "answer",
      "individuals_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
