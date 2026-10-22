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
The Nightingale (novel): The Nightingale is a novel by the American writer Agnes Sligh Turnbull (1888–1982) set in a fictional rural Western Pennsylvania village (but much like the author's birthplace of New Alexandria, Pennsylvania, about thirty miles east of Pittsburgh) at the turn of the 20th century.

The Gown of Glory: The Gown of Glory is a 1952 novel by the American writer Agnes Sligh Turnbull (1888–1982).  It is set in a fictional rural village of Ladykirk, which is much like the author's birthplace of New Alexandria, Pennsylvania, about thirty miles east of Pittsburgh.

TerraTrike: TerraTrike is a brand of recumbent tadpole tricycles manufactured by WizWheelz Inc.  TerraTrike is based in Grand Rapids, Michigan USA.  TerraTrike's 2013 product line consists of 5 models: Rover, Rambler, Tour II, Sportster, Tandem Pro.  Each model has 3 to 5 different component levels to meet each riders needs.

Kent, Sierra Leone: Kent is a coastal fishing village around the peninsular in the Western Area Rural District of Sierra Leone.  Kent lies approximately thirty miles east of Freetown.  Kent is known for its large beaches and its strong fishing community.

U.S. Route 16 in Michigan: US Highway 16 (US 16), also called Grand River Avenue for much of its length in the state, was one of the principal pre-Interstate roads in the state of Michigan.  Before the creation of the United States Numbered Highway System in 1926, the highway had been designated M-16.  The modern route of Grand River Avenue cuts across the Lower Peninsula in a northwest–southeast fashion from near Grand Rapids to Detroit.  Before the late 1950s and early 1960s, US 16 followed other roads between Muskegon and Grand Rapids, and then Grand River Avenue through Lansing to Detroit.  In the years immediately preceding the creation of the Interstate Highway System, US 16 was shifted from older roads to newer freeways.  Later, it was co-designated as an Interstate.  When the gap in the freeway was filled in around Lansing, the US 16 designation was decommissioned in the state.  The freeway was then solely designated Interstate 96 (I-96) east of Grand Rapids and I-196 west of that city.

The Day Must Dawn: The Day Must Dawn is a 1942 historical novel by the American writer Agnes Sligh Turnbull (1888–1982) set in 1777 in Hanna's Town, Pennsylvania, a frontier settlement thirty miles east of Pittsburgh.

Santo Domingo, San Vicente: Santo Domingo is a municipality in the San Vicente department of El Salvador.  It is located about thirty miles East of San Vicente.

Fort Polk: Fort Polk is a United States Army installation located in Vernon Parish, approximately ten miles east of Leesville, Louisiana, and thirty miles north of DeRidder in Beauregard Parish, Louisiana.

Claude, Texas: Claude is a city in and the county seat of Armstrong County, Texas, United States.  The population was 1,196 at the 2010 census.  It is located east of Amarillo in the south Texas Panhandle.  Claude is part of the Amarillo Metropolitan Statistical Area but is some thirty miles east of Amarillo.

Grand Rapids, Michigan: Grand Rapids is the second-largest city in Michigan, and the largest city in West Michigan.  It is on the Grand River about 30 mi east of Lake Michigan.  As of the 2010 census, the city population was 188,040.  In 2010, the Grand Rapids metropolitan area had a population of 1,005,648, and the combined statistical area of Grand Rapids-Muskegon-Holland had a population of 1,321,557.  Grand Rapids is the county seat of Kent County.

Question: TerraTrike is based in a city that is on the Grand River about thirty miles east of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company."
    },
    "company_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the company is based."
        },
        "state": {
          "type": "string",
          "description": "The state where the company is based."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "geographical_relationship": {
      "type": "object",
      "properties": {
        "distance_miles": {
          "type": "integer",
          "description": "The distance in miles."
        },
        "direction": {
          "type": "string",
          "description": "The cardinal direction relative to the reference point."
        },
        "reference_point": {
          "type": "string",
          "description": "The geographical feature or location that the city is relative to."
        }
      },
      "required": [
        "distance_miles",
        "direction",
        "reference_point"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "company_location",
    "geographical_relationship"
  ],
  "additionalProperties": false
}
