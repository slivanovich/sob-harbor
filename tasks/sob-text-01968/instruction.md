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
James River (Dakotas): The James River (also known as the Jim River or the Dakota River) is a tributary of the Missouri River, approximately 710 miles (1,140 km) long, draining an area of 20,653 square miles (53,490 km) in the U.S. states of North Dakota and South Dakota.  About 70 percent of the drainage area is in South Dakota.  The river provides the main drainage of the flat lowland area of the Dakotas between the two plateau regions known as the Coteau du Missouri and the Coteau des Prairies.  This narrow area was formed by the James lobe of the Laurentide Ice Sheet during the last ice age, and as a consequence the watershed of the river is slender and it has few major tributaries for a river of its length.

Coteau du Missouri: The Coteau du Missouri, or Missouri Plateau, is a large plateau that stretches along the eastern side of the valley of the Missouri River in central North Dakota and north-central South Dakota in the United States.  In the Canadian provinces of Saskatchewan and Alberta this physiographic region is classified as the uplands Missouri Coteau which is a part of the Great Plains Province or Alberta Plateau Region which extends across the south west corner of the province of Saskatchewan as well as the south east corner of the province of Alberta.  Historically, in Canada the area was known as the Palliser's Triangle regarded as an extension of the "Great American Desert" and unsuitable for agriculture and thus designated by Canadian geographer and explorer John Palliser.  The terrain of the Missouri Coteau features low hummocky, undulating, rolling hills, potholes, and grasslands.

Boundary Ranges: The Boundary Ranges, also known in the singular and as the Alaska Boundary Range, are the largest and most northerly subrange of the Coast Mountains.  They begin at the Nass River, near the southern end of the Alaska Panhandle in the Canadian province of British Columbia and run to the Kelsall River, near the Chilkoot Pass, beyond which are the Alsek Ranges of the Saint Elias Mountains, and northwards into the Yukon Territory flanking the west side of the Yukon River drainage as far as Champagne Pass, north of which being the Yukon Ranges.  To their east are the Skeena Mountains and Stikine Plateau of the Interior Mountains complex that lies northwest of the Interior Plateau; the immediately adjoining subregion of the Stikine Plateau is the Tahltan Highland.  To their northeast is the Tagish Highland, which is a subregion of the Yukon Plateau.  Both highlands are considered in some descriptions as included in the Coast Mountains.  The Alexander Archipelago lies offshore and is entirely within Alaska.

McGregor Plateau: The McGregor Plateau is a sub-plateau of the Fraser Plateau, the northernmost major subdivision of the Interior Plateau spanning the inland regions of the Pacific Northwest.  Located in British Columbia, Canada, to the east of the city of Prince George, British Columbia, the McGregor Plateau lies between the main spine of the Northern Rocky Mountains on the east and the Fraser River on the west, beginning on its southeast at the confluence of the Torpy River with the Fraser and running northwest, parallel to the Fraser and the Rockies, to end in the area of the Arctic and Pacific Lakes to the north of the great bend in the Fraser River just upstream from and to the northeast of Prince George.  The McGregor Plateau is very mountainous in character and includes several large rivers, the largest being the McGregor River and Herrick Creek.  Included in the McGregor Plateau is the McGregor Range, which lies between the McGregor and Torpy Rivers.

Nahlin Plateau: The Nahlin Plateau is a plateau in northwestern British Columbia, Canada, located between the Sheslay River and Tuya River on the west and east and the Nahlin River and the Stikine River to the north and south.  It is a subplateau of the Stikine Plateau; adjoining parts of the same larger plateau are the Taku Plateau to the northwest, the Tahltan Highland to the southwest and south, the Kawdy Plateau to the north, and the Spatsizi Plateau to the southeast.  The Nahlin Plateau is the location of the Level Mountain Range and Heart Peaks, two small mountain ranges forming parts of large shield volcanoes.

Cumberland Plateau: The Cumberland Plateau is the southern part of the Appalachian Plateau in the Appalachian Mountains of the United States.  It includes much of eastern Kentucky and Tennessee, and portions of northern Alabama and northwest Georgia.  The terms "Allegheny Plateau" and the "Cumberland Plateau" both refer to the dissected plateau lands lying west of the main Appalachian Mountains.  The terms stem from historical usage rather than geological difference, so there is no strict dividing line between the two.  Two major rivers share the names of the plateaus, with the Allegheny River rising in the Allegheny Plateau and the Cumberland River rising in the Cumberland Plateau in Harlan County, Kentucky.

California Plateau: California Plateau ( ) is an undulating ice-covered plateau, 30 nmi long and from 2 to wide, which rises to 3,000 m at the eastern side of Scott Glacier.  The plateau reaches a maximum height of 3,275 m in Mount Blackburn at the southern end.  The northwestern side of the plateau is marked by the steep rock cliffs of Watson Escarpment; the southeastern side grades gradually to the elevation of the interior ice.  It was mapped by the United States Geological Survey from ground surveys and from U.S. Navy aerial photography, 1960–64, and named by the Advisory Committee on Antarctic Names for the several branches of the University of California which have sent numerous researchers to work in Antarctica.

Deschutes River (Oregon): The Deschutes River in central Oregon is a major tributary of the Columbia River.  The river provides much of the drainage on the eastern side of the Cascade Range in Oregon, gathering many of the tributaries that descend from the drier, eastern flank of the mountains.  The Deschutes provided an important route to and from the Columbia for Native Americans for thousands of years, and then in the 19th century for pioneers on the Oregon Trail.  The river flows mostly through rugged and arid country, and its valley provides a cultural heart for central Oregon.  Today the river supplies water for irrigation and is popular in the summer for whitewater rafting and fishing.

Takahashi River: The Takahashi River (高梁川 , Takahashi-gawa ) is a Class A major river in the western part of Okayama Prefecture.  It acts as the main drainage for the Takahashi River Drainage System, and is one of the three main drainage rivers in Okayama Prefecture (the others being the Yoshii River and the Asahi River).

Shivwits Plateau: The Shivwits Plateau is a large plateau in northwest Arizona, and in the northwest of the Grand Canyon region.  Just like the Kaibab Plateau in the east Grand Canyon forces the course of the Colorado River encircling it, the Shivwits Plateau is the major course changer of the Colorado in west Grand Canyon.  The Colorado River goes due-south on the east perimeter of the plateau, goes west, then northwest to its outfall at Lake Mead.  The southwest of the plateau borders the Colorado, but a lower elevation section is directly riverside; it is lower elevation hills and small canyons, called Sanup Plateau, and bordering the section of the Colorado called the Lower Granite Gorge.  (The Lower Granite Gorge starts on the east side at the start of its due-south excursion around Shivwits Plateau.)

Question: The James River provides the main drainage between two plateau regions, the large plateau on the eastern side and which other plateau?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "river_name": {
      "type": "string",
      "description": "The name of the river being discussed."
    },
    "drainage_description": {
      "type": "string",
      "description": "A description of the river's drainage function."
    },
    "plateau_regions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the two plateau regions between which the river provides drainage."
    },
    "other_plateau_identified": {
      "type": "string",
      "description": "The name of the specific plateau region identified as the answer to the question."
    }
  },
  "required": [
    "river_name",
    "drainage_description",
    "plateau_regions",
    "other_plateau_identified"
  ],
  "additionalProperties": false
}
