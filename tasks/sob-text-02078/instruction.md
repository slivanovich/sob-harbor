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
Echelon Place: Echelon Place was an unfinished hotel, casino, shopping, and convention complex on the Las Vegas Strip, developed by Boyd Gaming.  It was to be a multi-use project on 87 acre with a 140000 sqft casino, 4 hotels providing 5,300 rooms, 25 restaurants and bars, and the 650000 sqft Las Vegas ExpoCenter.  Echelon Place would have been a 3,300 room hotel owned and operated by Boyd; other hotels were expected to be a Shangri-La Hotel, a Delano Hotel, a Mondrian Hotel, and the Echelon Tower.

WinStar World Casino: WinStar World Casino and Resort is a hotel and casino located near the Oklahoma–Texas state line, 1 mi north of the Red River, at Exit 1 off Interstate 35 and Winstar Boulevard in Thackerville, Oklahoma.  The casino opened as the WinStar Casino in 2004, and was expanded (with a 395-room hotel tower) and renamed the WinStar World Casino in 2009, with its 519000 sqft of casino floor making it the largest casino in the state of Oklahoma.  In August 2013, WinStar Resorts completed a major expansion project, which added a new 1000-room second hotel tower that was divided into two phases; this also added a new casino that is attached to the tower.  As a result of the completion of this expansion, the casino overtook Foxwoods Resort Casino to become the largest casino in the United States based on gaming floor space.  WinStar has over 7,400 electronic games, 46 table poker rooms, 99 total table games, Racer's off-track betting, High Limit Room, keno, and bingo.

Alon Las Vegas: The Alon Las Vegas was an upcoming luxury hotel and casino located on the Las Vegas Strip in Paradise, Nevada.  It was located on the site of the former New Frontier Hotel and Casino, near the Wynn Las Vegas and the Fashion Show Mall.

Wynn Las Vegas: Wynn Las Vegas, often simply referred to as Wynn, is a luxury resort and casino located on the Las Vegas Strip in Paradise, Nevada.  The US$2.7-billion resort is named after casino developer Steve Wynn and is the flagship property of Wynn Resorts.  The resort covers 215 acre .  It is located at the northeast corner of Las Vegas Boulevard and Sands Avenue, directly across The Strip from the Fashion Show Mall.

Gold Coast Hotel and Casino: The Gold Coast Hotel & Casino is a hotel and casino located in Paradise, Nevada.  This locals' casino is owned and operated by Boyd Gaming.  The Gold Coast is located one mile (1.6 km) west of the Las Vegas Strip on West Flamingo Road.  It is located across the street from the Palms Casino Resort and the Rio All Suite Hotel and Casino.

O'Sheas Casino: O'Sheas Casino is a casino located within The Linq on the Las Vegas Strip in Paradise, Nevada.  As part of The Linq, it is owned and operated by Caesars Entertainment Corporation and is connected on the exterior to a shopping/dining promenade, also owned by Caesars.  The revitalized O'Sheas has three bars - the main Dublin Up Bar, the Lucky Bar and the exterior-facing Blarney Bar.  The casino includes beer pong tables, a stage, a dance floor and a pit with games including blackjack, roulette, and craps.

SLS Las Vegas: The SLS Hotel & Casino Las Vegas (formerly Sahara Hotel and Casino) is a hotel and casino located on the Las Vegas Strip in Winchester, Nevada.  It is owned by Stockbridge Real Estate but is under contract to be purchased by Alex Meruelo and Meruelo Group (owners of the Grand Sierra Resort Hotel & Casino in Reno) with an expected closing date of Q3 2017.

The Linq: The Linq (formerly Flamingo Capri, Imperial Palace and The Quad) is a 2,640-room hotel, casino and shopping promenade on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by Caesars Entertainment Corporation.  As of 2012, the casino is 32890 sqft with 830 slot machines, 55 table games, and a race and sports book.

Hooters Casino Hotel: Hooters Casino Hotel is a hotel and casino located off the Las Vegas Strip in Paradise, Nevada, United States.  It is owned by Trinity Hotel Investors and operated by the Navegante Group.  It is located off the Strip next to the Tropicana and across the street from the MGM Grand Las Vegas.  The hotel has 696 rooms with a 35000 sqft casino.

Tropicana – Las Vegas Boulevard intersection: The Tropicana – Las Vegas Boulevard intersection on the Las Vegas Strip (Tropicana Avenue and Las Vegas Boulevard), is noteworthy for several reasons.  It was the first intersection in Las Vegas completely closed to street level pedestrian traffic and its four corners are home to four major resorts: Excalibur Hotel and Casino, Tropicana Las Vegas, New York-New York Hotel and Casino and MGM Grand Las Vegas—the latter has 5,044 rooms and was once the largest hotel in the world.  The resorts at the four corners have a total of 12,536 hotel rooms as of 2016.

Question: O'Sheas Casino is a casino located within The Linq, a 2,640-room hotel, casino and shopping promenade on the Las Vegas Strip in Paradise, in which state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "casino_name": {
      "type": "string",
      "description": "The name of the casino in question."
    },
    "parent_resort_name": {
      "type": "string",
      "description": "The name of the resort where the casino is located."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the casino is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the casino is located."
        },
        "on_las_vegas_strip": {
          "type": "boolean",
          "description": "Indicates if the casino is located on the Las Vegas Strip."
        }
      },
      "required": [
        "city",
        "state",
        "on_las_vegas_strip"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "casino_name",
    "parent_resort_name",
    "location_details"
  ],
  "additionalProperties": false
}
