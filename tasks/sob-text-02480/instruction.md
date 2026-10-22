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
Sammy Sosa: Samuel "Maiky" Peralta Sosa (born November 12, 1968) is a Haitian-Dominican former professional baseball right fielder.  Sosa played with four Major League Baseball teams over his career, most notably the Chicago Cubs.  Sosa's Major League career began with the Texas Rangers in 1989 .  After three seasons with the Chicago White Sox, Sosa became a member of the Cubs in 1992 and became one of the league's best hitters.  Sosa hit his 400th home run in his 1,354th game and his 5,273rd at-bat, the quickest in National League history.  In 1998, Sosa and Mark McGwire achieved national fame for their home run-hitting prowess in pursuit of Roger Maris' home run record.

Ron Blomberg: Ronald Mark Blomberg (born August 23, 1948), nicknamed Boomer, is an American former professional baseball player and minor league manager.  He played in Major League Baseball as a designated hitter, first baseman and right fielder.  He played for the New York Yankees (1969, 1971–76) and Chicago White Sox (1978), and was the manager of the Bet Shemesh Blue Sox in the Israel Baseball League (2007).  He was the first designated hitter in Major League Baseball history.

Larry Himes: Lawrence Austin Himes (born October 7, 1940 in Riverside, California, United States) was a general manager for two Major League Baseball teams: the Chicago White Sox (from 1986 until 1990) and the Chicago Cubs (from 1991 until 1994).  He is best known for trading for Sammy Sosa during each tenure.  Prior to becoming a general manager, he was the California Angels scouting director from 1981 through 1986.  During his nine-year playing career (1961–69), Himes was a catcher in minor league baseball, batting .249 in 725 games played.

Chicago White Sox: The Chicago White Sox are an American professional baseball team based in Chicago, Illinois.  The White Sox compete in Major League Baseball (MLB) as a member club of the American League (AL) Central division.  Home games are held at Guaranteed Rate Field, located on the city's South Side, and the team is owned by Jerry Reinsdorf.  They are one of two major league clubs in Chicago; the other is the Chicago Cubs, who are a member of the National League (NL) Central division.

Chicago Cubs: The Chicago Cubs are an American professional baseball team based in Chicago, Illinois.  The Cubs compete in Major League Baseball (MLB) as a member club of the National League (NL) Central division.  The team plays its home games at Wrigley Field, located on the city's North Side.  The Cubs are one of two major league teams in Chicago; the other, the Chicago White Sox, is a member of the American League (AL) Central division.  The Cubs, first known as the White Stockings, was a founding member of the NL in 1876, becoming the Chicago Cubs in 1903.

Rollie Zeider: Rollie Hubert Zeider (November 16, 1883 – September 12, 1967) was a professional baseball player.  An infielder (playing over 100 games at all four infield positions in his career), he played nine seasons in Major League Baseball for the Chicago White Sox (1910–13), New York Yankees (1913), Chicago Chi-Feds/Chicago Whales in the Federal League from 1914–15, and lastly the Chicago Cubs (1916–18).  He is one of only a few players to play for three different Chicago teams in his career, and one of two to do it in the 20th century.  He is the only player to hit home runs for all three Chicago major league teams in the twentieth century.  Along with Dutch Zwilling he is the only 20th century player to play in the same city in three different major leagues: American League (White Sox), Federal League (Chi-Feds/Whales), and the National League (Cubs).

Jermaine Dye: Jermaine Trevell Dye (born January 28, 1974) is an American former professional baseball right fielder.  Dye grew up in Northern California and was a multi-sport star at Will C. Wood High School in Vacaville.  Dye attended Cosumnes River College in Sacramento, where he played as a right fielder on a team that reached the playoffs.  Dye played in Major League Baseball (MLB) for the Atlanta Braves (1996), Kansas City Royals (1997–2001), Oakland Athletics (2001–2004), and the Chicago White Sox (2005–2009).  He won the World Series MVP with the White Sox in 2005.  Dye batted and threw right-handed and, in his prime, was known for his ability to hit for power and his powerful throwing arm.  Dye announced his retirement on March 31, 2011.

George Browne (baseball): George Edward Browne (January 12, 1876 – December 9, 1920) was an American professional baseball right fielder.  He played in Major League Baseball (MLB) for the Philadelphia Phillies, New York Giants, Boston Doves, Chicago Cubs, Washington Senators, Chicago White Sox, and Brooklyn Dodgers between 1901 and 1912.  He was the National League leader in runs scored in 1904 with New York.  For his career, he compiled a .273 batting average, 303 runs batted in, 614 runs scored, and 190 stolen bases.  Browne was a member of the 1905 World Series Champion Giants, hitting .227 with one RBI and two runs scored in the World Series.

Rick Renteria: Richard Avina Renteria (born December 25, 1961) is an American former Major League Baseball infielder who is currently the manager of the Chicago White Sox of Major League Baseball (MLB).  Renteria played in parts of five seasons between 1986 and 1994 with the Pittsburgh Pirates, Seattle Mariners, and Florida Marlins.  He then coached and managed in the Marlins organization until 2001, and in the San Diego Padres organization until 2013.  He was the manager of the Chicago Cubs in 2014.  Renteria was also the bench coach for the Chicago White Sox in 2016.

Jim McAnany: James McAnany (September 4, 1936 – December 16, 2015) was an American professional baseball player.  Primarily a right fielder, he played all or part of five seasons in Major League Baseball, from 1958 until 1962, for the Chicago White Sox and Chicago Cubs.  He was in the White Sox starting lineup for three of the six games in the 1959 World Series.

Question: Lawrence Austin Himes, was a general manager for two Major League Baseball teams: the Chicago White Sox (from 1986 until 1990) and the Chicago Cubs (from 1991 until 1994), and is best known for trading for which Haitian-Dominican former professional baseball right fielder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the baseball player."
    },
    "player_nationality": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The nationalities of the player."
    },
    "player_position": {
      "type": "string",
      "description": "The primary playing position of the player."
    },
    "general_manager": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the general manager."
        },
        "teams_managed": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "team_name": {
                "type": "string",
                "description": "The name of the MLB team."
              },
              "start_year": {
                "type": "integer",
                "description": "The start year of the general manager's tenure with the team."
              },
              "end_year": {
                "type": "integer",
                "description": "The end year of the general manager's tenure with the team."
              }
            },
            "required": [
              "team_name",
              "start_year",
              "end_year"
            ],
            "additionalProperties": false
          },
          "description": "A list of teams the general manager managed with their respective tenures."
        },
        "notable_action": {
          "type": "string",
          "description": "The action the general manager is best known for, related to the player."
        }
      },
      "required": [
        "name",
        "teams_managed",
        "notable_action"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_position",
    "general_manager"
  ],
  "additionalProperties": false
}
