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
Doug McDermott: Douglas Richard McDermott (born January 3, 1992) is an American professional basketball player for the New York Knicks of the National Basketball Association (NBA).  While playing college basketball for Creighton University, he led the nation in scoring in 2013–14, was a three-time consensus first-team All-American.  He was the consensus national player of the year as a senior in 2014, and finished his college career with the fifth-most points in NCAA Division I men's basketball history.  After graduating from Creighton, McDermott entered the 2014 NBA draft, where he was drafted 11th overall by the Chicago Bulls.  He went on to play two and half seasons for the Bulls before being traded to the Thunder in February 2017.  McDermott is the son of current Creighton coach, Greg McDermott; Greg coached McDermott during his college career.

Jake Young: Jacob Cardwell Young, III (March 22, 1968 — October 12, 2002) was an American football center who played college football for the University of Nebraska–Lincoln and attended Midland Lee High School in Midland, Texas.  He was a first-team All-American in 1988 and a consensus first-team All-American in 1989.  Young was inducted into the Nebraska Football Hall of Fame in 2000.  He was killed in the 2002 Bali bombings.

Nolan Smith: Nolan Derek Smith (born July 25, 1988) is an American former professional basketball player and current special assistant coach for the Duke Blue Devils men's basketball team.  He played college basketball for Duke before being drafted 21st overall by the Portland Trail Blazers in the 2011 NBA draft.  As a junior, he started at shooting guard for Duke's national champion 2010 team.  As a senior, he was named a consensus first-team All-American and the ACC Player of the Year.

1945 Northwestern Wildcats football team: The 1945 Northwestern Wildcats team represented Northwestern University during the 1945 Big Ten Conference football season.  In their 11th year under head coach Pappy Waldorf, the Wildcats compiled a 4–4–1 record (3–3–1 against Big Ten Conference opponents) and finished in fourth place in the Big Ten Conference.  End Max Morris and guard Jim Lecture were selected by both the Associated Press and United Press as first-team players on the 1945 All-Big Ten Conference football team.  Morris was also selected as a consensus first-team All-American.

1919 Princeton Tigers football team: The 1919 Princeton Tigers football team represented Princeton University in the 1919 college football season.  The team finished with a 4–2–1 record under sixth-year head coach Bill Roper.  No Princeton players were selected as consensus first-team honorees on the 1919 College Football All-America Team, but halfback Murray Trimble was selected as a first-team All-American by the "Reno Evening Gazette", and a second-team All-American by Walter Camp.

James Russell McKay: James Russell McKay (May 16, 1889 – October 16, 1966) was an American football player.  A native of Youngstown, Ohio, McKay played college football at the halfback position for Brown University in 1909 and 1910 and was selected as the captain of the 1910 Brown Bears football team.  In 1910, he was selected as a first-team All-American by the "Evening Standard", as determined by the consensus among the various Eastern football experts who picked All-American teams.  He was also named a first-team All-American by "The New York Sun", and by Ted Coy, and as a second-team All-American by Walter Camp.  After graduating from Brown, McKay returned to Youngstown where he worked as a lawyer.  He became a vice president at Home Savings & Loan in Youngstown.  He died in Youngstown in 1966 at age 77.  He was posthumously inducted into the Brown Hall of Fame in 1971.

Bob Westfall: Robert Barton "Bullet Bob" Westfall (May 5, 1919 – October 23, 1980) was an American football fullback who played for the University of Michigan (1939–1941) and the Detroit Lions (1944–1947).  He was a consensus first-team All-American in 1941 and a first-team All-Pro player in 1945.  In 1987, Westfall was enshrined in the College Football Hall of Fame.

Russ Smith (basketball): Russ Anton Smith (born April 19, 1991) is an American professional basketball player for Luoyang Zhonghe of the Chinese National Basketball League (NBL).  He played collegiately for the Louisville Cardinals, playing a starring role as a junior in helping them win the 2013 NCAA championship, while earning third-team All-American by the NABC and the Sporting News.  As a senior at Louisville, he was named a consensus first-team All-American.

2006 NBA All-Star Game: The 2006 NBA All-Star Game was played on Sunday, February 19, 2006 at the Toyota Center in Houston, Texas, home of the Houston Rockets.  The game was the 55th annual All-Star game.  The theme song was by Houston native Chamillionaire who made a new version of his hit "Turn It Up."  Trailing by 21 points, the East rode the hot shooting of LeBron James and the teamwork of the four All-Stars from the Detroit Pistons to a 122–120 victory over the West.  The 21-year-old James, who scored 29 points and grabbed six rebounds, became the youngest player to win MVP.  With the score tied, Dwyane Wade, who finished with 20 points, hit the game-winning layup with 16 seconds left.  Tracy McGrady of the Houston Rockets led all players with a game-high 36 points.  The Detroit Pistons tied a record with the 1962 Boston Celtics (Sam Jones, Bill Russell, Bob Cousy, Tom Heinsohn), 1975 Celtics (John Havlicek, JoJo White, Dave Cowens, Paul Silas), 1983 Philadelphia 76ers (Julius Erving, Moses Malone, Andrew Toney and Maurice Cheeks), 1998 Lakers (Kobe Bryant, Shaquille O'Neal, Eddie Jones and Nick Van Exel), 2011 Boston Celtics (Rajon Rondo, Kevin Garnett, Paul Pierce and Ray Allen), 2015 Atlanta Hawks (Al Horford, Jeff Teague, Paul Millsap and Kyle Korver), and 2017 Golden State Warriors (Stephen Curry, Kevin Durant, Klay Thompson, and Draymond Green) by sending four players to the All-Star game.

Paul Pierce: Paul Anthony Pierce (born October 13, 1977) is an American former professional basketball player who played 19 seasons in the National Basketball Association (NBA).  Pierce was a high school McDonald's All-American and earned consensus first-team All-America honors in his junior year at Kansas.

Question: What consensus first-team All-American during his junior year at Kansas was a member of the 2011 Boston Celtics?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the basketball player."
    },
    "college_career_highlights": {
      "type": "object",
      "properties": {
        "university": {
          "type": "string",
          "description": "The university where the player earned All-American honors."
        },
        "all_american_honor": {
          "type": "string",
          "description": "The specific All-American honor received."
        },
        "all_american_year_level": {
          "type": "string",
          "description": "The academic year level when the All-American honor was received."
        }
      },
      "required": [
        "university",
        "all_american_honor",
        "all_american_year_level"
      ],
      "additionalProperties": false
    },
    "nba_team_affiliation": {
      "type": "object",
      "properties": {
        "team_name": {
          "type": "string",
          "description": "The NBA team the player was a member of."
        },
        "affiliation_year": {
          "type": "integer",
          "description": "The specific year of the team affiliation."
        },
        "source_event_mention": {
          "type": "string",
          "description": "The event context where the team affiliation was mentioned."
        }
      },
      "required": [
        "team_name",
        "affiliation_year",
        "source_event_mention"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "college_career_highlights",
    "nba_team_affiliation"
  ],
  "additionalProperties": false
}
