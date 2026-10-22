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
The Left Shoe Company: The Left Shoe Company, previously Left Foot Company, is a made-to-measure male footwear manufacturer with offices in London, Los Angeles and in Helsinki.  The company was founded in 1998 as The Left Foot Company.  It was renamed and rebranded The Left Shoe Company in the fall of 2010.

Air Vegas: Air Vegas (IATA: 6V, ICAO: VGA, Call sign: Air Vegas) was an airline with its headquarters on the grounds of the North Las Vegas Air Terminal in North Las Vegas, Nevada.  It operated daily sightseeing flights from Las Vegas to the Grand Canyon.  Prior to moving to the North Las Vegas Airport its main bases were McCarran International Airport (LAS), Las Vegas and Henderson Executive Airport (HND), Las Vegas.

Las Vegas–Paradise, NV MSA: The Las Vegas–Paradise, NV MSA, also known as the Las Vegas–Henderson–Paradise, NV Metropolitan Statistical Area (2013), is in the southern part of the U.S. state of Nevada, coextensive since 2003 with Clark County, Nevada.  A central part of the metropolitan area is the Las Vegas Valley, a 600 sqmi basin that includes the metropolitan area's largest city, Las Vegas as well as the other primary city, Paradise, Nevada.  The area contains the largest concentration of people in the state.  Cities in the metropolitan area include Las Vegas, Henderson, North Las Vegas, and Boulder City.  The metropolitan area is one of the top tourist destinations in the world, drawing over 40 million international and domestic visitors in 2013 with a GMP of US$103.3 billion.

Zappos: Zappos.com is an online shoe and clothing shop based in Las Vegas, Nevada.

Las Vegas Weekly: Las Vegas Weekly is a free alternative weekly newspaper based in Henderson, Nevada, covering Las Vegas arts, entertainment, culture and news.  "Las Vegas Weekly" is published by Greenspun Media Group.  The paper was founded in 1992 by James P. Reza, Greg Ryan and Robert Ringle as a free monthly publication called "Scope Magazine" covering Southern Nevada's culture, arts, music and lifestyle from a decidedly Generation X perspective .  "Scope" published its first issue in April 1992.  In 1996, Reza partnered with Daniel Greenspun, forming a new company (Radiant City Publications LLC) to publish "Scope".  During this partnership, Reza continued on as Managing Editor, broadening the coverage to a more traditional alternative newsweekly style, and accelerated the publishing schedule to biweekly.  In 1998, Reza sold his remaining interest in "Scope" to The Greenspun Corporation, who retooled it and renamed it "Las Vegas Weekly".  As of December 2009, "Las Vegas Weekly" had a circulation of 65,000.

Nap pods: Nap pods are special chairs, often used in corporate/workplace environments and universities, that allow people to nap.  They are available at JFK airport, Google, and Zappos.  Washington State University also offers some.

Brown Shoe Company's Homes-Take Factory: Brown Shoe Company's Homes-Take Factory, also known as the International Hat Company Warehouse, is a historic building location at 1201 Russell Boulevard in the Soulard neighborhood of St. Louis, Missouri.  Built in 1904, by renowned architect Albert B. Groves, the building was originally a factory for the Brown Shoe Company, based in St. Louis.  In 1954, the factory was subsequently converted into a warehouse by the International Hat Company.  The site has been recognized as a testament to Grove's architectural expertise in the principles of factory design, namely technical advances in layout planning, operational efficiency, and employee safety.  Additionally, the factory epitomizes the early 20th century cultural transformation and socio-industrial development of St. Louis into a manufacturing powerhouse.  In particular, the Brown Shoe Company is recognized as a principal player in challenging the 19th century dominance of the New England shoe industry.  This significantly contributed to the early 20th century sobriquet of St. Louis as the city of "shoes, booze, and blues."  The Brown Shoe Company's Homes-Take factory is considered to be among the pioneering industrial facilities of this historic transformation.

Bacup Shoe Company: The Bacup Shoe Company is a footwear company based in the village of Stacksteads, near Bacup, Lancashire, England.  The Bacup Shoe Co. was founded and incorporated in 1928 by Ernst Goodwin.  The Bacup Shoe company was one of the last well known footwear manufacturers to stop manufacturing in the late 1990s and turn to importing footwear from the Far East.  Suppliers are based in China (where the company is also based), Vietnam and Spain.

Las Vegas Valley: The Las Vegas Valley is a major metropolitan area located in the southern part of the U.S. state of Nevada.  The largest urban agglomeration in the state, it is the heart of the Las Vegas–Paradise-Henderson, NV MSA.  The Valley is largely defined by the Las Vegas Valley landform, a 600 sqmi basin area surrounded by mountains to the north, south, east and west of the metropolitan area.  The Valley is home to the three largest incorporated cities in Nevada: Las Vegas, Henderson and North Las Vegas.  Five unincorporated towns governed by the Clark County government are part of the Las Vegas Township and constitute the largest community in the state of Nevada.

Las Vegas Uncork'd: Las Vegas Uncork'd (also referred to as Vegas Uncork'd and Vegas Uncorked) is an annual culinary and wine event in Las Vegas, Nevada.  The concept was developed by the Las Vegas Convention and Visitors Authority, their advertising agency R&R Partners and Las Vegas resort partners who originally considered a number of magazine partners such as Bon Appetit, Food & Wine and Gourmet.  Bon Appetit was selected as the magazine partner after a review with each magazine.  The event was launched in 2007 by the Las Vegas Convention and Visitors Authority, "Bon Appétit" magazine led by Editor-in-Chief Barbara Fairchild and co-creator and Executive Director Rob O'Keefe who led the first five years of development of what Eater.com called "the world's most innovative culinary event".  Las Vegas resort partners over the years include Bellagio, Caesars Palace and Wynn Las Vegas, MGM Grand, Mandalay Bay, The Venetian, Las Vegas and The Palazzo and each year the event features more than 80 celebrated chefs and over 25 events occurring over a spectacular four-day weekend.

Question: What shoe company based in Las Vegas, Nevada has nap pods in their offices?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the shoe company."
    },
    "location": {
      "type": "string",
      "description": "The city and state where the company is based."
    },
    "has_nap_pods": {
      "type": "boolean",
      "description": "Indicates whether the company has nap pods in its offices."
    }
  },
  "required": [
    "company_name",
    "location",
    "has_nap_pods"
  ],
  "additionalProperties": false
}
