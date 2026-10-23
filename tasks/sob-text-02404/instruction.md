{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPosorja: Posorja is a small village in Ecuador that lies about 120 km from the city Guayaquil at the delta of the Guayas River.  Posorja lies in a very dry climate zone.  Many years ago, the main occupation in Posorja was fishing.  However, increasing pollution of the sea and new high-tech fishing methods have drastically lowered the income of the people of Posorja.  Three fish processing factories give part-time work to some of the people.  Of the 15,000 people in the area, 60% do not have regular employment.\n\nRichard Stuverud: Richard Stuverud (born September 26, 1964) is an American drummer from Seattle, Washington, United States.  Known for playing in several bands in the Seattle scene, his first, in the early 80s, was the punk rock band The Fastbacks.  Through the mid-90s, Stuverud played in the bands Three Fish and Tres Mts. , both side projects of Pearl Jam bassist, Jeff Ament.  Three Fish released the albums \"Three Fish\" (1996) and \"The Quiet Table\" (1999), through Epic Records.  The album \"Tres Mts.  (Three Mountains),\" with Doug Pinnick of King's X and guest guitarist Mike McCready, was released in 2011.\n\nThe Limousines: The Limousines are an American indietronica band based out of California's San Francisco Bay Area.  Made up of multi-instrumentalist/producer Giovanni Giusti and\n\nThree Fish: Three Fish was an American rock band formed in 1994 by Pearl Jam's Jeff Ament.  The lineup featured Ament, Robbi Robb of Tribe after Tribe, and Richard Stuverud of the Fastbacks and War Babies.\n\nRaingods with Zippos: Raingods with Zippos is a 1999 progressive rock album by ex-Marillion vocalist Fish.  It was released on the Roadrunner record label, more well-known for its heavy metal releases.  \"Raingods with Zippos\" is often hailed as one of Fish's greatest solo achievements along with his 1990 debut Vigil in a Wilderness of Mirrors.  It is the first of three Fish albums to be produced by Elliot Ness (not including the \"best of\" collection Kettle of Fish from 1998, with which Ness was involved).  While he was not involved with the production of this album, Steven Wilson, most famous for his work with Porcupine Tree, played guitar on several of the tracks.\n\nAquarium (video game): Aquarium is a Tetris variant puzzle arcade game released by Excellent System in 1996 in Japan only.  Play consists of matching three fish shapes rows to make them disappear.\n\nThe Quiet Table: The Quiet Table is the second studio album by the American rock band Three Fish.  It was released on June 1, 1999 through Epic Records.\n\nRobot fish: A robot fish is a type of bionic robot, which has the shape and locomotion of a living fish.  Since the Massachusetts Institute of Technology first published research on them in 1989, there has been more than 400 articles published about robot fish.  According to these reports, approximately 40 different types of robot fish have been build, with 30 designs having only the capability to flip and drift in water.  Most robot fish are designed to emulate living fish which use Body-caudal fin (BCF) propulsion.  BCF robot fish can be divided into three categories: Single Joint (SJ), Multi-Joint (MJ), and smart material-based design.  The most important parts of researching and developing robot fish are advancing their control and navigation, enabling them to 'communicate' with their environment, making it possible for them to travel along a particular path, and to respond to commands to make their 'fins' flap.\n\nKorean nationality: Korean nationality (Korean: 한국국적 ) refers to citizenship of the Korea.  Korean citizen (Korean: 한국인 ) refers to citizen of the Korea.  Korea is divided into two distinct sovereign states, North Korea (Democratic People's Republic of Korea) and South Korea (Republic of Korea).  Nowadays, there are three kinds of Korean nationality: South Korean nationality, North Korean nationality, and Chōsen-seki (ethnic Koreans in Japan who have neither Japanese nor South Korean citizenship).\n\nThree Fish (album): Three Fish is the debut studio album by the American rock band Three Fish.  It was released on June 11, 1996 through Epic Records.\n\nQuestion: Three Fish and The Limousines, are bands of which nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"bands\": {\n      \"type\": \"array\",\n      \"description\": \"List of bands mentioned in the question.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the band.\"\n          }\n        },\n        \"required\": [\n          \"name\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The shared nationality of the bands.\"\n    },\n    \"number_of_bands\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of bands identified.\"\n    }\n  },\n  \"required\": [\n    \"bands\",\n    \"common_nationality\",\n    \"number_of_bands\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "bands": {
        "type": "array",
        "description": "List of bands mentioned in the question.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the band."
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        }
      },
      "common_nationality": {
        "type": "string",
        "description": "The shared nationality of the bands."
      },
      "number_of_bands": {
        "type": "integer",
        "description": "The total number of bands identified."
      }
    },
    "required": [
      "bands",
      "common_nationality",
      "number_of_bands"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
