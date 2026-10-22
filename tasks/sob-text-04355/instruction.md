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
Grand Island Army Air Field: Grand Island Army Airfield (IATA: GRI, ICAO: KGRI, FAA LID: GRI) was a United States Army Air Forces airfield which operated from 1942 to 1946.  After its closure, the base was reopened as Central Nebraska Regional Airport.

KOLN: KOLN, virtual and VHF digital channel 10, is the CBS-affiliated television station licensed to Lincoln, Nebraska, United States.  Owned by Gray Television, KOLN serves a large swath of southeast and central Nebraska through a large network of translator stations.  The station also operates a full-power semi-satellite, KGIN (virtual and VHF digital channel 11) in Grand Island, which serves the central portion of the market; KOLN and KGIN's on-air branding of 10/11 represents these two full-powered signals.  Combined, the two stations serve one of the largest coverage areas in the United States, stretching across 42 counties in southern and central Nebraska—almost two-thirds of the state's land mass—and an additional four counties in Kansas.  The station's studios are located on North 40th Street in Lincoln, with a central Nebraska bureau located on North Locust Street in Grand Island.  KOLN's transmitter is southeast of Goehner, while KGIN's transmitter is near Heartwell.

Unalaska, Alaska: Unalaska (Aleut: "Iluulux̂") is the largest city of the Aleutian Islands.  The city is in the Aleutians West Census Area, a regional component of the Unorganized Borough in the U.S. state of Alaska.  Unalaska is located on Unalaska Island and neighboring Amaknak Island in the Aleutian Islands off mainland Alaska.  The population was 4,376 at the 2010 census, which is 79% of the entire Aleutians West Census Area.  Unalaska is the second-largest city in the Unorganized Borough, behind Bethel.

Central Nebraska Regional Airport: Central Nebraska Regional Airport (IATA: GRI, ICAO: KGRI, FAA LID: GRI) is three miles northeast of Grand Island, in Hall County, Nebraska.  It is owned by the Hall County Airport Authority.  The airport sees two airlines, subsidized by the Essential Air Service program.

Sitka Spruce Park: Sitka Spruce Park is a public park in the city of Unalaska, Alaska.  The roughly 5 acre park is located on Biorka Drive on Amaknak Island, south of Unalaska Airport.  It is one of the few places on the island where there are a significant number of trees.  A small part of the park is a National Historic Landmark, as it was the site of the earliest documented afforestation in North America.  In 1805, Russian agents planted an unknown number of Sitka spruce trees in the area, of which six were documented to be surviving in 1978.

Nebraska Highway 39: Nebraska Highway 39 is a highway in central Nebraska.  It runs for a length of 42.05 mi .  It has a southern terminus west of Osceola at an intersection with Nebraska Highway 92.  Its northern terminus is at an intersection with Nebraska Highway 14 southeast of Albion.

Nebraska Highway 21: Nebraska Highway 21 is a highway in central Nebraska.  Its southern terminus is at Nebraska Highway 23 east of Eustis.  Its northern terminus is at an intersection with Nebraska Highway 2 and Nebraska Highway 92 in Broken Bow.

Unalaska Airport: Tom Madsen (Dutch Harbor) Airport (IATA: DUT, ICAO: PADU, FAA LID: DUT) is a state owned, public use airport in City of Dutch Harbor, on Amaknak Island in the Aleutian Islands, off the coast of the U.S. state of Alaska.  It is located near the Bering Sea coast of Unalaska Island, 800 mi southwest of Anchorage and 1950 mi from Seattle.

Western Nebraska Regional Airport: Western Nebraska Regional Airport (IATA: BFF, ICAO: KBFF, FAA LID: BFF) (William B. Heilig Field) is three miles east of Scottsbluff, in Scotts Bluff County, Nebraska.  The airport is owned by the Airport Authority of Scotts Bluff County.  It sees one passenger airline, subsidized by the Essential Air Service program.

Nebraska Highway 70: Nebraska Highway 70 is a highway in central Nebraska.  Its western terminus is at an intersection with Nebraska Highway 2 and Nebraska Highway 92 east of Broken Bow.  Its eastern terminus is at Nebraska Highway 14 in Elgin.

Question: Which airport is closer to west Nebraska, Unalaska Airport or Central Nebraska Regional Airport?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "closest_airport_name": {
      "type": "string",
      "description": "The name of the airport closer to west Nebraska."
    },
    "closest_airport_location": {
      "type": "string",
      "description": "The location of the airport closer to west Nebraska."
    },
    "other_airport_name": {
      "type": "string",
      "description": "The name of the other airport mentioned in the question."
    },
    "other_airport_location": {
      "type": "string",
      "description": "The location of the other airport."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why one airport is closer than the other."
    }
  },
  "required": [
    "closest_airport_name",
    "closest_airport_location",
    "other_airport_name",
    "other_airport_location",
    "reasoning"
  ],
  "additionalProperties": false
}
