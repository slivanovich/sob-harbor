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
Vero Beach Regional Airport: Vero Beach Regional Airport (IATA: VRB, ICAO: KVRB, FAA LID: VRB) is a public airport one mile northwest of Vero Beach in Indian River County, Florida, United States.  The airport is publicly owned and is the home of Piper Aircraft.

Holman Stadium (Vero Beach): Holman Stadium is a baseball stadium in Vero Beach, Florida, built in 1953 from an abandoned Naval base, to accommodate spring training for the Brooklyn Dodgers as part of a complex now called Historic Dodgertown.  In addition to the Dodgers' spring games, it was also the home of the Vero Beach Devil Rays, previously the Vero Beach Dodgers, of the Florida State League, through the 2008 season.  Official seating capacity is 6,500.

Yampa Valley Airport: Yampa Valley Regional Airport (IATA: KHDN, ICAO: HDN) is in Routt County, Colorado, two miles southeast of Hayden and about 25 mi west of Steamboat Springs.  Also known as Yampa Valley Regional Airport, it has the only scheduled passenger flights to northwest Colorado.  It is also used by larger business jets that cannot use the smaller Steamboat Springs Airport (Bob Adams Field).

Vero Beach Devil Rays: The Vero Beach Devil Rays, originally the Vero Beach Dodgers, were a minor league baseball team based in Vero Beach, Florida.  They played in the Class A-Advanced Florida State League from 1980–2008, at which point they relocated to Port Charlotte, Florida as the Charlotte Stone Crabs.  They played their home games at Holman Stadium.

WOSN: WOSN (97.1 MHz) is a commercial FM radio station broadcasting a Soft Adult Contemporary radio format.  Licensed to Indian River Shores, Florida, USA, the station serves the Vero Beach / Fort Pierce / Stuart media market.  The station license is held by Vero Beach Broadcasters.  Studios and offices are on 16th Street in Vero Beach and the transmitter is off 77th Street, also in Vero Beach.

Old Vero Beach Community Building: The Old Vero Beach Community Building (also known as the Vero Beach Service Center, Vero Beach Physical Arts Center, or Heritage Center) is a historic building in Vero Beach, Florida.  Located at 2146 14th Avenue, the Vero Beach Community Building was built in 1935 during the New Deal Era, a project that provided residents and visitors alike with social and entertainment activities during the great depression.  The building served as a social gathering place, playhouse, and meeting hall as well as the Headquarters for the Tourist Club.  The Community Building once hosted a zoo that consisted of a bear named "Alice", an alligator, monkeys and other animals.  The site of the zoo is now occupied by Pocahantas Park.  In 1943 a north wing was added to the building in order for it to become a servingmen's club.  Organized by director Dale Wimbrow, the addition consisted of lounge, a restroom, and showers.  After World War II, the 1943 addition became the Indian River Citrus Museum.  On January 19, 1993, it was added to the U.S. National Register of Historic Places.

Hayden, Colorado: The Town of Hayden is a Home Rule Municipality in Routt County, Colorado, United States.  The population was 1,634 at the 2000 census.  The town sits along U.S. Highway 40 in the Yampa River Valley between Craig and Steamboat Springs.  Hayden is located near the Yampa Valley Regional Airport, which has seasonal passenger jet airline service during the winter ski season nonstop to Atlanta, Chicago, Dallas/Ft.  Worth, Houston, Los Angeles, Minneapolis/St.  Paul, New York Newark, and Seattle, with year-round passenger air service to Denver.  The airport's close proximity to Hayden is reflected by its three letter identifying code: HDN.  Hayden is one of the smallest communities in the U.S. to have mainline passenger jet service provided by American Airlines, Delta Air Lines, and United Airlines on a scheduled basis, if only during the winter months when the ski season is underway in nearby Steamboat Springs.

Vero Beach Museum of Art: The Vero Beach Museum of Art is located at 3001 River Park Drive, Vero Beach, Florida.  It houses regional, state and national art exhibits and includes a sculpture garden.  The Vero Beach Museum of Art is the principal cultural arts facility of its kind on Florida’s Treasure Coast.  The accredited art museum includes art exhibitions, a sculpture garden, studio art and humanities classes, exhibition tours, performances, a museum store, film studies, an art research library, workshops and seminars, children and youth events, and community cultural celebrations.

Vero Beach Diesel Power Plant: The Vero Beach Diesel Power Plant (also known as the City of Vero Beach Municipal Power Plant) is a historic power plant in Vero Beach, Florida.  Located at 1133 19th Place, the Vero Beach Diesel Power Plant was built in 1926 replacing an earlier power plant due to the areas extensive growth.  It was built in the masonry vernacular style by architects Carter and Damerow and by the engineering firm of Kennard and Sons.  The structure was the city's first public utilitarian facility.  It is also the city's oldest municipal building.  On February 26, 1999, it was added to the U.S. National Register of Historic Places.  In June 2016, the Diesel Plant was sold to real estate developer Michael R. Rechter.  Following a $6 million renovation, the building and property were adapted and reutilized as American Icon Brewery - a brewpub/production brewery which opened in September 2017.

WTTB: WTTB (1490 AM, 105.7 FM) is a radio station broadcasting a News Talk Information format.  Licensed to Vero Beach, Florida, USA, the station serves the Vero Beach area.  The station is currently licensed to Vero Beach Broadcasters, LLC and features programming from ABC Radio, Westwood One and Premiere Radio Networks.  It is one of the oldest radio stations along the Treasure Coast.  Although it is widely believed the station's slogan, "Where the tropics begin", originated with WTTB, Dr. John Leroy Hutchison has been credited for coining the phrase back in the 1920s–nearly three decades before WTTB went on the air.  The phrase was used in the 2009 television series pilot for CBS's "Harper's Island".

Question: Is Vero Beach Regional Airport or Yampa Valley Airport further south?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "southernmost_airport_name": {
      "type": "string",
      "description": "The name of the airport located further south."
    },
    "airports_compared": {
      "type": "array",
      "description": "Details of the airports being compared.",
      "items": {
        "type": "object",
        "properties": {
          "airport_name": {
            "type": "string",
            "description": "The full name of the airport."
          },
          "iata_code": {
            "type": "string",
            "description": "The IATA code for the airport."
          },
          "location_state": {
            "type": "string",
            "description": "The state where the airport is located."
          },
          "location_county": {
            "type": "string",
            "description": "The county where the airport is located."
          }
        },
        "required": [
          "airport_name",
          "iata_code",
          "location_state",
          "location_county"
        ],
        "additionalProperties": false
      }
    },
    "comparison_reasoning": {
      "type": "string",
      "description": "The geographical basis for determining which airport is further south."
    }
  },
  "required": [
    "southernmost_airport_name",
    "airports_compared",
    "comparison_reasoning"
  ],
  "additionalProperties": false
}
