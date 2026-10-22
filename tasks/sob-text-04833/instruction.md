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
Atlas Obscura: Atlas Obscura is an online magazine, led by American journalist David Plotz.  It was founded in 2009 by author Joshua Foer and documentary film-maker Dylan Thuras.  It features pieces on a variety of topics, including travel and exploration, history, science and some news.

Karaj Payam Noor University: Karaj Payam Noor University is located in Karaj, Iran, and has two campuses.  The main campus is located in Gohardasht, and another campus is located on Ghalamestan Street.  The university was founded in 2000-01.  In the school's founding year, 70 students were admitted for their BS in accounting.  The university now offers 52 courses at BS, BA, BE, MS, and MBA levels and has over 15,000 students.

Julia Turner (journalist): Julia Turner is an American journalist and critic.  She has been the editor-in-chief of online magazine "Slate" since 2014, replacing David Plotz.  She was one of a panel of three hosts on WNYC's Gabfest.

Muscular Dystrophy Canada: Muscular Dystrophy Canada (MDC) (French: Dystrophie musculaire Canada ) is a non-profit organization that strives to find a cure for neuromuscular disorders.  Founded in 1954 as Muscular Dystrophy Association of Canada, volunteers and staff nationwide have helped to provide support and resources to those affected.  Since the founding year, over $64 million has been put towards research via collaborations, fundraising events, and donations.

Louaize Club: Louaize Club is the basketball department of Notre Dame University – Louaize , a university basketball club basked in Zouk Mosbeh.  The club was established in the founding year of 1978 and is currently participating in the 2016 Lebanese Basketball League.

LensCulture: LensCulture is a photography network and online magazine about contemporary photography in art, media, politics, commerce and popular cultures worldwide: "a resource to keep up with the latest trends and debates in contemporary photography".  In addition to its online magazine and publishing network, LensCulture has hosted international photography portfolio reviews each year in Paris since 2010 in partnership with Paris Photo.  LensCulture sponsors international photography awards and grants several times per year, as well as traveling exhibitions of award-winning photography.

David Plotz: David Plotz (born January 31, 1970) is an American journalist and is currently the CEO of "Atlas Obscura", an online magazine devoted to discovery and exploration.  A writer with "Slate" since its inception in 1996, Plotz was the online magazine's editor from June 2008 until July 2014, succeeding Jacob Weisberg.

Diocesan Native Female Training School: Diocesan Native Female Training School (DNFTS, ) was a school under the Anglican Church of Hong Kong in the 19th century, founded in 1860 and closed down in 1868.  Its premises now belong to today's Bonham Road Government Primary School().  In 1869, another institution called Diocesan Home and Orphanage (DHO, later renamed Diocesan School and Orphanage, and now known as Diocesan Boys' School) was founded in the same place.  Due to the obvious differences in founding groups, vision of education, personnel arrangement and students’ background, DNFTS has been regarded only as a forerunner, and called ‘the First Foundation’ by DHO and later DBS.  Using 1869 as its founding year, DBS calls itself ‘the Second Foundation’.  As for Diocesan Girls' School, founded in Rose Villas near DSO in 1899, it claims to be the successor of DNFTS and traces the founding year back to 1860.

Stavanger: Stavanger (] ) is a city and municipality in Norway.  The city is the third-largest urban zone and metropolitan area in Norway (through conurbation with neighbouring Sandnes) and the administrative centre of Rogaland county.  The municipality is the fourth most populous in Norway.  Located on the Stavanger Peninsula in Southwest Norway, Stavanger counts its official founding year as 1125, the year the Stavanger Cathedral was completed.  Stavangers core is to a large degree 18th- and 19th-century wooden houses that are protected and considered part of the city's cultural heritage.  This has caused the town centre and inner city to retain a small-town character with an unusually high ratio of detached houses, and has contributed significantly to spreading the city's population growth to outlying parts of Greater Stavanger.

Small Wars Journal: The Small Wars Journal ("SWJ") is an online magazine focusing on intrastate conflict.  Aside from its online magazine, "SWJ" hosts an accompanying blog and the Small Wars Council discussion board.  Other site features include an online reference library, recommended reading and event listings.  The magazine is published by the Small Wars Foundation, a non-profit corporation.

Question: What is the founding year of the online magazine that David Plotz is currently the CEO of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_name": {
      "type": "string",
      "description": "The name of the online magazine."
    },
    "ceo_name": {
      "type": "string",
      "description": "The name of the current CEO of the magazine."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the online magazine was founded."
    }
  },
  "required": [
    "magazine_name",
    "ceo_name",
    "founding_year"
  ],
  "additionalProperties": false
}
