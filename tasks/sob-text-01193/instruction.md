{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSouthaven, Mississippi: Southaven is a city in DeSoto County, Mississippi, United States.  It is a suburb of Memphis, Tennessee, and a principal city in the Memphis metropolitan area.  The 2010 census reported a population of 48,982, making Southaven the third largest city in Mississippi.  Southaven is traversed from north to south by the I-55/I-69 freeway.  The city's name derives from the fact that Southaven is located south of Whitehaven, a neighborhood in Memphis.\n\nLanders Center: The Landers Center is an 8,400-seat multi-purpose arena in Southaven, Mississippi.  It was built in 2000.  It is home to the Mississippi RiverKings, a team in the Southern Professional Hockey League.\n\nKobi Simmons: Kobi Simmons (born July 4, 1997) is an American professional basketball player for the Memphis Grizzlies of the National Basketball Association (NBA), on a two-way contract with the Grizzlies' NBA G League affiliate, the Memphis Hustle.  He played college basketball for the Arizona Wildcats.\n\nMemphis Sport: Memphis Sport is a sports and fitness magazine featuring articles on local and regional teams, players and events.  In addition, \"Memphis Sport\" focuses on health and fitness for an active lifestyle.  The magazine debuted in Memphis, Tennessee in July 2006.  Local franchises covered include the University of Memphis Tigers, Memphis Redbirds, Mississippi Riverkings and Tennessee Titans.\n\nVince Hunter: Vincent Shamar Hunter (born August 5, 1994) is an American professional basketball player for the Memphis Grizzlies of the National Basketball Association (NBA) on a two-way contract with the Grizzlies' NBA G League affiliate, the Memphis Hustle.  He played college basketball for UTEP.\n\nHumphrey Coliseum: Humphrey Coliseum is a 10,575-seat multi-purpose arena located on the campus of Mississippi State University, just outside of Starkville, Mississippi, that opened for the 1975-76 basketball season.  Nicknamed The Hump, it is home to the Mississippi State Bulldogs men's and women's basketball teams.  It is the largest on-campus basketball arena in the state of Mississippi.  The building is the equivalent of seven stories high and is in the shape of an oval 318' long by 268' wide.  The outside is marked by regular concrete columns and Mississippi red brick siding, and the school seal adorns the front of the building.  In 2004, a center hung scoreboard was provided by the Henry Mize Foundation.  The scoreboard features four sides, each with a video screen.  In addition to basketball, the arena is a popular venue for concerts, graduation ceremonies, and other events.\n\nMemphis Hustle: The Memphis Hustle are an American professional basketball team of the NBA G League announced to begin play for the 2017–18 season as an affiliate of the Memphis Grizzlies of the National Basketball Association (NBA).  Based in the Memphis suburb of Southaven, Mississippi, the team will play their home games at the Landers Center.\n\nTanger Outlets Southaven (Memphis): Tanger Outlets Southaven is an outlet mall in Southaven, Mississippi, just outside Memphis, Tennessee.  The mall, located at the intersection of I-55/I-69 and Church Road, began construction in January 2015 and opened in November 2015.  Tanger Outlets Southaven is the first outlet mall in the Memphis metro area.\n\n2010–11 Mississippi RiverKings season: The 2010–11 Mississippi RiverKings season was the 19th season of the Central Hockey League (CHL) franchise in Southaven, Mississippi.\n\nMississippi RiverKings: The Mississippi RiverKings are a professional minor league ice hockey team.  The RiverKings are a member of the Southern Professional Hockey League, playing their first nineteen seasons from the 1992–93 season to the 2010–11 season in the Central Hockey League.  In July 2007, after 15 seasons as the Memphis RiverKings, the name was changed to Mississippi RiverKings.  The RiverKings are the oldest continuously operating professional sports franchise in the Memphis Metropolitan Area.\n\nQuestion: What multi-purpose arena in Southaven, Mississippi is the home of the Memphis Hustle and the Mississippi RiverKings?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"arena_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the multi-purpose arena.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the arena is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the arena is located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"capacity_seats\": {\n      \"type\": \"integer\",\n      \"description\": \"The seating capacity of the arena.\"\n    },\n    \"built_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the arena was built.\"\n    },\n    \"hosted_teams\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professional sports teams that call this arena home.\"\n    }\n  },\n  \"required\": [\n    \"arena_name\",\n    \"location\",\n    \"capacity_seats\",\n    \"built_year\",\n    \"hosted_teams\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "arena_name": {
        "type": "string",
        "description": "The name of the multi-purpose arena."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the arena is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the arena is located."
          }
        },
        "required": [
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "capacity_seats": {
        "type": "integer",
        "description": "The seating capacity of the arena."
      },
      "built_year": {
        "type": "integer",
        "description": "The year the arena was built."
      },
      "hosted_teams": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professional sports teams that call this arena home."
      }
    },
    "required": [
      "arena_name",
      "location",
      "capacity_seats",
      "built_year",
      "hosted_teams"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
