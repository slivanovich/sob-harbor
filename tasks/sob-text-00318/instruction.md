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
Emily Cain: Emily Ann Cain (born March 29, 1980) is an American politician from Maine and Executive Director of EMILY's List.  A member of the Democratic Party, Cain served in the Maine Senate from 2012 to 2014, representing the 30th district which includes part of Penobscot County.  She was previously a member of the Maine House of Representatives from 2004 to 2012, where she served as Minority Leader from 2008 to 2010 and as House Chair of the Appropriations & Financial Affairs Committee from 2010 to 2012.

Emily Grove (singer): Emily Grove (born August 1, 1991) is a singer-songwriter and musician from Wall, New Jersey.  Her sound has been described as alternative folk.  Emily Grove is active in the Asbury Park music scene in Monmouth County, New Jersey.  Emily Grove was the recipient of the 2011 and 2012 Asbury Music Awards for Best Female Acoustic Act, and 2011 and 2012 Jersey Acoustic Music Awards for Top Female Vocalist and Top Female Songwriter.  She has played with and opened for Glen Burtnik, Willie Nile, Ari Hest, Rhett Miller (Old 97s), Marshall Crenshaw, Dan Reed Network, and John Lefler (Dashboard Confessional).  Grove has toured the UK and US opening for and playing with David Ford.  Grove also performs in venues ranging from well known New Jersey music venues such as The Saint and the Stone Pony through music venues in New York City and Boston.

Bethany LeSueur: Bethany LeSueur (born January 6, 1983) is a former Long Island high school basketball player.  A six-year starter at guard for Garden City High School, LeSueur compiled a record of 121-12, a .910 winning percentage.  LeSueur led her team to three state final fours, three Long Island Championships, three Nassau County Championships, and six Conference Championships.  LeSueur was a scoring machine compiling 38 games of 30+ points.  Bethany LeSueur was twice named Gatorade Player of the Year for New York (2000, 2001) as well as Miss New York Basketball (2001).  She was a Street & Smith All-American, USA Today All-American, and also started in the Nike-WBCA All America Game.  LeSueur holds the Long Island scoring record (male or female) with 3,167 points.

Logan Vandeveer: Logan Vandeveer, early Texas Ranger, soldier, pioneer; ranger, cattleman, and civic leader, was born in Casey county, Kentucky about 1815.  He was the son of William and Emily (Shackleford) Vandeveer.  He came to Texas in 1833, joining Stephen F. Austin's Little Colony at Mina in present-day Bastrop County.

Emily Patricia Gibson: Emily Patricia Gibson (c.1864–24 April 1947) was a New Zealand proof-reader, feminist, socialist and internationalist.  She was born in Dublin, County Dublin, Ireland on c.1864.

Emily Fuller: Emily Fuller (born August 9, 1941) is an American artist who has been working in a variety of media since the Seventies.  Also known as Emily Rutgers Fuller, Emily R. Fuller, and Emily Fuller Kingston, she lives and works in New York City and Dutchess County, New York.

Baron Mount Temple: Baron Mount Temple was a title that was created twice in British history, both times in the Peerage of the United Kingdom.  The first creation came on 25 May 1880 when the Liberal politician the Honourable William Cowper-Temple was made Baron Mount Temple, of Mount Temple in the County of Sligo.  He was born William Cowper, the second son of Peter Clavering-Cowper, 5th Earl Cowper (see Earl Cowper for earlier history of the family) by his wife the Honourable Emily, sister of The 2nd Viscount Melbourne.  Emily married as her second husband The 3rd Viscount Palmerston, a man who would serve as British Prime Minister.  Lord Palmerston, an Anglo-Irish peer, died in 1865 when the viscountcy and his junior title of Baron Temple, of Mount Temple, became extinct.  Emily died 11 September 1869, leaving her second husband's estates, including Broadlands in Hampshire, to her second son, William, who thereupon adopted by Royal licence the surname Cowper-Temple, in whose favour the Mount Temple title was revived in 1880.

Glendale, California: Glendale is a city in Los Angeles County, California, United States.  Its estimated 2014 population was 200,167, making it the third largest city in Los Angeles County and the 23rd-largest city in California.  It is located about 8 miles (13 km) north of downtown Los Angeles.

Emily Lesueur: Emily LeSueur (born November 7, 1972 in Glendale, California) is an American competitor in synchronized swimming and Olympic champion.

Basil Davenport: Basil Davenport (1905-1966) was a literary critic, United States academic, anthologist, author of science fiction novels, and other genres.  He was born in Louisville, Kentucky on March 7, 1905, the son of Ira William Davenport and Emily Andrews Davison.  He died on April 7, 1966, in New York County, New York, at the age of 61.

Question: What county was Emily Lesueur born in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "birth_city": {
      "type": "string",
      "description": "The city where the person was born."
    },
    "birth_state": {
      "type": "string",
      "description": "The state where the person was born."
    },
    "birth_county": {
      "type": "string",
      "description": "The county where the person was born."
    }
  },
  "required": [
    "person_name",
    "birth_city",
    "birth_state",
    "birth_county"
  ],
  "additionalProperties": false
}
