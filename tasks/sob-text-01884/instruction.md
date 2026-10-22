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
Jack Brooks Regional Airport: Jack Brooks Regional Airport (IATA: BPT, ICAO: KBPT, FAA LID: BPT) , formerly Southeast Texas Regional Airport, is near Port Arthur, Texas, nine miles (14 km) southeast of Beaumont and northeast of Port Arthur.  It was formerly the Jefferson County Airport, but its name was changed to honor former U.S. Representative Jack Brooks (D - Beaumont).  The airport is southwest of the city of Nederland in unincorporated Jefferson County, and is used for general aviation.  Southwest Airlines ended scheduled service (in 1980).  A number of other airlines have also initiated and then ceased service including American Eagle, Continental, Delta/Delta Connection and United Express.  The latest chapter with regard to passenger airline service at the airport involves the resumption of service by American Eagle on behalf of American Airlines to Dallas/Ft.  Worth (DFW).

Norwegian Air Shuttle: Norwegian Air Shuttle ASA (), trading as Norwegian, is a Norwegian low-cost airline.  It is the third largest low-cost carrier in Europe, the largest airline in Scandinavia, and the ninth-largest airline in Europe in terms of passenger numbers.  It offers a high-frequency domestic flight schedule within Scandinavia and Finland, and to business destinations such as London, as well as to holiday destinations in the Mediterranean and the Canary Islands, transporting over 30 million people in 2016.  The airline is known for its distinctive livery of white with a red nose, with portraits of distinguished Scandinavians on the tail fins of its aircraft.

America West Airlines: America West Airlines was a U.S. airline headquartered in Tempe, Arizona.  Their main hub was at Sky Harbor Airport in Phoenix, Arizona, with a secondary hub at Las Vegas McCarran International Airport in Las Vegas, Nevada.  The airline became part of the US Airways Group after it acquired the larger airline in 2005 and adopted the US Airways brand name.  America West was the second largest low-cost carrier in the U.S. after Southwest Airlines and served approximately 100 destinations in the US, Canada, and Mexico.  Service to Europe was provided through codeshare partners.  In March 2005, the airline operated a fleet of 132 aircraft, with a single maintenance base at Sky Harbor Airport in Phoenix.  Regional jet and/or turboprop feeder flights were operated on a code sharing basis by Mesa Airlines and Chautauqua Airlines as America West Express.

Low-cost carrier: A low-cost carrier or low-cost airline (also known as "no-frills", "discount" or "budget" carrier or airline, or "LCC") is an airline that generally has lower fares and fewer comforts.  To make up for revenue lost in decreased ticket prices, the airline may charge for extras such as food, priority boarding, seat allocating, and baggage.  As of July 2014, the world's largest low-cost carrier is Southwest Airlines, which operates in the United States and some surrounding areas.

Norwegian Air Shuttle destinations: Norwegian Air Shuttle is a low-cost airline operating from Norway, Sweden, Denmark, Finland, Spain and the United Kingdom.  As of December 2012, it operates to 87 airports in 25 countries across three continents, from its operating bases.  Norwegian was founded in 1993 as a regional airline to operate routes for Braathens SAFE in Western Norway.  It became a domestic, main-haul low-cost carrier from 1 September 2002, when it took into use Boeing 737-300.  In 2006, Norwegian Air Shuttle established its first non-Norwegian base at Warsaw Frédéric Chopin Airport in Poland.  A year later, Norwegian bought the Swedish low-cost carrier FlyNordic, which was merged into Norwegian a year later.

Jetsgo: Jetsgo Corporation was a Canadian low-cost carrier based in the Saint-Laurent area of Montreal.  Jetsgo served 19 destinations across Canada, 10 destinations in the United States, and 12 scheduled weekend-charter destinations in the Caribbean.  At the time the third-largest carrier in the country, Jetsgo abruptly ended service and entered bankruptcy protection on March 11, 2005, leaving thousands of passengers stranded at the beginning of the busy March-break travel season.  According to news outlets, the airline was processing orders and taking payments for flights the night before they claimed bankruptcy and ceased operations.

Southwest Airlines: Southwest Airlines Co. () is a major U.S. airline and the world's largest low-cost carrier headquartered in Dallas, Texas.

List of low-cost airlines: The following is a list of low-cost carriers organized by home country.  A low-cost carrier or low-cost airline (also known as a no-frills, discount or budget carrier or airline) is an airline that offers generally low fares in exchange for eliminating many traditional passenger services.  Regional airlines, which may compete with low-cost airlines on some routes, are listed at List of regional airlines.

China Airlines: China Airlines (CAL) () () is the flag carrier and largest airline of the Republic of China (Taiwan).  It is headquartered in Taoyuan International Airport and has 12,607 regular employees.  China Airlines operates over 1,400 flights weekly to 118 airports in 115 cities (including codeshare) across Asia, Europe, North America and Oceania.  The cargo division operates 91 pure freighter flights weekly.  The carrier was, in 2013, the 29th and 10th largest airline in the world in terms of passenger revenue per kilometer (RPK) and freight RPK, respectively.  China Airlines has three airline subsidiaries: Mandarin Airlines operates flights to domestic and low-demand regional destinations; China Airlines Cargo, a member of Skyteam Cargo, operates a fleet of freighter aircraft and manages its parent airline's cargo-hold capacity; Tigerair Taiwan is a low-cost carrier established by China Airlines and Singaporean airline group Tigerair Holdings and is wholly owned by China Airlines Group.

United Airlines: United Airlines, Inc., commonly referred to as United, is a major U.S. airline headquartered in Chicago, Illinois.  It is the world's third-largest airline when measured by revenue, after American Airlines and Delta Air Lines.  United operates a large domestic and international route network, with an extensive presence in the Asia-Pacific region.  United is a founding member of Star Alliance, the world's largest airline alliance.  Regional service is operated by independent carriers under the brand name United Express.  Its main competitors are American Airlines, Delta Air Lines, and Southwest Airlines.

Question: What major U.S. airline and the world's largest low-cost carrier headquartered in Dallas, Texas, ended service at Jack Brooks Regional Airport in 1980?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airline_name": {
      "type": "string",
      "description": "The name of the airline."
    },
    "is_major_us_airline": {
      "type": "boolean",
      "description": "Indicates if the airline is a major U.S. airline."
    },
    "is_worlds_largest_low_cost_carrier": {
      "type": "boolean",
      "description": "Indicates if the airline is the world's largest low-cost carrier."
    },
    "headquarters_city": {
      "type": "string",
      "description": "The city where the airline is headquartered."
    },
    "airport_name": {
      "type": "string",
      "description": "The name of the airport where service ended."
    },
    "service_end_year": {
      "type": "integer",
      "description": "The year the airline ended service at the specified airport."
    }
  },
  "required": [
    "airline_name",
    "is_major_us_airline",
    "is_worlds_largest_low_cost_carrier",
    "headquarters_city",
    "airport_name",
    "service_end_year"
  ],
  "additionalProperties": false
}
