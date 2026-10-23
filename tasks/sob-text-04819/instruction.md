{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBilly Sandow: Wilhelm Baumann (September 4, 1884 – September 15, 1972), better known as Billy Sandow, was an American professional wrestler and promoter.  He is best remembered as the manager of professional wrestler Ed \"Strangler\" Lewis and a subsequent member of the famed Gold Dust Trio promotion that changed the face of the industry during the 1920s (along with Lewis and Joseph \"Toots\" Mondt).  He may have taken his ring name from Eugen Sandow, a professional wrestler and strongman in the late 19th century; in turn, former WWE wrestler Damien Sandow would adopt his own ring name in honor of Sandow almost a century later.  Sandow also served as manager for such wrestling champions as Billy Jenkins, Marin Plestina, Jumping Joe Savoldi and Everett Marshall, and also used the ring name The Zebra Kid in 1951.  He was a charter inductee of the Wrestling Observer Newsletter Hall of Fame in 1996.\n\nHiro Matsuda: Yasuhiro Kojima (小島 泰弘 , Kojima Yasuhiro ) , (July 22, 1937 – November 27, 1999), was a Japanese/American professional wrestler and trainer best known by his ring name Hiro Matsuda.  He trained many professional wrestlers including Hulk Hogan, Keiji Mutoh, \"Mr. Wonderful\" Paul Orndorff, Scott Hall, Lex Luger, \"Cowboy\" Bob Orton Jr, and Ron Simmons.\n\nRobert N. Bradbury: Robert N. Bradbury (March 23, 1886 – November 24, 1949) was an American film director and screenwriter who directed 125 movies between 1918 and 1941.  He is most famous for directing early Western films starring John Wayne in the 1930s, including \"Riders of Destiny\" (1933; an early singing-cowboy movie), \"The Lucky Texan\" (1934), \"West of the Divide\" (1934), \"Blue Steel\" (1934), \"The Man From Utah\" (1934), \"The Star Packer\" (1934), \"The Trail Beyond\" (1934; co-starring Noah Beery, Sr. and Noah Beery, Jr.), \"The Lawless Frontier\" (1934), \"Texas Terror\" (1935), \"Rainbow Valley\" (1935), \"The Dawn Rider\" (1935), \"Westward Ho\" (1935), and \"Lawless Range\" (1935).  These were inexpensively shot \"Poverty Row\" movies; many were also written by Bradbury and almost all of them featured character actor George \"Gabby\" Hayes.  Bradbury also shot numerous similar films during this period starring his son Bob Steele or Johnny Mack Brown.  Bradbury occasionally billed himself as \"Robert North Bradbury\", \"R.N. Bradbury\", or \"Robert Bradbury\".\n\nBob Orton: Robert Keith Orton Sr. (July 21, 1929 – July 16, 2006) was an American professional wrestler.\n\nBam Bam (wrestler): Jesús Guillermo Anaya Cortés is a Mexican luchador, or professional wrestler, best known under the ring name \"Bam Bam\", a Mini-Estrella, or \"Mini\" wrestler.  Anaya made his professional wrestling debut in 2002 and has worked mainly for the Mexican professional wrestling promotion Consejo Mundial de Lucha Libre (CMLL), where he is a former CMLL World Mini-Estrella Champion.  He is the son of professional wrestler Popitekus, Jr. who also helped train him for his pro wrestling career.\n\nBob Orton Jr.: Robert Keith Orton Jr. (born November 10, 1950), better known by the ring name \"Cowboy\" Bob Orton, is an American professional wrestler.  He is the son of professional wrestler Bob Orton Sr., the brother of professional wrestler Barry Orton, and the father of professional wrestler Randy Orton.  He is best known for his time in the WWF (World Wrestling Federation, now WWE).  He has also wrestled for several promotions in the United States, Japan, and other countries.\n\nKenji Sakaguchi (actor): Kenji Sakaguchi (坂口憲二 , Sakaguchi Kenji , born 8 November 1975) is a Japanese actor.  He has appeared in more than thirty films since 2000.  He is the son of former professional wrestler Seiji Sakaguchi and the brother of current professional wrestler Yukio.\n\nRandy Orton: Randal Keith Orton (born April 1, 1980) is an American professional wrestler and actor.  He is currently signed to WWE, where he performs on the SmackDown brand.\n\nAlex Roy (darts player): Alex Roy (born 4 September 1974 in Watford, Hertfordshire) is a darts player who competes in Professional Darts Corporation events.  He uses the nickname Ace of Herts for this matches and is with Dave Holland Management.  Roy's entrance music is \"Burn in My Light\" by Mercy Drive, which was the former theme of professional wrestler Randy Orton.  Roy even does Orton's trademark pose to the song once he steps onto the oche.\n\nBarry Orton: Randal Barry Orton (born May 28, 1958), better known as Barry Orton, is an American actor, musician, and former professional wrestler.  He is the son of retired professional wrestler Bob Orton, brother of professional wrestler Bob Orton Jr., and uncle of professional wrestler Randy Orton.\n\nQuestion: Barry Orton, is an American actor, musician, and former professional wrestler who has a son Bob Orton who plays in what sport?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who is the primary subject of the question.\"\n    },\n    \"person_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions held by the person.\"\n    },\n    \"has_son_named_bob_orton\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the context states that Barry Orton has a son named Bob Orton.\"\n    },\n    \"known_family_members\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the family member.\"\n          },\n          \"relationship_to_barry\": {\n            \"type\": \"string\",\n            \"enum\": [\n              \"father\",\n              \"brother\",\n              \"nephew\"\n            ],\n            \"description\": \"The relationship of this individual to Barry Orton.\"\n          },\n          \"profession\": {\n            \"type\": \"string\",\n            \"description\": \"The profession of the family member.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"relationship_to_barry\",\n          \"profession\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of Barry Orton's family members explicitly mentioned in the context, along with their relationships and professions.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"person_professions\",\n    \"has_son_named_bob_orton\",\n    \"known_family_members\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person who is the primary subject of the question."
      },
      "person_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions held by the person."
      },
      "has_son_named_bob_orton": {
        "type": "boolean",
        "description": "Indicates whether the context states that Barry Orton has a son named Bob Orton."
      },
      "known_family_members": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the family member."
            },
            "relationship_to_barry": {
              "type": "string",
              "enum": [
                "father",
                "brother",
                "nephew"
              ],
              "description": "The relationship of this individual to Barry Orton."
            },
            "profession": {
              "type": "string",
              "description": "The profession of the family member."
            }
          },
          "required": [
            "name",
            "relationship_to_barry",
            "profession"
          ],
          "additionalProperties": false
        },
        "description": "A list of Barry Orton's family members explicitly mentioned in the context, along with their relationships and professions."
      }
    },
    "required": [
      "person_name",
      "person_professions",
      "has_son_named_bob_orton",
      "known_family_members"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
