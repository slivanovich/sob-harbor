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
Vapotherm: Vapotherm Inc., is a privately held corporation based in Exeter, New Hampshire that was founded in 1999 as a medical device manufacturer after creating the first heated and humidified high flow therapy nasal cannula system.

Cargill: Cargill, Inc. is an American privately held global corporation based in Minnetonka, Minnesota, a Minneapolis suburb, but incorporated in Wilmington, Delaware.  Founded in 1865, it is now the largest privately held corporation in the United States in terms of revenue.  If it were a public company, it would rank, as of 2015, number 15 on the Fortune 500, behind McKesson and ahead of AT&T.

Concord, California: Concord ( ) is the largest city in Contra Costa County, California.  At the 2010 census, the city had a population of 122,067 making it the 8th largest city in the San Francisco Bay Area.  Founded in 1869 as the community of Todos Santos by Salvio Pacheco, the name was changed to Concord within months.  The city is a major regional suburban East Bay center within the San Francisco Bay Area, and is 29 mi east of San Francisco.

Sharks Sports and Entertainment: Sharks Sports and Entertainment, Inc. is a privately held corporation based in San Jose, California, which owns and operates a number of sports properties, most notably the San Jose Sharks of the National Hockey League.  The company was established in 2000 as Silicon Valley Sports and Entertainment by Sharks owners Gordon and George Gund III to manage the business operations of the team, San Jose Arena (now SAP Center at San Jose) and the events held at the arena.  SVSE was among the assets purchased by San Jose Sports & Entertainment Enterprises when it bought the team and related properties from the Gund brothers in 2002, and became a subsidiary of SJSE as a result of the purchase.  The company was renamed Sharks Sports and Entertainment on August 24, 2011.

Valencia Group: Valencia Group is a privately held corporation based in Houston that has five hotel properties in the United States and numerous projects under development.

ImageTrend Inc: ImageTrend, Incorporated is a privately held corporation based in Lakeville, Minnesota in the United States.  ImageTrend began business in 1998, incorporating as a privately held Minnesota-based S-Corporation which develops Web-based software applications.

TLA Entertainment Group: TLA Entertainment Group is a privately held corporation based in Philadelphia, Pennsylvania.  It was founded in 1981.

Ovation Pharmaceuticals: Ovation Pharmaceuticals is an American manufacturer and distributor of pharmaceuticals products.  It was founded in 2000 by Jeffrey Aronin and is headquartered in Deerfield, Illinois.  A major office is also located near Lebanon, New Jersey.  Ovation is a privately held corporation based on a business model of acquiring mature but under-promoted pharmaceuticals, as well as pharmaceutical candidates which are far along the development and FDA certification processes.  Since 2009 the company has been wholly owned by the Danish pharmaceutical company Lundbeck.

BIAS: BIAS (originally known as Berkley Integrated Audio Software) was a privately held corporation based in Petaluma, California.  It ceased all business operations as of June, 2012.

BevMo!: BevMo!  is a privately held corporation based in Concord, California, selling mainly alcoholic beverages.  The company was founded in January 1994 as Beverages & More!  in the San Francisco Bay Area, and re-branded as "BevMo!"  in January 2001.  By October 2009, the company had 100 stores in Arizona and California.  As of September 2013, the number had expanded to 148 stores, including nine in Washington state.

Question:  BevMo! is a privately held corporation based in a city located how far from San Francisco ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the corporation."
    },
    "base_city": {
      "type": "string",
      "description": "The city where the corporation is based."
    },
    "city_location_details": {
      "type": "object",
      "properties": {
        "distance_from_san_francisco_miles": {
          "type": "integer",
          "description": "The distance of the base city from San Francisco in miles."
        },
        "direction_from_san_francisco": {
          "type": "string",
          "description": "The cardinal direction of the base city from San Francisco."
        }
      },
      "required": [
        "distance_from_san_francisco_miles",
        "direction_from_san_francisco"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "base_city",
    "city_location_details"
  ],
  "additionalProperties": false
}
