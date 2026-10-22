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
Gary Peters (politician): Gary Charles Peters (born December 1, 1958) is an American politician and businessman who is the junior United States Senator from Michigan.  A member of the Democratic Party, he was the U.S. Representative for Michigan 's 14 congressional district from 2013 until his election to the Senate.  The district includes the eastern half of Detroit, as well as the Grosse Pointes, Hamtramck, Southfield and Pontiac.  He previously represented Michigan 's 9 congressional district from 2009 to 2013.  Following the redrawing of congressional district boundaries after the 2010 United States Census, Peters defeated fellow Congressman Hansen Clarke in the Democratic primary and won re-election in the newly redrawn 14th District.

Allard K. Lowenstein: Allard Kenneth Lowenstein (January 16, 1929 – March 14, 1980) was an American Democratic politician, including a U.S. Representative of the 5th Congressional District in Nassau County, New York for one term in 1969 to 1971.  His work in the Civil Rights Movement and the antiwar movement has been cited as an inspiration by public figures including U.S. Secretary of State John Kerry; former U.S. Senators Bill Bradley, Gary Hart and Donald W. Riegle, Jr.; former U.S. Representative Barney Frank, California gubernatorial candidate Phil Angelides, columnist William F. Buckley, Jr., actor Warren Beatty, former White House Counsel Gregory Craig, former New York City Public Advocate Mark Green, and musician-songwriters Peter Yarrow and Harry Chapin.

Tom Graves: John Thomas Graves Jr. (born February 3, 1970) is the U.S. Representative for Georgia 's 14 congressional district , serving since winning a special election for Georgia 's 9 congressional district in 2010.  He is a member of the Republican Party.  Graves served in the Georgia House of Representatives before being elected to the House of Representatives.

Connie Mack IV: Cornelius Harvey McGillicuddy (born August 12, 1967), popularly known as Connie Mack IV, is the former U.S. Representative for  's 14 congressional district , serving from 2005 to 2013.  A member of the Republican Party, he was the Republican nominee for Senate in 2012, but lost to Democratic incumbent Bill Nelson.  He subsequently began a career in lobbying and currently represents Hungarian Prime Minister Viktor Orbán, among others.  Mack, born in Fort Myers, Florida, is the son of former Republican U.S. Senator Connie Mack III.

Frederick R. Lehlbach: Frederick Reimold Lehlbach (January 31, 1876 – August 4, 1937) was an American lawyer and politician.  As a Republican, Lehlbach served as the U.S. Representative for New Jersey's 10th congressional district from 1915 to 1933 and as the representative from New Jersey's 12th congressional district from 1933 to 1937.  Lehlbach was also the nephew of Herman Lehlbach, a former U.S. Representative from New Jersey's 6th congressional district who served from 1885 to 1891.

United States Senate election in Florida, 2012: The 2012 United States Senate election in Florida was held on November 6, 2012, alongside a presidential election, other elections to the United States Congress, as well as various state and local elections.  The primary election was held August 14, 2012.  Incumbent Democratic U.S. Senator Bill Nelson won reelection to a third term, defeating Republican U.S. Representative Connie Mack IV by 13%, winning 55% to 42%.  Nelson defeated Mack by over 1 million votes.

Bill Foster (politician): George William Foster (born October 7, 1955) is an American physicist, businessman and U.S. Representative for  's 11th congressional district , winning the seat in 2012.  He was previously the U.S. Representative for  's 14 congressional district from 2008 to 2011.  He is a member of the Democratic Party.

Mary Jo Kilroy: Mary Jo Kilroy (born April 30, 1949) is the former U.S. Representative for Ohio 's 15 congressional district , serving from 2009 until 2011.  She is a member of the Democratic Party from Ohio.  In her first term she introduced a bill to lend $20 million per year to small businesses (HR5322) and an amendment to assign liability to credit reporting agencies.  She also contributed to legislation on executive pay.  She was defeated in her November 2, 2010 re-election bid.  In 2012 she ran in the newly redrawn, Columbus-based 3rd congressional district but lost in the primary.

Steve LaTourette: Steven Clare "Steve" LaTourette (July 22, 1954 – August 3, 2016) was an American politician who served as the U.S. Representative for Ohio 's 19 congressional district and then Ohio 's 14 congressional district from 1995 to 2013.  He was a member of the Republican Party.  On July 30, 2012, it was reported that he would retire at the end of his term and not seek re-election.  He subsequently co-founded a lobbying firm.

Michael F. Doyle: Michael F. Doyle (born August 5, 1953) is the U.S. Representative for Pennsylvania 's 14 congressional district , serving in Congress since 1995, making him the Congressman from Pennsylvania with the most seniority, and the dean of the state's Congressional Delegation.  He is a member of the Democratic Party.  The district is based in Pittsburgh and includes most of Allegheny County.

Question: who defeated the former U.S. Representative for 's 14 congressional district in the 2012 Florida Elections?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "election_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the election took place"
        },
        "state": {
          "type": "string",
          "description": "The state where the election was held"
        },
        "election_type": {
          "type": "string",
          "description": "The type of election (e.g., Senate, Presidential)"
        }
      },
      "required": [
        "year",
        "state",
        "election_type"
      ],
      "additionalProperties": false
    },
    "winner": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the winning candidate"
        },
        "party": {
          "type": "string",
          "description": "The political party of the winner"
        },
        "incumbent_status": {
          "type": "string",
          "description": "Whether the winner was an incumbent"
        },
        "office_held": {
          "type": "string",
          "description": "The office held by the winner"
        },
        "vote_percentage": {
          "type": "integer",
          "description": "The percentage of votes received by the winner"
        }
      },
      "required": [
        "name",
        "party",
        "incumbent_status",
        "office_held",
        "vote_percentage"
      ],
      "additionalProperties": false
    },
    "defeated_candidate": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the defeated candidate"
        },
        "party": {
          "type": "string",
          "description": "The political party of the defeated candidate"
        },
        "former_office": {
          "type": "string",
          "description": "The former office held by the defeated candidate"
        },
        "former_district": {
          "type": "integer",
          "description": "The congressional district number the defeated candidate formerly represented"
        },
        "vote_percentage": {
          "type": "integer",
          "description": "The percentage of votes received by the defeated candidate"
        }
      },
      "required": [
        "name",
        "party",
        "former_office",
        "former_district",
        "vote_percentage"
      ],
      "additionalProperties": false
    },
    "margin_of_victory_percentage": {
      "type": "integer",
      "description": "The percentage difference in votes between the winner and the defeated candidate"
    }
  },
  "required": [
    "election_details",
    "winner",
    "defeated_candidate",
    "margin_of_victory_percentage"
  ],
  "additionalProperties": false
}
