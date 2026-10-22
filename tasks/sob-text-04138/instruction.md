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
WTKS-FM: WTKS-FM is a radio station serving the Orlando and Central Florida areas, airing a hybrid talk radio/alternative rock format.  The station is owned and operated by iHeartMedia and licensed by the (U.S.) Federal Communications Commission to broadcast from Cocoa Beach, Florida (though the studio is located in Maitland, Florida).  WTKS-FM's transmission tower is in Bithlo, Florida.

Cliffwood Beach, New Jersey: Cliffwood Beach is an unincorporated community and census-designated place (CDP) located within Aberdeen Township, in Monmouth County, New Jersey, United States.  As of the 2010 United States Census, the CDP's population was 17,011.  As of the 2010 United States Census, the CDP's population was 3,194.

Sewaren, New Jersey: Sewaren is an unincorporated community and census-designated place (CDP) within Woodbridge Township, in Middlesex County, New Jersey, United States.  As of the 2010 United States Census, the CDP's population was 17,011.  As of the 2010 United States Census, the CDP's population was 2,756.

Ethnic groups in Los Angeles: The 1990 United States Census and 2000 United States Census found that non-Hispanic whites were becoming a minority in Los Angeles.  Estimates for the 2010 United States Census results find Latinos to be approximately half (47-49%) of the city's population, growing from 40% in 2000 and 30-35% in 1990 census.

Brainards, New Jersey: Brainards is an unincorporated community and census-designated place (CDP) located within Harmony Township, in Warren County, New Jersey, United States, that was created as part of the 2010 United States Census.  As of the 2010 United States Census, the CDP's population was 202.  It was formerly known as Martin's Creek.

Blairstown (CDP), New Jersey: Blairstown is an unincorporated community and census-designated place (CDP) located within Blairstown Township, in Warren County, New Jersey, United States, that was created as part of the 2010 United States Census.  As of the 2010 United States Census, the CDP's population was 515.

Anderson, New Jersey: Anderson is a Census-designated place located within Mansfield Township, in Warren County, New Jersey, United States, that was created as part of the 2010 United States Census.  As of the 2010 United States Census, the CDP's population was 342.

Strathmore, New Jersey: Strathmore is an unincorporated community and census-designated place (CDP) within Aberdeen Township, in Monmouth County, New Jersey, United States.  As of the 2010 United States Census, the CDP's population was 17,011.  As of the 2010 United States Census, the CDP's population was 7,258.

Cocoa Beach, Florida: Cocoa Beach is a city in Brevard County, Florida.  The population was 11,231 at the 2010 United States Census.  It is part of the Palm Bay-Melbourne-Titusville, Florida Metropolitan Statistical Area.

Dallas: Dallas ( ) is a city in the U.S. state of Texas.  It is the most populous city in the Dallas–Fort Worth metroplex, which is the fourth most populous metropolitan area in the United States.  The city's population ranks ninth in the U.S. and third in Texas after Houston and San Antonio.  The city's prominence arose from its historical importance as a center for the oil and cotton industries, and its position along numerous railroad lines.  The bulk of the city is in Dallas County, of which it is the county seat; however, sections of the city are located in Collin, Denton, Kaufman, and Rockwall counties.  According to the 2010 United States Census, the city had a population of 1,197,816.  The United States Census Bureau's estimate for the city's population increased to 1,317,929 as of July 1, 2016.

Question: According to the 2010 United States Census, what was the population of the city from which WTKS-FM broadcasts?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city."
    },
    "census_year": {
      "type": "integer",
      "description": "The year of the United States Census."
    },
    "population": {
      "type": "integer",
      "description": "The population of the city according to the specified census."
    },
    "radio_station_call_sign": {
      "type": "string",
      "description": "The call sign of the radio station."
    },
    "broadcast_licensing_location": {
      "type": "string",
      "description": "The type of location from which the station is licensed to broadcast (e.g., city, CDP)."
    }
  },
  "required": [
    "city_name",
    "census_year",
    "population",
    "radio_station_call_sign",
    "broadcast_licensing_location"
  ],
  "additionalProperties": false
}
