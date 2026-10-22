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
Tropicana – Las Vegas Boulevard intersection: The Tropicana – Las Vegas Boulevard intersection on the Las Vegas Strip (Tropicana Avenue and Las Vegas Boulevard), is noteworthy for several reasons.  It was the first intersection in Las Vegas completely closed to street level pedestrian traffic and its four corners are home to four major resorts: Excalibur Hotel and Casino, Tropicana Las Vegas, New York-New York Hotel and Casino and MGM Grand Las Vegas—the latter has 5,044 rooms and was once the largest hotel in the world.  The resorts at the four corners have a total of 12,536 hotel rooms as of 2016.

Hooters Casino Hotel: Hooters Casino Hotel is a hotel and casino located off the Las Vegas Strip in Paradise, Nevada, United States.  It is owned by Trinity Hotel Investors and operated by the Navegante Group.  It is located off the Strip next to the Tropicana and across the street from the MGM Grand Las Vegas.  The hotel has 696 rooms with a 35000 sqft casino.

CityCenter: CityCenter (also known as CityCenter Las Vegas) is a 16797000 sqft mixed-use, urban complex on 76 acre located on the Las Vegas Strip in Paradise, Nevada.  The project was started by MGM Resorts International; Dubai World became a joint partner during the project's construction phase.  It is the largest privately funded construction project in the history of the United States.  The project is connected by a people mover system to adjacent MGM properties Monte Carlo Las Vegas and Bellagio Las Vegas.  As of 2015, the "CityCenter" branding has been largely retired, with the focus instead on the Aria brand of the development's centerpiece property in names such as the "Aria Express" (formerly "CityCenter Tram") and "Aria Art Collection" (formerly "CityCenter Art Collection").

Westgate Las Vegas Resort &amp; Casino: The Westgate Las Vegas Resort & Casino is a hotel and casino in Winchester, Nevada.  It is owned by Westgate Resorts and operated by Navegante Group.  It has 2,956 hotel rooms including 305 suites.  It opened in 1969 as the International Hotel, and was known for many years as the Las Vegas Hilton, then briefly as the LVH – Las Vegas Hotel and Casino.  It was renamed the Westgate Las Vegas on July 1, 2014.

El Rancho Vegas: El Rancho Vegas was a hotel and casino on the Las Vegas Strip.  It was located at 2500 Las Vegas Boulevard, at the southwest corner of Las Vegas Boulevard and Sahara Avenue, and opened on April 3, 1941.  Until 1942, it was the largest hotel in Las Vegas with 110 rooms.  On June 17, 1960, the hotel was destroyed by fire.  In 1982, the El Rancho Hotel and Casino formerly known as the Thunderbird and later as the Silverbird opened across the street from the former site of the El Rancho Vegas, creating some confusion.

Bally's Las Vegas: Bally's Las Vegas (formerly MGM Grand Hotel and Casino) is a hotel and casino on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by Caesars Entertainment Corporation.  The hotel features 2,814 extra-sized guestrooms that are 450 sqft or larger and over 175000 sqft of banquet and meeting space.  The casino occupies 66187 sqft .  About 75% of the rooms are in the Indigo Tower, and were renovated in 2004.  The remaining rooms are located in the Jubilee Tower, constructed in 1981.

Holy Cow Casino and Brewery: Holy Cow!  Casino and Brewery (formerly Foxy's Firehouse) was a locals casino and microbrewery on South Las Vegas Boulevard, north of the Las Vegas Strip, in Las Vegas, Nevada.  The property began in 1955 as Foxy's Deli, which operated until its closure in 1975.  A year later, the building was reopened as a casino named Foxy's Firehouse, which later closed in 1988.  Tom "Big Dog" Wiesner purchased the building and reopened it as the Holy Cow casino in 1992.  Wiesner added a microbrewery the following year, making the Holy Cow the first brewery to open in Las Vegas.  Wiesner persuaded the state to change its laws that had prohibited breweries from operating in Las Vegas.

Echelon Place: Echelon Place was an unfinished hotel, casino, shopping, and convention complex on the Las Vegas Strip, developed by Boyd Gaming.  It was to be a multi-use project on 87 acre with a 140000 sqft casino, 4 hotels providing 5,300 rooms, 25 restaurants and bars, and the 650000 sqft Las Vegas ExpoCenter.  Echelon Place would have been a 3,300 room hotel owned and operated by Boyd; other hotels were expected to be a Shangri-La Hotel, a Delano Hotel, a Mondrian Hotel, and the Echelon Tower.

Monte Carlo Resort and Casino: The Monte Carlo Resort and Casino is a megaresort hotel and casino on the Las Vegas Strip in Paradise, Nevada, United States.  The hotel, with a height of 360 ft , has 32 floors, featuring a 102000 sqft casino floor with 1,400 slot machines, 60 table games, and 15 poker tables.  It is owned and operated by MGM Resorts International.  The hotel offers 2,992 guest rooms, including 259 luxury suites.  It is being converted from late 2016 to 2018 into the Park MGM, with the upper floors converted into a boutique hotel, NoMad Las Vegas.

MGM Grand Las Vegas: The MGM Grand Las Vegas (formerly Marina and MGM-Marina) is a hotel and casino located on the Las Vegas Strip in Paradise, Nevada.  The MGM Grand is the largest single hotel in the United States with 5,124 rooms.  It is also the third-largest hotel complex in the world by number of rooms and second-largest hotel resort complex in the United States behind the combined The Venetian and The Palazzo.  When it opened in 1993, the MGM Grand was the largest hotel complex in the world.

Question: How many guest rooms are offered in the megaresort hotel and casino adjacent to CityCenter on the Las Vegas Strip?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "hotel_name": {
      "type": "string",
      "description": "The name of the megaresort hotel and casino."
    },
    "is_megaresort": {
      "type": "boolean",
      "description": "Indicates if the property is a megaresort."
    },
    "is_adjacent_to_citycenter": {
      "type": "boolean",
      "description": "Indicates if the property is adjacent to CityCenter."
    },
    "guest_room_count": {
      "type": "integer",
      "description": "The total number of guest rooms offered by the hotel."
    },
    "suite_count": {
      "type": "integer",
      "description": "The number of luxury suites included in the guest room count."
    }
  },
  "required": [
    "hotel_name",
    "is_megaresort",
    "is_adjacent_to_citycenter",
    "guest_room_count"
  ],
  "additionalProperties": false
}
