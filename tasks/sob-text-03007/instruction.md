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
Real estate investing: Real estate investing involves the purchase, ownership, management, rental and/or sale of real estate for profit.  Improvement of realty property as part of a real estate investment strategy is generally considered to be a sub-specialty of real estate investing called real estate development.  Real estate is an asset form with limited liquidity relative to other investments, it is also capital intensive (although capital may be gained through mortgage leverage) and is highly cash flow dependent.  If these factors are not well understood and managed by the investor, real estate becomes a risky investment.  The primary cause of investment failure for real estate is that the investor goes into negative cash flow for a period of time that is not sustainable, often forcing them to resell the property at a loss or go into insolvency.  A similar practice known as flipping is another reason for failure as the nature of the investment is often associated with short term profit with less effort.

Gary W. Keller: Gary Keller is an American entrepreneur and best-selling author.  He is the founder of Keller Williams Realty International, which is the largest real estate company in the world by agent count.  Keller founded Keller Williams on training and education and later brought his teachings to print.  His books include "The Millionaire Real Estate Agent," "The Real Estate Investor," and "The ONE Thing".  He currently serves as the Chairman of the Board at Keller Williams Realty International.

Frederick S. Pardee: Frederick S. Pardee (born 1932) is an American economist, real estate investor and philanthropist from Los Angeles, California.  An alumnus of Boston University, Fred Pardee has now become one of the largest donors to the University.  He was a researcher at the RAND Corporation from 1957 to 1971.  He is a philanthropist and real estate investor who owns and manages apartment buildings in Los Angeles.  He has made charitable contributions to the RAND Corporation as well as several universities in the United States and a school in South Africa.  His most prominent charitable gift was of US$25 million to Boston University for the establishment of the Frederick S. Pardee School of Global Studies at Boston University, named for him.

Morris Goldseker: Morris Goldseker (December 24, 1898 - June 1973) was a real estate business tycoon, broker, and philanthropist.  He was President and Founder of M. Goldseker Real Estate Company, a Baltimore-based real-estate brokerage and services company, and is the founder of the Morris Goldseker Foundation.  Goldseker became a prominent real estate investor and broker and multi-millionaire in Baltimore during his forty-two years in the real estate business.

Real estate investment association: A real estate investment association or REIA may be a for profit or not for profit organization.  The typical mission of a REIA is to provide a forum both for networking as well as for professional level training in real estate investment.  The goals, methods, and tools available to a professional real estate investor are generally not the same as a typical real estate transaction.  For example: a professional investor may do hundreds of deals without even once obtaining a commercial loan to do so.  REIAs are a place for aspiring real estate investors to learn about transaction engineering, or ways to put together deals involving multiple parties in such a way that each party benefits from the transaction.

Rex Maughan: Rex G. Maughan is the founder, president, and CEO of Forever Living Products, a multi-level marketing program that sells aloe-vera based cosmetics and other personal products.  He is also a real-estate investor.

Scott Picken: Scott Picken is a South African-born real estate investor and entrepreneur.  He is the co-founder of Wealth Migrate, a fintech company that offers real estate investments on its online marketplace through crowdfunding.  He began offering real estate investment solutions at the age of 26 when he founded International Property Solutions. " The Huffington Post" named Wealth Migrate as one of the top 60 real estate crowdfunding solutions in the United States in 2014.

Real estate entrepreneur: A real estate entrepreneur or a real estate investor to a lesser extent is someone who actively or passively invests in real estate.  An active investor may buy a property, make repairs and/or improvements to the property, and sell it later for a profit.  A passive investor might hire a real estate firm to find and manage an investment property for him.  Typically, investors choose real estate for several reasons: cash flow, capital appreciation, depreciation, tax benefits and leverage.

Forever Living Products: Forever Living Products International, Inc. (FLPI) is a privately held multi-level marketing (MLM) company based in Scottsdale, Arizona, which manufactures and sells aloe vera-based drinks and bee-derived cosmetics, nutritional supplements, and personal care products.  The company was founded in 1978 by CEO Rex Maughan.  After acquiring the company Aloe Vera of America by the 1990s, In 2010, the company reported having over 4,000 employees, a network of 9.3 million distributors, and revenue of $1.7 billion.

Sunshine Empire: Sunshine Empire was a Multi Level Marketing (MLM) company, set up in 2006, based in Singapore.  It is now defunct, with assets frozen by the Singapore Court.  The company is listed by the Singapore Government's Monetary Authority in its Investor's Alert List, for possibly running investment schemes without authority.  After investigation by the Commercial Affairs Department (CAD) of the Singapore Police and a court trial, Sunshine Empire's Directors were charged with and found guilty of fraud, criminal breach of trust and falsifying accounts.

Question: What is the name of the multi level marketing company founded in 1978 by a real estate investor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the multi-level marketing company."
    },
    "company_type": {
      "type": "string",
      "description": "The type of company, e.g., 'Multi-level marketing'."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the company was founded."
    },
    "founder_details": {
      "type": "object",
      "properties": {
        "founder_name": {
          "type": "string",
          "description": "The name of the company's founder."
        },
        "is_real_estate_investor": {
          "type": "boolean",
          "description": "Indicates if the founder is also a real estate investor."
        }
      },
      "required": [
        "founder_name",
        "is_real_estate_investor"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "company_type",
    "founding_year",
    "founder_details"
  ],
  "additionalProperties": false
}
