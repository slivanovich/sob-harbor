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
1965 Alabama Crimson Tide football team: The 1965 Alabama Crimson Tide football team (variously "Alabama", "UA" or "Bama") represented the University of Alabama in the 1965 college football season.  It was the Crimson Tide's 71st overall and 32nd season as a member of the Southeastern Conference (SEC).  The team was led by head coach Bear Bryant, in his eighth year, and played their home games at Denny Stadium in Tuscaloosa, Legion Field in Birmingham and Ladd Stadium in Mobile, Alabama.  They finished season with nine wins, one loss and one tie (9–1–1 overall, 6–1–1 in the SEC), as SEC champions and with a victory over Nebraska in the Orange Bowl.  Alabama was also recognized as national champions by the AP Poll after their Orange Bowl win.

2015 Clemson Tigers football team: The 2015 Clemson Tigers football team represented Clemson University in the 2015 NCAA Division I FBS football season.  The Tigers were led by head coach Dabo Swinney in his seventh full year and eighth overall since taking over midway through 2008 season.  They played their home games at Memorial Stadium, also known as "Death Valley."  Clemson competed in the Atlantic Division of the Atlantic Coast Conference.  On December 5, 2015, the Tigers won the 2015 ACC Championship Game by defeating the North Carolina Tar Heels, 45–37, capping their first undefeated regular season since winning the national title in 1981.  Ranked No. 1 throughout the College Football Playoff (CFP) rankings, Clemson defeated the No. 4 Oklahoma Sooners, 37–17, in the 2015 Orange Bowl to advance to the College Football Playoff National Championship.  On January 11, 2016, the No. 2 Alabama Crimson Tide (13–1) defeated the No. 1 Clemson Tigers (14–0) in the 2016 national championship, 45–40.  Both Clemson and Alabama finished the season 14–1.

1988 Orange Bowl: The 1988 Orange Bowl was an American college football bowl game between the Miami Hurricanes and the Oklahoma Sooners.  It was the 54th edition of the Orange Bowl and took place at the Orange Bowl stadium in Miami, Florida on January 1, 1988.  Miami was coached by Jimmy Johnson and Oklahoma was coached by Barry Switzer.  Miami won the game, 20–14.  To date, it is the only time the opposing head coaches from a college national championship football game each later served as head coach of the same professional football team, and won the Super Bowl with that team, that team being the Dallas Cowboys.

2017 Orange Bowl: The 2017 Orange Bowl will be a college football bowl game that will be played on December 30, 2017 at the Hard Rock stadium in Miami Gardens, Florida.  It will be one of the 2017–18 bowl games that will conclude the 2017 FBS football season.  Sponsored by the Capital One financial services organization, the game is officially known as the Capital One Orange Bowl.  The winner of the game will receive the Orange Bowl trophy.

Mark Mangino: Mark Thomas Mangino (born August 26, 1956) is an American football coach, who until October 26, 2015 served as offensive coordinator and tight ends coach at Iowa State University.  Previously, Mangino served as the head football coach at the University of Kansas from 2002 to 2009.  In 2007, Mangino received several national coach of the year honors after leading the Jayhawks to their first 12-win season in school history and an Orange Bowl victory.  However, he resigned as coach at Kansas two seasons later following allegations of mistreatment of players.

Mississippi Veterans Memorial Stadium: Mississippi Veterans Memorial Stadium is an outdoor football stadium in Jackson, Mississippi, United States.  Veterans Memorial Stadium is the home field of the Jackson State Tigers football team.  The stadium was originally known as War Veterans Memorial Stadium then later as Hinds County War Memorial Stadium before finally being christened with its current moniker.  In the past it has served as an alternate home stadium for The University of Mississippi, Mississippi State University, and the University of Southern Mississippi.  From 1973 to 1990 the Egg Bowl was played there and from 1992 to 2013 it hosted the Mississippi High School Activities Association state championship football games.  In addition to college and high school games it has hosted several National Football League (NFL) preseason games.

2011 West Virginia Mountaineers football team: The 2011 West Virginia Mountaineer football team represented West Virginia University in the 2011 NCAA Division I FBS football season as members of the Big East Conference.  The Mountaineers were led by Dana Holgorsen, who was his first season as head coach.  West Virginia played their home games on Mountaineer Field at Milan Puskar Stadium in Morgantown, West Virginia.  They finished the season 10–3, 5–2 in Big East play to earn a share of the Big East Conference championship with Cincinnati and Louisville.  The Mountaineers earned the league's automatic berth in the BCS due to being the highest ranked of the Big East champions in the final BCS rankings.  They were invited to the Orange Bowl for the first time ever where they defeated Clemson 70–33.  West Virginia is now 3–0 in BCS games and the 70 points in the Orange Bowl is the most points ever scored by one team in a bowl game.

2002 Kansas Jayhawks football team: The 2002 Kansas Jayhawks football team represented the University of Kansas in the 2002 NCAA Division I-A football season.  They participated as members of the Big 12 Conference in the North Division.  They were coached by head coach Mark Mangino and played their home games at Memorial Stadium in Lawrence, Kansas.

1967 Oklahoma Sooners football team: The 1967 Oklahoma Sooners football team represented the University of Oklahoma during the 1967 college football season.  They played their home games at Oklahoma Memorial Stadium and competed as members of the Big Eight Conference.  They were coached by head coach Chuck Fairbanks.  The Sooners defeated Tennessee, 26–24, to win the Orange Bowl in Miami, Florida.

2014 Orange Bowl (January): The 2014 Orange Bowl was a college football bowl game played on Friday, January 3, 2014, at Sun Life Stadium in Miami Gardens, Florida.  The 80th annual Orange Bowl, featured the Clemson Tigers from the Atlantic Coast Conference and the Ohio State Buckeyes from the Big Ten Conference.  The game was broadcast live on ESPN at 8:30 PM EST.  It was one of the 2013–14 bowl games that concluded the 2013 FBS football season.  It was sponsored by Discover Financial Services and was officially known as the Discover Orange Bowl.

Question: What football coach won an Orange Bowl and coached his home games at Memorial Stadium?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the football coach."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the coach led."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the team played home games."
    },
    "stadium_location": {
      "type": "string",
      "description": "The city and state where the stadium is located."
    },
    "orange_bowl_win_year": {
      "type": "integer",
      "description": "The year the coach's team won the Orange Bowl."
    }
  },
  "required": [
    "coach_name",
    "team_name",
    "stadium_name",
    "stadium_location",
    "orange_bowl_win_year"
  ],
  "additionalProperties": false
}
