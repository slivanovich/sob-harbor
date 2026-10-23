{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHenry Hudson Parkway: The Henry Hudson Parkway is an 11.05 mi parkway in New York City.  The southern terminus is at West 72nd Street in Manhattan, where the parkway continues south as the West Side Highway.  It is often erroneously referred to as the West Side Highway throughout its entire course in Manhattan.  The northern terminus is at the Bronx–Westchester county boundary, where it continues north as the Saw Mill River Parkway.  All but the northernmost mile of the road is co-signed as New York State Route 9A (NY 9A).  In addition, the entirety of the parkway is designated New York State Route 907V (NY 907V), an unsigned reference route.\n\nWantagh State Parkway: The Wantagh State Parkway is a 13.33 mi long state parkway on Long Island, New York, in the United States.  It links the Ocean Parkway in Jones Beach State Park with the Northern State Parkway in Westbury.  The parkway is located approximately 30 mi east of Manhattan and 14 mi east of the Nassau–Queens border.  Construction began in 1927 on this, one of the earliest of the Long Island parkways, with the initial 5 mi segment opening two years later as the Jones Beach Causeway, connecting Merrick Road in Wantagh to newly opened Jones Beach State Park.  The parkway is inventoried by the New York State Department of Transportation (NYSDOT) as New York State Route 908T (NY 908T), an unsigned reference route.\n\nNorthern State Parkway: The Northern State Parkway (also known as the Northern State or Northern Parkway) is a 28.88 mi limited-access state parkway on Long Island in the U.S. state of New York.  The western terminus is at the Queens–Nassau County line, where the parkway continues westward into New York City as the Grand Central Parkway.  The eastern terminus is at New York State Route 347 (NY 347) and NY 454 in Hauppauge.  The parkway is designated New York State Route 908G (NY 908G), an unsigned reference route.  As its name implies, the parkway services communities along the northern half of the island.\n\nOcean Parkway (Long Island): The Ocean Parkway is a 15.59 mi parkway that traverses Jones Beach Island between Jones Beach State Park and Captree State Park on Long Island, New York, in the United States.  It begins at the southern terminus of the Meadowbrook State Parkway and heads east across Jones Beach Island, intersecting the south end of the Wantagh State Parkway before ending just past the southern terminus of the Robert Moses Causeway.  The highway is designated New York State Route 909D (NY 909D), an unsigned reference route.\n\nMeadowbrook State Parkway: The Meadowbrook State Parkway (also known as the Meadowbrook, the Meadowbrook Parkway or the MSP) is a 12.52 mi parkway in Nassau County, New York, in the United States.  Its southern terminus is at a full cloverleaf interchange with the Bay and Ocean parkways in Jones Beach State Park.  The parkway heads north, crossing South Oyster Bay and intersecting Loop Parkway before crossing onto the mainland and connecting to the Southern State Parkway in North Merrick.  It continues north to the village of Carle Place, where the Meadowbrook Parkway ends at exit 31A of the Northern State Parkway.  The Meadowbrook Parkway is designated New York State Route 908E (NY 908E), an unsigned reference route.  Most of the road is limited to non-commercial traffic, like most parkways in the state of New York; however, the portion south of Merrick Road is open to commercial traffic.\n\nRobert Moses Causeway: The Robert Moses Causeway is an 8.10 mi -long parkway in Suffolk County, New York, in the United States.  The parkway, originally known as the Captree Causeway, connects West Islip on Long Island to the barrier beach islands, such as Captree Island, Jones Beach Island, and the western tip of Fire Island, to the south.  It is designated New York State Route 908J (NY 908J), an unsigned reference route.  Except south of NY 27A, the road, like most parkways in New York State, is limited to non-commercial traffic.\n\nNiagara Scenic Parkway: The Niagara Scenic Parkway (known as the Robert Moses State Parkway until 2016) is an 18.42 mi long north–south highway in western Niagara County, New York, in the United States.  Its southern terminus is at the LaSalle Expressway on the east bank of the Niagara River in Niagara Falls.  The northern terminus is at NY 18 at Four Mile Creek State Park in Porter near Lake Ontario.  Originally, the parkway was one continuous road; however, due to low usage, a portion of the parkway near Niagara Falls was removed, separating the parkway into two sections.  The length of the parkway is designated as New York State Route 957A by the New York State Department of Transportation (NYSDOT).  A 1.16 mi long spur connecting the Niagara Scenic Parkway to Fort Niagara State Park near Youngstown is designated as New York State Route 958A.  Both reference route designations are unsigned.\n\nConey Island Avenue: Coney Island Avenue is a roadway in the New York City borough of Brooklyn that runs north-south for a distance of roughly five miles, almost parallel to Ocean Parkway and Ocean Avenue.  It begins at Brighton Beach Avenue in Coney Island and goes north to Park Circle at the southwest corner of Prospect Park, where it becomes Prospect Park Southwest.  Near-parallel Ocean Parkway terminates five blocks south and three blocks west of that intersection, becoming the Prospect Expressway (New York State Route 27).  Ocean Parkway originally extended north to Park Circle, where Coney Island Avenue meets Prospect Park, until construction of the Prospect Expressway replaced the northern half-mile of Ocean Parkway but included ramps to the edge of Prospect Park.\n\nBronx River Parkway: The Bronx River Parkway (sometimes abbreviated as the Bronx Parkway) is a 19.12 mi long parkway in downstate New York in the United States.  It is named for the nearby Bronx River, which it parallels.  The southern terminus of the parkway is at Story Avenue near Bruckner Expressway in the Bronx neighborhood of Soundview.  The northern terminus is at the Kensico Circle in North Castle, Westchester County, where the parkway connects to the Taconic State Parkway and, via a short connector, New York State Route 22 (NY 22).  Within the Bronx, the parkway is maintained by the New York State Department of Transportation and is designated New York State Route 907H (NY 907H), an unsigned reference route.  In Westchester County, the parkway is maintained by the Westchester County Department of Public Works and is designated unsigned County Route 9987 (CR 9987).\n\nYonkers Avenue: Yonkers Avenue is an east–west street in the city of Yonkers in Westchester County, New York, in the United States.  It is one of four major east–west through routes in the city.  The western terminus of the street is at Nepperhan Avenue, which connects to U.S. Route 9 (US 9) and New York State Route 9A (NY 9A).  Its eastern terminus is at Bronx River Road near the Bronx River Parkway.  The entirety of Yonkers Avenue is maintained by the New York State Department of Transportation as New York State Route 983C from Nepperhan Avenue to the Saw Mill River Parkway and New York State Route 984E from the Saw Mill Parkway to Bronx River Road.  Both are unsigned reference route designations.\n\nQuestion: The Ocean Parkway ends just past the southern terminus of a causeway that has what New York State Route designation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"parkway_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the parkway whose terminus is being described.\"\n    },\n    \"terminus_location_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of where the parkway ends, referencing another feature.\"\n    },\n    \"related_causeway\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the causeway mentioned in relation to the parkway's terminus.\"\n        },\n        \"route_designation\": {\n          \"type\": \"string\",\n          \"description\": \"The New York State Route designation for the causeway.\"\n        },\n        \"is_unsigned_reference_route\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the route designation is an unsigned reference route.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"route_designation\",\n        \"is_unsigned_reference_route\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer_route_designation\": {\n      \"type\": \"string\",\n      \"description\": \"The specific New York State Route designation that answers the question.\"\n    }\n  },\n  \"required\": [\n    \"parkway_name\",\n    \"terminus_location_description\",\n    \"related_causeway\",\n    \"final_answer_route_designation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "parkway_name": {
        "type": "string",
        "description": "The name of the parkway whose terminus is being described."
      },
      "terminus_location_description": {
        "type": "string",
        "description": "A description of where the parkway ends, referencing another feature."
      },
      "related_causeway": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the causeway mentioned in relation to the parkway's terminus."
          },
          "route_designation": {
            "type": "string",
            "description": "The New York State Route designation for the causeway."
          },
          "is_unsigned_reference_route": {
            "type": "boolean",
            "description": "Indicates if the route designation is an unsigned reference route."
          }
        },
        "required": [
          "name",
          "route_designation",
          "is_unsigned_reference_route"
        ],
        "additionalProperties": false
      },
      "final_answer_route_designation": {
        "type": "string",
        "description": "The specific New York State Route designation that answers the question."
      }
    },
    "required": [
      "parkway_name",
      "terminus_location_description",
      "related_causeway",
      "final_answer_route_designation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
