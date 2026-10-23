{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nScott McCord: William Scott McCord (born April 19, 1971) is a Canadian actor, voice actor, musician, and composer currently based in Brooklyn.  A versatile performer, he has appeared in the films \"16 Blocks\", \"Shoot 'Em Up\", and the animated feature \"The Nut Job\".  On television, he is best known for his voice over work in popular animated series.  He plays Dan Kuso in \"Bakugan Battle Brawlers\", Tetsuya Watarigani in \"Beyblade Metal Fusion\", Owen and Trent in Fresh Animation's \"Total Drama\" series, Skull Boy in \"Ruby Gloom\", McGee in \"Camp Lakebottom\", and Jake in the animated TVOKids/Nickelodeon television series, \"PAW Patrol\".  He is also Co-Artistic Director of Toronto-based Criminal Theatre, along with playwright and actor Rosa Laborde.  In 2016, he won the Canada Screens Award for Best Performance in an Animated Series for his role as Squidgy on Guru's Justin Time.  In 2002 he was nominated for a Dora Mavor Moore Award with Best Performance by a Male in Independent Theatre for his performance in Jacob Richmond's The Qualities of Zero.  He has released two albums, the solo effort Blues For Sunshine (2009) and Scott McCord and the Bonafide Truth (2012).  The latter is also the name of the soul/jazz/blues/rock eight piece band that was created for touring the first album.  Scott McCord and the Bonafide Truth were nominated for Best Artist of the Year at the 2010 Maple Blues Awards.\n\nJames Woods: James Howard Woods (born April 18, 1947) is an American actor and producer.  He is known primarily for playing villainous roles, and has appeared in a variety of films, including \"The Way We Were\" (1973), \"The Onion Field\" (1979), \"Videodrome\" (1983), \"Once Upon a Time in America\" (1984), \"Best Seller\" (1987), \"Chaplin\" (1992), \"Casino\" (1995), \"Nixon\" (1995), \"Vampires\" (1998), \"Straw Dogs\" (2011) and \"White House Down\" (2013).  On television, he is known for portraying the titular protagonist of \"Shark\" (2006–2008), and for playing himself on eight episodes of the animated series \"Family Guy\", as well as on one episode of \"The Simpsons\".\n\nPablo Schreiber: Pablo Tell Schreiber (born April 26, 1978) is a Canadian-American actor known for his dramatic stage work and for his portrayal of Nick Sobotka on \"The Wire\" and for his role of George \"Pornstache\" Mendez on \"Orange Is the New Black\".  He was nominated for a Tony Award for his performance in \"Awake and Sing! \" on Broadway.  He also narrated the \"American Psycho\" audiobook.  He also starred in the HBO series \"The Brink\" as Lieutenant Commander Zeke \"Z-Pak\" Tilson, a Naval pilot who is also a drug dealer, and played a leading role in the Michael Bay film \"\" (2016).  He also played William Lewis on \"Law and Order Special Victims Unit\".  He appears in the television adaptation of \"American Gods\" as the leprechaun Mad Sweeney.\n\nRyan Stiles: Ryan Lee Stiles (born April 22, 1959) is a Canadian-American actor, comedian, producer and director whose work is often associated with improvisational comedy.  He is best known for his career and co-production work on the American and British versions of \"Whose Line Is It Anyway?\"  and the role of Lewis Kiniski on \"The Drew Carey Show\".  He played Herb Melnick on the CBS comedy \"Two and a Half Men\" and was a performer on the show \"Drew Carey's Improv-A-Ganza\".\n\nWill Arnett: William Emerson Arnett ( ; born May 4, 1970) is a Canadian-American actor, voice actor and comedian.  He is best known for his role as George Oscar \"Gob\" Bluth II in the Fox/Netflix series \"Arrested Development\" (2003–2006, 2013, 2018); as well as his titular role as BoJack Horseman in the Netflix Original Series of the same name (2014-present).  He has appeared in films such as \"Blades of Glory\" (2007), \"Hot Rod\" (2007) and \"Teenage Mutant Ninja Turtles\" (2014).\n\nPedro Regas: Petros \"Pedro\" Regas (Greek: Πέτρος Ρεγάκος; April 18, 1897 – August 10, 1974) was a Greek American actor born in Sparta, Greece and was the brother of actor George Regas.\n\nGravedale High: Gravedale High (also known as Rick Moranis in Gravedale High) is an animated series produced by Hanna-Barbera for NBC Productions (the latter company owns all rights to the series).  The series premiered in the fall of 1990 on NBC and lasted thirteen episodes.\n\nEric McCormack: Eric James McCormack (born April 18, 1963) is a Canadian-American actor known for his role as Will Truman in the American sitcom \"Will & Grace\" and Dr. Daniel Pierce in the American crime drama \"Perception\".\n\nRick Moranis: Frederick Allan \"Rick\" Moranis (born April 18, 1953) is a Canadian-American actor, comedian, screenwriter, producer, musician, and songwriter.  He is currently on film acting hiatus.  He came to prominence in the sketch comedy series \"Second City Television\" (\"SCTV\") in the 1980s and later appeared in several Hollywood films, including \"Strange Brew\" (1983), \"Ghostbusters\" (1984), \"Spaceballs\" (1987), \"Little Shop of Horrors\" (1986), \"Honey, I Shrunk the Kids\" (1989, and its 1992 and 1997 sequels), \"Parenthood\" (1989), \"My Blue Heaven\" (1990), and \"The Flintstones\" (1994).\n\nDrew Seeley: Andrew Michael Edgar \"Drew\" Seeley (born April 30, 1982) is a Canadian-American actor, singer and dancer.  He has recorded many songs for the Walt Disney Company.  He danced as a child in Ontario until he was about pre-teen age and then moved to Florida.  Drew is married to actress/comedian Amy Paffrath.\n\nQuestion: What animated series has the same name as a Canadian-American actor born April 18, 1953?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\"\n        },\n        \"nationality\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"animated_series\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"main_title\": {\n          \"type\": \"string\"\n        },\n        \"alternative_title_with_actor\": {\n          \"type\": \"string\"\n        },\n        \"premiere_year\": {\n          \"type\": \"integer\"\n        },\n        \"number_of_episodes\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"main_title\",\n        \"alternative_title_with_actor\",\n        \"premiere_year\",\n        \"number_of_episodes\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"reasoning\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"actor_details\",\n    \"animated_series\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "birth_date": {
            "type": "string",
            "format": "date"
          },
          "nationality": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "birth_date",
          "nationality"
        ],
        "additionalProperties": false
      },
      "animated_series": {
        "type": "object",
        "properties": {
          "main_title": {
            "type": "string"
          },
          "alternative_title_with_actor": {
            "type": "string"
          },
          "premiere_year": {
            "type": "integer"
          },
          "number_of_episodes": {
            "type": "integer"
          }
        },
        "required": [
          "main_title",
          "alternative_title_with_actor",
          "premiere_year",
          "number_of_episodes"
        ],
        "additionalProperties": false
      },
      "reasoning": {
        "type": "string"
      }
    },
    "required": [
      "actor_details",
      "animated_series",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
