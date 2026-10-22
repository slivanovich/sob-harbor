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
Chappaqua, New York: Chappaqua is a hamlet and census-designated place in the town of New Castle, in northern Westchester County, New York.  It is on 0.45 sqmi of land on the east bank of the Hudson River, about 30 mi north of New York City.  The hamlet is served by the Chappaqua station of the Metro-North Railroad's Harlem Line.  In the New York State Legislature it is within the New York State Assembly's 93rd district and the New York Senate's 40th district.  In Congress the village is in New York's 17th District.

4th &amp; B'way Records: 4th & B'way Records (pronounced and spelled out completely as Fourth and Broadway Records in the UK) was a US-based subsidiary of Island Records that specialized in street-oriented music such as hip hop.  Established in 1984, it was the flagship label of the Island Trading Company, the independent-distribution parent company of Island's other record labels that operated in the US.  However, 4th & B'way was not distributed through major-label channels—the flagship Island label was distributed by Atlantic Records at that time—until the label and distribution company were acquired by PolyGram Records in 1989, when Island Trading became a unit of PolyGram Group Distribution and was renamed Independent Label Sales (ILS).  It was also one of several US-based Island labels that were named after nearby New York City streets when Island's US headquarters were located at 14 East 4th Street in Manhattan, the same building that held the legendary Greenwich Village branch of Tower Records, and also nearby at 400 Lafayette Street.  When Island moved its headquarters to the Worldwide Plaza Building at 825 8th Avenue in 1995, where PolyGram's US headquarters were also located, the empty 4th Street offices became the headquarters of V2 Records.

Charles C. Lockwood: Charles Clapp Lockwood (September 2, 1877 – September 21, 1958) was an American lawyer and a Republican Party politician from New York.  He was a member of the New York State Senate, 1915-22 (4th District 1915-18, 7th District 1919-22) and a Justice of the New York Supreme Court 2nd District, 1932-47.  He is probably best known for presiding the Joint Legislative Committee on Housing, also known as the Lockwood Committee (1919-1922), investigating rents and housing in New York City after World War I.

Újpest: Újpest (] ; German: "Neu-Pest" , English: New Pest ) is the 4th District in Budapest, Hungary.  It is located on the left bank of the Danube River.  The name Újpest means "new Pest" because the city was formed on the border of the city of Pest, Hungary in 1838.  Újpest was a village for 6 decades until 1907 when it became a town.  In 1950, the town was unified with Budapest to form Greater Budapest.  Since 1950, Újpest is the 4th District of Budapest.

Lindenhurst, New York: Lindenhurst is a village in Suffolk County, New York, United States, on the southern shore of Long Island in the town of Babylon.  The population was 27,253 at the 2010 census.

Phil Boyle: Phillip A. "Phil" Boyle (born July 21, 1961) is the Senator for the 4th District of the New York Senate.  He is a Republican.  The district includes the villages of Babylon, Brightwaters, Lindenhurst, Ocean Beach, Saltaire in Suffolk County on Long Island.

New Taipei City Constituency 4: New Taipei 4th district () formerly known as Taipei County 4th district (2008–2010) is a single-member constituency for the Legislative Yuan since 2008.

4th Street (Manhattan): 4th Street is a street in Lower Manhattan, New York City.  It starts at Avenue D as East 4th Street and continues to Broadway, where it becomes West 4th Street.  It continues west until the Avenue of the Americas (Sixth Avenue), where West 4th Street turns north and confusingly intersects with West 10th, 11th, 12th, and 13th Streets in Greenwich Village.  Most of the street has the same 40 ft width between curbstones as others in the prevailing street grid, striped as two curbside lanes and one traffic lane, with one-way traffic eastbound.  The portion from Seventh to Eighth Avenues is westbound (northbound geographically) and is approximately 35 ft wide, a legacy of the original Greenwich Village street grid.  The section of four short blocks from MacDougal Street to University Place which forms the southern border of Washington Square Park is called Washington Square South.

Richard A. Slisz: Richard A. Slisz is a former Democrat US politician from Cheektowaga, New York.  He served in the Erie County Legislature from 1974 to 1987.  Slisz represented the 4th District from 1974 to 1981, and then the 8th District from 1982 to 1987.

Pennsylvania's 10th congressional district: Pennsylvania's 10th Congressional District is located in the central and northeast regions of the state.  The district was one of the 12 original districts created prior to the 4th Congress.  It is currently represented by Republican Tom Marino, who defeated Democratic incumbent Chris Carney during the 2010 U.S. House elections.  In 2006, the 10th district experienced one of the greatest party shifts among all House seats that switched party control: in 2004, Republican Don Sherwood won with an 86% margin of victory over his nearest opponent and two years later, Carney unseated Sherwood by a 53%–47% margin.  In 2008, Carney won reelection by 12 points but the district swung back in 2010, electing Tom Marino.  The district is mostly Republican in its political composition, an aspect of the district that is reflected especially well in presidential elections.  In 2004, President George W. Bush won 60 percent of the vote in the district and in 2008, Senator John McCain beat Senator Barack Obama here by a margin of 54 percent to 45 percent.  Nonetheless, Carney easily won reelection as a Democrat the same year McCain won the district.  However, in the 2010 midterm elections, Marino unseated Carney by a 55%–45% margin.  In 2016, local business man and former mayor of Lewisburg, Pennsylvania, Mike Molesevich challenged Marino for the seat, but he fell to the Republican in November by more than two to one.  Marino remains the congressman in the 10th district, but he has expressed interest in a 2018 gubernatorial run rather than standing for reelection.

Question: What village of population 27,253 is located in the 4th District of New York?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "village_name": {
      "type": "string",
      "description": "The name of the village."
    },
    "population": {
      "type": "integer",
      "description": "The population of the village."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "county": {
          "type": "string",
          "description": "The county where the village is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the village is located."
        },
        "senate_district": {
          "type": "integer",
          "description": "The New York State Senate district the village is part of."
        }
      },
      "required": [
        "county",
        "state",
        "senate_district"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "village_name",
    "population",
    "location_details"
  ],
  "additionalProperties": false
}
