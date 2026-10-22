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
Archaeal Richmond Mine acidophilic nanoorganisms: Archaeal Richmond Mine acidophilic nanoorganisms (ARMAN) were first discovered in an extremely acidic mine located in northern California (Richmond Mine at Iron Mountain) by Brett Baker in Jill Banfield's laboratory at the University of California Berkeley.  These novel groups of archaea named ARMAN-1, ARMAN-2 ("Candidatus" Micrarchaeum acidiphilum ARMAN-2 ), and ARMAN-3 were missed by previous PCR-based surveys of the mine community because the ARMANs have several mismatches with commonly used PCR primers for 16S rRNA genes.  Baker "et al." detected them in a later study using shotgun sequencing of the community.  The three groups were originally thought to represent three unique lineages deeply branched within the Euryarchaeota, a subgroup of the Archaea.  However, this has been revised, based on more complete archaeal genomic tree, that they belong to a super phylum named DPANN.  The ARMAN groups now comprise deeply divergent phyla named Micrarchaeota and Parvarchaeota.  Their 16S rRNA genes differ by as much as 17% between the three groups.  Prior to their discovery all of the Archaea shown to be associated with Iron Mountain belonged to the order Thermoplasmatales (e.g., "Ferroplasma acidarmanus").

Burra Burra Mine (Tennessee): The Burra Burra Mine is a copper mine located in Ducktown, Tennessee, in the southeastern United States.  Named for the famous mine in Australia, the Burra Burra Mine extracted over 15 million tons (14 million metric tons) of copper ore during its 60 years of operation between 1899 and 1959.  The mine's remaining structures are listed on the National Register of Historic Places as part of the Burra Burra Mine Historic District.  The site is also home to the Ducktown Basin Museum, and the museum and mine are a Tennessee State Historic Site operated in partnership with the Tennessee Historical Commission.

Big Dan Mine: Big Dan Mine is an abandoned underground mine in Northeastern Ontario, Canada.  It is located about 1 km southwest of Net Lake and just west of the Ontario Northland Railway in east-central Strathy Township.  It is named after Dan O'Connor, who first claimed the site in the 1890s.

Discovery Mine: The Discovery Mine was a gold mine 81 kilometers northeast (approx bearing of 15 degrees) of Yellowknife, Northwest Territories that operated between 1950 and 1969.  Gold was discovered here by Alfred Giauque in 1944.  A complete townsite, on Giauque Lake, was established by the company to house workers and their families.  The mine produced one million troy ounces (31,000 kg) of gold from one million tons of ore.  The abandoned townsite, not accessible by road, was demolished in 2005.

Sago Mine disaster: The Sago Mine disaster was a coal mine explosion on January 2, 2006, at the Sago Mine in Sago, West Virginia, United States, near the Upshur County seat of Buckhannon.  The blast and collapse trapped 13 miners for nearly two days; only one survived.  It was the worst mining disaster in the United States since the Jim Walter Resources Mine disaster in Alabama on September 23, 2001, and the worst disaster in West Virginia since the 1968 Farmington Mine disaster.  It was exceeded four years later by the Upper Big Branch Mine disaster, also a coal mine explosion in West Virginia, which killed 29 miners in April 2010.

Jackson Mine: The Jackson Mine is an open pit iron mine in Negaunee, Michigan, extracting resources from the Marquette Iron Range.  The first iron mine in the Lake Superior region, Jackson Mine was designated as a Michigan State Historic Site in 1956 and listed on the National Register of Historic Places in 1971.  The Lake Superior Mining Institute said, the mine "is attractive in the iron ore region of Michigan and the entire Lake Superior region, because of the fact it was here that the first discovery of iron ore was made, here the first mining was done, and from its ore the first iron was manufactured."  Multiple other mines soon followed the Jackson's lead, establishing the foundation of the economy of the entire region.  The mine is located northwest of intersection of Business M-28 and Cornish Town Road.

Mount Baker Gold Rush: The Mount Baker Gold Rush (1897 to mid 1920's) occurred in Whatcom County, Washington, United States, upon the discovery of the Lone Jack Mine.  The Mount Baker area was flooded with prospectors which led to the staking of many claims both patented and unpatented.  The most notable mines staked soon after the Lone Jack are the Boundary Red Mountain Mine, Garget Mine (a.k.a. Gold Run Mine), Gold Basin Mine, Silver Tip Mine, and the Evergreen Mine.

O'Connor Mine: O'Connor Mine, also known as Milestone Mine, is an abandoned surface mine in Northeastern Ontario, Canada.  It is located about 1 km southwest of the town of Temagami near the Northeast Arm of Lake Temagami in northern Strathcona Township.  It is named after John O'Connor who first developed the mine site.

Calhoun Mine: The Calhoun Mine is perhaps the oldest and best-known mine in Lumpkin County, Georgia.  When gold was discovered in Lumpkin County in 1828, which led to the Georgia Gold Rush in 1829, it was discovered on 239 acre owned by Robert Obar.  After at least two intermediary sales, the land was purchased by Senator John C. Calhoun of South Carolina, who was also the 7th Vice President of the United States.  Calhoun started a mining company to mine the land and later allowed his son-in-law Thomas Green Clemson, the founder of Clemson University, to manage it.  The ore deposit was a very rich deposit and, according to an 1856 letter from Clemson to his brother-in-law, was still producing significant quantities of gold nearly 30 years after its initial discovery on the land.  This mine - along with the Consolidated Mine and the Loud Mine - were some of the most productive mines in the Georgia Gold Belt.

Leckie Mine: Leckie Mine, also known as Penrose Mine and Little Dan Mine, is an abandoned gold producing underground mine in Northeastern Ontario, Canada, located on the eastern shore of Arsenic Lake 4 km north of the town of Temagami.  It is entirely owned by Temagami Gold Inc.  An estimated 483,500 tonnes of ore remain in the mine, which could contain 102,720 ounces of gold.

Question: Between Discovery Mine and Big Dan Mine, which mine was named after Dan O'Connor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mine_named_after_person": {
      "type": "string",
      "description": "The name of the mine that was named after the specified person."
    },
    "person_name": {
      "type": "string",
      "description": "The name of the person the mine was named after."
    },
    "other_mine_considered": {
      "type": "string",
      "description": "The name of the other mine that was considered in the comparison."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why the identified mine was named after the person, based on the context."
    }
  },
  "required": [
    "mine_named_after_person",
    "person_name",
    "other_mine_considered",
    "reasoning"
  ],
  "additionalProperties": false
}
