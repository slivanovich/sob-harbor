{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Christmas Carol (1997 film): A Christmas Carol is a 1997 American animated musical film version of the book of the same name by Charles Dickens.  It features eight new songs and a voice line-up including Tim Curry, Whoopi Goldberg, Ed Asner, and Michael York.\n\nUp (2009 film): Up is a 2009 American 3D computer-animated comedy-adventure film produced by Pixar Animation Studios and released by Walt Disney Pictures.  Directed by Pete Docter, the film centers on an elderly widower named Carl Fredricksen (Ed Asner) and an earnest young \"Wilderness Explorer\" (a fictional youth group similar to the Boy Scouts) named Russell (Jordan Nagai).  By tying thousands of balloons to his home, Carl sets out to fulfill his dream to see the wilds of South America and complete a promise made to his late wife, Ellie.  The film was co-directed by Bob Peterson, with music composed by Michael Giacchino.\n\nGood Men: Good Men is a 12-minute short film starring Ed Asner and Mark Rydell, written & directed by Brian Connors and produced by Sean Tracey.  Associate Producers were Dean Jamali, Neal Wilde, Tom Downey, Phil Gillin, and Mehrdad Sahafi.  This micro-budget, two-character film was shot in one day.  The drama takes place on an afternoon before an Oscar party.  Asner & Rydell get into an argument over the Holocaust, the proposed mosque at ground zero and the conspiracy allegations surrounding the 9/11 attacks on the World Trade Center.  \"Good Men\" won Best Short at The Los Angeles Arthouse Film Festival in 2012 and screened in numerous cities around the U.S. as well as around the world.\n\nLuxo Jr. (character): Luxo Jr. is a desk lamp character and the corporate mascot of Pixar Animation Studios.  Luxo Jr. is the protagonist of the short film of the same name and appears on the production logo of every Pixar film, hopping on screen and bouncing on the letter I. John Lasseter created Luxo Junior, modeling the character after his own Luxo brand lamp.  The manufacturer of Luxo lamps sued Disney, the parent company of Pixar, for selling Luxo Jr. branded merchandise in 2009.\n\nPAJ animation studio: PAJ animation studio is a persian animation film studio based in IRAN.  The studio produced several short films, television commercials, and one feature film.  It was founded on 30 October 2007.  PAJ animation studio produced a mini series called the hidden lives in 2017 .\n\nFarkhondeh Torabi: Farkhondeh Torabi (born March, 1965 in Tehran, Iran) is an internationally acclaimed Persian animation director.\n\nAxel: The Biggest Little Hero: Axel: The Biggest Little Hero (original title: Bonta) is a 2013 animated 3-D film written and directed by Leo Lee.  The English language version stars the voices of Yuri Lowenthal, Sarah Natochenny, Colleen O'Shaughnessey, Kate Higgins and Ed Asner.  Under its original title of \"Bonto\", the film released nationwide across China on August 2, 2013, as China’s very first 3-D film to combine stereoscopic effects with CG technology, representing their highest level of animation.\n\nEd Asner filmography: Ed Asner has a career in Hollywood that spans over five decades, in film as well as television and voice acting.\n\nMehrdad Raissi Ardali: Mehrdad Raissi Ardali (Persian: مهرداد رئیسی اردلی‎ ‎ ), born (1978--)20 1978 in Iran, is a prolific Iranian voice actor, dubbing director, founder, director, CEO and Quality Control Manager of Glory Entertainment (The Association of Tehran Young Voice Actors).  He has also provided Persian voices for several animation characters, including famous characters such as Donkey in \"Shrek\", Marty in \"Madagascar\", \"\" and \"\", Buck in \"\", Bolt in \"Bolt\", Carl Fredricksen in \"Up\", Flynn Rider in \"Tangled\", The Once-ler in \"The Lorax\", RJ in \"Over the Hedge\", Francesco Bernoulli in \"Cars 2\", Mr. Ping in \"Kung fu Panda\", Ramon in \"Happy Feet 2\", The Man in the Yellow Hat in \"Curious George\", Raoul in \"A Monster in Paris\", Kevin in \"\", Barry in \"Bee Movie\", Bunnymund in \"Rise of the Guardians\", Guy in \"The Croods\" and Kristoff in \"Frozen (2013 film)\".\n\nI Know That Voice: I Know That Voice is a documentary about American voice acting.  It premiered on November 6, 2013, at Grauman's Egyptian Theatre.  It is narrated by John DiMaggio, the voice of Bender on \"Futurama\" and Jake on \"Adventure Time\", and stars DiMaggio and many other voice actors, including Billy West, Tara Strong, Tom Kenny, Grey DeLisle, June Foray, Rachael MacFarlane, Mark Hamill, Ed Asner, Robin Atkin Downes, and Pamela Adlon.\n\nQuestion: Who provided the voice in the Persian animation of the 2009 Pixar film of the character orginally voiced by Ed Asner\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the animated film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"animation_studio\": {\n          \"type\": \"string\",\n          \"description\": \"The animation studio that produced the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"animation_studio\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"character_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character.\"\n        },\n        \"original_voice_actor\": {\n          \"type\": \"string\",\n          \"description\": \"The original English voice actor for the character.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"original_voice_actor\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"persian_dubbing_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"voice_actor\": {\n          \"type\": \"string\",\n          \"description\": \"The voice actor who provided the Persian voice for the character.\"\n        }\n      },\n      \"required\": [\n        \"voice_actor\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_details\",\n    \"character_details\",\n    \"persian_dubbing_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the animated film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "animation_studio": {
            "type": "string",
            "description": "The animation studio that produced the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "animation_studio"
        ],
        "additionalProperties": false
      },
      "character_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the character."
          },
          "original_voice_actor": {
            "type": "string",
            "description": "The original English voice actor for the character."
          }
        },
        "required": [
          "name",
          "original_voice_actor"
        ],
        "additionalProperties": false
      },
      "persian_dubbing_details": {
        "type": "object",
        "properties": {
          "voice_actor": {
            "type": "string",
            "description": "The voice actor who provided the Persian voice for the character."
          }
        },
        "required": [
          "voice_actor"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_details",
      "character_details",
      "persian_dubbing_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
