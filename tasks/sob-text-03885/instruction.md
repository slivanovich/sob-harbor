{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMonroe County Airport (Alabama): Monroe County Airport (IATA: MVC, ICAO: KMVC, FAA LID: MVC) is a county-owned public-use airport located three nautical miles (6 km) south of the central business district of Monroeville, in Monroe County, Alabama, United States.  According to the FAA's National Plan of Integrated Airport Systems for 2009–2013, it is categorized as a \"general aviation\" facility.\n\nLittle River Airport: Little River Airport (ICAO: KLLR) is a small county-owned public-use airport located three nautical miles (6 km) southeast of the central business district of Little River, in Mendocino County, California, United States.\n\nBeatty Airport: Beatty Airport (IATA: BTY, ICAO: KBTY, FAA LID: BTY) is a county-owned public-use airport located three nautical miles (6 km) southwest of the central business district of Beatty, a town in Nye County, Nevada, United States.\n\nWoodward Field (airport): Woodward Field (IATA: CDN, ICAO: KCDN, FAA LID: CDN) is a county-owned public-use airport located three nautical miles (6 km) northeast of the central business district of Camden, a city in Kershaw County, South Carolina, United States.  It is also known as the Kershaw County Airport.  The airport serves the general aviation community, with no scheduled commercial airline service.\n\nGreene County Regional Airport: Greene County Regional Airport (FAA LID: 3J7) is a county-owned public-use airport located three nautical miles (6 km) northeast of the central business district of Greensboro, a city in Greene County, Georgia, United States.  As per the FAA's National Plan of Integrated Airport Systems for 2009-2013, it is classified as a \"general aviation\" airport.\n\nDavis Field (Georgia): Davis Field (FAA LID: 3J6) is a county-owned public-use airport located three nautical miles (6 km) southwest of the central business district of Folkston, a city in Charlton County, Georgia, United States.\n\nSullivan County Airport: Sullivan County Airport (IATA: SIV, ICAO: KSIV, FAA LID: SIV) is a county-owned public-use airport located three nautical miles (6 km) northwest of the central business district of Sullivan, a city in Sullivan County, Indiana, United States.  It is included in the FAA's National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a \"general aviation\" facility.\n\nMyrtle Beach International Airport: Myrtle Beach International Airport (IATA: MYR, ICAO: KMYR, FAA LID: MYR) is a county-owned public-use airport located three nautical miles (6 km) southwest of the central business district of Myrtle Beach, in Horry County, South Carolina, United States.  It was formerly known as Myrtle Beach Jetport (1974–1989) and is located on site of the former Myrtle Beach Air Force Base, which also includes The Market Common shopping complex.\n\nBeatty, Nevada: Beatty (pronounced BAY-dee) is an unincorporated town along the Amargosa River in Nye County in the U.S. state of Nevada.  U.S. Route 95 runs through the town, which lies between Tonopah, about 90 mi to the north, and Las Vegas, about 120 mi to the southeast.  State Route 374 connects Beatty to Death Valley National Park, about 8 mi to the west.\n\nPlacerville Airport: Placerville Airport (IATA: PVF, ICAO: KPVF, FAA LID: PVF) is a county-owned public-use airport located three nautical miles (6 km) east of the central business district of Placerville, in El Dorado County, California, United States.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a \"general aviation\" airport.\n\nQuestion: Beatty Airport is a county-owned public-use airport located three nautical miles (6 km) southwest of the central business district of which unincorporated town along the Amargosa River in Nye County in the U.S. state of Nevada?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airport.\"\n    },\n    \"town_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"town_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the unincorporated town.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the town is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The U.S. state where the town is located.\"\n        },\n        \"is_unincorporated\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the town is unincorporated.\"\n        },\n        \"river_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the river the town is along.\"\n        }\n      },\n      \"required\": [\n        \"town_name\",\n        \"county\",\n        \"state\",\n        \"is_unincorporated\",\n        \"river_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"airport_location_relative_to_town\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"distance_nautical_miles\": {\n          \"type\": \"integer\",\n          \"description\": \"The distance from the town's central business district to the airport in nautical miles.\"\n        },\n        \"distance_km\": {\n          \"type\": \"integer\",\n          \"description\": \"The distance from the town's central business district to the airport in kilometers.\"\n        },\n        \"relative_direction_from_town_cbd\": {\n          \"type\": \"string\",\n          \"description\": \"The direction of the airport relative to the town's central business district.\"\n        }\n      },\n      \"required\": [\n        \"distance_nautical_miles\",\n        \"distance_km\",\n        \"relative_direction_from_town_cbd\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"airport_name\",\n    \"town_details\",\n    \"airport_location_relative_to_town\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airport_name": {
        "type": "string",
        "description": "The name of the airport."
      },
      "town_details": {
        "type": "object",
        "properties": {
          "town_name": {
            "type": "string",
            "description": "The name of the unincorporated town."
          },
          "county": {
            "type": "string",
            "description": "The county where the town is located."
          },
          "state": {
            "type": "string",
            "description": "The U.S. state where the town is located."
          },
          "is_unincorporated": {
            "type": "boolean",
            "description": "Indicates if the town is unincorporated."
          },
          "river_name": {
            "type": "string",
            "description": "The name of the river the town is along."
          }
        },
        "required": [
          "town_name",
          "county",
          "state",
          "is_unincorporated",
          "river_name"
        ],
        "additionalProperties": false
      },
      "airport_location_relative_to_town": {
        "type": "object",
        "properties": {
          "distance_nautical_miles": {
            "type": "integer",
            "description": "The distance from the town's central business district to the airport in nautical miles."
          },
          "distance_km": {
            "type": "integer",
            "description": "The distance from the town's central business district to the airport in kilometers."
          },
          "relative_direction_from_town_cbd": {
            "type": "string",
            "description": "The direction of the airport relative to the town's central business district."
          }
        },
        "required": [
          "distance_nautical_miles",
          "distance_km",
          "relative_direction_from_town_cbd"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "airport_name",
      "town_details",
      "airport_location_relative_to_town"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
