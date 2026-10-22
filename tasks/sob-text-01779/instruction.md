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
Stevie Tu'ikolovatu: Stevie Tu'ikolovatu (born June 28, 1991) is an American football defensive tackle for the Tampa Bay Buccaneers of the National Football League (NFL).  He played college football at Utah before transferring to USC.  He is the nephew of Sione Po'uha who was a defensive tackle drafted by the New York Jets in 2005.

2010 Tampa Bay Buccaneers season: The 2010 Tampa Bay Buccaneers season was the club's 35th season as a franchise in the NFL.  The Buccaneers entered the season attempting to improve on their 3–13 record and last place finish in the NFC South in 2009, a feat they accomplished after only six games.  The Buccaneers achieved the best turnaround in franchise history and became the first team since the NFL merger in 1970 to start 10 rookies and achieve a winning season.  Raheem Morris spent his second season as head coach.  The Buccaneers had the third overall pick in the 2010 NFL Draft, with which they selected Gerald McCoy.

Defensive tackle: A defensive tackle (DT) is typically the largest and strongest of the defensive players in American football.  The defensive tackle typically lines up opposite one of the offensive guards.  Depending on a team's individual defensive scheme, a defensive tackle may be called upon to fill several different roles.  These roles may include merely holding the point of attack by refusing to be moved or penetrating a certain gap between offensive linemen to break up a play in the opponent's backfield.  If a defensive tackle reads a pass play, his primary responsibility is to pursue the quarterback, or simply knock the pass down at the line if it's within arm's reach.  Other responsibilities of the defensive tackle may be to pursue the screen pass or drop into coverage in a zone blitz scheme.  In a traditional 4–3 defensive set, there is no nose tackle.  Instead there is a left and right defensive tackle.  Some teams especially in the NFL do have a nose tackle in this scheme, but most of them do not.

Santana Dotson: Santana N. Dotson (born December 19, 1969 in New Orleans, Louisiana) is a former American football defensive tackle in the National Football League.  He was a part of Houston's Yates High School football team when it won the 1985 5A state championship.  While at Baylor, Dotson was voted All-American in 1991.  He won the 1992 NFL Defensive Rookie of the Year with the Tampa Bay Buccaneers and played in two Super Bowls with the Green Bay Packers.

Shelton Quarles: Shelton Eugene Quarles (born September 11, 1971) is a former linebacker for the Tampa Bay Buccaneers, the team he played for in his ten-year career from 1997 to 2006.  He formally served as the Director of Pro Scouting for the Tampa Bay Buccaneers but now serves as Director of Football Operations for the Tampa Bay Buccaneers.

Mark Dominik: Mark Dominik (born March 9, 1971) is a former professional football executive and scout for the Kansas City Chiefs and Tampa Bay Buccaneers of the National Football League (NFL) from 1994 to 2013.  Dominik joined the Tampa Bay Buccaneers after spending a year and a half working in both the college and pro personnel departments of the Kansas City Chiefs.  In 1995, Dominik was named Pro Personnel Assistant with the Tampa Bay Buccaneers.  He moved up to Pro Scout, Coordinator of Pro Scouting and onto Director of Pro Scouting from 1997 to 2008.  Dominik succeeded Bruce Allen as General Manager on January 17, 2009.  Dominik held the position of General Manager from 2009 thru the 2013 season.  Dominik during his tenure as General Manager with the Tampa Bay Buccaneers was active in the military community.  He was a finalist in the NFL's salute to service award in 2012.  Dominik is currently an analyst for ESPN where he is on SportsCenter, NFL Insiders, ESPN Radio and NFL Live.  Dominik is a host on Sirius XM NFL Radio.  Born in St. Cloud, Minnesota, Dominik holds a bachelor of science degree in sports management from the University of Kansas.

Brian Price (American football, born 1989): Brian Larisso Price (born April 10, 1989) is a former American football defensive tackle in the National Football League for the Tampa Bay Buccaneers.  After playing college football at the University of California, Los Angeles, he was drafted by the Tampa Bay Buccaneers in the second round of the 2010 NFL Draft.

Maulty Moore: Maulty Moore (born August 12, 1946), is a former professional American football defensive tackle who played for five seasons with the Miami Dolphins, the Cincinnati Bengals, and the Tampa Bay Buccaneers.  Undrafted on graduating Bethune-Cookman College in 1970, he began a year of conditioning that added 50 pounds to his undersized frame before trying out for the Dolphins as a free agent.  He was signed to the Dolphins' taxi squad in 1971, and promoted to special teams the next year.  He blocked a Roy Gerela field goal attempt during the Dolphins' victory over the Pittsburgh Steelers.  Waived by the Dolphins in 1975, he spent a year with the Bengals before finishing his career in 1976 with the then expansion Tampa Bay Buccaneers.  Moore went on to teach in the Broward County school system.

Gerald McCoy: Gerald Keith McCoy Jr. (born February 25, 1988) is an American football defensive tackle for the Tampa Bay Buccaneers of the National Football League (NFL).  He played college football at Oklahoma, where he earned consensus All-American honors, and was drafted by the Buccaneers third overall in the 2010 NFL Draft.  Since joining the Buccaneers and the NFL, he has been selected to the Pro Bowl five consecutive years.

David Logan (American football): David Logan (October 25, 1956 – January 13, 1999) was an American football defensive tackle in the National Football League.  He was drafted by the Tampa Bay Buccaneers in the 12th round of the 1979 NFL Draft.  He played college football at Pittsburgh.  A nose tackle with the Tampa Bay Buccaneers from 1979 to 1986, Logan finished his career ranked second on the team's all-time sack list and sixth in career tackles.  Named an All-Pro in 1984 and alternate three times in his career, finishing his NFL playing career with the Green Bay Packers in 1987.

Question: Which Oklahoma All-American defensive tackle helped the 2010 Tampa Bay Buccaneers achieve the best turnaround in franchise history?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the player."
        },
        "position": {
          "type": "string",
          "description": "The primary playing position of the player."
        },
        "college": {
          "type": "string",
          "description": "The college the player attended."
        },
        "all_american_honors": {
          "type": "boolean",
          "description": "Indicates if the player earned All-American honors in college."
        }
      },
      "required": [
        "name",
        "position",
        "college",
        "all_american_honors"
      ],
      "additionalProperties": false
    },
    "team_season_details": {
      "type": "object",
      "properties": {
        "team_name": {
          "type": "string",
          "description": "The name of the NFL team."
        },
        "season_year": {
          "type": "integer",
          "description": "The year of the NFL season."
        },
        "season_achievement": {
          "type": "string",
          "description": "A notable achievement of the team during that season."
        }
      },
      "required": [
        "team_name",
        "season_year",
        "season_achievement"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the player who is the answer to the question."
    }
  },
  "required": [
    "player",
    "team_season_details",
    "final_answer"
  ],
  "additionalProperties": false
}
