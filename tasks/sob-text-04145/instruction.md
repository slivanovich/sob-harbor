{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMissouri Pacific Railroad: The Missouri Pacific Railroad (reporting mark MP) , commonly abbreviated MoPac, with nickname of The Mop, was one of the first railroads in the United States west of the Mississippi River.  MoPac was a Class I railroad growing from dozens of predecessors and mergers, including the St. Louis, Iron Mountain and Southern Railway (SLIMS), Texas and Pacific Railway (TP), Chicago and Eastern Illinois Railroad (C&EI), St. Louis, Brownsville and Mexico Railway (SLBM), Kansas, Oklahoma and Gulf Railway (KO&G), Midland Valley Railroad (MV), San Antonio, Uvalde and Gulf Railroad (SAU&G), Gulf Coast Lines (GC), International-Great Northern Railroad (IGN), New Orleans, Texas and Mexico Railway (NOTM), Missouri-Illinois Railroad (MI), as well as the small Central Branch Railway (an early predecessor of MP in Kansas and south central Nebraska), and joint ventures such as the Alton and Southern Railroad (AS).\n\nRay Point, Texas: Ray Point is a small rural unincorporated community in Live Oak County, Texas, United States.  It is a German farming community typical for much of Texas.  The most prominent remaining structures are the Ray Point community center and the Ray Point Mercantile (closed).  Nearby is the Ray Point cemetery.  The nearest city is Three Rivers.\n\nUnion Pacific Railroad: The Union Pacific Railroad (or Union Pacific Railroad Company and simply Union Pacific) is a freight hauling railroad that operates 8,500 locomotives over 32,100 route-miles in 23 states west of Chicago and New Orleans.  The Union Pacific Railroad system is the largest in the United States and it is one of the world's largest transportation companies.  The Union Pacific Railroad is the principal operating company of the Union Pacific Corporation (); both are headquartered in Omaha, Nebraska.\n\nLebanon, Texas: Lebanon was the name of two different communities that were founded in Texas in the 19th Century, neither of which exists today.  The first was a town located in Collin County that had a post office designated as Lebanon, Texas, before it was relocated to Frisco, Texas.  The second was a smaller unincorporated community located in Live Oak County of which only a cemetery remains today.\n\nOrleans Cross Roads, West Virginia: Orleans Cross Roads is an unincorporated community hamlet that lies on the western flanks of Sideling Hill on the Potomac River in Morgan County, West Virginia.  To its south, Rockwell Run, a mountain stream fed by springs, empties into the Potomac.  Orleans Cross Roads lies along the old Baltimore and Ohio Railroad directly across the river from Little Orleans.  It is accessible by way of Orleans Road (CR 18/1) from Cacapon Road (West Virginia Route 9) via Detour Road (CR 18).\n\nGeorge West, Texas: George West is a city in Live Oak County, Texas, United States, and named for cattle rancher George Washington West.  The population was 2,524 at the 2000 census.  It is the county seat of Live Oak County.  George West was named the \"storytelling capital of Texas\" in 2005 by the Texas Senate; and it hosts the \"George West Storyfest\", a festival that features storytelling, cowboy poetry, and music.  Numerous ranches surround George West.\n\nDinero, Texas: Dinero is an unincorporated community in eastern Live Oak County, Texas, United States.  It lies along local roads south of Interstate 37, southeast of the city of George West, the county seat of Live Oak County.  Its elevation is 112 feet (34 m).  Though there used to be a post office, it was shut down in 2008 and the 78350 zip code was removed.\n\nWhitsett, Texas: Whitsett is an unincorporated community in northwestern Live Oak County, Texas, United States.  It lies at the intersection of U.S. Route 281 and FM 99, along the Union Pacific Railroad and fifteen miles north of Three Rivers.  Whitsett is best known as being the setting for the 2008 horror film \"The Wild Man of the Navidad\".\n\nOakville, Texas: Oakville is an unincorporated community in northeastern Live Oak County, Texas, United States.  It lies along Interstate 37 northeast of the city of George West, the county seat of Live Oak County.  Its elevation is 171 feet (52 m).  Although Oakville is unincorporated, it has a post office, with the ZIP code of 78060.\n\nSwinney Switch, Texas: Swinney Switch, also known as Swinney, is an unincorporated community in southeastern Live Oak County, Texas, United States.  It lies approximately 12 mi southeast of the city of George West, the county seat of Live Oak County, at the intersection of FM 534 and FM 3024 near Interstate 37.  Its elevation is 210 ft .\n\nQuestion: What freight hauling railroad that operates 8,500 locomotives over 32,100 route-miles in 23 states west of Chicago and New Orleans, has an unincorporated community in northwestern Live Oak County, Texas, United States that lies along it?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"railroad_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the freight hauling railroad.\"\n    },\n    \"operational_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"locomotive_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of locomotives operated by the railroad.\"\n        },\n        \"route_miles\": {\n          \"type\": \"integer\",\n          \"description\": \"The total route-miles operated by the railroad.\"\n        },\n        \"states_operated_in_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of states the railroad operates in.\"\n        }\n      },\n      \"required\": [\n        \"locomotive_count\",\n        \"route_miles\",\n        \"states_operated_in_count\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"associated_community\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"community_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the unincorporated community.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the community is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the community is located.\"\n        },\n        \"location_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the community's location relative to the railroad.\"\n        }\n      },\n      \"required\": [\n        \"community_name\",\n        \"county\",\n        \"state\",\n        \"location_description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"railroad_name\",\n    \"operational_details\",\n    \"associated_community\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "railroad_name": {
        "type": "string",
        "description": "The name of the freight hauling railroad."
      },
      "operational_details": {
        "type": "object",
        "properties": {
          "locomotive_count": {
            "type": "integer",
            "description": "The number of locomotives operated by the railroad."
          },
          "route_miles": {
            "type": "integer",
            "description": "The total route-miles operated by the railroad."
          },
          "states_operated_in_count": {
            "type": "integer",
            "description": "The number of states the railroad operates in."
          }
        },
        "required": [
          "locomotive_count",
          "route_miles",
          "states_operated_in_count"
        ],
        "additionalProperties": false
      },
      "associated_community": {
        "type": "object",
        "properties": {
          "community_name": {
            "type": "string",
            "description": "The name of the unincorporated community."
          },
          "county": {
            "type": "string",
            "description": "The county where the community is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the community is located."
          },
          "location_description": {
            "type": "string",
            "description": "A description of the community's location relative to the railroad."
          }
        },
        "required": [
          "community_name",
          "county",
          "state",
          "location_description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "railroad_name",
      "operational_details",
      "associated_community"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
