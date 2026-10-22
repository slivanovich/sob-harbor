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
Minne-Ha-Ha II: The Minne-Ha-Ha is a sternwheel steamboat on Lake George, New York.  It is owned and operated by the Lake George Steamboat Company.

New York State Route 28N: New York State Route 28N (NY 28N) is an east–west state highway in the North Country of New York in the United States.  It extends for 50.95 mi through the Adirondack Mountains from Blue Mountain Lake to North Creek.  The route is a northerly alternate route to NY 28 between both locations; as such, it passes through several communities that NY 28 bypasses to the south.  The westernmost 10 mi of NY 28N overlap with NY 30 through the town of Long Lake.  NY 28N and NY 30 split in the hamlet of Long Lake, from where NY 30 heads to the north and NY 28N proceeds eastward through mountainous regions of Adirondack Park.

New York State Route 426: New York State Route 426 (NY 426) is a state highway located entirely within Chautauqua County, New York, in the United States.  It runs just over 13 mi from one section of the Pennsylvania state line to another, passing through two small hamlets and providing the Southern Tier Expressway (Interstate 86 or I-86 and NY 17) with its westernmost exit in New York.  NY 426 is the westernmost north–south state highway in New York.

Chautauqua Belle: The steamer Chautauqua Belle is an authentic Mississippi River-style sternwheel steamboat owned and operated by U.S. Steam Lines Ltd, operating on Chautauqua Lake in Western New York.

Kiwassa Lake: Kiwassa Lake, originally called Lonesome Pond, is a 280-acre lake in the north-central Adirondack Park, south of Dewey Mountain, between Lower Saranac Lake and Oseetah Lake, two miles southwest of the village of Saranac Lake, New York, United States.  It drains into Lake Oseetah, and thence into the Saranac River.  The westernmost shore line is owned by New York State.

New York State Route 474: New York State Route 474 (NY 474) is a state highway located entirely within Chautauqua County in the westernmost corner of New York in the United States.  It begins at the section of the Pennsylvania state line that runs north–south and runs eastward, initially paralleling the state line before taking a more northeasterly alignment toward Chautauqua Lake.  The route ends adjacent to the lake at a junction with NY 394 in the town of Busti.  NY 474 was originally designated as New York State Route 74 in 1930 before being renumbered to NY 474 c. 1973 .  The route continues westward into Pennsylvania as Pennsylvania Route 474 (PA 474), which was assigned in the 1980s.

Lake George Steamboat Company: The Lake George Steamboat Company was incorporated in 1817 to operate steamboats on Lake George, New York.  It is the oldest company in the Lake George region.  The company operates steamboats that run the full length of Lake George between Ticonderoga at the north end of the lake and the village of Lake George at the south end of the lake.

Camp Lourdes: Ten Mile Point (Tenmile Point) is a scenic area on the shore of Skaneateles Lake, New York, a popular picnic spot for lake outings in the late 19th and early 20th centuries.  It is located at the mouth of a ravine on alluvium.  Onandaga County Road 72 runs through it and is locally known as "10 Mile Point Road".  It was formerly the property of the Skaneateles Railroad and Steamboat Company (Skaneateles Park Company) who built a steamboat dock, a dancing pavilion and planted a grove of trees there.  Their planned hotel was never built.  And in 1906 Ten Mile Point was purchased by the Auburn and Syracuse Electric Railroad Company from the Skaneateles Park Company.  It is now the location of Lourdes Camp, an historic facility of the local Roman Catholic diocese.  In 1990 the "Six Town Picnic'" that had been held annually from 1885 until World War II was revived at Ten Mile Point.

Western New York: Western New York is the westernmost region of the state of New York.  It includes the cities of Buffalo, Rochester, Niagara Falls, the surrounding suburbs, as well as the outlying rural areas of the Great Lakes lowlands, the Genesee Valley, and the Southern Tier.  One writer suggests Western New York's eastern border to be the Preemption Line, an historic political division of Native American tribal lands.

Mohican II: Mohican II is a historic steel riveted hull excursion steamboat located at Lake George in Warren County, New York.  She was built in 1907-08 for the Lake George Steamboat Company by the T.S. Marvel Shipuilding Company of Newburgh, New York.  She measures 117 ft in length, 26 ft in beam, and 8.3 ft depth of hold.  She was designed for use on Lake George as an excursion vessel, has been in continuous use for over 100 years and is the oldest passenger vessel in the United States.

Question: What lake in the westernmost region of the state of New York had an authentic Mississippi River-style sternwheel steamboat operating on it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "lake_name": {
      "type": "string",
      "description": "The name of the lake."
    },
    "region": {
      "type": "string",
      "description": "The region of New York where the lake is located."
    },
    "steamboat_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the steamboat."
        },
        "style": {
          "type": "string",
          "description": "The style of the steamboat."
        },
        "operator": {
          "type": "string",
          "description": "The company operating the steamboat."
        }
      },
      "required": [
        "name",
        "style",
        "operator"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "lake_name",
    "region",
    "steamboat_details"
  ],
  "additionalProperties": false
}
