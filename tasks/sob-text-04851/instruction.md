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
MGM Macau: MGM Macau (; formerly known as MGM Grand Macau) is a 35-story, 600-room casino resort in Sé, Macau.  Under a sub concession approved by the Macau government, the project is owned and operated as a 50–50 joint venture between MGM Resorts International and Pansy Ho, daughter of Macau casino magnate Stanley Ho.  The sub-concession is one of several examples of new casino construction following the end of the government-granted monopoly held for decades by Stanley Ho.

Mandalay Resort Group: Mandalay Resort Group (formerly Circus Circus Enterprises) was a hotel-casino operator based in Paradise, Nevada.  Its major properties included Mandalay Bay, Luxor, Excalibur and Circus Circus, as well as half of the Monte Carlo.  In terms of market capitalization, it was one of the largest casino operators in the world.  Its stock traded on the New York Stock Exchange with the ticker symbol "CIR" and "MBG".

Corey I. Sanders: Corey Sanders has served as Chief Operating Officer of MGM Resorts International since June 2010.  He oversees operations at the Company’s wholly owned properties, which in Nevada include Bellagio (resort), MGM Grand Las Vegas, Mandalay Bay, The Mirage, New York-New York Hotel and Casino, Monte Carlo Resort and Casino, Luxor Las Vegas, Excalibur Hotel and Casino, Circus Circus Las Vegas, Circus Circus Reno, Gold Strike Jean and Railroad Pass Casino.  He also oversees Beau Rivage (Mississippi) in Biloxi and Gold Strike Tunica, both in Mississippi, as well as MGM Grand Detroit.

Borgata: Borgata Hotel Casino & Spa is a hotel, casino, and spa in Atlantic City, New Jersey, United States.  It is owned and operated by MGM Resorts International.  The casino hotel features 2,002 rooms and is the largest hotel in New Jersey.  Borgata opened in July 2003 and is the top-grossing casino in Atlantic City.

Monte Carlo Resort and Casino: The Monte Carlo Resort and Casino is a megaresort hotel and casino on the Las Vegas Strip in Paradise, Nevada, United States.  The hotel, with a height of 360 ft , has 32 floors, featuring a 102000 sqft casino floor with 1,400 slot machines, 60 table games, and 15 poker tables.  It is owned and operated by MGM Resorts International.  The hotel offers 2,992 guest rooms, including 259 luxury suites.  It is being converted from late 2016 to 2018 into the Park MGM, with the upper floors converted into a boutique hotel, NoMad Las Vegas.

MGM Growth Properties: MGM Growth Properties LLC is a real estate investment trust that invests in large-scale destination entertainment and leisure resorts.  As of December 31, 2016, the company owned 11 properties operated by MGM Resorts International, comprising 27,233 hotel rooms.  The company leases the properties to MGM Resorts International via NNN Leases for an annual payment of $745 million.

MGM Springfield: MGM Springfield is a $950 million resort casino under construction in Springfield, Massachusetts.  The casino, which is scheduled to open in 2018, will be owned and operated by MGM Resorts International.

MGM Resorts International: MGM Resorts International is a global hospitality and entertainment company operating destination resorts in Las Vegas, Mississippi, New Jersey and Detroit, including Bellagio, MGM Grand, Mandalay Bay and The Mirage.  The company recently opened MGM National Harbor in Maryland and is developing MGM Springfield in Massachusetts.  It has a majority interest in MGM China Holdings Limited, which owns the MGM Macau resort and casino and is developing a gaming resort in Cotai.  MGM Resorts owns 50 percent of CityCenter in Las Vegas, which features ARIA Resort & Casino.  It has a majority controlling interest in MGM Growth Properties, a real estate investment trust.

Mandalay Bay: Mandalay Bay is a 43-story luxury resort and casino on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by MGM Resorts International.  One of the property's towers operates as the Delano; the Four Seasons Hotel is independently operated within the Mandalay Bay tower, occupying 5 floors (35–39).

WinStar World Casino: WinStar World Casino and Resort is a hotel and casino located near the Oklahoma–Texas state line, 1 mi north of the Red River, at Exit 1 off Interstate 35 and Winstar Boulevard in Thackerville, Oklahoma.  The casino opened as the WinStar Casino in 2004, and was expanded (with a 395-room hotel tower) and renamed the WinStar World Casino in 2009, with its 519000 sqft of casino floor making it the largest casino in the state of Oklahoma.  In August 2013, WinStar Resorts completed a major expansion project, which added a new 1000-room second hotel tower that was divided into two phases; this also added a new casino that is attached to the tower.  As a result of the completion of this expansion, the casino overtook Foxwoods Resort Casino to become the largest casino in the United States based on gaming floor space.  WinStar has over 7,400 electronic games, 46 table poker rooms, 99 total table games, Racer's off-track betting, High Limit Room, keno, and bingo.

Question: What resort and casino owned and operated by MGM Resorts International, included in the largest casino operators in the world?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "resort_casino_name": {
      "type": "string",
      "description": "The name of the resort and casino."
    },
    "current_owner_operator": {
      "type": "string",
      "description": "The company that currently owns and operates the resort and casino."
    },
    "was_part_of_large_operator_group": {
      "type": "boolean",
      "description": "Indicates if the resort was part of a group considered one of the largest casino operators."
    },
    "previous_operator_group_name": {
      "type": "string",
      "description": "The name of the previous operator group that was among the largest."
    },
    "previous_operator_group_status": {
      "type": "string",
      "description": "Description of the previous operator group's status in the industry."
    },
    "location": {
      "type": "string",
      "description": "The geographical location of the resort and casino."
    },
    "number_of_stories": {
      "type": "integer",
      "description": "The number of stories in the resort's main building."
    }
  },
  "required": [
    "resort_casino_name",
    "current_owner_operator",
    "was_part_of_large_operator_group",
    "previous_operator_group_name",
    "previous_operator_group_status",
    "location",
    "number_of_stories"
  ],
  "additionalProperties": false
}
