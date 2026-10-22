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
Jenni Byrne: Jenni Byrne was a political advisor for the Conservative Party of Canada and former Prime Minister Stephen Harper.  She was once referred to as "the most powerful woman in Ottawa" and "the other woman" behind Prime Minister Stephen Harper.

Premiership of Stephen Harper: Stephen Harper's tenure as Prime Minister began on February 6, 2006 when Harper and his first cabinet were sworn in by Governor General Michaelle Jean.  Harper was invited to form the 28th Canadian Ministry and become Prime Minister of Canada following the 2006 election where Harper's Conservative Party of Canada won a plurality of seats in the Canadian House of Commons leading to the resignation of Liberal prime minister Paul Martin.  In the 2011 federal election, Harper won his first majority government.

Premiership of Justin Trudeau: Justin Trudeau's tenure as prime minister began on November 4, 2015, when the first Cabinet headed by him was sworn in by Governor General David Johnston.  Trudeau was invited to form the 29th Canadian Ministry and become Prime Minister of Canada following the 2015 election, where Trudeau's Liberal Party won a majority of the seats in the Canadian House of Commons, leading to the resignation of Conservative Prime Minister Stephen Harper.

Canadian Tire: Canadian Tire Corporation, Limited is a Canadian retail company which sells a wide range of automotive, sports and leisure, and home products.  Some stores also sell toys and food products.  Retail operations include: Canadian Tire, the core retail and automotive service operation, which operates a large car repair garage in each store; Canadian Tire Petroleum; Mark's, a men’s, women’s, and work apparel retailer; sporting goods and sportswear retail conglomerate FGL Sports; and PartSource, which retails auto parts and accessories.  The company's head office is in Toronto, Ontario.  The retailer is known for its Canadian Tire money, a loyalty program first introduced in 1958, where customers are provided with coupons resembling paper money worth 0.4% of their purchase that can be used in subsequent purchases as scrip at Canadian Tire stores and gas stations, and some merchants in flea markets.

Peter MacKay: Peter Gordon MacKay {'1': ", '2': ", '3': ", '4': "} (born September 27, 1965) is a lawyer and politician from Nova Scotia, Canada.  He was a Member of Parliament from 1997 to 2015 and has served as Minister of Justice and Attorney General (2013–2015), Minister of National Defence (2007–2013), and Minister of Foreign Affairs (2006–2007) in the Cabinet of Canada under Prime Minister Stephen Harper.  MacKay was the final leader of the Progressive Conservative Party of Canada (PC Party), and he agreed to merge the party with Stephen Harper's Canadian Alliance in 2003, forming the Conservative Party of Canada.

Canadian Tire money: Canadian Tire money, officially Canadian Tire 'money', (CTM) is a loyalty program operated by the Canadian retail chain Canadian Tire.  It consists of coupons, issued by the company, which resembles real banknotes.  It can be used as scrip in Canadian Tire stores, but is not considered a private currency.  The notes are printed on paper similar to what Canadian currency was printed on when they were printed on real paper, and were jointly produced by two of the country’s long-established security printers, British American Banknote Company (BABN) and Canadian Bank Note Company (CBN).  Some privately owned businesses in Canada accept CTM as payment (see history below), since the owners of many such businesses shop at Canadian Tire.  In Canadian Tire stores, CTM is accepted for Canadian money at par.

Dimitri Soudas: Dimitri Soudas (born July 10, 1979) is the former Director of Communications to the Canadian Prime Minister Stephen Harper, former Executive Director of the Canadian Olympic Committee and former Executive Director of the Conservative Party of Canada.  He is currently the Managing Partner of Stampede Group, Senior Advisor to the President of Cavalia and is a member of two Boards of Directors.

Josée Verner: Josée Verner, PC (born December 30, 1959) is a Canadian politician.  She represented the electoral district of Louis-Saint-Laurent in the Canadian House of Commons from 2006 to 2011 as a member of the Conservative Party of Canada.  She also served as a minister in the Cabinet of Prime Minister Stephen Harper serving as Minister of Intergovernmental Affairs, President of the Queen’s Privy Council for Canada and Minister for La Francophonie.  On May 18, 2011, it was announced that she would be appointed to the Canadian Senate following the loss of her seat in the 2011 federal election, and she was she formally appointed on June 13, 2011.

Sandra Buckler: Sandra Buckler is a former director of communications for the Office of the Prime Minister of Canada under Conservative Party of Canada Prime Minister Stephen Harper.  She was appointed in 2006 and resigned from her position on June 26, 2008.  Her tenure was contentious, including charges from the national media that she was overly restricted in sharing information, pressing journalists to instead focus on photo ops and adhering rigorously to talking points from the Office of the Prime Minister (PMO), as well as accusations from Members of Parliament that she had bullied them, and charges of conflict of interest.  She joined Canadian Tire as Vice President of communications in 2015.

Gary Lunn: Gary Vincent Lunn, (born May 8, 1957 in Trail, British Columbia) is a former Canadian Member of Parliament for the British Columbia riding of Saanich—Gulf Islands.  He served in the House of Commons from 1997 to 2011, first as a member of the Reform Party of Canada and subsequently as a member of the Canadian Alliance and the Conservative Party of Canada.  He was Minister of State (Sport) in the Cabinet of Prime Minister Stephen Harper and Official Opposition Critic for Métis and Non-Status Indians, Minister of State for Northern Development, and Critic of the Secretary of State for Human Resources Development.  Lunn lost his seat in the 2011 federal election in Canada in an upset to the Leader of the Green Party, Elizabeth May.

Question: Sandra Buckler is a former director of communications for the Office of the Prime Minister of Canada under Conservative Party of Canada Prime Minister Stephen Harper, she joined Canadian Tire Corporation, Limited, a Canadian retail company which sells a wide range of automotive, sports and leisure, and home products, as Vice President of communications in which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the company the person joined."
    },
    "company_description": {
      "type": "string",
      "description": "A brief description of the company."
    },
    "role_at_company": {
      "type": "string",
      "description": "The role the person took at the company."
    },
    "year_joined": {
      "type": "integer",
      "description": "The year the person joined the company."
    }
  },
  "required": [
    "person_name",
    "company_name",
    "company_description",
    "role_at_company",
    "year_joined"
  ],
  "additionalProperties": false
}
