{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMontclair State University station: Montclair State University Station at Little Falls is a New Jersey Transit rail station in the Great Notch area of Little Falls, New Jersey on the Montclair-Boonton Line.  The station, which opened on October 20, 2004, is located on Clove Road near Route 46 and the Montclair State University campus, and was built at a cost of US$ , following the completion of the Montclair Connection.  Although the station itself was not officially open, a temporary platform was built to allow the under-construction station to serve one of its main purposes as the Montclair-Boonton Line's primary transfer station.\n\nGreat Notch station: The Great Notch train station, formerly known as Caldwell Junction, was a small New Jersey Transit facility in the Great Notch section of Little Falls, New Jersey.  The station was served seven times a day, three inbound morning trains to Hoboken Terminal and four outbound evening trains from Hoboken by the Montclair-Boonton Line from Monday to Friday.  Located at the intersection of Notch Road and Long Hill Road, it was the second of three stations in Little Falls, the other two being Montclair State University and Little Falls, and was the first on the line to be strictly served by diesel trains.  However, most trains bypassed this station and continued on to Little Falls (westbound) and Montclair State University (eastbound).  The station was served by a single track with an unused side track.  The last trains stopped at the station on January 15, 2010, at 7:41pm.\n\nLittle Falls station: Little Falls is the second of two stations maintained by New Jersey Transit in Little Falls, New Jersey.  The station, on the Montclair-Boonton Line is the first to receive limited revenue service due to the end of electrification at the site of the former Great Notch station.  Little Falls station, located at Union Avenue (Passaic County Route 646) in downtown has one side platform with the 1915 station depot, built of brick on the side.  The station contains one track for revenue service, and a passing siding for trains.  The station is the eighth fare zone, costing $7.75 for a one-way ticket to Hoboken Terminal and a dollar more to transfer at Newark Broad Street to New York Pennsylvania Station.  The station has 194 parking spaces, 134 on Railroad Avenue at Montclair Avenue and sixty more along Montclair Avenue.  A ticket machine is available.  The station is not accessible for handicapped persons.  Anyone wishing to receive train service for handicapped must go to Montclair State University station or Wayne Route 23 Transit Center across the Passaic River in Wayne.\n\nMontclair State University: Montclair State University is a public doctoral research university (R3) located in the Upper Montclair section of Montclair, at the intersection of the Great Notch area of Little Falls, and the Montclair Heights section of Clifton, in the U.S. state of New Jersey.  Montclair State University is the second largest University in New Jersey.  As of October 2015, there were 20,465 total enrolled students: 16,336 undergraduate students and 4,129 graduate students.  The campus covers approximately 500 acre , inclusive of the New Jersey School of Conservation in Stokes State Forest.  The University attracts students from within the state, from many other states in the Northeast and elsewhere, and many foreign countries.  More than 250 majors, minors and concentrations are offered.\n\nHank Ferris: Henry M. \"Hank\" Ferris is a former head football coach for the Montclair State University Red Hawks in Upper Montclair, New Jersey.  In three seasons as head coach he compiled a record of 9–17.\n\nUpper Montclair station: Upper Montclair is a New Jersey Transit station in Upper Montclair, New Jersey, a CDP of Montclair, New Jersey.  The station is part of the Montclair-Boonton Line.  The station is located between two grade level crossings on Bellevue Avenue and Lorraine Avenue, and between North Mountain Avenue and Upper Montclair Plaza parallel to the railroad, and is within steps of the Upper Montclair Business District.  The station is at mile point 13.7 on the Boonton Line.  Closing the grade crossing of Lorraine Avenue is being considered for safety reasons.\n\nGreat Notch, New Jersey: Great Notch is an unincorporated community located in eastern Little Falls, in Passaic County, New Jersey, United States.  It gets its name from a gap in the first of the Watchung Mountains.  Located in Great Notch are parts of Montclair State University and the Great Notch Fire Company.\n\nClary Anderson: Clarence Oscar \"Clary\" Anderson (c. 1911 – August 1988) was an American football and baseball player and coach in the United States.  He was the head baseball and football coach for the Montclair State University Red Hawks in Upper Montclair, New Jersey.  In seven seasons as football head coach he compiled a record of 46–20–3, including the first five straight conference titles in the newly formed New Jersey State Athletic Conference from 1969 to 1973.  Prior to that, he was the very successful head coach in football for decades at Montclair High School.\n\nJerry Edwards: Gerald \"Jerry\" Edwards was a former head football coach for the Montclair State University Red Hawks in Upper Montclair, New Jersey.  In six seasons as head coach he compiled a record of 36–12.  Edwards also coached Montclair State's track and field and J.V. basketball teams.  He died in 2010 after a short illness.\n\nMontclair Heights station: Montclair Heights is a New Jersey Transit station in Montclair, New Jersey along the Montclair-Boonton Line.  The name of the station comes from the nearby community, which consists of parts of both Montclair and neighboring Clifton that share the Montclair Heights name.\n\nQuestion: Henry M. \"Hank\" Ferris is a former head football coach for which public doctoral research university (R3) located in the Upper Montclair section of Montclair, at the intersection of the Great Notch area of Little Falls, and the Montclair Heights section of Clifton, in the U.S. state of New Jersey?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the public doctoral research university.\"\n    },\n    \"university_classification\": {\n      \"type\": \"string\",\n      \"description\": \"The classification of the university, e.g., public doctoral research university (R3).\"\n    },\n    \"university_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"main_section\": {\n          \"type\": \"string\",\n          \"description\": \"The primary section of the city where the university is located.\"\n        },\n        \"main_city\": {\n          \"type\": \"string\",\n          \"description\": \"The main city where the university is located.\"\n        },\n        \"intersecting_areas\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"area_name\": {\n                \"type\": \"string\",\n                \"description\": \"The name of an intersecting area.\"\n              },\n              \"municipality\": {\n                \"type\": \"string\",\n                \"description\": \"The municipality associated with the intersecting area.\"\n              }\n            },\n            \"required\": [\n              \"area_name\",\n              \"municipality\"\n            ],\n            \"additionalProperties\": false\n          },\n          \"description\": \"A list of areas and their municipalities that intersect at the university's location.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The U.S. state where the university is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the university is located.\"\n        }\n      },\n      \"required\": [\n        \"main_section\",\n        \"main_city\",\n        \"intersecting_areas\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"associated_coach\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"coach_full_name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the coach.\"\n        },\n        \"coach_nickname\": {\n          \"type\": \"string\",\n          \"description\": \"The nickname of the coach.\"\n        },\n        \"coach_role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the coach at the university.\"\n        }\n      },\n      \"required\": [\n        \"coach_full_name\",\n        \"coach_nickname\",\n        \"coach_role\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"university_classification\",\n    \"university_location\",\n    \"associated_coach\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the public doctoral research university."
      },
      "university_classification": {
        "type": "string",
        "description": "The classification of the university, e.g., public doctoral research university (R3)."
      },
      "university_location": {
        "type": "object",
        "properties": {
          "main_section": {
            "type": "string",
            "description": "The primary section of the city where the university is located."
          },
          "main_city": {
            "type": "string",
            "description": "The main city where the university is located."
          },
          "intersecting_areas": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "area_name": {
                  "type": "string",
                  "description": "The name of an intersecting area."
                },
                "municipality": {
                  "type": "string",
                  "description": "The municipality associated with the intersecting area."
                }
              },
              "required": [
                "area_name",
                "municipality"
              ],
              "additionalProperties": false
            },
            "description": "A list of areas and their municipalities that intersect at the university's location."
          },
          "state": {
            "type": "string",
            "description": "The U.S. state where the university is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the university is located."
          }
        },
        "required": [
          "main_section",
          "main_city",
          "intersecting_areas",
          "state",
          "country"
        ],
        "additionalProperties": false
      },
      "associated_coach": {
        "type": "object",
        "properties": {
          "coach_full_name": {
            "type": "string",
            "description": "The full name of the coach."
          },
          "coach_nickname": {
            "type": "string",
            "description": "The nickname of the coach."
          },
          "coach_role": {
            "type": "string",
            "description": "The role of the coach at the university."
          }
        },
        "required": [
          "coach_full_name",
          "coach_nickname",
          "coach_role"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "university_name",
      "university_classification",
      "university_location",
      "associated_coach"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
