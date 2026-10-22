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
Karen Handel: Karen Christine Handel (née Walker; born April 18, 1962) is an American businesswoman, politician, and member of the United States House of Representatives for Georgia's 6th congressional district.  In 2017, she became the first Republican woman to be elected to the U.S. Congress from Georgia after defeating Democratic candidate Jon Ossoff on June 20 in the 2017 special election to fill the vacancy in Georgia's 6th congressional district in the most expensive congressional race in American history.

Shelli Yoder: Shelli Renee Yoder (born August 30, 1968) is an American Democratic Party politician.  A former Miss Indiana titleholder and Miss America 1993 contestant, Yoder has held positions at a number of non-profit organizations.  She was the Democratic Party nominee for the United States House of Representatives in Indiana's 9th congressional district in the 2012 race and is currently a member of the County Council for Monroe County, Indiana.  In August 2015, Yoder announced she would run for Indiana's 9th congressional district in 2016.  The 9th was an open seat due to incumbent Todd Young running for the United States Senate.  Yoder was defeated by Republican nominee Trey Hollingsworth in the November 8, 2016, general election.

George H. Christopher: George Henry Christopher (December 9, 1888 – January 23, 1959) was a Democratic Party representative from Missouri's 6th congressional district from January 3, 1949 to January 3, 1951 and from the Missouri's 4th congressional district from January 3, 1955 until his death January 23, 1959.

John Delaney presidential campaign, 2020: The 2020 presidential campaign of John Delaney, the U.S. Representative representing Maryland's 6th congressional district, was announced on July 28, 2017.  He became the first prominent Democrat to announce a campaign for the 2020 presidential election.

John Delaney (Maryland politician): John Kevin Delaney (born April 16, 1963) is an American politician and businessman who has been the United States Representative for Maryland's 6th congressional district since 2013 and is running for President of the United States in 2020.  The district, the state's second-largest, includes nearly the entire western portion of the state, but the bulk of its vote is cast in the outer suburbs of Washington, D.C. He is a member of the Democratic Party.

Dick Muri: Richard Walter "Dick" Muri (born November 30, 1953) is an American politician of the Republican Party.  He is a member of the Washington House of Representatives, representing the 28th legislative district.  Muri was appointed to the Washington State House of Representatives following (now former) State Representative Steve O'Ban's appointment to the Washington State Senate after State Senator Mike Carrell's death.  From 2003 to 2012, he served as a Republican member of the Pierce County Council, representing the 6th District.  In 2010, he ran as a Republican candidate for U.S. Congress in Washington's 9th congressional district against incumbent Democratic Congressman Adam Smith, eventually losing to Smith by nearly 10 points.  In 2012, he again ran, this time in Washington's 10th congressional district against Denny Heck, losing by 17 points.

Maryland's 6th congressional district: Maryland's 6th congressional district elects a representative to the United States House of Representatives from the northwest part of the state.  Today the district comprises all of Garrett, Allegany, and Washington counties as well as portions of Montgomery and Frederick counties.  The seat is currently represented by John Delaney (D).

Frederick R. Lehlbach: Frederick Reimold Lehlbach (January 31, 1876 – August 4, 1937) was an American lawyer and politician.  As a Republican, Lehlbach served as the U.S. Representative for New Jersey's 10th congressional district from 1915 to 1933 and as the representative from New Jersey's 12th congressional district from 1933 to 1937.  Lehlbach was also the nephew of Herman Lehlbach, a former U.S. Representative from New Jersey's 6th congressional district who served from 1885 to 1891.

Georgia's 6th congressional district: Georgia's 6th congressional district is a congressional district in the U.S. state of Georgia.  It is currently represented by Republican Karen Handel.  The district's boundaries have been redrawn following the 2010 census, which granted an additional congressional seat to Georgia.  The first election using the new district boundaries (listed below) was the 2012 congressional elections.

Rick Nolan: Richard Michael Nolan (born December 17, 1943) is an American politician and member of the Minnesota Democratic–Farmer–Labor Party who has been the U.S. Representative for Minnesota's 8th congressional district since 2013 and previously served as the U.S. Representative for Minnesota's 6th congressional district from 1975 to 1981.

Question: Which member of Maryland's 6th congressional district is running for President of the United States in 2020?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "candidate_name": {
      "type": "string",
      "description": "The full name of the political candidate."
    },
    "congressional_district": {
      "type": "integer",
      "description": "The number of the congressional district represented."
    },
    "state": {
      "type": "string",
      "description": "The state the congressional district is in."
    },
    "political_party": {
      "type": "string",
      "description": "The political party the candidate belongs to."
    },
    "is_running_for_president_2020": {
      "type": "boolean",
      "description": "Indicates if the candidate is running for President in 2020."
    }
  },
  "required": [
    "candidate_name",
    "congressional_district",
    "state",
    "political_party",
    "is_running_for_president_2020"
  ],
  "additionalProperties": false
}
