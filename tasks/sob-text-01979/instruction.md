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
Jack Lambert (footballer): Jack Lambert (22 May 1902 – 7 December 1940) was an English footballer who played as a striker.  Lambert featured for clubs, Leeds United, Doncaster Rovers, Arsenal & Fulham in his playing career.  He went on to coach at clubs Margate as well as Arsenal.  Lambert is also Arsenal's joint highest hattrick scorer of all time.

Lira Motorsports: Lira Motorsports is an American professional stock car racing team that last competed in the NASCAR Camping World Truck Series, and the ARCA Racing Series.  Owned by Carlos and Amanda Lira, the team made its debut in the ARCA Racing Series in 2015, fielding multiple cars and drivers throughout the year.  The team made its Camping World Truck Series debut on November 20, 2015 at Homestead-Miami Speedway.  Lira Motorsports also fields cars in NASCAR Whelen All-American Late Model Series competition.  Lira Motorsports is a driver development satellite team for Roush Fenway Racing.

Joe Schobert: Joe Schobert (born November 6, 1993) is an American football middle linebacker for the Cleveland Browns of the National Football League (NFL).  He was selected by the Browns in the fourth round during the 2016 NFL Draft.  Schobert played college football at the University of Wisconsin-Madison where he won the Jack Lambert Trophy in 2015 as the nation's best linebacker.

Turner Scott Motorsports: Turner Scott Motorsports (TSM), formerly Turner Motorsports was an American professional stock car racing team that last competed in the NASCAR Sprint Cup Series, the Nationwide Series, the Camping World Truck Series, the K&N Pro Series East and the ARCA Racing Series.  The team was based in Mooresville, North Carolina co-owned by Texas businessman Steve Turner and North Carolina businessman Harry Scott Jr..  The team fielded cars in the NASCAR Xfinity Series, Camping World Truck Series and K&N Pro Series East, utilizing Hendrick Motorsports engines.  Co-owner Scott also owned the unaffiliated Sprint Cup Series team HScott Motorsports.

M-10000: The Union Pacific Railroad's M-10000, delivered to the railroad on February 12, 1934, at a cost of $230,997, was the first internal combustion engine, lightweight streamlined express passenger train built in the United States.  The M-10000 featured a turret cab, an inward-slanting Duralumin body with a nose formed of parabolic arches, and large nose air intakes on each side of the centerline.  The prime mover was a 600 hp Winton 191-A V12 distillate engine.  This engine design was unrelated to the later 201 or 201A Winton diesels.  There were three cars: a driving, power and baggage car at the front; and two passenger cars.  The 204 ft long, 85 ST train was fully articulated, with trucks shared between cars.  The front truck carried one General Electric traction motor per axle, and was the only one powered.  The train was painted in Armour Yellow with Leaf Brown roof and undersides.  Later, the area around the front air intake was also painted yellow.  Dividing lines of red separated the colors.

Fred Gehrke: Clarence Fred Gehrke (April 24, 1918 – February 9, 2002) was an American football player and executive.  He played in the National Football League (NFL) for the Cleveland / Los Angeles Rams, San Francisco 49ers and Chicago Cardinals from 1940 through 1950.  To boost team morale, Gehrke designed and painted the Los Angeles Rams logo in 1948, which was the first painted on the helmets of an NFL team.  He later served as the general manager of the Denver Broncos from 1977 through 1981.  He is the great-grandfather of Miami Marlin Christian Yelich

SBIII Motorsports: SBIII Motorsports is a former NASCAR Cup Series motor racing team.  The team was owned by Pittsburgh, Pennsylvania businessman Scott Barbour and fielded the No. 58 Ford Taurus during the 1999 NASCAR Winston Cup Series season.  The team was named for Barbour's son (Scott Barbour III) and was painted black and yellow in honor of former Pittsburgh Steelers player Jack Lambert.

Jack Lambert (American football): John Harold Lambert (born July 8, 1952) is a former American football linebacker who played in the National Football League (NFL).  Recognized by the Pro Football Hall of Fame in 1990 as "the premier linebacker of his era," Lambert was the starting middle linebacker for four Super Bowl-winning teams during an 11-year career with the Pittsburgh Steelers.

1974 Pittsburgh Steelers season: The 1974 Pittsburgh Steelers season was capped off with a 10-3-1 record and the Super Bowl IX championship.  The '74 team became the first team in Steelers history (42 seasons) to win a league title following one of the franchise's greatest playoff runs ever.  After the hiring of head coach Chuck Noll in 1969, Noll signed Defensive Tackle #75 Joe Greene.  He then signed Quarterback #12 Terry Bradshaw in 1970.  Linebacker #59 Jack Ham and Cornerback #47 Mel Blount arrived in 1971.  And in 1972, the Steelers signed a fullback from nearby Penn.  State in Franco Harris.  By 1973, Joe Greene was flanked on the line by Dwight White, Ernie Holmes, and L. C. Greenwood.  In the 1974 draft, the Steelers took no time in signing some more talent for the team.  Wide Receiver #88 Lynn Swann and #82 John Stallworth, Linebacker Jack Lambert, and Center Mike Webster all became future hall of famers.

Deyangshar: Deyangshar is the name given to the central open courtyard of a monastery in Tibet and parts of Myanmar where it is used for ceremonies, burning incense and prayer and to divide the living quarters from the temples of Buddhist prayer and study.  One such example is the Potala Palace of the Dalai Lama in Lhasa, where the great palacial monastery is divided into a white and a red palace with a yellow painted Deyangshar separating to two sectors.

Question: Which NFL team did Jack Lambert play for and thereby honors them with black and yellow painted cars for the SBill Motorsports cars?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the American football player."
    },
    "nfl_team": {
      "type": "string",
      "description": "The NFL team the player played for."
    },
    "motorsports_team_honoring_player": {
      "type": "string",
      "description": "The motorsports team that honored the player."
    },
    "car_colors_honoring_player": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The colors used on the motorsports cars to honor the player."
    }
  },
  "required": [
    "player_name",
    "nfl_team",
    "motorsports_team_honoring_player",
    "car_colors_honoring_player"
  ],
  "additionalProperties": false
}
