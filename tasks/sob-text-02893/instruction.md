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
Rolling Road station: Rolling Road station is a Virginia Railway Express station in Burke, Virginia.  The station serves the Virginia Railway Express Manassas Line, and shares the right-of-way with Amtrak's "Cardinal" and "Crescent" trains; however, no Amtrak trains stop here.

Rippon station: Rippon station is a Virginia Railway Express station located at 15511 Farm Creek Drive in Woodbridge, Virginia.  The station, one of two VRE stations in Woodbridge, is located at a southerly dead end, and is named for the closest and last intersection with Farm Creek Drive.  It serves the Fredericksburg Line and shares the right-of-way with Amtrak's "Northeast Regional, Silver Meteor, Silver Star, Palmetto, Auto Train", and "Carolinian" trains; however, no Amtrak trains stop here.  Rippon station is located along the west side of the Featherstone National Wildlife Refuge.

Virginia Railway Express: The Virginia Railway Express (VRE) (reporting mark VREX) is a regional/commuter rail service that connects the Northern Virginia suburbs to Union Station in Washington, D.C., via two lines: the Fredericksburg Line from Fredericksburg, Virginia, and the Manassas Line from Broad Run/Airport station in Bristow, Virginia.

Broad Run station: Broad Run station is a Virginia Railway Express station located at 10637 Piper Lane in the Bristow section of unincorporated Prince William County, Virginia, United States, adjacent to Manassas Regional Airport.  It is the last station on VRE's Manassas Line, and has parking for 885 cars.  The station is located on a siding that leads off the 2 track main line.  The siding continues to a yard for the Virginia Railway Express.

Fredericksburg station: Fredericksburg is a passenger rail station in Fredericksburg, Virginia.  It is served by Amtrak's "Carolinian" and "Northeast Regional" lines, "Silver Meteor", and the Virginia Railway Express's Fredericksburg Line.  It is located on Lafayette Boulevard (US BUS 1).

Leeland Road station: Leeland Road station is a Virginia Railway Express station located at 275 Leeland Road in Stafford, Virginia, although VRE states that its address is in Falmouth, Virginia.  The station serves the Fredericksburg Line and shares the right-of-way with Amtrak's "Northeast Regional", "Silver Meteor", "Silver Star", "Palmetto", "Auto Train", "Carolinian" and "Piedmont" trains.  However, no Amtrak trains stop here.  The station is located next to the Leeland Station community, which was named after the VRE station.  It is also next to Conway Elementary School.

Lorton station (VRE): Lorton station is a railroad station located at 8990 Lorton Station Boulevard in Lorton, Virginia.  It is served by the Virginia Railway Express Fredericksburg Line.  This station is one mile north from Amtrak's Lorton station, the northern terminus of the "Auto Train".  Amtrak's "Northeast Regional", "Silver Meteor", "Silver Star", "Palmetto", and "Carolinian" trains share the line but do not stop at either Lorton station.

Manassas Park station: Manassas Park station is a Virginia Railway Express station in Manassas Park, Virginia.  The station serves the Virginia Railway Express Manassas Line, and shares the right-of-way with Amtrak's "Cardinal" and "Crescent" trains; however, no Amtrak trains stop here.

Northeast Regional: The Northeast Regional is a higher-speed rail service operated by Amtrak in the Northeastern and Mid-Atlantic United States.  In the past it has been known as the "NortheastDirect", "Acela Regional", or "Regional".  It is the busiest Amtrak route, carrying 8.04 million passengers in fiscal year (FY) 2013, a 0.4% increase over the 8.01 million passengers in FY2012.  The "Northeast Regional" service earned over $568.7 million in gross ticket revenue in FY2013, a 6.2% increase over the $536 million earned during FY2012.

Brooke station: Brooke is a Virginia Railway Express station located at 1721 Brooke Road in Brooke near Stafford, Virginia.  Free parking is available and located on a hill leading from the road.  The station serves the Fredericksburg Line and shares the right-of-way with Amtrak's "Northeast Regional", "Silver Meteor", "Silver Star", "Auto Train", "Palmetto", "Carolinian" and "Piedmont" trains; however, no Amtrak trains stop here.

Question: Leeland Road station is a Virginia Railway Express station located at 275 Leeland Road in Stafford, Virginia, the station serves the Fredericksburg Line and shares the right-of-way with the Northeast Regional, a higher-speed rail service operated by who, in the Northeastern and Mid-Atlantic United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "vre_station_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Virginia Railway Express station."
        },
        "line_served": {
          "type": "string",
          "description": "The VRE line served by the station."
        }
      },
      "required": [
        "name",
        "line_served"
      ],
      "additionalProperties": false
    },
    "shared_amtrak_service_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Amtrak service that shares the right-of-way."
        },
        "service_type": {
          "type": "string",
          "description": "The type of rail service."
        },
        "operator": {
          "type": "string",
          "description": "The operator of the Amtrak service."
        },
        "operating_region": {
          "type": "string",
          "description": "The region where the service is operated."
        }
      },
      "required": [
        "name",
        "service_type",
        "operator",
        "operating_region"
      ],
      "additionalProperties": false
    },
    "operator_of_northeast_regional": {
      "type": "string",
      "description": "The direct answer to who operates the Northeast Regional service."
    }
  },
  "required": [
    "vre_station_info",
    "shared_amtrak_service_details",
    "operator_of_northeast_regional"
  ],
  "additionalProperties": false
}
