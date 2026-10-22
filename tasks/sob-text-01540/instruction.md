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
Oconomowoc Lake, Wisconsin: Oconomowoc Lake is a village in Waukesha County, Wisconsin, United States.  Located just outside the City of Oconomowoc, the village includes the residential area encircling Oconomowoc Lake.

Oconomowoc, Wisconsin: Oconomowoc is a city in Waukesha County, Wisconsin, United States.  The name was derived from Coo-no-mo-wauk, the Potawatomi term for "waterfall."  The population was 15,712 at the 2010 census.  The city is partially adjacent to the Town of Oconomowoc and near the village of Oconomowoc Lake, Wisconsin.

Waukesha County Technical College: Waukesha County Technical College (also WCTC) is a technical (community) college in the Waukesha County area, in the U.S. state of Wisconsin.  The college has campuses in Waukesha and Pewaukee.  It is a member of the 16 school Wisconsin Technical College System.

Bugs Moran: Adelard Cunin (August 21, 1893 – February 25, 1957), better known as George 'Bugs' Moran, was a Chicago Prohibition-era gangster.  He was incarcerated three times before turning 21.  On February 14, 1929, in an event that has become known as the Saint Valentine's Day Massacre, seven members of his gang were gunned down in a warehouse, supposedly on the orders of Moran's rival Al Capone.

Waukesha County Airport: 'Waukesha County Airport/Crites Field (IATA: UES, ICAO: KUES, FAA LID: UES) , is a public use airport located two miles (3 km) north of the central business district of Waukesha, a city in Waukesha County, Wisconsin, United States.  It is owned and operated by Waukesha County.  It is included in the Federal Aviation Administration (FAA) National Plan of Integrated Airport Systems for 2017–2021, in which it is categorized as a national reliever aviation facility.

Waukesha County gangsters: In the early 1900s Waukesha County, Wisconsin was a big resort area and vacation spot for people living in Chicago.  Among the people who visited Oconomowoc's for a little rest and relaxation were Chicago's most notorious gangsters, such as Baby Face Nelson, Bugs Moran, John Dillinger and Al Capone.  Wisconsin's heavily wooded areas were perfect for laying low after a job.

Monterey, Wisconsin: Monterey is an unincorporated community located in the town of Oconomowoc, in Waukesha County, Wisconsin, United States.  Monterey is located near Wisconsin Highway 67 4.5 mi north of the city of Oconomowoc.

Oconomowoc (town), Wisconsin: Oconomowoc is a town in Waukesha County, Wisconsin, United States.  The population was 7,451 at the 2000 census.  The City of Oconomowoc and the Villages of Chenequa and Lac La Belle are located partially in the town.  The unincorporated communities of Mapleton, Monterey, and Okauchee Lake, are located in the town.  The unincorporated community of Stone Bank is located partially in the town.

Mapleton, Wisconsin: Mapleton is an unincorporated community located in the town of Oconomowoc, in Waukesha County, Wisconsin, United States.  Mapleton is 5 mi north-northeast of the city of Oconomowoc.

Lac La Belle, Wisconsin: Lac La Belle is a village located mostly in Waukesha County in the U.S. state of Wisconsin.  The population was 290 at the 2010 census.  Of this, 289 were in Waukesha County, and one person was in Jefferson County.  The village is located mostly within the town of Oconomowoc in Waukesha County.  On March 28, 2002, the village annexed a portion of land in the town of Ixonia in Jefferson County.

Question: In the early 1900s Waukesha County, Wisconsin was a big resort area and vacation spot for people living in Chicago, among the people who visited Oconomowoc's for a little rest and relaxation were Chicago's most notorious gangsters, such as Adelard Cunin, better known as George 'Bugs' Moran, was a Chicago Prohibition-era gangster, and was incarcerated three times, before turning what age?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "gangster_name": {
      "type": "string",
      "description": "The birth name of the gangster."
    },
    "alias": {
      "type": "string",
      "description": "The better-known alias of the gangster."
    },
    "era": {
      "type": "string",
      "description": "The historical era the gangster was active in."
    },
    "incarceration_details": {
      "type": "object",
      "properties": {
        "number_of_incarcerations": {
          "type": "integer",
          "description": "The number of times the gangster was incarcerated."
        },
        "age_before_which_incarcerated": {
          "type": "integer",
          "description": "The age before which the incarcerations occurred."
        }
      },
      "required": [
        "number_of_incarcerations",
        "age_before_which_incarcerated"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "gangster_name",
    "alias",
    "era",
    "incarceration_details"
  ],
  "additionalProperties": false
}
