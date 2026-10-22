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
Hite Brewery: Hite Brewery Company Limited ( ; Korean: 하이트맥주 ; ) is a South Korean brewery company headquartered in Yeongdeungpo-gu, Seoul.  Its main products are beer, rice wine, and mineral water.  The company was established as Chosun Breweries in 1933.  In 2001 the company had three factories, and in 2002 its market share of the domestic beer market was some 55%, up from 30% in 1992.

Louisville Zombie Attack: The Louisville Zombie Attack started on August 29, 2005 as a flash mob, is a public event in Louisville, Kentucky held annually in August.  Before 2016, it had been held on August 29 at 8:29 p.m., but the 2016 event was moved to August 27 (which fell on a Saturday that year) at the same time and rebranded as the "Louisville Zombie Walk".  This resulted in a lawsuit between two of the event's co-founders, John King and Lyndi Curtis, which resulted in Curtis abandoning all rights to the event.  The Louisville Zombie Walk's co-organizer, Jason Bessemann, was not named in the suit and went on to promote the 2017 Louisville Zombie Walk as a separate event three days before the original.  Several thousand participants dressed and made up as zombies gather in the Highlands area and march down Bardstown Road to the end point of the walk.  An after party is typically thrown by all the bars included in the nightlife throughout the street after the walk.  Some of the bars included are: Nowhere Bar, Highlands Taproom, Big Bar, Baxter's, and many others in the local area.  Throughout the years, the walk grew by thousands as word of mouth caught on.  The last few years, the walk has generated over 10,000 walkers, with 30,000 in 2013 and 32,000 in 2014.  Over 40,000 walkers were anticipated for the 2015 event.  It began as a birthday party for three friends, but has turned into a real event recognized by local businesses.  The event typically costs around $10,000 to function, but the event is kept free to the public due to donations.

Littleton Gazette: The Littleton Gazette is an online newspaper based in Littleton, Colorado.  It specializes in local, community-based news and invites contributions from its readers and local businesses.  Its motto, adopted from an article in the original print newspaper called the Littleton Gazette, is "The day is long gone by for Littleton to slumber."

Holiday Hills (Washington): Holiday Hills are a group of mostly treeless, loam hills in Spokane County, Washington, at the foothills of the Selkirk Range.  Originally the hills were unnamed, but a resort opened on Carlson Hill, and eventually the hill became known as "Holiday Hill".  Eventually the name "Holiday Hills" was used to refer to the surrounding hills as a whole.  Eventually the name spread to local businesses, and when the resort, and other businesses eventually closed down, the hills retained their names.

Local Investing Opportunity Network: A Local Investing Opportunity Network, known as a (LION), is a loosely organized group of people who meet regularly with the goal of investing money in their local community.  The group will generally consist of individuals who have money to invest and people who might be in a position where they would be seeking investors.  The LION is designed to create opportunities for local businesses, individuals, and local investors to network and develop informal relationships.  The U.S. Securities and Exchange Commission has created some very specific laws about how one can ask for money.  These laws limit any kind of public offerings of shares/interest in a company (i.e. securities), unless there are proper filings and the people investing are considered accredited investors.  There is a general exemption that the SEC does not regulate where the investors are friends with the people they are investing in.  The LION hosts informal gatherings with the idea that friendships would form and the SEC guidelines would not be violated when any investments occur.  The LION also documents who attends the gatherings as a means of creating a paper trail proving that the individuals involved in an investment had the opportunity to form an informal relationship.

Masan: Masan was a former capital city of South Gyeongsang Province, South Korea.  The city is located in the coastal region along the Masan Bay (마산만, "Masan-man"), approximately 35 km away from Busan westward.  It was known for a textile industry, and now Hite Brewery is one of its major local business.  Since 2010, two neighbor cities and Masan have been united into Changwon .

Folk2Folk: Folk2Folk is a peer-to-peer business lender (P2P) specialising in local secured lending.  As a P2P lender it matches local businesses looking for finance with individual investors giving both sides a generally better rate than traditional banks.  Folk2Folk only provides secured loans, meaning that each loan is secured against property or land.  Folk2Folk's head office is based in Launceston, Cornwall, England.  The company operates online as well as having high street branches across the UK, currently in Devon, Cornwall, Somerset, Yorkshire and Gloucestershire.  It is one of the largest peer-to-peer lenders to business in the UK having lent over £160m to local, rural and entreprenuerial businesses.

Valley India Times: Valley India Times is an Indian American newspaper based in Arizona, mailed out to readers on a monthly basis.  The newspaper delivers to all major counties within the state, as well as to out of state subscribers.  It was created in 2000; the original name for the Indian newspaper, which was used during the first year of publishing, was "AZ India".  Due to the purchasing agreement when business ownership changed in 2000, the name was changed.  "Valley India Times" is the only Indian American newspaper in Arizona.  The paper, a complimentary mailing, has a website and social media networks.  Local businesses, holy establishments, and restaurants receive copies of the newspaper.

Diveagar: Diveagar (Dive Agar) is a village located in Shrivardhan Taluka, Raigad district in the Indian state of Maharashtra, approximately 170 kilometers south of Mumbai. The area is peaceful, clean and sparsely populated.  The region includes a fishing settlement, a beach, a temple, local businesses engaged in coconut and beetle nut tree farming, and some tourism businesses such as restaurants, cottage rentals and hotels, and six villages (from north to south): Velās, Musalmāndi, Agar Panchaitan, Diveagar, Borlai Panchaitan, and Kārle.  The beach, facing the Arabian Sea, is approximately four kilometers long and undeveloped.  At the north end of the beach where a small stream enters the ocean there is the fishing settlement, Velas Agar, and some paddy farming, while at the south end there is a sanctuary for migratory seabirds.  Nearby, there is a small fishing village, where vendors sell fresh fish, which goes by name of Bharadkhol.  The beach is accessible from the Mumbai-Goa highway via Kolad or Karnala.

Lukens Main Office Building: Lukens Main Office Building is a historic office building located at Coatesville, Chester County, Pennsylvania, USA.  The original section was designed by the noted architectural firm of Cope & Stewardson and built in 1902, for the Lukens Steel Company.  It is a 2½-story, seven bay, brick "T"-shaped building in a Colonial Revival / Georgian Revival style.  It has a hipped roof with dormers and flanking two-story, three bay wings.  A duplicate of the original structure was added to it in 1916, making it an "H"-shaped building.  The addition was designed by the successor firm of Page & Stewardson.  Today the building is home to the National Iron & Steel Heritage Museum and other local businesses and organizations.

Question: What was the original name of the brewery which is one of Masan's major local businesses?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "business_type": {
      "type": "string",
      "description": "The type of business."
    },
    "current_business_name": {
      "type": "string",
      "description": "The current name of the business."
    },
    "original_business_name": {
      "type": "string",
      "description": "The original name of the business."
    },
    "location_city": {
      "type": "string",
      "description": "The city where the business is a major local entity."
    }
  },
  "required": [
    "business_type",
    "current_business_name",
    "original_business_name",
    "location_city"
  ],
  "additionalProperties": false
}
