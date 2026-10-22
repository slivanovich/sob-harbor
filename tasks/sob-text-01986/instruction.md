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
Oswego, Montana: Oswego is an unincorporated community in Valley County, Montana, United States.  It is located along U.S. Route 2 between the cities of Frazer and Wolf Point.  Oswego is located on the Fort Peck Indiean Reservation.

Fort Peck, Montana: Fort Peck is a town in Valley County, Montana, United States.  The population was 233 at the 2010 census.

Fort Peck Dam: The Fort Peck Dam is the highest of six major dams along the Missouri River, located in northeast Montana in the United States, near Glasgow, and adjacent to the community of Fort Peck.  At 21026 ft in length and over 250 ft in height, it is the largest hydraulically filled dam in the United States, and creates Fort Peck Lake, the fifth largest man-made lake in the U.S., more than 130 mi long, 200 ft deep, and it has a 1520 mi shoreline which is longer than the state of California's coastline.  It lies within the Charles M. Russell National Wildlife Refuge.  The dam and the 134 mi lake exist for the purposes of hydroelectric power generation, flood control, and water quality management.

Wolf Point, Montana: Wolf Point is a city in and the county seat of Roosevelt County, Montana, United States.  The population was 2,621 at the 2010 census.  It is the largest community on the Fort Peck Indian Reservation.  Wolf Point is the home of the annual Wild Horse Stampede, held every year during the second weekend of July.  Wolf Point's Wild Horse Stampede is the oldest rodeo in Montana, and has been called the "Grandaddy of Montana Rodeos".

Montana Highway 117: Montana Highway 117 is a 13.1 mi state highway in the U.S. state of Montana.  Formerly Secondary Highway 249, the route allows traffic from Montana Highway 24 at Fort Peck to travel north to U.S. Route 2 at Nashua, providing a shortcut between the two routes, as well as providing access from the north to the Fort Peck Dam and Fort Peck Lake.

Fort Peck Theatre: The Fort Peck Theatre was built as a temporary structure in 1934 in Fort Peck, Montana to serve as a movie theatre.  It is also known as the Fort Peck Summer Theatre.  The theater was designed in a pseudo-Swiss-chalet style as an amenity for the 50,000 U.S. Army Corps of Engineers workers and their families at the Fort Peck Dam project.  The interior features open-truss wood construction, with handcrafted light fixtures fabricated in Corps of Engineers workshops.  The theater survived to become a permanent facility, and in 2008 was in use as a community theater.

Glasgow, Montana: Glasgow is a city in and the county seat of Valley County, Montana, United States, with an estimated population of 3,414 as of 2015.

Fort Peck Indian Agency: The Fort Peck Agency of the Bureau of Indian Affairs is responsible for the Fort Peck Indian Reservation is located near Wolf Point, Montana.

Tiber Dam: Tiber Dam, located in southern Liberty County in northern Montana, USA, is a dam on the Marias River which forms Lake Elwell, also known as Tiber Reservoir.  Construction on the dam began in 1952 and it was complete in 1956.  Between 1967 and 1969, a dyke was added to the southern rim of the reservoir near the dam due to difficulties with the spillway settling.  From 1976 to 1989, the spillway was rehabilitated.  The dam is also considered one of the biggest earth-fill dams in the world, along with Fort Peck Dam.

Fort Peck Lake: Fort Peck Lake, or Lake Fort Peck, is a major reservoir in Montana, formed by the Fort Peck Dam on the Missouri River.  The lake lies in the eastern prairie region of Montana approximately 140 mi east of Great Falls and 120 mi north of Billings, reaching into portions of six counties.

Question: Fort Peck Dam is located near the county seat of Valley County, Montana, a city with what population in 2015?

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
      "description": "The name of the county for which the city is the county seat."
    },
    "is_county_seat": {
      "type": "boolean",
      "description": "Indicates if the city is the county seat."
    },
    "population_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year for which the population is reported."
        },
        "count": {
          "type": "integer",
          "description": "The estimated population count."
        }
      },
      "required": [
        "year",
        "count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "city_name",
    "county_name",
    "is_county_seat",
    "population_details"
  ],
  "additionalProperties": false
}
