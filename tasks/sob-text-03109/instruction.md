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
Michael Grimm (politician): Michael Gerard Grimm (born February 7, 1970) is an American businessman, and politician who represented New York in the United States Congress from 2011 to 2015.  Grimm represented New York's 13th congressional district during his first term, after which he represented New York's 11th congressional district.  Both districts consisted of Staten Island and parts of Brooklyn.  Grimm is a member of the Republican Party, and during his time in office was the only Republican to represent a significant portion of New York City.  He is a former FBI agent, businessman, attorney, and U.S. Marine, having served in the Persian Gulf War.

Howie Lind: Howard R. Lind (born October 3, 1957) is a retired U.S. Navy commander, former Special Assistant in the Office of the Secretary of Defense, former 10th Congressional District Republican chairman, was a 2014 candidate for the U.S. Senate in Virginia, and a 2014 candidate for the Republican nomination in Virginia's 10th Congressional District.

Jerrold Nadler: Jerrold Lewis Nadler (born June 13, 1947) is an American attorney and politician who serves as the U.S. Representative for New York 's 10 congressional district .  He is a member of the Democratic Party.

New York's 10th congressional district: New York's 10th Congressional District is a congressional district for the United States House of Representatives, formerly located from 2003 to 2013 in Brooklyn, New York City, currently represented by Democrat Jerrold Nadler.  The district contains the southern portion of Morningside Heights, the Upper West Side of Manhattan, the west side of Midtown Manhattan, the west side of Lower Manhattan, including Greenwich Village and the Financial District, and parts of Brooklyn, including Borough Park.

Dan Donovan (politician): Daniel Michael Donovan Jr. (born November 6, 1956) is an American attorney, former district attorney, and congressman from New York City.  He is currently the United States Representative for New York's 11th congressional district, winning the seat in May 2015 special election.  He found himself in the national limelight in 2014 after declining to indict Officer Daniel Pantaleo who put Eric Garner in a chokehold which some believed led to Garner's death.

Massachusetts's 10th congressional district: Massachusetts's 10th congressional district was a former district that last included parts of the South Shore of Massachusetts, and all of Cape Cod and the islands.  The District existed since 1795, but became obsolete for the 113th Congress in 2013 as district lines were redrawn to accommodate the loss of the seat due to reapportionment as a result of the 2010 Census.  Effective from the elections of 2012, most of the district falls into the new Massachusetts 9th congressional district, with some northern portions falling in the new 8th district.

Massachusetts's 5th congressional district: Massachusetts' 5th congressional district is a congressional district in eastern Massachusetts.  The district is represented by Katherine Clark.  Massachusetts congressional redistricting after the 2010 census has changed the borders of the district starting with the elections of 2012, with the new 3rd district largely taking the place of the old 5th.  The 5th district had covered many of the communities represented in the old 7th district.  As of 2010, the population of the 5th congressional district was 727,515.  On July 15, 2013, Ed Markey resigned from the seat to become the junior Senator from Massachusetts.  On December 10, 2013, Democrat Katherine Clark won a special election to fill the seat for the remainder of the 113th Congress.  She was sworn into office on December 12, 2013.

Frederick R. Lehlbach: Frederick Reimold Lehlbach (January 31, 1876 – August 4, 1937) was an American lawyer and politician.  As a Republican, Lehlbach served as the U.S. Representative for New Jersey's 10th congressional district from 1915 to 1933 and as the representative from New Jersey's 12th congressional district from 1933 to 1937.  Lehlbach was also the nephew of Herman Lehlbach, a former U.S. Representative from New Jersey's 6th congressional district who served from 1885 to 1891.

John Duncan Sr.: John James Duncan Sr. (March 14, 1919 – June 21, 1988) was an American attorney and Republican politician who represented Tennessee's 2nd Congressional District in the U. S. House of Representatives from 1965 until his death in 1988.  He also served as Mayor of Knoxville, Tennessee, from 1959 to 1964, and as assistant attorney general of Knox County, from 1948 until 1956.  He is the father of Congressman John Duncan Jr., who currently represents the 2nd District.

Dick Muri: Richard Walter "Dick" Muri (born November 30, 1953) is an American politician of the Republican Party.  He is a member of the Washington House of Representatives, representing the 28th legislative district.  Muri was appointed to the Washington State House of Representatives following (now former) State Representative Steve O'Ban's appointment to the Washington State Senate after State Senator Mike Carrell's death.  From 2003 to 2012, he served as a Republican member of the Pierce County Council, representing the 6th District.  In 2010, he ran as a Republican candidate for U.S. Congress in Washington's 9th congressional district against incumbent Democratic Congressman Adam Smith, eventually losing to Smith by nearly 10 points.  In 2012, he again ran, this time in Washington's 10th congressional district against Denny Heck, losing by 17 points.

Question: What American attorney currently represents New York's 10th Congressional District?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "representative": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "profession": {
          "type": "string"
        },
        "political_party": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "profession",
        "political_party"
      ],
      "additionalProperties": false
    },
    "congressional_district": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string"
        },
        "district_number": {
          "type": "integer"
        }
      },
      "required": [
        "state",
        "district_number"
      ],
      "additionalProperties": false
    },
    "is_current_representative": {
      "type": "boolean"
    }
  },
  "required": [
    "representative",
    "congressional_district",
    "is_current_representative"
  ],
  "additionalProperties": false
}
