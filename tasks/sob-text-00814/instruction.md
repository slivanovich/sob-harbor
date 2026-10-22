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
Daniel Burnham Jr: Daniel Hudson Burnham, Jr. (1886–1961), was an architect and urban planner based in Chicago and one of the sons of renowned planner Daniel H. Burnham.  Burnham, Jr., was director of public works for the Century of Progress 1933-34 World's Fair in Chicago, the same role his father held for the World's Columbian Exposition of 1893.

John Wellborn Root: John Wellborn Root (January 10, 1850 – January 15, 1891) was an American architect who was based in Chicago with Daniel Burnham.  He was one of the founders of the Chicago School style.  Two of his buildings have been designated a National Historic Landmark; others have been designated Chicago landmarks and listed on the National Register of Historic Places.  In 1958, he received the AIA Gold Medal.

Daniel Burnham: Daniel Hudson Burnham, FAIA (September 4, 1846 – June 1, 1912) was an American architect and urban designer.  He was the Director of Works for the World's Columbian Exposition in Chicago.

John Wellborn Root, Jr.: John Wellborn Root, Jr. (1887–1963) was a significant United States architect based in Chicago.  He was the son of architect John Wellborn Root.  As a young man, he graduated from Cornell University and studied architecture at Paris' École nationale supérieure des Beaux-Arts, where he became friends with John Augur Holabird, the son of another famous Chicago architect.  Root returned to the States and joined his friend on the architectural staff at Holabird & Roche in 1919.

Western Association of Architects: The Western Association of Architects (WAA) was an American professional body founded in Chicago in 1884 separately from the American Institute of Architects (AIA) by John Wellborn Root, Daniel Burnham, Dankmar Adler, and Louis Sullivan, because they felt slighted by East Coast architects of the AIA.  "Members consisted of architects from the Midwest and the South with chapters forming in many states.  The WAA was the first architectural organization to petition for licensure of architects.  Many architects were members of both WAA and AIA..." The WAA merged with the AIA in 1889.

Burnham Park (Philippines): Burnham Park is a 32.84 hectare urban park located at the heart of the Baguio, in the Philippines.  It was named after the American architect and urban planner, Daniel Hudson Burnham who laid the plans for the city.  Several stretch of roads around the park lead to Camp John Hay, a former recreational base of the United States Armed Forces in the Philippines.

Union Stock Yard Gate: The Union Stock Yard Gate, located on Exchange Avenue at Peoria Street, was the entrance to the famous Union Stock Yards in Chicago.  The gate was probably designed by John Wellborn Root of Burnham and Root around 1875, and is the only significant structural element of the stock yards to survive.  It was designated a National Historic Landmark in 1981.  The plaza surrounding the gate also includes the city's principal memorial to its firefighters.

Rookery Building: The Rookery Building is a historic landmark located at 209 South LaSalle Street in the Loop community area of Chicago in Cook County, Illinois, United States.  Completed by John Wellborn Root and Daniel Burnham of Burnham and Root in 1888, it is considered one of their masterpiece buildings, and was once the location of their office.  The building measures 181 ft , is twelve stories tall and is considered the oldest standing high-rise in Chicago.  It has a unique style with exterior load-bearing walls and an interior steel frame, which provided a transition between accepted and new building techniques.  The lobby was remodeled in 1905 by Frank Lloyd Wright.  Beginning in 1989, the lobby was restored to the original Wright design.

Society for Savings Building: The Society for Savings Building, also known as the Society Corp.  Building, is a high-rise building on Public Square in downtown Cleveland, Ohio, United States.  The building was constructed in 1889, and stood as the tallest building in Cleveland until 1896, when it was surpassed by the 221-foot (67 m) Guardian Bank Building.  The building stands 152 feet (46 m) tall, with 10 floors.  The Society for Savings Building is often considered to be the first modern skyscraper in Cleveland and the state of Ohio.  It was designed by John Wellborn Root of the Chicago-based architectural firm Burnham & Root.

Burnham and Root: Burnham and Root was one of Chicago's most famous architectural companies of the nineteenth century.  It was established by John Wellborn Root and Daniel Hudson Burnham.

Question: Who was born first John Wellborn Root or  Daniel Hudson Burnham? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the first person."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the second person."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "object",
      "properties": {
        "earlier_born_person_name": {
          "type": "string",
          "description": "The name of the person who was born earlier."
        },
        "birth_year_difference_years": {
          "type": "integer",
          "description": "The difference in birth years between the two individuals."
        }
      },
      "required": [
        "earlier_born_person_name",
        "birth_year_difference_years"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_1",
    "person_2",
    "comparison_result"
  ],
  "additionalProperties": false
}
