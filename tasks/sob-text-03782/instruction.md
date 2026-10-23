{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nChelsea Peretti: Chelsea Vanessa Peretti (born February 20, 1978) is an American comedian, actress, and writer.  She is best known for portraying Gina Linetti on the Fox comedy series \"Brooklyn Nine-Nine\". \" Paste\" ranked her Twitter account #75 on \"The 75 Best Twitter Accounts of 2014\".\n\nChas Hodges: Charles Nicholas \"Chas\" Hodges (born 28 December 1943) is an English musician and singer, probably best known for being one half, and lead vocalist, of the English musical duo Chas & Dave.\n\nVinnie Chas: Vincent Charles Pusateri (May 4, 1963 – April 6, 2010), best known by his stage name Vinnie Chas, was an American musician.  Born in Honolulu, Hawaii, he moved to Washington State as a child and while growing up there, he went to Bethel High School and were in several bands with childhood friend Jerry Cantrell.  In 1987, Chas joined Hollywood-based hard rock band Pretty Boy Floyd as their bassist.  He died on April 6, 2010 in Vancouver, Washington and is laid to rest in Spanaway, Washington.\n\nJimmie Walker: James Carter Walker, Jr. (born June 25, 1947), known professionally as Jimmie Walker, is an American actor and comedian.  Walker is best known for portraying James Evans, Jr. (J.J.), the oldest son of Florida and James Evans, Sr. on the CBS television series \"Good Times\" which originally ran from 1974–1979.  Walker was nominated for Golden Globe awards \"Best Supporting Actor In A Television Series\" in 1975 and 1976 for his role.  While on the show, Walker's character was known for the catchphrase \"\"Dy-no-mite!\"\"  which he also used in his mid–1970s TV commercial for a Panasonic line of cassette and 8-track tape players.  He also starred in \"Let's Do It Again\" with John Amos, and \"The Greatest Thing That Almost Happened\" with James Earl Jones.  Walker continues to tour the country with his stand-up comedy routine.\n\nBill Hicks: William Melvin Hicks (December 16, 1961 – February 26, 1994) was an American stand-up comedian, social critic, satirist, and musician.  His material, encompassing a wide range of social issues including religion, politics, and philosophy, was controversial, and often steeped in dark comedy.\n\nShaheed Woods: Shaheed K. Woods (born Shaheed Kamal Jihad Woods) is an American actor, comedian born and raised in Jersey City, New Jersey.  He is best known for \"A Gentleman\", \"Midnight Delight\", \"Life!  Camera Action...\" earning him accolades.\n\nChas Early: Chas Early is a British actor and playwright.  He has appeared on TV shows such as Casualty and EastEnders, \"Skins\" and Mayo.  He is probably best known for portraying the late comedian Bill Hicks in his one-man show, \"Bill Hicks: Slight Return\".\n\nLucy Pargeter: Lucy Kate Pargeter (born 1 March 1977) is an English actress.  She is best known for playing Helen Raven in \"Crossroads\" and Chas Dingle in \"Emmerdale\".  In 2013, she landed third place in the 13th series of I'm a Celebrity...Get Me Out of Here! .\n\nDave Peacock (musician): David Victor \"Dave\" Peacock (born 24 May 1945) is an English musician and bass guitarist.  He was raised in Ponders End and the Freezywater areas of Enfield.  Peacock is best known as having been one half of the English musical duo, Chas & Dave from 1975.\n\nSaeed Zahedi: Sir Mir Saeed Zahedi, OBE FREng RDI FIMechE PhD (born 23 May 1957) is a British-Iranian biomedical engineer and innovator who is currently the Technical Director at Chas A Blatchford & Sons.  He was named Royal Designer for Industry in 2014 and knighted \"for services to Engineering and Innovation\" in 2017.  He is one of the leading designers of prosthetics, best known for his work in the development of the world's first fully integrated, microprocessor controlled, lower limb system, Linx.\n\nQuestion: Chas Early is best known for portraying a comedian born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"portrayed_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person portrayed by the actor.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the person portrayed.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the person portrayed.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the comedian that Chas Early is best known for portraying.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"portrayed_person\",\n    \"answer_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "portrayed_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person portrayed by the actor."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the person portrayed."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the person portrayed."
          }
        },
        "required": [
          "name",
          "profession",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "answer_birth_year": {
        "type": "integer",
        "description": "The birth year of the comedian that Chas Early is best known for portraying."
      }
    },
    "required": [
      "actor_name",
      "portrayed_person",
      "answer_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
