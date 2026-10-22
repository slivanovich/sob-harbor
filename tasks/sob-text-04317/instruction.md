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
Low-cost carrier: A low-cost carrier or low-cost airline (also known as "no-frills", "discount" or "budget" carrier or airline, or "LCC") is an airline that generally has lower fares and fewer comforts.  To make up for revenue lost in decreased ticket prices, the airline may charge for extras such as food, priority boarding, seat allocating, and baggage.  As of July 2014, the world's largest low-cost carrier is Southwest Airlines, which operates in the United States and some surrounding areas.

Norwegian Air Shuttle destinations: Norwegian Air Shuttle is a low-cost airline operating from Norway, Sweden, Denmark, Finland, Spain and the United Kingdom.  As of December 2012, it operates to 87 airports in 25 countries across three continents, from its operating bases.  Norwegian was founded in 1993 as a regional airline to operate routes for Braathens SAFE in Western Norway.  It became a domestic, main-haul low-cost carrier from 1 September 2002, when it took into use Boeing 737-300.  In 2006, Norwegian Air Shuttle established its first non-Norwegian base at Warsaw Frédéric Chopin Airport in Poland.  A year later, Norwegian bought the Swedish low-cost carrier FlyNordic, which was merged into Norwegian a year later.

Thai Airways: Thai Airways International Public Company Limited, trading as THAI (, Thai: บริษัท การบินไทย จำกัด (มหาชน) ) is the flag carrier airline of Thailand.  Formed in 1988, the airline has its corporate headquarters in Vibhavadi Rangsit Road, Chatuchak District, Bangkok, and primarily operates out of Suvarnabhumi Airport.  THAI is a founding member of the Star Alliance.  The airline is the largest shareholder of the low-cost carrier Nok Air with a 39 percent stake, and it launched a regional carrier under the name Thai Smile in the middle of 2012 using new Airbus A320 aircraft.

Southwest Airlines: Southwest Airlines Co. () is a major U.S. airline and the world's largest low-cost carrier headquartered in Dallas, Texas.

Norwegian Air Shuttle: Norwegian Air Shuttle ASA (), trading as Norwegian, is a Norwegian low-cost airline.  It is the third largest low-cost carrier in Europe, the largest airline in Scandinavia, and the ninth-largest airline in Europe in terms of passenger numbers.  It offers a high-frequency domestic flight schedule within Scandinavia and Finland, and to business destinations such as London, as well as to holiday destinations in the Mediterranean and the Canary Islands, transporting over 30 million people in 2016.  The airline is known for its distinctive livery of white with a red nose, with portraits of distinguished Scandinavians on the tail fins of its aircraft.

China Airlines: China Airlines (CAL) () () is the flag carrier and largest airline of the Republic of China (Taiwan).  It is headquartered in Taoyuan International Airport and has 12,607 regular employees.  China Airlines operates over 1,400 flights weekly to 118 airports in 115 cities (including codeshare) across Asia, Europe, North America and Oceania.  The cargo division operates 91 pure freighter flights weekly.  The carrier was, in 2013, the 29th and 10th largest airline in the world in terms of passenger revenue per kilometer (RPK) and freight RPK, respectively.  China Airlines has three airline subsidiaries: Mandarin Airlines operates flights to domestic and low-demand regional destinations; China Airlines Cargo, a member of Skyteam Cargo, operates a fleet of freighter aircraft and manages its parent airline's cargo-hold capacity; Tigerair Taiwan is a low-cost carrier established by China Airlines and Singaporean airline group Tigerair Holdings and is wholly owned by China Airlines Group.

List of low-cost airlines: The following is a list of low-cost carriers organized by home country.  A low-cost carrier or low-cost airline (also known as a no-frills, discount or budget carrier or airline) is an airline that offers generally low fares in exchange for eliminating many traditional passenger services.  Regional airlines, which may compete with low-cost airlines on some routes, are listed at List of regional airlines.

AirTran Airways: AirTran Airways was an American low-cost airline headquartered originally in Orlando, Florida, then in Dallas, Texas, after its acquisition by Southwest Airlines, into which it was integrated.  AirTran operated nearly 700 daily flights, primarily in the eastern and midwestern United States, with its principal hub at Hartsfield-Jackson Atlanta International Airport where it operated nearly 200 daily departures.  AirTran's fleet consisted of Boeing 717-200 aircraft, of which it was the world's largest operator, and Boeing 737-700 aircraft.  It was fully integrated into Southwest Airlines on December 28, 2014.

AirTran Holdings: AirTran Holdings () was a Nevada corporation, based in Orlando, Florida, United States, that operated as an airline holding company.  Its primary asset was AirTran Airways until Southwest Airlines acquired AirTran on May 2, 2011.

America West Airlines: America West Airlines was a U.S. airline headquartered in Tempe, Arizona.  Their main hub was at Sky Harbor Airport in Phoenix, Arizona, with a secondary hub at Las Vegas McCarran International Airport in Las Vegas, Nevada.  The airline became part of the US Airways Group after it acquired the larger airline in 2005 and adopted the US Airways brand name.  America West was the second largest low-cost carrier in the U.S. after Southwest Airlines and served approximately 100 destinations in the US, Canada, and Mexico.  Service to Europe was provided through codeshare partners.  In March 2005, the airline operated a fleet of 132 aircraft, with a single maintenance base at Sky Harbor Airport in Phoenix.  Regional jet and/or turboprop feeder flights were operated on a code sharing basis by Mesa Airlines and Chautauqua Airlines as America West Express.

Question: On what date did the world's largest low-cost carrier airline acquire AirTran?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "acquiring_carrier": {
      "type": "string",
      "description": "The name of the airline that performed the acquisition."
    },
    "acquiring_carrier_status": {
      "type": "string",
      "description": "The status or title of the acquiring carrier as described in the context."
    },
    "acquired_carrier": {
      "type": "string",
      "description": "The name of the airline that was acquired."
    },
    "acquisition_date": {
      "type": "string",
      "format": "date",
      "description": "The date when the acquisition took place."
    }
  },
  "required": [
    "acquiring_carrier",
    "acquiring_carrier_status",
    "acquired_carrier",
    "acquisition_date"
  ],
  "additionalProperties": false
}
