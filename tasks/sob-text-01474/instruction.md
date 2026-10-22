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
Adventuredome: Adventuredome (formerly Grand Slam Canyon) is a 5 acre indoor amusement park located at Circus Circus in Las Vegas, Nevada, on the Las Vegas Strip.  The park is connected to the hotel inside a large glass dome, and currently offers 25 rides and attractions including the Canyon Blaster roller coaster, rock climbing wall, 18-hole miniature golf course, an video game arcade, clown shows, Xtreme Zone, Pikes Pass, Virtual Reality Zone, Midway Games, and carnival-type games.  Because the park is enclosed, it is not affected by cold, rainy, or windy weather, unlike most theme parks, and is open year-round.  Every October since 2003, the Adventuredome is changed to Fright Dome as a Halloween-themed theme park.

T-Mobile Arena: T-Mobile Arena is a multi-use indoor arena on the Las Vegas Strip in Paradise, Nevada.  Opened on April 6, 2016, the arena is a joint venture between MGM Resorts International and the Anschutz Entertainment Group.

Kiva Dunes: Kiva Dunes is a public golf course located in Baldwin County, just west of Gulf Shores, Alabama.  The course was designed by professional golfer Jerry Pate, and was immediately ranked #2 in Golf Digest's "Best New Public Course (US)" when it opened in 1995.  More recently, the publication ranked the course #58 on "America’s 100 Greatest Public Courses".  GolfLink currently lists Kiva Dunes as one of the best golf course in the state  and it is ranked #44 in Golf Week's "Top 100 Resort Courses" and #76 in their "Top 100 Residential Courses".

Kananaskis Country Golf Course: Kananaskis Country Golf Course is a publicly accessible world-renowned 36-hole golf course situated in Kananaskis Country, a park system west of Calgary, Alberta, Canada in the foothills and front ranges of the Canadian Rockies which opened in 1983 at a cost of $25.5 million.  The golf course near Kananaskis Village, Alberta designed by the golf course architect Robert Trent Jones, consists of two 18-hole golf layouts, played beneath Mt.Lorette and Mt.Kidd, after which the courses are respectively named.  "Score Golf Magazine" has consistently ranked this facility as a top 100 course in Canada.  Kananaskis Country Golf Course is part of the collection of seven golf courses and resorts in Alberta, the Canadian Rockies Golf – "the most storied and recognized group of golf courses in Canada."  About sixty thousand rounds of golf were played there annually with eighty-five percent played by Albertans.  The golf course includes the pro-shop, club house, tournament centre and other golf course buildings which were valued at $15 million in 2015.  During the June 2013 Alberta floods, Kananaskis Country "sustained the most extensive damage in its 36-year history."  The Alberta government committed $18 million to rebuild the Course and to protect it from future flood damage.

Dunes (hotel and casino): The Dunes Hotel was a hotel and casino on the Las Vegas Strip in Paradise, Nevada, that operated from May 23, 1955 to January 26, 1993.  Designed by architect Maxwell Starkman, it was the tenth resort to open on the Strip.  Bellagio now stands on the former grounds.  The Dunes golf course is now occupied by parts of Monte Carlo, New York-New York, CityCenter, and Cosmopolitan, and T-Mobile Arena.

Arlington Hotel Open: The Arlington Hotel Open was a PGA Tour event that was played from 1955 to 1963 at the Arlington golf course of the Hot Springs Country Club near the Arlington Hotel, now known as the Arlington Resort Hotel and Spa, a 484-room resort in the Ouachita Mountains of Hot Springs National Park in Arkansas.  The event was also known as the Hot Springs Open or Hot Springs Open Invitational.  The Majestic Golf Course was constructed by Willie Park, Jnr.  in 1898.  The Arlington Golf Course was designed and built by William Diddle in 1927.  Golf legend Jimmy Demaret won the last of his 31 PGA Tour wins at this event in 1957.

Mystic Dunes Golf Club: Mystic Dunes Golf Club is a resort style golf course in Celebration, Florida designed by Gary Koch.  Par is 71.  The course measures 7012 yards long from the back tees.  Its signature hole is the 177 yard par 3 #2, with a waterfall to the left of the green.  The golf club resides on the Mystic Dunes Resort & Golf Club timeshare resort owned by Diamond Resorts International, and was previously known as the "Wyndham Palms Resort and Country Club".

Bellagio (resort): Bellagio is a resort, luxury hotel and casino on the Las Vegas Strip in Paradise, Nevada.  It is owned and operated by MGM Resorts International and was built on the site of the demolished Dunes hotel and casino.  Inspired by the Lake Como town of Bellagio in Italy, Bellagio is famed for its elegance.  One of its most notable features is an 8 acre lake between the building and the Strip, which houses the Fountains of Bellagio, a large dancing water fountain synchronized to music.

Barnbougle Dunes: Barnbougle Dunes Golf Links is a golf course located near the seaside village of Bridport in Tasmania's North-East.  The 18 hole championship layout was designed by course architects Tom Doak and Mike Clayton, and is set among sand dunes overlooking Bass Strait.  The course has been highly rated since opening in 2005, recognised as Australia's number one public access course, and fifth best course of any sort in Australia.  Barnbougle Dunes is the first new Australian course to enter the World's Top 100 courses since rankings began, coming in at 49 after its first appraisal.  It has since improved to be ranked the 35th best course in the world, and is ranked the 12th best links course in the world.

Dakota Dunes Casino: Dakota Dunes Casino, is a casino located on land belonging to the Whitecap Dakota First Nation, south of Saskatoon, Saskatchewan, Canada along Saskatchewan Highway 219.  The 84,000 sq. ft facility includes a Casino (with 500 slot machines, 14 table games), multi-purpose rooms, and restaurant opened in 2007 at a cost of $27 Million Canadian.  The casino is attached to the Dakota Dunes Golf Links 18 hole Golf Course.

Question: Name the multi-use indoor arena on the Las Vegas Strip which occupies The Dunes golf course, part of The Dunes Hotel, the tenth resort to open on the strip?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "arena_name": {
      "type": "string",
      "description": "The name of the multi-use indoor arena."
    },
    "location": {
      "type": "string",
      "description": "The specific location of the arena."
    },
    "occupies_dunes_golf_course": {
      "type": "boolean",
      "description": "Indicates if the arena occupies part of The Dunes golf course."
    },
    "dunes_hotel_details": {
      "type": "object",
      "properties": {
        "hotel_name": {
          "type": "string",
          "description": "The name of The Dunes Hotel."
        },
        "opening_rank_on_strip": {
          "type": "integer",
          "description": "The rank of The Dunes Hotel's opening on the Las Vegas Strip."
        },
        "operated_from_year": {
          "type": "integer",
          "description": "The year The Dunes Hotel began operation."
        },
        "operated_to_year": {
          "type": "integer",
          "description": "The year The Dunes Hotel ceased operation."
        }
      },
      "required": [
        "hotel_name",
        "opening_rank_on_strip",
        "operated_from_year",
        "operated_to_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "arena_name",
    "location",
    "occupies_dunes_golf_course",
    "dunes_hotel_details"
  ],
  "additionalProperties": false
}
