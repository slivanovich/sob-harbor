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
Stella K. Abraham High School for Girls: Stella K. Abraham High School for Girls is a Modern Orthodox Jewish day school, a college preparatory high school for grades 9-12, located in Hewlett Bay Park in Nassau County, New York, United States.  As of 2011 it had some 340 students and approximately 50 teachers.  There are a total of 1,054 alumnae.  The principal of 9th and 10th grade is Raizi Chechick, and the principal of 11th and 12th grade is Dr. Tzipora Meier.  Head of school is currently Helen Spirn.

Pretoria High School for Girls: Pretoria High School for Girls, also called Girls High or PHSG, is a public, fee charging, English medium high school for girls located in Hatfield, Pretoria, Gauteng, South Africa.  It is the sister school to Pretoria Boys High School.

North Shore School District: North Shore Central School District is a public school district located in northern Nassau County, in the North Shore region of Long Island, New York.  It encompasses the villages and hamlets of Glenwood Landing, Glen Head, Sea Cliff, Old Brookville and parts of Greenvale and Roslyn Harbor.  About 2,790 students, grades K–12, attend the North Shore Public Schools.

South Shore (Long Island): The South Shore of Long Island, in the U.S. state of New York, is the area along Long Island's Atlantic Ocean shoreline.  Though some consider the South Shore to include parts of Queens, particularly the beach communities in the Rockaways such as Belle Harbor, the term is generally used to refer to the Long Island coastline in Nassau and Suffolk counties.  It is often used as a generic name for the entire southern half of Long Island rather than just the area immediately adjacent to the coastline.

Sound Shore Parkway: Sound Shore Parkway was a formerly proposed parkway intended to run primarily across the north shore of Long Island between the City of Glen Cove and the Town of Smithtown, New York.  Like Ocean Parkway on the south shore, and Lake Ontario State Parkway in Upstate New York, it was meant to provide both recreational use and a seaview, in this case a view of the Long Island Sound.  The parkway was to include two new state parks in Lattingtown, and Eatons Neck.

Long Island Sound: Long Island Sound is a tidal estuary of the Atlantic Ocean, lying between the eastern shores of Bronx County, New York City, southern Westchester County, and Connecticut to the north, and the North Shore of Long Island, to the south.  From east to west, the sound stretches 110 miles (177 km) from the East River in New York City, along the North Shore of Long Island, to Block Island Sound.  A mix of freshwater from tributaries and saltwater from the ocean, Long Island Sound is 21 miles (34 km) at its widest point and varies in depth from 65 to .

South Shore High School (Chicago): South Shore International College Preparatory High School (commonly known as South Shore) is a public 4–year selective enrollment high school located in the South Shore neighborhood on the south–east side of Chicago, Illinois, United States.  Opened in 1940 as South Shore High School, South Shore is a part of the Chicago Public Schools district.

Hewlett Bay Park, New York: Hewlett Bay Park is a village in Nassau County, New York in the USA, on the South Shore of Long Island.  As of the United States 2010 Census, the village population was 404.

Carmel College, Auckland: Carmel College is a Catholic secondary school for girls located in Milford on Auckland's North Shore.  It was established by the Sisters of Mercy in 1957 starting with a student roll of only fifteen girls.  The College's brother school is nearby Rosmini College.

Hewlett, New York: Hewlett is a hamlet and census-designated place (CDP) in Nassau County, New York on the South Shore of Long Island.  As of the United States 2010 Census, the CDP population was 6,819.  Hewlett Bay Park and Hewlett Harbor consist of many mansions and harbor villas with very large property, a few dating back to the time of the American Revolution.  This area, like Back/Old Lawrence is unique because its rural affluence is similar in character to the more well known Gold Coast of the North Shore instead of being more urbanized like the rest of the South Shore of Nassau County.

Question: Is Stella K. Abraham High School for Girls located on the south shore or north shore of Long Island? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "school_name": {
      "type": "string",
      "description": "The name of the high school."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "village": {
          "type": "string",
          "description": "The village where the school is located."
        },
        "county": {
          "type": "string",
          "description": "The county where the school is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the school is located."
        }
      },
      "required": [
        "village",
        "county",
        "state"
      ],
      "additionalProperties": false
    },
    "long_island_shore_designation": {
      "type": "string",
      "description": "Whether the location is on the South Shore or North Shore of Long Island."
    },
    "is_on_south_shore": {
      "type": "boolean",
      "description": "True if the school is located on the South Shore of Long Island, false otherwise."
    }
  },
  "required": [
    "school_name",
    "location_details",
    "long_island_shore_designation",
    "is_on_south_shore"
  ],
  "additionalProperties": false
}
