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
Mount Le Conte (Tennessee): Mount Le Conte (or LeConte) is a mountain in Sevier County, Tennessee located in the Great Smoky Mountains National Park.  At 6593 ft it is the third highest peak in the national park, behind Clingmans Dome (6,643 ft, 2,024 m) and Mount Guyot (6,621 ft, 2,018 m).  It is also the highest peak that is completely within Tennessee.  However, from its immediate base to its summit, Mount Le Conte is one of the highest peaks in the Appalachian Mountains rising 5,301 ft (1,616 m) from its base, near Gatlinburg, Tennessee (1,292 ft/394 m).

Alum Cave Trail: The Alum Cave Trail (also referred to as Alum Cave Bluff Trail) is an American hiking trail in the Great Smoky Mountains National Park, in Sevier County, Tennessee.  The trail ascends Mount Le Conte, the sixth highest mountain east of the Mississippi River, and passes by many notable landmarks, such as Arch Rock, Inspiration Point, the Duckhawk Peaks, and Cliff Top, before merging with Rainbow Falls Trail near the summit.

Bullhead Trail: The Bullhead Trail is an American hiking trail in the Great Smoky Mountains National Park, in Sevier County, Tennessee.  The trail ascends Mount Le Conte, the tallest  (and sixth highest) mountain east of the Mississippi River and offers outstanding views before joining the Rainbow Falls Trail before terminating near the LeConte Lodge.

The Boulevard Trail: The Boulevard Trail is an American hiking trail in the Great Smoky Mountains National Park, in Sevier County, Tennessee.  The trail ascends Mount Le Conte, the tallest (and sixth highest) mountain east of the Mississippi River and offers high-elevation views before terminating near the LeConte Lodge.

Mount Le Conte (California): Mount Le Conte (or LeConte) is a mountain located in the Sierra Nevada of California.  The boundary between Inyo and Tulare counties runs along the crest of the Sierra, across Mount Le Conte.  The mountain was named in 1895 for Joseph Le Conte (1823–1901), the first professor of geology and natural history at the University of California.

Great Smoky Mountains National Park: Great Smoky Mountains National Park is a United States National Park and UNESCO World Heritage Site that straddles the ridgeline of the Great Smoky Mountains, part of the Blue Ridge Mountains, which are a division of the larger Appalachian Mountain chain.  The border between Tennessee and North Carolina runs northeast to southwest through the centerline of the park.  It is the most visited national park in the United States with over 11.3 million recreational visitors in 2016.  On its route from Maine to Georgia, the Appalachian Trail also passes through the center of the park.  The park was chartered by the United States Congress in 1934 and officially dedicated by President Franklin Delano Roosevelt in 1940.

Little Greenbrier (Great Smoky Mountains): Little Greenbrier is the name of a former Appalachian community that is now an historical area in the Great Smoky Mountains of East Tennessee.  The community was situated in a hollow rising from Metcalf Bottoms along Little River to the upper slopes of Cove Mountain, in the northeastern section of the national park.  Little Greenbrier was once known simply as "Greenbrier," but the "Little" was added to its name to distinguish it from the larger Greenbrier located between Mount Le Conte and Mount Guyot to the east.

Trillium Gap Trail: The Trillium Gap Trail is an American hiking trail in the Great Smoky Mountains National Park, in Sevier County, Tennessee.  The trail ascends Mount Le Conte, the tallest (and sixth highest) mountain east of the Mississippi River and passes both Grotto Falls and Trillium Gap before reaching the LeConte Lodge, near the summit.  The trail to Grotto Falls is one of the busiest in the national park.

Rainbow Falls Trail: The Rainbow Falls Trail is an American hiking trail in the Great Smoky Mountains National Park, in Sevier County, Tennessee.  The trail ascends Mount Le Conte, the tallest (and sixth-highest) mountain east of the Mississippi River, and passes Rainbow Falls before absorbing the Alum Cave Trail and terminating near the LeConte Lodge.

Sugarland Mountain Trail: The Sugarland Mountain Trail is an American hiking trail, in the Great Smoky Mountains National Park of Sevier County, Tennessee.  The trail traverses Sugarland Mountain, a massive ridge running perpendicular to the main crest of the Smokies and effectively dividing the park's north-central section from its northwestern section.  Sugarland Mountain is flanked by the deep upper valleys of two of the park's major watersheds— the West Fork of the Little Pigeon River (to the east) and Little River (to the west).  The trail passes through several forest types, including deciduous forest at lower elevations, heaths ("hells") along the mountain's backbone formations, and a stand of Southern Appalachian spruce-fir forest in the upper elevations.  Occasional breaks in the foliage allow for views of Mount Le Conte and Sevier County to the east and Blanket Mountain and the ridges above Elkmont to the west.

Question: When was the national park Mount Le Conte is located in chartered by Congress?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "park_name": {
      "type": "string",
      "description": "The name of the national park."
    },
    "mountain_name": {
      "type": "string",
      "description": "The name of the mountain located within the park."
    },
    "location_state": {
      "type": "string",
      "description": "The state where the mountain is located within the park."
    },
    "charter_year": {
      "type": "integer",
      "description": "The year the national park was chartered by the United States Congress."
    }
  },
  "required": [
    "park_name",
    "mountain_name",
    "location_state",
    "charter_year"
  ],
  "additionalProperties": false
}
