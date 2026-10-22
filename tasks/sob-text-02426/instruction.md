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
John Alexander Paul Macgregor: General John Alexander Paul Macgregor (1780 – 5 March 1868), born John Alexander Paul, was an officer in the Bengal Army.

John Alexander Austin House: The John Alexander Austin House is a historic house in Memphis, Tennessee, U.S..  It was built circa 1876 for John Alexander Austin, a veteran of the Confederate States Army during the American Civil War of 1861-1865, and a clothing retailer.  It was designed in the Italianate architectural style.  It has been listed on the National Register of Historic Places since July 12, 1984.

Henry Burney: Henry Burney (27 February 1792 – 4 March 1845) was a British commercial traveller and diplomat for the British East India Company.  His parents were Richard Thomas Burney (1768–1808), headmaster of the Orphan School at Kidderpore, and Jane Burney (1772–1842), and he was a nephew of the English writer Frances Burney (1752–1840).  On 30 June 1818 at St. George's Church in George Town, Penang, Malaya, he married Janet Bannerman (1799–1865), with whom he had 13 children, eight of whom were still living at the time of his death.  She was the niece of John Alexander Bannerman, who was governor of Penang in Malaya.

The Northern Territories: The Northern Territories was an electronic music project from Sweden.  It was started in Uppsala in 1992 by John Alexander Ericson (vocals, instruments and electronics) and Stefan Sääf (vocals and electronics).  Musically this group centred on synthpop, their first two releases came on German label Machinery Records.  Later their music became more guitar influenced.  John Alexander Ericson started a solo career after their disbanding.

William Edward Phillips: William Edward Phillips was acting governor of the Prince of Wales' Island on three separate occasions; On the premature death of newly arrived Lieutenant-Governor Charles Andrew Bruce, Dec. 1810 till Archibald Seton arrived in 1811.  On the premature death of Lieutenant-governor William Petrie in 1816 till the arrival of Colonel John Alexander Bannerman in 1817.  On the premature death of Colonel John Alexander Bannerman in 1819 until he was appointed Lieutenant-governor in 1820.  He served as Lieutenant-Governor of Prince of Wales' Island from 4 June 1820 to 30 August 1824.

John Alexander Low Waddell: John Alexander Low Waddell (1854 – March 3, 1938, often shortened to J.A.L. Waddell and sometimes known as John Alexander Waddell) was an American civil engineer and prolific bridge designer, with more than a thousand structures to his credit in the United States, Canada, as well as Mexico, Russia, China, Japan, and New Zealand.  Waddell’s work set standards for elevated railroad systems and helped develop materials suitable for large span bridges.  His most important contribution was the development of the steam-powered high-lift bridge.  His design was first used in 1893 for Chicago's South Halsted Street Lift-Bridge over the Chicago River; he went on to design more than 100 other movable bridges, and the company he founded continues to make movable bridges of various types.  Waddell was a widely respected writer on bridge design, and an advocate of quality training of engineers.  Many of Waddell's surviving bridges are now considered historic landmarks.

Greg Alexander: Gregory Peter Stephen "Greg" Alexander (born 4 March 1965) is a former professional rugby league footballer of the 1980s and 90s who has since become a radio, television commentator and noted rugby league journalist.  Originally a goal-kicking half-back, in his career he played for and captained the Penrith Panthers and the Auckland Warriors clubs and also represented his country and state on several occasions.  Alexander's position for the majority of his career was at half-back, however early in his career – particularly in representative sides – he was moved to fullback.  It was this ability to play different positions with great success that saw Alexander make both the 1986 and the 1990 Kangaroo Tours.

John Alexander (footballer, born 1955): John Alexander (born 5 October 1955) is an English former footballer who holds the post of club secretary at Manchester United.  Born in Liverpool, Alexander began his football career with a club called Ulysses, before being picked up by Millwall, for whom he made his league debut in 1976.  After scoring twice in 15 appearances over the course of two years with Millwall, he moved to Reading; he enjoyed greater success with Reading, scoring nine goals in 25 games.  In 1981, he joined Northampton Town, but spent just one season with them before retiring from football at the age of 26 in 1982.  Upon retiring from football, Alexander got a job with the BBC, but he later returned to football as club secretary at Watford.  In 2000, he took up the same post at Tottenham Hotspur, spending 10 years there before applying for the same job at Manchester United, where he would replace the retiring Ken Ramsden.  He took over at Manchester United on 1 July 2010.  He is the uncle of Liverpool player Trent Alexander-Arnold.

Donald Macpherson: Lt-Col Donald Macpherson of Gaskmore and Kingston was an army officer who fought in the American Revolution, the War of 1812 and who raised a regiment of Clansmen from Scotland at his own expense to fight for Britain and Canada.  His nephew was Sir John Alexander Macdonald, GCB, KCMG, PC, PC (Can) first Prime Minister of Canada and driving force behind Canadian Confederation

Trent Alexander-Arnold: Trent John Alexander-Arnold (born 7 October 1998) is an English professional footballer who plays as a right-back for Premier League club Liverpool.  He is an academy graduate of Liverpool and made his senior debut for the club in 2016, aged 18.  The following year, he won the club's Young Player of the Season award.  He has also represented England at all youth levels from under-16 through to under-19.  Due to the length of his name, his surname is shortened to Alexander for Premier League fixtures.

Question: When did the nephew of John Alexander make his debut for Liverpool?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who made the debut."
    },
    "relationship_to_john_alexander": {
      "type": "string",
      "description": "The relationship of the person to John Alexander."
    },
    "club_debuted_for": {
      "type": "string",
      "description": "The name of the club for which the person made their debut."
    },
    "debut_year": {
      "type": "integer",
      "description": "The year the person made their senior debut for the club."
    }
  },
  "required": [
    "person_name",
    "relationship_to_john_alexander",
    "club_debuted_for",
    "debut_year"
  ],
  "additionalProperties": false
}
