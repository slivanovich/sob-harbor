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
Highland (Capital MetroRail station): Highland is a Capital MetroRail commuter rail station in Austin, Texas, USA.  It is located in northeast Austin at the intersection of Airport Boulevard and Highland Mall Boulevard, just northwest of the I-35/Highway 290 interchange directly across the street from Highland Mall.

Brookside Shopping District: The Brookside Shopping District is located in the Brookside neighborhood of Kansas City, Missouri at 63rd Street & Brookside Boulevard.  This district was founded in 1920 as Kansas City’s first suburban shopping center.

Occidental Life Insurance Company Building: Occidental Life Insurance Company Building is a historic office building located at Raleigh, North Carolina.  The building is located in Cameron Village, North Carolina's first suburban shopping center.  It was built in 1956, and is a four-story, 68,000 square-foot steel frame structure encapsulated in concrete.  The building was design by architecture firm Kemp, Bunch & Jackson and in the International Style.  It has a brick base, limestone walls, aluminum windows with green-tinted glass, and entrance canopies with rounded aluminum eaves.  Prior to moving to this building, the Occidental Life Insurance Company offices were housed in the Professional Building for nearly 30 years.

Seletar Mall: The Seletar Mall (Chinese: 利达广场) is a suburban shopping mall located in Fernvale of Sengkang New Town, Singapore.  The mall is the first mall in the North-Eastern part of Singapore to house a cinema.  Construction of the mall started in year end 2012 and it officially opened on November 28, 2014.

Shoppers World Danforth: Shoppers World Danforth is a hybrid shopping plaza and shopping mall in Toronto, Ontario, Canada.  It has 40 stores serving parts of East York, Scarborough and The Beaches, near the Victoria Park subway station.  Today a moderately sized suburban plaza, it has a notable place in history as one of the first suburban and one of the first enclosed malls in Canada.  It is approximately 342500 sqft in area.

Downtown Norfolk, Virginia: Similarly, the advent of newer suburban shopping destinations spelled demise for the fortunes of downtown's Granby Street commercial corridor, located just a few blocks inland from the waterfront.  Granby Street traditionally played the role as the premiere shopping and gathering spot in the Hampton Roads region and numerous department stores such as Smith & Welton (1898-1988), Rices Nachmans (1918-1985) and Ames and Brownley (1898-1973), fine hotels and theaters once lined its sidewalks.  However, new suburban shopping developments promised more convenience and comfort.  The opening of Pembroke Mall in Virginia Beach, the region's first climate controlled shopping mall, and JANAF Shopping Center in Norfolk's Military Circle area, helped foment Granby Street's spiral into commercial obsolescence.  With amenities such as ample free parking at the door of one's favorite store, and in the case of Pembroke Mall, climate control, the businesses of downtown's Granby Street found it harder and harder to compete.

Barton Creek Square: Barton Creek Square is an enclosed shopping mall located in southwest Austin, Texas in the United States, near the intersection of Texas State Highway Loop 1 and Texas State Highway Loop 360.  Eponymously named after Barton Creek, Texas, the shopping mall was built in 1980.  In November 1981, the mall became the first in Texas to have Braille and bold print signage throughout the center.

Bedok Mall: Bedok Mall (Chinese: 勿落广场) is a large suburban shopping mall in Bedok, Singapore and part of a mixed development compromising of retail and residential development that is integrated with a bus interchange.  Located at the heart of Bedok, the integrated retail and residential development comprises a 3-storey lifestyle and family shopping mall and eight 15-storey residential towers called Bedok Residences.  It was the first major shopping mall to open in Bedok and was built on the site of the former Bedok bus interchange.

AMK Hub: AMK Hub (abbreviation for Ang Mo Kio Hub; Simplified Chinese: 宏茂桥购物坊) is a suburban shopping mall located in Ang Mo Kio, within the North-East Region of Singapore.  It is connected to Ang Mo Kio Bus Interchange which is linked to Ang Mo Kio MRT station via an underpass.  The shopping mall has 48,250 square metres of gross floor area and 350000 sqft of retail space.

Highland Mall: Highland Mall was a shopping mall located in north Austin, Texas, on Airport Boulevard west of I-35 and north of US Route 290.  Opened in 1971, Highland Mall was Austin's first suburban shopping mall.  Highland Mall was jointly owned by General Growth and Simon Property Group until 2011.  Austin Community College began acquiring the surrounding land in 2010, assumed ownership of the last parcel it did not already control in August 2011.  On April 29, 2015, Highland Mall officially closed its doors.

Question: What highway was the first suburban shopping mall in Austin, Texas located on?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mall_name": {
      "type": "string",
      "description": "The name of the shopping mall."
    },
    "city": {
      "type": "string",
      "description": "The city where the mall is located."
    },
    "state": {
      "type": "string",
      "description": "The state where the mall is located."
    },
    "is_first_suburban_mall": {
      "type": "boolean",
      "description": "Indicates if this was the first suburban shopping mall in its city."
    },
    "nearby_highways": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of highways the mall was located near."
    }
  },
  "required": [
    "mall_name",
    "city",
    "state",
    "is_first_suburban_mall",
    "nearby_highways"
  ],
  "additionalProperties": false
}
