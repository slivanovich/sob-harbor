{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKen Sagoes: Ken Sagoes (born 1967) is an American actor.  He is best known for his role as Roland Kincaid in the fantasy horror film \"\" (1987) and the sequel \"\" (1988).  Sagoes' portrayed Darryl in the television series \"What's Happening Now!! \" from 1987-1988.  He has made guest appearances on shows such as \"The Twilight Zone\" (Episode: \"But Can She Type? \"), \"Night Court\", \"My So-Called Life\", \"Martin\", \"The Parkers\", \"The Division\", and \"The District\".\n\nBrooke Kennedy: Brooke Kennedy is an American television producer and director.  Her credits include \"Crime Story\", \"My So-Called Life\", \"Numb3rs\", \"Pushing Daisies\" and \"Fringe\".  She was also a producer and director on \"Third Watch\" and currently serves as a producer on \"The Good Wife\".  In addition, she was also a writer on the series \"Prince Street\" and \"Third Watch\".  In 2010 and 2011, she was nominated two Primetime Emmy Awards for \"The Good Wife\" as a part of the producing team.\n\nDevon Gummersall: Devon Gummersall (born October 15, 1978) is an American actor, writer, and television and film director best known for his role as on ABC's \"My So-Called Life\".\n\nJared Leto: Jared Joseph Leto ( ; born December 26, 1971) is an American actor, singer, songwriter, and director.  After starting his career with television appearances in the early 1990s, Leto achieved recognition for his role as Jordan Catalano on the television series \"My So-Called Life\" (1994).  He made his film debut in \"How to Make an American Quilt\" (1995) and received critical praise for his performance in \"Prefontaine\" (1997).  Leto played supporting roles in \"The Thin Red Line\" (1998), \"Fight Club\" (1999) and \"American Psycho\" (2000), as well as the lead role in \"Urban Legend\" (1998), and earned critical acclaim after portraying heroin addict Harry Goldfarb in \"Requiem for a Dream\" (2000).  He later began focusing increasingly on his music career, returning to acting with \"Panic Room\" (2002), \"Alexander\" (2004), \"Lord of War\" (2005), \"Lonely Hearts\" (2006), \"Chapter 27\" (2007), and \"Mr. Nobody\" (2009).  In 2012, he directed the documentary film \"Artifact\".  In 2016, he played the DC Comics supervillain Joker in the DC Extended Universe film \"Suicide Squad\".\n\nJared Leto filmography: Jared Leto is an American entertainer who has had an extensive career in film, music, and television.  He made his debut with minor roles in the television shows \"Camp Wilder\" (1992) and \"Almost Home\" (1993).  He achieved recognition in 1994 for his role as Jordan Catalano in the teen drama television series \"My So-Called Life\".  The show was praised for its portrayal of adolescence and gained a cult following, despite being canceled after only one season.  The same year, he made his television film debut starring alongside Alicia Silverstone in \"Cool and the Crazy\".  Leto's first film role was in the 1995 drama \"How to Make an American Quilt\".  He later co-starred with Christina Ricci in \"The Last of the High Kings\" (1996) and received a supporting role in \"Switchback\" (1997).  In 1997, Leto starred in the biopic \"Prefontaine\" in which he played the role of Olympic hopeful Steve Prefontaine.  His portrayal received positive reviews from critics and is often considered his breakthrough role.  The following year, Leto starred together with Alicia Witt in the horror \"Urban Legend\".  He then acted alongside Sean Penn and Adrien Brody in the war film \"The Thin Red Line\" (1998).  After playing supporting roles in \"Black and White\" and \"Girl, Interrupted\", Leto portrayed Angel Face in \"Fight Club\" (1999), which has since became a cult film.\n\nBasil (film): Basil is a 1998 British historical drama film directed by Radha Bharadwaj and starring Christian Slater, Jared Leto, Claire Forlani and Derek Jacobi.  It was based on the 1852 novel \"Basil\" by Victorian author Wilkie Collins.  The adaptation is by Bharadwaj.\n\nMy So-Called Life: My So-Called Life is an American teen drama television series created by Winnie Holzman and produced by Edward Zwick and Marshall Herskovitz.  It originally aired on ABC from August 25, 1994, to January 26, 1995, and was distributed by The Bedford Falls Company with ABC Productions.\n\nChannon Roe: James Channon Roe (born October 27, 1969) is an American actor.  He began his film and television career in the mid-1990s.  He first appeared on TV series \"My So-Called Life\" as Billy in 1994.  Roe began his acting career in independent films, including \"The Low Life\" and \"Junked\".\n\nPilot (My So-Called Life): \"Pilot\" is the first episode of the American teen drama television series \"My So-Called Life\".  The episode premiered on ABC on August 25, 1994.  Written by series creator Winnie Holzman and directed by Scott Winant, the episode begins the story of Angela Chase (Claire Danes), a fifteen-year-old high school sophomore who is experiencing the difficulties of friends and parents.  In addition, the pilot also introduces the supporting cast, including Angela's parents, Patty and Graham, her two best friends, Rayanne Graff and Rickie Vasquez, as well as Angela's love interest, Jordan Catalano.\n\nWilson Cruz: Wilson Cruz (born Wilson Echevarría; December 27, 1973) is an American actor known for playing Rickie Vasquez on \"My So-Called Life\", Angel in the Broadway production of \"Rent\" and the recurring character Junito on \"Noah's Arc\".  As an openly gay man of Puerto Rican ancestry, he has served as an advocate for gay youth, especially gay youth of color.\n\nQuestion: When was the American actor, singer, songwriter, and director born who has role in both Basil and \"My So-Called Life\" (1994)?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the person in YYYY-MM-DD format.\"\n    },\n    \"professions\": {\n      \"type\": \"array\",\n      \"description\": \"A list of professions attributed to the person.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"notable_roles\": {\n      \"type\": \"array\",\n      \"description\": \"A list of specific roles or appearances that helped identify the person.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\",\n            \"description\": \"The title of the film or television series.\"\n          },\n          \"year\": {\n            \"type\": \"integer\",\n            \"description\": \"The year of release or airing.\"\n          },\n          \"character_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the character played, if specified.\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"year\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"birth_date\",\n    \"professions\",\n    \"notable_roles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person identified."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the person in YYYY-MM-DD format."
      },
      "professions": {
        "type": "array",
        "description": "A list of professions attributed to the person.",
        "items": {
          "type": "string"
        }
      },
      "notable_roles": {
        "type": "array",
        "description": "A list of specific roles or appearances that helped identify the person.",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "The title of the film or television series."
            },
            "year": {
              "type": "integer",
              "description": "The year of release or airing."
            },
            "character_name": {
              "type": "string",
              "description": "The name of the character played, if specified."
            }
          },
          "required": [
            "title",
            "year"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "person_name",
      "birth_date",
      "professions",
      "notable_roles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
