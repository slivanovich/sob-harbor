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
Alpine National Park: The Alpine National Park is a national park located in the Central Highlands and Alpine regions of Victoria, Australia.  The 646000 ha national park is located northeast of Melbourne.  It is the largest National Park in Victoria, and covers much of the higher areas of the Great Dividing Range in Victoria, including Victoria's highest point, Mount Bogong at 1986 m and the associated subalpine woodland and grassland of the Bogong High Plains.  The park's north-eastern boundary is along the border with New South Wales, where it abuts the Kosciuszko National Park.  On 7 November 2008 the Alpine National Park was added to the Australian National Heritage List as one of eleven areas constituting the Australian Alps National Parks and Reserves.

Haleakalā National Park: Haleakalā National Park is a national park located on the island of Maui in the U.S. state of Hawaiʻ i.  The park covers an area of 33,265 acre , of which 19,270 acre is a wilderness area.

Dunes of Texel National Park: Dunes of Texel National Park (Dutch: "Nationaal Park Duinen van Texel" ) is a national park located on the North-Holland island of Texel in the Netherlands.  All dune systems on the western side of the island and the large coastal plains on both the northern and southern points of the island are part of the park.  The park covers approximately 43 km2 and attained national park status in 2002.  The visitor center is located in the natural history museum Ecomare.

Haleakala Wilderness: Haleakala Wilderness is a designated wilderness area within Haleakala National Park on the island of Maui in the U.S. state of Hawaii.  It was designated on October 20, 1976, with 19270 acre , and was expanded to 24719 acre in 2005.  Encompassing the crater of Haleakalā, the Wilderness is accessible by two trails – Halemauu and Keoneheehee (Sliding Sands).

Middle Button Island National Park: Middle Button Island National Park is an Indian national park located in the Andaman and Nicobar Islands.  The park was created in 1979 and is situated about 200 km northeast of Port Blair, capital of the island group.  The total area that the national park covers is about 64 km2 .  Along with the neighbouring islands of North Button and South Button, both also national parks, it forms part of the Rani Jhansi Marine National Park off the coast of South Andaman Island.

Under-the-Rim Trail: The Under-the-Rim Trail is a 22.9 mi hiking trail in Bryce Canyon National Park, Utah.  The trail was established by the National Park Service to provide access to the portions of the park located below the rim of the Paunsaugunt Plateau, whose edge forms the eroded natural amphitheater for which the park is famous.  Plans dating to 1932 proposed the trail so that wooded portions of the park's east side could be accessed, primarily for fire suppression activities rather than for access to scenic features.  Work began on the trail in 1934, using Civilian Conservation Corps labor from CCC Camp NP-3, with work continuing into 1935.

Hawaii Route 31: Hawaii Route 31, also known as the Pi'ilani Highway, is a 38-mile road on the island of Maui in the U.S. state of Hawaii.  The state road begins in at an intersection with Hawaii Routes 310 and 311 in the West Maui town of Kihei.  The highway formerly ran parallel to the coast all the way to the southern terminus of the Hana Highway (Route 360), until developments in Wailea and Makena blocked access. .  The Kihei section of the highway now terminates in Wailea, and the much longer Kaupo section, which is county-maintained as County Road 31, connects Route 37 near Kula to the Route 360 south of Hana (at the western border of Haleakala National Park).

Hosmer's Grove: Hosmer's Grove is an example of experimental forestation from Hawaii's territorial days.  Located just inside Haleakala National Park near the summit of Haleakala in Maui, Hawaii, it includes a campsite and several hiking trails.

Haleakala Trail: The Haleakalā Trail (also sometimes known as the "Haleakala Bridle Trail") is the historic public access route to Haleakalā Crater and the summit of Haleakalā, which are now part of Haleakalā National Park.

Hawaiian Islands Biosphere Reserve: The Hawaiian Islands Biosphere Reserve is a UNESCO biosphere reserve in the Hawaiian Islands, created in 1980.  It comprises Hawaii Volcanoes National Park on the island of Hawaii, and Haleakala National Park on the island of Maui, with a total area of 995.45 square kilometres.

Question: The Haleakala Trail is located in the national park located on the island of Maui that covers how big of an area?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "national_park_name": {
      "type": "string",
      "description": "The name of the national park."
    },
    "located_on_island": {
      "type": "string",
      "description": "The island where the national park is located."
    },
    "total_area": {
      "type": "number",
      "description": "The total area of the national park."
    },
    "area_unit": {
      "type": "string",
      "description": "The unit of measurement for the total area."
    }
  },
  "required": [
    "national_park_name",
    "located_on_island",
    "total_area",
    "area_unit"
  ],
  "additionalProperties": false
}
