{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHarwich, Massachusetts: Harwich ( ) is a New England town on Cape Cod, in Barnstable County in the state of Massachusetts in the United States.  At the 2010 census it had a population of 12,243.  The town is a popular vacation spot, located near the Cape Cod National Seashore.  Harwich's beaches are on the Nantucket Sound side of Cape Cod.  Harwich has three active harbors.  Saquatucket, Wychmere and Allen Harbors are all in Harwich Port.  The town of Harwich includes the villages of Pleasant Lake, West Harwich, East Harwich, Harwich Port, Harwich Center, North Harwich and South Harwich.  Harwich is also home to the exclusive Wequassett Resort and Golf Club.\n\nCape Cod Central Railroad: The Cape Cod Central Railroad is a heritage railroad located on Cape Cod, Massachusetts.  It operates on a rail line known as the Cape Main Line which is owned by Massachusetts Department of Transportation.  The line was previously owned and operated by the Cape Cod Railroad, the Old Colony Railroad, and later the New Haven Railroad, each of which operated passenger trains on the line from 1854 to 1959.  Although it is the namesake of the Cape Cod Central Railroad (1861–68), the two companies are unrelated.  This company, however, is the first of this brand name to not be a railroad company just on paper.\n\nCape Cod Bay: Cape Cod Bay is a large bay of the Atlantic Ocean adjacent to the U.S. state of Massachusetts.  Measuring 604 sqmi below a line drawn from Brant Rock in Marshfield to Race Point in Provincetown, Massachusetts, it is enclosed by Cape Cod to the south and east, and Plymouth County, Massachusetts, to the west.  To the north of Cape Cod Bay lie Massachusetts Bay and the Atlantic Ocean.  Cape Cod Bay is the southernmost extremity of the Gulf of Maine.  Cape Cod Bay is one of the bays adjacent to Massachusetts that give it the name Bay State.  The others are Narragansett Bay, Buzzards Bay, and Massachusetts Bay.\n\nSolid State Phased Array Radar System: The Solid State Phased Array Radar System (SSPARS, colloquially \"BMEWS radar network'\" as late as 2004) is a USAF radar, computer, and communications system for missile warning and space surveillance \"at five (5) geographically separated units worldwide including Beale AFB, CA, Cape Cod, AFS, MA, Clear AFS, AK, RAF Fylingdales, UK, and Thule AB, Greenland.\"  SSPARS completed replacement of the RCA 474L Ballistic Missile Early Warning System when the last SSPAR (phased array radar with 2500 \"solid state transmitter\" modules) was operational at Clear in 2001, the year SSPARS equipment included:\n\nJoint Base Cape Cod: The Joint Base Cape Cod is a joint base created by the Commonwealth of Massachusetts and the United States War Department in 1935.  Governor James Curley signed the state bill to allocate and purchase land for a military facility, and establishing a formal commission to manage this new state military property and personnel.  After 22000 acre of land was secured in Cape Cod, the Massachusetts National Guard began erecting tents and a basic training program in the following year.  Formerly the Massachusetts Military Reservation, it was renamed in 2013 to Joint Base Cape Cod.\n\nCape Cod Air Force Station: Cape Cod Air Force Station is a US Air Force station located in the northwest corner of Joint Base Cape Cod, United States, on Flatrock Hill in Massachusetts.  It consists of one PAVE PAWS radar station and is in continuous operation.\n\nCape Cod Rail Trail: The Cape Cod Rail Trail (CCRT) is a 22 mi paved rail trail located on Cape Cod in Massachusetts.  The trail route passes through the towns of Dennis, Harwich, Brewster, Orleans, Eastham, and Wellfleet.  It connects to the 6-plus mile (10 km) Old Colony Rail Trail leading to Chatham, and 8 miles (13 km) of trails within Nickerson State Park.  It also passes near the end of the Nauset Bike Trail leading to Coast Guard Beach in Cape Cod National Seashore.  Short side trips on roads lead to several other national seashore beaches.\n\nRockland Trust: Rockland Trust is a commercial bank based in Rockland, Massachusetts that serves Southeastern Massachusetts, Coastal Massachusetts, Cape Cod, and Boston's MetroWest.  Established in 1907 as Rockland Trust Company, it is one of few local banks that retain their original name and independent ownership after more than 100 years.  (Rockland Trust Company is the wholly owned subsidiary of Independent Bank Corp., which is publicly traded on NASDAQ (INDB).)  Rockland Trust is the largest publicly traded commercial bank headquartered in Massachusetts, with more than 8 billion in assets and over 1000 employees.  Rockland Trust offers a wide range of commercial, retail, commercial banking products and services, business and consumer loans, insurance products and services, and investment management services from: 77 retail branches, 10 commercial lending centers, and 4 mortgage banking centers located throughout Eastern Massachusetts and on Cape Cod; and 4 investment management offices located in Southeastern Massachusetts, on Cape Cod, and in Rhode Island.  Corporate headquarters are in Hanover, Massachusetts.\n\nHyannis, Massachusetts: Hyannis is the largest of the seven villages in the town of Barnstable, Massachusetts, in the United States.  It is the commercial and transportation hub of Cape Cod and was designated an urban area as of the 1990 census.  Because of this, many refer to Hyannis as the \"Capital of the Cape\".  It contains a majority of the Barnstable Town offices and two important shopping districts: the historic downtown Main Street and the Route 132 Commercial District, including Cape Cod Mall and Independence Park, headquarters of Cape Cod Potato Chips.  Cape Cod Hospital in Hyannis is the largest on Cape Cod.\n\nOld Cape Cod: \"Old Cape Cod\" is a song, written by Claire Rothrock, Milton Yakus, and Allan Jeffrey, and published in 1957.  The single, as recorded by Patti Page, became a gold record, having sold over a million copies.  Having been hailed by \"Cape Codders\" as the \"unofficial Cape Cod Anthem, if ever there was one\", the song has been credited with \"putting the Cape on the map\" and helping to establish Cape Cod as a major tourist destination.\n\nQuestion: What state is Cape Cod located in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity being located.\"\n    },\n    \"entity_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of entity, e.g., geographical region, town, base.\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"state_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the state where the entity is located.\"\n        },\n        \"state_abbreviation\": {\n          \"type\": \"string\",\n          \"description\": \"The two-letter abbreviation for the state.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the entity is located.\"\n        }\n      },\n      \"required\": [\n        \"state_name\",\n        \"state_abbreviation\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"entity_type\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the entity being located."
      },
      "entity_type": {
        "type": "string",
        "description": "The type of entity, e.g., geographical region, town, base."
      },
      "location": {
        "type": "object",
        "properties": {
          "state_name": {
            "type": "string",
            "description": "The full name of the state where the entity is located."
          },
          "state_abbreviation": {
            "type": "string",
            "description": "The two-letter abbreviation for the state."
          },
          "country": {
            "type": "string",
            "description": "The country where the entity is located."
          }
        },
        "required": [
          "state_name",
          "state_abbreviation",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_name",
      "entity_type",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
