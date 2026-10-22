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
Honda Motorcycle and Scooter India: Honda Motorcycle and Scooter India, Private Limited (HMSI) is the wholly owned Indian subsidiary of Honda Motor Company, Limited, Japan.  Founded in 1999, it was the fourth Honda automotive venture in India, after Kinetic Honda Motor Ltd (1984-1998), Hero Honda (1984-2011) and Honda Siel Cars India (1995-2012).  HMSI was established in 1999 at Manesar, District Gurgaon, Haryana.

Honda Aircraft Company: The Honda Aircraft Company is a wholly owned subsidiary of the Honda Motor Company that has developed the prototype HondaJet and is slated to manufacture and market the production version of the aircraft.  The company was formed as a separate entity in August 2006 under the leadership of president and CEO Michimasa Fujino.

Mugen Motorsports: Mugen Motorsports (M-TEC Co., Ltd) (無限) is a Japanese company formed in 1973 by Hirotoshi Honda, the son of Honda Motor Company founder Soichiro Honda, and Masao Kimura.  Mugen, meaning "Without Limit", "Unlimited" or "Vast", (hence the commonly placed word "Power" after, denoting "Unlimited Power") is an engine tuner and parts manufacturer that manufactures OEM parts such as body kits and sports exhausts for Honda Motor Company.  Despite the family connections, however, Mugen is not, and has never been, owned by Honda Motor Company; Mugen owner Hirotoshi Honda has been the major shareholder in Honda since his father's death in 1991.

CVCC: CVCC is a trademark by the Honda Motor Company for an engine with reduced automotive emissions, which stood for "Compound Vortex Controlled Combustion".  The first mention of Honda developed CVCC technology was done by Mr. Soichiro Honda February 12, 1971, at the Federation of Economic Organizations Hall in Otemachi, Chiyoda-ku, Tokyo.  Honda's engineers at the time, Mr. Date conferred with Mr. Yagi and Mr. Nakagawa about the possibility of creating lean combustion via a prechamber, which some diesel engines utilized.  The first engine to be installed with the CVCC approach for testing was the single-cylinder, 300 cc Honda EA engine used in the Honda N600 hatchback in January 1970.  This technology allowed Honda's cars to meet Japanese and United States emission standards in the 1970s without a catalytic converter.  A type of stratified charge engine, it first appeared on the 1975 "ED1" engine.  As emission laws advanced and required more stringent admissible levels, Honda abandoned the CVCC method and introduced PGM-FI, or Programmed Fuel Injection on all Honda vehicles.  Some vehicles in Japan had a combination of electronically controlled carburetors, called PGM-Carb on specific, transitional Honda D, E and ZC engines.

Honda advanced technology: Honda Advanced Technology is part of Honda's long-standing research and development program focused on building new models for their automotive products and automotive-related technologies, with many of the advances pertaining to engine technology.  Honda's commitment to pursuit of ideas and exploration of technological challenges has led to practical solutions ranging from fuel-efficient vehicles and engines, to more sophisticated applications such as the humanoid robot, ASIMO, and the Honda HA-420 HondaJet, a six-passenger business jet.

American Honda Motor Company: The American Honda Motor Company, Inc. (sometimes abbreviated as AHM) is a North American subsidiary of the Honda Motor Company, Ltd. It was founded in 1959.  The company combines product sales, service and coordinating functions of Honda in North America, and is responsible for distribution, marketing and sales of Honda and Acura brand automobiles, Honda power sports products, including motorcycles, scooters and all-terrain vehicles, and Honda power equipment products, including lawnmowers, tillers, string trimmers, snow blowers, generators, small displacement general-purpose engines and marine outboard engines.

Honda HA-420 HondaJet: The Honda HA-420 HondaJet is the first aircraft developed by Honda Aircraft Company.  The light business jet was designed in Japan and then developed and manufactured in Greensboro, North Carolina in the United States.

Honda Cars India: Honda Cars India Ltd (HCIL) is a subsidiary of Honda of Japan for the production, marketing and export of passenger cars in India.  Formerly known as Honda Siel Cars India Ltd, it began operations in 1995 as a joint venture between Honda Motor Company and Usha International of Siddharth Shriram Group.  In August, 2012, Honda bought out Usha International's entire 3.16 percent stake for 1.8 billion in the joint venture.  The company officially changed its name to Honda Cars India Ltd (HCIL) and became a 100% subsidiary of Honda.

Honda Aero: Honda Aero, Inc. (HAI), a wholly owned subsidiary of Honda Motor Co., Ltd., is headquartered in Burlington, North Carolina near the Burlington - Alamance Regional Airport.  The Burlington facility will serve as the primary production location for engines developed and marketed by GE Honda Aero Engines, LLC (a joint venture between Honda Aero and GE), beginning with the GE Honda HF120 turbofan engine.  Development of the facility represents a $27 million capital expenditure by Honda, bringing the company's total North American capital investment to more than $9 billion.  Production began with the GE Honda Aero Engine HF120 on March 17, 2015.

Michimasa Fujino: Michimasa Fujino (藤野 道格 , Fujino Michimasa ) is a Japanese engineer and businessman, the founding president and CEO of Honda Aircraft Company, the Honda subsidiary.  At Honda Aircraft, he is responsible for Honda’s overall aircraft business strategy, operation, design, development, certification, marketing, sales and production of the innovative HondaJet.  Since 2015, he has also concurrently served as a managing officer of Honda Motor Co., Ltd.

Question: The Honda Aircraft Company is a wholly owned subsidiary of the Honda Motor Company, the Honda HA-420 HondaJet is the first aircraft developed by Honda Aircraft Company, the light business jet, was designed in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "aircraft_name": {
      "type": "string",
      "description": "The name of the aircraft."
    },
    "developer_company": {
      "type": "string",
      "description": "The company responsible for developing the aircraft."
    },
    "company_ownership_status": {
      "type": "string",
      "description": "The ownership status of the developer company relative to Honda Motor Company."
    },
    "design_country": {
      "type": "string",
      "description": "The country where the aircraft was designed."
    }
  },
  "required": [
    "aircraft_name",
    "developer_company",
    "company_ownership_status",
    "design_country"
  ],
  "additionalProperties": false
}
