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
Nidec ASI: Nidec ASI is an Italian multinational company based in Milan, that designs and manufactures rotating electrical machines, Power electronics and industrial automation.  It was founded in 2013 with the acquisition of Ansaldo Sistemi Industriali by Nidec Corporation.  Working in electrical engineering, designs and manufactures of electric motors and generators, power electronics and control systems and automation for industrial applications, Nidec ASI was founded in 2012 when Nidec, a Japanese multinational corporation listed on the and , NJ and ON TOPIX 100 Component and Nikkei, acquired Ansaldo Sistemi Industriali (ASI).  ASI, an industrial branch of the Ansaldo Group, was privatized in 2000.  Its markets include petrochemical, energy, steel, marine and industrial automation.

PZL-Świdnik: PZL Świdnik S.A ("Wytwórnia Sprzętu Komunikacyjnego PZL-Świdnik S.A.") is the biggest helicopter manufacturer in Poland.  Its main products are PZL W-3 Sokół and PZL SW-4 Puszczyk helicopters.  In early 2010 the factory was acquired by AgustaWestland (since 2015 became part of Leonardo-Finmeccanica’s Helicopter Division).

AgustaWestland: AgustaWestland S.p.A was an Italian helicopter design and manufacturing company and wholly owned subsidiary of Finmeccanica S.p.a., (now called Leonardo).  It was formed in July 2000 as an Anglo-Italian multinational company, when Finmeccanica and GKN merged their respective helicopter subsidiaries (Agusta and Westland Helicopters) to form AgustaWestland, with each holding a 50% share.  Finmeccanica acquired GKN's stake in AgustaWestland in 2004.  From 1 January 2016, the activities of AgustaWestland were merged into Leonardo-Finmeccanica's Helicopter Sector.

Bristlecone (company): Bristlecone is a supply chain consulting and system Integration multinational company, founded in 1996, with its headquarters situated at San Jose, California.  The company is a part of $16.9 billion multinational Mahindra Group.  They have completed more than 300 engagements across 20 different industry verticals till now.  The company is ranked among the top 10 supply chain system integrators of 2012 in Gartner's Supply Chain System Integrators survey.

Pari Networks: Pari Networks was an America-based multinational company based in Milpitas, California.  It was a provider of network configuration and change management (NCCM) and compliance management solutions.  It was acquired by Cisco Systems and its employees will be integrated into Cisco's Network Services Unit.

Redox Brands: Redox Brands was a marketing company formed in 2000 by Todd Wichmann and Richard Owen, former executives with the multinational consumer products firm Procter & Gamble (P&G).  The company's first product was Oxydol brand purchased from P&G.  P&G would continue manufacturing Oxydol and provide back office support.  Redox had won out over private label companies in the purchase of Oxydol.  Biz was purchased in an auction from P&G in the Summer of 2000.  Forbes estimated that Oxydol was sold for $7 million and Biz for greater than $40 million.  In one year, Oxydol sales were 800% greater than when acquired.

SunGard: SunGard was an American multinational company based in Wayne, Pennsylvania, which provided software and services to education, financial services, and public sector organizations.  It was formed in 1983, as a spin-off of the computer services division of Sun Oil Company.  The name of the company originally was an acronym which stood for Sun Guaranteed Access to Recovered Data, a reference to the disaster recovery business it helped pioneer.  SunGard was ranked at 480th in the U.S. Fortune 500 list in the year 2012.

Italcementi: Italcementi is an Italian multinational company, quoted on the Borsa Italiana, which produces cement, ready-mix concrete and construction aggregates.  In 2015, 45% of Italcementi was acquired by HeidelbergCement, together forming the world's second largest cement producer.

Premier Cruises: Premier Cruises was a cruise line holding company formed in the early 1990s that focused on the family cruise market as well as on developing cruise operations in new geographic markets.  The company's business focus was to acquire older cruise vessels, refurbish these vessels in order to offer "traditional cruise experiences", operate the vessels in geographic areas, such as Europe and south/Central America, which the major operators such as Carnival Cruise Line, Norwegian Cruise Line and Royal Caribbean International were not focusing at the time, and to market their cruises largely to European and South American customers through strategic marketing partnerships with some of the major tour and travel groups in the world such as Thomson Holidays in the U.K, TUI in Germany, Fritidsresor in Scandinavia, Alpitour in Italy and Pullmantur in Spain (subsequently acquired by Royal Caribbean International for $800 million,) as well as through more than a dozen operators in south / Central America such as CVC in Brazil (which was acquired by the Carlyle Group [63.6%] in January 2010 for $250 million).  The company was operating out of its main offices in Cape Canaveral and Miami, Florida.

Outsource Partners International: Outsource Partners International (OPI) was acquired by EXL in June 2011.  The acquisition marked the end of F&A outsourcing of OPI.  OPI was a multinational company with headquarters in New York, NY and Los Angeles, CA.  It operates from more than a dozen global locations throughout the US, UK, India, Bulgaria, and Malaysia.  OPI was formed in 2002 through the acquisition of big four accounting firm's Business Process Outsourcing (BPO) division and itAccounts, a finance and accounting BPO company with an offshore F&A outsourcing facility in Bangalore, India.  It offers finance, accounting and tax outsourcing services.

Question: In early 2010 PZL-Świdnik was acquired by a multinational company formed in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "acquired_company_name": {
      "type": "string",
      "description": "The name of the company that was acquired."
    },
    "acquiring_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the multinational company that performed the acquisition."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the acquiring company was formed."
        },
        "acquisition_year": {
          "type": "integer",
          "description": "The year the acquisition took place."
        }
      },
      "required": [
        "name",
        "founding_year",
        "acquisition_year"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "integer",
      "description": "The founding year of the acquiring company."
    }
  },
  "required": [
    "acquired_company_name",
    "acquiring_company",
    "final_answer"
  ],
  "additionalProperties": false
}
