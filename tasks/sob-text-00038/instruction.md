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
Beardstown High School: Beardstown Junior/Senior High School, also known as Beardstown Middle/High School or BHS, is a public school for grades 6 through 12 at located at 500 East 15th Street in Beardstown, Illinois, a small city in Cass County, Illinois, in the Midwestern United States.  BHS is the only middle school and only high school of Beardstown Community Unit School District 15.  The campus is located 45 miles northwest of Springfield, Illinois, and serves a mixed village and rural residential community.  The school does not lie within a metropolitan or micropolitan statistical area.

Clear Lake, Cass County, Illinois: Clear Lake is an unincorporated community in Cass County, Illinois, United States.  Clear Lake is near the south bank of the Sangamon River, west of Chandlerville and northeast of Beardstown.

Sangamon, Illinois: Sangamon is an unincorporated community in Oakley Township, Macon County, Illinois, United States.  Sangamon is located along the Norfolk Southern Railway, 5.5 mi east-northeast of downtown Decatur.

Sangamon Ordnance Plant: The Sangamon Ordnance Plant was a United States Army ammunition manufacturing facility constructed and operated during World War II.  It was located west of Illiopolis in Sangamon County, Illinois encompassing 20,000 acres (80 km²).  It began as two separate plants, the Sangamon and the Oak Ordnance Plants, separated by Illinois Route 36 and operated by Remington Rand and Johnson & Johnson respectively.  Prior to the end of World War II, the facility was consolidated into the Sangamon Ordnance Plant, operated by Remington Rand.

Philadelphia and Columbia Railroad: Philadelphia and Columbia Railroad (P&CR) (1834) was one of the earliest commercial railroads in the United States, running 82 mi from Philadelphia to Columbia, Pennsylvania, it was built by the Pennsylvania Canal Commission in lieu of a canal from Columbia to Philadelphia; in 1857 it became part of the Pennsylvania Railroad, and its trackage lives on today operated by Norfolk-Southern.  The Philadelphia and Columbia Railroad's western terminus was located near the former ferry site known as Wright's Ferry, in the town once of that name, but now Columbia in Lancaster County.  There the P&CR met with the Pennsylvania Canal—navigations and improvements on the Susquehanna River east bank approximately 30 mi south of Harrisburg, Pennsylvania.  Most of its right-of-way was obtained by the actions of the Pennsylvania Canal Commission which operated the railroad under the various enabling acts of the Pennsylvania legislature known as the Main Line of Public Works in support of a far sighted plan to link the whole state by canals.  With an engineering study reporting back a finding that obtaining sufficient waters to flood the intended 80+ mile canal from Philadelphia to Columbia, the Canal Commission and legislature authorized the railway on the right of way intended for the canal.

Beardstown and Sangamon Canal: The Beardstown and Sangamon Canal was a canal plan developed in the mid-1830s, with avid backing by Abraham Lincoln, then an Illinois state legislator, to make large portions of the Sangamon River between Springfield, Illinois, and Beardstown, Illinois, navigable via a canal to the junction with the Illinois River, which in turn flows into the Mississippi River.

Alamo Canal: The Alamo Canal (Spanish: "Canal del Álamo" ) was a 14 mi long waterway that connected the Colorado River to the head of the Alamo River.  The canal was constructed to provide irrigation to the Imperial Valley.  A small portion of the canal was located in the United States but the majority of the canal was located in Mexico.  The Alamo Canal is also known as the Imperial Canal.

Port Mercer Canal House: The Port Mercer Canal House is a historic house along the Delaware and Raritan Canal.  It is located at 4278 Quakerbridge Road in the Port Mercer section of Lawrence Township, Mercer County, New Jersey, United States, near the border of West Windsor Township and Princeton, New Jersey.  The house was built in the 1830s as housing for bridgetender and his family.  The bridgetender was needed to open the swing bridge when canal boats came through, then close it to allow traffic to cross over the canal.  From approximately 1900 to 1934, the bridgetender was John Arrowsmith.  He and his wife lived in the three bedroom house with their eight children.  The Arrowsmiths loved living at the house and their children enjoyed sleeping outside by the canal in the summer and skating on the frozen canal to Trenton in the winter.

Alexandria Canal (Virginia): The Alexandria Canal was a canal in the United States that connected the city of Alexandria to Georgetown in the District of Columbia.

Archer, Illinois: Archer is an unincorporated community in Curran Township, Sangamon County, Illinois, United States.  Archer is located on the Sangamon Valley Trail on the western border of Springfield.

Question: Are the Beardstown and Sangamon Canal, and Alexandria Canal both located in the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "canals_in_united_states": {
      "type": "boolean",
      "description": "True if both specified canals are located in the United States, false otherwise."
    },
    "canal_evaluation": {
      "type": "array",
      "description": "Details for each canal evaluated regarding its location.",
      "items": {
        "type": "object",
        "properties": {
          "canal_name": {
            "type": "string",
            "description": "The name of the canal."
          },
          "is_located_in_united_states": {
            "type": "boolean",
            "description": "True if the canal is located in the United States."
          },
          "us_locations": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of US states or districts where the canal is located or passes through."
          }
        },
        "required": [
          "canal_name",
          "is_located_in_united_states",
          "us_locations"
        ],
        "additionalProperties": false
      }
    },
    "total_canals_evaluated": {
      "type": "integer",
      "description": "The total number of canals checked for their location."
    }
  },
  "required": [
    "canals_in_united_states",
    "canal_evaluation",
    "total_canals_evaluated"
  ],
  "additionalProperties": false
}
