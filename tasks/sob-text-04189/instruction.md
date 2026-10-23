{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHolman Stadium (Nashua): Holman Stadium is a baseball stadium in Nashua, New Hampshire.  It was constructed in 1937, as a multi-purpose stadium, by the City of Nashua.  The official seating capacity is 4,000 people.  Holman is currently the home of the Nashua Silver Knights of the Futures Collegiate Baseball League.\n\nWinnipeg Maroons: The Winnipeg Maroons were a minor League baseball team based in Winnipeg, Manitoba, United States, which played in the Northern League from 1902–1942.  Their home field from 1906 to 1922 was Happyland Park, which had a seating capacity of 4,000.  They subsequently played at Sherbourne Park, which had a seating capacity of 3,500.  One of the most successful teams in the league, they won league championships eight times (1902, 1903, 1907, 1912, 1916, 1935, 1939, 1942).\n\nPhilippine Sports Stadium: The Philippine Sports Stadium, also known as New Era University (NEU) Stadium, is a football and track stadium at Ciudad de Victoria, a 140-hectare tourism enterprise zone in the towns of Bocaue and Santa Maria in Bulacan, Philippines.  The stadium was built right next to the Philippine Arena, the world's largest indoor arena.  The stadium is the largest football stadium in the Philippines with a maximum seating capacity of 25,000.  Its seating capacity is more than twice the seating capacity of the Rizal Memorial Stadium, the national stadium of the country which has a seating capacity of 12,000.\n\nDoak Field: Doak Field (or The Doak) is a baseball venue in Raleigh, North Carolina, United States.  It opened in 1966 and is home to the North Carolina State University Wolfpack college baseball team of the NCAA's Division I Atlantic Coast Conference (ACC).  It is named for Charles Doak, who was the head coach of the NC State baseball team from 1924–1939.  The stadium is located on NC State's Central Campus, behind Lee and Sullivan residence halls.  The diamond is in the north/northwest corner of its block, which is bounded by Thurman Drive (third base, north/northeast); Dail Park and the residence halls (left field, east/southeast); Sullivan Drive (right field, south/southwest); and Varsity Drive (first base, west/northwest).  Its seating capacity is 2,500 spectators, with an overflow capacity of 3,000.  The largest crowd at Doak Field since its 2004 renovation was 3,109 on April 28, 2007, in a series finale between NC State and its rival UNC.  Doak Field hosted the Atlantic Coast Conference Baseball Tournament in both 1974 and in 1980.  NC State won the championship in 1974, while Clemson won in 1980.\n\nSeating capacity: Seating capacity is the number of people who can be seated in a specific space, in terms of both the physical space available, and limitations set by law.  Seating capacity can be used in the description of anything ranging from an automobile that seats two to a stadium that seats hundreds of thousands of people.  The largest sporting venue in the world, the Indianapolis Motor Speedway, has a permanent seating capacity for more than 235,000 people and infield seating that raises capacity to an approximate 400,000.\n\nNashua Silver Knights: The Nashua Silver Knights is a summer collegiate baseball team based in Nashua, New Hampshire.  It is a charter member of the Futures Collegiate Baseball League (FCBL), a wood-bat league with a 56-game regular season comprising 9 teams from New Hampshire to western Connecticut.  The team's home games are played at Holman Stadium in Nashua.  The team is owned by Drew Weber, who used to also own the Lowell Spinners, the Class A minor league affiliate of the Boston Red Sox.\n\nAlumni Stadium (Guelph): Alumni Stadium is a multi-purpose stadium at the University of Guelph in Guelph, Ontario, Canada.  It is home to the Guelph Gryphons varsity football team.  It was built in 1970, and has a fixed seating capacity of approximately 8,500, including fixed seating and the grass hill on the east side of the stadium.  On October 27, 2011, it was announced that the stadium would undergo an $18 million expansion and renovation that will bring fixed seating capacity up to 7,500.  It was also announced that an eight-lane track would be installed as well as synthetic turf for the field.\n\nKyle Field: Kyle Field is the football stadium located on the campus of Texas A&M University in College Station, Texas.  It has been the home to the Texas A&M Aggie football team in rudimentary form since 1904, and as a complete stadium since 1927.  It is known as the \"\"Home of the 12th Man\"\".  The seating capacity of 102,733 in 2015 makes the stadium the largest in the Southeastern Conference and the fourth largest stadium in the NCAA, fourth largest stadium in the United States, and the fifth largest non-racing stadium in the world.  Within the state of Texas, Kyle Field has the largest regular seating capacity, while AT&T Stadium has a larger overall capacity.\n\nEstadio Revolución: Estadio de la Revolución is a sports arena located near the downtown area of Torreón in Coahuila, Mexico.  It has a seating capacity of 12,000.  Though used mainly for baseball games, it sometimes hosts concerts and other non-sport events.  It is the home field of the Vaqueros Laguna baseball team.  Since it was originally constructed as a multi sport stadium and featured a running track the Estadio de la Revolución features the largest foul territory of any ball park within the Mexican League, the area of the former running track.  The stadium is named to commemorate the Mexican Revolution of 1910–1920, a political change that was still recent at the time of the venue's opening on 15 September 1932.  The stadium was renovated in the fall of 2002 to provide a refurbished appearance for the baseball team's reorganization, renaming, and new season starting in 2003.\n\nFirstEnergy Stadium: FirstEnergy Stadium, officially FirstEnergy Stadium, Home of the Cleveland Browns, is a multi-purpose stadium in Cleveland, Ohio, United States, primarily for American football.  It is the home field of the Cleveland Browns of the National Football League (NFL), and serves as a venue for other events such as college and high school football, soccer, and concerts.  It opened in 1999 as Cleveland Browns Stadium and was renovated in two phases in early 2014 and 2015.  The initial seating capacity was listed at 73,200 people, but following the first phase of the renovation project in 2014, seating capacity was reduced to 67,431.  Since 2017, capacity is listed at 67,895.  The stadium sits on 31 acre of land between Lake Erie and the Cleveland Memorial Shoreway in the North Coast Harbor area of downtown Cleveland, adjacent to the Great Lakes Science Center and Rock and Roll Hall of Fame.  The site was previously the location of Cleveland Stadium from 1931 to 1996.\n\nQuestion: What is the seating capacity of the stadium that is the home of the baseball team owned by Drew Weber?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"stadium_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the stadium.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The city and state/country where the stadium is located.\"\n        },\n        \"seating_capacity\": {\n          \"type\": \"integer\",\n          \"description\": \"The official seating capacity of the stadium.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\",\n        \"seating_capacity\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"home_team_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the baseball team.\"\n        },\n        \"owner\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the owner of the baseball team.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"owner\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer\": {\n      \"type\": \"integer\",\n      \"description\": \"The seating capacity of the stadium that is home to the specified team.\"\n    }\n  },\n  \"required\": [\n    \"stadium_details\",\n    \"home_team_details\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "stadium_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the stadium."
          },
          "location": {
            "type": "string",
            "description": "The city and state/country where the stadium is located."
          },
          "seating_capacity": {
            "type": "integer",
            "description": "The official seating capacity of the stadium."
          }
        },
        "required": [
          "name",
          "location",
          "seating_capacity"
        ],
        "additionalProperties": false
      },
      "home_team_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the baseball team."
          },
          "owner": {
            "type": "string",
            "description": "The name of the owner of the baseball team."
          }
        },
        "required": [
          "name",
          "owner"
        ],
        "additionalProperties": false
      },
      "final_answer": {
        "type": "integer",
        "description": "The seating capacity of the stadium that is home to the specified team."
      }
    },
    "required": [
      "stadium_details",
      "home_team_details",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
