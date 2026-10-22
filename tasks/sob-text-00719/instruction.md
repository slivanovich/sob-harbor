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
Illinois Route 164: Illinois Route 164 is a state road in rural western Illinois.  It runs from U.S. Route 34 in Gladstone to U.S. Route 34 and Illinois Route 41 in Galesburg.  This distance is 35.70 mi .

Illinois Route 167: Illinois Route 167 is an east–west state road entirely located in Knox County in western Illinois.  It runs from U.S. Route 34 northeast of Wataga to Illinois Route 180 east of Victoria.  Illinois 167 is 12.24 mi long.  The route is maintained by the Illinois Department of Transportation.

Illinois Route 89: Illinois Route 89 is a rural, north–south state highway in central Illinois.  It runs from U.S. Route 34 in La Moille to Illinois Route 116 in Metamora.  Routes 26 and 89 are the main north–south roads between Interstate 39/U.S. Route 51 and Illinois Route 29.  This is a distance of 55.48 mi

Walter Payton: Walter Jerry Payton (July 25, 1954 – November 1, 1999) was an American football running back who played for the Chicago Bears of the National Football League (NFL) for thirteen seasons.  Payton was known around the NFL as "Sweetness".  A nine-time Pro Bowl selectee, Payton is remembered as a prolific rusher, once holding records for career rushing yards, touchdowns, carries, yards from scrimmage, all-purpose yards, and many other categories.  He was also versatile, and retired with the most receptions by a non-receiver, and had eight career touchdown passes.  He was elected into the Pro Football Hall of Fame in 1993 and the College Football Hall of Fame in 1996.  Hall of Fame NFL player and coach Mike Ditka described Payton as the greatest football player he had ever seen—but even greater as a human being.

Fisher, Oregon: Fisher is an unincorporated community in rural Lincoln County, Oregon, United States.  Fisher lies along Five Rivers Road, 9.2 mi south of its intersection with Oregon Route 34.  It is slightly north of the Lincoln–Lane county line in the Siuslaw National Forest.  A stream called "Five Rivers" flows northwest through Fisher, about 12 mi by water from the stream's mouth on the Alsea River.  Route 34 runs along the Alsea River between Alsea and Waldport.

U.S. Route 34 in Illinois: U.S. Route 34 (US 34) is an east–west highway In the state of Illinois that runs from the Iowa state line at Gulfport, west of Galesburg, to Illinois Route 43 (IL 43) and Historic U.S. Route 66 at Harlem Avenue in Berwyn.  The entire highway in Illinois is named the Walter Payton Memorial Highway after Pro Football Hall of Famer Walter Payton, who wore #34 for the Chicago Bears.  The highway is 211.37 mi long within the state.

Connecticut Route 34: Route 34 is a primary state highway in the U.S. state of Connecticut.  Route 34 is 24.37 mi long, and extends from Washington Street near I-84/US 6 in Newtown to the junction of I-95 and I-91 in New Haven.  The highways connects the New Haven and Danbury areas via the Lower Naugatuck River Valley.  The portion of the route between New Haven and Derby was an early toll road known as the Derby Turnpike.

U.S. Route 34 in Colorado: U.S. Route 34 in Colorado is a segment of U.S. Route 34.  Its west end is at U.S. Highway 40 in Granby and its east end is at the Nebraska border east of Laird, Colorado.

New Jersey Route 34: Route 34 is a state highway in the central part of the U.S. state of New Jersey.  The route runs 26.79 mi from an intersection with Route 35 and Route 70 (the former Brielle Circle) in Wall Township, Monmouth County north to an intersection with U.S. Route 9 (US 9) in Old Bridge Township, Middlesex County.  The route is a four-lane divided highway between its southern terminus and the north end of the Route 33 concurrency in Howell Township; along this stretch, the route intersects the Garden State Parkway and Interstate 195 (I-195)/Route 138 within a short distance of each other.  North of Route 33, Route 34 is an undivided two- to four-lane road that intersects Route 18 in Colts Neck Township and Route 79 in Matawan.  Route 34 passes through mostly suburban areas along its route.

Illinois Route 41: Illinois Route 41 is a north–south highway in rural west-central Illinois.  It runs from U.S. Route 136 near Macomb north to U.S. Route 34 and Illinois Route 164 in Galesburg, a distance of 37.53 mi .  Illinois 41 is maintained by the Illinois Department of Transportation.

Question: What is the birthday of the running back that U.S Route 34 in Illinois is named after?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person the highway is named after."
    },
    "person_role": {
      "type": "string",
      "description": "The primary role or profession of the person."
    },
    "highway_designation": {
      "type": "string",
      "description": "The official designation of the highway."
    },
    "memorial_highway_name": {
      "type": "string",
      "description": "The specific memorial name given to the highway."
    },
    "birthday": {
      "type": "string",
      "description": "The birth date of the person."
    }
  },
  "required": [
    "person_name",
    "person_role",
    "highway_designation",
    "memorial_highway_name",
    "birthday"
  ],
  "additionalProperties": false
}
