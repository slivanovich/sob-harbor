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
List of Oklahoma Sooners head football coaches: The Oklahoma Sooners football program is a college football team that represents the University of Oklahoma.  The team has had 22 head coaches since organized football began in 1895.  The Sooners have played in more than 1,200 games in its 121 seasons.  In those seasons, eight coaches have led the Sooners to postseason bowl games: Tom Stidham, Jim Tatum, Bud Wilkinson, Gomer Jones, Chuck Fairbanks, Barry Switzer, Gary Gibbs and Bob Stoops.  Eight coaches have won conference championships with the Sooners: Bennie Owen, Stidham, Dewey Luster, Tatum, Wilkinson, Fairbanks, Switzer and Stoops.  Wilkinson, Switzer and Stoops have also won national championships with the Sooners.  Stoops is the all-time leader in games coached and won, Owen is the all-time leader in years coached, while Switzer is the all-time leader in winning percentage.  John Harts is, in terms of winning percentage, the worst coach the Sooners have had as he lost the only game he coached.  John Blake has the lowest winning percentage of those who have coached more than one game with .353 in his 34 games.

1984 Oklahoma Sooners football team: The 1984 Oklahoma Sooners football team represented the University of Oklahoma in the college football 1984 NCAA Division I-A season.  Oklahoma Sooners football participated in the former Big Eight Conference at that time and played its home games in Gaylord Family Oklahoma Memorial Stadium where it has played its home games since 1923.  The team posted a 9–2–1 overall record and a 6–1 conference record to earn a share of the Conference title under head coach Barry Switzer who took the helm in 1973.  This was Switzer's ninth conference title in twelve seasons.

1985 Oklahoma Sooners football team: The 1985 Oklahoma Sooners football team represented the University of Oklahoma in the college football season of 1985–1986.  This year was Barry Switzer's 13th season as head coach.  The Sooners ended this season with 11 wins and a sole loss coming to the Miami Hurricanes in Norman, in a game in which the Sooners lost starting quarterback Troy Aikman for the season.  The Sooners were forced to place their trust in lightning-quick true freshman quarterback Jamelle Holieway and a physical defense featuring three All-Americans, who led them to a Big 8 Conference title and a national championship.  This was Oklahoma's sixth national championship and 34th conference championship in school history.

1956 Oklahoma Sooners football team: The 1956 Oklahoma Sooners football team (variously "Oklahoma", "OU", or the "Sooners") represented the University of Oklahoma in the 1956 college football season.  It was the 62nd season of play for the Sooners.  The team was led by Hall of Fame head coach Bud Wilkinson.  They were led on offense by quarterback Jim Harris, and played their home games at Oklahoma Memorial Stadium in Norman, Oklahoma.

1978 Oklahoma Sooners football team: The 1978 Oklahoma Sooners football team represented the University of Oklahoma in the college football 1978 NCAA Division I-A season.  Oklahoma Sooners football participated in the former Big Eight Conference at that time and played its home games in Oklahoma Memorial Stadium where it has played its home games since 1923.  The team posted an 11–1 overall record and a 6–1 conference record to earn a share of the conference title under head coach Barry Switzer.  This was Switzer's sixth conference title in six seasons since taking the helm in 1973.

1979 Oklahoma Sooners football team: The 1979 Oklahoma Sooners football team represented the University of Oklahoma in the college football 1979 NCAA Division I-A season.  Oklahoma Sooners football participated in the former Big Eight Conference at that time and played its home games in Gaylord Family Oklahoma Memorial Stadium where it has played its home games since 1923.  The team posted an 11–1 overall record and a 7–0 conference record to earn the Conference title outright under head coach Barry Switzer who took the helm in 1973.  This was Switzer's seventh conference title and fourth undefeated conference record in seven seasons.

Barry Switzer: Barry Layne Switzer (born October 5, 1937) is a former American football player and coach.  He served for 16 years as head football coach at the University of Oklahoma and four years as head coach for the Dallas Cowboys of the National Football League (NFL).  He helped the Cowboys win Super Bowl XXX against the Pittsburgh Steelers.  He has one of the highest winning percentages of any college football coach in history, and is one of only three head coaches to win both a college football national championship and a Super Bowl, the others being Jimmy Johnson and Pete Carroll.

1981 Oklahoma Sooners football team: The 1981 Oklahoma Sooners football team represented the University of Oklahoma during the 1981 NCAA Division I-A football season.  They played their home games at Oklahoma Memorial Stadium and competed as members of the Big Eight Conference.  They were coached by head coach Barry Switzer.  The Sooners defeated the <a href="">Houston Cougars

1895 Oklahoma Sooners football team: The 1895 Oklahoma Sooners football team represented the Oklahoma Sooners of the University of Oklahoma during the 1895 college football season and was its first football team ever fielded.  The team completed its inaugural season with a 0–1 record.  The Sooners played their first football game in history against a town team from Oklahoma City and lost by a final score of 34–0.  This was the program's one and only season under the guidance of head coach John A. Harts, the next season he was gold prospecting in the Arctic.

1915 Oklahoma Sooners football team: The 1915 Oklahoma Sooners football team represented the University of Oklahoma in the 1915 college football season.  In their 11th year under head coach Bennie Owen, the Sooners compiled a 10–0 record (3–0 against conference opponents), and outscored their opponents by a combined total of 370 to 54.  This was the first season that the Sooners participated in the Southwest Conference.  The team was retroactively selected as the national champion for 1914 by the Billingsley Report using its alternate "margin of victory" methodology.

Question: What is the date of birth of the coach of the 1981 Sooners football team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the head coach for the specified team season."
    },
    "team_season": {
      "type": "integer",
      "description": "The year of the football season for the team."
    },
    "date_of_birth": {
      "type": "string",
      "description": "The date of birth of the coach in YYYY-MM-DD format."
    }
  },
  "required": [
    "coach_name",
    "team_season",
    "date_of_birth"
  ],
  "additionalProperties": false
}
