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
Schuylkill County Airport: Schuylkill County Airport (ICAO: KZER, FAA LID: ZER) , also known as Schuylkill County Joe Zerbey Airport, is a public use airport located eight nautical miles (9 mi, 15 km) west of the central business district of Pottsville, a city in Schuylkill County, Pennsylvania, United States.  It is owned by the Schuylkill County Airport Authority.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.

Crawford County Airport: Crawford County Airport (ICAO: KRSV, FAA LID: RSV) is a public use airport located four nautical miles (5 mi, 7 km) east of the central business district of Robinson, a city in Crawford County, Illinois, United States.  It is owned by the Crawford County Airport Authority and was formerly known as Robinson Municipal Airport.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.

St. Mary's Airport (Alaska): St. Mary's Airport (IATA: KSM, ICAO: PASM, FAA LID: KSM) is a public airport located four miles (6 km) west of the central business district of St. Mary's, in the Kusilvak Census Area of the U.S. state of Alaska.  This airport is publicly owned by the State of Alaska Department of Transportation and Public Facilities (DOT&PF) - Northern Region.

Modesto City–County Airport: Modesto City–County Airport (IATA: MOD, ICAO: KMOD, FAA LID: MOD) (Harry Sham Field) is two miles (3 km) southeast of Modesto in Stanislaus County, California, USA.

St. Clair County Airport: St. Clair County Airport (IATA: PLR, ICAO: KPLR, FAA LID: PLR) is a public use airport located three nautical miles (6 km) southeast of the central business district of Pell City, in St. Clair County, Alabama, United States.  It is owned by the St. Clair County Airport Authority.  According to the FAA's National Plan of Integrated Airport Systems for 2009–2013, it is categorized as a "reliever airport" for the Birmingham-Shuttlesworth International Airport.

St. Mary's County Regional Airport: St. Mary's County Regional Airport (IATA: LTW, FAA LID: 2W6) , also known as Captain Walter Francis Duke Regional Airport, is a public airport located in St. Mary's County, Maryland, four miles (six km) northeast of the central business district of Leonardtown.  The airport is also located 8 nmi west of Naval Air Station Patuxent River.  It is owned and operated by the St. Mary's County Board of County Commissioners.

Atlanta South Regional Airport: Henry County Airport (FAA LID: KHMP) , is a public-use county airport located three nautical miles (6 km) west of the central business district of Hampton, a city in Henry County, Georgia, United States.  It was known as Clayton County Airport – Tara Field, which was the name still used by the Federal Aviation Administration (FAA) and the Georgia Department of Transportation (GDOT) until approval of the Atlanta South Regional Airport name.  The airport was renamed Atlanta South Regional Airport, which was approved by the airport board of commissioners in December 2011, and was approved by the GDOT and the FAA before it went into effect.

Greater Portsmouth Regional Airport: Greater Portsmouth Regional Airport (IATA: PMH, ICAO: KPMH, FAA LID: PMH) , also known as Scioto County Airport, is a public use airport located on State Route 335 in the community of Minford, Ohio, 10 nautical miles (12 mi, 19 km) northeast of the central business district of Portsmouth, a city in Scioto County, Ohio, United States.  It is owned by the Scioto County Airport Authority.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.

Clinton–Sampson County Airport: Clinton–Sampson County Airport (IATA: CTZ, ICAO: KCTZ, FAA LID: CTZ) is a public use airport located two nautical miles (4 km) southwest of the central business district of Clinton, a city in Sampson County, North Carolina, United States.  It is owned by the city and county.  This airport is included in the National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a "general aviation" facility.  It was formerly known as Sampson County Airport.

Modesto City Schools: Modesto City School District is a public school district based in Stanislaus County, California, United States, with an enrollment of approximately 32,000 students.  Founded in 1871, the district consists of an elementary district and a high school district with a common administration.  Seven other school districts feed into Modesto City Schools at the high school level.

Question: Are both Modesto City–County Airport and St. Mary's Airport located in the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airports_checked": {
      "type": "array",
      "description": "List of airports whose location was verified.",
      "items": {
        "type": "object",
        "properties": {
          "airport_name": {
            "type": "string",
            "description": "The name of the airport."
          },
          "is_located_in_usa": {
            "type": "boolean",
            "description": "Indicates if the airport is located in the United States."
          },
          "state_or_county": {
            "type": "string",
            "description": "The state or county where the airport is located within the USA."
          }
        },
        "required": [
          "airport_name",
          "is_located_in_usa",
          "state_or_county"
        ],
        "additionalProperties": false
      }
    },
    "all_airports_in_usa": {
      "type": "boolean",
      "description": "True if all specified airports are located in the United States, false otherwise."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of the conclusion based on the locations found."
    }
  },
  "required": [
    "airports_checked",
    "all_airports_in_usa",
    "reasoning"
  ],
  "additionalProperties": false
}
