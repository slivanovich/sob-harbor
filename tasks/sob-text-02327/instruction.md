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
Camelback Inn: Camelback Inn (officially titled: JW Marriott Scottsdale Camelback Inn Resort and Spa) is a historic resort and spa owned by JW Marriott Hotels and located on the southern slope of Mummy Mountain in Paradise Valley, Arizona.  Established in 1936 by Jack Stewart and John C. Lincoln, the resort's popularity among Hollywood celebrities and political leaders made it a significant contributor to the region's growth.  In 2012, Camelback Inn was one of three North American hotels which had maintained a AAA 5-Diamond rating since the award's inception in 1975.  In 2013, AAA reduced the hotel's status to four diamonds.

Sunset Mountains (Arizona): The Sunset Mountains in Coconino County, Arizona are two a small mesas known as East Sunset Mountain and West Sunset Mountain, located southeast of Winslow.  State Route 87 passes between the mountains.

Belleview-Biltmore Hotel: The Belleview Biltmore Resort and Spa was a historic resort hotel located at 25 Belleview Boulevard in the town of Belleair, Florida, United States.  The 400,000 sqft hotel structure was the last remaining grand historic hotel of its period in Florida that existed as a resort, and the only Henry Plant hotel still in operation when it closed in 2009.  The building was noted for its architectural features, with its unique green sloped roof and white wood-sided exterior, and extensive handcrafted woodwork and Tiffany glass inside.  Constructed of native Florida pine wood, it was said to be the largest occupied wood frame structure in the world during its heyday.

Sunset Beach Hotel: The Sunset Beach Hotel, also referred to as Peters' Sunset Beach Resort, is a historic resort hotel in Glenwood Township, Pope County, Minnesota, 5 mi southwest of Glenwood, United States.  Situated on the southern shore of Lake Minnewaska, three structures of the private, commercial resort were placed on the National Register of Historic Places (NRHP) on February 11, 1982.  The complex is notable because it stands as one of the best-preserved early resorts in west central Minnesota, and as a center of seasonal resort activity on the lake since the second decade of the twentieth century.

St. Petersburg Open Invitational: The St. Petersburg Open Invitational, first played as the St. Petersburg Open, was a PGA Tour event that was held at three St. Petersburg, Florida area clubs for 29 years from 1930 until 1964.  The clubs that hosted the event were: Lakewood Country Club (now known as St. Petersburg Country Club), Pasadena Country Club (now known as Pasadena Yacht and Country Club), and Sunset Golf Club of the Vinoy Park Hotel (now known as the Renaissance Vinoy Resort & Golf Club).

Asheville Open: The Asheville Open was a golf tournament on the LPGA Tour from 1957 to 1960.  It was played at the Asheville Country Club in Asheville, North Carolina.  In 1958 and 1959, some rounds were also played at the Beaver Lake Golf Club and the Biltmore Forest Country Club.

Grove Park Historic District: Grove Park Historic District is a national historic district located at Asheville, Buncombe County, North Carolina.  The district encompasses 290 contributing buildings and 1 contributing site in a predominantly residential section Asheville.  The planned suburban community was originally platted and developed in 1908-1913 and 1914.  It includes representative examples of Colonial Revival, Tudor Revival, and Bungalow style dwellings.  The community was laid out by noted landscape architect Chauncey Beadle.  The Kimberly Amendment to Grove Park was an expansion made to the original Grove Park development in 1923.  It includes the former Asheville Country Club, now the Grove Park Inn Country Club.

Eagle Mountain House: Eagle Mountain House is a historic resort hotel at 179 Carter Notch Road in Jackson, New Hampshire.  Built in 1916 and enlarged in 1929, it is one of the few surviving grand mountain resort hotels in the White Mountains of New Hampshire.  It was listed on the National Register of Historic Places in 1990.

The Omni Grove Park Inn: The Grove Park Inn is an historic resort hotel on the western-facing slope of Sunset Mountain within the Blue Ridge Mountains, in Asheville, North Carolina.  It is a AAA Four-Diamond Hotel and has been since

Manor and Cottages: Manor and Cottages is a historic resort complex and national historic district located at Asheville, Buncombe County, North Carolina.  The complex encompassed 36 contributing buildings that were built starting in 1898.  The main hotel, The Manor, was built starting in 1898-1899, and consists of a rambling group of interconnected wings with elements of the Colonial Revival, Shingle Style, and Tudor Revival styles.  Wings were added to the original building in 1903 and 1913-1914.  Located on the property are the contributing Club House (c. 1903) and a 19 guest cottages built between 1899 and 1920.  The hotel was later converted for use as a retirement hotel for elderly persons with limited incomes.

Question: What is this historic resort hotel on the western-facing slope of Sunset Mountain, formerly known as Asheville Country Club?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "hotel_name": {
      "type": "string",
      "description": "The name of the historic resort hotel."
    },
    "hotel_type": {
      "type": "string",
      "description": "The type of establishment, e.g., 'historic resort hotel'."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "mountain_slope": {
          "type": "string",
          "description": "The specific slope of the mountain where the hotel is located."
        },
        "mountain_name": {
          "type": "string",
          "description": "The name of the mountain."
        },
        "city": {
          "type": "string",
          "description": "The city where the hotel is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the hotel is located."
        }
      },
      "required": [
        "mountain_slope",
        "mountain_name",
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "associated_country_club": {
      "type": "object",
      "properties": {
        "former_name": {
          "type": "string",
          "description": "The former name of the country club associated with the hotel."
        },
        "current_name": {
          "type": "string",
          "description": "The current name of the country club associated with the hotel."
        }
      },
      "required": [
        "former_name",
        "current_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "hotel_name",
    "hotel_type",
    "location_details",
    "associated_country_club"
  ],
  "additionalProperties": false
}
