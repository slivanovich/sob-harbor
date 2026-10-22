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
1601 Vine Street: The Alexander is an intended mixed-use high-rise in the Pennsylvanian city of Philadelphia, presently under construction.  The building is adjacent to the Philadelphia Pennsylvania Temple, which was designed by Perkins+Will.  This project will consist of one tower, as well as a Mormon meetinghouse next to the building, which will be clad in red brick.

Delaware Valley: The Delaware Valley is the valley through which the Delaware River flows.  By extension, this toponym is commonly used to refer to Greater Philadelphia or Philadelphia metropolitan area ("the [Lower] Delaware Valley Metropolitan Area"), which straddles the Lower Delaware River just north of its estuary.  The Delaware Valley Metropolitan Area is located at the southern part of the Northeast megalopolis and as such, the Delaware Valley can be described as either a metropolitan statistical area (MSA), or as a broader combined statistical area (CSA).  The Delaware Valley Metropolitan Area is composed of several counties in southeastern Pennsylvania and southwestern New Jersey, one county in northern Delaware and one county in northeastern Maryland.  The MSA has a population of over 6 million, while the CSA has a population of over 7.1 million (as of the 2010 Census Bureau count).  Philadelphia, being the region's major commercial, cultural, and industrial center, wields a rather large sphere of influence that affects the counties that immediately surround it.

Finns Point: Finns Point is a small strategic promontory in Pennsville Township, Salem County, New Jersey, and New Castle County, Delaware, located at the southwest corner of the New Jersey peninsula, on the east bank of the Delaware River near its mouth on Delaware Bay.  Due to the wording of the original charter defining the boundaries of New Jersey and Delaware, part of the promontory is actually enclosed within the state of Delaware's border, due to tidal flow and the manner in which the borders between New Jersey and Delaware were first laid out.  Therefore, this portion of Finns Point is an exclave of Delaware, cut off from the rest of the state by Delaware Bay.  The area is about 10 mi south of the city of Wilmington, and directly across the Delaware River from the New Castle area, and the Delaware River entrance to the Chesapeake & Delaware Canal.  Pea Patch Island, part of the state of Delaware, sits in the channel of the river facing the promontory.

Delaware River Viaduct: The Delaware River Viaduct is a reinforced concrete railroad bridge across the Delaware River about 2 mi south of the Delaware Water Gap that was built in 1908-10 as part of the Lackawanna Cut-Off rail line.  It is the sister to the line's larger Paulinskill Viaduct.  The Delaware River Viaduct also crosses Interstate 80 on the east (New Jersey) side of the river and Slateford Road and the Lackawanna Railroad's "Old Road" (now Delaware-Lackawanna) on the west (Pennsylvania) side.  Abandoned in 1983, it is part of a New Jersey Transit proposal to restore passenger service to Scranton, Pennsylvania.

Shellpot Creek: Shellpot Creek is a tributary of the Delaware River in northeast New Castle County, Delaware.  The stream rises between Grubb Road and Shipley Road, south of Naaman's Road at in Brandywine Hundred and flows southeast for about six miles before discharging into the Delaware River at near Edgemoor.  Prior to 1938, the stream drained into the Brandywine Creek, but was subsequently redirected to the Delaware River.

New Jersey Route 29: Route 29 is a state highway in the U.S. state of New Jersey.  It runs 34.76 mi from an interchange with Interstate 295 (I-295) in Hamilton Township in Mercer County, where it continues as I-195, to Route 12 (Bridge Street / Race Street) in Frenchtown, Hunterdon County.  Between the southern terminus and I-95, the route is a mix of freeway and four-lane divided highway that runs along the Delaware River through Trenton.  This section includes a truck-restricted tunnel that was built along the river near historic houses and Riverview Cemetery.  North of I-95, Route 29 turns into a scenic and mostly two-lane highway.  North of the South Trenton Tunnel, it is designated the Delaware River Scenic Byway, a New Jersey Scenic Byway and National Scenic Byway, that follows the Delaware River in mostly rural sections of Mercer County and Hunterdon County.  The obsolete Delaware & Raritan Canal usually stands between the river and the highway.  Most sections of this portion of Route 29 are completely shaded due to the tree canopy.  Route 29 also has a spur, Route 129, which connects Route 29 to U.S. Route 1 (US 1) in Trenton.

Fort DuPont State Park: Fort DuPont State Park is a Delaware state park located in Delaware City, Delaware.  Fort DuPont itself, named after Rear Admiral Samuel Francis duPont, was used as a military base from the Civil War through World War II, and was part of a three fort defense system, with Fort Delaware and Fort Mott with the purpose of protecting the Delaware River and the city of Philadelphia from naval attacks.  Fort DuPont State Park is situated along the Delaware River and Chesapeake and Delaware Canal.

Delaware River: The Delaware River is a major river on the Atlantic coast of the United States.  It drains an area of 14119 sqmi in five U.S. states—New York, New Jersey, Pennsylvania, Maryland and Delaware.  Rising in two branches in New York state's Catskill Mountains, the river flows 419 mi into Delaware Bay where its waters enter the Atlantic Ocean near Cape May in New Jersey and Cape Henlopen in Delaware.  Not including Delaware Bay, the river's length including its two branches is 388 mi .

Easton, Pennsylvania: Easton is a city in and the county seat of Northampton County, Pennsylvania, United States.  The city's population was 26,800 as of the 2010 census.  Easton is located at the confluence of the Delaware River and the Lehigh River, roughly 55 mi north of Philadelphia and 70 mi west of New York City.

Lumberville–Raven Rock Bridge: The Lumberville–Raven Rock Bridge, also known as the Lumberville Foot Bridge, is a free pedestrian bridge over the Delaware River.  The bridge connects Bull's Island Recreation Area near Raven Rock, Delaware Township in Hunterdon County, New Jersey to Lumberville, Solebury Township in Bucks County, Pennsylvania, United States.  The bridge, which is one of the two exclusively pedestrian bridges over the Delaware River, is owned and operated by the Delaware River Joint Toll Bridge Commission.

Question: Which Pennsylvanian city sits at the confluence of the Delaware River?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city."
    },
    "state": {
      "type": "string",
      "description": "The U.S. state where the city is located."
    },
    "rivers_at_confluence": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of rivers that meet at the city's confluence."
    },
    "is_county_seat": {
      "type": "boolean",
      "description": "Indicates if the city is a county seat."
    },
    "county_name": {
      "type": "string",
      "description": "The name of the county if the city is a county seat."
    }
  },
  "required": [
    "city_name",
    "state",
    "rivers_at_confluence",
    "is_county_seat",
    "county_name"
  ],
  "additionalProperties": false
}
