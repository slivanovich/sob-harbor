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
Geoff Jenkins: Geoff Jenkins (born July 21, 1974) is a former outfielder in Major League Baseball.  He played for the Milwaukee Brewers from 1998 to 2007 and the Philadelphia Phillies in 2008.  Jenkins is fourth on the Brewers all-time career home run list trailing only Hall-of-Famer Robin Yount, former MVP Ryan Braun, and former first baseman Prince Fielder.  He is currently on the coaching staff of the Peoria Explorers in the Freedom Pro Baseball League.

Dan Johnson (baseball): Daniel Ryan "Dan" Johnson (born August 10, 1979) is an American professional baseball first baseman for the Bravos de León of the Mexican Baseball League.  He has played most of his ten seasons in Major League Baseball and Nippon Professional Baseball as a first baseman and pitcher, but has never held a Major League starting job for an entire season.  He is perhaps best known for hitting a dramatic two-out, two-strike home run for the Tampa Bay Rays in the bottom of the ninth inning of the last game of the 2011 season, also known as Wild Card Wednesday.  That home run tied the game, which the Rays eventually won, sending them to the playoffs.  His clutch hitting for the Rays, along with his red hair and beard, earned him the nickname "The Great Pumpkin".

Chris Davis (baseball): Christopher Lyn "Chris" Davis (born March 17, 1986), nicknamed "Crush Davis", is an American professional baseball first baseman and outfielder for the Baltimore Orioles of Major League Baseball (MLB).  He stands 6 ft tall and weighs 230 lb .  Davis played in MLB for the Texas Rangers from 2008 until being traded to the Baltimore Orioles in 2011.  He bats left-handed and throws right-handed.  While primarily a first baseman and right fielder throughout his career, Davis has also played third base and designated hitter.

Katsuo Osugi: Katsuo Osugi (大杉 勝男, March 5, 1945 – April 30, 1992) was a Japanese professional baseball first baseman in Nippon Professional Baseball.  He played for the Toei Flyers / Nittaku Home Flyers / Nippon Ham Fighters from 1965 to 1974 and the Yakult Swallows from 1975 to 1983.  He was the Japan Series MVP in 1978 and was inducted into the Japanese Baseball Hall of Fame in 1997.  Osugi's 486 career home runs places him ninth on the all-time NPB list.

Bryan LaHair: Bryan Allan LaHair (born November 5, 1982) is an American professional baseball first baseman for the Somerset Patriots of the Atlantic League of Professional Baseball.  He has played in Major League Baseball (MLB) for the Seattle Mariners and Chicago Cubs and in Nippon Professional Baseball (NPB) for the Fukuoka SoftBank Hawks.

Harmon Killebrew: Harmon Clayton Killebrew ( ; June 29, 1936 – May 17, 2011), nicknamed "The Killer" and "Hammerin' Harmon", was an American professional baseball first baseman, third baseman, and left fielder.  During his 22-year career in Major League Baseball (MLB), primarily with the Minnesota Twins, Killebrew was a prolific power hitter who, at the time of his retirement, was second only to Babe Ruth in American League (AL) home runs and was the AL career leader in home runs by a right-handed batter (since broken by Alex Rodriguez).  He was inducted into the National Baseball Hall of Fame in 1984.

Fred McGriff: Frederick Stanley McGriff (born October 31, 1963) is an American former professional baseball first baseman, who played for six Major League Baseball (MLB) teams from 1986 through 2004.  A power-hitting first baseman, he became a five-time All-Star and led both leagues in home runs in separate years – the American League in 1989 and the National League in 1992.  McGriff finished his career with 493 home runs, tied with Hall of Fame player Lou Gehrig, and only seven homers away from joining the 500 home run club.  He won a World Series title as a first baseman with the Atlanta Braves in 1995.  He currently works in the Atlanta Braves' front office as Special Assistant to Baseball Operations.

Anthony Rizzo: Anthony Vincent Rizzo (born August 8, 1989) is an American professional baseball first baseman for the Chicago Cubs of Major League Baseball (MLB).  He is a three-time All-Star.  Rizzo was selected by the Boston Red Sox in the sixth round of the 2007 MLB draft and became a top minor league prospect in the Red Sox organization.  He was traded to the San Diego Padres after the 2010 season along with three other prospects in exchange for All-Star first baseman Adrian Gonzalez.  After being traded to the Cubs in 2012, he developed into an All-Star player.

Prince Fielder: Prince Semien Fielder (born May 9, 1984) is an American professional baseball first baseman and designated hitter for the Texas Rangers of Major League Baseball (MLB).  He has also played for the Milwaukee Brewers and Detroit Tigers.  He was selected in the first round of the 2002 Major League Baseball draft by the Brewers out of Eau Gallie High School in Melbourne, Florida, and spent the first seven years of his MLB career with the Brewers before signing with the Detroit Tigers in January 2012.  In November 2013, he was traded to the Rangers, where he ended his playing career due to injury in 2016.

Chris Johnson (baseball): Christopher Dalton Johnson (born October 1, 1984) is an American professional baseball first baseman in the Baltimore Orioles organization.  He has played in Major League Baseball (MLB) for the Houston Astros, Arizona Diamondbacks, Atlanta Braves, Cleveland Indians, and Miami Marlins.  While primarily a first baseman for the Marlins, Johnson has mostly played third base throughout his career.

Question: Who is the American professional baseball first baseman who is on the Hall of Fame list with Geoff Jenkins

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the baseball player."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "primary_position": {
      "type": "string",
      "description": "The primary playing position of the player."
    },
    "is_explicitly_hall_of_famer_in_context": {
      "type": "boolean",
      "description": "Indicates if the player is explicitly stated as a Hall-of-Famer in the provided context."
    },
    "association_with_jenkins_and_hall_of_famer": {
      "type": "string",
      "description": "Explains the player's association with Geoff Jenkins and a Hall-of-Famer as described in the context."
    }
  },
  "required": [
    "player_name",
    "nationality",
    "primary_position",
    "association_with_jenkins_and_hall_of_famer"
  ],
  "additionalProperties": false
}
