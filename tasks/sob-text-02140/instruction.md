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
Allegheny-Clarion Valley School District: Allegheny-Clarion Valley School District (ACVSD) is a small, rural, public school district in western Pennsylvania.  It spans portions of four counties and is the only Pennsylvania public school district to do so.  The District is one of the 500 public school districts of Pennsylvania.  The Allegheny-Clarion Valley School District encompasses approximately 121 sqmi .  In Armstrong County it covers the City of Parker and Hovey Township.  In Butler County it serves Allegheny Township.  In Clarion County it serves the Boroughs of Emlenton, Foxburg and St. Petersburg and Perry Township and Richland Township.  In Venango County it serves the Borough of Emlenton and Richland Township and Scrubgrass Township.  According to 2000 federal census data, Allegheny-Clarion Valley School District serves a resident population of 5,944.  By 2010, the District's population declined to 5,749 people.  In 2009, the District residents' per capita income was $15,525, while the median family income was $36,867.  In the Commonwealth of Pennsylvania, the median family income was $49,501 and the United States median family income was $49,445, in 2010.  By 2013, the median household income in the United States rose to $52,100.

Exelon: Exelon Corporation is an American Fortune 100 energy company headquartered in Chicago, Illinois.  It generates revenues of approximately $34.5 billion and employs approximately 34,000 people.  Exelon is the largest electric holding company in the United States by revenue, the largest regulated utility in the United States with approximately 10 million customers, and is also the largest operator of nuclear power plants in the United States.  It was created in October 2000 by the merger of PECO Energy Company and Unicom, of Philadelphia and Chicago respectively.  Unicom owned Commonwealth Edison.  Exelon operates regulated utilities in Illinois, Pennsylvania, Maryland, Delaware, New Jersey, and Washington, DC.  In October 2009, Exelon had full or majority ownership of 17 nuclear reactors in 10 nuclear power plants. Exelon has operations and business activities in 47 states, the District of Columbia and Canada and is the largest competitive U.S. power generator with approximately 35,000 megawatts of owned capacity.  Exelon merged with Constellation Energy Group in March 2012 and acquired Pepco Holdings in March 2016.  Exelon consists of eight main operating subsidiaries with Exelon Generation, a deregulated energy generator, Constellation, a deregulated competitive energy supplier, and six regulated utilities, Commonwealth Edison (Illinois), Philadelphia Electric Company (Pennsylvania), Baltimore Gas and Electric (Maryland), Delmarva Power & Light (Delaware and Maryland), Atlantic City Electric (New Jersey), and Potomac Electric Power Company (Washington, DC and Maryland).

Pittsburgh: Pittsburgh ( ) is a city in the Commonwealth of Pennsylvania in the United States, and is the county seat of Allegheny County.  As of 2017, a total population of 305,704 lives within the city limits, making it the 63rd-largest city in the U.S. The metropolitan population of 2,353,045 is the largest in both the Ohio Valley and Appalachia, the second-largest in Pennsylvania (behind Philadelphia), and the 26th-largest in the U.S.

Pennsylvania (song): "Pennsylvania" is the official state song of the Commonwealth of Pennsylvania.  The song was written and composed by Eddie Khoury and Ronnie Bonner and serves as the official song for all public purposes.  State Representative Frank L. Oliver introduced the bill for the song, and it was adopted by the General Assembly and signed into law by Governor Robert P. Casey on November 29, 1990.

Flag of Harrisburg, Pennsylvania: The flag of Harrisburg, Pennsylvania, consists of a blue field, with the city emblem centered in the middle of the flag.  The emblem should not be confused with the city seal.  The emblem consists of a white keystone with a red border, and incorporates the capitol dome which denotes the city's significance as the state capital of the Commonwealth of Pennsylvania.  The current flag came into use in the early 1990s.  Harrisburg received the All-America City Award given by the National Civic League in 1984-85 and 1990.  An older version of the city’s flag incorporated the city emblem with a dark blue field and yellow border.

Beans in My Ears: "Beans in My Ears" is a song created and sung by protest singer and contributing editor to folk-centric "Broadside Magazine", Len Chandler.  It became a hit single when covered by The Serendipity Singers, reaching number 30 in June 1964.  Doctors protested that many children were actually putting beans in their ears so it was banned in some places such as Pittsburgh and Boston.  Numerous public health boards reportedly blacklisted the song, as well, according to Chandler.  "Some television shows asked us to do something different," said Bryan Sennett of the Serendipity Singers.  "Understandably so--it was dangerous.  Obviously, (the song) was a statement about adults not listening to children."  Pittsburgh radio station KDKA's program manager Jack Williams imposed the ban due to the number of listener complaints and doctor reports about children putting objects in their ears in the three weeks following the song's release on the station.

Harrisburg, Pennsylvania: Harrisburg (Pennsylvania German: "Harrisbarrig") is the capital city of the Commonwealth of Pennsylvania in the United States, and the county seat of Dauphin County.  With a population of 48,904, it is the ninth-largest city in the Commonwealth.  It lies on the east bank of the Susquehanna River, 107 mi west of Philadelphia.

Allentown School District: The Allentown School District is a large, urban public school district located in Lehigh County, Pennsylvania, in the United States.  The District is one of the 500 public school districts of Pennsylvania.  Serving most of the city of Allentown, it is the fourth largest school district in Pennsylvania, with 17,962 students, with 15.7% White, 17.4% Black, 64.4% Hispanic, 1.4% Asian, 0.17% Native American.  The School District of the City of Allentown encompasses approximately 17 sqmi .  According to 2010 federal census data, the Allentown School District serves a resident population of 118,032.  Per the US Census Bureau data, it served a resident population of 106,630 in 2000.  In 2009, the per capita income was $16,282, while the median family income was $37,356.  In the Commonwealth, the median family income was $49,501 and the United States median family income was $49,445, in 2010.  By 2013, the median household income in the United States rose to $52,100.

Commonwealth Charter Academy: Commonwealth Charter Academy (previously named Commonwealth Connections Academy) is a large, public, cyber charter school.  The school serves all school-aged children in the Commonwealth of Pennsylvania regardless of where the child lives.  The Academy's headquarters is located in Harrisburg, Pennsylvania.  It is one of sixteen public cyber charters schools operating in the Commonwealth of Pennsylvania.  The School operates seven additional branches, called Family Service Centers, across the Commonwealth: Andreas, Bryn Mawr, Harrisburg, Center City Philadelphia, Pittsburgh, Scranton and Williamsport.  When the School was originally approved it served Kindergarten through 8th grade pupils all across Pennsylvania.

District Attorney of Philadelphia: The Office of the District Attorney of Philadelphia is the largest prosecutor's office in Pennsylvania, and one of the largest in the nation.  It serves the more than 1.5 million citizens of the City and County of Philadelphia, Pennsylvania.  The current District Attorney of Philadelphia is Kelly Hodges The district attorney represents the Commonwealth of Pennsylvania and the City & County of Philadelphia in all criminal and other prosecutions.

Question: Which city in the commonwealth of Pennsylvania was the song Beans in My Ears banned ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "banned_song_title": {
      "type": "string",
      "description": "The title of the song that was banned."
    },
    "banned_city_name": {
      "type": "string",
      "description": "The name of the city where the song was banned."
    },
    "city_state": {
      "type": "string",
      "description": "The state in which the city is located."
    },
    "reason_for_ban": {
      "type": "string",
      "description": "The reason why the song was banned."
    },
    "banning_entity": {
      "type": "string",
      "description": "The entity or organization that imposed the ban."
    }
  },
  "required": [
    "banned_song_title",
    "banned_city_name",
    "city_state",
    "reason_for_ban",
    "banning_entity"
  ],
  "additionalProperties": false
}
