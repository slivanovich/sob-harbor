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
St. Clair, Michigan: St. Clair is a city in St. Clair County in the eastern "Thumb" of the U.S. state of Michigan.  The population was 5,485 at the 2010 census.  The city is located on the St. Clair River near the southeast corner of St. Clair Township.

Lake St. Clair Metropark: Lake St. Clair Metropark/Metro Beach Metropark is a 770-acre unit of the Huron-Clinton Metroparks system located roughly 20 miles (32 km) northeast of downtown Detroit, Michigan in Harrison Township, Macomb County.  Lake St. Clair Metropark has been in existence since 1950 and has seen many changes since then.  Originally named St. Clair Metropolitan Beach, it was renamed in 1953 to Metropolitan Beach Metropark and later shortened to Metro Beach Metropark.  On December 8, 2011, the Board of Commissioners for the Huron-Clinton Metroparks approved changing the name to Lake St. Clair Metropark.  The park is located at Jefferson Avenue and Metropolitan Parkway (16 Mile Road) and there are signs to Lake St. Clair Metropark on Interstate 94 (I-94).

Chip St. Clair: Chip Anthony St. Clair (born August 1, 1975) is an American author and motivational speaker, best known for his inspirational memoir, "The Butterfly Garden: Surviving Childhood on the Run with one of America's Most Wanted".  St. Clair's story has been featured on "Dateline" and "Good Morning America" among others.  In 2004, St. Clair worked with legislators and helped to create and pass the "Identity Theft Protection Act" in Michigan.  In 2005, he received a U.S. Congressional Record on behalf of his child advocacy work.  Prior to founding his own organization, St. Clair was Regional Director of the Michigan chapter of Justice for Children, where he made tremendous strides in aiding children caught up in the nation’s distressed child welfare system.  He created legislative initiatives, community awareness programs, and internship programs that still resonate among victims, survivors, and key stakeholders in the child welfare community.  His direct involvement in the chapter’s casework played a substantial role in the apprehension of two known child predators whose brutality toward children grabbed national headlines.

Georgetown, Guyana: Georgetown is the capital of Guyana, located in Region 4, which is also known as the Demerara-Mahaica region.  It is the country's largest urban centre.  It is situated on the Atlantic Ocean coast at the mouth of the Demerara River and it was nicknamed 'Garden City of the Caribbean.'

Lake St. Clair: Lake St. Clair (French: "Lac Sainte-Claire" ) is a freshwater lake that lies between the Canadian province of Ontario and the U.S. state of Michigan.  It was named after Clare of Assisi, on whose feast day it was navigated and christened by French Catholic explorers in 1679.  It is part of the Great Lakes system, and along with the St. Clair River and Detroit River, Lake St. Clair connects Lake Huron (to its north) with Lake Erie (to its south).  It has a total surface area of about 430 sqmi and average depth of just 11 ft ; to ensure an uninterrupted waterway, government agencies on both sides of the lake have maintained a deep shipping channel through the shallow lake for more than a century.

Belle River Power Plant: Belle River Power Plant is a major coal- and natural gas-fired power plant owned by Detroit Edison, a subsidiary of DTE Energy.  It is located in St. Clair County, Michigan, on the peninsula formed by the St. Clair and Belle rivers.  The plant was built across M-29 from the St. Clair Power Plant in East China, Michigan, and shares the coal delivery terminal with it.  The Belle River plant shares cooling water from the St. Clair River with its sister plant.  Five oil-fueled internal combustion generators (named IC1, IC2, 3, 4, and 5) were built in 1981, with the total output 13.75 megawatt.  Coal-fired unit 1 of the Belle River plant was completed in 1984, followed by a similar unit 2 in 1985.  Each unit has a nameplate capacity of 697.5 MWe, however the coal-fired plant as a whole generates 1260 MWe all year around.  In 1999, three peaker natural-gas fired turbines (named 12-1, 12-2, and 13-1) were added, with the total name-plate capacity of 256 MWe.

Gairy St. Clair: Gairy St. Clair (born 2 February 1975 in Georgetown, Guyana) is a professional boxer in the junior lightweight (130 lb) division.  He is the former IBF world junior-lightweight champion.

Saint Clair Area School District: The St. Clair Area School District is a diminutive, suburban public school district in Schuylkill County, Pennsylvania.  Centered on the borough of St. Clair, it also encompasses the boroughs of Middleport and New Philadelphia, plus the townships of Blythe Township, New Castle Township, and East Norwegian Township.  The district is one of the 500 public school districts of Pennsylvania.  Saint Clair Area School District encompasses approximately 48 sqmi .  According to 2000 federal census data, it served a resident population of 7,020.  By 2010, the US Census Bureau reported that the district's resident population declined to 6,695 people.  The educational attainment levels for the St. Clair Area School District population (25 years old and over) were 82.6% high school graduates and 9.8% college graduates.

Gloriana St. Clair: Gloriana St. Clair (born 1939) is a pioneer in the field of academic librarianship, as well as a scholar of Norse Mythology and its relationship to the works of J.R.R. Tolkien.  She is currently the Principal Investigator of the Olive Executable Archive as well as the official University Liaison to the Pittsburgh chapter of the Osher Lifelong Learning Institute at Carnegie Mellon University.  She is Dean Emerita of Carnegie Mellon University Libraries (1998-2013).  Before coming to Carnegie Mellon, St. Clair held leadership positions at several other universities.  St. Clair attended the University of California, Berkeley, receiving a bachelor's degree in English in 1962 and a master's degree in library science in 1963.

St. Clair Power Plant: The Saint Clair Power Plant is a major coal- and oil-fired power plant owned by Detroit Edison, a subsidiary of DTE Energy.  It is located in St. Clair County, Michigan, on the west bank of St. Clair River.  The plant is across M-29 from the newer Belle River Power Plant in East China, Michigan.  The first four units of St. Clair were built in 1953–1954.  Since then, three more generating units have been added to the plant.  The St. Clair Power Plant generates 1982 megawatts in total.  It is Detroit Edison's second largest power producer.  The power plant has a large impact on the local economy, employing about 300 workers.

Question: What is the nickname of Gairy St. Clair's hometown?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "hometown_name": {
      "type": "string",
      "description": "The name of the person's hometown."
    },
    "hometown_country": {
      "type": "string",
      "description": "The country where the hometown is located."
    },
    "hometown_nickname": {
      "type": "string",
      "description": "The nickname of the person's hometown."
    }
  },
  "required": [
    "person_name",
    "hometown_name",
    "hometown_country",
    "hometown_nickname"
  ],
  "additionalProperties": false
}
