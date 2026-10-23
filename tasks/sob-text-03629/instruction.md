{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMarshall Space Flight Center: The George C. Marshall Space Flight Center (MSFC), located in Huntsville, Alabama, is the U.S. government's civilian rocketry and spacecraft propulsion research center.  The largest NASA center, MSFC's first mission was developing the Saturn launch vehicles for the Apollo moon program.  Marshall has been the agency's lead center for Space Shuttle propulsion and its external tank; payloads and related crew training; International Space Station (ISS) design and assembly; and computers, networks, and information management.  Located on the Redstone Arsenal near Huntsville, Alabama, MSFC is named in honor of General of the Army George Marshall.\n\nBruce Robinson: Bruce Robinson (born 2 May 1946) is an English director, screenwriter, novelist and actor.  He wrote and directed the cult classic \"Withnail and I\" (1987), a film with comic and tragic elements set in London in the 1960s, which drew on his experiences as a struggling actor, living in poverty in Camden Town.\n\nPolicy Planning Staff (United States): The Policy Planning Staff (sometimes referred to as the Policy Planning Council, the Office of Policy Planning or by its in-house acronym S/P) is the principal strategic arm of the United States Department of State.  It was created in 1947 by renowned Foreign Service Officer George F. Kennan at the request of Secretary of State George Marshall to serve \"as a source of independent policy analysis and advice for the Secretary of State.\"  Its first assignment was to design the Marshall Plan.\n\nGeorge Marshall (director): George E. Marshall (December 29, 1891 – February 17, 1975) was an American actor, screenwriter, producer, film and television director, active through the first six decades of movie history.\n\nGeorge C. Marshall High School: George C. Marshall High School is a public school in northern Virginia, located in Idylwood in unincorporated Fairfax County, near Falls Church.  Named for General George Marshall, it opened in 1962 and is part of Fairfax County Public Schools (FCPS).  It is ranked at #343 in the nation for public schools and has received a gold award for Best High Schools from the U.S. News & World Report 2016.  It is ranked 11th in Virginia and 8th in Fairfax County.  George C. Marshall High School is a fully accredited high school based on the Standards of Learning tests in Virginia.\n\nShow Them No Mercy!: Show Them No Mercy!  is a 1935 American crime film directed by George Marshall and written by Kubec Glasmon and Henry Lehrman.  The film stars Rochelle Hudson, Cesar Romero, Bruce Cabot, Edward Norris, Edward Brophy and Warren Hymer.  The film was released on December 6, 1935, by 20th Century Fox.\n\nCharles Marshall (colonel): Charles Marshall (October 3, 1830 – April 19, 1902) was a Confederate Army officer during the American Civil War.  Marshall served as an aide de camp, assistant adjutant general and military secretary to Gen. Robert E. Lee.  He was also a cousin of World War II General George Marshall.\n\nThe Guns of Fort Petticoat: The Guns of Fort Petticoat is a 1957 Technicolor Western produced by Harry Joe Brown and Audie Murphy for Columbia Pictures.  It was based on the 1955 short story \"Petticoat Brigade\" by Chester William Harrison (1913–1994) that he expanded into a novelization for the film's release.  It was directed by George Marshall and filmed at the Iverson Movie Ranch and at Old Tucson.  The working title of the film was \"Petticoat Brigade\"; screenwriter and television director Walter Doniger was originally set to have directed the film.  The fictional story tells the tale of an Army deserter training a disparate group of women to be Indian fighters climaxing in a Battle of the Alamo type action.\n\nGeorge Marshall (philanthropist): Reverend George Marshall (1753 in Bishop Waltham, Hants – 1819) served as a curate in Horsham for over thirty years, from about 1778 until his death in 1819, although he was not fully ordained as a minister until 1802.  Marshall also acted as chaplain to the prisoners in Horsham gaol.  It is clear from some of his letters in the Horsham Museum archives that George Marshall was a somewhat awkward and abrasive character.\n\nGeorge Marshall Ruge: George Marshall Ruge is an American film director, writer, second unit director, stunt coordinator, and actor.\n\nQuestion: George Marshall and Bruce Robinson, have occupations of director, screenwriter, and actor?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"target_occupations\": {\n      \"type\": \"array\",\n      \"description\": \"A list of occupations that the question is inquiring about for the individuals.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"occupations_listed_in_context\": {\n            \"type\": \"array\",\n            \"description\": \"All occupations found for this individual in the provided context.\",\n            \"items\": {\n              \"type\": \"string\"\n            }\n          },\n          \"has_all_target_occupations\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the individual has all the occupations specified in 'target_occupations', false otherwise.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"occupations_listed_in_context\",\n          \"has_all_target_occupations\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"all_individuals_have_target_occupations\": {\n      \"type\": \"boolean\",\n      \"description\": \"The final answer to the question: True if all specified individuals have all the target occupations, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"target_occupations\",\n    \"individuals\",\n    \"all_individuals_have_target_occupations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "target_occupations": {
        "type": "array",
        "description": "A list of occupations that the question is inquiring about for the individuals.",
        "items": {
          "type": "string"
        }
      },
      "individuals": {
        "type": "array",
        "description": "Details about each individual mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "occupations_listed_in_context": {
              "type": "array",
              "description": "All occupations found for this individual in the provided context.",
              "items": {
                "type": "string"
              }
            },
            "has_all_target_occupations": {
              "type": "boolean",
              "description": "True if the individual has all the occupations specified in 'target_occupations', false otherwise."
            }
          },
          "required": [
            "name",
            "occupations_listed_in_context",
            "has_all_target_occupations"
          ],
          "additionalProperties": false
        }
      },
      "all_individuals_have_target_occupations": {
        "type": "boolean",
        "description": "The final answer to the question: True if all specified individuals have all the target occupations, false otherwise."
      }
    },
    "required": [
      "question_asked",
      "target_occupations",
      "individuals",
      "all_individuals_have_target_occupations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
