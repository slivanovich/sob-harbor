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

Morgan Carroll: Morgan Lenore Carroll (born November 24, 1971) is an American politician from Colorado and is currently the Chairwoman of the Colorado Democratic Party.  A Democrat, Carroll represented Colorado House District 36 in the city of Aurora from 2004 to 2008, and she represented the state's 29th Senate district from 2009 to 2017.  Carroll served as President of the Colorado State Senate from 2013 to 2014 and as minority leader in 2015.  Carroll stepped down as minority leader in July 2015 to unsuccessfully run against incumbent Republican Mike Coffman for Colorado's 6th congressional district in the U.S. House of Representatives.  In addition to her legislative work, Carroll works for the law firm of Bachus & Schanker.

Dick Muri: Richard Walter "Dick" Muri (born November 30, 1953) is an American politician of the Republican Party.  He is a member of the Washington House of Representatives, representing the 28th legislative district.  Muri was appointed to the Washington State House of Representatives following (now former) State Representative Steve O'Ban's appointment to the Washington State Senate after State Senator Mike Carrell's death.  From 2003 to 2012, he served as a Republican member of the Pierce County Council, representing the 6th District.  In 2010, he ran as a Republican candidate for U.S. Congress in Washington's 9th congressional district against incumbent Democratic Congressman Adam Smith, eventually losing to Smith by nearly 10 points.  In 2012, he again ran, this time in Washington's 10th congressional district against Denny Heck, losing by 17 points.

Massachusetts's 5th congressional district: Massachusetts' 5th congressional district is a congressional district in eastern Massachusetts.  The district is represented by Katherine Clark.  Massachusetts congressional redistricting after the 2010 census has changed the borders of the district starting with the elections of 2012, with the new 3rd district largely taking the place of the old 5th.  The 5th district had covered many of the communities represented in the old 7th district.  As of 2010, the population of the 5th congressional district was 727,515.  On July 15, 2013, Ed Markey resigned from the seat to become the junior Senator from Massachusetts.  On December 10, 2013, Democrat Katherine Clark won a special election to fill the seat for the remainder of the 113th Congress.  She was sworn into office on December 12, 2013.

Hansen Clarke: Hansen Clarke (born March 2, 1957) is an American politician and former U.S. Congressman and Representative-elect in the 14th Congressional District of Michigan.  A Democrat, he was the U.S. Representative for Michigan 's 13th congressional district from 2011 to 2013.  Prior to his election to Congress, he had been a member of the Michigan House of Representatives from 1991 through 1992 and from 1999 through 2002, and had represented the 1st District in the Michigan Senate from 2003 to 2011.  Clarke was also the first U.S. Congressman of Bangladeshi descent.

Frederick R. Lehlbach: Frederick Reimold Lehlbach (January 31, 1876 – August 4, 1937) was an American lawyer and politician.  As a Republican, Lehlbach served as the U.S. Representative for New Jersey's 10th congressional district from 1915 to 1933 and as the representative from New Jersey's 12th congressional district from 1933 to 1937.  Lehlbach was also the nephew of Herman Lehlbach, a former U.S. Representative from New Jersey's 6th congressional district who served from 1885 to 1891.

Frank Lucas (Oklahoma politician): Frank Dean Lucas (born January 6, 1960) is an American politician.  Lucas is the U.S. Representative for Oklahoma 's 3 congressional district , serving since 2003, having previously represented the 6th district, from 1994 to 2003.  He is a member of the Republican Party and chairs the House Committee on Agriculture.  His district, numbered as the 6th district from 1994 to 2003, is the largest congressional district in the state and one of the largest in the nation that does not cover an entire state.  It covers 34,088.49 square miles and stretches from the Panhandle to the fringes of the Tulsa suburbs—almost half of the state's land mass.

Rick Nolan: Richard Michael Nolan (born December 17, 1943) is an American politician and member of the Minnesota Democratic–Farmer–Labor Party who has been the U.S. Representative for Minnesota's 8th congressional district since 2013 and previously served as the U.S. Representative for Minnesota's 6th congressional district from 1975 to 1981.

Fire from the Heartland: Fire From the Heartland: the Awakening of the Conservative Woman is a 2010 American documentary film written and directed by former Breitbart News LLC executive chairman Steve Bannon, and produced by David N. Bossie for Citizens United Productions.  The documentary stars Michele Bachmann, Deneen Borelli, and Ann Coulter, and focuses on female participation in conservative politics.

Michele Bachmann: Michele Marie Bachmann ( ; "née" Amble; born April 6, 1956) is an American politician.  A Republican, she is a former member of the United States House of Representatives, who represented Minnesota's 6th congressional district, a post she held from 2007 to 2015.  The district includes several of the northern suburbs of the Twin Cities, as well as St. Cloud.

Question: Among 'Fire From the Heartland' documentary stars who is an American politician and represented Minnesota's 6th congressional district  from 2007 to 2015?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "documentary_title": {
      "type": "string",
      "description": "The full title of the documentary mentioned in the question."
    },
    "documentary_stars": {
      "type": "array",
      "description": "A list of individuals who starred in the documentary, along with their relevant political information if available.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the documentary star."
          },
          "is_politician": {
            "type": "boolean",
            "description": "Indicates if the star is identified as an American politician in the context."
          },
          "political_office": {
            "type": "string",
            "description": "The political office held by the star, if applicable."
          },
          "congressional_district": {
            "type": "string",
            "description": "The specific congressional district represented by the star, if applicable."
          },
          "term_start_year": {
            "type": "integer",
            "description": "The start year of the congressional term, if applicable."
          },
          "term_end_year": {
            "type": "integer",
            "description": "The end year of the congressional term, if applicable."
          }
        },
        "required": [
          "name",
          "is_politician"
        ],
        "additionalProperties": false
      }
    },
    "identified_politician": {
      "type": "object",
      "description": "The politician identified based on the criteria in the question.",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the identified politician."
        },
        "congressional_district_represented": {
          "type": "string",
          "description": "The specific congressional district represented by the politician."
        },
        "term_start_year": {
          "type": "integer",
          "description": "The start year of the congressional term."
        },
        "term_end_year": {
          "type": "integer",
          "description": "The end year of the congressional term."
        }
      },
      "required": [
        "name",
        "congressional_district_represented",
        "term_start_year",
        "term_end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "documentary_title",
    "documentary_stars",
    "identified_politician"
  ],
  "additionalProperties": false
}
