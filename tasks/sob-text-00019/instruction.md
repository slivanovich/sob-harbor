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
Wittman Regional Airport: Wittman Regional Airport (IATA: OSH, ICAO: KOSH, FAA LID: OSH) is a county owned public use airport located two nautical miles (4 km) south of the central business district of Oshkosh, a city in Winnebago County, Wisconsin, United States.  It is located adjacent to Pioneer Airport, part of the EAA Aviation Museum.  The airport was named after pioneer air racer, aircraft designer and builder Steve Wittman in 1972.  Originally named "Winnebago County Airport", the name "Steve Wittman Field" was proposed in 1968 and it is also known as Wittman Field.  It is included in the Federal Aviation Administration (FAA) National Plan of Integrated Airport Systems for 2017–2021, in which it is categorized as a regional general aviation facility.

Sand Point Airport: Sand Point Airport (IATA: SDP, ICAO: PASD, FAA LID: SDP) is a state owned, public use airport located two nautical miles (4 km) southwest of the central business district of Sand Point, a city in the Aleutians East Borough in the U.S. state of Alaska.  Scheduled airline service to Anchorage International Airport is provided by Peninsula Airways (PenAir).

Columbia Gorge Regional Airport: Columbia Gorge Regional Airport (IATA: DLS, ICAO: KDLS, FAA LID: DLS) , also referred to as The Dalles Municipal Airport, is a public use airport in Klickitat County in the U.S. state of Washington.  It is located near Dallesport, Washington and two nautical miles (4 km) northeast of the city of The Dalles in the state of Oregon.  The airport is jointly owned by the city of The Dalles and Klickitat County.  It is adjacent to the Columbia River, near the east end of the Columbia River Gorge National Scenic Area.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.

Mayor of Kalawao County: The Mayor of Kalawao County is the chief executive officer of Kalawao County in the U.S. state of Hawaii.  Kalawao County, which lacks a local government, is administered by the Hawaii Department of Health.  Under Hawaii state law, the Director of the Hawaii Department of Health, who is appointed by the Governor of Hawaii, simultaneously serves as the Mayor of Kalawao County while in office.  The Mayor of Kalawao County holds executive powers similar to other elected Hawaiian mayors, including the responsibilities of health, public safety and law and order.  The Mayor appoints a county sheriff selected from Kalawao County residents.  He or she visits Kalawao several times a year to meet with local residents.  Kalawao County, which is located on the Kalaupapa Peninsula on the north coast of Moloka'i, consists of three villages - Kalaupapa, Kalawao, and Waikolu.

Louisa County Airport: Louisa County Airport (IATA: LOW, ICAO: KLKU, FAA LID: LKU) , also known as Freeman Field, is a public use airport located two nautical miles (4 km) southeast of the central business district of Louisa, a town in Louisa County, Virginia, United States.  Although most U.S. airports use the same three-letter location identifier for the FAA and IATA, this airport is assigned LKU by the FAA and LOW by the IATA.

Southwest Michigan Regional Airport: Southwest Michigan Regional Airport (IATA: BEH, ICAO: KBEH, FAA LID: BEH) is a public use airport located two nautical miles (4 km) northeast of the central business district of Benton Harbor, a city in Berrien County, Michigan, United States.  The airport is owned by the cities of Benton Harbor and St. Joseph, Michigan.  It is included in the Federal Aviation Administration (FAA) National Plan of Integrated Airport Systems for 2017–2021, in which it is categorized as a regional general aviation facility.

Kalaupapa, Hawaii: Kalaupapa is a small unincorporated community on the island of Molokaʻ i, within Kalawao County in the U.S. state of Hawaii.  In 1866, during the reign of Kamehameha V, the Hawaii legislature passed a law that resulted in the designation of Molokaʻ i as the site for a leper colony, where seriously affected patients could be quarantined, to prevent them from infecting others.  At the time, the disease was little understood: it was believed to be highly contagious and incurable.  In the communities where people with leprosy lived and were treated were under the administration of the Board of Health, which appointed superintendents on the island.

Kalawao County, Hawaii: Kalawao County is a county located in the U.S. state of Hawaii.  The county encompasses the Kalaupapa or Makanalua Peninsula, on the north coast of the island of Molokaʻ i.  The small peninsula is isolated from the rest of Molokaʻ i by sea cliffs over a quarter-mile high—the only land access is a mule trail.  According to a 2016 census estimate, Kalawao County was the least-populated county in the United States and occupies the least area of any county.

Kalaupapa Airport: Kalaupapa Airport (IATA: LUP, ICAO: PHLU, FAA LID: LUP) is a regional public use airport of the state of Hawaii, located on the northern peninsula of the island of Molokaʻ i, two nautical miles (4 km) north of Kalaupapa Settlement, in Kalawao County.  Most flights to Kalaupapa originate from Molokai Airport or from airports on the other Hawaiian islands by unscheduled air taxis and general aviation.  It is also used as a cargo facility carrying goods for Kalaupapa, which has no road access from the rest of Molokai.

Dillingham Airfield: Dillingham Airfield (IATA: HDH, ICAO: PHDH, FAA LID: HDH) is a public and military use airport located two nautical miles (4 km) west of the central business district of Mokulēʻ ia, in Honolulu County on the North Shore of Oʻ ahu in the U.S. state of Hawaii.  It is operated by the Hawaii Department of Transportation under a 25-year lease from the United States Army.  The airport is primarily used for gliding and sky diving operations, and also houses Civil Air Patrol (CAP) glider aircraft.  Military operations consist largely of night operations for night vision device training and orientation flights for the Air Force Auxiliary (CAP).  This airport is included in the Federal Aviation Administration (FAA) National Plan of Integrated Airport Systems for 2017–2021, in which it is categorized as a basic general aviation facility.

Question: Kalaupapa Airport (IATA: LUP, ICAO: PHLU, FAA LID: LUP) is a regional public use airport of the state of Hawaii, located on the northern peninsula of the island of Molokaʻ i, two nautical miles (4 km) north of which city Settlement, that's a small unincorporated community on the island of Molokaʻ i, within Kalawao County in the U.S. state of Hawaii?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airport_name": {
      "type": "string",
      "description": "The name of the airport."
    },
    "settlement_name": {
      "type": "string",
      "description": "The name of the settlement associated with the airport."
    },
    "distance_from_settlement_km": {
      "type": "integer",
      "description": "The distance of the airport from the settlement in kilometers."
    },
    "relative_direction_from_settlement": {
      "type": "string",
      "description": "The direction of the airport relative to the settlement (e.g., 'north', 'south')."
    },
    "settlement_type": {
      "type": "string",
      "description": "The type of community the settlement is (e.g., 'unincorporated community')."
    },
    "settlement_location": {
      "type": "object",
      "properties": {
        "island": {
          "type": "string",
          "description": "The island where the settlement is located."
        },
        "county": {
          "type": "string",
          "description": "The county where the settlement is located."
        },
        "state": {
          "type": "string",
          "description": "The U.S. state where the settlement is located."
        }
      },
      "required": [
        "island",
        "county",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "airport_name",
    "settlement_name",
    "distance_from_settlement_km",
    "relative_direction_from_settlement",
    "settlement_type",
    "settlement_location"
  ],
  "additionalProperties": false
}
