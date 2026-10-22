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
Montana gubernatorial election, 1944: The 1944 Montana gubernatorial election took place on November 7, 1944.  Incumbent Governor of Montana Sam C. Ford, who was first elected Governor in 1940, ran for re-election.  He won the Republican primary and moved on to the general election, where he was opposed by Leif Erickson, a former Chief Justice of the Montana Supreme Court and the Democratic nominee.  Although then-President Franklin D. Roosevelt comfortably won the state in that year's presidential election, Ford defeated Erickson by a wide margin to win his second and final term as governor.

Burton K. Wheeler: Burton Kendall Wheeler (February 27, 1882January 6, 1975) was an attorney and an American politician of the Democratic Party in Montana; he served as a United States Senator from 1923 until 1947.  He returned to his law practice and lived in Washington, D.C. for his remaining years.

Texas Democratic primary and caucuses, 2008: The 2008 Texas Democratic primary and caucuses were a series of events to determine the delegates that the Texas Democratic Party sent to the 2008 Democratic National Convention.  Delegates were selected using results from two sources: the Texas Presidential Primary held on March 4 by the Secretary of State of Texas's office, and a series of caucus events held between March 4 and June 7 by the Texas Democratic Party.  The indecisive results of Super Tuesday, and the fact that Texas had the largest number of delegates among the states remaining on the Democratic primary calendar, resulted in the Texas primary receiving significant attention from both the Hillary Clinton and Barack Obama campaigns.

United States Senate election in Montana, 1946: The 1946 United States Senate election in Montana took place on November 5, 1946.  Incumbent United States Senator Burton K. Wheeler, who was first elected to the Senate in 1922, and was re-elected in 1928, 1934, and 1940, ran for re-election.  He was challenged in the Democratic primary by Leif Erickson, the Chief Justice of the Montana Supreme Court, and, following a close election, was narrowly defeated by Erickson.  In the general election, Erickson faced State Senator Zales Ecton, the Republican nominee.  Ultimately, Ecton defeated Erickson by a fairly wide margin, and won his first and only term in the Senate.

Montana gubernatorial election, 1932: The 1932 Montana gubernatorial election took place on November 8, 1932.  Incumbent Governor of Montana John E. Erickson, who was first elected governor in 1924 and was re-elected in 1928, ran for re-election.  He won the Democratic primary with a plurality and advanced to the general election, where he faced Frank A. Hazelbaker, the Lieutenant Governor of Montana.  Despite the fact that Franklin D. Roosevelt carried the state in a landslide in the presidential election that year, Erickson only narrowly defeated Hazelbaker to win re-election to his third and final term as governor, though he would later resign just a few months into his term to appoint himself to the United States Senate.

Doug Gansler: Douglas F. "Doug" Gansler (born October 30, 1962) is an American attorney politician who served as the 45th Attorney General of Maryland.  Gansler previously served as the State's Attorney for Montgomery County, Maryland from 1999 to 2007.  He then won nomination in the state Democratic primary election for Attorney General and defeated Republican candidate Scott Rolle in the 2006 general election, taking 61% of the vote.  He was re-elected unopposed in the 2010 election.  Gansler lost the Democratic Primary race for Governor of Maryland on June 24, 2014 to Anthony Brown.

Pennsylvania Democratic primary, 2008: The 2008 Democratic primary in Pennsylvania was held on April 22 by the Pennsylvania Department of State in which voters chose their preference for the Democratic Party's candidate for the 2008 U.S. Presidential election.  Voters also chose the Pennsylvania Democratic Party's candidates for various state and local offices.  The selected candidates will be placed on the ballot of the 2008 General Election on November 4.  The Democratic primary was part of a General Primary that also included the 2008 Pennsylvania Republican primary.

Montana gubernatorial election, 1928: The 1928 Montana gubernatorial election took place on November 6, 1928.  Incumbent Governor of Montana John E. Erickson, who was first elected Governor in 1924, ran for re-election.  Erickson only narrowly won the Democratic primary against future Governor Roy E. Ayers, and advanced to the general election, where he was opposed by Wellington D. Rankin, the Attorney General of Montana.  Although Herbert Hoover carried the state in a landslide in the presidential election that year, Erickson managed to win re-election to his second term as Governor in a landslide over Rankin.

Susan Montee: Susan Montee (born July 6, 1959) is an American politician from the U.S. state of Missouri who served as the 35th State Auditor of Missouri.  She won the election in November 2006 and was sworn into her position on January 4, 2007.  She was the third woman in succession to serve as State Auditor of Missouri.  She succeeded now-U.S. Senator Claire McCaskill.  Montee is a member of the Democratic Party.  She was defeated in the 2010 election by Tom Schweich.  In 2011 Montee was elected the Chair of the Missouri Democratic Party, which she stepped down from later that year to run for Lieutenant Governor.  Susan defeated seven other candidates in the August, 2012 Missouri Democratic Primary for Lieutenant Governor of Missouri.  She lost the general election on November 6, 2012 to the Republican incumbent, Peter Kinder.

Bill McChesney (politician): Bill McChesney (born October 3, 1948) is an American politician and member of the Democratic Party who was a member of the Montana House of Representatives, representing District 40, from 2007 to 2015.  Term-limited in 2014, he ran for the 19th District of the Montana Senate but was defeated by Republican incumbent Frederick Moore.  He ran for Governor of Montana in the 2016 election against Democratic incumbent Steve Bullock, but lost in the Democratic primary.

Question: What  attorney and an American politician of the Democratic Party in Montana was was challenged in the Democratic primary by Leif Erickson in an  election in Montana ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_name": {
      "type": "string",
      "description": "The full name of the politician."
    },
    "party_affiliation": {
      "type": "string",
      "description": "The political party the politician belongs to."
    },
    "role_at_time_of_challenge": {
      "type": "string",
      "description": "The political office held by the politician when challenged in the primary."
    },
    "challenger_name": {
      "type": "string",
      "description": "The name of the person who challenged the politician in the primary."
    },
    "election_year": {
      "type": "integer",
      "description": "The year the election took place."
    },
    "election_type": {
      "type": "string",
      "description": "The type of election (e.g., United States Senate election)."
    },
    "primary_outcome_for_politician": {
      "type": "string",
      "description": "The outcome for the politician in the primary election."
    }
  },
  "required": [
    "politician_name",
    "party_affiliation",
    "role_at_time_of_challenge",
    "challenger_name",
    "election_year",
    "election_type",
    "primary_outcome_for_politician"
  ],
  "additionalProperties": false
}
