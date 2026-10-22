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
Kenya Television Network: Kenya Television Network (KTN) is one of the leading television stations in Kenya with its headquarters located along Mombasa Road Nairobi, at the Standard Group Centre Nairobi.  It was founded in March 1990 by Jared Kangwana and was the first non-pay privately owned TV-station in Africa, and the first to break KBC's monopoly in Kenya.  KTN became famous for Activism Journalism in the 1990s, developing a sophisticated, aggressive and unique style news coverage, and has continued with the same hard line stance, issues-based reporting to date, branding itself as the 'authoritative and independent' news channel.  KTN became the model for some governments in Africa when they allowed media liberalisation to take place in the late 1990s.  Many of the new radio and TV stations across East and Central Africa not only relied on KTN as a model, but benefited directly in terms of recruiting former KTN staff to run their operations.

Gamania: Gamania Digital Entertainment Co., Ltd. (Gamania) is a PC online game and digital entertainment corporation with its headquarters located in New Taipei, Taiwan.  It was the first Taiwanese online game brand to expand globally, with overseas branch offices publishing and developing digital entertainment contents in Tokyo, Seoul, Shanghai, Beijing, and Hong Kong.  It was also looking to set up branch offices in North America and Europe in 2010.

Cuppy's Coffee: Cuppy's Coffee is a specialty coffee and smoothie franchise company with its headquarters located in Greenville, South Carolina.  The company is under new ownership and management.  Cuppy's Coffee & More, Inc. was a privately owned specialty coffee franchise.  The firm marketed franchise opportunities on its website and describes a comprehensive, 10-day training program for its franchisees (6 days at its headquarters, 4 days onsite).  The firm employed approximately 145 employees at its corporate headquarters in Fort Walton Beach, Florida before moving to Altoona, PA in September, 2008.  Cuppy's, along with Java Jo'z national chain folded in 2009.  However, former franchisees still continue to use the name in their shops.

Gerald D. Hines: Gerald D. Hines (born 1925) is the founder and chairman of Hines, a privately held real estate firm with its U.S. headquarters located in Houston, Texas, and its European headquarters located in London.  As of 2016, Gerald Hines' net worth equaled USD $1.3 billion.

1st Infantry Division (Romania): The 1st Infantry Division Dacica was one of the major units of the Romanian Land Forces, with its headquarters located in Bucharest.  It was the heraldic successor of the Romanian First Army.  On 31 August 2015, 1st Infantry Division headquarters disbanded, to become, three months later, the Headquarters Multinational Division Southeast of NATO's Allied Joint Force Command Naples.

Hoffmann-La Roche: F. Hoffmann-La Roche AG is a Swiss multinational healthcare company that operates worldwide under two divisions: Pharmaceuticals and Diagnostics.  Its holding company, Roche Holding AG, has bearer shares listed on the SIX Swiss Exchange.  The company headquarters are located in Basel.

Fruehauf Trailer Corporation: Fruehauf Trailer Corporation, previously Fruehauf Trailer Company (1918–1963) and Fruehauf Corporation (1963–1989), was an American company engaged in the manufacture and sale of truck trailers, and other machinery and equipment, with headquarters located in Detroit, Michigan.  It was founded in 1918 in Detroit, after August Fruehauf created the semi-trailer and launched a new industry.  The Fruehauf trailer company introduced revolutionary inventions to trucking and transportation with hydraulic dump trailers, bulk tanker trailers, and automatic fifth wheel coupling among their over one thousand patents, including the shipping container in 1956.  Expanding across the country, Fruehauf had 16 plants and over 80 distributorships for parts and service.  Globally, the company expanded into Europe, South America and Asia.  Following a proxy battle in the late 1980s the company filed for bankrupt protection in 1997.  International divisions became independent, U.S. subsidiaries like Kelsey Hayes, Pro-Par, Budd Wheels and Hobbs were sold; Wabash National acquired the crippled company in 1997.

Ipatasertib: Ipatasertib (RG7440) is an experimental cancer drug in development by Roche.  It is a small molecule inhibitor of Akt.  It was discovered by Array Biopharma and is currently in phase II trials for treatment of breast cancer.

Transportistas Unidos Mexicanos: Transportistas Unidos Mexicanos otherwise known as TUM or TUM Transportistas, is a Mexican Trucking Company based out of Mexico City founded in 1938.  TUM operates 18 terminals all over Mexico, with its corporate headquarters located in Mexico City Mexico, and its international headquarters located across from the U.S.' busiest port of entry in Nuevo Laredo, Tamaulipas.  TUM carries a fleet of over 1,800 Trucks, 2,500 trailers, and 1,800 drivers making it the largest trucking company in Mexico.

Stratolaunch Systems: Stratolaunch Systems Corporation is a space transportation venture developing a new air launch to orbit system, with its corporate headquarters located in Seattle, Washington.  The project was officially announced in December 2011 by Microsoft co-founder Paul G. Allen and Scaled Composites founder Burt Rutan, who had previously collaborated on the creation of SpaceShipOne.

Question: Where is the company that is developing Ipatasertib headquarters located?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company developing the drug."
    },
    "drug_name": {
      "type": "string",
      "description": "The name of the drug being developed."
    },
    "headquarters_location": {
      "type": "string",
      "description": "The city where the company's headquarters is located."
    },
    "country": {
      "type": "string",
      "description": "The country where the company's headquarters is located."
    },
    "development_status": {
      "type": "string",
      "description": "The current development status of the drug."
    }
  },
  "required": [
    "company_name",
    "drug_name",
    "headquarters_location",
    "country",
    "development_status"
  ],
  "additionalProperties": false
}
