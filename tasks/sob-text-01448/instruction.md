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
Tom Garfinkel: Tom Garfinkel is the president and chief executive officer of the Miami Dolphins and Hard Rock Stadium (previously Sun Life Stadium), having been named to the position on September 9, 2013.

Rose Bowl Game: The Rose Bowl Game is an annual American college football bowl game, usually played on January 1 (New Year's Day) at the Rose Bowl stadium in Pasadena, California.  When New Year's Day falls on a Sunday, the game is played on Monday, January 2 (15 times now).  The Rose Bowl is nicknamed "The Granddaddy of Them All" because it is the oldest bowl game.  It was first played in 1902, and has been played annually since 1916.  Since 1945, it has been the highest attended college football bowl game.  It is a part of the Pasadena Tournament of Roses Association's "America's New Year Celebration," which also includes the historic Rose Parade.

Glen Post: Glen F. Post III (born October 4, 1952) is the chief executive officer and president of CenturyLink, an S&P 500 integrated communications service provider based out of Monroe, Louisiana.  He earned a bachelor's degree in accounting in 1974 at Louisiana Tech University and an MBA in 1976 at Louisiana Tech.  Post joined CenturyTel in 1976.  He was named vice president in 1982 and was promoted to senior vice president and treasurer in 1984.  He was appointed to the CenturyTel board of directors in 1985, and the following year he was promoted to senior vice president and chief financial officer.  In 1988 Post was named executive vice president and chief operating officer.  He became the president and chief operating officer of CenturyTel in 1990.  In 1992 Post was named vice chairman of the board, president, and chief executive officer.  In 2002 he was appointed chairman of the board and chief executive officer.  Since 2009 Post has served as chief executive officer and president of CenturyLink.  His honors include: Louisiana Tech College of Administration and Business Distinguished Alumni in 1991, Louisiana Tech University Tower Medallion Award in 1997 and DeGree Enterprises Lifetime Achievement Award in Business 2003.

College Football Playoff National Championship: The College Football Playoff National Championship is a post-season college football bowl game, used to determine a national champion of the NCAA Division I Football Bowl Subdivision (FBS), which began play in the 2014 college football season.  The game serves as the final of the College Football Playoff, a bracket tournament between the top four teams in the country as determined by a selection committee, which was established as a successor to the Bowl Championship Series and its similar BCS National Championship Game.  Unlike the BCS championship, the participating teams in the College Football Playoff National Championship are determined by two semi-final bowls—hosted by two of the consortium's six member bowls yearly—and the top two teams as determined by the selection committee do not automatically advance to the game in lieu of other bowls.

Gator Bowl Stadium: The Gator Bowl was an American football stadium in Jacksonville, Florida.  Originally built in 1927, all but a small portion was razed in 1994 in preparation for the Jacksonville Jaguars' inaugural season; the reconstructed stadium became Jacksonville Municipal Stadium, now EverBank Field.  The old stadium and its replacement have hosted the Gator Bowl, a post-season college football bowl game now known as the Taxslayer Bowl, since its inception in 1946.  It also hosted the Florida–Georgia game, an annual college football rivalry game between the University of Florida and the University of Georgia, and was home to several professional sports teams, including the Jacksonville Sharks of the World Football League (WFL), the Jacksonville Tea Men soccer team, and the Jacksonville Bulls of the United States Football League.

1973 Rose Bowl: The 1973 Rose Bowl was a college football bowl game played on January 1, 1973.  It was the 59th Rose Bowl Game.  The USC Trojans defeated the Ohio State Buckeyes, 42–17.  USC running back Sam Cunningham scored four touchdowns and was named the Rose Bowl Player Of The Game.  The Trojans were voted unanimously the number one team in college football, the first time in college football history.  The attendance of 106,869 set the Rose Bowl Stadium record, as well as the NCAA bowl game record.

2015 Rose Bowl: The 2015 Rose Bowl (officially known as the College Football Playoff Semifinal at the Rose Bowl Game presented by Northwestern Mutual) was a college football bowl game played on January 1, 2015, at the Rose Bowl stadium in Pasadena, California.  This 101st Rose Bowl Game, as a semifinal for the College Football Playoff (CFP), matched the Oregon Ducks against the Florida State Seminoles as selected by the system's selection committee to compete for a spot at the National Championship game to be played on January 12, 2015 at AT&T Stadium in Arlington, Texas.  It was one of the 2014–15 bowl games that concluded the 2014 FBS football season.

Orange Bowl: The Orange Bowl is an annual American college football bowl game played at Hard Rock Stadium in Miami Gardens, Florida.  This bowl game is sponsored by Capital One and part of the College Football Playoff.  It has been played annually since January 1, 1935.  The Orange Bowl, along with the Sugar Bowl and the Sun Bowl, is the second-oldest bowl game in the country, behind the Rose Bowl (first played 1902, played annually since 1916).

Hard Rock Stadium: Hard Rock Stadium is a multipurpose football stadium located in Miami Gardens, Florida, a suburb north of Miami.  It is the home stadium of the Miami Dolphins of the National Football League (NFL), and the Miami Hurricanes from the University of Miami.  The facility also hosts the Orange Bowl, an annual college football bowl game.  It was the home to the Florida Marlins of Major League Baseball (MLB) from 1993 to 2011.

2018 Rose Bowl: The 2018 Rose Bowl is a college football bowl game that will be played on January 1, 2018 at the Rose Bowl stadium in Pasadena, California.  This 104th Rose Bowl Game, as a semifinal for the College Football Playoff (CFP), will match two of the top four teams selected by the system's selection committee to compete for a spot at the 2018 College Football Playoff National Championship game to be played on January 8, 2018 at Mercedes-Benz Stadium.  It is one of the 2017–18 bowl games that will conclude the 2017 FBS football season.  Sponsored by the Northwestern Mutual financial services organization, the game is officially known as the Rose Bowl presented by Northwestern Mutual.

Question: Which college football bowl game is hosted at the stadium for which Tom Garfinkel is chief executive officer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bowl_game_name": {
      "type": "string",
      "description": "The name of the college football bowl game."
    },
    "stadium_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the stadium."
        },
        "location": {
          "type": "string",
          "description": "The location of the stadium."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "ceo_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the chief executive officer."
        },
        "title": {
          "type": "string",
          "description": "The title of the chief executive officer."
        }
      },
      "required": [
        "name",
        "title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "bowl_game_name",
    "stadium_info",
    "ceo_info"
  ],
  "additionalProperties": false
}
