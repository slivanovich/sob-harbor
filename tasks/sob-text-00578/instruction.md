{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPierre Regional Airport: Pierre Regional Airport (IATA: PIR, ICAO: KPIR, FAA LID: PIR) is a city owned, public airport three miles east of Pierre, in Hughes County, South Dakota, United States.  The airport was served by two airlines until January 31, 2012 when Delta Air Lines regional affiliate Delta Connection ceased all service.  Great Lakes Airlines now flies both east and west via interline agreements with Delta Air Lines, Frontier Airlines and United Airlines.\n\nPensacola International Airport: Pensacola International Airport (IATA: PNS, ICAO: KPNS, FAA LID: PNS) , formerly Pensacola Gulf Coast Regional Airport and Pensacola Regional Airport (Hagler Field), is a public use airport three nautical miles (6 km) northeast of the central business district of Pensacola, in Escambia County, Florida, United States.  It is owned by the City of Pensacola.  Despite the name, this airport does not offer direct international flights.  This airport is one of the five major airports in North Florida, others being: Northwest Florida Beaches International Airport, Destin-Fort Walton Beach Airport Tallahassee International Airport, and Jacksonville International Airport.\n\nGrand Junction Regional Airport: Grand Junction Regional Airport (IATA: KGJT, ICAO: GJT) is a public airport three miles northeast of Grand Junction, in Mesa County, Colorado.  Owned by the Grand Junction Regional Airport Authority, it is the largest airport in western Colorado and third largest in the state, behind Denver International Airport and Colorado Springs Airport.\n\nNorthern Aroostook Regional Airport: Northern Aroostook Regional Airport (IATA: WFK, ICAO: KFVE, FAA LID: FVE) is a public airport three miles (5 km) east of the central business district of Frenchville, a town in Aroostook County, Maine, United States.  It is owned by the Northern Aroostook Regional Airport Authority.\n\nYeager Airport: Yeager Airport (IATA: CRW, ICAO: KCRW, FAA LID: CRW) is a public airport three miles (6 km) east of downtown Charleston, in Kanawha County, West Virginia, United States.  It is owned by the Central West Virginia Regional Airport Authority.  The airport hosts McLaughlin Air National Guard Base, home to nine C-130 Hercules aircraft of the West Virginia Air National Guard's 130th Airlift Wing (130 AW), an Air Mobility Command (AMC)-gained unit of the West Virginia Air National Guard.\n\nEastern WV Regional Airport: The Eastern West Virginia Regional Airport (IATA: MRB, ICAO: KMRB, FAA LID: MRB) , also known as Shepherd Field, is a civilian-owned, public use airport located four nautical miles (5 mi, 7 km) south of the central business district of Martinsburg, a city in Berkeley County, West Virginia, United States.  It is owned by the Eastern West Virginia Regional Airport Authority or EWVRAA.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, in which the Federal Aviation Administration categorized it as a \"reliever airport\".\n\nSt. George Regional Airport: St. George Regional Airport (IATA: SGU, ICAO: KSGU, FAA LID: SGU) is a city-owned, public-use airport located five nautical miles (5.8 miles; 9.3 km) southeast of the central business district of St. George, a city in Washington County, Utah, United States.\n\nReading Regional Airport: Reading Regional Airport (IATA: RDG, ICAO: KRDG, FAA LID: RDG) (also known as Carl A. Spaatz Field) is a public airport three miles (5 km) northwest of Reading, in Berks County, Pennsylvania.  It is owned by the Reading Regional Airport Authority.\n\nGreenbrier Valley Airport: Greenbrier Valley Airport (IATA: KLWB, ICAO: LWB) is a public airport three miles (5 km) north of Lewisburg in Greenbrier County, West Virginia, United States.  It has one runway and is owned by the Greenbrier County Airport Authority.  Silver Airways (\"United Express\") has scheduled airline flights, subsidized by the Essential Air Service program, to Washington-Dulles International Airport, which replaced Cleveland-Hopkins International Airport in summer 2012.  Silver Airways also flies to Atlanta-Hartsfield International Airport as an independent airline, replacing Delta Connection.\n\nEastern Oregon Regional Airport: Eastern Oregon Regional Airport (IATA: PDT, ICAO: KPDT, FAA LID: PDT) (Eastern Oregon Regional Airport at Pendleton) is a city-owned public airport three miles northwest of Pendleton, in Umatilla County, Oregon.  It is used for general aviation and by one airline subsidized by the Essential Air Service program.\n\nQuestion: Which airport, Yeager Airport or St. George Regional Airport,  is a public airport three miles (6 km) east of downtown Charleston, West Virginia?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airport that matches the description.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"distance_miles\": {\n          \"type\": \"integer\",\n          \"description\": \"The distance from the city center in miles.\"\n        },\n        \"distance_km\": {\n          \"type\": \"integer\",\n          \"description\": \"The distance from the city center in kilometers.\"\n        },\n        \"direction\": {\n          \"type\": \"string\",\n          \"description\": \"The direction from the city center.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city the airport serves.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the airport is located.\"\n        }\n      },\n      \"required\": [\n        \"distance_miles\",\n        \"distance_km\",\n        \"direction\",\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_public_airport\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the airport is a public airport.\"\n    }\n  },\n  \"required\": [\n    \"airport_name\",\n    \"location_details\",\n    \"is_public_airport\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airport_name": {
        "type": "string",
        "description": "The name of the airport that matches the description."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "distance_miles": {
            "type": "integer",
            "description": "The distance from the city center in miles."
          },
          "distance_km": {
            "type": "integer",
            "description": "The distance from the city center in kilometers."
          },
          "direction": {
            "type": "string",
            "description": "The direction from the city center."
          },
          "city": {
            "type": "string",
            "description": "The city the airport serves."
          },
          "state": {
            "type": "string",
            "description": "The state where the airport is located."
          }
        },
        "required": [
          "distance_miles",
          "distance_km",
          "direction",
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "is_public_airport": {
        "type": "boolean",
        "description": "Indicates if the airport is a public airport."
      }
    },
    "required": [
      "airport_name",
      "location_details",
      "is_public_airport"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
