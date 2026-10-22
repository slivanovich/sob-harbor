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
Southern Columbia Area School District: Southern Columbia Area School District is a small, rural, public school district located in Catawissa, Pennsylvania.  It serves communities in two counties.  In Columbia County the district serves: Catawissa Borough, Catawissa Township, Locust Township, Roaring Creek Township, and Cleveland Township.  This includes the boroughs of: Slabtown and Numidia.  In Northumberland County it serves Ralpho Township.  Southern Columbia Area School District encompasses approximately 108 sqmi .  According to 2000 federal census data, it serves a resident population of 9,803.  By 2010, the US Census Bureau reported that the district's population increased to 10,386 people.  The per capita income of residents was $18,969 in 2009, while the median family income was $45,889.  In the Commonwealth, the median family income was $49,501 and the United States median family income was $49,445, in 2010.  The district is one of the 500 public school districts of Pennsylvania.

Lake City, Florida: Lake City is the county seat of Columbia County, Florida, United States.  As of the 2010 census, the city's population was 12,046.  It is the principal city of the Lake City Micropolitan Statistical Area, which is composed of Columbia County, and had a 2010 population of 67,531.

WUAF-LP: WUAF-LP (107.9 FM, is a Gospel music formatted radio station primarily serving the Lake City, Florida, area, owned by Angel Ministries of Lake City Inc.

Columbia County, Pennsylvania: Columbia County is a county located in the U.S. state of Pennsylvania.  As of the 2010 census, the population was 67,295.  Its county seat is Bloomsburg.  The county was created on March 22, 1813, from part of Northumberland County and named for "Columbia", a poetic name for the United States that alludes to Christopher Columbus.

Benton Area School District: The Benton Area School District is a diminutive, rural, public school district.  Benton Area School District serves the boroughs of Benton and Stillwater and Benton Township, Fishing Creek Township, Jackson Township and Sugarloaf Township in Columbia County, Pennsylvania.  The District encompasses approximately 97 sqmi .  According to 2000 federal census data, it served a resident population of 5,260.  By 2010, the District's population declined to 5,231 people.  It is one of eight public school districts operating in Columbia County and is one of the 500 public school districts of Pennsylvania in 2016.

Columbia County, Arkansas: Columbia County is a county located in the U.S. state of Arkansas.  As of the 2010 census, the population was 24,552.  The county seat is Magnolia.  The county was formed on December 17, 1852, and was named for Christopher Columbus.  The Magnolia, AR Micropolitan Statistical Area includes all of Columbia County.

Columbia County, Washington: Columbia County is a county located in the U.S. state of Washington.  As of the 2010 census, the population was 4,078, making it the third-least populous county in Washington.  The county seat and largest city is Dayton.  The county was created out of Walla Walla County on November 11, 1875 and is named after the Columbia River.

Bloomsburg, Pennsylvania: Bloomsburg is a town in Columbia County, Pennsylvania, United States, located 40 mi southwest of Wilkes-Barre along the Susquehanna River.  It is the county seat of Columbia County and the only incorporated town in Pennsylvania.  As of the 2010 census, Bloomsburg had a population of 14,855, with an estimated population of 14,519 in 2013.

Portage, Wisconsin: Portage is a city in and the county seat of Columbia County, Wisconsin, United States.  The population was 10,662 at the 2010 census making it the largest city in Columbia County.  The city is part of the Madison Metropolitan Statistical Area.

Magnolia, Arkansas: Magnolia is a city in Columbia County, Arkansas, United States.  As of the 2010 census the population was 11,577.  The city is the county seat of Columbia County.

Question: WUAF-LP serves this county seat of Columbia County, Florida, with what population according to the 2010 census

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city."
    },
    "county_name": {
      "type": "string",
      "description": "The name of the county the city is the seat of."
    },
    "state_name": {
      "type": "string",
      "description": "The name of the state the city is located in."
    },
    "is_county_seat": {
      "type": "boolean",
      "description": "Indicates if the city is a county seat."
    },
    "population_2010": {
      "type": "integer",
      "description": "The population of the city according to the 2010 census."
    },
    "radio_station_serving_city": {
      "type": "string",
      "description": "The name of the radio station primarily serving this city."
    }
  },
  "required": [
    "city_name",
    "county_name",
    "state_name",
    "is_county_seat",
    "population_2010",
    "radio_station_serving_city"
  ],
  "additionalProperties": false
}
