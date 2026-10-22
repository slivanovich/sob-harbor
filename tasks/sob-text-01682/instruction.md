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
Aquarius Casino Resort: Aquarius Casino Resort (formerly Flamingo Hilton Laughlin and Flamingo Laughlin) is a hotel and casino located on the banks of the Colorado River in Laughlin, Nevada.  It is owned and operated by American Casino & Entertainment Properties and is the largest hotel in Laughlin.

Cottonwood Cove, Nevada: Cottonwood Cove is situated at the banks of Lake Mohave on the Nevada-Arizona border in Clark County, Nevada, United States.  It stands just 13.1 miles (21 kilometers) and 23 minutes east of Searchlight, 12.5 miles (20 kilometers) north of Laughlin and an hour away from Las Vegas.  It is the site of the Cottonwood Cove Resort and Marina.  The cove is part of the Lake Mead National Recreation Area administered by the U.S. National Park Service.  The desert lake is approximately 67 miles long and is backed by the Davis Dam on the Colorado River.

Laughlin/Bullhead International Airport: Laughlin/Bullhead International Airport (IATA: IFP, ICAO: KIFP, FAA LID: IFP) is a public use airport located one nautical mile (2 km) north of the central business district of Bullhead City, in Mohave County, Arizona, United States.  It is owned by Mohave County.  The airport is across the Colorado River and one block away from Laughlin, Nevada.  Many of the rooms at Laughlin's casino-hotels offer a view of the airport.  It was named "2011 Airport of the Year" by the Arizona Department of Transportation.

Vegas Vic: Vegas Vic is a Las Vegas, Nevada neon sign that resembles a cowboy that was erected on the exterior of The Pioneer Club in Las Vegas in 1951.  The sign was a departure in graphic design from typeface based neon signs, to a friendly and welcoming human form of a cowboy.  The sign's human-like abilities of talking and waving its arm constituted an immediate acceptance as the unofficial welcoming sign reproduced thousands of times over the years and all over the world.  The trademark is currently owned by Pioneer Hotel, Inc. which owns and operates the Pioneer Hotel and Gambling Hall in Laughlin, Nevada.  The sign can still be found at 25 E Fremont Street, where he has been since 1951 on the exterior of what used to be The Pioneer Club but is currently a souvenir shop.  Pioneer Hotel, Inc. is the owner of the Pioneer Hotel and Gambling Hall along the Colorado River in Laughlin, Nevada that has a twin of the Vegas Vic image on another large sign referred to as River Rick.

Laughlin, Nevada: Laughlin is an unincorporated town and census-designated place in Clark County, Nevada, United States, and a port located on the Colorado River.  Laughlin is 90 mi south of Las Vegas, located in the far southern tip of Nevada.  It is best known for its gaming, entertainment, and water recreation.  As of the 2010 census, the population was 7,323.  The nearby communities of Bullhead City, Arizona; Needles, California; Fort Mohave, Arizona; and Mohave Valley, Arizona, bring the Laughlin area's total population to about 100,000.

Boulder Wash Cove: Boulder Wash Cove is a cove in Lake Mead, in Clark County, Nevada.  Boulder Wash for which the cove is named has its mouth in the cove at an elevation of 1,204 / 367 meters when the reservoir is at its full level.

Cottonwood Island (Nevada): Cottonwood Island, a large island in the Colorado River, within Cottonwood Valley, in Clark County, Nevada.  Cottonwood Island was a low-lying island about 10 miles long and up to 3 miles wide.  It was forested by cottonwoods and also after the spring flood, cluttered with driftwood from the riparian woodlands along the upper watershed of the Colorado River, washed down and caught in the first wide valley where the river slowed and spread out.  Cottonwood Island was important as a source wood and of fuel for steamboats on that river and for the early mills and mines in El Dorado Canyon.

Lake Mohave: Lake Mohave is a reservoir on the Colorado River between the Hoover Dam and Davis Dam in Cottonwood Valley defining the border between Nevada and Arizona in the United States.  This 67 mile stretch of the Colorado River flows past Boulder City, Nelson, Searchlight, Cottonwood Cove, Cal-Nev-Ari, and Laughlin to the west in Nevada and Willow Beach and Bullhead City to the east in Arizona.  A maximum width of 4 miles wide and an elevation of 647 ft , Lake Mohave encompasses 28,260 acres of water.  As Lake Mead lies to the north of the Hoover Dam, Lake Mohave and adjacent lands forming its shoreline are part of the Lake Mead National Recreation Area administered by the U.S. National Park Service.

Clark County Water Reclamation District: The Clark County Water Reclamation District (District) is a government wastewater treatment agency in Clark County, Nevada.  As a member of the Southern Nevada Water Authority, its mission is to treat millions of gallons of wastewater that is produced every day.  The District is the largest water treatment agency in Southern Nevada and is responsible for treating wastewater from unincorporated parts of Clark County within the Las Vegas Valley, including most of the Las Vegas Strip, and the communities of Blue Diamond, Moapa Valley, Nevada, Indaian Springs, Nevada, Laughlin, Nevada, and Searchlight.

River Run Riot: The River Run Riot was a violent confrontation between the Hells Angels and the Mongols motorcycle clubs that occurred on April 27, 2002, in Laughlin, Nevada during the Laughlin River Run.  The conflict began when members of the Hells Angels went to Harrah's Laughlin to confront members of the Mongols who had allegedly harassed vendors that sold Hells Angels related merchandise.  Mongol Anthony Barrera, 43, was stabbed to death, and two Hells Angels, Jeramie Bell, 27, and Robert Tumelty, 50, were shot to death.

Question: What county is Cottonwood Cove, Nevada and Laughlin, Nevada in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "county_name": {
      "type": "string",
      "description": "The name of the county where the places are located."
    },
    "state_name": {
      "type": "string",
      "description": "The name of the state where the county is located."
    },
    "located_places": {
      "type": "array",
      "description": "A list of places found within the specified county.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "county_name",
    "state_name",
    "located_places"
  ],
  "additionalProperties": false
}
