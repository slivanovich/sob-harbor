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
Chambers Covered Bridge: The Chambers Covered Bridge is a covered bridge located in Cottage Grove, Oregon, United States.  It is 78 ft long and spans the Coast Fork Willamette River.  It was built in 1925 to carry rail traffic hauling logs from the Lorane Valley to the J.H. Chambers Mill, a lumber mill which was located on an area between South Highway 99 and the Coast Fork Willamette River.  The mill closed in the 1950s after a second fire burned the mill down.  The railroad tracks were removed and the bridge was left.  The mill property is now being developed as a housing development called Riverwalk.  The Chambers Covered Railroad Bridge is the only remaining fully covered railroad bridge west of the Mississippi River.

Old Stone Arch Bridge (Clark Center, Illinois): The Old Stone Arch Bridge was a stone arch bridge located along the former route of the National Road in Clark Center, Illinois.  The limestone bridge was 8.9 ft high and 81.5 ft long with a 17.8 ft span.  The U.S. Army Corps of Engineers built the bridge between 1828 and 1837, the period in which the Corps improved much of the National Road.  The National Road was the first major highway built by the U.S. government and brought settlers and goods from the Eastern United States to Illinois.  The bridge became part the Illinois state highway system in 1918, and later became part of U.S. Route 40; it served road traffic until 1933, when US 40 was realigned through the area.

Shell Rock Bridge: The Shell Rock Bridge is a historic bridge located in Shell Rock, Iowa, United States.  It spans the Shell Rock River for 266 ft .  On May 11, 1915, the Butler County Board of Supervisors approved contracts for the Waterloo, Iowa bridge contractor Miller-Hey Construction Co. to build three bridges.  This concrete filled spandrel arch bridge was completed in the fall of 1915 for $16,500.  The bridge was designed by the Iowa State Highway Commission.  It was listed on the National Register of Historic Places in 1998.

Clay Wade Bailey Bridge: The Clay Wade Bailey Bridge is a cantilever bridge carrying U.S. Route 42 and U.S. Route 127 across the Ohio River, connecting Cincinnati, Ohio and Covington, Kentucky.  This also marks the termination of U.S. Route 25.  The bridge's main span is 675 ft .  It is a 3-lane bridge; Two lanes are dedicated to travel each way and the middle lane is a reversible lane, meaning the direction of travel of the middle lane changes according to the time of day.

U.S. Route 127 in Kentucky: U.S. Route 127 (US 127) in Kentucky runs 207.7 mi from the Tennessee state line in rural Clinton County to the Ohio state line in Cincinnati.  The southern portion of the route is mostly rural, winding through various small towns along the way.  It later runs through the state capital of Frankfort before continuing north, eventually passing through several Cincinnati suburbs in Northern Kentucky, joining US 42 near Warsaw and US 25 in Florence before crossing the Ohio River via the Clay Wade Bailey Bridge.

U.S. Route 25: U.S. Route 25 (US 25) is a north–south United States highway that runs for 750 mi from Brunswick, Georgia, to the Ohio state line in Covington, Kentucky.

Blackburn Point Bridge: The Blackburn Point Bridge is a historic swing bridge located near Osprey, Florida, United States, that is listed on the U.S. National Register of Historic Places.  It is a one-lane swing bridge located on Blackburn Point Road at the Gulf Intracoastal Waterway.  It is the northernmost of the two bridges connecting the barrier island Casey Key to the mainland of Florida.  It was constructed by the Champion Bridge Co. and opened to traffic in December 1926.

Phil G. McDonald Bridge: The Phil G. McDonald Memorial Bridge, also known as the "Glade Creek Bridge", is a deck truss bridge located in Raleigh County, West Virginia near the city of Beckley.  The bridge is among the ten highest bridges in the United States, and the highest bridge within the Interstate Highway System being a part of I-64, with a deck height of 700 ft above Glade Creek.  The bridge is also among the top fifty highest bridges in the world.

Indiana State Highway Bridge 42-11-3101: Indiana State Highway Bridge 42-11-3101, also known as Poland Bridge, is a historic Parker through truss bridge located in Cass Township, Clay County, Indiana.  It was built by the Vincennes Bridge Company and erected in 1939.  It carries State Road 42 over the Eel River.  It measures 175 feet long and rests on a concrete abutment and concrete pier.

Indiana State Highway Bridge 46-11-1316: Indiana State Highway Bridge 46-11-1316, also known as Bowling Bridge, is a historic Parker through truss bridge located in Washington Township, Clay County, Indiana.  It was built by the Vincennes Bridge Company and erected in 1939.  It carries State Road 46 over the Eel River.  It consists of two 196 foot long spans and rests on concrete abutments and a concrete pier.

Question: From which state in the south does this United States highway, at whose termination is Clay Wade Bailey Bridge located,  start?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "highway_name": {
      "type": "string",
      "description": "The name of the United States highway."
    },
    "termination_bridge": {
      "type": "string",
      "description": "The bridge where the highway terminates."
    },
    "starting_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the highway starts."
        },
        "state": {
          "type": "string",
          "description": "The state where the highway starts."
        },
        "is_southern_state": {
          "type": "boolean",
          "description": "Indicates if the starting state is considered a southern state."
        }
      },
      "required": [
        "city",
        "state",
        "is_southern_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "highway_name",
    "termination_bridge",
    "starting_location"
  ],
  "additionalProperties": false
}
