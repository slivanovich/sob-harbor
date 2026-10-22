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
Clayton Lake, Maine: Clayton Lake is an unincorporated village in Aroostook County, Maine, United States.  The community is located on the north shore of its eponymous lake within the North Maine Woods in southwestern Aroostook County.

Penobscot Indian Island Reservation: Penobscot Indian Island Reservation is an Indian reservation for the Penobscot Tribe of Maine, a federally recognized tribe of the Penobscot in Penobscot County, Maine, United States, near Old Town.  The population was 610 at the 2010 census.  The reservation extends for many miles alongside 15 towns and two unorganized territories in a thin string along the Penobscot River, from its base at Indian Island, near Old Town and Milford, northward to the vicinity of East Millinocket, almost entirely in Penobscot County.  A small, uninhabited part of the reservation is in South Aroostook, Aroostook County, by which it passes along its way northward.

Don Voisine: Don Voisine (born 1952 in Fort Kent, Maine) is an American abstract painter living in the Williamsburg neighborhood of Brooklyn, New York, USA.  In the fall of 2016 Voisine a 15 year survey of his work, "X/V," was organized by the Center for Maine Contemporary Art, Rockland, ME.  In 1997 he was elected a member of American Abstract Artists and became President of the group in 2004.  Voisine was elected to the National Academy in 2010.  His work is included in the public collections of the Corcoran Gallery of Art, Washington, DC, Cincinnati Art Museum, Peabody Essex Museum, Salem MA, the Portland Museum of Art, Portland, ME, the Missoula Art Museum in Missoula, MT and the National Academy, New York, NY.

Cary Plantation, Maine: Cary Plantation is a plantation in Aroostook County, Maine.  As of the 2010 census, it had a population of 218.  In July 2015, Cary Plantation residents began a plan to deorganize and become residents of the Maine Unorganized Territory.  However, in March 2016, the Maine Legislature rejected Cary Plantation's application, citing the financial burden deorganization would add to the remaining municipalities in Aroostook County.

Eagle Lake, Maine: Eagle Lake is a town in Aroostook County, Maine, United States.  The population was 864 at the 2010 census.  The town was named by a body of troops heading from Bangor to the Aroostook War for the many eagles that they saw around the lake.  49.0% of the population speaks French, reflecting a trend in Northeastern Maine.

Houlton (CDP), Maine: Houlton is a census-designated place (CDP) comprising the main village within the town of Houlton in Aroostook County, Maine, United States.  The population of the CDP was 4,856 at the 2010 census, out of a population of 6,123 for the entire town.  Houlton is the county seat of Aroostook County.  The northern terminus of Interstate 95 and eastern terminus of U.S. Route 2 are just east of the CDP at the Canada–United States border.

Aroostook National Wildlife Refuge: Aroostook National Wildlife Refuge is located on part of the former Loring Air Force Base, in Aroostook County, Maine.  It was established in 1998, when 4700 acre were transferred from the United States Air Force to the United States Fish and Wildlife Service.  This refuge also administers some 2400 acre of wetland conservation easements throughout Aroostook County.  It is close to the state park where visitors hike for particular seasons.  In a portion of Maine where the landscape is dominated by agricultural crops such as potatoes and broccoli, Aroostook National Wildlife Refuge protects valuable wildlife habitat.  The variety of habitat types attracts a diversity of wildlife species.

Fort Kent, Maine: Fort Kent is a town in Aroostook County, Maine, United States.  The population was 4,097 in the 2010 census.  Fort Kent is home to an Olympic biathlete training center, an annual CAN-AM dogsled race, and the Fort Kent Blockhouse, built in reaction to the Aroostook War and in modern times designated a national historic site.  Principal industries include agriculture (particularly potatoes and forestry) and textiles.  Fort Kent is the northern terminus of U.S. 1 and the ending point of the Northern Forest Canoe Trail.  Fort Kent signed a lease agreement with the Fish River Flying Club on July 8, 2011 to repair, maintain, and operate the local municipal airport, which had been closed since the 1980s.

Woodland, Aroostook County, Maine: Woodland is a town in Aroostook County, Maine, United States.  The population was 1,213 at the 2010 census.  Because the state of Maine has a law stating that no two towns may share the same name, Woodland of Aroostook County and Woodland of Washington County found themselves before the Maine State Supreme Court in the late 1990s.  Because it was founded as a township first, the Woodland of Aroostook County was allowed to keep its name and Woodland of Washington County was ordered by the court to choose a new name: "Baileyville."

Presque Isle, Maine: Presque Isle is the commercial center and largest city in Aroostook County, Maine, United States.  The population was 9,171 in 2015 as estimated by the US Census, a decrease from the count of 9,692 in the 2010 Census.  The city is home to the University of Maine at Presque Isle, Northern Maine Community College, Husson University Presque Isle, Northern Maine Fairgrounds, The Aroostook Centre Mall, and the Northern Maine Regional Airport.

Question: What was the population of this town in Aroostook County, Maine, that was the birthplace of Don Voisine?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose birthplace is being queried."
    },
    "birthplace_name": {
      "type": "string",
      "description": "The name of the town where the person was born."
    },
    "birthplace_county": {
      "type": "string",
      "description": "The county of the birthplace."
    },
    "birthplace_population": {
      "type": "integer",
      "description": "The population of the birthplace."
    },
    "population_census_year": {
      "type": "integer",
      "description": "The year of the census for the reported population."
    }
  },
  "required": [
    "person_name",
    "birthplace_name",
    "birthplace_county",
    "birthplace_population",
    "population_census_year"
  ],
  "additionalProperties": false
}
