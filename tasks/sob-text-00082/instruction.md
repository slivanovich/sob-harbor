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
Ocoee Dam No. 1: Ocoee Dam Number 1 is a hydroelectric dam on the Ocoee River in Polk County in the U.S. state of Tennessee.  The dam impounds the 1930 acre Parksville Reservoir (often called Ocoee Lake), and is the farthest downstream of four dams on the Toccoa/Ocoee River owned and operated by the Tennessee Valley Authority.  Completed in 1911, Ocoee No. 1 was one of the first hydroelectric projects in Tennessee.

Lumber River State Park: Lumber River State Park is a North Carolina, United States, state park along the Lumber River in Scotland, Hoke, Robeson and Columbus counties.  It covers 11,259 acre along a 115-mile (185-km) stretch of the Lumber River.  Lumber River State Park is located in North Carolina's Coastal Plain.  It was established in 1989 as both a state park and designated as a "Natural and Scenic River" by the North Carolina General Assembly.  In addition, it is the only blackwater river in North Carolina to be designated as a National Wild and Scenic River by the Department of the Interior.

Toccoa/Ocoee River: The Toccoa River and Ocoee River are the names in use for a single 93 mi river that flows northwestward through the southern Appalachian Mountains of the southeastern United States.  It is a tributary of the Hiwassee River, which it joins in Polk County, Tennessee, near the town of Benton.  Three power generating dams are operated along it.

Fall River State Park: Fall River State Park is a state park in Greenwood County, Kansas USA, southwest of the city of Toronto.  Located near the Flint Hills, Fall River State Park is 980 acre and can be accessed by going along 144 Highway 105.  The state park features six different hiking trails including Casner Creek, Turkey Run, Post Oak, Overlook, Bluestem, and Catclaw.

Ocoee Scenic Byway: The Ocoee Scenic Byway is a 26 mi National Forest Scenic Byway and Tennessee Scenic Byway that traverses through the Cherokee National Forest, in East Tennessee.  It is part of U.S. Route 64, and features the Ocoee Whitewater Center and scenic bluffs along Ocoee River and Gorge.

Hiwassee/Ocoee Scenic River State Park: The Hiwassee/Ocoee Scenic River State Park is a Tennessee state park in Polk County, Tennessee, United States, that provides access to the Hiwassee and Ocoee rivers.

Wicomico River (Potomac River): The Wicomico River is a 13.0 mi tributary of the lower tidal portion of the Potomac River located in the U.S. state of Maryland south of Washington, DC.  The river empties into the Potomac at Cobb Island and St. Margaret's Island.  Its watershed area (excluding water) is 77 sqmi , with 2% impervious surface in 1994.  in Charles, St. Mary's, and southern Prince George's counties.  The lower section of the river forms part of the boundary between Charles and St. Mary's counties.  The Wicomico River was designated a Scenic River under the Maryland Scenic River Act in 1968, and there are Scenic River Commissions for it in both Charles and St. Mary's counties (see links below).

Ocoee Dam No. 2: Ocoee Dam Number 2 is a hydroelectric dam on the Ocoee River in Polk County in the U.S. state of Tennessee.  The dam impounds the Ocoee No. 2 Reservoir and is one of four dams on the Toccoa/Ocoee River owned and operated by the Tennessee Valley Authority.  Ocoee Dam No. 2— which was completed in 1913— is perhaps most notable for its design, which utilizes a wooden flume that carries water from the reservoir down the side of the Ocoee Gorge to the dam's powerhouse 5 mi downstream.  Ocoee No. 2 is also situated at the center of one of the nation's top whitewater rafting locations, and the dam's releases help to maintain consistent rapids on the river during warmer months.

Smith River State Recreational Waterway: Smith River State Recreational Waterway, popularly known as the Smith River State Park, is a protected river corridor and "virtual park" owned and operated by the state of Montana in the United States.  The site is not officially a state park, but rather a State Recreational Waterway and managed River Corridor.  The park consists of the state-owned Smith River; a Montana Department of Fish, Wildlife and Parks (FWP) put-in access point, Camp Baker; 27 FWP-owned and -leased boat camps on the shore of the river; and the FWP-owned Eden Bridge take-out point.  Little of the area is owned by FWP.  Much of the surrounding shoreline is owned by the United States Forest Service, United States Bureau of Land Management, and private owners.  Through management agreements with other government agencies and private landowners, FWP manages the 58.9 mi Smith River Corridor as a "virtual state park".  The Smith River is the only river in the state of Montana where a permit is required to boat or float on the river.

Ocoee Dam No. 3: Ocoee Dam No. 3 is a hydroelectric dam on the Ocoee River in Polk County, in the U.S. state of Tennessee.  It is one of four dams on the Toccoa/Ocoee River owned and operated by the Tennessee Valley Authority, which built the dam in the early 1940s to meet emergency demands for electricity during World War II.  The dam impounds the 360 acre Ocoee No. 3 Reservoir, which stretches 11 mi upriver to the Tennessee-Georgia state line.  Ocoee No. 3's powerhouse is actually located several miles downstream from the dam, and is fed by a 2.5 mi conduit that carries water to it from the reservoir.

Question: How many power generating dams are operated along the river that is accessed through the Hiwassee/Ocoee Scenic River State Park?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "park_name": {
      "type": "string",
      "description": "The name of the state park providing access to the river."
    },
    "river_name": {
      "type": "string",
      "description": "The name of the river accessed through the park."
    },
    "number_of_power_generating_dams": {
      "type": "integer",
      "description": "The total count of power generating dams on the specified river."
    },
    "dam_details": {
      "type": "array",
      "description": "A list of details for each power generating dam on the river.",
      "items": {
        "type": "object",
        "properties": {
          "dam_name": {
            "type": "string",
            "description": "The name of the dam."
          },
          "dam_type": {
            "type": "string",
            "description": "The type of the dam, e.g., hydroelectric."
          }
        },
        "required": [
          "dam_name",
          "dam_type"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "park_name",
    "river_name",
    "number_of_power_generating_dams",
    "dam_details"
  ],
  "additionalProperties": false
}
