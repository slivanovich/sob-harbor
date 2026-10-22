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
Swan Inn: The Swan Inn (formerly thought to have been called the Saracen's Head) is a Grade II listed pub dating back several centuries.  It is located in the City of Westminster at 66 Bayswater Road, London W2.  Today a popular tourist haunt at the edge of Hyde Park, run by Fuller's Brewery, it was in former times a resting point for stage coaches proceeding toward London.

Chelsea, Alabama: Chelsea is a city in Shelby County, Alabama, United States.  It is part of the Birmingham metropolitan area.  Chelsea was incorporated on March 1, 1996, with a population of 906.  At the 2000 census the population was 2,949.  According to the U.S. Census Bureau, the 2010 population for Chelsea was 10,183.  Its seasonal campsite for visitors is Hargis Retreat which began in 1984.  Chelsea is widely considered the fastest growing city in Shelby County, which is the fastest growing county in the state of Alabama.

Chelsea, Oklahoma: Chelsea is a town in Rogers County, Oklahoma.  The population was 1,964 at the 2010 census, a decline of 8.3 percent from 2,136 at the 2000 census.  Chelsea was named after the area in London, England, by Charles Peach, a railroad official who was a native of that city.  Chelsea used to be one of the largest towns in Oklahoma.  Chelsea is the home of Oklahoma's first oil well.

Moorhouse, Cumbria: Moorhouse is a village on the B5307 road in the civil parish of Burgh by Sands in the Carlisle District, located in the English county of Cumbria.  It is near the city of Carlisle.  It has a pub called 'The Royal Oak Inn' and a football team called 'Moorhouse Football Club', who play in the Carlisle City Sunday League: Premier Division.

Foreland, Isle of Wight: Foreland or Forelands is the easternmost point of the Isle of Wight, part of the village of Bembridge.  It is located about 6.5 miles due south of the city of Portsmouth on the British mainland, separated by the eastern reaches of the Solent.  It is characterised by a pub called the Crab and Lobster Inn and various beach huts plus a beach cafe and a coast guard lookout.  In the sea are the reefs of Bembridge Ledge which is rich in edible crabs, lobsters and spider crabs and shoals of mackerel.  In the Crab & Lobster Inn are photographs of the many shipwrecks, which included the submarine HMS Alliance, now a museum ship at Gosport and the First World War troopship the S.S. Mehndi carrying troops from South Africa, with great loss of life.

Chelsea (CDP), Wisconsin: Chelsea is an unincorporated census-designated place located in the town of Chelsea, Taylor County, Wisconsin, United States.  Chelsea is 5 mi west-southwest of Rib Lake.  As of the 2010 census, its population is 113.

Chelsea Pub &amp; Inn: Chelsea Pub & Inn was a historic pub and hotel, founded in 1858 in Atlantic City, New Jersey.  The structure has been a part of the Atlantic City’s landscape since 1880.  The building was formerly Grossman’s Kosher Hotel.

Llansannor: It has a population of roughly 200 people.  It contains a parish church, a pub (the City Inn, now closed), a primary school and a village hall, which has recently been rebuilt thanks to the efforts of the parishioners.

Chelsea Garden Cemetery: Chelsea Garden Cemetery is a historic cemetery bounded by Shawmut Street, and Central and Chester Avenues in Chelsea, Massachusetts.  The cemetery was established in 1841 to provide the city a burying ground in the then-fashionable rural cemetery style.  It has a network of paths which wind over the undulating 3 acre of terrain.  One of its focal points was originally a man-made pond, located at the lowest point in the cemetery; it was filled in late in the 19th century.  The cemetery is estimated to hold more than 1,600 burials; due to the transient nature of the Chelsea population over the period of the cemetery's existence, with little historical continuity, it has had a history neglect and vandalism.  The fringes of the cemetery were also damaged by the 1908 fire that devastated the city (which also destroyed some cemetery records).

Atlantic City, New Jersey: Atlantic City is a resort city in Atlantic County, New Jersey, United States, known for its casinos, boardwalks, and beaches.  In 2010, it had a population of 39,558.  The city was incorporated on May 1, 1854, from portions of Egg Harbor Township and Galloway Township.  It borders Absecon, Brigantine, Pleasantville, Ventnor City, West Atlantic City, and the Atlantic Ocean.

Question: What was the population of the city in 2010 where Chelsea Pub & Inn is located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city where the Chelsea Pub & Inn is located."
    },
    "state": {
      "type": "string",
      "description": "The state where the city is located."
    },
    "country": {
      "type": "string",
      "description": "The country where the city is located."
    },
    "population_year": {
      "type": "integer",
      "description": "The year for which the population is provided."
    },
    "population_count": {
      "type": "integer",
      "description": "The population count for the specified year."
    }
  },
  "required": [
    "city_name",
    "state",
    "country",
    "population_year",
    "population_count"
  ],
  "additionalProperties": false
}
