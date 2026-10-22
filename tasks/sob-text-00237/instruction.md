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
Newton, Georgia: Newton is a city in Baker County, Georgia, United States.  As of the 2010 census, the city population was 654.  The city is the county seat of Baker County.

Baker County, Georgia: Baker County is a county in Georgia.  As of the 2010 census, the population was 3,451.  The county seat and only city is Newton.  The county was created December 12, 1825 from the eastern portion of Early County by an act of the Georgia General Assembly and is named for Colonel John Baker, a hero of the American Revolutionary War.

Mineral Wells, Texas: Mineral Wells is a city in Palo Pinto and Parker counties in the U.S. state of Texas.  The population was 16,788 at the 2010 census (14,644 in Palo Pinto and 2144 in Parker).  The city is named for mineral springs in the area, which were highly popular in the early 1900s.  Mineral Wells is most famous for its Baker Hotel.

Macclenny, Florida: Macclenny is a city in Baker County, Florida and is one of the principal municipalities comprising Greater Jacksonville.  The population was 6,374 at the 2010 census, up from 4,459 in 2000.  It is the county seat of Baker County.

Elkhart, Kansas: Elkhart is a city in and the county seat of Morton County, Kansas, United States.  The south edge of the city is the Kansas-Oklahoma state border.  As of the 2010 census, the city population was 2,205.

Baldwin City, Kansas: Baldwin City is a city in Douglas County, Kansas, United States about 12 mi south of Lawrence and 15 mi west of Gardner.  As of the 2010 census, the city population was 4,515.  The city is home to Baker University, the state's oldest four-year university.

Baker County, Oregon: Baker County is a county in the U.S. state of Oregon.  As of the 2010 census, the population was 16,134.  The county seat and largest city is Baker City.  The county was split from the eastern part of Wasco County.  Union County and Malheur County were set off from Baker County in 1864 and 1887 respectively.  It is named after Edward Dickinson Baker, a senator from Oregon who was killed at Ball's Bluff, a battle of the Civil War in Virginia in 1861.

Baker City, Oregon: Baker City is a city in and the county seat of Baker County, Oregon, United States.  It was named after Edward D. Baker, the only U.S. Senator ever killed in military combat.  The population was 9,828 at the 2010 census.

Baker, Louisiana: Baker is a small city in East Baton Rouge Parish, Louisiana, United States, and a part of the Baton Rouge Metropolitan Statistical Area.  It is the fourth-largest city in East Baton Rouge Parish.  The population was 13,895 as of the 2010 census, an increase of 102 persons from the 2000 tabulation of 13,793.

Thane Baker: Walter Thane Baker (born October 4, 1931 in Elkhart, Kansas) is an American former sprinter and winner of the gold medal in the 4x100 m relay at the 1956 Summer Olympics in Melbourne, Australia, with a new world record of 39.5 seconds.  At those Olympics Baker also won a silver medal in the 100-meter and a bronze in the 200-meter.  At the 1952 Summer Olympics in Helsinki, he won a silver medal in the 200-meter.

Question: Walter Thane Baker was born in a city with a population of what as of the 2010 census?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "birth_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the person was born."
        },
        "state": {
          "type": "string",
          "description": "The state where the person was born."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "population_data": {
      "type": "object",
      "properties": {
        "census_year": {
          "type": "integer",
          "description": "The year of the census."
        },
        "city_population": {
          "type": "integer",
          "description": "The population of the city according to the specified census."
        }
      },
      "required": [
        "census_year",
        "city_population"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "birth_location",
    "population_data"
  ],
  "additionalProperties": false
}
