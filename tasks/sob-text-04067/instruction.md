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
University of Maryland, Baltimore County: The University of Maryland, Baltimore County (often referred to as UMBC) is an American public research university, located in Baltimore County, Maryland, United States, mostly in the community of Catonsville, approximately 10 minutes (8.3 miles) from downtown Baltimore City, 9 minutes (6.1 miles) from Baltimore–Washington International Airport (BWI).  With a fall 2016 enrollment of 13,640 students, 48 undergraduate majors, over 60 graduate programs (36 master, 24 doctoral, and 17 graduate certificate programs) and the first university research park in Maryland, UMBC has been named the #1 Up-and-Coming University for six years in a row, since 2009, by "US News & World Report".  In addition, "US News & World Report" has placed UMBC in the top ten for best undergraduate teaching six years in a row, being placed at #5, the second highest-ranked public university.

Munsey Park, New York: Munsey Park is a village in Nassau County, New York, United States.  The population was 2,693 at the 2010 census.

Falls Road station: Falls Road station is a Baltimore Light Rail station in Baltimore, Maryland.  It is the first stop in surrounding suburban Baltimore County while traveling north from downtown Baltimore.  The stop is located near the Mount Washington neighborhood in the Jones Falls Valley, and is often used by commuters as a back-up to Mount Washington for parking when the lot at Mt. Washington is full.  The station is adjacent to Lake Roland Park and Dam (renamed Robert E. Lee Park in the 1940s), constructed in the late 1850s as part of the first segment of the city's new public water supply system in 1860 along the upper Jones Falls stream which flows south through the city emptying into the Inner Harbor of the Patapsco River of Baltimore Harbor and can be viewed from certain parts of the park.  Although only used for several decades as part of the metropolitan area's public water system until shifting in the 1880s to a larger flowing supply piped from the Gunpowder Falls and construction of the first phase at the Loch Raven Reservoir and its taller Dam.  Old Lake Roland and Dam are still owned by the City of Baltimore's Department of Recreation and Parks with its surrounding forested watershed, it is now operated and managed by its partner agency, the Baltimore County Department of Recreation and Parks through a recent contract agreement.

New York Press (historical): The New York Press was a New York City newspaper that began publication in December 1887 and continued publication until July 2, 1916, when its owner Frank Munsey merged it with his newly-purchased "New York Sun".  The "New York Press" published notable writers such as Stephen Crane.

Long Island Electric Railway: The Long Island Electric Railway was a streetcar company operating in Brooklyn, Queens, and Nassau County, New York, United States between 1894 and 1926.  The company was partially owned by the Long Island Consolidated Electric Companies, a holding company for the Long Island Rail Road and partially by August Belmont and the Interborough Rapid Transit Company.  It connected the east end of the Fulton Street El at Crescent Street station in City Line, Brooklyn with Jamaica, Queens, and ran from there to the Nassau County line at Queens Village and to Far Rockaway, Queens via Nassau County.  It also had a connection to Belmont Park.  The New York and Long Island Traction Company used trackage rights over its line from Crescent Street to Queens Village.

Baltimore Convention Center: The Baltimore Convention Center is a convention and exhibition hall located in downtown Baltimore, Maryland.  The Center is a municipal building owned and operated by the City of Baltimore.  The facility was constructed in two separate phases: the original Center, with 425,000 sqft of exhibition and meeting space, opened in August 1979 at a cost of $51.4 million.  A $151 million expansion, which increased the Center's total size to 1225000 sqft , was completed in April 1997.  The 752-room, city-owned Hilton Baltimore hotel opened in August 2008, connected to the convention center by an enclosed skywalk bridge.  Another expansion to the Baltimore Convention Center has been proposed at an estimated cost of $400 million that includes a new 500 room hotel and an 18,500 seat arena; this project is estimated to cost $900 million, this proposal is no longer active and considered dead.  As of March 2016, the State of Maryland is going to explore expanding the Baltimore Convention Center for an estimated cost of $600 million and build a new hotel attached to the expansion.  As of August 2016, the proposal of having a combined expanded convention center, arena and hotel has been revived.  Mayor Stephanie Rawlings-Blake requested a $1 million feasibility study from the Maryland Stadium Authority which was approved on August 2, 2016.

Railroad Magazine: Railroad Magazine was a pulp magazine which first published in October 1906, founded by Frank Anderson Munsey.  A railroad man born in Maine in 1854, he moved to New York City in 1892, where he authored a few books and published periodicals and newspapers in many cities.  The magazine's first offices were located in the Flatiron Building in New York City.  At the time of its founding, there was no organized railroad enthusiast movement, and initially the magazine was targeted towards railroaders and retirees.  The magazine title was later combined with "Railfan" to form the new "Railfan & Railroad", published by Carstens Publications.

Old Nassau County Courthouse (New York): The Old Nassau County Courthouse, also known as the Nassau County Courthouse and the Historic Nassau County Courthouse, is an historic 2-story courthouse building located at 1550 Franklin Avenue in Garden City, Nassau County, New York.  Designed by noted New York City architect William B. Tubby in the Classical Revival style of architecture with a grand rotunda capped by a white dome, it was built of poured-in-place reinforced concrete.  Then governor Theodore Roosevelt laid its cornerstone in 1900 and it was finished in 1901.  Wings designed by Tubby were added in 1916.  Later additions and renovations were 1924-1928 under the supervision of architect William J. Beardsley, who had designed the Dutchess County Court House in Poughkeepsie.

Frank Munsey: Frank Andrew Munsey (21 August 1854 – 22 December 1925) was an American newspaper and magazine publisher and author.  He was born in Mercer, Maine, but spent most of his life in New York City.  The village of Munsey Park, New York is named for him, along with the Munsey Building in downtown Baltimore, Maryland at the southeast corner of North Calvert Street and East Fayette Street.

William D. Boyce: William Dickson "W. D." Boyce (June 16, 1858 – June 11, 1929) was an American newspaper man, entrepreneur, magazine publisher, and explorer.  He was the founder of the Boy Scouts of America (BSA) and the short-lived Lone Scouts of America (LSA).  Born in Allegheny County, Pennsylvania, he acquired a love for the outdoors early in his life.  After working as a schoolteacher and a coal miner, Boyce attended Wooster Academy in Ohio before moving to the Midwest and Canada.  An astute businessman, Boyce successfully established several newspapers, such as "The Commercial" in Winnipeg, Manitoba and the "Lisbon Clipper" in Lisbon, North Dakota.  With his first wife, Mary Jane Beacom, he moved to Chicago to pursue his entrepreneurial ambitions.  There he established the Mutual Newspaper Publishing Company and the weekly "Saturday Blade", which catered to a rural audience and was distributed by thousands of newspaper boys.  With his novel employment of newsboys to boost newspaper sales, Boyce's namesake publishing company maintained a circulation of 500,000 copies per week by 1894.  Boyce strongly supported worker rights, as demonstrated by his businesses' support of labor unions and his concern for his newsboys' well-being.

Question: Frank Andrew Munsey (21 August 1854 – 22 December 1925) was an American newspaper and magazine publisher and author, which village in Nassau County, New York, is named for him, along with the Munsey Building in downtown Baltimore, Maryland?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        },
        "occupation": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of occupations of the person."
        }
      },
      "required": [
        "name",
        "occupation"
      ],
      "additionalProperties": false
    },
    "named_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "entity_type": {
            "type": "string",
            "description": "The type of entity named after the person (e.g., village, building)."
          },
          "entity_name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "location": {
            "type": "string",
            "description": "The geographical location of the entity."
          }
        },
        "required": [
          "entity_type",
          "entity_name",
          "location"
        ],
        "additionalProperties": false
      },
      "description": "A list of entities named after the person."
    },
    "question_answer": {
      "type": "string",
      "description": "The direct answer to the question about the village named after the person."
    }
  },
  "required": [
    "person_of_interest",
    "named_entities",
    "question_answer"
  ],
  "additionalProperties": false
}
