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
East Hanover Township, New Jersey: East Hanover Township is a township in Morris County, New Jersey, United States.  As of the 2010 United States Census, the township's population was 11,157, reflecting a decline of 236 (-2.1%) from the 11,393 counted in the 2000 Census, which had in turn increased by 1,467 (+14.8%) from the 9,926 counted in the 1990 Census.  The manufacturing plant of Mondelēz International (formerly Nabisco) and the pharmaceutical company Novartis are located in East Hanover.

Hanover Park Regional High School District: The Hanover Park Regional High School District is a comprehensive regional public school district that serves students in ninth through twelfth grades from three communities in Morris County, New Jersey, United States.  Students come from East Hanover Township, Florham Park and Hanover Township.

New Jersey Route 10: Route 10 is a 23.51 mi state highway in the northern part of the U.S. state of New Jersey.  It runs from an intersection with U.S. Route 46 (US 46) in Roxbury Township, Morris County east to County Route 577 (CR 577)/CR 677 (Prospect Avenue) in West Orange, Essex County.  Route 10 is a major route through northern New Jersey that runs through Ledgewood, East Hanover, and Livingston.  It is a four-lane highway for most of its length with the exception of the easternmost part of the route.  Route 10 features intersections with many major roads including Route 53 and US 202 in Morris Plains and Interstate 287 (I-287) in Hanover Township.

Whippany Park High School: Whippany Park High School is a four-year comprehensive public high school that serves students in ninth through twelfth grade from Hanover Township in Morris County, New Jersey, United States, operating as one of the two secondary schools of the Hanover Park Regional High School District.  The other school in the district, Hanover Park High School, serves students from East Hanover and Florham Park.  The school is located in the Whippany section of Hanover Township.

Hanover Park High School: Hanover Park High School is a four-year comprehensive public high school that serves students in ninth through twelfth grades from East Hanover Township and Florham Park, in Morris County, New Jersey, United States, operating as one of the two secondary schools of the Hanover Park Regional High School District.  Hanover Park's sister school is Whippany Park High School, which serves students from Hanover Township, where the school is located.  The school opened in 1956.

Lower Dauphin School District: Lower Dauphin School District is a midsized, suburban public school district located in central Pennsylvania.  The Lower Dauphin School District encompasses approximately 89 sqmi .  The Lower Dauphin School District spans Hummelstown, Pennsylvania, East Hanover Township, Pennsylvania, Londonderry Township, Dauphin County, Pennsylvania, South Hanover Township, Pennsylvania, and Conewago Township, Dauphin County, Pennsylvania.  According to 2000 federal census data it served a resident population of 22,546.  By 2010, the district's population increased to 24,747 people.  The educational attainment levels for the Lower Dauphin School District population (25 years old and over) were 91.2% high school graduates and 28.2% college graduates.  The district is one of the 500 public school districts of Pennsylvania.

Cedar Knolls, New Jersey: Cedar Knolls is an unincorporated community located within Hanover Township in Morris County, New Jersey, United States.  It is part of Hanover Township along with Whippany.

East Hanover School District: The East Hanover School District is a community public school district that serves students in pre-kindergarten through eighth grade from East Hanover, in Morris County, New Jersey, United States.

27th Legislative District (New Jersey): New Jersey's 27th Legislative District is one of 40 in the New Jersey Legislature.  As of the 2011 apportionment, the district includes the Essex and Morris County municipalities of Caldwell Borough, Chatham Township, East Hanover Township, Essex Fells Borough, Florham Park Borough, Hanover Township, Harding Township, Livingston Township, Madison Borough, Maplewood Township, Millburn Township, Roseland Borough, South Orange Village Township, and West Orange Township.

Novartis: Novartis International AG is a Swiss multinational pharmaceutical company based in Basel, Switzerland.  It is one of the largest pharmaceutical companies by both market cap and sales.

Question: East Hanover Township is a township in Morris County, New Jersey, the manufacturing plant of which pharmaceutical company, a Swiss multinational pharmaceutical company, are located in East Hanover?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the pharmaceutical company."
    },
    "company_type": {
      "type": "string",
      "description": "The type of company, e.g., 'pharmaceutical company'."
    },
    "headquarters_country": {
      "type": "string",
      "description": "The country where the company is headquartered."
    },
    "is_multinational": {
      "type": "boolean",
      "description": "Indicates if the company is multinational."
    },
    "plant_location_township": {
      "type": "string",
      "description": "The township where the company's plant is located."
    },
    "plant_location_county": {
      "type": "string",
      "description": "The county where the company's plant is located."
    },
    "plant_location_state": {
      "type": "string",
      "description": "The state where the company's plant is located."
    }
  },
  "required": [
    "company_name",
    "company_type",
    "headquarters_country",
    "is_multinational",
    "plant_location_township",
    "plant_location_county",
    "plant_location_state"
  ],
  "additionalProperties": false
}
