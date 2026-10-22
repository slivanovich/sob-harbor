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
CapitaLand: CapitaLand Limited (Chinese: 凯德集团,), is a Singapore based real estate company.  Formed in November 2000 as a result of a merger of DBS Land and Pidemco Land, it is one of Asia's largest real estate companies headquartered and listed in Singapore.  The company leverages its significant asset base, design and development capabilities, active capital management strategies, and extensive market network and operational capabilities to develop high-quality real estate products and services.  Its two core markets are Singapore and China, while Indonesia, Malaysia and Vietnam have been identified as new growth markets.  The company also has one of the largest real estate fund management businesses with assets located in Asia.  CapitaLand’s listed real estate investment trusts (REITs) are CapitaLand Mall Trust, CapitaLand Commercial Trust, Ascott Residence Trust, CapitaLand Retail China Trust and CapitaLand Malaysia Mall Trust.

F. Blair Wimbush: Frederick Blair Wimbush (born July 24, 1955), is a retired American railroad executive and lawyer.  He continues to be a civic and professional leader.  From 1980 to 2004, Wimbush progressed through positions of increasing responsibility in the Norfolk and Western Railway Company and Norfolk Southern Corporation Law Departments, including Senior General Counsel in 2002.  In June 2004, he was elected Vice President, Real Estate of Norfolk Southern Corporation, parent company of Norfolk Southern Railway Company.  In November 2007, he became the first, and as of August 11, 2012 the only, executive level Corporate Sustainability Officer in the railroad industry, in addition to his real estate position.  He managed several large conservation and energy efficiency projects for the company and has spoken on corporate sustainability at several corporate and educational conferences.  He retired from Norfolk Southern Corporation after 35 years of service on May 1, 2015.  Wimbush has served on the boards of the Hampton Roads Association of Commercial Real Estate, Hampton Roads Economic Development Alliance, and the Monarch Bank Norfolk City Board.  On April 4, 2015, Virginia Governor Terry McAuliffe announced that Wimbush had been appointed to the Virginia Port Authority board.  On June 24, 2016, Governor McAuliffe reappointed Wimbush to a full five-year term ending June 30, 2021.

Simon Youth Foundation: Simon Youth Foundation (SYF) is a non-profit, 501 (c)(3) organization that supports efforts in the United States to improve the national academic dropout rate and increase college accessibility by partnering with established public school systems.  The foundation's parent company is the Simon Property Group.  Although SYF works closely with Simon Property Group, it is not a corporate or grant-making foundation.  SYF is headquartered in Indianapolis, Indiana.  Its current CEO is J. Michael Durnil, Ph.D.

Brookfield Office Properties: Brookfield Office Properties Inc. is a North American commercial real estate company, wholly owned by Brookfield Property Partners.  The company has its headquarters operations in New York, Toronto and Sydney.

Simon Property Group: Simon Property Group, Inc. is an American commercial real estate company in the United States and the largest real estate investment trust (REIT).  It is also the largest shopping mall operator in America.

Northstar Commercial Partners: Northstar Commercial Partners is an American commercial real estate investment company headquartered in Denver, Colorado.  Founded by Brian Watson in 2000, the company acquires distressed commercial real estate or vacant properties and rehabilitates them for lease or use.

Cimls: The Commercial Investment Multiple Listing Service (CIMLS.com) is a private company based in Vancouver, WA.  Its primary business is to provide commercial real estate data.  This includes commercial property listings (for sale and for lease) as well as comparable sale data in the United States.  CIMLS.com was founded 2001 and is now one of the largest data sources in the commercial real estate industry.  As of February 2012 the site has 280,000 registered members, 200,000 listings and $280 billion worth of commercial property listings.  Commercial real estate brokerages that currently list on this site are: Century 21, CBRE, Coldwell Banker, Grubb & Ellis, and Prudential.

Alain Pinel Realtors: Alain Pinel Realtors (APR) is a residential real estate company in California.  The company focuses on luxury real estate in the San Francisco Bay Area.  APR was co-founded in 1990 by Alain Pinel ( original CEO and President), together with Helen Pastorino and Paul L. Hulme (present CEO).  In 2008, Alain Pinel Realtors opened Alain Pinel Investment Group in San Francisco to focus on commercial real estate.

Mack-Cali Realty Corporation: Mack-Cali Realty Corporation is a publicly traded real estate investment trust (REIT) with holdings throughout the Northeast and New Jersey.  The majority of Mack-Cali’s holdings are in commercial real estate including class A office space, although in recent years they have increased investment in multi-family residential properties.  The company provides commercial real estate leasing, management, and development services for their real estate properties.  Its headquarters are located in Jersey City, New Jersey.

Mary Ann Tighe: Mary Ann Tighe is an American commercial real estate broker and CEO of the New York Tri-State Region of CBRE, the world’s largest commercial real estate services firm.  Tighe has made commercial transactions totaling more than 97.5 million square feet and has been cited as a groundbreaker in a traditionally male-dominated industry.  Her deals have anchored more than 14.4 million square feet of new construction in the New York region, a total believed to be a record in commercial brokerage.  Tighe has been named to "Crain’s New York Business" Most Powerful Women in New York since the listing was inaugurated in 2007, ranking #1 in 2011 across all New York City industries.

Question: The non-profit organization, Simon Youth Foundation's parent company is an American commercial real estate company and also the largest what in the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "non_profit_organization_name": {
      "type": "string",
      "description": "The name of the non-profit organization."
    },
    "parent_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the parent company."
        },
        "type": {
          "type": "string",
          "description": "The type of business the parent company operates."
        },
        "largest_categories_in_us": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of categories in which the parent company is the largest in the United States."
        }
      },
      "required": [
        "name",
        "type",
        "largest_categories_in_us"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The specific answer to the question asked."
    }
  },
  "required": [
    "non_profit_organization_name",
    "parent_company",
    "answer"
  ],
  "additionalProperties": false
}
