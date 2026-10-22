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
Illinois's at-large congressional district: Illinois elected its United States Representative At-Large on a general ticket upon achieving statehood December 3, 1818.  It last elected a US Representative in the Election of 1946.  The district has been inactive since.

Charles Dominique Joseph Bouligny: Charles "Dominique" Joseph Bouligny (August 22, 1773March 4, 1833) was a lawyer and politician, elected as U.S. Senator from Louisiana, serving 1824 to 1829.  He had earlier served in the state House of Representatives.  Of French and Spanish descent, he was brother to Louis Bouligny, a state representative, and uncle of John Edward Bouligny, who was elected as US Representative from New Orleans.

Alfonso E. Lenhardt: Alfonso E. Lenhardt (born 1943) represented the United States as Ambassador to Tanzania from 2009-2013.  He was chosen as the US representative to the East African Community since 2010.  He left his post in October 2013.  From 2001 to 2003, he served as Sergeant at Arms of the United States Senate.

Silas L. Niblack: Silas Leslie Niblack (March 17, 1825 – February 13, 1883) was a Democratic US Representative from Florida.  He was the cousin of William Ellis Niblack, US Representative from Indiana.

Tom Cole: Thomas Jeffery Cole (born April 28, 1949) is the U.S. Representative for Oklahoma 's 4 congressional district , serving since 2003.  He is a member of the Republican Party.  He is a Deputy Majority Whip.  The chairman of the National Republican Congressional Committee (NRCC) from 2006 to 2008, he was, during his tenure, the fourth-ranking Republican leader in the House.  As of 2015, Cole – a member of the Chickasaw Nation – is one of only two registered Native Americans in Congress (the other being fellow Oklahoman Markwayne Mullin).

Lorado Taft: Lorado Zadoc Taft (April 29, 1860 – October 30, 1936) was an American sculptor, writer and educator.  Taft was born in Elmwood, Illinois, in 1860 and died in his home studio in Chicago in 1936.  Taft was the father of US Representative Emily Taft Douglas, father-in-law to her husband, US Senator Paul Douglas, and a distant relative of US President William Howard Taft.

Markwayne Mullin: Markwayne Mullin (born July 26, 1977) is an American politician and businessman who has been the United States representative for Oklahoma's 2nd congressional district since 2013.  He owns several businesses, which he took over at twenty, when his father became ill.  Mullin, a member of the Republican Party, was elected to the U.S. House of Representatives in the 2012 elections, succeeding Democratic representative Dan Boren.

Ruth Bryan Owen: Ruth Baird Bryan Leavitt Owen Rohde, best remembered as Ruth Bryan Owen, (October 2, 1885 – July 26, 1954) was a politician and the first woman appointed as a United States ambassador.  The daughter of attorney William Jennings Bryan and Mary E. Baird, she was a Democrat, who in 1929 was elected as Florida’s (and the South's) first woman US Representative, coming from Florida’s 4th district.  Representative Owen was also the first woman to earn a seat on the House Foreign Affairs Committee.

Dan Boren: Daniel David Boren (born August 2, 1973) is a retired American politician, who served as the U.S. Representative for Oklahoma 's 2 congressional district from 2005 to 2013.  The district includes most of the eastern part of the state outside of Tulsa.  He is a member of the Democratic Party.

Joshua Reed Giddings Law Office: The Joshua Reed Giddings Law Office is a National Historic Landmark in Jefferson, Ohio.  Joshua Reed Giddings was a prominent abolitionist who served as a US Representative from 1838 to 1859.  His Federal style two-room offices were located next to Giddings' house at 104 N. Chestnut St. The building was moved to 108 E. Jefferson Street in 2013 to make way for a McDonald's Restaurant.  The law office and Jefferson Village Police Department currently reside on the land formerly occupied by Jefferson Elementary School which was demolished in 2009.  The land is now known as Giddings Park.

Question: Markwayne Mullin succeeded which US Representative for Oklahoma in 2013?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "successor_representative": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the representative who succeeded another."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "succeeded_representative": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the representative who was succeeded."
        },
        "party": {
          "type": "string",
          "description": "The political party of the succeeded representative."
        }
      },
      "required": [
        "name",
        "party"
      ],
      "additionalProperties": false
    },
    "congressional_district": {
      "type": "string",
      "description": "The congressional district involved in the succession."
    },
    "year_of_succession": {
      "type": "integer",
      "description": "The year the succession took place."
    }
  },
  "required": [
    "successor_representative",
    "succeeded_representative",
    "congressional_district",
    "year_of_succession"
  ],
  "additionalProperties": false
}
