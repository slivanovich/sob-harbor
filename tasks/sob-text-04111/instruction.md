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
Alabama gubernatorial election, 1998: The Alabama gubernatorial election of 1998 was held on 3 November 1998 to select the governor of the state of Alabama.  The election saw incumbent Fob James (R) taking on Lieutenant Governor Don Siegelman (D).  The result saw Don Siegelman win a decisive victory over Fob James.  As of 2017, this is the most recent election in which a Democrat was elected Governor of Alabama.

Lieutenant Governor of Illinois: The Lieutenant Governor of Illinois is the second highest executive of the State of Illinois.  In Illinois, the lieutenant governor and governor run on a joint ticket, and are directly elected by popular vote.  Candidates for lieutenant governor ran separately in the primary from candidates for governor until 2014, when the system was changed to allow the gubernatorial nominee of a party to select the nominee for lieutenant governor.  When the Governor of Illinois becomes unable to discharge the duties of that office, the lieutenant governor becomes acting governor.  If the Governor dies, resigns or is removed from office, the lieutenant governor becomes governor.  Under the Illinois Constitution, the Attorney General is next in line of succession to the Governor's office after the lieutenant governor, but does not succeed to the Lieutenant Governor's office.  From the impeachment of Rod Blagojevich in 2009 until the inauguration of Sheila Simon in 2011, Attorney General Lisa Madigan would have become Governor if Pat Quinn had vacated the office.  Historically, the lieutenant governor has been from either the Democratic Party or Republican Party.  As of January 12, 2015, the lieutenant governor is Evelyn Sanguinetti.

Troy King: Troy Robin King (born August 22, 1968) is the former attorney general of the state of Alabama, United States.  He previously served as an assistant attorney general and a legal adviser to both Republican governors Bob Riley and Fob James.  King was appointed by Governor Bob Riley in 2004, when William Pryor resigned to accept a federal judgeship.  He then defeated Mobile County District Attorney John Tyson, Jr., in the 2006 election by a 54-46% margin.  He sought a second term but was defeated in the Republican primary, securing 40 percent of the vote to the roughly 60 percent by Luther Strange.

Don Siegelman: Donald Eugene "Don" Siegelman (born February 24, 1946) is a former American politician and lawyer who has held numerous offices in the state of Alabama.  He served one term as the 51st Governor of Alabama from 1999 to 2003.  Siegelman was the last member of the Democratic Party, as well as the only Roman Catholic, to hold the office of governor.  He is the only person in the history of Alabama to be elected to serve in all four of the top statewide elected offices: Secretary of State, Attorney General, Lieutenant Governor and Governor.  He served in Alabama politics for 26 years.

Alabama gubernatorial election, 1978: The 1978 Alabama gubernatorial election took place on November 7, 1978, to elect the Governor of Alabama.  Incumbent Democratic Governor George Wallace did not run for re-election.  Fob James, a businessman who had switched from the Republican Party to the Democratic Party and campaigned as a "born-again Democrat", won the Democratic primary in an upset over Attorney General Bill Baxley.  He went on to defeat Guy Hunt in a landslide in the general election.

Daniel Greene (artist): Daniel E. Greene PSA, NA, AWS (born 1934) is an American artist who works in the media of pastels and oil painting.  The Encyclopædia Britannica considers Mr. Greene the foremost pastelist in the United States.  His paintings and pastels are in over 700 public and private collections in the United States and abroad.  Highly regarded as a portrait artist, his subjects have included leaders of Government, Banking, Education and Industry.  Some of his sitters include First Lady Eleanor Roosevelt, Ayn Rand, Astronaut Walter Schirra, William Randolph Hearst, “Wendy’s” founder Dave Thomas, Commentator Rush Limbaugh, Composer Alan Menken, Bryant Gumbel and Bob Schieffer of CBS TV.  Governmental Portraits include Secretary of Agriculture Ann Veneman, Governor Paul Laxalt of Nevada, Governor Gerald Baliles of Virginia, Governor Benjamin Cayetano of Hawaii, and Governor Fob James of Alabama.  Business sitters include the chairmen of the boards of Honeywell, Coca-Cola Company, Dupont Corporation, Endo Pharmaceuticals, American Express, The New York Stock Exchange and IBM.  Mr. Greene has also painted the Deans, Presidents and Benefactors of Tufts, Duke, Columbia, North Carolina, West Point, Delaware, Penn State, New York, Princeton, Rutgers, Yale and Harvard Universities.

Joseph S. Johnston: Joseph S. Johnston is a circuit judge of the 13th Judicial Circuit in State of Alabama.  Appointed by Governor Fob James in April, 1997, Johnston became the first Republican to hold a circuit or district judgeship in Mobile County.  He was elected without opposition in 1998, 2000 and 2006.

Alabama gubernatorial election, 1982: The Alabama gubernatorial election of 1982 included the last campaign and final electoral victory of George Wallace.  The election occurred on November 2, 1982.  Incumbent Governor Fob James declined to run for a second term, allowing for an open election in 1982.  In the Democratic primary, Wallace received challenges from Lieutenant Governor George McMillan, Speaker of the State House Joe McCorquodale, Jr., former Governor Jim Folsom, and Reuben McKinley.  Because Wallace did not receive a majority of the votes, he advanced to a run-off with McMillan and then narrowly won the Democratic nomination.  Montgomery Mayor Emory Folmar went unchallenged for the Republican nomination.

Alabama gubernatorial election, 1994: The 1994 Alabama gubernatorial election was held on 8 November 1994 to select the governor of the state of Alabama.  The election saw Republican Fob James defeat Democratic incumbent Governor Jim Folsom, Jr. in an upset.

Tim James (politician): Tim James (born March 3, 1962) is an American businessman from Alabama.  The son of former Alabama Governor Fob James, he sought and lost the Republican Party nomination for Governor of Alabama twice, finishing third in the Republican primaries in both 2002 and 2010.

Question: What Alabama governor ran against Fob James in 1998?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "election_year": {
      "type": "integer",
      "description": "The year the gubernatorial election took place."
    },
    "incumbent_governor": {
      "type": "string",
      "description": "The name of the incumbent governor in the election."
    },
    "challenger_candidate": {
      "type": "string",
      "description": "The name of the candidate who ran against the incumbent governor."
    },
    "challenger_party": {
      "type": "string",
      "description": "The political party of the challenger candidate."
    },
    "challenger_became_governor": {
      "type": "boolean",
      "description": "Indicates whether the challenger candidate later served as governor."
    },
    "election_winner": {
      "type": "string",
      "description": "The name of the candidate who won the election."
    }
  },
  "required": [
    "election_year",
    "incumbent_governor",
    "challenger_candidate",
    "challenger_party",
    "challenger_became_governor",
    "election_winner"
  ],
  "additionalProperties": false
}
