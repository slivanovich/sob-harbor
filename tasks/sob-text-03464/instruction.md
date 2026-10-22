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
Tiger Airways Holdings: Tiger Airways Holdings Limited () is a Singapore-based holding company for a group of low-cost carriers operating in the Asia-Pacific region, consisting of its flagship airline and wholly owned subsidiary, Tigerair (Tiger Airways Singapore).  The holding company was formed in 2007 to allow for easier management of the airline subsidiaries, as well as any future expansion, without having to focus on operational issues, leaving those to the airlines themselves.

Republic Airways Holdings: Republic Airways Holdings, Inc. is an American airline holding corporation based in Indianapolis, Indiana, that owns Republic Airline, an American regional airline operating in the United States.

Mesa Air Group: Mesa Air Group, Inc. is a Nevada Corporation commercial aviation holding company with headquarters in Suite 700 at 410 North 44th Street in the Camelback East area of Phoenix, Arizona, United States.  The company operates one regional airline subsidiary: Mesa Airlines which operates as American Eagle, US Airways Express and United Express under contractual agreements with American Airlines and United Airlines respectively.

Republic Airline: Republic Airline Inc., operating as Republic Airline, is a regional airline subsidiary of Republic Airways Holdings that operates service as American Eagle, Delta Connection, and United Express using a fleet of Embraer 170 and Embraer 175 regional jets.  It is headquartered in Indianapolis, Indiana.  Its call sign "Brickyard" is derived from the nickname of the Indianapolis Motor Speedway.

Midwest Airlines: Midwest Airlines (formerly Midwest Express) was a U.S.-based airline and, for a short time, an operating brand of Republic Airways Holdings based in Oak Creek, Wisconsin, operating from Milwaukee's General Mitchell International Airport.  On April 13, 2010, parent company Republic announced that Midwest Airlines and Frontier Airlines would merge, with the Midwest brand disappearing in late 2011.

Tigerair: Tiger Airways Singapore Pte Ltd, operating as Tigerair, was a budget airline headquartered in Singapore.  It operated services to regional destinations in Southeast Asia, Bangladesh, China and India from its main base at Singapore Changi Airport.  It was founded as an independent airline in 2003, and was listed on the Singapore Stock Exchange under the Tiger Airways Holdings name in 2010.  In October 2014, parent company Tiger Airways Holdings became a subsidiary of the SIA Group, who took a 56% ownership stake.

Regional Airline Association: The Regional Airline Association (RAA) is a business association founded in 1975 that represents 31 North American regional airlines and 280 associate, non-airline members.  This includes manufacturers of products and services supporting the regional airline industry.  The RAA is the collective bargaining voice for its members' interests and lobbies on their behalf before the United States Congress, Department of Transportation, Federal Aviation Administration and other federal agencies.  The RAA represents the financial and economic interests of regional airline employers and regional airline support industry employers.  The Regional Airline Association does not represent financial or economic interest of airline employees, either union or other.  The RAA is headquartered in Washington DC.

William Roshko Holdings Company: William Roshko Holdings Company is a U.S. holding company with headquarters in Beach Haven, New Jersey for real estate properties owned by the Roshko family through a private, family-owned real estate investment trust.  William Roshko Holdings Company is the largest personal holding company for real estate acquisitions and development in the northeast United States.  It has been favorably reviewed following the real estate collapse of 2008 as being bullish with a prudential investment mentality, and named one of "America's Most Admired Companies" by Wall Street professionals.  In the 2012 report to the Congressional House Committee on Financial Services by the office of U.S. Treasury Secretary Timothy Geithner, the Treasury reported it had implemented increased supervision over banks and non-banks following the collapse, and specifically noted William Roshko Holdings Company as a "key market infrastructure investor" which voluntarily accepted enhanced government risk management standards.

Chautauqua Airlines: Chautauqua Airlines, Inc., was an American regional airline and a subsidiary of Republic Airways Holdings based in Indianapolis, Indiana, United States.  Prior to the shut down of operations, it operated scheduled passenger services to 52 airports in the United States and Canada via code sharing agreements as the Delta Connection for Delta Air Lines and AmericanConnection for American Airlines.  Chautauqua previously flew feeder services for other airlines as well via code sharing agreements.  Its last day in operation was December 31, 2014, at which time all flying was absorbed by the Shuttle America certificate.

Timothy E. Hoeksema: Timothy E. Hoeksema (born January 25, 1947) was the chairman of Midwest Air Group who transformed the air fleet of the Kimberly Clark paper mill company into Midwest Airlines.  He retired in July 2009 after the company was sold to Republic Airways Holdings after running into financial trouble.

Question: The Republic Airways Holdings company is based in the same location as which of its regional airline subsidiary's headquarters?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "parent_company_name": {
      "type": "string",
      "description": "The name of the parent holding company."
    },
    "parent_company_headquarters": {
      "type": "string",
      "description": "The headquarters location of the parent company."
    },
    "subsidiaries_with_matching_headquarters": {
      "type": "array",
      "description": "A list of regional airline subsidiaries that share the same headquarters location as the parent company.",
      "items": {
        "type": "object",
        "properties": {
          "subsidiary_name": {
            "type": "string",
            "description": "The name of the subsidiary airline."
          },
          "subsidiary_headquarters": {
            "type": "string",
            "description": "The headquarters location of the subsidiary airline."
          }
        },
        "required": [
          "subsidiary_name",
          "subsidiary_headquarters"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "parent_company_name",
    "parent_company_headquarters",
    "subsidiaries_with_matching_headquarters"
  ],
  "additionalProperties": false
}
