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
North Town Hall: The North Town Hall is one of two historic 19th-century town halls in Chelmsford, Massachusetts.  Located at 31 Princeton Street, near the North Chelmsford village center, it is a 2-1/2 story wood frame structure with Greek Revival styling.  It was built in 1853, and was used, alternating with the Centre Town Hall, for town meetings until 1885.  It was thereafter used as a community meeting hall and polling station, a role it served until 1967, when the town moved its school administration offices there.  In 2011 the building underwent a full restoration, and is again used as a community center.

Former Greenwood Town Hall: The Former Greenwood Town Hall is located at 270 Main Street (Maine State Route 26) in Locke Mills, the main village of Greenwood, Maine.  Completed in 1931, the building has been a center of civic and social activities since, hosting town meetings, elections, school graduations, dances, and private functions.  It was replaced as town hall by the present facilities in 1988, and is now maintained by a local non-profit.  It was listed on the National Register of Historic Places in 2001.

Winchester Town Hall (New Hampshire): The town hall of Winchester, New Hampshire, is located on Main Street, just south of the junction of New Hampshire Route 10 and New Hampshire Route 119 in the center of the town.  Built of brick in 1911-12 to a design by S. Winthrop St. Clair, it is the only Gothic Revival town hall in Cheshire County.  It was built because the previous town meeting house (a combination town hall and church at the site of the Winchester Memorial Church) was destroyed by fire.  The church was also designed by St. Clair, a Boston-based architect who hailed from Winchester.

Sangerville, Maine: Sangerville is a town in Piscataquis County, Maine, United States.  The population was 1,343 at the 2010 census.  The town was named after Colonel Calvin Sanger, a landowner.

Uxbridge Town Hall: Uxbridge Town Hall is the town hall of Uxbridge, Massachusetts, located at 45 South Main Street.  It is listed on the National Register of Historic Places.  It was built in 1879 and added to the historic registry 100 years later.  Amos P. Cutting of Worcester was the architect.  Ferry & Gardner of Springfield also submitted plans.

Troy Village Historic District: The Troy Village Historic District is a historic district encompassing the historic village center of Troy, New Hampshire, United States.  The district is centered along New Hampshire Route 12, north to Marlborough Road and south to the junction with South Main Street.  To the east of NH 12 it includes School Street, Mill Street, and Monadnock Street as far as Mill Street, and most of the abutting streets.  On the west side it includes Russell, Water, and Prospect streets, and South Main Street nearly to Longmeadow Drive.  It was listed on the National Register of Historic Places in 2002.

Sangerville Town Hall: Sangerville Town Hall is located at 1 Town Hall Lane (corner of South Main Street) in the village center of Sangerville, Maine.  Built in 1902, it is one of the rural community's most sophisticated architectural buildings.  It was designed and built by a local contractor, and has well-proportioned Colonial Revival features.  It was listed on the National Register of Historic Places in 1991.

Sutton Center Historic District: The Sutton Center Historic District is a historic district encompassing the center of the village of Sutton, Massachusetts.  The district, which covers 435 acre , is centered on the junction of Boston Road, Singletary Avenue, and Uxbridge Road.  Boston Road is a major east-west route through the town, and the other two roads run north-south through the village center.  A typically rural village center, its civic and institutional buildings are clustered near the intersection on its south side, in the general area of the town common.  The town common and cemetery were laid out in 1719, after settlement of the township began in 1716.  There are a few surviving houses that date to the middle of the 18th century or earlier; exact dates for most are uncertain.  There are only a few institutional buildings: the 1829 Congregational Church, the 1983 Town Hall, built on the site of the town's first purpose-built town hall (1885), and Rufus Putnam Hall, an 1824 school building and Masonic lodge that now houses the local history museum.  Only one commercial structure the 1839 Brick Block, stands in the village.  There is also a historic animal pound, a rectangular stone structure used to pen stray livestock, which dates to the early days of the town.

Pawlet Town Hall: Pawlet Town Hall houses the municipal offices of the town of Pawlet, Vermont.  Located at 122 School Street in the village center, it was built in 1881 as a combined town hall, meeting and performance venue, and retail establishment.  It has served as town hall since its construction, and is a good local example of late Italianate architecture.  It was listed on the National Register of Historic Places in 1995.

Robert Carleton House: The Robert Carleton House is a historic house on North Main Street in Sangerville, Maine.  Built c. 1819, it is one of the oldest surviving buildings in Piscataquis County.  The 2-1/2 story wood frame structure, with vernacular Federal style, was built by Robert Carleton on land purchased from his brother, a worker in the nearby fulling mill.  It was listed on the National Register of Historic Places in 1975.

Question: Sangerville Town Hall is located at 1 Town Hall Lane (corner of South Main Street) in the village center of Sangerville, Maine, Sangerville is a town in Piscataquis County, Maine, in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "town_name": {
      "type": "string",
      "description": "The name of the town."
    },
    "county": {
      "type": "string",
      "description": "The county where the town is located."
    },
    "state": {
      "type": "string",
      "description": "The state where the town is located."
    },
    "country": {
      "type": "string",
      "description": "The country where the town is located."
    }
  },
  "required": [
    "town_name",
    "county",
    "state",
    "country"
  ],
  "additionalProperties": false
}
