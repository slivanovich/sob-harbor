{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLamont Johnson: Ernest Lamont Johnson Jr. (September 30, 1922 – October 24, 2010) was an American actor and film director who has appeared in and directed many television shows and movies.  He won two Emmy Awards.\n\nManglehorn: Manglehorn is a 2014 American drama film directed by David Gordon Green and written by Paul Logan.  The film stars Al Pacino, Holly Hunter, Harmony Korine and Chris Messina.  It was selected to compete for the Golden Lion at the 71st Venice International Film Festival.  The film was released in theaters on June 19, 2015, by IFC Films.\n\nMister Lonely: Mister Lonely is a 2007 British-French-Irish-American comedy-drama film directed by Harmony Korine and co-written with his brother Avi Korine.  The film features an ensemble cast of international actors, including Diego Luna, Samantha Morton, Denis Lavant, Werner Herzog, James Fox, Anita Pallenberg and Leos Carax.\n\nDivision Films: Division Films is a Los Angeles-based film finance and production company established by Wicks Walker in 2012.  The company's first film was \"Spring Breakers\" starring James Franco, Selena Gomez, Vanessa Hudgens and Ashley Benson.  Walker and another producer greenlit the production after Benoît Debie was recruited as cinematographer to work alongside director Harmony Korine and with Selena Gomez added to the cast. \" Spring Breakers\" was selected for competition in the 69th Venice Film Festival and released worldwide in 2013.\n\nCary Woods: Cary Woods is an American film producer of over twenty titles across various genres, from worldwide blockbusters \"Scream\" and \"Godzilla\" to critically acclaimed breakouts by filmmakers Alexander Payne (\"Citizen Ruth\"), Larry Clark (\"Kids\"), Doug Liman (\"Swingers\"), James Mangold (\"Cop Land\") and Harmony Korine (\"Gummo\").\n\nFight Harm: Fight Harm is an abandoned project by Harmony Korine filmed in 1999.  The premise was to verbally provoke passers-by into a fight.  The rules were Korine couldn't throw the first punch and the person confronted had to be bigger than Korine.  To Korine, \"Fight Harm\" was high-comedy reminiscent of Buster Keaton.  \"I wanted to push humour to extreme limits to demonstrate that there's a tragic component in everything.\"  Filmed in New York, the project was abandoned following the injuries Korine received while shooting.\n\nLamont Johnson (Fretless Bassist): Eugene Lamont Johnson (born April 20, 1955, in Highland Park, Michigan), commonly known as E Lamont Johnson or Lamont Johnson, is an American musician.  He was the lead singer of the composition \"This Must Be Heaven\" and electric fretless bassist of the R&B band Brainstorm.  As a result of his electric fretless bass work throughout the mid 1970s, He gained recognition for being the first internationally recognized electric fretless bassist in R&B music.\n\nSpring Breakers: Spring Breakers is a 2012 American crime film written and directed by Harmony Korine.  It stars James Franco, Vanessa Hudgens, Selena Gomez, Ashley Benson and Rachel Korine and follows four college-aged girls on their spring break in Florida where they meet an eccentric local drug dealer named Alien who helps them in a time of desperation, and their eventual descent into a world of drugs, crime, and violence.\n\nHarmony Korine: Harmony Korine (born January 4, 1973) is an American film director and screenwriter.  He is best known for writing \"Kids\" and for writing and directing \"Spring Breakers\", \"Gummo\", \"Julien Donkey-Boy\" and \"Mister Lonely\".  His film \"Trash Humpers\" premiered at Toronto International Film Festival and won the main prize, the DOX Award, at CPH:DOX in November 2009.  His most recent film, \"Spring Breakers\", was released in 2013.\n\nA Crack Up at the Race Riots: A Crack Up at the Race Riots is a novel written by Harmony Korine, writer of such cult films as \"Kids\" and \"Spring Breakers\".  He is also writer/director of Gummo, Julien Donkey-Boy, Mister Lonely, and Trash Humpers.  The book was released in 1998 and had been taken out of print, however a new edition has been published by Drag City.\n\nQuestion: What do Lamont Johnson and Harmony Korine have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The profession shared by both individuals.\"\n    },\n    \"description_of_commonality\": {\n      \"type\": \"string\",\n      \"description\": \"A brief explanation of the shared commonality based on the context.\"\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"Details about each individual mentioned.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the individual.\"\n          },\n          \"primary_occupation\": {\n            \"type\": \"string\",\n            \"description\": \"The main occupation(s) of the individual as described in the context.\"\n          },\n          \"is_also_film_director\": {\n            \"type\": \"boolean\",\n            \"description\": \"Indicates if the individual is a film director.\"\n          },\n          \"directed_films\": {\n            \"type\": \"array\",\n            \"items\": {\n              \"type\": \"string\"\n            },\n            \"description\": \"A list of specific films directed by the individual, if mentioned.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"primary_occupation\",\n          \"is_also_film_director\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"common_profession\",\n    \"description_of_commonality\",\n    \"individuals\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_profession": {
        "type": "string",
        "description": "The profession shared by both individuals."
      },
      "description_of_commonality": {
        "type": "string",
        "description": "A brief explanation of the shared commonality based on the context."
      },
      "individuals": {
        "type": "array",
        "description": "Details about each individual mentioned.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The full name of the individual."
            },
            "primary_occupation": {
              "type": "string",
              "description": "The main occupation(s) of the individual as described in the context."
            },
            "is_also_film_director": {
              "type": "boolean",
              "description": "Indicates if the individual is a film director."
            },
            "directed_films": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of specific films directed by the individual, if mentioned."
            }
          },
          "required": [
            "name",
            "primary_occupation",
            "is_also_film_director"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "common_profession",
      "description_of_commonality",
      "individuals"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
