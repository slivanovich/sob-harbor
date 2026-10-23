{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIn the Basement (film): In the Basement (\"Im Keller\") is a 2014 Austrian documentary film directed by Ulrich Seidl about people and their obsessions, and what they do in their basements in their free time.  It was part of the Out of Competition section at the 71st Venice International Film Festival.\n\nPittsburgh toilet: A Pittsburgh toilet, often called a \"Pittsburgh potty\", is a common fixture in pre-World War II houses built in Pittsburgh, Pennsylvania, United States.  It consists of an ordinary flush toilet installed in the basement, with no surrounding walls.  As Pittsburgh was historically an industrial town, still called \"The Steel City,\" toilets such as these could be used by steelworkers and miners: grimy from the day's labor, they could use an exterior door to enter the basement directly from outside and use the basement's shower and toilet before heading upstairs.  Most of these toilets are paired with a crude basement shower apparatus and large sink, which often doubles as a laundry basin.  Also, because western Pennsylvania is a steep topographical zone, many basements have their own entryway, allowing homeowners to enter from their yard or garage, cleanse themselves promptly in their basement, and then ascend their basement stairs refreshed.\n\nLizard Lounge: The Lizard Lounge is a nightclub situated in between Harvard Square and Porter Square on Massachusetts Avenue in Cambridge, Massachusetts.  It is below the restaurant Cambridge Common.  It may be a small basement bar, but it is known for the musicians it hosts.  The owners also own Cambridge Common, West Side Lounge, and Toad – another live music venue.  They carry a large selection of beers, including many local ones such as those made at Cambridge Brewing Company.\n\nFirst White Terror: The White Terror was a period during the French Revolution in 1795, when a wave of violent attacks swept across much of France.  The victims of this violence were people identified as being associated with the Reign of Terror - followers of Robespierre and Marat, and members of local Jacobin clubs.  The violence was perpetrated primarily by those whose relatives or associates had been victims of the Great Terror, or whose lives and livelihoods had been threatened by the government and its supporters before the Thermidorean Reaction.  Principally these were, in Paris, the Muscadins, and in the countryside, monarchists, supporters of the Girondins, those who opposed the Civil Constitution of the Clergy and those otherwise hostile to the Jacobin political agenda.  The Great Terror had been largely an organised political programme, based on laws such as the Law of 22 Prairial, and enacted through official institutions such as the Revolutionary Tribunal, but the White Terror was essentially a series of unco-ordinated attacks by local activists who shared common perspectives but no central organisation.  In particular locations, there were however more organised counter-revolutionary movements such as the Companions of Jehu in Lyon and the Companions of the Sun in Provence.  The name 'White Terror' derives from the white cockades worn in the hats of royalists.\n\nBasement apartment: A basement apartment is an apartment located below street level, underneath another structure—usually an apartment building, but possibly a house or a business.  Rent in basement apartments is usually much lower than it is in above-ground units, due to a number of deficiencies common to basement apartments.  The apartments are usually cramped, and tend to be noisy, both from uninsulated building noises and from traffic on the adjacent street.  They are also particularly vulnerable to burglary, especially those with windows at sidewalk level.  In some instances, residential use of below-ground space is illegal, but is done anyway in order for the building owner to generate extra income.\n\n(T)error: (T)ERROR is an American 2015 documentary film directed by Lyric R. Cabral and David Felix Sutcliffe.  The film follows undercover FBI informant Saeed \"Shariff\" Torres as he engages in a sting operation targeting a white Muslim man named Khalifah Ali Al-Akili.  The film won the Special Jury Award for Breakout First Feature at the 2015 Sundance Film Festival, where it premiered.\n\nThick-skinned deformation: Thick-skinned deformation is a geological term which refers to crustal shortening that involves basement rocks and deep-seated faults as opposed to only the upper units of cover rocks above the basement which is known as thin-skinned deformation.  While thin-skinned deformation is common in many different localities, thick-skinned deformation requires much more strain to occur and is a rarer type of deformation.\n\nThin basement membrane disease: Thin basement membrane disease (TBMD, also known as \"benign familial hematuria\" and \"thin basement membrane nephropathy\") is, along with IgA nephropathy, the most common cause of asymptomatic hematuria.  The only abnormal finding in this disease is a thinning of the basement membrane of the glomeruli in the kidneys.  Its importance lies in the fact that it has a benign prognosis, with patients maintaining a normal kidney function throughout their lives.\n\nPolitz Day School: Politz Day School is a private Modern Orthodox Jewish day school in Cherry Hill, New Jersey.  Established in 1968, the school was originally operated exclusively as a preschool, located in the basement of Congregation Sons of Israel.  Politz serves students in Southern New Jersey, as well as those from Delaware and the Philadelphia area.  The school serves students from preschool (for children as young as two) through eighth grade, giving students the chance to learn in an environment that combines the abundance of the Jewish religion with a traditional secular education.  The school shares a common facility with Congregation Sons of Israel.\n\nRecreation room: A recreation room (also known as a rec room, rumpus room, or ruckus room) is a room used for a variety of purposes, such as parties, games and other everyday or casual use.  The term is common in the United States, Australia, New Zealand and Canada, but is less common in the United Kingdom where the preferred term is games room.  Often children and teenagers entertain their friends in the rec room, which is often located in the basement, away from the main living areas of the house.  Usually it is a larger space than a living room to have the ability to serve multiple purposes and entertain moderately large groups.\n\nQuestion: What do Terror and In the Basement have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_one_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\"\n        },\n        \"director\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"country_of_origin\",\n        \"director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_two_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\"\n        },\n        \"director\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"country_of_origin\",\n        \"director\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"shared_category\": {\n      \"type\": \"string\",\n      \"description\": \"The common category or genre shared by both films.\"\n    }\n  },\n  \"required\": [\n    \"film_one_details\",\n    \"film_two_details\",\n    \"shared_category\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_one_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "country_of_origin": {
            "type": "string"
          },
          "director": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "release_year",
          "country_of_origin",
          "director"
        ],
        "additionalProperties": false
      },
      "film_two_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "country_of_origin": {
            "type": "string"
          },
          "director": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "release_year",
          "country_of_origin",
          "director"
        ],
        "additionalProperties": false
      },
      "shared_category": {
        "type": "string",
        "description": "The common category or genre shared by both films."
      }
    },
    "required": [
      "film_one_details",
      "film_two_details",
      "shared_category"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
