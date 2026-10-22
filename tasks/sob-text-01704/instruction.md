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
O'Sheas Casino: O'Sheas Casino is a casino located within The Linq on the Las Vegas Strip in Paradise, Nevada.  As part of The Linq, it is owned and operated by Caesars Entertainment Corporation and is connected on the exterior to a shopping/dining promenade, also owned by Caesars.  The revitalized O'Sheas has three bars - the main Dublin Up Bar, the Lucky Bar and the exterior-facing Blarney Bar.  The casino includes beer pong tables, a stage, a dance floor and a pit with games including blackjack, roulette, and craps.

Westgate station (Las Vegas Monorail): Westgate station is a station on the Las Vegas Monorail.  The station is an island platform located at the Westgate Las Vegas Resort & Casino.  The Westgate Station is located near the main entrance of the property.  The station can be reached through the SpaceQuest Casino in the front of the hotel.  It is the only monorail station in Las Vegas that is located in the front of the hotel.  The monorail station at the Westgate is the shortest distance from a hotel than any other station.

Frank Marino (female impersonator): Frank Marino (born November 20, 1963 in Brooklyn, New York) is a female impersonator dubbed "Ms. Las Vegas" for his longtime starring role as Joan Rivers in the Las Vegas drag revue "Frank Marino's Divas Las Vegas", playing at the Imperial Palace Hotel and Casino (now The Linq) on the Las Vegas Strip.

Harrah's Las Vegas: Harrah's Las Vegas (formerly Holiday Casino) is a hotel and casino located on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by Caesars Entertainment Corporation.  It has over 1,200 slot machines.

The Linq: The Linq (formerly Flamingo Capri, Imperial Palace and The Quad) is a 2,640-room hotel, casino and shopping promenade on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by Caesars Entertainment Corporation.  As of 2012, the casino is 32890 sqft with 830 slot machines, 55 table games, and a race and sports book.

Harrah's &amp; The Linq station: Harrah's & The Linq station (originally Harrah's/Imperial Palace station, and then Harrah's/The Quad station) is a station on the Las Vegas Monorail.  The station is an island platform located between the Harrah's Las Vegas hotel and The Linq (formerly Imperial Palace and then The Quad Resort and Casino).  The station is located on the east side of Las Vegas Boulevard between the two hotels.  The station may be entered through either resort by heading to the back of these properties and following the signs to reach the Monorail station connector.

Harrah's New Orleans: Harrah's New Orleans is a casino located in New Orleans, Louisiana, near the foot of Canal Street a block away from the Mississippi River.  It is a 115000 sqft casino with approximately 2,100 slot machines, over 90 table games and a poker room.  There are several places to eat ranging from buffet style to fine dining.  Since its opening in 1999 Harrah's has been renting nearby hotel rooms to accommodate its guests; currently, the newly renovated 202-room Wyndham Riverfront Hotel is providing such accommodations.  In order to avoid leasing rooms, the casino opened its own 27-story hotel tower with 450 rooms across the street from the casino on September 21, 2006, just days ahead of the New Orleans Saints return to the Louisiana Superdome.  It is the only land-based private casino with table games in the state by Louisiana law (there are other casinos in the state with their gambling facilities on floating boats and horse racing racinos with slot machines).  It is referred to in state statute as "the official gaming establishment", see Chp.10, Title 4 of Louisiana Revised Statutes.

Monte Carlo Resort and Casino: The Monte Carlo Resort and Casino is a megaresort hotel and casino on the Las Vegas Strip in Paradise, Nevada, United States.  The hotel, with a height of 360 ft , has 32 floors, featuring a 102000 sqft casino floor with 1,400 slot machines, 60 table games, and 15 poker tables.  It is owned and operated by MGM Resorts International.  The hotel offers 2,992 guest rooms, including 259 luxury suites.  It is being converted from late 2016 to 2018 into the Park MGM, with the upper floors converted into a boutique hotel, NoMad Las Vegas.

Dennis Nikrasch: Dennis Nikrasch (September 12, 1941 – 2010) was a Vegas slot cheater and a former locksmith who was responsible for spearheading the biggest casino theft in Las Vegas history, by grabbing $16,000,000 from rigging slot machines over a 22-year period.  His career began in Chicago, Illinois as a locksmith.  He then found out that he could break into any lock he wished, due to his extensive knowledge of the tools, and became associated with members from a key Chicago crime family until his arrest in 1961.  When he was released in 1970, he realized that he could make even bigger profits by manipulating slot machines in Las Vegas.  From 1976 until 1983, he obtained $10 million from this method.  He was then found in 1986 and sentenced to five years in prison.  He was released in 1991, but didn't return to Vegas headlines until 1996, when he returned, this time with a new approach in response to the higher levels of security.  He actually managed to keep his cheating secret until November 1998, when one of his accomplices revealed information about his cheating machines.  He was arrested and sentenced to 7.5 years in prison, being released in 2004.  He died in 2010 from unknown causes.

SLS station: SLS station (originally Sahara) is a station on the Las Vegas Monorail, in Las Vegas, Nevada, United States.  The station is a side platform located at the Sahara Hotel and Casino.  The Sahara Station could be reached in two ways: from inside the hotel via a hallway located behind the Casbar Theatre Lounge (closed on May 16, 2011) or from street level on Paradise Road behind the Sahara.  The tracks just north of Sahara station were designed to provide access to a possible downtown extension of the monorail via the northern portion of the Las Vegas Strip in the area of the Circus Circus Las Vegas and the Riviera.

Question: Harrah's & The Linq station is an island platform located between The Linq and a hotel and casino on the Las Vegas Strip that has over 1200 slot machines, and is owned and operated by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the monorail station."
    },
    "located_between": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Entities between which the station is located."
    },
    "identified_hotel_casino": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the hotel and casino identified by the description."
        },
        "slot_machines_count": {
          "type": "integer",
          "description": "The number of slot machines at the identified hotel and casino."
        },
        "owner_operator": {
          "type": "string",
          "description": "The owner and operator of the identified hotel and casino."
        }
      },
      "required": [
        "name",
        "slot_machines_count",
        "owner_operator"
      ],
      "additionalProperties": false
    },
    "owner_operator_of_identified_hotel": {
      "type": "string",
      "description": "The owner and operator of the hotel and casino that fits the description."
    }
  },
  "required": [
    "station_name",
    "located_between",
    "identified_hotel_casino",
    "owner_operator_of_identified_hotel"
  ],
  "additionalProperties": false
}
