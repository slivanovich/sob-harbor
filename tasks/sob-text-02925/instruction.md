{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMargaret Brown: Margaret \"Maggie\" Brown (née Tobin) (July 18, 1867 – October 26, 1932) (posthumously known as \"The Unsinkable Molly Brown\") was an American socialite and philanthropist.  She is best remembered for exhorting the crew in Lifeboat No. 6 to return to the debris field of the 1912 sinking of RMS \"Titanic\" to look for survivors.  Accounts differ on whether the boat actually returned to look for survivors, and if so, if any survivors were found.  During her lifetime, her friends called her \"Maggie\", but even by her death, obituaries referred to her as the \"Unsinkable Mrs. Brown\".  The reference was further reinforced by a 1960 Broadway musical based on her life and its 1964 film adaptation which were both entitled \"The Unsinkable Molly Brown\".\n\nDivine Lust: Divine Lust is a Broadway musical created by and featuring Damian Perkins and Glenda Benevides.\n\nMurder of Troy LaFerrara: Troy LaFerrara was a Port Trevorton, Pennsylvania man murdered on November 11, 2013.  Miranda Barbour and her husband, Elytte Barbour, were found guilty and sentenced to life in prison in September 2014.\n\nFort Knox (Maine): Fort Knox, now Fort Knox State Park or Fort Knox State Historic Site, is located on the western bank of the Penobscot River in the town of Prospect, Maine, about 5 mi from the mouth of the river.  Built between 1844 and 1869, it was the first fort in Maine built entirely of granite; most previous forts used wood, earth, and stone.  It is named after Major General Henry Knox, the first U.S. Secretary of War and Commander of Artillery during the American Revolutionary War, who at the end of his life lived not far away in Thomaston.  The fort was designated a National Historic Landmark in 1970, as a virtually intact example of a mid-19th century granite coastal fortification.  Fort Knox also serves as the entry site for the observation tower of the Penobscot Narrows Bridge that opened to the public on 19 May 2007.\n\nDaniel Wozniak (murderer): Daniel Patrick Wozniak (born March 23, 1984) is a former Southern California community theater actor and convicted double-murderer on California's Death Row.  In May 2010, Wozniak murdered two people as part of a plan to steal money from one of the victims.  The money was going to be used to pay for his upcoming wedding and honeymoon.  Wozniak murdered his neighbor and friend, PFC Samuel E. Herr, 26, an OEF Army Veteran of the 1-91 Airborne Cav, and Herr's college friend Juri \"Julie\" Kibuishi, 23.\n\nGraeme Burton: Graeme Burton is a New Zealander who murdered two people in two separate incidents fourteen years apart.  The second murder occurred six months after he was released on parole in 2006.  This led to increased public concern about the release of high risk offenders on parole and to internal reviews by the Probation Service and the New Zealand Parole Board of their decision-making and management processes.\n\nDoaksville, Choctaw Nation: Doaksville is a former settlement, now a ghost town, located in present-day Choctaw County, Oklahoma.  It was founded between 1824 and 1831, by people of the Choctaw Indian tribe who were forced to leave their homes in the Southeastern United States and relocate in an area designated in for their resettlement in Indian Territory.  The community was named for Joseph Doak, co-owner of the local trading post.  The town flourished until the U.S. Army abandoned nearby Fort Towson in 1854, though it remained as the Choctaw capital until 1859, then declined precipitately after being bypassed by a new railroad in 1870.  It is now a ghost town and an archaeological preservation site.\n\nHecla, Montana: Hecla was a town in Beaverhead County, Montana.  It has been designated as a ghost town with only a few ruined buildings remaining.  It was notable at one time as the home of Blanche Lamont, who taught at Hecla's one-room schoolhouse.  Lamont would become the first of two murder victims of Theodore Durrant.  Margaret Brown also lived there for a time.\n\nAkira Nishiguchi: Akira Nishiguchi (西口 彰 , \"Nishiguchi Akira\" , December 14, 1925 – December 11, 1970) was a Japanese serial killer and fraudster.  According to Abdul Haq Shafaq, Nishiguchi himself is most known for being able to confuse Japanese police into believing that he was only connected to fraud rather than the murders.  While engaging in confidence scams, he murdered two people, was put on the most wanted list, and killed three others while escaping.  The police also regretted that they didn't find Nishiguchi, who was found by an 11-year-old girl.  A prosecutor called him \"the Black Gold Medalist in history\".  Ryuzo Saki published a book about Nishiguchi, which became the basis for the film \"Vengeance Is Mine\".  His crimes were the direct catalyst for the creation of the Japanese \"Metropolitan Designated Case\" system\n\nGhost Town, Oakland, California: Ghost Town (sometimes spelled Ghosttown) is the informal name of the Foster Hoover Historic District neighborhood in West Oakland, Oakland, California.  The community is known for its violence and blight .  Some people believe the name originates from a drug king pin who referred to the area as a ghost town due to the shortage of other drug dealers whose absence was attributed to the king pin's dominance over the area.  Others believe it derives from the two former casket companies located side by side on Filbert Street between 30th and 32nd Streets, while others claim that the presence of ghostly white people in an historically black neighborhood gave it its name.  Ghost Town stretches from 27th Street to 35th Street in the area immediately southwest of the MacArthur Maze.  Others see the neighborhood bounded by Adeline on the West and San Pablo on the East.  Ghost Town Farms, one of the more successful expressions of urban agriculture activity in Oakland is located in the heart of the district at 2727 Martin Luther King Jr.  Way, between 27th and 28th Streets.  The area is also one of Oakland's many open-air art galleries, with exceptional muralist work continually on exhibition, particularly along Martin Luther King Jr.  Way.  This neighborhood has an active citizen crime patrol, including one group of seniors who walk the neighborhood weekly to get physical exercise and report blight.  Jerry Brown, governor of California and former Mayor of Oakland stated: \"Instead of an omnibus crime bill, you have to deal with shootings in Ghost Town in West Oakland and sideshows in East Oakland.\"  Brown made attempts to turn around the blighted West Oakland neighborhood after \"60 Minutes\" featured it in a television profile.  Housing prices have increased.  So has drug dealing, especially since nearby parks were closed by the City of Oakland.  Prostitution, in 2015, has been on the decline for at least a decade.\n\nQuestion: A woman who had a broadway musical created based on her life lived in a city now designated as a ghost town where what man murdered two people?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"woman_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the woman.\"\n        },\n        \"broadway_musical_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the Broadway musical based on her life.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"broadway_musical_title\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"ghost_town_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the ghost town where the woman lived.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the ghost town is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"murder_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"murderer_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the man who murdered two people.\"\n        },\n        \"victims_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of people murdered by this man.\"\n        },\n        \"victim_connections_to_town\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"victim_name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of a victim.\"\n              },\n              \"connection_to_town\": {\n                \"type\": \"string\",\n                \"description\": \"How the victim was connected to the ghost town.\"\n              }\n            },\n            \"required\": [\n              \"victim_name\",\n              \"connection_to_town\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"Details about the victims and their connection to the ghost town.\"\n        }\n      },\n      \"required\": [\n        \"murderer_name\",\n        \"victims_count\",\n        \"victim_connections_to_town\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"woman_details\",\n    \"ghost_town_details\",\n    \"murder_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "woman_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the woman."
          },
          "broadway_musical_title": {
            "type": "string",
            "description": "The title of the Broadway musical based on her life."
          }
        },
        "required": [
          "name",
          "broadway_musical_title"
        ],
        "additionalProperties": false
      },
      "ghost_town_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the ghost town where the woman lived."
          },
          "state": {
            "type": "string",
            "description": "The state where the ghost town is located."
          }
        },
        "required": [
          "name",
          "state"
        ],
        "additionalProperties": false
      },
      "murder_details": {
        "type": "object",
        "properties": {
          "murderer_name": {
            "type": "string",
            "description": "The name of the man who murdered two people."
          },
          "victims_count": {
            "type": "integer",
            "description": "The number of people murdered by this man."
          },
          "victim_connections_to_town": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "victim_name": {
                  "type": "string",
                  "description": "The name of a victim."
                },
                "connection_to_town": {
                  "type": "string",
                  "description": "How the victim was connected to the ghost town."
                }
              },
              "required": [
                "victim_name",
                "connection_to_town"
              ],
              "additionalProperties": false
            },
            "description": "Details about the victims and their connection to the ghost town."
          }
        },
        "required": [
          "murderer_name",
          "victims_count",
          "victim_connections_to_town"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "woman_details",
      "ghost_town_details",
      "murder_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
