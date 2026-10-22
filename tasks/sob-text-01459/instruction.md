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
Radnor Township, Peoria County, Illinois: Radnor Township is located in Peoria County, Illinois.  As of the 2010 census, its population was 3,613 and it contained 1,330 housing units.  Radnor Township was named after Radnor, Pennsylvania.

Wayne, Pennsylvania: Wayne is an unincorporated community located on the Main Line, centered in Delaware County, Pennsylvania, United States.  While the center of Wayne is in Radnor Township, Wayne extends into both Tredyffrin Township in Chester County and Upper Merion Township in Montgomery County.  The center of Wayne was designated the Downtown Wayne Historic District in 2012.  Considering the large area served by the Wayne post office, the community may extend slightly into Easttown Township, Chester County, as well.

Villanova School of Business: The Villanova School of Business is Villanova University's business school and offers nine undergraduate degrees, six graduate programs, an executive MBA program, and several executive education programs.  The programs are accredited by the Association to Advance Collegiate Schools of Business (AACSB).  The school is located in Villanova, Pennsylvania (part of Radnor Township).  s of 2016 , "Bloomberg's Businessweek" ranked Villanova School of Business first for undergraduate business education.

Radnor Township School District: Radnor Township School District is a school district that serves Radnor Township, Pennsylvania and has 3 elementary schools, one middle school, and one high school.  Due to the mostly affluent demographic of the Main Line (of which the Radnor Township School District is a part) some locals place their children in local private schools.  Those that do put their children in the Radnor Township School District generally do so for its reputation as an excellent school district, as it has several blue ribbon schools.

Strafford, Pennsylvania: Strafford is an unincorporated community in the southeastern part of the U.S. state of Pennsylvania, located partly in Tredyffrin Township, Chester County, and partly in Radnor Township, Delaware County.  It is served by its own stop on the SEPTA Paoli/Thorndale Line regional rail train.  The SEPTA station at Strafford is one of the few buildings that survives from the 1876 Centennial Exposition at Philadelphia.  It is also the site of the Strafford Friends School, and Old Eagle School.  It is in the Eastern Standard time zone.  Elevation is 440 feet.

Jason Steinhauer: Jason Steinhauer is an American public historian and inaugural director of the Albert Lepage Center for History in the Public Interest at Villanova University.  He is a published writer, contributor to TIME, and creator of the field of History Communication.  He previously worked at The John W. Kluge Center at the Library of Congress.

University of Southern California: The University of Southern California (USC or SC) is a private research university located in Los Angeles, California.  Founded in 1880, it is the oldest private research university in California.  USC has historically educated a large number of the region's business leaders and professionals.  In recent decades, the university has also leveraged its location in Los Angeles to establish relationships with research and cultural institutions throughout Asia and the Pacific Rim.  An engine for economic activity, USC contributes $8 billion annually to the economy of the Los Angeles metropolitan area and California.

Villanova, Pennsylvania: Villanova is a community in the United States Commonwealth of Pennsylvania.  It straddles Lower Merion Township of Montgomery County and Radnor Township of Delaware County.  It is located at the center of the Pennsylvania Main Line, a series of highly affluent Philadelphia suburban towns located along the original east-west railroad tracks of the Pennsylvania Railroad.  It is served by the SEPTA Paoli/Thorndale Line regional rail train and Norristown High Speed Line.

Villanova University: Villanova University is a private research university located in Radnor Township, a suburb northwest of Philadelphia, Pennsylvania, within the Archdiocese of Philadelphia in the United States.  Named after Saint Thomas of Villanova, the school is the oldest Catholic university in the Commonwealth of Pennsylvania.

Radnor Township, Quebec: The Radnor Township is located in the administrative region of Mauricie, in the province of Quebec, in Canada.  Today, the administration of this territory is under the city of Shawinigan and Mekinac Regional County Municipality (RCM).  Rectangular, the Canton is about 5 km wide and 38 km deep, oriented northwest to southeast.  The central part of the township is in La Mauricie National Park, on the west bank of the Saint-Maurice River which cut diagonally this township.  The southeastern part of the township includes the municipalities of Saint-Jean-des-Piles, Grandes-Piles, Saint-Roch-de-Mékinac, sector Lac-à-la-Tortue (grouped since 2001 in the city of Shawinigan) and Garneau railway junction (located northeast of Grand-Mère).

Question: Jason Steinhauer is a historian at what private research university located in Radnor Township?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person mentioned in the question."
    },
    "university_name": {
      "type": "string",
      "description": "The name of the university where the person is affiliated."
    },
    "university_type": {
      "type": "string",
      "description": "The type of the university (e.g., private research)."
    },
    "university_location": {
      "type": "string",
      "description": "The township where the university is located."
    },
    "person_role_at_university": {
      "type": "string",
      "description": "The role or position of the person at the university."
    }
  },
  "required": [
    "person_name",
    "university_name",
    "university_type",
    "university_location",
    "person_role_at_university"
  ],
  "additionalProperties": false
}
