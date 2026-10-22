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
Marie Redd: Marie Redd is a United States politician from the state of West Virginia.  Redd was a Democratic West Virginia State Senator from the 5th District, which conatins Cabell County and a small portion of Wayne County.  In 1998, she defeated incumbent Republican State Senator Thomas F. Scott in the general election, thereby becoming the first African-American state senator in West Virginia history.  Redd lost to Evan Jenkins in the 2002 Democratic primary election and again in 2006.

Mary Lou Rath: Mary Lou Rath is a former state senator in New York.  A Republican, she represents the state's 61st Senate District, which consists of parts of Erie County and all of Genesee County.  In January 2007, she was appointed to the post of Deputy Majority Leader for State/Federal Relations, making her the only woman in the Senate Republican leadership.  She announced her retirement in 2008 and was succeeded by Erie County Legislator Michael Ranzenhofer.  Senator Ranzenhofer had also succeeded Senator Rath as Minority Leader of the Erie County Legislature when Senator Rath stepped down to become a state senator.

Corey Palumbo: Corey Lee Palumbo (born August 16, 1972) is a West Virginia State Senator representing the 17th district in the West Virginia Senate.  A state senator since 2009, he previously served as a member of the West Virginia House of Delegates from 2003 to 2009.  He is the son of Mario Palumbo, the 32nd Attorney General of West Virginia as well as a former five-term state senator.

Dwite Pedersen: Dwite Pedersen (born 1941) is a Nebraska state senator from Elkhorn, Nebraska in the Nebraska Legislature and substance abuse counselor.

Carey Baker: Carey Baker is a gun shop owner, active First Sergeant in the Florida Army National Guard, and former Republican State Senator from Florida.  He served as a State Senator from the 20th Senate District starting in 2004.  Before serving as Florida State Senator, Baker served in the Florida House of Representatives from 2000 to 2004.  In November 2008, Senator Baker announced his candidacy to be Florida’s next Commissioner of Agriculture and Consumer Services but later dropped out of the race.  In 2012, he was elected to the position of Property Appraiser for Lake County, Florida.

Brandon Bell (Virginia politician): J. Brandon Bell II (born December 20, 1958) is an American former Virginia state senator and small businessman from Charlottesville.  Bell was state senator for two non-consecutive terms, replacing Republican State Senator Malfourd W. Trumbo in an open race over Democratic Party Candidate Stephen H. Emick (a relative of Malfourd's predecessor Dudley J. Emick Jr.) when Trumbo retired after 3 terms, having first been elected in 1991.

Nebraska: Nebraska is a state that lies in both the Great Plains and the Midwestern United States.  The state is bordered by South Dakota to the north, Iowa to the east and Missouri to the southeast, both across the Missouri River, Kansas to the south, Colorado to the southwest and Wyoming to the west.  It is the only triply landlocked U.S. state.  Nebraska's area is just over 77,220 sq mi (200,000 km) with almost 1.9 million people.  Its state capital is Lincoln, and its largest city is Omaha, which is on the Missouri River.

Robert Irwin (North Carolina State Senator): Gen. Robert Irwin of Steele Creek Township, Mecklenburg County, North Carolina (1738-1800) was a long term North Carolina State Senator.  The first State Senator ever elected from Mecklenburg County, he served as the North Carolina State Senator from Mecklenburg County in the years 1778-1783, again, in the years 1787 and 1795, and, finally, from 1797-1800, dying in office.  Prior to entering the Senate, Irwin commanded Patriot (American Revolution) militia forces of the North Carolina State Militia, rising to the rank of a general of command in the 1st Mecklenburg County Regiment (Est. 1775, Split into 1st & 2nd regiments 1780, and Disest.  1783).  He commanded the battalion while fighting strategically against Loyalist (American Revolution) militia forces beside South Carolina patriot militia General Thomas Sumter at the Battle of Rocky Mount and later beside him victoriously against loyalist provisional units and militia while heavily outnumbered at the Battle of Hanging Rock.  Irwin is reported to have been a signer of the Mecklenburg Declaration of Independence.  Gen. Irwin was of the Presbyterian faith.

Don Pederson: Don Pederson (born 1928) is a Nebraska state senator from North Platte, Nebraska in the Nebraska Legislature and an attorney.

Irene Griffin: Irene T. Griffin (July 25, 1899 – April 1983) was an American Republican Party politician who served in the New Jersey General Assembly.  She served one year in the Legislature, but became a bit of a perennial candidate, losing three races for the Assembly, two for the Senate, and one for Congress.  Griffin first ran for the State Assembly in 1942, but lost the Republican primary to future U.S. Senator Clifford P. Case, future State Senator Kenneth Hand, and two others.  When Case ran for Congress in 1944, Griffin ran again and won the nomination and the election.  She did run for a second term in 1945, but sought the Republican nomination for State Senator in 1947, losing to hand in the primary.  She ran again for Assembly in 1951, but lost the primary to incumbent Florence P. Dwyer.  She again challenged Dwyer in 1956, this time in a primary for the U.S. House of Representatives; she lost and Dwyer went on to unseat an incumbent in the general election.  She ran for the Assembly in 1957, upsetting the frontrunner, Nelson Stamler in the Republican primary.  She lost the General Election to Democrat Mildred Barry Hughes.  Griffin lost a State Senate primary in 1962 to Stamler, who had since been elected Assemblyman.  In 1967, she lost a Republican primary for State Assembly to Hugo Pfaltz and Peter J. McDonough by a 2-1 margin.

Question: What is the area of the State where Dwite Pederson is a state senator ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "state_name": {
      "type": "string",
      "description": "The name of the state where the senator serves."
    },
    "state_area": {
      "type": "object",
      "properties": {
        "value": {
          "type": "number",
          "description": "The numerical value of the state's area."
        },
        "unit": {
          "type": "string",
          "description": "The unit of measurement for the state's area."
        },
        "description": {
          "type": "string",
          "description": "A descriptive phrase about the state's area, if available."
        }
      },
      "required": [
        "value",
        "unit"
      ],
      "additionalProperties": false
    },
    "senator_name": {
      "type": "string",
      "description": "The name of the state senator in question."
    }
  },
  "required": [
    "state_name",
    "state_area",
    "senator_name"
  ],
  "additionalProperties": false
}
