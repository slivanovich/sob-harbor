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
R. E. Hoy No. 1 Oil Well: The R.E. Hoy No. 1 Oil Well was constructed by the Sinclair Oil & Refining Corporation in September 1916.  It has been listed on the National Register of Historic Places since 1986.  Milton C. Garber and his brother Bert Garber hired geologist Dorsey Hager to determine potential drilling locations on their properties.  The Garber brothers contracted Harry F. Sinclair to construct a well on R. E. Hoy's farm (NE corner, Section 25, T22N, R4W,

Power Rangers S.P.D.: Power Rangers S.P.D. is an American television series and the thirteenth season of the "Power Rangers" franchise, based on the Super Sentai series, "Tokusou Sentai Dekaranger".  It debuted on February 5, 2005, on ABC Family.  New episodes continued to debut on ABC Family until the episode "Messenger, Part 1".  Starting with "Messenger, Part 2" episodes began to debut on Toon Disney.  It is also the title for the Korean dub of "Dekaranger" in South Korea, whose logo is similar to the American series.  S.P.D. stands for "Space Patrol Delta"; in "Dekaranger", it stood for "Special Police Dekaranger", and in the South Korean dub of "Dekaranger", it stood for "Special Police Delta".  A Japanese dub of "S.P.D." started airing on Toei's digital television channel in Japan starting in August 2011, with two DVD volumes released on August 5.  It features the original "Dekaranger" cast members dubbing over the voices of their American counterparts (with the exception of Mako Ishino, who is the series' narrator rather than voicing her character's counterpart).

Donghae-1 gas field: Donghae-1 gas field is a natural gas field located offshore in the Sea of Japan (East Sea).  It was discovered in 1997 and developed by Korea National Oil Corporation.  The natural gas field is operated and owned by Korea National Oil Corporation.  The total proven reserves of the Donghae-1 gas field are around 250 billion cubic feet (7.1×10m³), and production is centered on 50 million cubic feet/day (1.4×10m³).

Robert Holding: Robert Earl Holding (November 29, 1926 – April 19, 2013) was an American businessman who owned Sinclair Oil Corporation, the Little America Hotels, the Grand America Hotel, the Westgate Hotel in San Diego, California (directed by Georg Hochfilzer), and two ski resorts, Sun Valley in central Idaho since 1977, and Snowbasin near Ogden, Utah, since 1984.

ARCO: Atlantic Richfield Company (ARCO) is an American oil company with operations in the United States, Indonesia, the North Sea, and the South China Sea.  It has more than 1,300 gas stations in the western part of the United States.  ARCO was formed by the merger of East Coast–based Atlantic Refining and California-based Richfield Oil Corporation in 1966.  A merger in 1969 brought in Sinclair Oil Corporation.  It became a subsidiary of UK-based BP plc in 2000 through its BP West Coast Products LLC (BPWCP) affiliate.  On August 13, 2012, it was announced that Tesoro would purchase ARCO and its refinery for $2.5 billion.  However, the deal came under fire due to increasing fuel prices.  Many activists urged state and federal regulators to block the sale due to concerns that it would reduce competition and could lead to higher fuel prices at ARCO stations (ARCO stations make up more than half of all stations with the lowest fuel prices in California).  On June 3, 2013, BP sold ARCO and the Carson Refinery to Tesoro for $2.5 billion.  BP sold its Southern California terminals (Vinvale, Colton, San Diego, Hathaway, and Hynes) to Tesoro Logistics LP, including the Carson Storage Facility.  BP will continue to own the ampm brand and sell it to Tesoro for Southern California, Arizona, and Nevada.  BP exclusively licensed the ARCO rights from Tesoro for Northern California, Oregon, and Washington.

Little America, Wyoming: Little America is a census-designated place (CDP) in Sweetwater County, Wyoming, United States.  The population was 68 at the 2010 census.  The community got its name from the Little America motel, which was purposefully located in a remote location as a haven, not unlike the base camp the polar explorer Richard E. Byrd set up in the Antarctic in 1928.  However, being situated on a coast-to-coast highway and offering travel services, it thrived, launching a chain of travel facilities by the same name.  Its developer, Robert Earl Holding, died on April 19, 2013, with a personal net worth of over $3 billion.

Canadian petroleum companies: Although there are numerous oil companies operating in Canada, the majority of production, refining and marketing is done by fewer than 20 of them.  According to the 2013 edition of Forbes Global 2000, canoils.com and any other list that emphasizes market capitalization and revenue when sizing up companies, as of March 31, 2014 these are the largest Canada-based oil and gas companies (they are either based entirely in Canada or majority Canadian owned).  However more recent changes, possibly mergers or a stronger showing in the price of oil could mean a few of the oil sands producers are underrepresented; this is because Canadian companies are increasingly dependent on production from that source, which is hurt severely when oil prices decline below 50 to 60 dollars a barrel since costs per barrel traditionally exceed $28 and non-upgraded bitumen (<10 API) produces 1.7 fewer barrels per metric ton than West Texas Intermediate oil (according to calculation).  A few of the larger companies (Penn West Petroleum and Athabasca Oil Corporation) don't show up in the Forbes list because its ranking system takes many different factors into account.

Robert Earl (singer): Robert Earl (born Monty Leigh, 17 November 1926) was an English singer of traditional pop music in the United Kingdom in the 1950s and 1960s, whose style was operatic, like fellow crooners David Whitfield, David Hughes and Edmund Hockridge.  He is the father of the businessman Robert Earl.

Sinclair Oil Corporation: Sinclair Oil Corporation is an American petroleum corporation, founded by Harry F. Sinclair on May 1, 1916, as the Sinclair Oil and Refining Corporation by combining the assets of 11 small petroleum companies.  Originally a New York corporation, Sinclair Oil reincorporated in Wyoming in 1976.  The corporation's logo features the silhouette of a large green dinosaur.

Arystan oil field: Arystan Oil Field is an oil field located in Mangystau Province, Kazakhstan.  It was discovered in 2008 and developed by Korea National Oil Corporation.  The oil field is operated and owned by Korea National Oil Corporation.  The total proven reserves of the Arystan oil field are around 57.8 million barrels (7.89×10tonnes), and production is centered on 1480 oilbbl/d .

Question: Robert Earl Holding was an American businessman who owned Sinclair Oil Corporation whose logo features the silhouette of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "owner_name": {
      "type": "string",
      "description": "The name of the businessman who owned the company."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the oil corporation."
    },
    "logo_description": {
      "type": "string",
      "description": "A full description of the company's logo."
    },
    "logo_animal": {
      "type": "string",
      "description": "The type of animal featured in the logo."
    },
    "logo_color": {
      "type": "string",
      "description": "The color of the animal in the logo."
    }
  },
  "required": [
    "owner_name",
    "company_name",
    "logo_description",
    "logo_animal",
    "logo_color"
  ],
  "additionalProperties": false
}
