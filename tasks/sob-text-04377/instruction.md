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
Dairy Creek (Oregon): Dairy Creek is a 10.55 mi tributary of the Tualatin River in the U.S. state of Oregon.  It begins at the confluence of its east and west forks near the unincorporated community of Schefflin and meanders southeast across the Tualatin Valley to the Tualatin River near Hillsboro, in Washington County.  East Fork Dairy Creek begins at in Columbia County, slightly north of its border with Washington County, and flows generally south for 22 mi .  West Fork Dairy Creek, also about 22 mi long, forms at , near the unincorporated community of Tophill, and flows generally southeast.  Before railroads displaced river boats on the Tualatin, some steamships also worked the lower section of Dairy Creek, with plans to go as far up stream as Centerville.

Drift Creek (Siletz Bay): Drift Creek is a tributary, about 18 mi long, of Siletz Bay in the U.S. state of Oregon.  The creek begins near Stott Mountain in the Central Oregon Coast Range in Lincoln County and follows a winding course generally west through the Siuslaw National Forest to enter the bay south of Lincoln City on the Pacific Ocean.  It passes under U.S. Route 101 just before reaching the bay.

Cascade Range: The Cascade Range or Cascades is a major mountain range of western North America, extending from southern British Columbia through Washington and Oregon to Northern California.  It includes both non-volcanic mountains, such as the North Cascades, and the notable volcanoes known as the High Cascades.  The small part of the range in British Columbia is referred to as the Canadian Cascades or, locally, as the Cascade Mountains.  The latter term is also sometimes used by Washington residents to refer to the Washington section of the Cascades in addition to North Cascades, the more usual U.S. term, as in North Cascades National Park.  The highest peak in the range is Mount Rainier in Washington at 14411 ft .

Horse Creek (McKenzie River): Horse Creek is a tributary of the McKenzie River in near the unincorporated community of McKenzie Bridge in Lane County in the U.S. state of Oregon.  It begins in the Cascade Range in the Three Sisters Wilderness of the Willamette National Forest.  Its headwaters are near the Deschutes County border and the Pacific Crest Trail.  It flows generally northwest to meet the river about 65 mi upstream of the McKenzie's confluence with the Willamette River.

Little Beaver Creek (Lorain County, Ohio): Little Beaver Creek is a tributary of Beaver Creek (a.k.a. "Big Beaver Creek") in Lorain County, Ohio.  Little Beaver Creek begins north of the Lorain County Regional Airport and runs northerly until the Little Beaver joins with the Big Beaver in the present city-limits of Lorain, Ohio.  (There is a smaller tributary of the Little Beaver which begins near the bygone village of "Whiskeyville".)

Ritner Creek: Ritner Creek is a tributary of the Luckiamute River in Polk County in the U.S. state of Oregon.  The creek begins near Bald Mountain in the Central Oregon Coast Range and flows generally southeast to meet the Luckiamute southwest of Pedee and north of Kings Valley.  The confluence is 31 mi upstream of the Luckiamute's mouth on the Willamette River.  Named tributaries of Ritner Creek from source to mouth are Sheythe, Love, Clayton, and Kinsey creeks.

Horse Creek, Wyoming: Horse Creek is an unincorporated community in western Laramie County, Wyoming, United States.  It lies between Horse Creek to the north, and the South Fork of Horse Creek to the south, along WYO 211 northwest of the city of Cheyenne, the county seat of Laramie County.  Its elevation is 6,506 feet (1,983 m).  Although Horse Creek is unincorporated, it has a post office, with the ZIP code of 82061.  As of the 2010 census, Horse Creek had an estimated population of 39.

Dead Indian Creek (Oregon): Dead Indian Creek is a tributary of South Fork Little Butte Creek in Jackson County, in the U.S. state of Oregon.  It flows generally north through the Rogue River – Siskiyou National Forest in the Cascade Range east of Medford.  The creek begins at 2562 ft above sea level near Howard Prairie Lake and enters the South Fork at Camp Latgawa.  The South Fork flows northwest to meet the North Fork near Lake Creek; combined they form Little Butte Creek, a tributary of the Rogue River.

Cedar Creek (South Fork Eel River): Cedar Creek is an 11.2 mi tributary of the South Fork Eel River in Mendocino County in the U.S. state of California.  The creek begins southeast of Red Mountain, at an elevation of 778 ft .  It makes an S-curve west-northwest then bends sharply south, dropping into the valley of the South Fork Eel.  The confluence is south of the city of Leggett, on the river's right bank.  The only named tributary of Cedar Creek is Little Cedar Creek, a headwaters tributary.  Big Dann Creek joins the South Fork Eel on the same bank, just upstream of Cedar Creek, while the next major tributary downstream of Cedar is Rock Creek.  The Cedar Creek watershed is rugged and has few tributaries.

Oaks Creek: Oaks Creek drains Canadarago Lake, which is situated in the north central region of Otsego County, New York.  The creek begins by Schuyler Lake, New York and flows southeast approximately 9.32 miles before converging with the Susquehanna River south of Cooperstown, New York, by Index, New York. From the source to Oaksville, New York the creek flows along Panther Mountain.  Fly Creek is a main tributary to oaks creek that converges with Oaks Creek south of Fly Creek, New York.

Question: Horse Creek begins in which North American mountain range?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creek_name": {
      "type": "string",
      "description": "The name of the creek."
    },
    "feature_type": {
      "type": "string",
      "description": "The type of geographical feature, e.g., 'tributary' or 'creek'."
    },
    "origin_details": {
      "type": "object",
      "properties": {
        "mountain_range": {
          "type": "string",
          "description": "The mountain range where the creek begins."
        },
        "country_state": {
          "type": "string",
          "description": "The U.S. state where the creek begins."
        }
      },
      "required": [
        "mountain_range",
        "country_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "creek_name",
    "feature_type",
    "origin_details"
  ],
  "additionalProperties": false
}
