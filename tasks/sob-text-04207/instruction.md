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
Deerfield Beach, Florida: Deerfield Beach is a city in Broward County, Florida, United States.  It is located just south of the Palm Beach County line.  The city is named for the numerous deer that once roamed the area.  As of the 2010 United States Census, the population was 75,018.  It is a principal city of the Miami metropolitan area, which was home to an estimated 6,012,331 people at the 2015 census.

Deerfield Beach Island: Deerfield Beach Island, also colloquially known as DBI and Deerfield Cay, is an island off the eastern mainland of Boca Raton and Deerfield Beach, Florida, United States.

Deerfield Beach Arboretum: The Deerfield Beach Arboretum, also known as the Tree Zoo, is an arboretum and botanical garden located at 2841 West Hillsboro Boulevard, Deerfield Beach, Florida, United States.  It covers 9 acres (3.6 ha).  It is owned by the city of Deerfield Beach and managed by The Friends of the Deerfield Beach Arboretum.  It contains more than 200 different species of trees and palms from around the world, with more than 50 different species of flowering trees.

Florida State Road 810: State Road 810 (SR 810), locally known as Hillsboro Boulevard, is east–west street in Broward County, Florida.  The western terminus of SR 810 is an intersection with US 441–SR 7 on the city line between Coconut Creek and Parkland, and the eastern terminus is at an intersection with Ocean Drive (SR A1A) in Deerfield Beach.  Within Deerfield Beach, Hillsboro Boulevard forms the axis separating the north and south sections of the street numbering system.  The road is within one mile (1.6 km) south of neighboring Palm Beach County throughout its entire route.

Jeremy Kellem: Jeremy Kellem (born June 6, 1989) is an American football defensive back who is currently a free agent.  He played college football at Middle Tennessee State University and attended Deerfield Beach High School in Deerfield Beach, Florida.  He has also been a member of the New Orleans VooDoo and Omaha Nighthawks.

Palm Beach County, Florida: Palm Beach County is a county located in the state of Florida, directly north of Broward County.  As of the 2010 census, the population was 1,320,134, making it the third-most populous county in Florida.  The largest city and county seat is West Palm Beach.  Named after one of its oldest settlements, Palm Beach, the county was established in 1909, after being split from Dade County.  The county's modern-day boundaries were established in 1963.  Palm Beach County is one of the three counties in South Florida which make up the Miami metropolitan area, which was home to an estimated 6,012,331 people at the 2015 census.

South Florida Railway Museum: The South Florida Railway Museum is a railroad museum located in the Deerfield Beach Seaboard Air Line Railway Station in Deerfield Beach, Florida.  It is operated by volunteers.

Deerfield Beach High School: Deerfield Beach High School (DBHS) is a public high school in Deerfield Beach, Florida.  It is part of Broward School District and has an enrollment of approximately 2,409.

Deerfield Beach Elementary School: The Deerfield Beach Elementary School is a historic school in Deerfield Beach, Florida.  It is located at 651 Northeast 1st Street.  On April 16, 1990, it was added to the U.S. National Register of Historic Places.

Deerfield Beach station: Deerfield Beach station, also known as the Old Deerfield Beach Seaboard Air Line Railway Station, is a train station in Deerfield Beach, Florida.  It is served by Amtrak intercity rail and Tri-Rail commuter rail.

Question: Which county in Florida is the third-most populous and is north of Deerfield Beach?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "county_name": {
      "type": "string",
      "description": "The name of the county."
    },
    "population_details": {
      "type": "object",
      "properties": {
        "count": {
          "type": "integer",
          "description": "The population count of the county."
        },
        "census_year": {
          "type": "integer",
          "description": "The year the population census was taken."
        },
        "population_rank_description": {
          "type": "string",
          "description": "A description of the county's population rank."
        }
      },
      "required": [
        "count",
        "census_year",
        "population_rank_description"
      ],
      "additionalProperties": false
    },
    "location_relative_to_deerfield_beach": {
      "type": "string",
      "description": "Describes the county's location relative to Deerfield Beach."
    }
  },
  "required": [
    "county_name",
    "population_details",
    "location_relative_to_deerfield_beach"
  ],
  "additionalProperties": false
}
