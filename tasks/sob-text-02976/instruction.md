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
Monroe, Louisiana: Monroe (historically French: "Poste-du-Ouachita" ) is the eighth-largest city in the U.S. state of Louisiana.  It is the parish seat of Ouachita Parish.  In the official 2010 census, Monroe had a population of 48,815.  The municipal population declined by 8.1 percent over the past decade; it was 53,107 in the 2000 census.  After a recheck in 2012, the Census Bureau changed the 2010 population from 48,815 to 49,147.  Mayor Jamie Mayo, however, maintains that the Monroe population is more than 50,000 and indicated that he will pursue a continued challenge to the count.

Garden City, South Carolina: Garden City, sometimes known as Garden City Beach, is a census-designated place (CDP) in Horry County, South Carolina, United States.  While Garden City is sometimes considered to be a city it is not incorporated and does not yet have a city council or mayor.  The population was 9,357 at the 2000 census and the 2010 population estimate is around 11,014.  Garden City Beach is located directly south of Surfside Beach and ends on a peninsula at the mouth of Murrells Inlet.

Chupacabrachelys: Chupacabrachelys is an extinct genus of bothremydid turtle which existed in western Texas, United States during the late Cretaceous epoch (Campanian age).  Its fossils were discovered in Aguja Formation in the Big Bend region, and its type example is one of the most complete bothremydid specimens known.  It was first named by Thomas M. Lehman and Steven L. Wick in 2010 and the type species is "Chupacabrachelys complexus".

Palm Beach County, Florida: Palm Beach County is a county located in the state of Florida, directly north of Broward County.  As of the 2010 census, the population was 1,320,134, making it the third-most populous county in Florida.  The largest city and county seat is West Palm Beach.  Named after one of its oldest settlements, Palm Beach, the county was established in 1909, after being split from Dade County.  The county's modern-day boundaries were established in 1963.  Palm Beach County is one of the three counties in South Florida which make up the Miami metropolitan area, which was home to an estimated 6,012,331 people at the 2015 census.

Waco, Texas: Waco ( ) is a city which is the county seat of McLennan County, Texas, United States.  It is situated along the Brazos River and I-35, halfway between Dallas and Austin.  The city had a 2010 population of 124,805, making it the 22nd-most populous city in the state.  The US Census 2016 population estimate is 134,432 The Waco Metropolitan Statistical Area consists of McLennan and Falls Counties, which had a 2010 population of 234,906.  Falls County was added to the Waco MSA in 2013.  The US Census 2016 population estimate for the Waco MSA is 265,207.

Steven L. Labriola: Steven L. Labriola (born June 26, 1962) is an American politician.  From 1997 to 2002, he served as the representative of the 12th district in the New York State Assembly.  From 2004 to 2010, he served as the town clerk for Oyster Bay, New York.

Steven K. Baum: Steven K. Baum, PhD is a genocide scholar, gerontologist with an MA in psychopharmacology from New Mexico State University (2010).  He has written several books including The Psychology of Genocide (Cambridge University Press 2008), Antisemitism Explained (UPA 2012), and with co-editors Florette Cohen and Steven L. Jacobs, the forthcoming Antisemitism in North America (Brill).  He founded with N. E. Rosenberg and is chief editor of the Journal for the Study of Antisemitism (JSA).  Baum practices psychology in Albuquerque, New Mexico.

Steve Black (politician): Steven L. Black is a Canadian politician, currently mayor of Timmins, Ontario.  He was elected in the municipal election on October 27, 2014 defeating former Councillor Todd Lever by taking 65% of the vote, and becoming Timmins' youngest Mayor ever elected.  He succeeded retiring mayor Tom Laughren.

Steven L. Miller: Steven L. Miller is a businessman who has been a prominent leader in the American oil industry, serving as Chairman of the Board of Directors, President, and C.E.O. of Shell Oil Company from 1999 to his retirement in 2002.  A native of Kansas City, Missouri, he was born in 1945, and attended the University of Illinois at Urbana-Champaign in 1967.  He currently resides in Houston, Texas, where he promotes volunteer work through his company, SLM Discovery Ventures.

Steven L. Abrams: Steven L. Abrams (born 1958 in Des Moines, Iowa) is an American politician.  He is the first mayor of Palm Beach County in the U.S. state of Florida.  He previously served as chairman of the Palm Beach County Board of County Commissioners.  He represents District 4 on the county commission.  Abrams is the former mayor of the City of Boca Raton, Florida.  A lawyer, he was elected mayor in March 2001 and re-elected in 2003 and 2005.  He previously served as a city council member from 1989-1999.  In March 2009, Abrams was appointed by Florida governor Charlie Crist to occupy the district four county commission seat vacated by Mary McCarty after her resignation due to federal corruption charges.  He won election to a full term when no one filed to run against him in 2010.  Abrams received his bachelor's degree from Harvard University in Government in 1980 and his law degree from The George Washington University in 1985.  His past experience includes law clerk in the White House under President Ronald Reagan.  He was a partner of the now defunct Rothstein Rosenfeldt Adler firm.

Question: What was the 2010 population of the city where Steven L. Abrams was mayor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who was mayor."
    },
    "location_of_mayorship": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the city or county where the person was mayor."
        },
        "type": {
          "type": "string",
          "description": "The type of the location (e.g., city, county)."
        },
        "state": {
          "type": "string",
          "description": "The U.S. state where the location is situated."
        }
      },
      "required": [
        "name",
        "type",
        "state"
      ],
      "additionalProperties": false
    },
    "population_data": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year for which the population data is provided."
        },
        "value": {
          "type": "integer",
          "description": "The population value for the specified year."
        }
      },
      "required": [
        "year",
        "value"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "location_of_mayorship",
    "population_data"
  ],
  "additionalProperties": false
}
