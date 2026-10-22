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
Chernihivske: Chernihivske (Ukrainian: Чернігівське , translit.  "Chernigivske’") is a beer brand produced in Ukraine.  It is named after Chernihiv, the location of the first brewery that produced Chernihivske, although the beer is now also produced in the Ukrainian cities of Mykolaiv and Kharkiv.  The company is currently owned by SUN InBev Ukraine, a subsidiary of AB InBev.

Wards Brewing Company: Wards Brewing Company was a brewing company based at Sheaf Brewery on Ecclesall Road, Sheffield, England, now a subsidiary of Double Maxim Beer Company.  The most famous brand produced was Wards Best Bitter.

Heavy Seas Beer: Heavy Seas Beer is brewed by Clipper City Brewing Company, in Baltimore, Maryland.  The brewery was established by Hugh Sisson in 1995.  Previously, Sisson operated Maryland's first brewpub, Sisson's.  In 2010, the brewery rebranded.  While the name of the company remains Clipper City Brewing Company, all of its beer falls under the Heavy Seas brand.  Heavy Seas hosts tours on most weekends.  It is located at 4615 Hollins Ferry Road, Suite B, in the Halethorpe section of Baltimore.  Heavy Seas currently offers a variety of beer styles in approx. 18 states within the United States.  Several Heavy Seas beers have been awarded and include the following: Cutlass Amber Lager (a repeat medal winner at the Great American Beer Festival from 2006-2010, bronze medal winner at the 2010 World Beer Cup and silver medal winner at the 2012 World Beer Cup as Heavy Seas Märzen), Powder Monkey Pale Ale (silver medal winner at the 2008 Great American Beer Festival and bronze medal winner at the 2010 World Beer Cup as Heavy Seas Pale Ale), Small Craft Warning Uber Pils (bronze medal winner at the 2004 Great American Beer Festival), Gold Ale (gold medal winner at the 2010 World Beer Cup, bronze medal winner at the 2010 Great American Beer Festival and bronze medal winner at the 2014 Great American Beer Festival as Heavy Seas Gold Ale) and Winter Storm Imperial ESB (gold medal winner at the 2008 World Beer Cup).

Mahou-San Miguel Group: Mahou San Miguel is a Spanish brewing company, founded in Madrid in 1890 under the name of "Hijos de Casimiro Mahou, fabrica de hielo y cerveza" (The Sons of Casimiro Mahou, production of ice and beer).  Mahou San Miguel is the leading brand in the Spanish beer market.

Taedonggang Brewing Company: The Taedonggang Brewing Company (Taedonggang, Chosongul: 대동강 맥주) is a state-owned North Korean beer brewery company that brews the Taedonggang beer.  The brewery is located in East Pyongyang and has facilities of tens of thousands of square meters.

Por Larrañaga: Por Larrañaga (meaning "by Larrañaga") is the name of a cigar brand produced in Cuba for Habanos SA, the Cuban state-owned tobacco company, as well as a non-Cuban line of cigars produced in the Dominican Republic and Honduras for Altadis, a division of Imperial Tobacco.  Por Larrañaga cigars have been in continuous production in Cuba since 1834, longer than any other Cuban cigar brand.

The Booth Brewing Co.: The Booth Brewing Co. is a microbrewery headquartered in Seoul, South Korea.  Sunghoo Yang, a former investment analyst, Heeyoon Kim, a former Korean medicine doctor, and Daniel Tudor, a journalist for The Economist founded the brewery in 2015, after operating a pizza pub since 2013 [].  They acquired the brewing facility in Eureka, California, previously owned by Lost Coast Brewery, in 2015.  They are well known for Taedonggang Pale Ale, a collaboration beer with Danish microbrewery Mikkeller, and also for being the second foreign craft brewer to produce beer in their own facility in the United States.

Beer in North Korea: North Korea has at least ten major breweries and many microbreweries that supply a wide range of beer products.  The top brand is the light lager Taedonggang which is internationally known for its quality.

Ožujsko: Ožujsko (fully "Ožujsko pivo"; lit.  March Beer), also known and marketed as Žuja, is a Croatian brand of lager beer (5%).  It is the flagship brand produced by Zagrebačka pivovara, the biggest brewery in the country which is a part of Molson Coors Brewing Company since 2013.

Taedonggang: Taedonggang is a brand of North Korean beer brewed by the state-owned Taedonggang Brewing Company based in Pyongyang.  There are four brands of beer marketed as Taedonggang, though the brand known simply as "Taedonggang Beer" is that described below.

Question: Taedonggang beer is the leading brand produced by a state-owned brewery in which Asian city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "beer_brand_name": {
      "type": "string",
      "description": "The name of the beer brand."
    },
    "brewery_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the brewery."
        },
        "ownership_type": {
          "type": "string",
          "description": "The type of ownership of the brewery (e.g., state-owned)."
        },
        "location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the brewery is located."
            },
            "country": {
              "type": "string",
              "description": "The country where the brewery is located."
            },
            "continent": {
              "type": "string",
              "description": "The continent where the brewery is located."
            }
          },
          "required": [
            "city",
            "country",
            "continent"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "ownership_type",
        "location"
      ],
      "additionalProperties": false
    },
    "is_leading_brand_in_country": {
      "type": "boolean",
      "description": "Indicates if the beer brand is the leading brand in its country."
    }
  },
  "required": [
    "beer_brand_name",
    "brewery_details",
    "is_leading_brand_in_country"
  ],
  "additionalProperties": false
}
