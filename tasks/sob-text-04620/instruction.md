{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOhio State Route 203: State Route 203 (SR 203, OH 203) is a 22.14 mi long north–south state highway in the central portion of the U.S. state of Ohio.  The southern terminus of SR 203 is at a four-way stop intersection with SR 37 just 0.50 mi northwest of the city limits of Delaware.  Its northern terminus is at SR 309 approximately 4 mi northwest of Marion.\n\nPolk County, Florida: Polk County is located in the State of Florida.  The county population was 602,095, as of the 2010 census.  Its county seat is Bartow, and its largest city is Lakeland.\n\nOhio State Route 294: State Route 294 (SR 294) is a 24.23 mi long east–west state highway in the northwestern quadrant of the U.S. state of Ohio.  The route's western terminus is at SR 37 nearly 3.25 mi northwest of the village of Marseilles.  Its eastern terminus is at its junction with SR 98 about 4.75 mi south of the city of Bucyrus.\n\nOhio State Route 521: State Route 521 (SR 521) is an east–west state highway in central Ohio.  Existing entirely within Delaware County, the western terminus of SR 521 is at SR 37 in Delaware.  Its eastern terminus is at SR 656 in the hamlet of Olive Green, located approximately 5 mi north of Sunbury.\n\nFlorida State Road 37: State Road 37 (SR 37) is a state highway which runs from SR 62 at Duette, Florida north to Lakeland.  The road primarily runs through Polk County, with small sections in Hillsborough and Manatee counties.  The road is signed as Church Avenue in Mulberry and South Florida Avenue in Lakeland.\n\nCalifornia State Route 37: State Route 37 (SR 37) is a state highway in the northern part of California that runs 21 miles (34 km) along the northern shore of San Pablo Bay.  It is built from U.S. Route 101 in Novato and runs through the southern tip of Sonoma and Solano Counties to Interstate 80 in Vallejo not through Napa County, on 37 the county line sign says Sonoma on one side of the highway and Solano on the other side.  It serves as a vital connection between the four counties of the North Bay Area, north of San Francisco; Sonoma Raceway and Six Flags Discovery Kingdom are accessible from Route 37.\n\nIndiana State Road 44: Indiana State Road 44 (SR 44) in the State of Indiana begins in the west at State Road 37 (SR 37) in Martinsville and runs eastward to the Ohio state line in Union County in two broken sections.  It is broken in Franklin from Indiana State Road 144 and Interstate 65.\n\nIndiana State Road 128: State Road 128 (SR 128) is a state road in the central part of the U.S. state of Indiana.  Running for about 10.865 mi in a general east–west direction, connecting Frankton and rural Madison County.  The western terminus is at a junction with SR 13 and SR 37, south of Elwood.  The eastern terminus is at an intersection with SR 9, south of Alexandria.  The highway passes through mostly agricultural and residential properties, as a two-lane roadway.  SR 128 was originally introduced in the late 1930s or early 1940s routed along its modern routing.  The entire roadway was paved in the late 1960s.\n\nFrank O'Bannon Highway: The Frank O'Bannon Highway is a series of highways in the state of Indiana.  The highway follows existing segments, from south to north, of State Road 37 (SR 37} from Tell City to Eckerty, SR 64 at Eckerty, SR 145 from Eckerty to French Lick, SR 56 from French Lick to Prospect, U.S. Route 150 (US 150, concurrent with SR 56) from Prospect to Paoli, and SR 37 once again from Paoli to Bedford.  With the exception of the four-lane Mitchell-to-Bedford segment (SR 37), the majority of the highway is two lanes.\n\nAlabama State Route 37: State Route 37 (SR 37) is a 0.768 mi state highway in Dale County in the southeastern part of the U.S. state of Alabama.  The southern terminus of the highway is at an intersection with US 84/SR 134 at Daleville and leads to the Tank Hill Gate of Fort Rucker, where the highway ends.  SR 37 is routed along a two-lane undivided highway for its brief length.\n\nQuestion: What is the largest city in the county containing the majority of SR 37?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"state_route_number\": {\n      \"type\": \"integer\",\n      \"description\": \"The numerical identifier of the state route.\"\n    },\n    \"state_route_location\": {\n      \"type\": \"string\",\n      \"description\": \"The U.S. state where the identified state route is primarily located.\"\n    },\n    \"county_containing_majority\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the county that contains the majority of the state route.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the county is located.\"\n        },\n        \"largest_city\": {\n          \"type\": \"string\",\n          \"description\": \"The largest city within the identified county.\"\n        },\n        \"county_seat\": {\n          \"type\": \"string\",\n          \"description\": \"The county seat of the identified county.\"\n        },\n        \"population_2010_census\": {\n          \"type\": \"integer\",\n          \"description\": \"The population of the county as of the 2010 census.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"state\",\n        \"largest_city\",\n        \"county_seat\",\n        \"population_2010_census\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"state_route_number\",\n    \"state_route_location\",\n    \"county_containing_majority\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "state_route_number": {
        "type": "integer",
        "description": "The numerical identifier of the state route."
      },
      "state_route_location": {
        "type": "string",
        "description": "The U.S. state where the identified state route is primarily located."
      },
      "county_containing_majority": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the county that contains the majority of the state route."
          },
          "state": {
            "type": "string",
            "description": "The state where the county is located."
          },
          "largest_city": {
            "type": "string",
            "description": "The largest city within the identified county."
          },
          "county_seat": {
            "type": "string",
            "description": "The county seat of the identified county."
          },
          "population_2010_census": {
            "type": "integer",
            "description": "The population of the county as of the 2010 census."
          }
        },
        "required": [
          "name",
          "state",
          "largest_city",
          "county_seat",
          "population_2010_census"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "state_route_number",
      "state_route_location",
      "county_containing_majority"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
