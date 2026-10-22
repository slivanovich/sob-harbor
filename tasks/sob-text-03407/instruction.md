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
Avi Resort &amp; Casino: Avi Resort & Casino is a hotel and casino located near the southern tip of Nevada on the banks of the Colorado River in Laughlin, Nevada next to Fort Mohave, Arizona.  Within walking distance of the California and Arizona borders, it is owned by the Fort Mojave Tribe and operated under an agreement with the state of Nevada.  It has a 465-room hotel, a 25000 sqft casino and a 260-space RV park with internet access.

SLS station: SLS station (originally Sahara) is a station on the Las Vegas Monorail, in Las Vegas, Nevada, United States.  The station is a side platform located at the Sahara Hotel and Casino.  The Sahara Station could be reached in two ways: from inside the hotel via a hallway located behind the Casbar Theatre Lounge (closed on May 16, 2011) or from street level on Paradise Road behind the Sahara.  The tracks just north of Sahara station were designed to provide access to a possible downtown extension of the monorail via the northern portion of the Las Vegas Strip in the area of the Circus Circus Las Vegas and the Riviera.

William G. Bennett (gaming executive): William G. Bennett (November 16, 1924-December 22, 2002) was an American gaming executive and real estate developer.  Noted for pioneering Las Vegas as a destination for middle-class tourists and their families, he is best remembered for his establishment of gaming giant Circus Circus Enterprises in 1974.  He served as chairman of Circus Circus between 1974 and 1994.  Under his leadership Circus Circus would go on to develop numerous additional properties throughout Nevada, including the Excalibur and Luxor casinos in Las Vegas.  Following his departure from Circus Circus, Bennett purchased the Sahara Hotel and Casino in Las Vegas in 1995 and operated it until his death in 2002.

Adventuredome: Adventuredome (formerly Grand Slam Canyon) is a 5 acre indoor amusement park located at Circus Circus in Las Vegas, Nevada, on the Las Vegas Strip.  The park is connected to the hotel inside a large glass dome, and currently offers 25 rides and attractions including the Canyon Blaster roller coaster, rock climbing wall, 18-hole miniature golf course, an video game arcade, clown shows, Xtreme Zone, Pikes Pass, Virtual Reality Zone, Midway Games, and carnival-type games.  Because the park is enclosed, it is not affected by cold, rainy, or windy weather, unlike most theme parks, and is open year-round.  Every October since 2003, the Adventuredome is changed to Fright Dome as a Halloween-themed theme park.

Hooters Casino Hotel: Hooters Casino Hotel is a hotel and casino located off the Las Vegas Strip in Paradise, Nevada, United States.  It is owned by Trinity Hotel Investors and operated by the Navegante Group.  It is located off the Strip next to the Tropicana and across the street from the MGM Grand Las Vegas.  The hotel has 696 rooms with a 35000 sqft casino.

Corey I. Sanders: Corey Sanders has served as Chief Operating Officer of MGM Resorts International since June 2010.  He oversees operations at the Company’s wholly owned properties, which in Nevada include Bellagio (resort), MGM Grand Las Vegas, Mandalay Bay, The Mirage, New York-New York Hotel and Casino, Monte Carlo Resort and Casino, Luxor Las Vegas, Excalibur Hotel and Casino, Circus Circus Las Vegas, Circus Circus Reno, Gold Strike Jean and Railroad Pass Casino.  He also oversees Beau Rivage (Mississippi) in Biloxi and Gold Strike Tunica, both in Mississippi, as well as MGM Grand Detroit.

Circus Circus Las Vegas: Circus Circus Las Vegas is a hotel, 123928 sqft casino, and RV park located on the Las Vegas Strip in Winchester, Nevada.  It is owned and operated by MGM Resorts International.  Circus Circus features circus acts and carnival type games daily on the Midway.

Monte Carlo Resort and Casino: The Monte Carlo Resort and Casino is a megaresort hotel and casino on the Las Vegas Strip in Paradise, Nevada, United States.  The hotel, with a height of 360 ft , has 32 floors, featuring a 102000 sqft casino floor with 1,400 slot machines, 60 table games, and 15 poker tables.  It is owned and operated by MGM Resorts International.  The hotel offers 2,992 guest rooms, including 259 luxury suites.  It is being converted from late 2016 to 2018 into the Park MGM, with the upper floors converted into a boutique hotel, NoMad Las Vegas.

Las Vegas Festival Grounds: Las Vegas Festival Grounds (formerly MGM Resorts Festival Grounds) is a 33 acre open-air venue located on the Las Vegas Strip, north of the MGM-owned Circus Circus Hotel and Casino in Winchester, Nevada.

Mandalay Resort Group: Mandalay Resort Group (formerly Circus Circus Enterprises) was a hotel-casino operator based in Paradise, Nevada.  Its major properties included Mandalay Bay, Luxor, Excalibur and Circus Circus, as well as half of the Monte Carlo.  In terms of market capitalization, it was one of the largest casino operators in the world.  Its stock traded on the New York Stock Exchange with the ticker symbol "CIR" and "MBG".

Question: Mandalay Resort Group (formerly Circus Circus Enterprises) was a hotel-casino operator based in Paradise, Nevada, one of its major properties included which hotel, 123928 sqft casino, and RV park located on the Las Vegas Strip in Winchester, Nevada?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "property_name": {
      "type": "string",
      "description": "The name of the hotel and casino property."
    },
    "property_type": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Types of facilities offered by the property."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the property is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the property is located."
        },
        "strip_location": {
          "type": "string",
          "description": "Specific location on the Las Vegas Strip."
        }
      },
      "required": [
        "city",
        "state",
        "strip_location"
      ],
      "additionalProperties": false
    },
    "casino_details": {
      "type": "object",
      "properties": {
        "square_footage": {
          "type": "integer",
          "description": "The total square footage of the casino."
        }
      },
      "required": [
        "square_footage"
      ],
      "additionalProperties": false
    },
    "former_owner_group": {
      "type": "string",
      "description": "The group that formerly owned the property as per the question context."
    }
  },
  "required": [
    "property_name",
    "property_type",
    "location",
    "casino_details",
    "former_owner_group"
  ],
  "additionalProperties": false
}
