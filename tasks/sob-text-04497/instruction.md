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
New Salem, New York: New Salem is a hamlet in the town of New Scotland, Albany County, New York.  It is located in a valley at the foot of the Helderberg Escarpment along New York State Route 85.  A local fair and car show is held every year in this small hamlet.  It is also home to the town of New Scotland's community center and museum.

Avon, New York: Avon ( ) is a town in Livingston County, New York, United States.  The town is bordered on the north by the town of Rush, New York in Monroe County.  Avon is south of Rochester.  The population was 7,146 at the 2010 census.  The town is named after the river Avon.  The town has a village within it also called Avon.

Voorheesville, New York: Voorheesville is a village within the town of New Scotland in Albany County, New York, United States.  It is a suburb of Albany and part of the city's historic metropolitan area.  The population was 2,789 at the 2010 census.  The village is named after a railroad attorney, Alonzo B. Voorhees.

Billy Montana: Billy Montana (born September 28, 1959 in Voorheesville, New York) is an American country music singer-songwriter.  Between 1987 and 1995, Montana released one studio album and charted six singles on "Billboard"' s Hot Country Singles & Tracks chart.  As a songwriter, Montana's songs have been recorded by Garth Brooks, Sara Evans, Jo Dee Messina, Tim McGraw, Martina McBride, Sister Hazel and Kenny Rogers, among others.

Fishkill, New York: Fishkill is a village within the town of Fishkill in Dutchess County, New York, United States.  The village population was 2,171 at the 2010 census.  It is part of the Poughkeepsie–Newburgh–Middletown, NY Metropolitan Statistical Area as well as the larger New York–Newark–Bridgeport, NY-NJ-CT-PA Combined Statistical Area.

Grafton County, New Hampshire: Grafton County is a county located in the state of New Hampshire, in the United States.  As of the 2010 census, the population was 89,118.  Its county seat is North Haverhill, which is a village within the town of Haverhill.  Until 1972, the county courthouse and other offices were located in downtown Woodsville, a larger village within the town of Haverhill.

New York State Route 85A: New York State Route 85A (NY 85A) is an east–west state highway in Albany County, New York, in the United States.  It serves as a 5.54 mi , two-lane alternate route of NY 85 through the town of New Scotland, running from the hamlet of New Salem to the hamlet of New Scotland.  While NY 85 bypasses the village of Voorheesville to the south, NY 85A directly serves it, connecting to two state routes inside of the village limits.  The route was assigned c. 1932 to its current alignment.

New York State Route 396: New York State Route 396 (NY 396) is an east–west state highway in Albany County, New York, in the United States.  The route is functionally a spur route as it connects to another signed state highway at only one end.  The western terminus of NY 396 is at an intersection with County Route 103 (CR 103) in Callanans Corners, a small hamlet situated just south of the Bethlehem–Coeymans town line in the town of Coeymans.  Its eastern terminus is at a junction with NY 144 in Bethlehem east of the hamlet of Selkirk.  West of Callanans Corners, the road continues northwestward to NY 443 in New Scotland as CR 301.  NY 396 was assigned as part of the 1930 renumbering of state highways in New York.

Becraft Formation: The Becraft Formation is a geologic formation of marine sedimentary rock found in New York State.  The Becraft is a part of the lower Devonian Helderberg Group and conformably overlies the New Scotland Formation and is overlain by the Alsen Formation throughout the lower Hudson Valley of New York State.  The formation is Gedinnian in age.  Outcrops of the formation are found from the New York-New Jersey border to the Helderbergs of Albany County, New York and as far west as Schoharie County, New York.  The thickness of the formation varies from around 3 meters in Canajoharie to 8 meters thick in Albany and swells to 27 meters near Kingston.  The Becraft Formation is named for Becraft Mountain in western Columbia County, New York where it prominently crops out.

Slingerlands, New York: Slingerlands is a hamlet in the town of Bethlehem, Albany County, New York.  It is located immediately west of Delmar and near the New Scotland town-line and south of the Albany city-limits.  It is a suburb of Albany.  The Slingerlands ZIP Code (12159) includes parts of the towns of New Scotland and Guilderland.

Question: Billy Montana was born in a village within the town of New Scotland, in what county in New York?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "birth_location": {
      "type": "object",
      "properties": {
        "place_name": {
          "type": "string",
          "description": "The name of the village where the person was born."
        },
        "place_type": {
          "type": "string",
          "description": "The type of the place (e.g., village, hamlet)."
        },
        "town_name": {
          "type": "string",
          "description": "The name of the town the village is within."
        },
        "county_name": {
          "type": "string",
          "description": "The name of the county."
        },
        "state_name": {
          "type": "string",
          "description": "The name of the state."
        }
      },
      "required": [
        "place_name",
        "place_type",
        "town_name",
        "county_name",
        "state_name"
      ],
      "additionalProperties": false
    },
    "answer_county": {
      "type": "string",
      "description": "The final answer to the question: the county where the person was born."
    }
  },
  "required": [
    "person_name",
    "birth_location",
    "answer_county"
  ],
  "additionalProperties": false
}
