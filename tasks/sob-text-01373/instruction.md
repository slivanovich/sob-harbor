Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Peach State Airport: Alexander Memorial Airport (FAA LID: GA2) , also known as Peach State Aerodrome or Candler Field, is a public grass strip located 1 mile (1.6 km) west of Williamson, Georgia, in the United States.  Alexander Memorial Airport is located in picturesque rural Pike County, 27 nautical miles (50 km) south of Hartsfield-Jackson Atlanta International Airport.

Will Rogers – Wiley Post Memorial Seaplane Base: The Will Rogers – Wiley Post Memorial Seaplane Base (FAA LID: W36) , is a seaplane base located on Lake Washington, inside the perimeter fence of the northwest corner of the Renton Municipal Airport in Renton, Washington.  It was named for the fact that these Rogers and Post, two famous personalities, departed from this point on their ultimately-fatal trip to points in Alaska.

Wiley Post–Will Rogers Memorial Airport: Wiley Post–Will Rogers Memorial Airport, (IATA: BRW, ICAO: PABR, FAA LID: BRW) often referred to as Post/Rogers Memorial is a public airport located in Utqiaġvik, a city in the North Slope Borough of the U.S. state of Alaska.  The airport is owned by the state.  Situated on the Chukchi Sea at a latitude of 71.29°N, the airport is the farthest north of any in US territory.  The airport is named after American humorist Will Rogers and aviator Wiley Post, both of whom died about 9 mi away at Point Barrow in a 1935 airplane crash.

Everts Air Cargo: Everts Air Cargo is an American Part 121 airline based in Fairbanks, Alaska, USA.  It operates D.O.D, scheduled and charter airline cargo within Alaska, Canada, Mexico and continental US Its Maintenance base is Fairbanks International Airport with its major cargo hub at Ted Stevens Anchorage International Airport.

Renton Municipal Airport: Renton Municipal Airport (IATA: RNT, ICAO: KRNT, FAA LID: RNT) is a public use airport located in Renton, a city in King County, Washington, United States.  The airport was renamed Clayton Scott Field in 2005 to celebrate the 100th birthday of Clayton Scott.  The airport's northern boundary is Lake Washington and the Will Rogers - Wiley Post Memorial Seaplane Base.  Renton Airport has a floating dock and a launching ramp for conversion from wheeled landings to water takeoffs and landings.

Northern Air Cargo: Northern Air Cargo is an American cargo airline based in Anchorage, Alaska, USA.  It operates services within Alaska and to Canada and mainland USA.  Its main base is Ted Stevens Anchorage International Airport, with a hub at Fairbanks International Airport.

Rogers-Post Site: The Rogers-Post Site, located on the North Slope of the U.S. state of Alaska, is the location of a plane crash that killed humorist Will Rogers and aviator Wiley Post on August 15, 1935, during an aerial tour of Alaska.  It is about 11 mi southwest of Barrow, on the north side of Walakpa Bay near the mouth of the Walakpa River.  The flight was described by the AP as prelude to a planned Trans-Siberian flight to Moscow.  The pair were flying from Fairbanks to Barrow when they encountered fog and low-visibility.  Locating a hole in the fog at Walakpa Bay, they landed.  They spent some time with a small party of Alaska Natives and received directions for the short distance remaining to Barrow.  They were barely airborne, around 50 ft , when the motor failed.  The aircraft plummeted into the lagoon and overturned.  It was the first fatal air accident Barrow had known.

Weeks Field: Weeks Field was the first airport for Fairbanks, Alaska, existing from 1923 to 1951, when most operations were moved to Fairbanks International Airport.  In later years, the term Weeks Field came to be known for neighborhoods of Fairbanks in the path and vicinity of the former airstrip.  Most of the area became a city (later borough) park and residential areas, with the few surviving buildings serving mostly commercial functions.

Everts Air: Everts Air is an American airline based in Fairbanks, Alaska, USA.  It operates scheduled and charter airline cargo as well as passenger services within Alaska and Canada.  Its main base is Fairbanks International Airport with its major hub at Ted Stevens Anchorage International Airport.

Fairbanks International Airport: Fairbanks International Airport (IATA: FAI, ICAO: PAFA, FAA LID: FAI) is a state-owned public-use airport located three miles (5 km) southwest of the central business district of Fairbanks, a city in the Fairbanks North Star Borough of the United States state of Alaska.  Fairbanks is the smallest city in the United States with non-stop service to Europe, as Condor offers weekly flights to Frankfurt during the summer tourist season.  In addition, Air North is another international airline with flights (to Canada) and Antonov Airlines offers cargo flights to South Korea.

Question: Fairbanks International Airport and Wiley Post–Will Rogers Memorial Airport, are located in which U.S. state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "description": "List of airports mentioned in the question and their locations.",
      "items": {
        "type": "object",
        "properties": {
          "airport_name": {
            "type": "string",
            "description": "The name of the airport."
          },
          "location_state": {
            "type": "string",
            "description": "The U.S. state where the airport is located."
          }
        },
        "required": [
          "airport_name",
          "location_state"
        ],
        "additionalProperties": false
      }
    },
    "common_state": {
      "type": "string",
      "description": "The U.S. state common to all listed airports."
    },
    "number_of_airports_found": {
      "type": "integer",
      "description": "The count of airports whose location was identified."
    }
  },
  "required": [
    "airports",
    "common_state",
    "number_of_airports_found"
  ],
  "additionalProperties": false
}
