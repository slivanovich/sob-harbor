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
Nebraska Admiral: Nebraska Admiral (formally, Admiral in the Great Navy of the State of Nebraska) is Nebraska's highest honor, and an honorary title bestowed upon individuals by approval of the Governor of Nebraska, the only triply landlocked U.S. state.  It is not a military rank, requires no duties, and carries with it no pay or other compensation.  Admirals have the option of joining the Nebraska Admirals Association, a non-profit organization that promotes "The Good Life" of Nebraska.

Maianthemum canadense: Maianthemum canadense (Canadian may-lily, Canada mayflower, false lily-of-the-valley, Canadian lily-of-the-valley, wild lily-of-the-valley, Two-leaved Solomonseal) is a dominant understory perennial flowering plant, native to the sub-boreal conifer forests in Canada and the northern United States, from Yukon and British Columbia east to Newfoundland and south to Nebraska and Pennsylvania, and also in the Appalachian Mountains to northern Georgia.  It can be found growing under both evergreen and deciduous trees.

Sacralism: Sacralism is the confluence of church and state wherein one is called upon to change the other.

Lake Sebago: At 310 acre , Lake Sebago is the largest lake in Harriman State Park in the U.S. state of New York.  The name is Algonquian for "big water".  Operated by the Palisades Interstate Park Commission, Lake Sebago is surrounded by picnic lawns and play fields, and is popular with anglers fishing for landlocked salmon, lake trout, bass, perch and sunfish.  The lake has a swimming beach, hand boat launch (electric motors only) and cabin camping.  Lake Sebago lies near Sloatsburg.  It is located just south of Lake Kanawauke and is accessible by auto from Seven Lakes Drive.

Nebraska: Nebraska is a state that lies in both the Great Plains and the Midwestern United States.  The state is bordered by South Dakota to the north, Iowa to the east and Missouri to the southeast, both across the Missouri River, Kansas to the south, Colorado to the southwest and Wyoming to the west.  It is the only triply landlocked U.S. state.  Nebraska's area is just over 77,220 sq mi (200,000 km) with almost 1.9 million people.  Its state capital is Lincoln, and its largest city is Omaha, which is on the Missouri River.

Capital District, New York: The Capital District, also known as the Capital Region, refers to the metropolitan area surrounding Albany, the capital of the U.S. state of New York.  With a population of 1,170,483 (2013), the Capital District is the fourth largest metropolitan region in the state and the 45th largest in the country.  Companies that have headquarters in Albany include CommerceHub and the Environment One Corporation.  In the 21st century, the Capital District has emerged as a major anchor of Tech Valley, the moniker describing the technologically-focused region of eastern New York State.  The Capital District was first settled by the Dutch in the early 17th century and came under British control in 1664.  Albany has been the permanent capital of the state of New York since 1797.  The Capital District is notable for many historical events that predate the independence of the United States, including the Albany Plan of Union and The Battles of Saratoga.

Metamorphic reaction: A metamorphic reaction is a chemical reaction that takes place during the geological process of metamorphism wherein one assemblage of minerals is transformed into a second assemblage which is stable under the new temperature/pressure conditions resulting in the final stable state of the observed metamorphic rock.

Alder Gulch: Alder Gulch (alternatively called Alder Creek) is a place in the Ruby River valley, in the U.S. state of Montana, where gold was discovered on May 26, 1863 by William Fairweather and a group of men including Barney Hughes, Thomas Cover, Henry Rodgers, Henry Edgar and Bill Sweeney who were returning to the gold fields of Grasshopper Creek, Bannack, Montana.  They were on their way to Yellowstone Country from Bannack but were waylaid by a band of Crow Indians.  After being ordered out of Crow hunting grounds, they crossed the East Slope of the Tobacco Root Mountains and camped for the night in Elk Park, where William "Bill" Fairweather and Henry Edgar discovered gold, while the remaining party was out hunting for meat.  Agreeing to keep the new discovery quiet the group of miners returned to the town of Bannack for supplies.  Unfortunately word leaked out about the new strike, and miners followed the Fairweather party out of town.  The party stopped at the Point of Rocks, part way between Bannack and Alder Gulch, and established the Fairweather Mining District in a miners meeting.  It was agreed that the discoverers were entitled to two claims and first choice.  The first stampede of miners reached Alder Gulch June 6, 1863 and the population swelled to over 10,000 in less than 3 months.  The "Fourteen Mile City" ran the length of the gulch, and included the towns of Junction City, Adobe Town, Nevada City, Central City, Virginia City, Montana, Bear Town, Highland, Pine Grove French Town, Hungry Hollow, and Summit.  Upon arrival the miners lived in brush wickiups, dugouts and under overhanging rocks until cabins could be built.  The first structure built in Virginia City was the Mechanical Bakery.  Virginia City, and Nevada City were the centers of commerce during the height of the Alder Gulch gold rush.  In the first year the area had over 10,000 people living there.  Montana Territory was established in May 1864, and the first territorial capital was Bannock.  The capital then moved to Virginia City, where it remained until 1875.  The Alder Gulch diggings were the richest gold placer deposits ever discovered, and in three years $30,000,000 was taken from them, with $10,000,000 taken out in the first year.  Nowadays, except during summertime, the streets of Virginia City are usually quiet and relatively few visitors find their way to the 16 ton granite monument that marks the spot of that incredible discovery of May 26, 1863.

Plymouth, Michigan: Plymouth is a city in Wayne County in the U.S. state of Michigan.  The population was 9,132 at the 2010 census.  The City of Plymouth is landlocked, being entirely surrounded by the Charter Township of Plymouth.

List of harbors in Arizona: This list of harbors in the U.S. state of Arizona.  Being landlocked, all of the harbors are situated on lakes.

Question: What is the capital of the only triply landlocked U.S. state wherein one can find Maianthemum canadense?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "state_name": {
      "type": "string",
      "description": "The name of the U.S. state that meets the criteria."
    },
    "is_triply_landlocked": {
      "type": "boolean",
      "description": "Indicates if the state is the only triply landlocked U.S. state."
    },
    "plant_found_in_state": {
      "type": "boolean",
      "description": "Indicates if Maianthemum canadense is native to or found in the state."
    },
    "state_capital": {
      "type": "string",
      "description": "The capital city of the identified state."
    }
  },
  "required": [
    "state_name",
    "is_triply_landlocked",
    "plant_found_in_state",
    "state_capital"
  ],
  "additionalProperties": false
}
