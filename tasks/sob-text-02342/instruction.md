{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRob Brydon: Robert Brydon Jones, (born 3 May 1965), known professionally as Rob Brydon, is a Welsh actor, comedian, radio and television presenter, singer and impressionist.  He played Dr Paul Hamilton in the Australian/British comedy series \"Supernova\", Bryn West in the sitcom\" Gavin & Stacey\" and Keith Barret in the BBC comedy series \"Marion and Geoff\" and its spin-off \"The Keith Barret Show\".\n\nDavid Jason: Sir David John White, {'1': \", '2': \", '3': \", '4': \"} (born 2 February 1940), better known by his stage name David Jason, is an English actor and comedian.  He is perhaps best known for his portrayals of Derek \"Del Boy\" Trotter in the BBC comedy series \"Only Fools and Horses\", and Detective Inspector Jack Frost in the ITV crime drama \"A Touch of Frost\".\n\nJoivan Wade: Joivan Wade is an English actor who first appeared in the BBC comedy \"Big School\", before starring in teen drama \"Youngers\" on E4.  He is a YouTube performer with the online comedy series \"Mandem On The Wall\" and appeared in the \"Doctor Who\" Series 8 episode \"Flatline\" as Rigsy, a young graffiti artist who helped save the world.  Wade later returned as Rigsy in the \"Doctor Who\" Series 9 episode \"Face the Raven\".  Wade later joined the cast of BBC soap opera \"EastEnders\" in February 2016 as Jordan Johnson, taking over the role from Michael-Joel David Stuart.\n\nDel Boy: Derek Edward Trotter, more commonly known as Del Boy (born 12 July 1945), is the fictional lead character in the popular BBC sitcom \"Only Fools and Horses\" and one of the main characters of its prequel, \"Rock & Chips\".  He was played by David Jason in the original series and was portrayed as a teenager by James Buckley in the prequel.  Del is known for his broken French quotes which are usually completely out of context and a variety of catchphrases, including: \"He who dares – wins!\" , \"This time next year we'll be millionaires\", \"Lovely Jubbly!\" , \"You know it makes sense\" (which he usually says to his customers after they've agreed on a deal) and \"You plonker!\"  (which he usually says to Rodney).\n\nSwiss Toni: Swiss Toni is a fictional used-car dealer played by Charlie Higson, and also the title of a sitcom in which he is the main character.  Swiss is a 50-something car dealer going through a midlife crisis.  To Toni almost any situation in life is best considered as being \"like making love to a beautiful woman\", in some rather implausible ways.  Swiss is usually depicted wearing a grey suit and with his hair styled in a platinum blond bouffant quiff.  The character was created by Charlie Higson and Bob Mortimer and originally introduced in the BBC comedy series \"The Smell of Reeves and Mortimer\", but is best known as a recurring character in another BBC comedy series, \"The Fast Show\".\n\nBuster Merryfield: Harry \"Buster\" Merryfield (27 November 1920 – 23 June 1999) was an English actor best known for starring as Uncle Albert in the BBC comedy \"Only Fools and Horses\".\n\nThe Royal Bodyguard: The Royal Bodyguard is a British television sitcom, written by Mark Bussell and Justin Sbresni, and starring David Jason, Geoffrey Whitehead, Timothy Bentinck and Tim Downie.  A series of six episodes began on 26 December 2011, concluding on 30 January 2012.  The first episode picked up more than 8 million viewers but the series soon declined in ratings.  The series was heavily criticised by viewers and critics.  At 71 Jason was widely felt to be too old for the lead role.\n\nRock &amp; Chips: Rock & Chips is a British television comedy-drama and a prequel to the sitcom \"Only Fools and Horses\".  Set in 1960s Peckham, it focuses primarily on the lives of Del Trotter, Freddie Robdal and Joan and Reg Trotter.  Nicholas Lyndhurst, who played Rodney in \"Only Fools and Horses\", plays Robdal alongside James Buckley (Del Boy), Kellie Bright (Joan), Shaun Dingwall (Reg) and Phil Daniels (Grandad).  The Shazam Productions and BBC co-production was written by \"Only Fools and Horses\" creator John Sullivan, directed by Dewi Humphreys and produced by Gareth Gwenlan.\n\nKelly-Anne Lyons: Kelly-Anne Lyons (born 17 March 1985) is an American actress, television presenter, writer and model.  Lyons' breakthrough role was as the female lead, Kelly-Anne Manhattan, in the BBC comedy \"Dick and Dom's Funny Business\".  Before this, Lyons played the title role in \"Chelsey: OMG!\" , produced by British comedy and entertainment company Channel X.  She is known for her characters in hidden camera sketch shows such as ITV1’s \"Fool Britannia\" with Dom Joly and BBC1’s \"Richard Hammond’s Secret Service\", as well as MTV’s \"Flash Prank\", Channel 5 (UK) ’s \"Secret Interview\", and National Geographic’s \"Ape Man\".  She plays news anchor \"Felicity Bond\" in the BAFTA nominated BBC comedy \"DNN\" and \"Tess\" in BBC’s sitcom \"Badults\".\n\nDavid Benson: David Benson (born David Hodgson on 11 January 1962) is an English character actor, writer and comedian, most famous for his one-man show titled \"Think No Evil of Us: My Life with Kenneth Williams\" about the life and career of the late comedian, for which he won the \"Scotsman's\" Fringe First award in 1996, and for his television role as Noël Coward in the BBC comedy series \"Goodnight Sweetheart\".  His theatrical repertoire includes a wide range of Coward's best known songs, performed in-character as Coward.  When not touring in the theatre he can be found on BBC radio, playing all the character parts in the science fiction comedy series \"The Scarifyers\".\n\nQuestion:  The Royal Bodyguard is a British television sitcom starring an English actor best known for his portrayals of Derek \"Del Boy\" Trotter in what BBC comedy series? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor starring in 'The Royal Bodyguard'.\"\n    },\n    \"actor_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the actor.\"\n    },\n    \"series_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the series the actor starred in, as mentioned in the question.\"\n    },\n    \"best_known_role\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character the actor is best known for.\"\n        },\n        \"series_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the BBC comedy series where the actor played the best-known character.\"\n        },\n        \"series_network\": {\n          \"type\": \"string\",\n          \"description\": \"The network that broadcast the best-known series.\"\n        },\n        \"series_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the best-known series.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"series_name\",\n        \"series_network\",\n        \"series_genre\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"actor_nationality\",\n    \"series_starred_in\",\n    \"best_known_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor starring in 'The Royal Bodyguard'."
      },
      "actor_nationality": {
        "type": "string",
        "description": "The nationality of the actor."
      },
      "series_starred_in": {
        "type": "string",
        "description": "The name of the series the actor starred in, as mentioned in the question."
      },
      "best_known_role": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character the actor is best known for."
          },
          "series_name": {
            "type": "string",
            "description": "The name of the BBC comedy series where the actor played the best-known character."
          },
          "series_network": {
            "type": "string",
            "description": "The network that broadcast the best-known series."
          },
          "series_genre": {
            "type": "string",
            "description": "The genre of the best-known series."
          }
        },
        "required": [
          "character_name",
          "series_name",
          "series_network",
          "series_genre"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "actor_nationality",
      "series_starred_in",
      "best_known_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
