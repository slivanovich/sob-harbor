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
Elizabeth City Regional Airport: Elizabeth City Regional Airport (IATA: ECG, ICAO: KECG, FAA LID: ECG) is a joint civil-military public and military use airport located three nautical miles (6 km) southeast of the central business district of Elizabeth City, in Pasquotank County, North Carolina, United States.  The airport, on the shore of the Pasquotank River, is also known as Elizabeth City-Pasquotank County Regional Airport or ECG Regional Airport.  It is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.

Columbia Regional Airport: Columbia Regional Airport (IATA: KCOU, ICAO: COU) is a public city owned airport located about 10 nautical miles (12 mi, 19 km) southeast of the central business district of Columbia in Boone County, Missouri, United States.  The only commercial airport in the region of Mid-Missouri, it is served by two commercial airlines and also provides general aviation services.  Airport officials have created a plan to extend the 6,500 foot runway, and to construct a new terminal.  The runway will be extended first, with the terminal reconstruction to take place two years later.

Ralph Wien Memorial Airport: Ralph Wien Memorial Airport (IATA: OTZ, ICAO: PAOT, FAA LID: OTZ) is a state-owned public-use airport located one nautical mile (1.85 km) south of the central business district of Kotzebue, a city on the Baldwin Peninsula in the Northwest Arctic Borough of the U.S. state of Alaska.

John F. Kennedy Memorial Airport: John F. Kennedy Memorial Airport (IATA: ASX, ICAO: KASX, FAA LID: ASX) is a city and county owned public use airport located two nautical miles (4 km) southwest of the central business district of Ashland, a city in Ashland County, Wisconsin, United States.  It is also known as JFK Memorial Airport.

Norfolk Regional Airport: Norfolk Regional Airport (IATA: OFK, ICAO: KOFK, FAA LID: OFK) (Karl Stefan Memorial Field) is four miles southwest of Norfolk, in Madison County, Nebraska.  The airport is named for Karl Stefan, a local newspaper editor and radio announcer who served several terms in the United States Congress.  Until March 2011 it was known as Karl Stefan Memorial Airport.  The FAA's National Plan of Integrated Airport Systems for 2011–2015 categorized it as a "general aviation" facility.

Bering Air: Bering Air is an American airline headquartered in Nome, Alaska, USA.  It operates domestic scheduled passenger and charter airline services, as well as air ambulance and helicopter services.  Its main base is Nome Airport, with hubs at Ralph Wien Memorial Airport (Kotzebue) and Unalakleet Airport

Peach State Airport: Alexander Memorial Airport (FAA LID: GA2) , also known as Peach State Aerodrome or Candler Field, is a public grass strip located 1 mile (1.6 km) west of Williamson, Georgia, in the United States.  Alexander Memorial Airport is located in picturesque rural Pike County, 27 nautical miles (50 km) south of Hartsfield-Jackson Atlanta International Airport.

Friedman Memorial Airport: Friedman Memorial Airport (IATA: SUN, ICAO: KSUN, FAA LID: SUN) is a city-owned public-use airport in the northwest United States, located one nautical mile (2 km) southeast of the central business district of Hailey, the county seat of Blaine County, Idaho.  The airport is operated by the Friedman Memorial Airport Authority under a Joint Powers Agreement between the city of Hailey and Blaine County.  It serves the resort communities of Sun Valley and Ketchum, and the surrounding areas in the Wood River Valley.

Sedalia Regional Airport: Sedalia Regional Airport (IATA: DMO, ICAO: KDMO, FAA LID: DMO) is a city owned, public use airport located two nautical miles (4 km) east of the central business district of Sedalia, a city in Pettis County, Missouri, United States.  It was formerly known as Sedalia Memorial Airport.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.

West Kootenay Regional Airport: The West Kootenay Regional Airport, (Castlegar Airport) (IATA: YCG, ICAO: CYCG) is a small regional airport located 2 NM south southeast of Castlegar, British Columbia, Canada.  It is owned and operated by the City of Castlegar, and has a 15317 sqft passenger terminal.  Due to the mountainous terrain impinging on both runway approaches, there is no possibility of a straight-in approach.  The airport is therefore certified for day operations only, and the glideslope on approach is set to a steep 5.0° rather than the standard 3.0°.  The instrument approaches to Castlegar are considered among the most challenging of any in use at a commercial airport in North America.  As of 2011, the Dash-8s serving the airport required minimums of 3400 foot cloud ceilings and three miles visibility (Air Canada Jazz adds 100 feet and one mile to these minimums).

Question: Are Ralph Wien Memorial Airport and Columbia Regional Airport in the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airports": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "airport_name": {
            "type": "string"
          },
          "country": {
            "type": "string"
          }
        },
        "required": [
          "airport_name",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "are_in_same_country": {
      "type": "boolean"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "airports",
    "are_in_same_country",
    "reasoning"
  ],
  "additionalProperties": false
}
