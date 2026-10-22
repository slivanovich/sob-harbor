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
Davenport, Iowa: Davenport is the county seat of Scott County in Iowa and is the largest of the Quad Cities, a metropolitan area with a population estimate of 382,630 and a CSA population of 474,226, making it the 90th largest CSA in the nation.  Davenport was founded on May 14, 1836 by Antoine Le Claire and was named for his friend, George Davenport, a colonel during the Black Hawk War stationed at nearby Fort Armstrong.  According to the 2010 census, the city had a population of 99,685 (making it Iowa's third-largest city).  However, the city is currently appealing this figure, arguing that the Census Bureau missed a section of residents that would place the total population over 100,000, and indeed, even the Census Bureau's own "estimate" for Davenport's 2011 population is 100,802.

Huaihua: Huaihua () is a prefecture-level city in the south western Hunan, China.  it covers 27,564 km2 and is bordered by Xiangxi to the northern west; Zhangjiajie, Changde to the north; Yiyang, Loudi and Shaoyang to the east; Guilin and Liuzhou of Guangxi to the south; Qiandongnan, Tongren of Guizhou to the southern west.  It has 4,741,948 of population (2010 census), shares 7.22% of the province.  According to 2010 Census, there are 2,909,574 Han Chinese, Han shares 61.4% of the population, 1,832,289 population of minorities, 38.6%; Dong, Miao, Tujia, Yao and Bai are major native minorities.  Huaihua is the central region of Dong ethnic population, there lives 816,481 Dong people (2010 census), it shares 28.35 per centage of Chinese Dong ethnic group.

Altoona, Pennsylvania: Altoona is a city in Blair County, Pennsylvania, United States.  It is the principal city of the Altoona Metropolitan Statistical Area (MSA).  The population was 46,320 at the time of the 2010 Census, making it the eleventh most populous city in Pennsylvania.  The Altoona MSA includes all of Blair County and was recorded as having a population of 127,089 at the 2010 Census, around 100,000 of whom live within a 5 mi radius of the Altoona city center according to U.S. Census ZIP Code population data.  This includes the adjacent boroughs of Hollidaysburg and Duncansville, adjacent townships of Logan, Allegheny, Blair, Frankstown, Antis, and Tyrone, as well as nearby boroughs of Bellwood and Newry.

GrandPa's: GrandPa's or GrandPa Pidgeon's was a discount store founded in 1954 by Tom and Mildred Pidgeon, spreading across the midwest from its Bridgeton, Missouri (near St. Louis) origins, which remained truly "discount", when most others like Venture, Kmart and Target gradually raised prices in order to finance a more attractive layout and broader range of merchandise.  Tom Pidgeon, born in Sebring, Ohio in 1902, was in the low price china business from the early 1930s to the early 1950s.  He sold his company, Pidgeon Vitrified China in 1953 when he foresaw the impact plastic was having on the lower end dinnerware market.  The first Grandpa Pidgeon's was opened in February 1954 and managed by his son-in-law, John (Jack) Holley, born in 1924 in Galena, Kansas.

Union, South Carolina: The city of Union is the county seat of Union County, South Carolina, United States.  The population was 8,393 at the 2010 census.  It is the principal city of the Union Micropolitan Statistical Area (population 28,961 according to 2010 Census), an (MSA) which includes all of Union County and which is further included in the greater Greenville-Spartanburg-Anderson, South Carolina Combined Statistical Area (population 1,266,995 according to the 2010 Census).

Galena, Kansas: Galena is a city in Cherokee County, Kansas, United States.  As of the 2010 census, the city population was 3,085.

North Stamford: North Stamford is a section of Stamford, Connecticut, USA, north of the Merritt Parkway.  Mostly woody and hilly, it is the least densely populated, and highest income section of the city.  The two main roadways in North Stamford are High Ridge Road (Connecticut Route 137) and Long Ridge Road (Connecticut Route 104).  North Stamford borders Pound Ridge, New York at the New York line to the north, the "back country" section of Greenwich, Connecticut to the west, and the Town of New Canaan, Connecticut to the east.  According to the 2010 census, North Stamford has a population of 14,904.  The City of Stamford as a whole had a population of 122,643 (per the 2010 Census) with most recent estimates showing Stamford's population around 128,000.

Murrieta, California: Murrieta is a city in southwestern Riverside County, California, United States.  The population of Murrieta was 103,466 at the 2010 census.  Murrieta experienced a 133.7% population increase between 2000 and 2010, according to the most recent census, making Murrieta one of the fastest growing cities in the state.  This population boom in 2010 surpassed the population of the historically larger and more commercial city of Temecula to the south for the first time since the incorporation of either city.  Temecula and Murrieta together form the southwestern anchor of the Inland Empire region.  The Murrieta-Temecula-Menifee Urban Area had a population of 441,546 at the 2010 Census.  Largely residential in character, Murrieta is typically characterized as a commuter town, with many of its residents commuting to jobs in San Diego County, Orange County, Los Angeles County, Temecula, and Camp Pendleton.

White House, Tennessee: White House is a city in Robertson and Sumner counties in the United States state of Tennessee.  The population was 7,220 at the 2000 census.  It is approximately twenty-two miles north of downtown Nashville.  According to the city website a special census was conducted in 2008 that placed the city population at 9,891 residents, with 3,587 households within the city limits.  The population was 10,255 at the 2010 census which showed growth of 3,000 people from 2000 to 2010.  The 2013 population was 10,752.

Gaffney, South Carolina: Gaffney is a city in and the seat of Cherokee County, South Carolina, United States, in the Upstate region of South Carolina.  Gaffney is known as the "Peach Capital of South Carolina".  The population was 12,539 at the 2010 census, with an estimated population of 12,597 in 2014.  It is the principal city of the Gaffney, South Carolina, Micropolitan Statistical Area (population 55,662 according to 2012 estimates by the U.S. Census Bureau), which includes all of Cherokee County and which is further included in the greater Greenville-Spartanburg-Anderson, South Carolina Combined Statistical Area (population 1,384,996 according to year 2012 U.S. Census Bureau estimates).

Question: According to the 2010 census, what was they population of the city in which John (Jack) Holley was born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city where John (Jack) Holley was born."
    },
    "birth_year_of_person": {
      "type": "integer",
      "description": "The birth year of John (Jack) Holley."
    },
    "census_year": {
      "type": "integer",
      "description": "The year of the census for which the population is reported."
    },
    "population": {
      "type": "integer",
      "description": "The population of the city according to the specified census year."
    }
  },
  "required": [
    "city_name",
    "birth_year_of_person",
    "census_year",
    "population"
  ],
  "additionalProperties": false
}
