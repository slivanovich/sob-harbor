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
Green Bay Packers Fan Hall of Fame: The Green Bay Packers Fan Hall of Fame (capitalized by the organization as the Green Bay Packers FAN Hall of Fame) was the first hall of fame built to honor fans of a professional football team.  It was established by the Green Bay Packers and the Green Bay Packers Hall of Fame in 1998.  Fans may nominate themselves or others for inductions by submitting an essay of 500 words or less, accompanied by a photo or a two-minute video, explaining why they or another person are the ultimate Packers fan and deserve recognition.  Ten finalists are chosen by a selection committee composed of members of the Packer Hall of Fame board and members of the Green Bay Packers' front office, and are profiled in the Milwaukee Journal Sentinel, as well as on the Packers' website.  Fans are then given an opportunity to vote on the 10 finalists whose stories were profiled.

Kevin Steele: Kevin Steele (born May 17, 1958) is an American football coach and former player.  He is the current defensive coordinator for Auburn Tigers.  Prior to that, he was the defensive coordinator at LSU and coached inside linebackers for the football team at Alabama.  Previously, he was the defensive coordinator at Clemson University from 2009 until early 2012.  From 1999 to 2002, Steele served as the head football coach at Baylor University, compiling a record of 9–36 overall and 1–31 in the Big 12 Conference.

2005 Houston Texans season: The 2005 Houston Texans season was the fourth season in franchise history.  The Texans completed the season with the worst record in franchise history (a record that would later be matched in 2013).  This led to the Texans obtaining the first selection in the NFL Draft for the second time since the franchise formed in 2002.  The team fired head coach Dom Capers after the season; he was replaced by Denver Broncos offensive coordinator Gary Kubiak.

Fritz Shurmur: Leonard Frank "Fritz" Shurmur (July 15, 1932 – August 30, 1999) was an American football coach.  He served as the head football coach at the University of Wyoming from 1971 to 1974, compiling a record of 15–29.  He was subsequently an assistant coach in the National Football League (NFL) with the Detroit Lions (1975–1977), New England Patriots (1978–1981), Los Angeles Rams (1982–1990), Phoenix Cardinals (1991–1993), and Green Bay Packers (1994–1998).  Shurmur was the defensive coordinator for the 1996 Green Bay Packers team that won Super Bowl XXXI.  He was the uncle of former Cleveland Browns head coach Pat Shurmur.

Dom Capers: Ernest Dominic Capers (born August 7, 1950) is an American football coach and the current defensive coordinator for the Green Bay Packers of the National Football League (NFL).  Capers served as the head coach for the NFL's Carolina Panthers from 1995 to 1998 and for the Houston Texans from 2002 to 2005.  He is the only person to serve two different NFL expansion teams as their inaugural head coach.

2013 Green Bay Packers season: The Green Bay Packers season was the franchise's 94th season in the National Football League, the 95th overall and the eighth under head coach Mike McCarthy.  The Packers came into the 2013 season looking to win the NFC North for the 3rd year in a row.  They were coming off a 45-31 loss to the San Francisco 49ers in the NFC Divisional Playoffs.  The Packers started the 2013 season with a rematch with the 49ers in San Francisco.  They lost the game 34-28.  After winning their home opener against the Redskins, they lost 34-30 in Cincinnati to the Bengals after they had a 30-14 lead in the 3rd quarter.  After the loss, the Packers would win 4 games in a row to sit at 5-2 before losing a Monday Night game at home to the Bears 27-20.  In that game, the Packers would lose star quarterback Aaron Rodgers to a broken collarbone in the 1st quarter.  He would be replaced by Scott Tolzien and sometimes Matt Flynn.  In week 12, the Packers tied the Vikings 26-26.  It was Green Bay's first tie since 1987.  The Packers would lose the next game 40-10 to the Lions on Thanksgiving to sit at 5-6-1, and looking like being on the verge of missing the postseason for the first time since 2008.  The Packers would then beat the Falcons 22-21 to even their record at 6-6-1.  The following week, the Packers defeated the Dallas Cowboys 37-36 in Dallas after they had trailed 26-3 at halftime.  The comeback was the largest in franchise history.  The Packers would then lose a shootout with the Pittsburgh Steelers 38-31 at home to sit at 7-7-1, the first meeting between the teams since Super Bowl XLV.  The next week, the Packers defeated the Chicago Bears 33-28 at Soldier Field to clinch the NFC North in a game in which the winner would've clinched the division.  The game was famously well known for a touchdown catch made by Randall Cobb from Aaron Rodgers with less than a minute remaining to seal the win.  The play came on a 4th and 8 situation in which Cobb was wide open near the endzone.  The Packers entered the playoffs as the 4 seed in the NFC.  In the wild card game, they lost 23-20 in a rematch with the 49ers on a Phil Dawson field goal as time expired.  The game was one of the coldest in NFL playoff history, with a final temperature of 5 °F (-15 °C)

2013 Houston Texans season: The Houston Texans season was the franchise's 12th season in the National Football League.  The Texans failed to improve upon their 12–4 record from 2012, suffering through a season-ending 14-game losing streak following a 2–0 start and missing the playoffs for the first time since 2010.  Head coach Gary Kubiak was fired after eight seasons following their eleventh loss (Week 14 vs. the Jacksonville Jaguars).  Defensive coordinator Wade Phillips was named the interim head coach for the final three games of the season.  Their 14-game losing streak is the worst in team history.  Coming off a franchise-best 12–4 record just the year before, the Texans tie a league record with the Houston Oilers (who, coincidentally, also went 12–4 in 1993 and 2–14 in 1994) for the biggest season-to-season decline in win total.  On January 3, 2014, claiming that "I'm ready to kick 2013 the hell out the door", Texans owner Robert McNair announced that former Penn State head coach Bill O'Brien would be the Texans' third head coach.

Joe Whitt Jr.: Joe Whitt Jr. (born 1978) is an American football coach who is currently the cornerbacks coach of the Green Bay Packers of the National Football League (NFL).  After the majority of the defensive coaching staff was fired after a disappointing 2008 season, He was one of only two defensive coaches retained by the Packers.  He was then officially announced by the Packers that he was promoted from his defensive quality control position to his current cornerbacks coach on February 3 of 2009 after speculation by the media.  Whitt Jr. has also spent time with the Atlanta Falcons in 2007 as an Assistant Defensive Backs coach.  Whitt attended Auburn High School, graduating in 1997, and was a walk-on wide receiver for the Auburn University Tigers football team the following season before earning a scholarship.  When an injury ended his playing career, Whitt became a student assistant at Auburn University.  After completing a degree in communications in 2001, Whitt was hired as wide receivers coach at The Citadel, before moving on to become cornerbacks coach and recruiting coordinator at the University of Louisville under head coach Bobby Petrino in 2003.  In 2006, Whitt moved with Petrino to the Falcons.

Mike Vrabel: Michael George Vrabel ( ; born August 14, 1975) is a former American football linebacker and current defensive coordinator for the Houston Texans in the National Football League.  He played college football at Ohio State University, where he earned consensus All-American honors.  He was chosen by the Pittsburgh Steelers in the third round of the 1997 NFL Draft.  He also played professionally for the New England Patriots and Kansas City Chiefs.  After spending three years coaching linebackers and defensive linemen at Ohio State, Vrabel joined the Texans in January 2014 as linebackers coach.

Mike Sherman: Michael Francis Sherman (born December 19, 1954) is an American football coach and former player.  Sherman was the head coach of the Green Bay Packers from 2000 to 2005.  Sherman led the Packers to five consecutive winning seasons from 2000–04 and three divisional titles in 2002, 2003, and 2004.  He was also the head football coach at Texas A&M University from 2008 to 2011.  He has also been a coach in the NFL for the Seattle Seahawks, Houston Texans and Miami Dolphins.  Before he started coaching in the NFL, he served as an assistant coach at five different colleges, including Texas A&M, where he coached the offensive line for seven seasons.  He is one of few coaches that has been a head coach at every level - high school, college, and in the National Football League.  .

Question: Who replaced Dom Capers, the football coach and current defensive coordinator for the Green Bay Packers after he was fired by the Houston Texans in a season where they finished with the worst record in franchise history?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "replaced_coach": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the coach who was replaced."
        },
        "role_at_team": {
          "type": "string",
          "description": "The role the coach held at the team before being replaced."
        }
      },
      "required": [
        "name",
        "role_at_team"
      ],
      "additionalProperties": false
    },
    "replacing_coach": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the coach who replaced the previous coach."
        },
        "previous_role": {
          "type": "string",
          "description": "The role the replacing coach held immediately before taking the new position."
        }
      },
      "required": [
        "name",
        "previous_role"
      ],
      "additionalProperties": false
    },
    "team_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the team where the coaching change occurred."
        },
        "season_of_change": {
          "type": "integer",
          "description": "The year of the season when the coaching change took place."
        },
        "context_of_season": {
          "type": "string",
          "description": "A description of the team's performance or significant event during that season."
        }
      },
      "required": [
        "name",
        "season_of_change",
        "context_of_season"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "replaced_coach",
    "replacing_coach",
    "team_details"
  ],
  "additionalProperties": false
}
