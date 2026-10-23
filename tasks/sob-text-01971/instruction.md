{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSam Adams (Oregon politician): Samuel Francis \"Sam\" Adams (born September 3, 1963) is an American politician who is the former mayor of Portland, Oregon.  He grew up in Newport, Oregon, attended the University of Oregon and worked on a number of campaigns before taking office as a Portland commissioner.  Among them was Vera Katz's run for mayor of Portland.  After she won, he served as her chief of staff for eleven years and then went back to school, earning a degree in Political Science.\n\nEthan Strimling: Ethan King Strimling (born October 19, 1967) is the mayor of Portland, Maine, who served as a Democratic state senator from 2002 to 2009.  He was replaced by Justin Alfond.  He is Executive Director of LearningWorks, a West End non-profit organization, and has served as a political columnist and commentator for the Portland Press Herald.\n\nTBC (band): TBC (styled as tbc), are a Christian girl band who were launched by Innervation Trust in 2004, as a \"flagship\" girl band alongside their brother band Thebandwithnoname.  Innervation Trust is a Christian charity that exists to recruit and resource schools teams, dubbed \"Collectives\", each dedicated to a major city in the UK.  Innervation Trust is the product of Mark Pennells and Zarc Porter, a songwriter/producer partnership also credited with writing most of the music for, and co-founding, the World Wide Message Tribe.  After 7 years of promoting the Collective bands throughout every region of the UK, they were replaced by the primary school project, Pop Connection.  This has since been replaced by iSingPOP.  iSingPOP works in primary schools and will spend a week teaching all the children a number of songs (usually 7) as a choir and the next week will perform these songs in their local church or activity hall/centre with an audience.  They also have a recording day to make their very own album.\n\n7 Years and 50 Days (song): \"7 Years and 50 Days\" is the third single and title track from the album \"7 Years and 50 Days\" by German trance group Groove Coverage.\n\nAttempted Rape Act 1948: The Attempted Rape Act 1948 (11&12 Geo.  6 c. 19) was an Act of the Parliament of the United Kingdom that increased the maximum sentence for attempted rape from 2 years imprisonment to 7 years penal servitude.  (Penal servitude was abolished later that year by the Criminal Justice Act 1948, and replaced with imprisonment.)  The Attempted Rape Act was repealed and replaced by the Sexual Offences Act 1956, which maintained the maximum sentence of 7 years imprisonment until the 1956 Act was amended by the Sexual Offences Act 1985, which increased the maximum sentence to life imprisonment.\n\nGreat Getaway Game: The Great Getaway Game is a game show which aired on The Travel Channel from June 1, 1990 to April 1991, producing 39 episodes.  This was, to date, the network's sole attempt at a game show.  Its pilot was hosted by Jim Caldwell, but Wink Martindale took over as host for the actual series, in addition to producing it (coincidentally, Jim had replaced Wink after 7 years as the host of on \"Tic-Tac-Dough\").\n\nHoward Packett: Howard C. Packett is a former mayor of Salem, Virginia.  Under Salem's electoral system, the mayor is a member of the city council selected by the other members to serve as mayor.  Packett was elected to his final term on the city council in May 2004, and served that term until 2008.  Packett served on the council for 24 years.  Packett became mayor in 2006 when former mayor Carl Tarpley decided not to seek another term.  Randy Foley replaced Packett as mayor in 2008.\n\nCedar Avenue (band): Cedar Avenue is an American pop rock band from Minneapolis, Minnesota.  The band was formed in 2005 by lead vocalist Jesse Mathews and bassist Kyle Wachter.  Their song \"7 Years\" was featured in the season finale of the ABC / Global TV (Canada) series Rookie Blue.  \"7 Years\" was also featured on the Cities 97 Sampler Vol.  22.\n\nJustin Alfond: Justin Loring Alfond (born January 8, 1975) is an American politician and real estate developer.  He is a Democratic State Senator from the 8th District, which represents much of Portland.  Alfond was first elected to the State Senate in 2008 to replace Democrat Ethan Strimling; he beat former State Senator Anne Rand and Cliff Ginn.  He was re-elected in 2010 and 2012.  In 2012, he faced Green Independent Party Chair Asher Platts.  Alfond won with 71% of the vote in a two-way race.\n\nPortland, Maine mayoral election, 2011: The 2011 Portland, Maine mayoral election took place on November 8, 2011.  In November 2010, Portland voters approved a citywide referendum changing the city charter to recreate an elected mayor position that had previously been removed in 1923.  From 1923 until 2011, city councilors chose one of themselves each year to serve as mayor, a primarily ceremonial position.  On November 8, 2011, former State Senator and candidate for U.S. Congress Michael F. Brennan was elected.  On December 5, 2011, he was sworn in as the first citizen-elected mayor in 88 years.\n\nQuestion: Who was Portland, ME mayor for 7 years and was replaced by Justin Alfond?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person identified as the subject of the question.\"\n    },\n    \"mayoral_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_current_mayor\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the person is currently serving as mayor according to the context.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city for which the person is mayor.\"\n        }\n      },\n      \"required\": [\n        \"is_current_mayor\",\n        \"city\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"related_political_roles\": {\n      \"type\": \"array\",\n      \"description\": \"A list of other political roles held by the person, including details about their term and replacement.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"role_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of political role (e.g., 'state senator').\"\n          },\n          \"term_duration_years\": {\n            \"type\": \"integer\",\n            \"description\": \"The duration of the term in years.\"\n          },\n          \"term_start_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The start year of the term.\"\n          },\n          \"term_end_year\": {\n            \"type\": \"integer\",\n            \"description\": \"The end year of the term.\"\n          },\n          \"replaced_by\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the person who replaced them in this specific role.\"\n          },\n          \"replaced_in_role_type\": {\n            \"type\": \"string\",\n            \"description\": \"The specific role in which the replacement occurred.\"\n          }\n        },\n        \"required\": [\n          \"role_type\",\n          \"term_duration_years\",\n          \"term_start_year\",\n          \"term_end_year\",\n          \"replaced_by\",\n          \"replaced_in_role_type\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"mayoral_information\",\n    \"related_political_roles\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person identified as the subject of the question."
      },
      "mayoral_information": {
        "type": "object",
        "properties": {
          "is_current_mayor": {
            "type": "boolean",
            "description": "Indicates if the person is currently serving as mayor according to the context."
          },
          "city": {
            "type": "string",
            "description": "The city for which the person is mayor."
          }
        },
        "required": [
          "is_current_mayor",
          "city"
        ],
        "additionalProperties": false
      },
      "related_political_roles": {
        "type": "array",
        "description": "A list of other political roles held by the person, including details about their term and replacement.",
        "items": {
          "type": "object",
          "properties": {
            "role_type": {
              "type": "string",
              "description": "The type of political role (e.g., 'state senator')."
            },
            "term_duration_years": {
              "type": "integer",
              "description": "The duration of the term in years."
            },
            "term_start_year": {
              "type": "integer",
              "description": "The start year of the term."
            },
            "term_end_year": {
              "type": "integer",
              "description": "The end year of the term."
            },
            "replaced_by": {
              "type": "string",
              "description": "The name of the person who replaced them in this specific role."
            },
            "replaced_in_role_type": {
              "type": "string",
              "description": "The specific role in which the replacement occurred."
            }
          },
          "required": [
            "role_type",
            "term_duration_years",
            "term_start_year",
            "term_end_year",
            "replaced_by",
            "replaced_in_role_type"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "person_name",
      "mayoral_information",
      "related_political_roles"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
