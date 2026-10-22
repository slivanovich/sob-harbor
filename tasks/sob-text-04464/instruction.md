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
Walker-Woodward-Schaffer House: Walker-Woodward-Schaffer House, also known as the Jane Darwell Birthplace, is a historic home located at Palmyra, Marion County, Missouri.  It was built about 1868, and is a two-story, three bay, Italianate style brick dwelling.  It has a two-story rear wing with a two-story gallery porch.  Both sections have hipped roofs with bracketed cornices.  A verandah spans the front of the house.  It was the birthplace of actress Jane Darwell.

Greenwood, Mississippi: Greenwood is a city in and the county seat of Leflore County, Mississippi, located at the eastern edge of the Mississippi Delta, approximately 96 miles north of Jackson, Mississippi, and 130 miles south of Memphis, Tennessee.  It was a center of cotton planter culture in the 19th century.

Benjamin West Birthplace: The Benjamin West Birthplace is a historic home located on the campus of Swarthmore College in Swarthmore, Delaware County, Pennsylvania.  It was the birthplace of artist Benjamin West (1738-1820), who was an influential mentor to a generation of American painters, including Gilbert Stuart and Charles Willson Peale.  His birthplace was declared a National Historic Landmark in 1965, and added to the National Register of Historic Places in 1966.  It presently serves as Swarthmore's visitor information center.

James Brothers' House and Farm: James Brothers' House and Farm, also known as the Birthplace of Jesse James, is a historic home and farm complex located near Kearney, Clay County, Missouri.  The original log section of the farmhouse was built about 1822; it was later enlarged with a wood frame addition to form a "T"-plan dwelling.  The James Brothers' House is significant as the birthplace of Jesse James and Frank James and has been selected as the most important site related to the James Brothers in Missouri.  In 1974 Clay County, Missouri, bought it.  The county operates the site as a house museum and historic site.

Montross, Virginia: Montross is a town in Westmoreland County, Virginia, United States.  The population was 315 at the 2000 census.  It is the county seat of Westmoreland County.  Located in the historic Northern Neck of Virginia, Montross is near the George Washington Birthplace National Monument and Stratford Hall Plantation (birthplace of Robert E. Lee, Richard Henry Lee, and Francis Lightfoot Lee).

Valerie, California: Valerie is an unincorporated community in Riverside County, California, United States.  Valerie is located on California State Route 86 7.7 mi south of Coachella.

Valerie Brisco-Hooks: Valerie Ann Brisco-Hooks (born July 6, 1960 in Greenwood, Mississippi) won three gold medals as an Olympic track and field athlete at the 1984 Olympics at Los Angeles, California, making her the first Olympian to win gold medals in both the 200- and 400-meter races at a single Olympics.

Church Hill (Lexington, Virginia): Church Hill, also known as Timber Ridge Plantation, is a historic plantation house located near Lexington, Rockbridge County, Virginia.  It was built circa 1848, and is a two-story, three bay, rectangular brick Greek Revival style dwelling.  It has a one-story, rear kitchen ell.  The house features stuccoed Doric order pilasters at the corners and midpoints of the long sides.  Timber Ridge Plantation was the birthplace of Sam Houston (1793-1863).  On the property is a non-contributing log building which tradition claims was constructed from logs salvaged from the Sam Houston birthplace cabin.  The cabin is believed to have been located at the site of the kitchen ell.

June Griffith: June Marcia Griffith ("married" Collison) (born June 16, 1957) is a retired Guyanese track and field athlete.  She participated in both sprint and jumping events.  She represented Guyana in the 400 meters at the 1984 Olympics, making it to the semi-final round before finishing a non-qualifying 5th place in her semi final behind the eventual gold (Valerie Brisco-Hooks) and bronze (Kathy Smallwood-Cook) medalists.

Sheffield, Alabama: Sheffield is a city in Colbert County, Alabama, United States, and is included in the Shoals metropolitan area.  As of the 2010 census, the population of the city was 9,039.  Sheffield is the birthplace of "country-soul pioneer" and songwriter Arthur Alexander, French horn player Willie Ruff, notable attorney, actor, former senator and presidential contender Fred Thompson, Watergate committee U.S. Senator Howell Heflin and U.S. Senator Mitch McConnell, whose father was working in nearby Athens when he was born.  It sometimes is referred to as "the City of Senators" due to the births of Heflin, McConnell and Thompson within its borders.  Col. Harland Sanders worked in the Sheffield depot for Southern Railway in the 1900s.  It is also home to the Muscle Shoals Sound Studio where many popular 20th century musicians recorded their work, including Alexander and Ruff.  It is the site of historic Helen Keller Hospital, formerly known as Colbert County Hospital and originally constructed in 1921.  It was changed to Helen Keller Hospital in 1979, and Keller's birthplace Ivy Green is located less than one mile southwest of the hospital in adjacent Tuscumbia.

Question: The birthplace of Valerie Brisco-Hooks is located in which county?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "birthplace_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city of birth."
        },
        "state": {
          "type": "string",
          "description": "The state of birth."
        },
        "county": {
          "type": "string",
          "description": "The county of birth."
        }
      },
      "required": [
        "city",
        "state",
        "county"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "string",
      "description": "The direct answer to the question about the county."
    }
  },
  "required": [
    "person",
    "birthplace_location",
    "question_answer"
  ],
  "additionalProperties": false
}
