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
Lewis and Clark County, Montana: Lewis and Clark County is a county located in the U.S. state of Montana.  As of the 2010 census, the population was 63,395.  Its county seat is Helena, the state capital.  The numerical designation for Lewis and Clark County (used in the issuance of the state's license plates) is 5.  The county was established in 1865 as Edgerton County, and was renamed "Lewis and Clark County" two years later.  The present name was given in honor of explorers Lewis and Clark.

Frontier, Wyoming: Frontier (also North Kemmerer) is an unincorporated community in southern Lincoln County, Wyoming, United States.  It lies just north of the city of Kemmerer, the county seat of Lincoln County.  Its elevation is 6,932 feet (2,113 m).  Although Frontier is unincorporated, it had a post office, with the ZIP code of 83121 which closed in 2011.

North Springs, Tennessee: North Springs (also North Spring) is an unincorporated community in northwestern Jackson County, Tennessee, United States.  It lies along Tennessee State Routes 56 and 151, northwest of the town of Gainesboro, the county seat of Jackson County.  Its elevation is 604 feet (184 m).

Cimarron Redoubt: The Cimarron Redoubt (also known as the Deep Hole Redoubt) was an improvised U.S. Army fortification south of the city of Ashland in Clark County, Kansas, United States.  Built in 1870 near a major trade route's crossing of the Cimarron River, it was later used for a variety of civilian purposes, including a post office.  Today, it lies abandoned amid farm fields in southern Center Township.

Manly-McCann House: The Manly-McCann House is a historic building located at 402 S. 4th St. in Marshall, Illinois.  The Greek Revival building was constructed in 1838 to serve as a temporary courthouse for Clark County.  While Clark County moved its county seat to Marshall in 1837, a permanent courthouse could not be completed until 1839, so a smaller temporary building became necessary.  After the county government relocated, Marshall postmaster Uri Manly moved the city's post office and his store to the building.  The building later became a private home and had several owners; one of the longer owners of the house was the McCann family, who owned the house from 1891 to 1947 and constructed several additions on the rear.  The Clark County Historical Society bought the house in 1968 and uses it as the county's historical museum.

C-Tran (Washington): The C-Tran (stylized as C-TRAN), more formally the Clark County Public Transit Benefit Area Authority, is a public transit agency serving Clark County, Washington, United States, including the cities of Battle Ground, Camas, Vancouver and Washougal.  Founded in 1981, C-Tran operates fixed route bus services within Clark County, as well as paratransit services for qualified persons with disabilities (C-Van) and a dial-a-ride service in Camas, Ridgefield, and La Center (The Connector).  C-Tran also provides express commuter services between Clark County and various points in Portland, Oregon, including downtown, the Parkrose/Sumner and Delta Park MAX Light Rail stations (in northeast and north Portland), Lloyd District, and Oregon Health and Science University.

Clark County, Kansas: Clark County (county code CA) is a county located in the U.S. state of Kansas.  As of the 2010 census, the county population was 2,215.  Its county seat and most populous city is Ashland.

Springville, Clark County, Indiana: Springville was a small town that existed from 1798 to 1811 in Charlestown Township, Clark County, Indiana, United States.  It was named for the springs in the area that provided a good fresh water supply.  A Frenchman established a trading post at the site in 1799; Indians called it Tullytown due to the prominent trader Charles Tully (pronounced "two-lay").  It was located at the intersection of four Indian trails, two of which went to what is now Detroit, Michigan and Cincinnati, Ohio.  At Springville's peak it had 100 residents.  When Clark County was established, Springville was named the county seat on April 7, 1801, creating the first court in the county.  On June 9, 1802 the county seat was moved to Jeffersonville, starting the demise of Springville.

Clark County Sheriff's Office (Washington): The Clark County Sheriff's Office is the local, county-level law enforcement agency serving Clark County, Washington.  The Clark County Sheriff's Office was established in 1849 and is the oldest law enforcement organization in the state of Washington.  The Clark County Sheriff's Office employs approximately 450 employees who serve in three distinct branches; enforcement, corrections, and support.  The enforcement branch is composed of sworn deputy sheriffs who typically perform general policing duties such as patrolling the county, investigating crimes, serving arrest warrants, transporting prisoners, controlling disturbances, providing a safe atmosphere at large county events, along with a variety of other emergency and routine activities.  Deputy sheriff's also serve in specialty assignments such as detectives, narcotics, SWAT, K9, marine patrol, school resource officer, explosive disposal unit, traffic homicide, sex offender monitoring, computer forensics, and child abuse investigations.  Corrections deputies work in two different facilities; the main jail and the Lower River Road work center.  The main jail is a medium and high security jail facility which houses an average of 600 inmates daily.  The Lower River Road work center is a low-security jail facility which houses approximately 100 inmates.  Support branch employees are non-sworn employees who work in criminal records, warrants, finance, human resources, admin, and in jail support roles supervising jail inmates who work in food and laundry services.

Columbus, Mississippi: Columbus is a city in and the county seat of Lowndes County, Mississippi, United States, located primarily east, but also north and northeast of the Tombigbee River, which is also referred to as the Tennessee-Tombigbee Waterway .  It is approximately 146 mi northeast of Jackson, 92 mi north of Meridian, 63 mi south of Tupelo, 60 mi northwest of Tuscaloosa, Alabama, and 120 mi west of Birmingham, Alabama.  The population was 25,944 at the 2000 census and 23,640 in 2010.  The population in 2012 was estimated to be 23,452.  Columbus is the principal city of the Columbus Micropolitan Statistical Area, which is part of the larger Columbus-West Point Combined Statistical Area.  Columbus is also part of the area of Mississippi called The Golden Triangle, consisting of Columbus, West Point and Starkville, in the counties of Lowndes, Clay and Oktibbeha.

Question: What county seat of Clark County, Kansas, is also north of the Cimarron Redoubt?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "county_name": {
      "type": "string",
      "description": "The name of the county."
    },
    "county_seat": {
      "type": "string",
      "description": "The name of the county seat."
    },
    "landmark_name": {
      "type": "string",
      "description": "The name of the landmark mentioned in the question."
    },
    "relative_location_of_county_seat_to_landmark": {
      "type": "string",
      "description": "Describes the location of the county seat relative to the landmark."
    }
  },
  "required": [
    "county_name",
    "county_seat",
    "landmark_name",
    "relative_location_of_county_seat_to_landmark"
  ],
  "additionalProperties": false
}
