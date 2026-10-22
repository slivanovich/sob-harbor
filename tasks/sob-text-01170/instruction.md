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
Coya Knutson: Cornelia Genevive Gjesdal "Coya" Knutson (August 22, 1912 – October 10, 1996) was an American politician from the U.S. state of Minnesota.  She served two terms in the Minnesota House of Representatives, from 1951 to 1955, before winning election to the U.S. House of Representatives from Minnesota's 9th congressional district as a member of the Democratic-Farmer-Labor Party (DFL).  She served two terms there, in the 84th and 85th Congresses, (from January 3, 1955 to January 3, 1959).

Collin Peterson: Collin Clark Peterson (born June 29, 1944) is an American politician, member of the Minnesota Democratic–Farmer–Labor Party, the U.S. Representative for Minnesota 's 7 congressional district , and the most senior representative from Minnesota, serving since 1991.  He is the ranking member of the House Committee on Agriculture and the dean of the Minnesota congressional delegation.  A conservative Democrat, his district, Minnesota's largest and most rural district, includes most of the western area of the state, including Moorhead, Fergus Falls, Bemidji, Detroit Lakes, Thief River Falls, Willmar, Marshall, and Alexandria.

Dewey Township, Roseau County, Minnesota: Dewey Township is a township in Roseau County, Minnesota, United States.  The population was 114 at the 2000 census.  Dewey is in the 7th congressional district of Minnesota and is represented by Democrat Collin Peterson.

Rick Nolan: Richard Michael Nolan (born December 17, 1943) is an American politician and member of the Minnesota Democratic–Farmer–Labor Party who has been the U.S. Representative for Minnesota's 8th congressional district since 2013 and previously served as the U.S. Representative for Minnesota's 6th congressional district from 1975 to 1981.

Kerry Gauthier: Kerry Gauthier (born November 6, 1955) is an American politician who served in the Minnesota House of Representatives from 2011 to 2013, representing portions of St. Louis County.  A Democrat, he served as Treasurer for the Minnesota Democratic-Farmer-Labor Party from 2005 to 2006, and Democratic Chairman of the state's 8th Congressional District from 2000 to 2006.  He had been an alderman for the Duluth City Council and campaign consultant, notably for Becky Lourey in the 2006 Minnesota gubernatorial election.  He retired in 2013 in the wake of a sex scandal.

Tom Rukavina: Thomas "Tom" Rukavina (born August 23, 1950) is a Minnesota politician and former member of the Minnesota House of Representatives.  A member of the Democratic-Farmer-Labor Party, he represented District 5A, including the Mesabi Range in St. Louis County in northeastern Minnesota.  In 2010 he was an unsuccessful candidate for Governor of Minnesota, seeking the Democratic-Farmer-Labor Party nomination.  Rukavina was elected a St. Louis County Commissioner in 2014.

Pramila Jayapal: Pramila Jayapal (pronounced ; born September 21, 1965) is an American politician and activist from the State of Washington who currently serves as the U.S. Representative for Washington 's 7 congressional district , which encompasses most of Seattle as well as outlying parts of King County.  As a member of the Democratic Party, she represented the 37th legislative district in the Washington State Senate from 2015 to 2017.  She is the first Indian-American woman to serve in the U.S. House of Representatives. , the first woman to represent the 7th District in Congress, and the first Asian-American to represent Washington in Congress.  As a sitting State Senator, Jayapal endorsed Senator Bernie Sanders for President of the United States in the 2016 Democratic primary.

Betty McCollum: Betty Louise McCollum (born July 12, 1954) is the U.S. Representative for Minnesota 's 4 congressional district , serving since 2001.  She is a member of the Democratic-Farmer-Labor Party (DFL).  McCollum's district centers on St. Paul, Minnesota's capital city.  She is the second woman elected to Congress from Minnesota.

Roy Wier: Roy William Wier (February 25, 1888 – June 27, 1963) was a U.S. Representative from Minnesota; born in Redfield, Spink County, South Dakota; moved with his parents in 1896 to Minneapolis, Hennepin County, Minnesota; attended the public schools and North High School; learned the telephone and electrical trade, later going into theatrical stage-lighting work; during the First World War served in the United States Army for eighteen months, with overseas service; in 1920 became active in the trade-union movement in Minneapolis and had been officially a representative of the Trades and Labor Assembly of Minneapolis; member of the Minnesota House of Representatives 1933 – 1939; member of the Minneapolis Board of Education 1939 – 1948 and the board of directors of Hennepin County Red Cross; elected as a member of the Democratic-Farmer-Labor Party to the 81st, 82nd, 83rd, 84th, 85th, and 86th congresses, (January 3, 1949 – January 3, 1961); unsuccessful candidate for reelection in 1960 to the 87th congress; was a resident of Minneapolis until May 1962, when he moved to Edmonds, Washington; died in Seattle, Washington, June 27, 1963; remains were cremated and the ashes deposited in the columbarium of Evergreen Washelli Cemetery.

Mark Andrew (politician): Mark Charles Andrew (born July 15, 1950) is an American businessman and politician from Minneapolis, Minnesota.  He is a member of the Democratic-Farmer-Labor party and has served as Hennepin County Commissioner, representing the western portion of Minneapolis and St. Louis Park, as well as Chair of the Hennepin County Board of Commissioners.  He also served as Chair of the Democratic-Farmer-Labor party in 1995–1996.  In 2007, Andrew founded GreenMark, an environmental marketing firm.  In February 2013, Andrew announced his candidacy for Mayor in the 2013 Minneapolis mayoral election.

Question: What is the name of this American politician, member of the Minnesta Democratic-Farmer-Labor Party, the U.S. Representative for Minnesota's 7 congressional district, and the most senior representative from Minnesota, representing Dewey Township, Roseau County, Minnesota?  

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_name": {
      "type": "string",
      "description": "The full name of the American politician."
    },
    "political_party": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the political party."
        },
        "abbreviation": {
          "type": "string",
          "description": "The abbreviation of the political party."
        }
      },
      "required": [
        "name",
        "abbreviation"
      ],
      "additionalProperties": false
    },
    "representative_information": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "description": "The political role held by the individual."
        },
        "state": {
          "type": "string",
          "description": "The U.S. state the individual represents."
        },
        "congressional_district": {
          "type": "integer",
          "description": "The number of the congressional district represented."
        },
        "is_most_senior_representative_from_state": {
          "type": "boolean",
          "description": "Indicates if the individual is the most senior representative from their state."
        },
        "service_start_year": {
          "type": "integer",
          "description": "The year the individual began serving in their current representative role."
        }
      },
      "required": [
        "role",
        "state",
        "congressional_district",
        "is_most_senior_representative_from_state",
        "service_start_year"
      ],
      "additionalProperties": false
    },
    "represented_locations": {
      "type": "array",
      "description": "A list of locations represented by the politician.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the location."
          },
          "type": {
            "type": "string",
            "description": "The type of location (e.g., 'township', 'city')."
          },
          "state": {
            "type": "string",
            "description": "The state where the location is situated."
          },
          "county": {
            "type": "string",
            "description": "The county where the location is situated, if specified."
          }
        },
        "required": [
          "name",
          "type",
          "state"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "politician_name",
    "political_party",
    "representative_information",
    "represented_locations"
  ],
  "additionalProperties": false
}
