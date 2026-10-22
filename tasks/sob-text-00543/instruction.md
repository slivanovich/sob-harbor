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
Maine State Route 136: State Route 136 (SR 136) is a numbered state highway in Maine, United States.  It begins with SR 125 at the junction of U.S. Route 1 (US 1) in Freeport, and travels to Auburn.  Although it is only approximately 19 mi long, it connects three major Maine commerce areas (Lewiston, Auburn, and Freeport as well as points south).

Maryland Route 136: Maryland Route 136 (MD 136) is a state highway in the U.S. state of Maryland.  The state highway runs 30.04 mi from MD 7 near Abingdon north to MD 23 in Norrisville.  MD 136 is an L-shaped route that connects the communities of Creswell, Churchville, Dublin, and Whiteford in eastern Harford County with each other and with Norrisville in the county's northwestern corner.  The state highway is connected to the cities of Aberdeen and Havre de Grace via its connection with MD 22.  MD 136 is also linked to the county seat of Bel Air from the east through MD 22, from the northeast by U.S. Route 1 (US 1), from the north via MD 24, and from the northwest by MD 23.  The state highway starts on the coastal plain near the Chesapeake Bay and crosses Harford County's two main tributaries of the Susquehanna River, Deer Creek and Broad Creek, while traversing a wide swath of the Piedmont.  MD 136 is the second longest Maryland state highway entirely within one county after MD 235.

Maine State Route 6: State Route 6 is part of Maine's system of numbered state highways, running from the Quebec border, where that province's Quebec Route 173 reaches the U.S./Canada border at the Armstrong–Jackman Border Crossing just northwest of Sandy Bay Township, to the New Brunswick border in Vanceboro.  At just over 207 mi in length, it is the third-longest state highway in Maine (behind State Route 11 and State Route 9) and its fifth-longest numbered highway overall (U.S. Route 1 (US 1) and Interstate 95's (I-95) lengths are much longer).  SR 6 is the only highway in the state to both begin and end at the Canada–United States border.  Much of the route, particularly towards its western and extreme eastern ends, runs through very isolated parts of the state.

Hilham, Tennessee: Hilham is an unincorporated community in Overton County, Tennessee.  The community is situated around the junction of Tennessee State Route 136 (which runs north-to-south) and Tennessee State Route 85 (which runs east-to-west).  Although not a census-designated place, Hilham is part of a Zip Code Tabulation Area (38568) that covers most of rural northwest Overton County and part of northeast Jackson County.  As of the 2000 census, the population of this entire area was less than 2000.

Ashland UDC Jefferson Davis Highway Marker: The Ashland UDC Jefferson Davis Highway Marker is a commemorative marker on the Jefferson Davis Highway, in Hanover County, Virginia, outside of Richmond, Virginia.  It is a 42 in gray granite stone, with a slanted top, with two bronze plaques.  The Jefferson Davis Highway was conceived and marked by the United Daughters of the Confederacy, as a counter to the Lincoln Highway in the north, during 1913-1925.  In that era, named highways were being marked as automobile travel increased, and the advent of numbered highways eventually loomed.  The marker was placed at the junction of what is now US Route 1 and Cedar Lane (Virginia Route 623), between Richmond and Ashland, in 1927.  It has been moved twice: in the 1970s it was moved to accommodate the widening of Route 1, and it was moved across Route 1 in the 1980s.

Virginia State Route 136: State Route 136 (SR 136) is a primary state highway in the U.S. state of Virginia.  The state highway runs 1.17 mi from SR 652 east to U.S. Route 1 (US 1) within Alberta in northern Brunswick County.

Freeport, Maine: Freeport is a town in Cumberland County, Maine, United States.  The population was 7,879 at the 2010 census.  Known for its numerous outlet stores, Freeport is home to L.L. Bean, Wolfe's Neck Woods State Park, and the Desert of Maine.

New York State Route 136: New York State Route 136 (NY 136) is a state highway within the town of North Greenbush in Rensselaer County, New York, in the United States.  It begins at an intersection with U.S. Route 4 (US 4) just south of Troy and ends at a junction with NY 150 in the hamlet of Wynantskill.  NY 136 provides access to Hudson Valley Community College, located in an otherwise residential area of suburban Troy.  The route was assigned in the late 1930s as a connector between US 4 and Winter Street, then part of NY 40.  NY 136 was extended to its current length in 1980.

California State Route 299: State Route 299 (SR 299) is a state highway in the state of California that runs across the northern part of the state.  At 305.777 mi , it is the third longest California state highway (after Route 1 and Route 99).  Route 299 begins at US 101 at the northern edge of Arcata and continues in an easterly direction through to the Nevada state line.  Between Arcata and Redding, Route 299 intersects with State Route 96, and is briefly co-signed with State Route 3.  In Redding, it intersects with State Route 273, State Route 44, and Interstate 5.  East of Redding, it intersects with State Route 89, and a section is co-signed with State Route 139 before reaching Alturas.  It is then co-signed with U.S. Route 395 northeast of Alturas, and then runs east toward the border with Nevada.  A ghost town, Vya, Nevada, can be reached via this route, which after the border becomes a dirt road, which was formerly Nevada State Route 8A.

Henning High School: The town of Henning (population 241) is located in eastern Illinois in central Vermilion County.  U.S. Route 136 passes through Henning which sits just a stone's throw west of Illinois Route 1.  The C&EI Railroad (Chicago and Eastern Illinois) and the IC Railroad (Illinois Central) both had spurs that crossed in Henning.  The IC is no longer active; the C&EI spur ends in Henning for the purpose of serving the grain elevator still there.  The Indiana / Illinois state line is just 9 miles east of Henning.  A town of note in the area includes Danville just 11 miles south and a little east of Henning.

Question: In which town of Maine, with a population of 7979 in the 2010 census, does the State Route 136 begin at the junction with US Route 1?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "town_name": {
      "type": "string",
      "description": "The name of the town where the route begins."
    },
    "state": {
      "type": "string",
      "description": "The state where the town is located."
    },
    "route_details": {
      "type": "object",
      "properties": {
        "state_route_number": {
          "type": "integer",
          "description": "The number of the state route."
        },
        "junction_us_route": {
          "type": "integer",
          "description": "The number of the U.S. Route it junctions with."
        }
      },
      "required": [
        "state_route_number",
        "junction_us_route"
      ],
      "additionalProperties": false
    },
    "population_info": {
      "type": "object",
      "properties": {
        "census_year": {
          "type": "integer",
          "description": "The year of the census."
        },
        "population": {
          "type": "integer",
          "description": "The population of the town in the specified census year."
        }
      },
      "required": [
        "census_year",
        "population"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "town_name",
    "state",
    "route_details",
    "population_info"
  ],
  "additionalProperties": false
}
