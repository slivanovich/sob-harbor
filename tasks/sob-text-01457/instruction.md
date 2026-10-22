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
Bruce Poliquin: Bruce Lee Poliquin (born November 1, 1953) is an American businessman and politician.  A Republican, he represents Maine's 2nd congressional district in the United States House of Representatives.  Poliquin was elected to his seat in the 2014 general election.  From 2010 to 2012, he was the Maine State Treasurer.  He was a candidate for the Republican nomination for the U.S. Senate in 2012, finishing second in the primary election.  In January 2017 at the start of the 115th United States Congress, Poliquin is the only Republican representing a House district in New England.

Geography of the Philippines: The Philippines is an archipelago that consists of 7,641 islands with a total land area of 301780 km2 .  The 11 largest islands contain 95% of the total land area.  The largest of these islands is Luzon at about 105000 km2 .  The next largest island is Mindanao at about 95000 km2 .  The archipelago is around 800 km from the Asian mainland and is located between Taiwan and Borneo.

Northern Region, Manitoba: The Northern Region is a region in the Canadian province of Manitoba.  It is situated on the Canadian Shield and includes Manitoba's Hudson Bay coastline.  The major economic activities are mining and tourism.  The region is composed of four census divisions: 19 and 21–23 .  The land area of the region is 438,491.51 km² (169,302.52 mi²), which encompasses 67% of Manitoba's total land area.  The vast majority of the region is undeveloped wilderness.  Its total population at the 2011 census was 88,146, which was only 7.3% of Manitoba's total population in the 2011 census.  The largest municipality is the city of Thompson.  Other major population centers include the city of Flin Flon and the town of The Pas.  Indian reserves comprise more than 49% of the region's population.  There are 54 reserves with a total population of 40,572.  The largest of these are Norway House 17 and Peguis 1B.

Geography of Azerbaijan: Azerbaijan is situated in the Caucasus region of Eurasia.  Three physical features dominate Azerbaijan: the Caspian Sea, whose shoreline forms a natural boundary to the east; the Greater Caucasus mountain range to the north; and the extensive flatlands at the country's center.  About the size of Portugal or the state of Maine, Azerbaijan has a total land area of approximately 86,600 square kilometers, less than 1% of the land area of the former Soviet Union.  Of the three Transcaucasian states, Azerbaijan has the greatest land area.  Special administrative subdivisions are the Nakhchivan Autonomous Republic, which is separated from the rest of Azerbaijan by a strip of Armenian territory, and the Nagorno-Karabakh Autonomous Region, entirely within Azerbaijan.  (The status of Nagorno-Karabakh was under negotiation in 1994.)  Located in the region of the southern Caucasus Mountains, Azerbaijan borders the Caspian Sea to the east, Georgia and Russia to the north, Iran to the south, and Armenia to the southwest and west.  A small part of Nakhchivan also borders Turkey to the northwest.  The capital of Azerbaijan is the ancient city of Baku, which has the largest and best harbor on the Caspian Sea and has long been the center of the republic's oil industry.

List of islands of Tasmania: This is a list of islands of Tasmania, the smallest and southernmost state of Australia.  The Tasmanian mainland itself is an island, with an area of 64,103 km2 - 94.1% of the total land area of the state of Tasmania.  The eleven next largest islands have a combined area of 3,826 km2 , for a cumulative total of 99.75% of the state.  Over 300 smaller islands make up the remaining 173 km2 of total land area.

Zomba District: Zomba District is one of twelve districts in the Southern Region of Malawi, surrounded by the Districts of Chiradzulu, Blantyre, Mulanje, Phalombe, Machinga, Balaka and the Republic of Mozambique to the east.  The total land area is 2,580 km², representing three percent of the total land area of Malawi.  The capital is Zomba.

Maine's 2nd congressional district: Maine's 2nd congressional district is a congressional district in the U.S. state of Maine.  Covering 27326 sqmi , it comprises nearly 80% of the state's total land area.  It is the largest district east of the Mississippi River and the 24th-largest overall.  It is the second-most rural district in the United States, with 72.11% of its population in rural areas, behind only Kentucky's 5th congressional district.

Greater Accra Region: The Greater Accra Region has the smallest area of Ghana's 10 administrative regions, occupying a total land surface of 3,245 square kilometres or 1.4 per cent of the total land area of Ghana.  It is the second most populated region, after the Ashanti Region, with a population of 2,905,726 in 2000, accounting for 15.4 per cent of Ghana’s total population.

Protected areas of Himachal Pradesh: Forests in Himachal Pradesh currently cover an area of nearly 37,691 sqkm , which is about 38.3% of the total land area of the state.  The forests were once considered to be the main source of income of the state and most of the original forests were clear felled.  The emphasis has shifted, however, from exploitation to conservation.  The state government aims to increase forest cover to 50% of the total land area.  There have been various projects, including the establishment of protected areas such as National Parks, designed to preserve and expand the forests.

Ashanti Region: The Ashanti Region is located in south Ghana and is third largest of 10 administrative regions, occupying a total land surface of 24389 km2 or 10.2 per cent of the total land area of Ghana.  In terms of population, however, it is the most populated region with a population of 4,780,380 according to the 2010 census, accounting for 19.4% of Ghana’s total population.  The Ashanti Region is known for its major gold bar and cocoa production.  The largest city and regional capital is Kumasi.

Question: What is the political party of the politician who represents 80% of the state's total land area in Congress?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "political_party": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "political_party"
      ],
      "additionalProperties": false
    },
    "congressional_district": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "state_land_area_percentage": {
          "type": "number",
          "description": "Percentage of the state's total land area covered by the district"
        }
      },
      "required": [
        "name",
        "state_land_area_percentage"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The political party of the politician"
    }
  },
  "required": [
    "politician",
    "congressional_district",
    "answer"
  ],
  "additionalProperties": false
}
