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
Peter Lilley: Peter Bruce Lilley (born 23 August 1943) is a British Conservative Party politician who was a Member of Parliament (MP) from 1983 to 2017 representing the constituency of Hitchin and Harpenden from 1997 and, prior to boundary changes, represented St Albans.  He was a Cabinet minister in the governments of Margaret Thatcher and John Major, serving as Trade and Industry Secretary from July 1990 to April 1992, and as Social Security Secretary from April 1992 to May 1997, when he introduced Incapacity Benefit.

Kirk Stensrud: Kirk D. Stensrud (born March 1962) is a Minnesota politician and former member of the Minnesota House of Representatives who represented District 48A, which included portions of western Hennepin County in the Twin Cities metropolitan area.  A Republican, he is the owner of Fish Window Cleaning in Edina, and a former medical salesperson.

Neslihan Demir: Neslihan Demir, (born December 9, 1983 in Eskişehir) is a Turkish volleyball star, currently playing for Galatasaray.  She is one of the most successful athletes of Turkey and has been among FIVB Heroes.  She represented her country as the flag-bearer at the 2012 Summer Olympics Parade of Nations and the official advertisement face of Turkey for the 2020 Summer Olympics candidateship along with basketballer Hedo Türkoğlu.  Her position is opposite-hitter and she has won a lot of personal awards in international tournaments.  She studied at Gazi University.

Billy Mays: William Darrell "Billy" Mays Jr. (July 20, 1958 – June 28, 2009) was an American television direct-response advertisement salesperson most notable for promoting Fix-it, OxiClean, Orange Glo, Kaboom, Zorbeez, and other cleaning, home-based, and maintenance products on the Home Shopping Network, and through his company, Mays Promotions, Inc.

ICan Benefit: iCan Benefit Group, LLC is a US based insurance agency that provides access to a wide range of health care plans and lifestyle benefits, some of them through association membership in a not-for-profit corporation called the Healthcare Cost Containment United Association (HCCUA).  The company was represented by Billy Mays from May 2008 until his death in June 2009.  Mays referred to iCan's insurance product as "the most important product I've ever endorsed."  He also featured iCan Benefit on his Discovery Channel show Pitchmen, just prior to his death.

United States military jury: A United States military jury (or "Members", in military parlance) serves a function similar to an American civilian jury, but with several notable differences.  Only a General Court-Martial (which, depending on the offense, may impose any sentence including death and a dishonorable discharge) or Special Court-Martial (which, depending on the offense, can impose a sentence up to one year in confinement and a bad-conduct discharge) includes members.  There are no members in a trial by Summary Court-Martial (which, depending on the offense, can impose a sentence up to 30 days in confinement).  If the accused at a general court-martial or special court-martial chooses to be tried by members rather than by a military judge alone, then the members are responsible for both rendering a verdict and a sentence should the accused be found guilty of the charges.  The charges are brought forward by an officer called a "convening authority", and the convening authority also personally selects each of the members who will try the accused.  The charges which have been levied by the convening authority are prosecuted at courts-martial by Judge Advocates called "trial counsel".  Accused persons facing general or special courts-martial receive representation free of charge from Judge Advocates acting as defense counsel.  Accused persons may also be represented at general or special courts-martial by civilian attorneys hired at their own expense.  While not required by Congressional law, service policy provides that many military accused receive the benefit of representation from a Judge Advocate defense counsel free of charge at summary courts-martial as well.

Tom LaBonge: Thomas J. "Tom" LaBonge (born October 6, 1953) is an American politician.  He was a member of the Los Angeles City Council representing the 4th district, serving from 2001 to 2015.  He won a special election to fill the seat left vacant by the death of long-time council member John Ferraro.  The district represents a wide diversity of incomes and neighborhoods.  At the time he was in office, he was the Chairman of the Arts, Parks, Health and Aging committee, Vice Chairman of the Transportation Committee and the Ad Hoc River Committee, and member of the Trade, Commerce & Tourism Committee, and the Ad Hoc on Recovering Energy, Natural Resources & Economic Benefit from Waste for L.A. (RENEW LA) in the city of Los Angeles.  He is a member of the Democratic Party.

Tony Ellin: Tony Ellin (July 19, 1965 – June 14, 2000) was a top-ranked American professional pool player nicknamed "Hurricane," who specialized in the game of nine-ball.  Born in New Jersey, Ellin made his home in Ladson, South Carolina, near Charleston, and was a touring professional player in the 1990s.  He was killed on June 14, 2000, at age 34, when his 1999 Cadillac collided with a locomotive less than a block from his home.  Ellin was alone in his car when the accident occurred.  Lt. Mike Benton, a Charleston County sheriff, said Ellin was "apparently trying to beat the train to the crossing."  Ellin had played in the Sand Regency Open just days before his death.  He was survived by wife Shelby, and daughter Ashley Annette who was just 3 years old at the time of his death.  Later that year a Tony Ellin memorial tournament was held at Brass Tap and Billiards in Raleigh, North Carolina, with receipts to benefit the Ashley Ellin Scholarship Fund, which was formed to benefit Ellin's daughter after his death.

Tim Maurer: Timothy Robert "Tim" Maurer (born October 10, 1980) is an American singer, best known as the former lead singer of third-wave ska band Suburban Legends.  He has left the band on two separate occasions.  The first was in 2000 after the recording of Origin Edition.  He rejoined the band in early 2002 after his replacement singer Chris Batstone left the band.  He officially left the band again in September 2005 after the band's third consecutive appearance on the Jerry Lewis MDA Telethon, performing a new song entitled "Moving Closer."  The band's former trumpet player, Vincent Walker, rejoined the band for the performance, then took over as lead singer afterward.  Maurer returned for a final performance with the band on November 29, 2005 at Huntington Beach High School for a benefit show for the Ryan Dallas Cook Memorial Fund, which was set up following the death of Suburban Legends' trombonist Dallas Cook.

Jerry Rosenberg (pitchman): Gerald "Jerry" Rosenberg (born circa 1934) was an American television direct-response advertisement salesperson most notable for promoting local businesses.  His distinctive balding scalp, rotund body, thick Brooklyn accent and impassioned sales pitches made him a recognized television presence in the United States, primarily in the New York Metropolitan Area.

Question: When was the advertisement salesperson who represented ICan Benefit until his death born? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the advertisement salesperson."
    },
    "role": {
      "type": "string",
      "description": "The primary role or profession of the person."
    },
    "company_represented": {
      "type": "string",
      "description": "The company the person represented."
    },
    "birth_date": {
      "type": "string",
      "description": "The full birth date of the person."
    },
    "birth_year": {
      "type": "integer",
      "description": "The year of birth of the person."
    },
    "death_date": {
      "type": "string",
      "description": "The full death date of the person."
    }
  },
  "required": [
    "person_name",
    "role",
    "company_represented",
    "birth_date",
    "birth_year",
    "death_date"
  ],
  "additionalProperties": false
}
