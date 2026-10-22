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
Deering Oaks: Deering Oaks is a 55 acre public park in Portland, Maine, which has a baseball diamond, tennis courts, a playground, and a pond.  It is located west of downtown Portland and is bordered by Deering Avenue on the west, Forest Avenue on the east, Park Avenue to the south and Interstate 295 to the north.  State Street bisects the park.  Access is from State Street, Deering Avenue, or Park Avenue.  The Portland Farmers Market is located on the Park Avenue side of the park.  The park is listed on the National Register of Historic Places.

Richard McCarthy (activist): Richard McCarthy is the co-founder of the Crescent City Farmers Market and the executive director of Slow Food USA.  He was the founder of Market Umbrella and the Farmers Market Coalition.  In 2012, he was named a "Hero of the New South" by Southern Living magazine.  He is a graduate of the London School of Economics.

Travel + Leisure: Travel + Leisure is a travel magazine based in New York City, New York.  Published 12 times a year, it has 4.8 million readers, according to its corporate media kit.  It is owned and published by Time Inc. Its main competitors are "Condé Nast Traveler" and "National Geographic Traveler".

Farmers Market Promotion Program: The Farmers Market Promotion Program is a United States Department of Agriculture (USDA) program established by the 2002 farm bill (P.L. 107-171, Sec. 10605) to improve or expand existing farmers' markets, roadside stands, community-supported agriculture programs, and other direct producer-to-consumer market opportunities, and to develop or aid in the development of new farmers’ markets, etc.  The farm bill authorized unspecified amounts of appropriations for FY2002 through FY2007 for this program.

Midtown Farmers' Market: The Midtown Farmers Market is a seasonal open-air farmers market in the Midtown area of south Minneapolis.  Established in 2003, the market is held Saturdays from May through October, and Tuesdays from June through October in a parking lot in the Corcoran neighborhood.  The market is a project of the Corcoran Neighborhood Organization, and is known for a selection of locally-produced and organic fare.  All of the products sold at the market are grown or produced in Minnesota or Wisconsin by the individual vendors.  At the peak of the season, the Saturday market hosts over 70 vendors and draws over 60,000 shoppers each season.

Sunflower Farmers Market: Sunflower Farmers Market was an American chain of full-service grocery stores headquartered in Phoenix, Arizona, which emphasized value-priced natural and organic products. Sunflower opened its first store in Albuquerque, New Mexico in 2002.  In June 2013, Sunflower Farmers Market was operating 38 grocery stores located in eight Southwestern states: Arizona, California, Colorado, Nevada, New Mexico, Utah, Oklahoma and Texas (where it formerly operated as Newflower Farmers Market).  In June 2012, Sunflower merged with Sprouts Farmers Markets.

Portland Farmers Market (Maine): The Portland Farmers Market is a farmers market in Portland, Maine, U.S. Located in Deering Oaks, the market was named one of the ten best farmers markets in the United States by "Travel + Leisure" magazine in May 2010.  It is known for organic agricultural products as well as its community atmosphere.

Farmers' market: A farmers' market (also farmers market) is a physical retail market featuring foods sold directly by farmers to consumers.  Farmers' markets typically consist of booths, tables or stands, outdoors or indoors, where farmers sell fruits, vegetables, meats, and sometimes prepared foods and beverages.  They are distinguished from public markets, which are generally housed in permanent structures, open year-round, and offer a variety of non-farmer/producer vendors, packaged foods and non-food products.

Portland Farmers Market (Oregon): Portland Farmers Market is a nonprofit organization operating seven farmers markets in Portland, Oregon, United States.  The markets provide a direct connection to more than 200 vendors with deep roots in Oregon and Southwest Washington, including farms, nurseries, bakeries, meat and seafood providers, cheese makers and specialty food producers.  The flagship market at Portland State University was named the best farmers market in the United States for its size, varied offerings, live entertainment, weekly cooking demos, and more, by "Bravo TV."  The same market was ranked #2 in the country for its number of vendors, amount of local, seasonal produce, year-round live music, the market managers' consideration of every detail, and making the most of what the region has to offer by supporting local farmers, by "The Daily Meal".

Old LA (Highland Park) Farmers Market: The Old LA Certified Farmers Market (OLACFM) operates in the Highland Park neighborhood of Los Angeles, CA.  The farmers market is open every Tuesday from 3PM to dusk year round.  One of the newest certified farmers markets in the Los Angeles area, the market opened in April 2006 and serves Highland Park and other neighborhoods in Northeast Los Angeles, including Mt. Washington, Eagle Rock,(Glassel Park, Los Angeles ) and Montecito Heights.  The OLACFM is of moderate size by Los Angeles standards, with about 10 participating farmers.  The market is located in perhaps the "downtown" center of Northeast Los Angeles, adjacent to the Highland Park station on the Metro Gold Line light rail system at Marmion Way between Aves.  57 & 58, one block from busy Figueroa Street.

Question: In May 2010 the Portland Farmers Market was named one of the ten best farmers markets in the US by a magainze that has how many readers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "farmers_market_name": {
      "type": "string",
      "description": "The name of the farmers market that received recognition."
    },
    "recognition_award": {
      "type": "string",
      "description": "The specific award or recognition received by the farmers market."
    },
    "recognition_date": {
      "type": "string",
      "description": "The date when the recognition was announced."
    },
    "awarding_publication": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the magazine or publication that gave the award."
        },
        "reader_count": {
          "type": "number",
          "description": "The number of readers the publication has."
        },
        "reader_count_unit": {
          "type": "string",
          "description": "The unit for the reader count (e.g., 'million')."
        }
      },
      "required": [
        "name",
        "reader_count",
        "reader_count_unit"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "farmers_market_name",
    "recognition_award",
    "recognition_date",
    "awarding_publication"
  ],
  "additionalProperties": false
}
