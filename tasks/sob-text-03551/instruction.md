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
Jerry Schemmel: Jerry Schemmel (born November 26, 1959) is an American sportscaster, currently employed as a radio announcer for Major League Baseball's Colorado Rockies.  He was formerly the play-by-play announcer for the NBA's Denver Nuggets, calling their games from 1992 to 2010, until being hired as the full-time voice of the Rockies in January 2010.  Prior to that, he was a play by play announcer for the Minnesota Timberwolves.  He was the radio voice of Colorado State athletics during the 2009-2010 season and has been a fill-in broadcaster for the Rams each year since.

Harry Caray: Harry Caray (born Harry Christopher Carabina March 1, 1914 – February 18, 1998) was an American sportscaster on radio and television.  He covered five Major League Baseball teams, beginning with 25 years of calling the games of the St. Louis Cardinals with two of these years also spent calling games for the St. Louis Browns.  After a year working for the Oakland Athletics and eleven years with the Chicago White Sox, Caray spent the last sixteen years of his career as the announcer for the Chicago Cubs.

Jon Sciambi: Jon "Boog" Sciambi ( ; born April 11, 1970 in Philadelphia, Pennsylvania) is an American sportscaster for ESPN.  He has worked extensively as a baseball play-by-play announcer, calling games for ESPN television and on ESPN Radio.  Sciambi's nickname, "Boog," was given to him owing to his physical resemblance to former major league player Boog Powell.

Dave Armstrong (sportscaster): Dave Armstrong (born May 10, 1957 in Detroit, Michigan) is an American television sports announcer for professional and college sports.  He spent nine years as the play-by-play announcer for two Major League Baseball teams (Kansas City Royals and Colorado Rockies), in the NFL he has worked with both the Seattle Seahawks and the Kansas City Chiefs broadcasting regular and pre-season games and also announced several games for the NBA’s Denver Nuggets.  He broadcasts Big 12 college basketball games for ESPN Regional Television and has been calling games in this conference since 1988.  His signature “Wow!”  is known as the exclamation mark on exceptional plays.

Pat Hughes (sportscaster): Virgil Patrick "Pat" Hughes (born May 27, 1955) is an American sportscaster.  He has been the play-by-play voice of the Chicago Cubs Radio Network since 1996.  Hughes spent 12 years calling games for the Milwaukee Brewers, with broadcaster Bob Uecker.  Hughes also spent 17 years as a radio television play-by-play man for Marquette University basketball.  After his work with the Brewers, Hughes partnered with color commentator Ron Santo, former Hall of Fame third baseman for the Cubs, from 1996 to 2010, until Santo died of bladder cancer.  Their unique on-air chemistry came to be known as the "Pat and Ron Show".

Dummy Lynch: Matthew Daniel "Dummy" Lynch (February 7, 1926 – June 30, 1978) was an American Major League Baseball player.  A native of Dallas, Texas, Lynch was a paratrooper in the 82nd Airborne Division during World War II.  After the war, he attended Southern Methodist University, where he played both baseball and basketball.  He played one year of Major League Baseball for the Chicago Cubs in 1948.  He appeared in only seven games for the Cubs.  In seven major league at bats, he had two hits and a home run (off Warren Spahn) for a career batting average of .286 and a slugging percentage of .714.  He also played minor league baseball from 1948 to 1954 for several teams including the Waco Pirates, Des Moines Bruins, Portsmouth Cubs, Houston Buffaloes, Rochester Red Wings, Columbus Red Birds, Oklahoma City Indians, and Tulsa Oilers.  After retiring from baseball, Lynch became a lawyer in Texas.  In June 1978, he died in an automobile accident at Plano, Texas.

Bill Schoening: Bill Schoening is an American sportscaster who is currently the radio play-by-play voice of the San Antonio Spurs, a position he has held since the 2001-2002 season.  Prior to his work with the Spurs, Schoening broadcast for the Texas Longhorns for 12 years, calling football, basketball, and baseball games.  Schoening is a four-time winner of the Associated Press "Top Texas Play-by-Play Award," and also won the 2014 Texas Sportscaster of the Year Award from the National Sportscasters and Sportswriters Association.  In addition to his work with the Longhorns and Spurs, he has also broadcast National Football League, Major League Baseball, and arena football games.

Skip Caray: Harry Christopher "Skip" Caray Jr. (August 12, 1939 – August 3, 2008) was an American sportscaster, best known for his long career as a radio and television play-by-play announcer for the Atlanta Braves of Major League Baseball.  He was the son of baseball announcer Harry Caray, and the father of fellow Braves broadcaster Chip Caray; another son, Josh Caray, is a reporter for All News 106.7.

Pat Crawford (baseball): Clifford Rankin "Pat" Crawford, a.k.a. "Captain Pat", (January 28, 1902 – January 25, 1994) was a major league baseball player.  Crawford went to Davidson College.  He played baseball for several semi-pro and minor league teams throughout the 1920s including a stint as the left fielder for the 1922 Kinston Highwaymen in the Eastern Carolina Baseball Association, an independent or "outlaw league" team not affiliated with the National Association.  Crawford got his big break in 1929 when he made it to the majors with the New York Giants, which were still being managed by the Hall of Famer John McGraw.  On May 26, 1929, Crawford hit a pinch hit grand slam off Socks Seibold in the sixth inning.  Les Bell then hit a seventh inning pinch hit grand slam off Carl Hubbell.  This was the only time in history that two pinch hit grand slams were hit in the same game.  In 1931 and 1932, he had over 237 and 236 hits respectively for minor league Columbus, Ohio.  He went in and out of the majors through the 1934 season and was named league MVP of the American Association while playing for the Columbus Senators in 1932.  In 1934, Crawford found himself playing on the world champion St. Louis Cardinals.  The last two games of his major league career were World Series games.  His teammates on the Gashouse Gang that year included HOFers Frankie Frisch, Leo Durocher, Joe Medwick, Dizzy Dean, and Burleigh Grimes.  All told, Pat had a .280 batting average in 318 major league games.  He was one of the initial inductees in the Kinston Professional Baseball Hall of Fame on February 11, 1983.

Bob Uecker: Robert George Uecker ( ; born January 26, 1934) is an American former Major League Baseball player and current sportscaster, comedian, and actor.

Question: The American sportscaster Pat Hughes spent 12 years calling games with this broadcaster who played in the American Major League Baseball and now works as a comedian and actor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sportscaster_name": {
      "type": "string",
      "description": "The name of the sportscaster who collaborated with Pat Hughes."
    },
    "collaboration_details": {
      "type": "object",
      "properties": {
        "years_of_collaboration": {
          "type": "integer",
          "description": "The number of years Pat Hughes and the identified sportscaster called games together."
        },
        "team_broadcasted_for": {
          "type": "string",
          "description": "The Major League Baseball team they called games for during their collaboration."
        }
      },
      "required": [
        "years_of_collaboration",
        "team_broadcasted_for"
      ],
      "additionalProperties": false
    },
    "collaborator_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of current professions of the identified sportscaster."
    },
    "was_major_league_baseball_player": {
      "type": "boolean",
      "description": "Indicates if the identified sportscaster was a former Major League Baseball player."
    }
  },
  "required": [
    "sportscaster_name",
    "collaboration_details",
    "collaborator_professions",
    "was_major_league_baseball_player"
  ],
  "additionalProperties": false
}
