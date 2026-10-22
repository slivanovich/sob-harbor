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
Wyarno, Wyoming: Wyarno is an unincorporated community in central Sheridan County, Wyoming, United States.  It lies along Wyoming Highway 336 about 10 miles east of the city of Sheridan, the county seat of Sheridan County.  Although Wyarno is unincorporated, it has a post office, with the ZIP code of 82845.  Public education in the community of Wyarno is provided by Sheridan County School District #2.

Plentywood, Montana: Plentywood is a city in and the county seat of Sheridan County, Montana, United States.  The population was 1,734 at the 2010 census.

Banner, Wyoming: Banner is an unincorporated community in southern Sheridan County, Wyoming, United States.  It lies near Interstate 90, south of the city of Sheridan, the county seat of Sheridan County.  Its elevation is 4580 ft .  Although Banner is unincorporated, it had a post office, with the ZIP code of 82832, which closed in 2004.  Public education in the community of Banner is provided by Sheridan County School District #2.

Sheridan, Wyoming: Sheridan is a city in Sheridan County, Wyoming, United States.  The 2010 census put the population at 17,444 and a Micropolitan Statistical Area of 29,116.  It is the county seat of Sheridan County.

Raymond, Montana: Raymond is an unincorporated community in Sheridan County, Montana, United States, north of Plentywood.  It is famous for its salmon and is located nine miles away from the Canada–US.

Rushville, Nebraska: Rushville is a city in Sheridan County in the state of Nebraska, in the Great Plains region of the United States.  Its population was 890 at the 2010 census.  It is the county seat of Sheridan County.

Lakeside, Nebraska: Lakeside is an unincorporated community in southern Sheridan County, Nebraska, United States.  It lies along Nebraska Highways 2 and 250 south of the city of Rushville, the county seat of Sheridan County.  Its elevation is 3,881 feet (1,183 m).  Although Lakeside is unincorporated, it has a post office, with the ZIP code of 69351.

Kenneth Township, Sheridan County, Kansas: Kenneth Township is a township in Sheridan County, Kansas, United States.  As of the 2010 Census, it had a population of 1,350.  Hoxie, the county seat of Sheridan County, is located in Kenneth Township.

McClusky, North Dakota: McClusky is a city in Sheridan County, North Dakota, United States.  It is the county seat of Sheridan County.  The population was 380 at the 2010 census.  McClusky was founded in 1905.  It is the closest town to the geographical center of North Dakota, which lies about five miles to the southwest.

Leiter, Wyoming: Leiter is an unincorporated community in eastern Sheridan County, Wyoming, United States, along Clear Creek.  It lies along the concurrent U.S. Routes 14 and 16, east of the city of Sheridan, the county seat of Sheridan County.  Its elevation is 3,779 feet (1,152 m).  Although Leiter is unincorporated, it has a post office, with the ZIP code of 82837.  Public education in the community of Clearmont is provided by Sheridan County School District #3.

Question: What city, located South of Raymond, Montana, is the county seat of Sheridan County, Montana?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city."
    },
    "is_county_seat": {
      "type": "boolean",
      "description": "Indicates if the community is a county seat."
    },
    "county_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the county."
        },
        "state": {
          "type": "string",
          "description": "The state where the county is located."
        }
      },
      "required": [
        "name",
        "state"
      ],
      "additionalProperties": false
    },
    "population_2010": {
      "type": "integer",
      "description": "The population of the city according to the 2010 census."
    },
    "location_relative_to_raymond": {
      "type": "string",
      "description": "Describes the city's location relative to Raymond, Montana."
    }
  },
  "required": [
    "city_name",
    "is_county_seat",
    "county_details",
    "location_relative_to_raymond"
  ],
  "additionalProperties": false
}
