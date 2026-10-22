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
Adam Kinzinger: Adam Daniel Kinzinger (born February 27, 1978) is the U.S. Representative for Illinois 's 16 congressional district .  He is a member of the Republican Party.  He was first elected to Congress in 2010, winning election to represent Illinois's 11th congressional district.  After redistricting, he was re-elected to Congress in 2012, 2014, and 2016 to represent Illinois's 16th congressional district.

New York's 13th congressional district: New York's 13th Congressional District is a congressional district for the United States House of Representatives located in New York City, represented by Adriano Espaillat.  The district is the smallest Congressional district by area in the U.S.

Georgia's 11th congressional district: Georgia's 11th congressional district is a congressional district in the U.S. state of Georgia.  The district is currently represented by Republican Barry Loudermilk.  The district's boundaries have been redrawn following the 2010 census, which granted an additional congressional seat to Georgia.  The first election using the new district boundaries (listed below) were the 2012 congressional elections.

Dick Muri: Richard Walter "Dick" Muri (born November 30, 1953) is an American politician of the Republican Party.  He is a member of the Washington House of Representatives, representing the 28th legislative district.  Muri was appointed to the Washington State House of Representatives following (now former) State Representative Steve O'Ban's appointment to the Washington State Senate after State Senator Mike Carrell's death.  From 2003 to 2012, he served as a Republican member of the Pierce County Council, representing the 6th District.  In 2010, he ran as a Republican candidate for U.S. Congress in Washington's 9th congressional district against incumbent Democratic Congressman Adam Smith, eventually losing to Smith by nearly 10 points.  In 2012, he again ran, this time in Washington's 10th congressional district against Denny Heck, losing by 17 points.

Illinois's 19th congressional district: The 19th Congressional District of Illinois was a congressional district in Illinois.  The district became obsolete for 2013's 113th Congress, as population growth in Illinois was slower compared to other states.  It was last represented by Republican John Shimkus, who was redistricted to the 15th district.

New York's 19th congressional district: United States House of Representatives, New York District 19 is located in New York's Hudson Valley and Catskills regions.  District 19 lies north of the New York City metropolitan area and mostly south of Albany.  It is currently represented by Republican John Faso.

John Faso: John James Faso Jr. (born August 25, 1952) is an American politician and the U.S. Representative for New York 's 19 congressional district since January 3, 2017.  He served as minority leader of the New York State Assembly from 1998 until 2002, representing the 102nd district from 1987 until 2002.  A Republican, he gave up his seat in the Assembly to run for New York State Comptroller in 2002, losing to Alan Hevesi.  In 2006, he made a run for Governor of New York, but was defeated by Democratic nominee Eliot Spitzer.

Michael Grimm (politician): Michael Gerard Grimm (born February 7, 1970) is an American businessman, and politician who represented New York in the United States Congress from 2011 to 2015.  Grimm represented New York's 13th congressional district during his first term, after which he represented New York's 11th congressional district.  Both districts consisted of Staten Island and parts of Brooklyn.  Grimm is a member of the Republican Party, and during his time in office was the only Republican to represent a significant portion of New York City.  He is a former FBI agent, businessman, attorney, and U.S. Marine, having served in the Persian Gulf War.

Frederick R. Lehlbach: Frederick Reimold Lehlbach (January 31, 1876 – August 4, 1937) was an American lawyer and politician.  As a Republican, Lehlbach served as the U.S. Representative for New Jersey's 10th congressional district from 1915 to 1933 and as the representative from New Jersey's 12th congressional district from 1933 to 1937.  Lehlbach was also the nephew of Herman Lehlbach, a former U.S. Representative from New Jersey's 6th congressional district who served from 1885 to 1891.

Massachusetts's 5th congressional district: Massachusetts' 5th congressional district is a congressional district in eastern Massachusetts.  The district is represented by Katherine Clark.  Massachusetts congressional redistricting after the 2010 census has changed the borders of the district starting with the elections of 2012, with the new 3rd district largely taking the place of the old 5th.  The 5th district had covered many of the communities represented in the old 7th district.  As of 2010, the population of the 5th congressional district was 727,515.  On July 15, 2013, Ed Markey resigned from the seat to become the junior Senator from Massachusetts.  On December 10, 2013, Democrat Katherine Clark won a special election to fill the seat for the remainder of the 113th Congress.  She was sworn into office on December 12, 2013.

Question: New York's 19th congressional district is represented by what Republican?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "congressional_district": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string",
          "description": "The U.S. state the congressional district belongs to."
        },
        "district_number": {
          "type": "integer",
          "description": "The numerical identifier of the congressional district."
        }
      },
      "required": [
        "state",
        "district_number"
      ],
      "additionalProperties": false
    },
    "representative": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the U.S. Representative."
        },
        "party": {
          "type": "string",
          "description": "The political party of the representative."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the representative in YYYY-MM-DD format."
        },
        "date_assumed_office": {
          "type": "string",
          "format": "date",
          "description": "The date the representative assumed office for this district in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "party"
      ],
      "additionalProperties": false
    },
    "district_location_description": {
      "type": "string",
      "description": "A brief description of the geographical location of the district."
    }
  },
  "required": [
    "congressional_district",
    "representative",
    "district_location_description"
  ],
  "additionalProperties": false
}
