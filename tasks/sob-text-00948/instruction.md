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
Dow Jones Global Titans 50: The Dow Jones Global Titans 50 Index is a float-adjusted index of 50 of the largest (by market capitalization) and best known blue chip companies traded on the New York Stock Exchange, American Stock Exchange, Nasdaq, Euronext, London Stock Exchange, and Tokyo Stock Exchange.  The index represents the biggest and most liquid stocks traded in individual countries.  It was created by Dow Jones Indexes to reflect the globalization of international blue chip securities in the wake of mergers and the creation of mega-corporations.

Consolidated Tape Association: The Consolidated Tape Association (CTA) oversees the dissemination of real-time trade and quote information (market data) in New York Stock Exchange (NYSE) and American Stock Exchange (AMEX) listed securities (stocks and bonds).  It is currently chaired by Emily Kasparov of the Chicago Stock Exchange, the first woman and the youngest chair elected to the position.

China Concepts Stock: China Concepts Stock is a set of stock of companies whose assets or earnings have significant activities in mainland China.  The People's Republic of China is undergoing major financial transformation, and many leading mainland-based companies have chosen to list themselves overseas to gain access to foreign investor capital.  Currently, there are China Concepts Stocks listed on several major stock exchanges around the globe, including the Hong Kong Stock Exchange (HKEx), Singapore Exchange (SGX), New York Stock Exchange (NYSE), NASDAQ, NYSE MKT (formerly known as the American Stock Exchange), London Stock Exchange (LSE), Euronext, and the Tokyo Stock Exchange (TSE).

Financial District, Manhattan: The Financial District, also known as FiDi, is a neighborhood located at the southern tip of the borough of Manhattan in New York City, which comprises the offices and headquarters of many of the city's major financial institutions, including the New York Stock Exchange and the Federal Reserve Bank of New York.  Anchored on Wall Street in the Financial District, New York City has been called both the most financially powerful city and the leading financial center of the world, and the New York Stock Exchange is the world's largest stock exchange by total market capitalization.  Several other major exchanges have or had headquarters in the Financial District, including the New York Mercantile Exchange, NASDAQ, the New York Board of Trade, and the former American Stock Exchange.

NYSE American: NYSE American, formerly known as the American Stock Exchange (AMEX), and more recently as NYSE MKT, is an American stock exchange situated in New York City, New York.  AMEX was previously a mutual organization, owned by its members.  Until 1953, it was known as the New York Curb Exchange.

New York Stock Exchange: The New York Stock Exchange (abbreviated as NYSE and nicknamed "The Big Board"), is an American stock exchange located at 11 Wall Street, Lower Manhattan, New York City, New York.  It is by far the world's largest stock exchange by market capitalization of its listed companies at US$21.3 trillion as of June 2017.  The average daily trading value was approximately 169 billion in 2013.  The NYSE trading floor is located at 11 Wall Street and is composed of 21 rooms used for the facilitation of trading.  A fifth trading room, located at 30 Broad Street, was closed in February 2007.  The main building and the 11 Wall Street building were designated National Historic Landmarks in 1978.

Consolidated Stock Exchange of New York: The Consolidated Stock Exchange of New York, also known as the "New York Consolidated Stock Exchange" or "Consolidated", was a stock exchange in New York City, New York in direct competition to the New York Stock Exchange (NYSE) from 1885-1926.  It was formed from the merger of other smaller exchanges, and was referred to in the industry and press as the "Little Board."  By its official formation in 1885, its membership of 2403 was considered the second largest membership of any exchange in the United States.

LyondellBasell: LyondellBasell Industries N.V. () is a public multinational chemical company with American and European roots, incorporated in the Netherlands, with U.S. operations headquarters in Houston, Texas, and global operations in London, UK.  It was formed in December 2007 by the acquisition of Lyondell Chemical Company by Basell Polyolefins for $12.7 billion.  LyondellBasell was listed on the New York Stock Exchange on October 14, 2010.  Lyondell was delisted from the New York Stock Exchange (formerly NYSE: LYO ) after the acquisition.

Enerpac: The Enerpac business is a division of Actuant (NYSE: [ ATU] ), a $1.5 billion diversified global manufacturing company, and is headquartered in Menomonee Falls, Wisconsin.  Enerpac primarily plays in the high-pressure hydraulics market with locations in North and South America, Europe, Africa, Russia, the Middle East, Asia, Australia, and New Zealand.  The business has 28 offices in 22 different countries and over 1,000 employees.  Enerpac produces and globally distributes high-pressure hydraulic products.  The business focuses on the design of products, from small cylinders to computer-operated lifting & positioning systems.

American Stock Exchange Building: The American Stock Exchange Building, formerly known as the New York Curb Exchange Building, is the former headquarters of the American Stock Exchange.  It is located on Trinity Place in the Financial District of Lower Manhattan, New York City.  Built in 1921 and enlarged in 1929-31, the building represents a link to the historical practices of stock trading outside the strictures of the New York Stock Exchange, which took place outside ("on the curb") prior to the construction of this building.  It was designated a National Historic Landmark in 1978.  The building presently stands vacant, the stock exchange having moved out after merging with the NYSE in 2008.

Question: The Enerpac business is a division of which organization, NYSE: [ ATU], a $1.5 billion diversified global manufacturing company, and is headquartered in Menomonee Falls, Wisconsin, The New York Stock Exchange (abbreviated as NYSE), is an American stock exchange, it is by far the world's largest?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "division_name": {
      "type": "string",
      "description": "The name of the business division."
    },
    "parent_organization": {
      "type": "string",
      "description": "The name of the organization that the business division belongs to."
    },
    "parent_organization_details": {
      "type": "object",
      "properties": {
        "nyse_ticker": {
          "type": "string",
          "description": "The NYSE ticker symbol of the parent organization."
        },
        "market_value_billion_usd": {
          "type": "number",
          "description": "The market value of the parent organization in billions of USD."
        },
        "company_description": {
          "type": "string",
          "description": "A brief description of the parent organization's business type."
        },
        "headquarters_location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the parent organization is headquartered."
            },
            "state": {
              "type": "string",
              "description": "The state where the parent organization is headquartered."
            }
          },
          "required": [
            "city",
            "state"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "nyse_ticker",
        "market_value_billion_usd",
        "company_description",
        "headquarters_location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "division_name",
    "parent_organization",
    "parent_organization_details"
  ],
  "additionalProperties": false
}
