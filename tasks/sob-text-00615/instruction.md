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
Tonto Natural Bridge: Tonto Natural Bridge is a natural arch in Arizona, USA, that is believed to be the largest natural travertine bridge in the world.  The area surrounding the bridge has been made into a state park called Tonto Natural Bridge State Park, which is located off State Route 87, just 10 mi north of Payson.  Tonto Natural Bridge stands over a 400 ft tunnel that measures 150 ft at its widest point and reaches a height of 183 ft .

Kenlake State Resort Park: Kenlake State Resort Park is a park located on the western shore of Kentucky Lake.  The park's main entrance and most of its facilities are located in Marshall County; the park also extends into Calloway County.  The mailing address of the park is Hardin, Kentucky; however, it is located much closer to the unincorporated community of Aurora, Kentucky.  The nearest town of substantial size is Murray.  The park encompasses 1795 acre of land, 160300 acre of water, and features climate-controlled indoor tennis courts.  It was Kentucky's first state resort park.  Along with Lake Barkley State Resort Park and Kentucky Dam Village State Resort Park, Kenlake State Resort Park is part of the Land Between the Lakes National Recreation Area, originally organized by the Great Depression–era Tennessee Valley Authority (TVA).

Greenbo Lake State Resort Park: Greenbo Lake State Resort Park in Kentucky is a resort park in the northeastern part of the commonwealth, close to the town of Greenup, Kentucky in Greenup County on Kentucky State Route 1.  It features a 36-room lodge named for Greenup County resident and writer Jesse Hilton Stuart, a 63-site campground with 35 primitive sites, a swimming pool with slides, two tennis courts, an 18-hole miniature golf course, an amphitheater and a scuba refuge area.  The lodge contains a 232-seat dining room.  It is centered on the 300 acre Greenbo Lake that features a boat dock and marina.  There are over 25 mi of hiking, biking and horseback trails.  The park hosts a variety of community events each year including a quilt show, murder mystery dinner theaters, scrapbooking, and a 5K race.

Daniel Boone National Forest: Daniel Boone National Forest is the only national forest completely within the boundary of Kentucky.  Established in 1937, it was originally named the Cumberland National Forest, after the core region called the Cumberland Purchase Unit.  About 2100000 acre are contained within its current proclamation boundary, of which 706000 acre are owned and managed by the United States Department of Agriculture Forest Service (as of April 2006), up from around 620000 acre in the early to mid-1990s.

Natural Bridge State Resort Park: Natural Bridge State Resort Park is a Kentucky state park located in Powell and Wolfe Counties along the Middle Fork of the Red River, adjacent to the Red River Gorge Geologic Area and surrounded by the Daniel Boone National Forest.  Its namesake natural bridge is the centerpiece of the park.  The natural sandstone arch spans 78 ft and is 65 ft high.  The natural process of weathering formed the arch over millions of years.  The park is approximately 2300 acre of which approximately 1200 acre is dedicated by the Kentucky State Nature Preserves Commission as a nature preserve.  In 1981 this land was dedicated into the nature preserves system to protect the ecological communities and rare species habitat.  The first federally endangered Virginia big eared bats, "Corynorhinus townsendii virginianus", recorded in Kentucky were found at Natural Bridge State Resort Park in the 1950s.

Torrent Falls: Torrent Falls is a landmark outdoor residential property near the small community of Torrent, Kentucky, USA, which is near Natural Bridge State Park, Red River Gorge and Daniel Boone National Forest in Kentucky.  At one time, a health and vacation resort for the wealthy, it has a striking waterfall, both traditional and sport rock climbing, a loop trail and cabins available for vacation rentals on this private property.

Asplenium × gravesii: Asplenium × gravesii, commonly known as Graves' spleenwort, is a rare, sterile, hybrid fern, named for Edward Willis Graves (1882–1936).  It is formed by the crossing of Bradley's spleenwort ("A. bradleyi") with lobed spleenwort ("A. pinnatifidum").  It is only found where its parent species are both present; in practice, this proves to be a few scattered sites in the Appalachian Mountains, Shawnee Hills, and Ozarks, reaching perhaps its greatest local abundance around Natural Bridge State Resort Park.  Like its parents, it prefers to grow in acid soil in the crevices of sandstone cliffs.

Buckhorn Lake State Resort Park: Buckhorn Lake State Resort Park is a state park located in the northwest corner of Perry County, Kentucky.  The park itself encompasses 856 acre , while Buckhorn Lake, a mountain reservoir lake which serves as its major feature and which was created by damming the Middle Fork of the Kentucky River, covers approximately 1230 acre .  The park is adjacent to the northern edge of the Daniel Boone National Forest.

Arizona State Route 67: State Route 67 (SR 67) is a 43.4 mi long, north–south state highway in northern Arizona.  Also called the Kaibab Plateau – North Rim Parkway, SR 67 is the sole road that links U.S. Route 89A (US 89A) at Jacob Lake to the North Rim of Grand Canyon National Park.  Along the route, the road heads through the national park as well as Kaibab National Forest and is surrounded by evergreen trees.  The section inside the national park is maintained by the National Park Service (NPS), whereas the section north of the entrance, completely within Kaibab National Forest, is owned by the Arizona Department of Transportation (ADOT).  The road was built in the late 1920s and improved through the 1930s.  In 1941, the road received its number, and was given its designation as the parkway in the 1980s.  The parkway has received designations as a National Forest Scenic Byway as well as a National Scenic Byway.

Cumberland Falls State Resort Park: Cumberland Falls State Resort Park is a park located just southwest of Corbin, Kentucky and is contained entirely within the Daniel Boone National Forest.  The park encompasses 1657 acre and is named for its major feature, 68 ft Cumberland Falls.  The falls are one of the few places in the western hemisphere where a moonbow can frequently be seen on nights with a full moon.  The park is also the home of 44 ft Eagle Falls.

Question: ] Natural Bridge State Resort Park is surrounded by the only national forest completely within the boundary of Kentucky and was originally named what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "park_name": {
      "type": "string",
      "description": "The name of the state resort park mentioned in the question."
    },
    "surrounding_national_forest": {
      "type": "string",
      "description": "The name of the national forest that surrounds the park."
    },
    "is_only_national_forest_in_state": {
      "type": "boolean",
      "description": "Indicates if the surrounding national forest is the only one completely within Kentucky."
    },
    "national_forest_original_name": {
      "type": "string",
      "description": "The original name of the surrounding national forest."
    }
  },
  "required": [
    "park_name",
    "surrounding_national_forest",
    "is_only_national_forest_in_state",
    "national_forest_original_name"
  ],
  "additionalProperties": false
}
