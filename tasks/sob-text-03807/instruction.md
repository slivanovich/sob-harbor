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
Dick Armey: Richard Keith Armey ( ; born July 7, 1940) is an American politician.  He was a U.S. Representative from Texas'  (1985–2003) and House Majority Leader (1995–2003).  He was one of the engineers of the "Republican Revolution" of the 1990s, in which Republicans were elected to majorities of both houses of Congress for the first time in four decades.  Armey was one of the chief authors of the Contract with America.  Armey is also an author and former economics professor.  After his retirement from Congress, he has worked as a consultant, advisor, and lobbyist.

Peter B. Davidson: Peter B. Davidson is an American lawyer and government official who currently serves as the General Counsel of the United States Department of Commerce.  He was previously the senior vice president for congressional relations at Verizon Communications, general counsel to the United States Trade Representative, vice president for congressional relations at US West and Qwest, general counsel and policy director to the Majority Leader of the House of Representatives, attorney-advisor in the Office of Legal Counsel of the United States Department of Justice, director of congressional and media relations at the United States Information Agency, staffer to Representatives Dick Armey and Bill Frenzel, and law clerk on the United States Court of Appeals for the Tenth Circuit.

Jock Scott: John Wyeth Scott II (June 29, 1947 – April 25, 2009), known as Jock Scott, was a lawyer and college professor in Alexandria, Louisiana, who served three terms from District 26 in the Louisiana House of Representatives, first as a Democrat (1976–1985) and then as a Republican (1985–1988).  He was defeated in a race for the Louisiana State Senate in 1987.  He also lost two bids for the United States House of Representatives: a 1985 special election, when he ran as a Democrat, and in the 2004 nonpartisan blanket primary for the Fifth Congressional District, when he challenged fellow Republican U.S. Representative Rodney Alexander of Jackson Parish.

Michael C. Burgess: Michael Clifton Burgess (born December 23, 1950) is a Republican member of the United States House of Representatives representing  's 26 congressional district .  In 2002, he defeated Scott Armey, the son of House Majority Leader and then-U.S. Representative Dick Armey, in a primary runoff election.  Prior to his election, he practiced as a doctor of obstetrics and gynecology.

Contract with America: The Contract with America was a document released by the United States Republican Party during the 1994 Congressional election campaign.  Written by Newt Gingrich and Dick Armey, and in part using text from former President Ronald Reagan's 1985 State of the Union Address, the Contract detailed the actions the Republicans promised to take if they became the majority party in the United States House of Representatives for the first time in 40 years.  Many of the Contract's policy ideas originated at The Heritage Foundation, a conservative think tank.

Texas's 26th congressional district: Texas District 26 of the United States House of Representatives is a Congressional district in the state of Texas that serves an area in the northern portion of the Dallas-Fort Worth Metroplex centering on Denton County.  The current Representative is Michael C. Burgess.  The District is best known as the seat of former House Majority Leader Dick Armey.

Texas's 13th congressional district: Texas District 13 of the United States House of Representatives is a Congressional District of the U.S. state of Texas that includes most of the Texas Panhandle, parts of Texoma and northeastern parts of North Texas.  It winds across the Panhandle into the South Plains, then runs east across the Red River Valley.  Covering over 40000 sqmi , it is the second-largest district geographically in Texas and larger in area than thirteen entire states.  The principal cities in the district are Amarillo and Wichita Falls.  The current Representative is Republican Mac Thornberry.

Texas's 20th congressional district: Texas District 20 of the United States House of Representatives is a Congressional district that serves the western half of San Antonio and Bexar County in Texas.  The district is heavily Latino/Hispanic (predominantly of Mexican descent), as is the surrounding area.  Charlie Gonzalez, who represented the district from 1999 to 2013 after succeeding his father, Henry B. Gonzalez, did not seek re-election in the 2012 United States House of Representatives elections.  State representative Joaquín Castro, the Democratic nominee to replace Gonzalez, defeated David Rosa, the Republican nominee, in the race for Texas's 20th district on November 6, 2012.  His term began on January 3, 2013.

Ron Slotin: Ronald D. "Ron" Slotin (born 1963/64) is an American politician from the state of Georgia.  He served in the Georgia State Senate, opting not to run for reelection in 1996 so that he could run for the United States House of Representatives seat for Georgia 's 4 congressional district .  He ran in the 2017 special election to represent Georgia 's 6 congressional district in the United States House of Representatives, but was unsuccessful.

Texas's 8th congressional district: Texas District 8 of the United States House of Representatives is a Congressional district that includes Montgomery County and Walker County.  It includes much of the northern outlying areas of metro Houston.  The current Representative from District 8 is Kevin Brady and has been since 1997.  For the 2014 election cycle Craig McMichael, a veteran of the Marine Corps, and network engineer had challenged and lost to incumbent Kevin Brady in the Republican Primary.  In the 2014 General Election, Brady faced off against the Libertarian Party candidate, Ken Petty of Spring, Texas, who won his nomination in the Libertarian District Convention.  No Democrat ran.  In the 2016 election, the 20-year incumbent was challenged by 3 challengers: Andre Dean, Craig McMichael, and Steve Toth.  As of August 2017, Brady is expected to face Democrat Steven David in the 2018 election as well as Independent candidate Todd Carlton.  David is the first Democrat to challenge Brady since the 2012 election.

Question: Texas District 26 of the United States House of Representatives is a Congressional district in the state of Texas, the District is best known as the seat of  Dick Armey, an American politician, and former what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the politician."
    },
    "person_former_role": {
      "type": "string",
      "description": "The former political role held by the person."
    },
    "person_political_party": {
      "type": "string",
      "description": "The political party the person was associated with during their time in the specified role."
    },
    "associated_congressional_district_number": {
      "type": "integer",
      "description": "The number of the congressional district the person is associated with."
    },
    "associated_congressional_district_state": {
      "type": "string",
      "description": "The state of the congressional district."
    }
  },
  "required": [
    "person_name",
    "person_former_role",
    "person_political_party",
    "associated_congressional_district_number",
    "associated_congressional_district_state"
  ],
  "additionalProperties": false
}
