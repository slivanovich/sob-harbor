{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUniversity Park Airport: University Park Airport (IATA: SCE, ICAO: KUNV, FAA LID: UNV) is a public airport located in Benner Township, Centre County, Pennsylvania.  The airport serves the towns of State College and Bellefonte, and the surrounding area.\n\nColumbus Regional Airport Authority: Columbus Regional Airport Authority (CRAA) oversees the operations of John Glenn Columbus International Airport, Rickenbacker International Airport and Bolton Field airports in the Columbus, Ohio, area.\n\nInterstate 270 (Ohio): Interstate 270 (abbreviated I-270) is the beltway loop freeway in the Columbus metropolitan area, commonly known locally as \"The Outerbelt,\" or the \"Jack Nicklaus Freeway.\"  The \"western\" (and \"eastern\") terminus of I-270, at least in terms of the zero-milepost, is at the junction with I-71 east of Grove City, Ohio.  I-270, along with I-670, provides access to John Glenn Columbus International Airport.  The entire length of I-270 is 54.97 mi .  It is one of four interstate loops not to share with another interstate freeway, the others being I-295 in Florida, I-485 in North Carolina, and I-610 in Texas.\n\nJohn Glenn Columbus International Airport: John Glenn Columbus International Airport (IATA: CMH, ICAO: KCMH, FAA LID: CMH) , is an international airport located 6 mi east of downtown Columbus, Ohio.  Formerly known as Port Columbus International Airport, it is managed by the Columbus Regional Airport Authority, which also oversees operations at Rickenbacker International Airport and Bolton Field.  The airport code 'CMH' stands for \"Columbus Municipal Hangar,\" the original name for the airport.\n\nBrushstrokes in Flight: Brushstrokes in Flight is a 1984 sculpture by Roy Lichtenstein, installed at the John Glenn Columbus International Airport in Columbus, Ohio.  It is part of the \"Brushstrokes\" series of artworks that includes several paintings and sculptures whose subject is the actions made with a house-painter's brush.\n\nInterstate 670 (Ohio): Interstate 670 (I-670) is an Interstate Highway in the U.S. state of Ohio that passes through downtown Columbus, connecting I-70 west of downtown with I-270 and US 62 near the eastern suburb of Gahanna.  I-670 provides access to John Glenn Columbus International Airport, and intersects SR 315 and I-71 downtown.  The section between SR 315 and I-71 is commonly referred to by locals as the \"North Innerbelt\", with the rest of the innerbelt consisting of SR 315 (west), I-70 (south), and I-71 (east and south).\n\nBolton Field: Bolton Field (ICAO: KTZR, FAA LID: TZR) is a public airport eight miles (13 km) southwest of Columbus, in Franklin County, Ohio.  It is a towered airport operated under the Columbus Regional Airport Authority.  It is one of 12 general aviation reliever airports in Ohio recognized in the National Plan of Integrated Airport Systems (NPIAS) and is a reliever airport for John Glenn Columbus International Airport.\n\nRickenbacker International Airport: Rickenbacker International Airport (IATA: LCK, ICAO: KLCK, FAA LID: LCK) is a civil-military public airport 10 mi south of downtown Columbus, near Lockbourne in southern Franklin County, Ohio, United States.  The south end of the airport extends into Pickaway County.  The base was named for flying ace and Columbus native Eddie Rickenbacker.  It is managed by the Columbus Regional Airport Authority, which also operates John Glenn Columbus International Airport and Bolton Field.  Rickenbacker International is primarily a cargo airport for the city of Columbus, although since 2012 it has served an increasing number of passenger flights as well as charter carriers.\n\nCleveland Burke Lakefront Airport: Cleveland Burke Lakefront Airport (IATA: BKL, ICAO: KBKL, FAA LID: BKL) is a public airport on the shore of Lake Erie, in the northeast part of downtown Cleveland, Ohio, United States.  It classified as a general aviation airport and is an FAA designated reliever to Cleveland Hopkins International Airport (CLE), which is Greater Cleveland's primary airport.  In 2008, based on FAA data, Burke Lakefront was the fourth busiest airport in the state of Ohio after, Cleveland Hopkins, Port Columbus International and Akron-Canton, up from 7th in 2007.  It is named after former Cleveland mayor and U.S. senator Thomas A. Burke.\n\nJohn Glenn College of Public Affairs: The John Glenn College of Public Affairs is a public policy and management school at The Ohio State University.  The Glenn College offers undergraduate, graduate and doctoral programs in public affairs.  The Glenn College provides research, training and technical assistance to state, public and nonprofit organizations.  The college is named after United States Senator and Astronaut John Glenn.  On January 30, 2015, the Ohio State University Board of Trustees approved a change of status of the former John Glenn School of Public Affairs making the new John Glenn College of Public Affairs the 15th college at The Ohio State University.\n\nQuestion: Which airport's code is CMH, John Glenn Columbus International Airport or University Park Airport?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"target_iata_code\": {\n      \"type\": \"string\",\n      \"description\": \"The IATA code being queried.\"\n    },\n    \"airports_evaluated\": {\n      \"type\": \"array\",\n      \"description\": \"List of airports mentioned in the question and their details.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"airport_name\": {\n            \"type\": \"string\",\n            \"description\": \"The full name of the airport.\"\n          },\n          \"iata_code\": {\n            \"type\": \"string\",\n            \"description\": \"The IATA code for this airport.\"\n          }\n        },\n        \"required\": [\n          \"airport_name\",\n          \"iata_code\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"identified_airport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airport whose IATA code matches the target_iata_code.\"\n    }\n  },\n  \"required\": [\n    \"target_iata_code\",\n    \"airports_evaluated\",\n    \"identified_airport_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "target_iata_code": {
        "type": "string",
        "description": "The IATA code being queried."
      },
      "airports_evaluated": {
        "type": "array",
        "description": "List of airports mentioned in the question and their details.",
        "items": {
          "type": "object",
          "properties": {
            "airport_name": {
              "type": "string",
              "description": "The full name of the airport."
            },
            "iata_code": {
              "type": "string",
              "description": "The IATA code for this airport."
            }
          },
          "required": [
            "airport_name",
            "iata_code"
          ],
          "additionalProperties": false
        }
      },
      "identified_airport_name": {
        "type": "string",
        "description": "The name of the airport whose IATA code matches the target_iata_code."
      }
    },
    "required": [
      "target_iata_code",
      "airports_evaluated",
      "identified_airport_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
