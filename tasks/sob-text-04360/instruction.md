{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRay Brook, New York: Ray Brook is a hamlet in New York State, United States located on NY 86 between Saranac Lake and Lake Placid in the Town of North Elba in Essex County.  It is the site of the Adirondack Park Agency, the District 5 office of the New York State Department of Environmental Conservation, the Federal Correctional Institution, Ray Brook and the Adirondack Correctional Facility.  The New York State Office of Real Property Tax Services - an office within the New York State Department of Taxation and Finance - has an office here as well.\n\nU.S. Route 44 in New York: U.S. Route 44 (US 44) in the state of New York is a major east–west thoroughfare in the Hudson Valley region of the state.  Its entire 65.98 mi length is maintained by the New York State Department of Transportation (NYSDOT), with the exception of the Mid-Hudson Bridge, which is maintained by the New York State Bridge Authority.  The portion of the route in New York begins at an intersection with US 209 and New York State Route 55 (NY 55) near the hamlet of Kerhonkson and ends at the Connecticut state line near the village of Millerton.  The road passes through rural parts of Ulster and Dutchess counties before crossing into Litchfield County, Connecticut.\n\nBronx River Parkway: The Bronx River Parkway (sometimes abbreviated as the Bronx Parkway) is a 19.12 mi long parkway in downstate New York in the United States.  It is named for the nearby Bronx River, which it parallels.  The southern terminus of the parkway is at Story Avenue near Bruckner Expressway in the Bronx neighborhood of Soundview.  The northern terminus is at the Kensico Circle in North Castle, Westchester County, where the parkway connects to the Taconic State Parkway and, via a short connector, New York State Route 22 (NY 22).  Within the Bronx, the parkway is maintained by the New York State Department of Transportation and is designated New York State Route 907H (NY 907H), an unsigned reference route.  In Westchester County, the parkway is maintained by the Westchester County Department of Public Works and is designated unsigned County Route 9987 (CR 9987).\n\nMosholu Parkway: The Mosholu Parkway is a hybrid freeway-standard parkway and grade-level roadway in the New York City borough of the Bronx, constructed from 1935 to 1937 as part of the roadway network created under Robert Moses.  The roadway extends for 3.0 mi between the New York Botanical Garden (where its southeast end meets the Bronx River Parkway) and Van Cortlandt Park (where its northwest end meets the Henry Hudson Parkway).  The New York City Department of Transportation is responsible for the operation and maintenance of the roadway while the New York City Department of Parks and Recreation is responsible for the surrounding rights-of-way.  The parkway is designated as New York State Route 908F (NY 908F), an unsigned reference route, by the New York State Department of Transportation.\n\nProspect Mountain Veterans Memorial Highway: The Prospect Mountain Veterans Memorial Highway is a parkway located in the town of Lake George, New York.  The road is 5.88 mi long, starting at the U.S. Route 9 (US 9) and New York State Route 9N (NY 9N) concurrency and ending at the peak of Prospect Mountain.  Although the road is designated as New York State Route 917A, an unsigned reference route, by the New York State Department of Transportation, all maintenance on the roadway is performed by the New York State Department of Environmental Conservation.\n\nYonkers Avenue: Yonkers Avenue is an east–west street in the city of Yonkers in Westchester County, New York, in the United States.  It is one of four major east–west through routes in the city.  The western terminus of the street is at Nepperhan Avenue, which connects to U.S. Route 9 (US 9) and New York State Route 9A (NY 9A).  Its eastern terminus is at Bronx River Road near the Bronx River Parkway.  The entirety of Yonkers Avenue is maintained by the New York State Department of Transportation as New York State Route 983C from Nepperhan Avenue to the Saw Mill River Parkway and New York State Route 984E from the Saw Mill Parkway to Bronx River Road.  Both are unsigned reference route designations.\n\nNew York State Department of Public Works: The office of Superintendent of Public Works was created by an 1876 amendment to the New York State Constitution.  It abolished the canal commissioners and established that the Department of Public Works execute all laws relating to canal maintenance and navigation except for those functions performed by the New York State Engineer and Surveyor who continued to prepare maps, plans and estimates for canal construction and improvement.  The Canal Board (now consisting of the Superintendent of Public Works, the State Engineer and Surveyor, and the Commissioners of the Canal Fund) continued to handle hiring of employees and other personnel matters.  The Barge Canal Law of 1903 (Chapter 147) directed the Canal Board to oversee the enlargement of and improvements to the Erie Canal, the Champlain Canal and the Oswego Canal.  In 1967, the Department of Public Works was merged with other departments into the new New York State Department of Transportation.\n\nNew York State Route 380: New York State Route 380 (NY 380) was a 23 mi north–south state highway in Chautauqua County, New York, in the United States.  The southern terminus of the route was at an intersection with NY 60 in the town of Gerry.  Its northern terminus was at a junction with NY 5 north of the village of Brocton in the town of Portland.  In actuality, most of NY 380 was maintained by Chautauqua County; the only part that was maintained by the New York State Department of Transportation was from NY 424 in Stockton to the west end of its overlap with U.S. Route 20 (US 20) in Brocton.\n\nNew York State Route 351: New York State Route 351 (NY 351) is a north–south state highway in central Rensselaer County, New York, in the United States.  It extends for 8.16 mi from an intersection with NY 43 in the Sand Lake hamlet of West Sand Lake to a junction with NY 2 in the Brunswick hamlet of Cropseyville.  The portion of NY 351 north of the hamlet of Poestenkill was originally designated as New York State Route 153 in the 1930s.  This designation was removed in the 1940s, and the West Sand Lake–Cropseyville roadway became County Route 77 (CR 77) sometime afterward.  On April 1, 1980, all of CR 77 was transferred to the state of New York, at which time it was redesignated as NY 351 by the New York State Department of Transportation (NYSDOT).\n\nU.S. Route 20 in New York: U.S. Route 20 (US 20) is a part of the U.S. Highway System that runs from Newport, Oregon, to Boston, Massachusetts.  In the U.S. state of New York, US 20 extends 372.32 mi from the Pennsylvania state line at Ripley to the Massachusetts state line in the Berkshire Mountains.  US 20 is the longest surface road in New York.  It runs near the Lake Erie shore from Ripley to Buffalo and passes through the southern suburbs of Buffalo, the Finger Lakes, the glacial moraines of Central New York, and the city of Albany before crossing into Massachusetts.  US 20 connects to all three major north–south Interstate Highways in Upstate New York: Interstate 390 (I-390) near Avon, I-81 south of Syracuse, and I-87 in Albany by way of Fuller Road Alternate.\n\nQuestion: New York State Department of Transportation\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"organization_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the organization.\"\n    },\n    \"formation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the organization was formed or significantly restructured.\"\n        },\n        \"formed_from_merger\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the organization was formed as a result of a merger.\"\n        },\n        \"merged_organizations\": {\n          \"type\": \"array\",\n          \"description\": \"List of organizations that merged to form this entity.\",\n          \"items\": {\n            \"type\": \"string\"\n          }\n        }\n      },\n      \"required\": [\n        \"year\",\n        \"formed_from_merger\",\n        \"merged_organizations\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"involved_routes\": {\n      \"type\": \"array\",\n      \"description\": \"A list of routes with which the organization has a defined role.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"route_name\": {\n            \"type\": \"string\",\n            \"description\": \"The common name of the route.\"\n          },\n          \"route_designation\": {\n            \"type\": \"string\",\n            \"description\": \"The official designation of the route (e.g., US 44, NY 907H).\"\n          },\n          \"role\": {\n            \"type\": \"string\",\n            \"description\": \"The role of the organization regarding this route (e.g., 'maintains', 'designates', 'redesignates', 'maintains and designates').\"\n          },\n          \"scope_of_involvement\": {\n            \"type\": \"string\",\n            \"description\": \"A description of the specific portion or aspect of the route involved.\"\n          },\n          \"actual_maintenance_by_other_entity\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the entity that performs actual maintenance if different from this organization.\"\n          }\n        },\n        \"required\": [\n          \"route_name\",\n          \"route_designation\",\n          \"role\",\n          \"scope_of_involvement\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"organization_name\",\n    \"formation_details\",\n    \"involved_routes\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "organization_name": {
        "type": "string",
        "description": "The full name of the organization."
      },
      "formation_details": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer",
            "description": "The year the organization was formed or significantly restructured."
          },
          "formed_from_merger": {
            "type": "boolean",
            "description": "Indicates if the organization was formed as a result of a merger."
          },
          "merged_organizations": {
            "type": "array",
            "description": "List of organizations that merged to form this entity.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "year",
          "formed_from_merger",
          "merged_organizations"
        ],
        "additionalProperties": false
      },
      "involved_routes": {
        "type": "array",
        "description": "A list of routes with which the organization has a defined role.",
        "items": {
          "type": "object",
          "properties": {
            "route_name": {
              "type": "string",
              "description": "The common name of the route."
            },
            "route_designation": {
              "type": "string",
              "description": "The official designation of the route (e.g., US 44, NY 907H)."
            },
            "role": {
              "type": "string",
              "description": "The role of the organization regarding this route (e.g., 'maintains', 'designates', 'redesignates', 'maintains and designates')."
            },
            "scope_of_involvement": {
              "type": "string",
              "description": "A description of the specific portion or aspect of the route involved."
            },
            "actual_maintenance_by_other_entity": {
              "type": "string",
              "description": "The name of the entity that performs actual maintenance if different from this organization."
            }
          },
          "required": [
            "route_name",
            "route_designation",
            "role",
            "scope_of_involvement"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "organization_name",
      "formation_details",
      "involved_routes"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
