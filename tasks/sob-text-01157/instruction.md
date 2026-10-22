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
Frederick Thomas Gray: Frederick Thomas Gray (October 10, 1918 – May, 1992) was a Virginia attorney and Democratic Party politician.  Governor James Lindsay Almond Jr. appointed Gray to serve as Attorney General of Virginia after the resignation of Attorney General Albertis Harrison (a member of the Democratic political organization led by Senator Harry F. Byrd) to run for Governor of Virginia during the Massive Resistance crisis in Virginia.  Gray returned to private practice at Williams Mullen after Robert Young Button (elected Attorney General during the same 1961 election in which Harrison became Governor) took office.  Gray later served in the Virginia House of Delegates and the Virginia Senate (both part-time positions) as he continued his law practice.

Warren Spannaus: Warren R. Spannaus (born December 5, 1930) is an American politician from the Democratic-Farmer-Labor Party (DFL) and former Attorney General of Minnesota.  Spannaus graduated from the University of Minnesota Law School in 1963.  He was elected attorney general in 1970 and assumed office on January 4, 1971.  Spannaus was reelected to the position twice, in 1974 and 1978, serving from 1971 to 1983.  In 1982, he ran for Governor of Minnesota as the DFL-endorsed candidate but lost the primary election to former DFL Governor Rudy Perpich, who went on to win the general election.  Spannaus joined the Minneapolis-based law firm of Dorsey & Whitney and is now retired.  Spannaus married Marjorie Clarkson and had three children: Christine, David, and Laura.  He also has seven grandchildren: Andrew, Eric, Alison, Rocco, Marco, Jack and Elizabeth.

Pennsylvania Attorney General election, 2004: Pennsylvania's Attorney General election was held November 2, 2004.  Necessary primary elections were held on April 27, 2004.  Tom Corbett was elected Attorney General, a position that he had held from 1995-97 after being appointed by Governor Tom Ridge to fill a vacancy.  Corbett, who had been a U.S. Attorney, narrowly defeated Montgomery County District Attorney Bruce Castor in the Republican primary, then won by an even tighter margin in the general election.  Corbett's Democratic opponent was Jim Eisenhower, the 2002 nominee who had once served as an Assistant U.S. Attorney and had been a close confidant of Governor Ed Rendell.  Eisenhower won in a primary that featured three top-tier candidates: his opponents were David Barasch, a former U.S. Attorney, and John Morganelli, the Northampton County District Attorney who was narrowly defeated by Eisenhower in the previous Democratic primary for this position.

Peg Lautenschlager: Peggy A. "Peg" Lautenschlager (born November 22, 1955) is the current chair of the Wisconsin Ethics Commission.  She was Attorney General of the State of Wisconsin from January 3, 2003 to January 3, 2007.  She succeeded fellow Democrat Jim Doyle when Doyle was elected Governor of Wisconsin in 2002.  Lautenschlager is the first woman to have been elected Attorney General in the State of Wisconsin.

Frankie Sue Del Papa: Frankie Sue Del Papa (born September 21, 1949) is an American attorney and politician in the U.S. state of Nevada; she is associated with the Democratic Party.  Del Papa was the first woman elected as Secretary of State of Nevada (1986) and the first woman elected as Nevada Attorney General (1990, 1994, and 1998).  In addition, Del Papa was the first woman elected student body president at the University of Nevada.

Lori Swanson: Lori Swanson (born December 16, 1966) from Eagan, Minnesota is the Attorney General of the US state of Minnesota.  She was elected on November 7, 2006, and took office on January 2, 2007, succeeding Mike Hatch, who declined to run for re-election in order to run for governor.  She is the first woman elected Minnesota's Attorney General.

Virginia Attorney General election, 2005: The Virginia Attorney General election of 2005 took place on November 8, 2005, to elect the Attorney General of Virginia.  Jerry Kilgore, who had been elected attorney general in 2001, resigned in February 2005 to run for Governor, as is the tradition in Virginia.  He was replaced by Judith Jagdmann, the Deputy Attorney General for the Civil Litigation Division, who did not run in the election.

Bob Ferguson (politician): Robert Watson Ferguson (born February 23, 1965) is an American attorney and politician who is the 18th and current Attorney General of Washington, serving since 2013.  He was first elected Attorney General in 2012, and reelected in 2016.  Prior to serving as Attorney General, Ferguson was a member of the King County Council.  Ferguson is a member of the Democratic Party.

Minnesota Attorney General election, 2010: The 2010 Minnesota Attorney General election was held on Tuesday, November 2, 2010 to elect the Minnesota Attorney General for a four-year term.  Primary elections were held on August 10, 2010.  Incumbent Lori Swanson of the Minnesota Democratic–Farmer–Labor Party (DFL) won reelection to a second term.

Michigan Attorney General election, 2006: The Michigan Attorney General election of 2006 took place on November 7, 2006, to elect the Attorney General of Michigan.  Incumbent Mike Cox became the first Republican in over 50 years to be elected Attorney General and was seeking to become the first Republican since the amending of the Michigan Constitution to be re-elected.  Despite a 2005 scandal where Cox announced he had an extramarital affair before becoming Attorney General Cox won re-election easily, defeating Democratic nominee Amos Williams, taking 54 percent of the vote.

Question: The first woman elected Attorney General of Minnesota, served under what party?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who was the first woman elected Attorney General."
    },
    "office_held": {
      "type": "string",
      "description": "The office held by the person."
    },
    "state": {
      "type": "string",
      "description": "The U.S. state where the office was held."
    },
    "political_party": {
      "type": "string",
      "description": "The political party the person belonged to."
    },
    "election_year": {
      "type": "integer",
      "description": "The year the person was first elected to the office."
    },
    "is_first_woman_elected": {
      "type": "boolean",
      "description": "Indicates if the person was the first woman elected to this specific office in the state."
    }
  },
  "required": [
    "person_name",
    "office_held",
    "state",
    "political_party",
    "election_year",
    "is_first_woman_elected"
  ],
  "additionalProperties": false
}
