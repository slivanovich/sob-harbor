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
New Hampshire gubernatorial election, 1996: The 1996 New Hampshire gubernatorial election took place on November 5, 1996.  State Senator Jeanne Shaheen won the election.

New Hampshire gubernatorial election, 1992: The 1992 New Hampshire gubernatorial election took place on November 3, 1992.  Republican nominee Steve Merrill won the election.

New Hampshire gubernatorial election, 2016: The 2016 New Hampshire gubernatorial election took place on November 8, 2016, to elect the Governor of New Hampshire, concurrently with the 2016 U.S. presidential election, as well as elections to the United States Senate, elections to the United States House of Representatives and various state and local elections.

New Hampshire gubernatorial election, 2012: The 2012 New Hampshire gubernatorial election took place on November 6, 2012, concurrently with the 2012 U.S. presidential election, U.S. House elections, and various state and local elections.

New Hampshire gubernatorial election, 1990: The 1990 New Hampshire gubernatorial election took place on November 6, 1990.  Incumbent Governor Judd Gregg won reelection to a second term that would be his last, as he ran for and won election to the United States Senate in 1992.

Montana gubernatorial election, 1996: The 1996 Montana gubernatorial election took place on November 5, 1996.  Incumbent Governor of Montana Marc Racicot, who was first elected in 1992, ran for re-election.  After winning the Republican primary against a conservative activist, he moved on to the general election, where he was set to face Chet Blaylock, a former State Senator and the Democratic nominee.  However, on October 23, 1996, Blaylock died of a heart attack, and the Montana Democratic Party selected his running mate, State Senator Judy Jacobson, to replace him as the gubernatorial nominee, and she therefore appeared on the ballot as both the gubernatorial nominee and the lieutenant gubernatorial nominee.  Ultimately, however, Racicot was able to defeat Jacobson in a landslide to win re-election to his second and final term as governor.

New Hampshire gubernatorial election, 2006: The 2006 New Hampshire gubernatorial election took place on November 7, 2006.  Incumbent Democrat John Lynch defeated Republican James B. Coburn and won a second term as Governor of New Hampshire.

New Hampshire gubernatorial election, 1994: The 1994 New Hampshire gubernatorial election took place on November 8, 1994.  Incumbent Governor Steve Merrill won the election.

Jeanne Shaheen: Cynthia Jeanne Shaheen (née Bowers; January 28, 1947) is the senior United States Senator from New Hampshire, since 2009.

Minnesota lieutenant gubernatorial election, 1970: The 1970 Minnesota lieutenant gubernatorial election took place on November 3, 1970.  State Senator Rudy Perpich of the Minnesota Democratic-Farmer-Labor Party defeated Duluth Mayor Ben Boo of the Republican Party of Minnesota.  The 1970 lieutenant gubernatorial election was the final lieutenant gubernatorial election held before the Minnesota Constitution was amended to provide for elections of the Governor and Lieutenant Governor on a joint ticket.

Question: The 1996 New Hampshire gubernatorial election took place on November 5, 1996, who won the election for Senator?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "election_year": {
      "type": "integer",
      "description": "The year the election took place."
    },
    "election_date": {
      "type": "string",
      "description": "The specific date of the election."
    },
    "election_type": {
      "type": "string",
      "description": "The type of election (e.g., gubernatorial)."
    },
    "winner_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who won the election."
        },
        "role_at_time_of_election": {
          "type": "string",
          "description": "The political role or office held by the winner at the time of the election."
        },
        "office_won": {
          "type": "string",
          "description": "The office that was won in this election."
        }
      },
      "required": [
        "name",
        "role_at_time_of_election",
        "office_won"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "election_year",
    "election_date",
    "election_type",
    "winner_details"
  ],
  "additionalProperties": false
}
