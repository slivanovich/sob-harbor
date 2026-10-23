{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSeaStreak: SeaStreak is a private ferry company operating in the Port of New York and New Jersey and in New England.  It provides high-speed commuter service between points on the Raritan Bayshore in Monmouth County, New Jersey and in Manhattan in New York City as well as special event and sightseeing excursions in the harbor and seasonal service to the New England coast.\n\nEast Brunswick, New Jersey: East Brunswick is a township in Middlesex County, New Jersey, United States.  The suburban community is part of the New York City metropolitan area and is located on the southern shore of the Raritan River, directly adjacent to the city of New Brunswick.  According to the 2010 United States Census, the township's population was 47,512, reflecting an increase of 756 (+1.6%) from the 46,756 counted in the 2000 Census, which had in turn increased by 3,208 (+7.4%) from the 43,548 counted in the 1990 Census.\n\nRaritan Bay: Raritan Bay is a bay located at the southern portion of Lower New York Bay between the U.S. states of New York and New Jersey and is part of the New York Bight.  The bay is bounded on the northwest by New York's Staten Island, on the west by Perth Amboy, New Jersey, on the south by the Raritan Bayshore communities of Monmouth County, New Jersey, and on the east by Sandy Hook Bay.  The bay is named after the Raritans, a branch of the Lenape tribe who lived in the vicinity of the bay for thousands of years prior to the arrival of Dutch colonists in the 17th century.\n\nEdison, New Jersey: Edison is a township in Middlesex County, New Jersey, United States, in the New York City metropolitan area, and the Raritan Bayshore subregion of the Jersey Shore.  As of the 2010 United States Census, Edison had a total population of 99,967, retaining its position as the fifth-most populous municipality in New Jersey.  The 2010 population reflected an increase of 2,280 (+2.3%) from the 97,687 counted in the 2000 Census, which had in turn increased by 9,007 (+10.2%) from the 88,680 counted in 1990.  Edison's population has been above the 100,000 threshold since 2010, increasing by 2.7% to a Census-estimated 102,701 in 2015.\n\nKam Man Food: Kam Man Food (; abbreviated KM Food) is a Chinese supermarket chain with its corporate headquarters in Edison, New Jersey in the New York City metropolitan area.\n\nChinese Americans in New York City: The New York metropolitan area is home to the largest ethnic Chinese population outside of Asia, constituting the largest metropolitan Asian American group in the United States and the largest Asian-national metropolitan diaspora in the Western Hemisphere.  This population enumerates an estimated 812,410 uniracial individuals as of 2015, including at least 12 Chinatowns in the metropolitan area.  Six Chinatowns (or nine, including the emerging Chinatowns in Corona and Whitestone, Queens, and East Harlem, Manhattan) are located in New York City proper, and one each is located in Nassau County, Long Island; Edison, New Jersey; and Parsippany-Troy Hills, New Jersey.  This excludes fledgling ethnic Chinese enclaves emerging throughout the New York metropolitan area, such as Jersey City, New Jersey; China City of America in Sullivan County, New York; and \"Dragon Springs\" in Deerpark, Orange County, New York.  The Chinese American community in the New York metropolitan area is rising rapidly in population as well as economic and political influence.\n\nRaritan Bayshore: The Raritan Bayshore region of New Jersey is a subregion of the larger Jersey Shore.  It is the area around Raritan Bay from The Brunswicks to Sandy Hook, in Monmouth and Middlesex counties, including the towns of New Brunswick, home of Rutgers University, Edison, Perth Amboy, Keyport, \"Pearl of the Bayshore\", Keansburg, and Highlands, New Jersey.  It is the northernmost part of the Jersey Shore, located just south of New York City.  At Keansburg is a traditional amusement park while at Sandy Hook are found ocean beaches.  The Sadowski Parkway beach area in Perth Amboy, which lies at the mouth of the Raritan River, was deemed the \"Riviera of New Jersey\" by local government.  In the last years many of the beaches on the Bayshore area have been rediscovered and upgraded as the quality of the water continues to improve.\n\nU.S. Route 9 in New Jersey: U.S. Route 9 (US 9) is a U.S. highway in the northeast United States, running from Laurel, Delaware north to Champlain, New York.  In New Jersey, the route runs 166.80 mi from the Cape May–Lewes Ferry terminal in North Cape May, Cape May County, where the ferry carries US 9 across the Delaware Bay to Lewes, Delaware, north to the George Washington Bridge in Fort Lee, Bergen County, where the route along with Interstate 95 (I-95) and US 1 continue into New York City.  US 9 is the longest U.S. highway in the state.  From North Cape May north to Toms River in Ocean County, US 9 is mostly a two-lane undivided road that closely parallels the Garden State Parkway and runs near the Jersey Shore.  Along this stretch, it passes through the communities of Rio Grande, Cape May Court House, Somers Point, Pleasantville, Absecon, Tuckerton, Manahawkin, and Beachwood.  In the Toms River area, US 9 runs along the Garden State Parkway for a short distance before heading northwest away from it and the Jersey Shore into Lakewood Township.  Upon entering Monmouth County, the route transitions into a multilane suburban divided highway and continues through Howell Township, Freehold Township, Manalapan Township, Marlboro Township, Old Bridge Township, Sayreville, and South Amboy.  In Woodbridge Township, US 9 merges with US 1 and the two routes continue through northern New Jersey as US 1/9 to the George Washington Bridge.\n\nInterstate 287: Interstate 287 (I-287) is an auxiliary Interstate Highway in the US states of New Jersey and New York.  It is a partial beltway around New York City, serving the northern half of New Jersey and the counties of Rockland and Westchester in New York.  I-287, which is signed north–south in New Jersey and east–west in New York, follows a roughly horseshoe-shaped route from the New Jersey Turnpike (I-95) in Edison Township, New Jersey, clockwise to the New England Thruway (I-95) in Rye, New York, for 98.72 mi .  Through New Jersey, I-287 runs west from its southern terminus in Edison through suburban areas.  In Bridgewater Township, the freeway takes a more northeasterly course, paralleled by U.S. Route 202 (US 202).  The northernmost part of I-287 in New Jersey passes through mountainous surroundings.  After crossing into New York at Suffern, I-287 turns east on the New York State Thruway (I-87) and runs though Rockland County.  After crossing the Hudson River on the Tappan Zee Bridge, I-287 splits from I-87 near Tarrytown and continues east through Westchester County on the Cross-Westchester Expressway until it reaches the New England Thruway.\n\nGlen Burtnik: Glen Burtnik (born Glenn Burtnick, April 8, 1955) is a singer, songwriter, entertainer and multi-instrumentalist, best known as a former member of Styx.  Burtnik is originally from North Brunswick, New Jersey, in the Middlesex County part of the Raritan Bayshore and currently lives in Asbury Park, New Jersey, both popular Jersey Shore towns.  Burtnik has written hit songs for Randy Travis, Patty Smyth and Don Henley.  The spelling of his name has shortened a few times over the years (born Glenn Burtnick, then changed to Glen Burtnick, and finally Glen Burtnik, spelled with one N, no C).\n\nQuestion: Kam Man Food (abbreviated KM Food) is a Chinese supermarket chain with its corporate headquarters in Edison, a township in which county in New Jersey, United States, in the New York City metropolitan area, and the Raritan Bayshore subregion of the Jersey Shore?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity being described.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the entity (e.g., township, city).\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the entity is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the entity is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the entity is located.\"\n        }\n      },\n      \"required\": [\n        \"county\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"related_businesses\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"business_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of a business headquartered in this entity.\"\n          },\n          \"business_type\": {\n            \"type\": \"string\",\n            \"description\": \"The type of business.\"\n          }\n        },\n        \"required\": [\n          \"business_name\",\n          \"business_type\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"A list of businesses headquartered in the specified entity.\"\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"entity_type\",\n    \"location_details\",\n    \"related_businesses\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the entity being described."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of the entity (e.g., township, city)."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "county": {
            "type": "string",
            "description": "The county where the entity is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the entity is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the entity is located."
          }
        },
        "required": [
          "county",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "related_businesses": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "business_name": {
              "type": "string",
              "description": "The name of a business headquartered in this entity."
            },
            "business_type": {
              "type": "string",
              "description": "The type of business."
            }
          },
          "required": [
            "business_name",
            "business_type"
          ],
          "additionalProperties": false
        },
        "description": "A list of businesses headquartered in the specified entity."
      }
    },
    "required": [
      "entity_name",
      "entity_type",
      "location_details",
      "related_businesses"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
