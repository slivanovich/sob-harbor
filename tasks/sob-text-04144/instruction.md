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
West Branch Magalloway River: The West Branch of the Magalloway River is a 9.3 mi river in northernmost New Hampshire and northwestern Maine in the United States.  It is a tributary of the Magalloway River, located in the Androscoggin River watershed of Maine and New Hampshire.

West Branch Little Magalloway River: The West Branch of the Little Magalloway River is a 5.3 mi river in northern New Hampshire and northwestern Maine in the United States.  It is a tributary of the Little Magalloway River, located in the Androscoggin River watershed of Maine and New Hampshire.

East Branch Clarion River Lake: East Branch Clarion River Lake, or East Branch Lake is a reservoir at Elk State Park in Elk County, Pennsylvania, in the United States.  It was constructed by the U.S. Army Corps of Engineers by damming the East Branch of the Clarion River.  Construction of the rolled earth, impervious core dam was authorized by the Flood Control Act of 1944.  The lake is one of sixteen flood control projects administered by the Pittsburgh District of the Army Corps of Engineers.  East Branch Clarion River Lake helps to provide flood protection for the Clarion River valley and the lower portions of the Allegheny River and the upper portions of the Ohio River.

Magalloway River: The Magalloway River is a river in northwestern Maine and northern New Hampshire in the United States.  It is a tributary of the Androscoggin River, which flows to the Kennebec River at Merrymeeting Bay in Maine, near the Atlantic Ocean.  The total length of the river is 30 mi , or 48 mi if the distances across intervening lakes are included.

Rockland Branch: The Rockland Branch is a railroad from Brunswick, Maine to Rockland, Maine.  A charter was granted in 1849 to build a railway from the Portland and Kennebec Railroad on the west side of the Kennebec River to Rockland.  Construction through the rocky headlands of the Atlantic coast proved more expensive than anticipated.  The Knox and Lincoln Railroad commenced service to Rockland in 1871 using a ferry to cross the Kennebec River between Bath and Woolwich.  The Knox and Lincoln was leased by Maine Central Railroad in 1891, and became Maine Central's Rockland Branch in 1901.  Maine Central purchased the Samoset destination hotel in nearby Glen Cove (a part of neighbouring Rockport) in 1912, and offered direct passenger service for summer visitors from the large eastern cities.  Carlton bridge was completed in 1927 to carry the railroad and U.S. Route 1 over the Kennebec River.  Maine Central sold the Samoset hotel in 1941, and the last Maine Central passenger train to Rockland was on 4 April 1959.  The State of Maine purchased the branch in 1987 to prevent abandonment.  The line has subsequently been operated by the Maine Coast Railroad, the Maine Eastern Railroad, and, beginning in 2016, the Central Maine and Quebec Railway.

First East Branch Magalloway River: The First East Branch Magalloway River is a 7.0 mi river in northwestern Maine.  It is a tributary of the Magalloway River, which flows to the Androscoggin River and ultimately to the tidal Kennebec River and the Atlantic Ocean.

Third East Branch Magalloway River: The Third East Branch Magalloway River is a 4.0 mi stream in northwestern Maine.  It is a tributary of the West Branch Magalloway River, which flows to the Magalloway River, then the Androscoggin River, and ultimately to the tidal Kennebec River and the Atlantic Ocean.

Middle Branch Little Magalloway River: The Middle Branch of the Little Magalloway River is a 4.6 mi river in northern New Hampshire and northwestern Maine in the United States.  It is a tributary of the West Branch of the Little Magalloway, located in the Androscoggin River watershed of Maine and New Hampshire.

Second East Branch Magalloway River: The Second East Branch Magalloway River is a 3.5 mi river in northwestern Maine.  It is a tributary of the Magalloway River, part of the Androscoggin River watershed.

Kennebec River: The Kennebec River is a 170 mi river entirely within the U.S. state of Maine.

Question: What state does First East Branch Magalloway River and Kennebec River have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "river_names": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the rivers mentioned in the question."
    },
    "common_state": {
      "type": "string",
      "description": "The state that both rivers have in common."
    },
    "river_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the river."
          },
          "length_miles": {
            "type": "number",
            "description": "The length of the river in miles."
          },
          "location_states": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "States where the river is located."
          }
        },
        "required": [
          "name",
          "location_states"
        ],
        "additionalProperties": false
      },
      "description": "Details for each river mentioned."
    }
  },
  "required": [
    "river_names",
    "common_state",
    "river_details"
  ],
  "additionalProperties": false
}
