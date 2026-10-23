{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2010 Alaska C-17 crash: On July 28, 2010, a U.S. Air Force transport plane crashed at Elmendorf Air Force Base in Alaska, resulting in the death of all four crew members aboard.  The aircraft involved was a Boeing C-17 Globemaster III (tail number \"00-0173\") and the crash was the first fatal C-17 flight mishap.  The crew were practicing for Elmendorf's Arctic Thunder Air Show, which took place three days later.\n\nElmendorf Air Force Base: Elmendorf Air Force Base (IATA: EDF, ICAO: PAED, FAA LID: EDF) is a United States military facility in Anchorage, the largest city in Alaska.  Originally known as Elmendorf Field, it became Elmendorf Air Force Base after World War II, and in 2010 it merged with nearby Fort Richardson to form Joint Base Elmendorf-Richardson.\n\n1995 Alaska Boeing E-3 Sentry accident: The Alaska Boeing E-3 Sentry accident was the 22 September 1995 crash of a United States Air Force Boeing E-3 Sentry airborne early warning aircraft with the loss of all 24 people on board.  The aircraft, serial number \"77-0354\" with callsign \"Yukla 27,\" hit birds on departure from Elmendorf Air Force Base in Alaska, United States.  With the loss of thrust from both of the left engines the aircraft crashed into a wooded area less than a mile from the end of the runway.\n\nJoint Base Elmendorf–Richardson: Joint Base Elmendorf–Richardson (IATA: EDF, ICAO: PAED, FAA LID: EDF) , or J-BER as it is known to most military members, is a United States military facility in Anchorage, the largest city in Alaska.  It is an amalgamation of the United States Air Force's Elmendorf Air Force Base and the United States Army's Fort Richardson, which were merged in 2010.\n\nBoeing C-17 Globemaster III: The Boeing C-17 Globemaster III is a large military transport aircraft.  It was developed for the United States Air Force (USAF) from the 1980s to the early 1990s by McDonnell Douglas.  The C-17 carries forward the name of two previous piston-engined military cargo aircraft, the Douglas C-74 Globemaster and the Douglas C-124 Globemaster II.  The C-17 commonly performs tactical and strategic airlift missions, transporting troops and cargo throughout the world; additional roles include medical evacuation and airdrop duties.  It was designed to replace the Lockheed C-141 Starlifter, and also fulfill some of the duties of the Lockheed C-5 Galaxy, freeing the C-5 fleet for outsize cargo.\n\n4158th Strategic Wing: The 4158th Strategic Wing is a discontinued United States Air Force unit.  It was active in Alaska from 1960 to 1966 as a control and support organization for Strategic Air Command (SAC) units deployed to Elmendorf Air Force Base, Alaska.\n\n3d Operations Group: The 3d Operations Group is the operational flying component of the United States Air Force 3d Wing.  It is stationed at Elmendorf Air Force Base, Alaska, and is assigned to Pacific Air Forces' Eleventh Air Force.\n\n673d Air Base Wing: The 673d Air Base Wing is the support unit for Joint Base Elmendorf-Richardson, a combination of the United States Air Force's Elmendorf Air Force Base and the United States Army's Fort Richardson.  The 2005 Base Realignment and Closure Commission called for the combination of the two installations.  The wing replaced the 673d Air Base Wing (Provisional), which had been formed in January 2009, primarily from elements of the 3d Mission Support Group.\n\nDouble cantilever hangar: A Double cantilever hangar is a type of hangar that was constructed by the United States Air Force during the Cold War.  Large hangers were constructed at Castle Air Force Base, Loring Air Force Base, Carswell Air Force Base, and Travis Air Force Base, while smaller hangars were constructed at March Air Force Base, Edwards Air Force Base, Hanscom Air Force Base, and Homestead Air Force Base.\n\nRed Flag – Alaska: RED FLAG-Alaska is a realistic, 10-day air combat United States Air Force training exercise held up to four times a year.  It is held at Eielson Air Force Base and Elmendorf Air Force Base in the State of Alaska.  Each \"RED FLAG-Alaska\" exercise is a multi-service, multi-platform coordinated, combat operations exercise and corresponds to the designed operational capability of participating units.  In other words, exercises often involve several units whose military mission may differ significantly from that of other participating units.  \"RED FLAG-Alaska\" planners take those factors into consideration when designing exercises so participants get the maximum training possible without being placed at an unfair advantage during simulated combat scenarios.\n\nQuestion: What plane developed for the United States Air Force crashed in 2010 at Elmendorf Air Force Base in Alaska?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"aircraft_model_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the aircraft model involved in the crash.\"\n    },\n    \"aircraft_developer\": {\n      \"type\": \"string\",\n      \"description\": \"The company that developed the aircraft.\"\n    },\n    \"developed_for_usaf\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the aircraft was developed for the United States Air Force.\"\n    },\n    \"crash_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"crash_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the crash occurred.\"\n        },\n        \"crash_location\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Air Force Base where the crash took place.\"\n        },\n        \"fatalities_count\": {\n          \"type\": \"integer\",\n          \"description\": \"The number of people who died in the crash.\"\n        },\n        \"is_first_fatal_mishap_for_model\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if this was the first fatal mishap for this specific aircraft model.\"\n        }\n      },\n      \"required\": [\n        \"crash_year\",\n        \"crash_location\",\n        \"fatalities_count\",\n        \"is_first_fatal_mishap_for_model\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"aircraft_model_name\",\n    \"aircraft_developer\",\n    \"developed_for_usaf\",\n    \"crash_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "aircraft_model_name": {
        "type": "string",
        "description": "The full name of the aircraft model involved in the crash."
      },
      "aircraft_developer": {
        "type": "string",
        "description": "The company that developed the aircraft."
      },
      "developed_for_usaf": {
        "type": "boolean",
        "description": "Indicates if the aircraft was developed for the United States Air Force."
      },
      "crash_details": {
        "type": "object",
        "properties": {
          "crash_year": {
            "type": "integer",
            "description": "The year the crash occurred."
          },
          "crash_location": {
            "type": "string",
            "description": "The name of the Air Force Base where the crash took place."
          },
          "fatalities_count": {
            "type": "integer",
            "description": "The number of people who died in the crash."
          },
          "is_first_fatal_mishap_for_model": {
            "type": "boolean",
            "description": "True if this was the first fatal mishap for this specific aircraft model."
          }
        },
        "required": [
          "crash_year",
          "crash_location",
          "fatalities_count",
          "is_first_fatal_mishap_for_model"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "aircraft_model_name",
      "aircraft_developer",
      "developed_for_usaf",
      "crash_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
