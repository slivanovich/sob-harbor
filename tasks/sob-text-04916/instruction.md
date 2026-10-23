{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKSEE: KSEE, virtual channel 24 (UHF digital channel 38), is an NBC-affiliated television station located in Fresno, California, United States.  The station is owned by the Nexstar Media Group, as part of a duopoly with CBS affiliate KGPE (channel 47).  The two stations share studio facilities located on East McKinley Avenue in East Fresno (several blocks from Fresno Yosemite International Airport); KSEE maintains transmitter facilities located on Bear Mountain (near Meadow Lakes).\n\nCharlotte Douglas International Airport: Charlotte Douglas International Airport (IATA: CLT, ICAO: KCLT, FAA LID: CLT) is a joint civil-military public international airport located in Charlotte, North Carolina, United States.  Established in 1935 as Charlotte Municipal Airport, in 1954 the airport was renamed Douglas Municipal Airport after former Charlotte mayor Ben Elbert Douglas, Sr. The airport gained its current name in 1982 and, as of September 2017, it is the second largest hub for American Airlines after Dallas/Fort Worth International Airport, with service to 161 domestic and international destinations.  As of 2016 it was the 5th busiest airport in the United States, ranked by passenger traffic and aircraft movements.  It was also the 7th business airport in the world ranked by aircraft movements Charlotte is the largest airport in the United States without any nonstop service to Asia.  The airport serves as a major gateway to the Caribbean Islands.  CLT covers 5,558 acres (2,249 ha) of land.\n\nPaphos International Airport: Paphos International Airport (Greek: Διεθνής Αερολιμένας Πάφου ; Turkish: \"Baf Uluslararası Havaalanı\" ) (IATA: PFO, ICAO: LCPH) is a joint civil-military public airport located 6.5 km southeast of the city of Paphos, Cyprus.  It is the country's second largest airport, after Larnaca International Airport.  Paphos Airport is commonly used by tourists on vacation in western Cyprus, providing access to popular resorts such as Coral Bay, Limassol (about 50 km south-east) and Paphos itself.\n\nCoastal Carolina Regional Airport: Coastal Carolina Regional Airport (IATA: EWN, ICAO: KEWN, FAA LID: EWN) is a public airport located three miles (5 km) southeast of central business district of New Bern, a town in Craven County, North Carolina, United States.\n\nBrooksville–Tampa Bay Regional Airport: Brooksville–Tampa Bay Regional Airport (ICAO: KBKV, FAA LID: BKV) , formerly known as Hernando County Airport, is a joint civil-military public airport located 6 NM southwest of the central business district of Brooksville, a city in Hernando County, Florida, United States.  It is owned by Hernando County and is 45 mi north of Tampa.  While having consistent growth in its traffic rate, it does not yet serve the public through commercial airlines, but it does have charter and executive service.\n\nCombat Air Museum: The Combat Air Museum is a museum at Topeka Regional Airport / Forbes Field (former Forbes Air Force Base), in Williamsport Township, Shawnee County, near Topeka, Kansas.  Topeka Regional Airport is a joint civil-military public airport located six miles (10 km) south of the central business district of Topeka.\n\nFresno Yosemite International Airport: Fresno Yosemite International Airport (IATA: FAT, ICAO: KFAT, FAA LID: FAT) , formerly Fresno Air Terminal, is a joint civil-military public airport in eastern Fresno, in Fresno County, California.  Located approximately 64 miles south of Yosemite National Park on California State Route 41, it is the closest airfield to the Park with scheduled passenger airline jet service.  Situated near California State Route 168 and California State Route 180, the airport covers 1728 acres .  It maintains two runways and one helipad.  Fresno Yosemite International is the air transport center for the San Joaquin Valley, with flights to several airline hubs in the western United States.  International flights to Mexico are available through Aeroméxico and Volaris.  The airport is also home to the Fresno Air National Guard Base and the 144th Fighter Wing (144 FW) of the California Air National Guard.\n\nYosemite Area Regional Transportation System: The Yosemite Area Regional Transportation System, also known as YARTS, is a public transit bus line based in Merced, California.  YARTS provides scheduled service into popular locations within Merced, Mariposa, Mono, Madera, and Fresno counties, including Yosemite National Park and Fresno Yosemite International Airport.\n\nKMPH-TV: KMPH-TV, virtual channel 26 (UHF digital channel 28), is a Fox-affiliated television station serving Fresno, California, United States that is licensed to Visalia.  The station is owned by the Sinclair Broadcast Group as part of a duopoly with CW affiliate KFRE-TV (channel 59).  The two stations share studio facilities located on East McKinley Avenue in eastern Fresno (one mile southwest of Fresno Yosemite International Airport); KMPH maintains transmitter facilities located on Big Baldy Mountain in northwestern Tulare County.\n\nElizabeth City Regional Airport: Elizabeth City Regional Airport (IATA: ECG, ICAO: KECG, FAA LID: ECG) is a joint civil-military public and military use airport located three nautical miles (6 km) southeast of the central business district of Elizabeth City, in Pasquotank County, North Carolina, United States.  The airport, on the shore of the Pasquotank River, is also known as Elizabeth City-Pasquotank County Regional Airport or ECG Regional Airport.  It is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a \"general aviation\" facility.\n\nQuestion: Is Coastal Carolina Regional Airport a public airport or Fresno Yosemite International Airport, a joint civil-military public airport located in Craven County, North Carolina?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airport that matches the description.\"\n    },\n    \"airport_type\": {\n      \"type\": \"string\",\n      \"description\": \"The classification of the airport (e.g., public, civil-military public).\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the airport is located or near.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the airport is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the airport is located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the airport is located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"county\",\n        \"state\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"airport_name\",\n    \"airport_type\",\n    \"location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airport_name": {
        "type": "string",
        "description": "The name of the airport that matches the description."
      },
      "airport_type": {
        "type": "string",
        "description": "The classification of the airport (e.g., public, civil-military public)."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the airport is located or near."
          },
          "county": {
            "type": "string",
            "description": "The county where the airport is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the airport is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the airport is located."
          }
        },
        "required": [
          "city",
          "county",
          "state",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "airport_name",
      "airport_type",
      "location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
