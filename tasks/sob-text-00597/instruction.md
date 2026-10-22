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
SriLankan Airlines destinations: SriLankan Airlines, is the flag carrier of Sri Lanka.  Launched in 1979, the airline’s hub is located at Bandaranaike International Airport in Colombo, providing connections to its global route network of 96 destinations in 46 countries (including codeshare operations along with its partner OneWorld airlines).  The following is a list of destinations served by SriLankan Airlines, as of May 2017.  The list includes the city and country name; the airport codes of the International Air Transport Association (IATA airport code) and the International Civil Aviation Organization (ICAO airport code); the airport name.

Totana: Totana is a municipality in the Region of Murcia in Spain.  It has a population of 30,850.  The local economy is largely dependent on agriculture and related industries.  it has a railway station providing a service on the Cercanías Murcia/Alicante commuter line, providing connections to Alicante and Murcia.

Foshan–Dongguan Intercity Railway: Foshan-Dongguan Intercity Railway, also called the Fo-Guan Intercity Railway, is a planned high-speed railway within Guangdong province, China, between the cities of Foshan, via Guangzhou, to Dongguan.  It forms one leg of the Pearl River Delta Rapid Transit regional network and will provide connections with the Guangzhou–Dongguan–Shenzhen Intercity Railway, Dongguan–Huizhou Intercity Railway and local metro systems.  It will connect Panyu District, Guangzhou at the major Guangzhou South interchange, tunnelling under the Pearl River through Machong and Hongmei to Wanghong Railway Station providing connections via the Dongguan Rail Transit, the Guangzhou–Dongguan–Shenzhen Intercity Railway or the Dongguan–Huizhou Intercity Railway.  The length of the railway is 36.681 kilometres.  Although this first phase of the project is named "Foshan-Dongguan Intercity Railway", it does not pass through the city of Foshan in any way.  The second section of this railway from Guangzhou South to Foshan West Railway Station has been planned, prepared and the line is under construction as the "Guangfo Intercity Railway", the first phase of the Guangzhou Circle Intercity Railway.

VINE Transit: VINE Transit (an acronym for Valley Intercity Neighborhood Express.)  is a public transportation service in Napa County, California, United States; it is managed under the Napa Valley Transportation Authority and operated by Transdev.  The system offers extensive service throughout the County along with providing connections to other public transportation systems in adjacent counties.

U.S. Route 95 in Nevada: U.S. Route 95 (US 95) is a major U.S. highway traversing the U.S. state of Nevada from north to south directly through Las Vegas and providing connections to both Carson City (via US 50) and Reno (via Interstate 80).  US 95 is cosigned with Interstate 80 for 95 mi between a junction in Churchill County and Winnemucca before heading north into Oregon at McDermitt.

Interstate 64 in Indiana: Interstate 64 (I-64) in the U.S. state of Indiana is a major east–west highway providing access between Illinois and Kentucky.  It passes through Indiana as part of its connection between the two metropolitan areas of St Louis, Missouri, and Louisville, Kentucky.

Glen Allen, Alabama: Glen Allen is a town located in Fayette and Marion counties in the U.S. state of Alabama.  The town incorporated in May 1959.  At the 2010 census the population was 510.  Glen Allen is positioned along the BNSF railway and is near Interstate 22, providing access to multiple expanding industries.

Holt railway station: Holt railway station served the town of Holt in Norfolk, England.  It was part of the Midland and Great Northern Joint Railway network, which spread over much of East Anglia, providing connections to Cromer, Norwich and Yarmouth.  Closed in 1964, there are proposals afoot to rebuild the line through the locality as part of an orbital railway scheme.

Banbury Merton Street railway station: Banbury Merton Street was the first railway station to serve the Oxfordshire market town of Banbury in England.  It opened in 1850 as the northern terminus of the Buckinghamshire Railway providing connections to Bletchley and Oxford and closing for passengers in 1961 and goods in 1966.

Interstate 22: Interstate 22 (I-22) is an Interstate Highway that follows the U.S. Route 78 (US 78) corridor on a 213 mi route from Byhalia, Mississippi south of Memphis, Tennessee, to Birmingham, Alabama.  I-22 indirectly connects I-240, I-40, I-55, and I-69 in the northwest with I-65 and I-20/I-59 in the southeast.  When designated in 2012, it was designed to close a gap in the Interstate network allowing more direct connections between cities in the southeast (such as Atlanta and Birmingham) with those of the Great Plains (such as Oklahoma City and St. Louis).

Question: What town has access to industries while being located along a highway providing connections between cities in the southeast?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "town_name": {
      "type": "string",
      "description": "The name of the town."
    },
    "town_location": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string",
          "description": "The U.S. state where the town is located."
        },
        "counties": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The counties in which the town is located."
        }
      },
      "required": [
        "state",
        "counties"
      ],
      "additionalProperties": false
    },
    "nearby_highway": {
      "type": "object",
      "properties": {
        "highway_name": {
          "type": "string",
          "description": "The name or designation of the nearby highway."
        },
        "highway_type": {
          "type": "string",
          "description": "The type of highway (e.g., 'Interstate Highway')."
        },
        "provides_access_to_industries": {
          "type": "boolean",
          "description": "Indicates if the town, via the highway, provides access to industries."
        },
        "connects_southeast_cities": {
          "type": "boolean",
          "description": "Indicates if the highway provides connections between cities in the southeast."
        },
        "connected_cities_examples": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Examples of cities in the southeast connected by the highway."
        }
      },
      "required": [
        "highway_name",
        "highway_type",
        "provides_access_to_industries",
        "connects_southeast_cities",
        "connected_cities_examples"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "town_name",
    "town_location",
    "nearby_highway"
  ],
  "additionalProperties": false
}
