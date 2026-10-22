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
David Lukaszewski: David Lukaszewski (born 1970) is an American poker player.  He was a Poker Room Shift Manager at the Desert Diamond Casino who won a bracelet in the 2003 Casino Employees Championship event at the World Series of Poker.  The Casino Employees Championship event was the first time that Lukaszewski had played in a tournament with a buy-in greater than $50.  At the start of 2003, Lukaszewski set the modest goal of competing in a major poker tournament and at the last minute, he and several friends decided to drive to Las Vegas to play in the WSOP.  Lukaszewski won the entry to the event by winning a $65 single-table satellite at Binion's Horseshoe.  When the tournament reached the final three players, they started shooting Kamikaze's.  "We were all having such a great time, sitting around playing poker that I think we may have forgotten about the prize money and the bracelet."

High Roller (Valleyfair): High Roller is a wooden roller coaster located at Valleyfair in Shakopee, Minnesota.  High Roller is Valleyfair's oldest roller coaster, being built in 1976 when the park opened.  It is an out-and-back type coaster, and is 70 feet (21 m) at the highest peak with a top speed of 50 mph (80 km/h).

Super High Roller Bowl: The Super High Roller Bowl is an annual high stakes No Limit Hold'em poker tournament that takes place at the Aria Resort and Casino in Las Vegas, Nevada.  The first edition of the event was held in July 2015 and featured a $500,000 buy-in, drawing a field of 43 players.  Brian Rast won the inaugural tournament, earning $7,525,000.  For its second year the tournament was moved to May and the buy-in was lowered to $300,000.  Entries increased to 49 and Rainer Kempe captured the first prize of $5,000,000.  The website Poker Central sponsors the event and features a live stream throughout the duration of the tournament.

High Roller (Stratosphere): The High Roller (also known as the Let it Ride High Roller), was a steel roller coaster constructed on top of a building 909 ft over the Las Vegas Strip.  It was the highest roller coaster in the world when compared to the surrounding terrain.  It was located on top of the Stratosphere Tower, Las Vegas, Nevada, which is the tallest free-standing observation tower in the United States.  The coaster was manufactured by S&MC GmbH Structures and Machines.

Full Tilt Poker Championship at Red Rock: Full Tilt Poker Championship at Red Rock (also FullTiltPoker.Net Championship at Red Rock) was a seven-week televised shootout poker tournament played at the Red Rock Resort Spa and Casino in Summerlin near Las Vegas, Nevada.  The tournament was sponsored by online poker website Full Tilt Poker and aired by Fox Sports Net.  In each of the first six episodes, six professional poker player affiliated with Full Tilt Poker played a single-table freezeout tournament.  The winner of each freezeout won US$25,000 and advanced to the seven-handed final table.  The seventh seat at the final table was filled by Stefan Rehn, an Internet qualifier.  Tournaments featured a speed poker format, with players having 30 seconds to act on their hands with one 60-second time extension per match.

Scott Seiver: Scott Seiver (born April 14, 1985 in Columbus, Ohio) is a professional poker player from Cold Spring Harbor, New York, now residing in Las Vegas, Nevada who won the 2008 World Series of Poker $5,000 No Limit Hold'em event and is the winner of the $25,100 buy-in High Roller event at the 2010 L.A. Poker Classic.

Fedor Holz: Fedor Holz (born 25 July 1993) is a German professional poker player from Saarbrücken who focuses on high roller tournaments.  He is widely regarded as one of the best online and live tournament poker players in the modern era.  He was ranked by Pocketfives as best online MTT player in 2014 and 2015.  In July 2016, he won his first World Series of Poker bracelet in the $111,111 High Roller For One Drop, winning $4,981,775.  He is currently the 5th-highest ranked live tournament player on the Global Poker Index.

Las Vegas Uncork'd: Las Vegas Uncork'd (also referred to as Vegas Uncork'd and Vegas Uncorked) is an annual culinary and wine event in Las Vegas, Nevada.  The concept was developed by the Las Vegas Convention and Visitors Authority, their advertising agency R&R Partners and Las Vegas resort partners who originally considered a number of magazine partners such as Bon Appetit, Food & Wine and Gourmet.  Bon Appetit was selected as the magazine partner after a review with each magazine.  The event was launched in 2007 by the Las Vegas Convention and Visitors Authority, "Bon Appétit" magazine led by Editor-in-Chief Barbara Fairchild and co-creator and Executive Director Rob O'Keefe who led the first five years of development of what Eater.com called "the world's most innovative culinary event".  Las Vegas resort partners over the years include Bellagio, Caesars Palace and Wynn Las Vegas, MGM Grand, Mandalay Bay, The Venetian, Las Vegas and The Palazzo and each year the event features more than 80 celebrated chefs and over 25 events occurring over a spectacular four-day weekend.

Fabrice Soulier: Fabrice Soulier (born April 23, 1969 in Avignon, France) is a professional poker player with over $5.5 Million in live poker tournament winnings and won his first bracelet in the 2011 World Series of Poker $10,000 H.O.R.S.E. Championship.In 2013 he was the runner up in the 2013 World Series of Poker Europe € 10,000 + 450 No Limit Hold'em - Main Event (Event #6), Earning him € 610,000 ($ 824,513). In March 2014, Fabrice took down the € 10,000 + 300 No Limit Hold'em EPT High Roller event for €392,900 ($542,342).

Aria Resort and Casino: Aria Resort and Casino is a luxury resort and casino, part of the CityCenter complex on the Las Vegas Strip in Paradise, Nevada.  Aria consists of two curved glass and steel highrise towers adjoined at the center.  It opened on December 16, 2009 as a joint venture between MGM Resorts International and Infinity World Development.  At 4000000 sqft and 600 ft in height, it is the largest and tallest structure at CityCenter.

Question: The Super High Roller Bowl poker tournament in Las Vegas takes place at a resort that was opened in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "tournament_name": {
      "type": "string",
      "description": "The name of the poker tournament."
    },
    "venue": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the resort and casino where the tournament takes place."
        },
        "city": {
          "type": "string",
          "description": "The city where the venue is located."
        },
        "opening_year": {
          "type": "integer",
          "description": "The year the venue opened."
        }
      },
      "required": [
        "name",
        "city",
        "opening_year"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "integer",
      "description": "The opening year of the resort where the tournament is held."
    }
  },
  "required": [
    "tournament_name",
    "venue",
    "answer"
  ],
  "additionalProperties": false
}
