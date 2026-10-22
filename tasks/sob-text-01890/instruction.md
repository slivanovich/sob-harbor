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
Gorham, Maine: Gorham is a town in Cumberland County, Maine, United States.  The population was 16,381 at the 2010 census.  The 2012 estimate of Gorham's population was 16,667.  In addition to its urban village center known as Gorham Village or simply "the Village," the town encompasses a number of smaller, unincorporated villages and hamlets with distinct historical identities, including South Gorham, West Gorham, Little Falls, White Rock, and North Gorham.  Gorham is home to one of the three campuses of the University of Southern Maine.  In 2013, Gorham was voted second best town in Maine after Hampden by a financial website.

Westwood (Uniontown, Alabama): Westwood is a historic plantation in Uniontown, Alabama, United States.  The main house was built between 1836 and 1850 by James Lewis Price.  It is in the Greek Revival style with some Italianate influence.  The outbuildings include a smokehouse with architectural detailing identical to the main house, a carriage house, a dairy, and a cook’s quarters.  Westwood Plantation was added to the National Register of Historic Places as a historic district on November 21, 1974.  Boundary increases were made to the district on March 15, 1984 and December 10, 1984.

Fernside-Vacation House for Working Girls: Fernside, or the Vacation House for Working Girls, is a historic former resort hotel at 162 Mountain Road in Princeton, Massachusetts.  It is a complex of three buildings: its main house, a barn that was converted into a playhouse, and a two-car garage.  The core of the main house is a Federal style house built in 1835 by Benjamin Harrington.  The house was converted for use as a summer hotel around 1870, and in 1890 it was acquired by the Working Girls' Vacation Society as a place to provide summer recreation for city working women.  It is around this time that wings were added to the house, and the barn was converted to a playhouse.  The property was used by the Society until it was sold in 1989.  The facility is now owned by McLean Hospital, who used it as a drug treatment center.

Edward Steves Homestead: The Edward Steves Homestead is located in the Bexar County city of San Antonio in the U.S. state of Texas.  It was designed by architect Alfred Giles and designated a Recorded Texas Historic Landmark.  The main house was donated to the San Antonio Conservation Society in 1952.  The organization completely restored the main house as a museum and now conducts daily tours.  The complete homestead property consists of four individual structures: the main house museum, the carriage house, the river house, and the servants' quarters.  It is listed on the National Register of Historic Places listings in Bexar County, Texas, as a contributing structure of the King William Historic District.

John S. Williams House and Farm: John S. Williams House and Farm, also known as Old Chatham Sheepherding Farm and Inn, is a historic home and farm designated a national historic district and located at Chatham in Columbia County, New York.  The district includes seven contributing buildings.  They are: the main house, a farm employee cottage, another cottage, a stone tool shed (originally a smoke house), and three small barns / garages.  The main house is a two story, frame building with a center hall plan.  The house dates to the about 1770, but was extensively enlarged and remodelled in 1935-1936 in the Colonial Revival style, under direction by New York City architects Polhemus & Coffin.

United States House of Representatives Page: United States House of Representatives Page Program was a program run by the United States House of Representatives, under the office of the Clerk of the House, in which voluntary appointed high school juniors applicants acted as non-partisan federal employees in the House of Representatives, providing supplemental administrative support to House operations in a variety of capacities in Washington, D.C., at the United States Capitol.  Pages reported to "Chief Pages", commonly referred to as work bosses (or "House Page Work Supervisors") on the Democratic and Republican sides of the House of Representatives Floor.  As was the practice in Middle Ages, pages were used as a messaging service for the four main House Office Buildings (Rayburn, Longworth, Cannon, and Ford) as well as inside the Capitol.  Other Page responsibilities included: taking statements from members of Congress after speeches (for the Congressional Record), printing and delivering vote reports to various offices, tending members' personal needs while on the floor of the House, managing phones in the cloakrooms, and ringing the bells for votes.  Pages were nominated by representatives based upon a highly competitive application process.  Congressional Pages had served within the U.S. House of Representatives for almost 180 years.

Godillot Place: Godillot Place is a historic country estate at 60 and 65 Jesup Road in Westport, Connecticut.  The main house, now known as the Lyman Building, is Stick style structure, built c. 1880 around a core which is an 1804 farmhouse that now makes up the western section.  The building has asymmetrical massing characteristic of the late 19th century, with a busy roofline that has projecting gable sections and dormers that have decorative shingling and overlaid Stick woodwork.  Across the street from the main house stand a carriage house and barn that date to the time of the major alterations.  The design has been attributed to Palliser, Palliser & Co., a New York City architectural pattern book publisher.

Milwaukee: Milwaukee ( , ) is the largest city in the state of Wisconsin and the fifth-largest city in the Midwestern United States.  The county seat of Milwaukee County, it is on Lake Michigan's western shore.  Ranked by estimated 2014 population, Milwaukee was the 31st largest city in the United States.  The city's estimated population in 2015 was 600,155.  Milwaukee is the main cultural and economic center of the Milwaukee metropolitan area.  It is also part of the larger Milwaukee-Racine-Waukesha combined statistical area, which had an estimated population of 2,026,243 in the 2010 census.

William Diamond: William 'Bill' Diamond (born February 19, 1945) is an American politician and former teacher.  Diamond served as a Democratic State Senator from Maine's 12th District, including his residence in Windham.  He was first elected to the Maine House of Representatives in 1976 and served in the House until 1982, when he was elected to the Maine State Senate.  He served in the Senate until 1986.  In 1989, he succeeded Rodney S. Quinn as Maine's Secretary of State and was re-elected four years later.  He returned to elected office in 2004 when he was elected to the Senate.  Unable to seek re-election due to term-limits in 2012, Diamond was replaced by Republican Gary Plummer.

Rodney S. Quinn: Rodney Sharon Quinn (May 27, 1923 – October 27, 2012) was an American politician from Maine.  A Democrat, he served as the Secretary of State of Maine from 1979 to 1988.  He was first elected to the Maine House of Representatives in 1974, after running three times from Gorham.  He served as Assistant Majority Leader in the 108th legislature (1977-1979).

Question: What was the estimated population in 2012 of the city from which Rodney S. Quinn was elected to the Main House of Representatives in 1974?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city."
    },
    "person_elected": {
      "type": "string",
      "description": "The name of the person whose election history is relevant."
    },
    "election_year": {
      "type": "integer",
      "description": "The year the person was elected to the House of Representatives."
    },
    "estimated_population_year": {
      "type": "integer",
      "description": "The year for which the population estimate is provided."
    },
    "estimated_population": {
      "type": "integer",
      "description": "The estimated population of the city for the specified year."
    }
  },
  "required": [
    "city_name",
    "person_elected",
    "election_year",
    "estimated_population_year",
    "estimated_population"
  ],
  "additionalProperties": false
}
