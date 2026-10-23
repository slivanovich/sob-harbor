{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThomas A. Burke: Thomas Aloysius Burke (October 30, 1898December 5, 1971) was a Democratic Party politician from Ohio.  He served as the 48th mayor of Cleveland, Ohio and in the United States Senate from November 10, 1953 until December 2, 1954.  Cleveland Burke Lakefront Airport is named after him.\n\n1998 Medic Drug Grand Prix of Cleveland: The 1998 Medic Drug Grand Prix of Cleveland was the tenth round of the 1998 CART FedEx Champ Car World Series season, held on July 12, 1998, at the Burke Lakefront Airport in Cleveland, Ohio.  The race, once again was won by defending champion Alex Zanardi, who dominated the race once he passed his teammate and polesitter Jimmy Vasser (who was suffering from gearbox problems) on a restart.  The win was Zanardi's third consecutive of the season.\n\nLake Erie: Lake Erie ( ; French: \"Lac Érié\" ) is the fourth-largest lake (by surface area) of the five Great Lakes in North America, and the thirteenth-largest globally if measured in terms of surface area.  It is the southernmost, shallowest, and smallest by volume of the Great Lakes and therefore also has the shortest average water residence time.  At its deepest point Lake Erie is 210 ft deep.\n\nCleveland National Air Show: The Cleveland National Air Show is an annual air show held on Labor Day weekend at Burke Lakefront Airport in Cleveland, Ohio.  It was established in 1964 as an indirect successor to the National Air Races.  The show includes stunt airplanes, modern fighters and alternates between the U.S. Navy Blue Angels and U.S. Air Force Thunderbirds every other year.  The show typically runs from 9:00 a.m. to around 6:00 p.m. EDT.  The show usually starts with smaller acts, and the Blue Angels or Thunderbirds perform last.  Another regular attraction is the NASA Glenn Research Center, which usually has an exhibit located near the back of the show.  There is usually some type of heritage or legacy flight, sometimes both.\n\nNorth Coast Harbor: North Coast Harbor is a district in downtown Cleveland, Ohio on the shore of Lake Erie.  The district serves as the home of the Great Lakes Science Center, the Rock and Roll Hall of Fame and Museum, FirstEnergy Stadium, the Steamship William G. Mather Maritime Museum, the USS \"Cod\", Burke Lakefront Airport, Voinovich Bicentennial Park, and the Cleveland-Cuyahoga County Port Authority.  It is served by the West 3rd and North Coast stations on RTA's light rail Waterfront Line.\n\nCleveland Burke Lakefront Airport: Cleveland Burke Lakefront Airport (IATA: BKL, ICAO: KBKL, FAA LID: BKL) is a public airport on the shore of Lake Erie, in the northeast part of downtown Cleveland, Ohio, United States.  It classified as a general aviation airport and is an FAA designated reliever to Cleveland Hopkins International Airport (CLE), which is Greater Cleveland's primary airport.  In 2008, based on FAA data, Burke Lakefront was the fourth busiest airport in the state of Ohio after, Cleveland Hopkins, Port Columbus International and Akron-Canton, up from 7th in 2007.  It is named after former Cleveland mayor and U.S. senator Thomas A. Burke.\n\n2003 U.S. Bank Cleveland Grand Prix: The 2003 U.S. Bank Cleveland Grand Prix was the ninth round of 18 of the 2003 CART World Series season, held on July 5, 2003 at Burke Lakefront Airport in Cleveland, Ohio.  It was the first road course race to be held at night in CART history.\n\nPremier Flight Academy: Premier Flight Academy is an aviation school located in Cleveland at Cleveland Burke Lakefront Airport.  Premier Flight Academy offers a wide range of Part 61 courses as well as a Federal Aviation Administration and University Certified Part 141 International pilot training course.\n\n1999 Medic Drug Grand Prix of Cleveland: The 1999 Medic Drug Grand Prix of Cleveland was the ninth round of the 1999 CART FedEx Champ Car World Series season, held on June 27, 1999, at the Burke Lakefront Airport in Cleveland, Ohio.\n\nCleveland Hopkins International Airport: Cleveland Hopkins International Airport (IATA: CLE, ICAO: KCLE, FAA LID: CLE) is a public airport located nine miles (14 km) southwest of the central business district of Cleveland, Cuyahoga County, Ohio, United States.  It is the primary airport serving Northeast Ohio and is the largest and busiest airport in the state of Ohio.  The metropolitan area is also served by Burke Lakefront Airport and by Akron-Canton Regional Airport.  Cleveland Hopkins International Airport and Cleveland Burke Lakefront Airport together comprise the Cleveland Airport System, operated by the City of Cleveland's Department of Port Control.\n\nQuestion: Cleveland Burke Lakefront Airport is on the shores of which fourth-largest Great Lake?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airport_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airport in question.\"\n    },\n    \"lake_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Great Lake the airport is located on.\"\n    },\n    \"lake_properties\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"size_rank_great_lakes\": {\n          \"type\": \"integer\",\n          \"description\": \"The rank of the lake by surface area among the Great Lakes.\"\n        },\n        \"size_metric\": {\n          \"type\": \"string\",\n          \"description\": \"The metric used for ranking the lake's size.\"\n        }\n      },\n      \"required\": [\n        \"size_rank_great_lakes\",\n        \"size_metric\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"airport_location_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the airport's location relative to the lake.\"\n    },\n    \"city_state\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the airport is located.\"\n    }\n  },\n  \"required\": [\n    \"airport_name\",\n    \"lake_name\",\n    \"lake_properties\",\n    \"airport_location_description\",\n    \"city_state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airport_name": {
        "type": "string",
        "description": "The name of the airport in question."
      },
      "lake_name": {
        "type": "string",
        "description": "The name of the Great Lake the airport is located on."
      },
      "lake_properties": {
        "type": "object",
        "properties": {
          "size_rank_great_lakes": {
            "type": "integer",
            "description": "The rank of the lake by surface area among the Great Lakes."
          },
          "size_metric": {
            "type": "string",
            "description": "The metric used for ranking the lake's size."
          }
        },
        "required": [
          "size_rank_great_lakes",
          "size_metric"
        ],
        "additionalProperties": false
      },
      "airport_location_description": {
        "type": "string",
        "description": "A description of the airport's location relative to the lake."
      },
      "city_state": {
        "type": "string",
        "description": "The city and state where the airport is located."
      }
    },
    "required": [
      "airport_name",
      "lake_name",
      "lake_properties",
      "airport_location_description",
      "city_state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
