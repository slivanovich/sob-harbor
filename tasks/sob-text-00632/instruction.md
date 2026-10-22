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
Marc Colombo: Marc Edward Colombo (born October 8, 1978) is a former American football offensive tackle who played for ten seasons in the National Football League (NFL) for the Chicago Bears, Dallas Cowboys and Miami Dolphins.  He played college football at Boston College.  He is the current Assistant Offensive Line Coach for the Dallas Cowboys.

Vaughn Martin: Vaughn Martin (born April 18, 1986) is a Jamaican-born Canadian American football defensive tackle who is currently a free agent.  He was most recently a member of the Montreal Alouettes of the Canadian Football League (CFL).  He was drafted by the San Diego Chargers in the fourth round of the 2009 NFL Draft, the first Canadian university football player drafted by an NFL team as an underclassman.  He played university football at the University of Western Ontario.

Wane McGarity: Wane Keith McGarity (born September 30, 1976 in San Antonio, Texas) is a former American football wide receiver and return specialist in the National Football League and Canadian Football League for the Dallas Cowboys, New Orleans Saints, Calgary Stampeders and Winnipeg Blue Bombers.  He was drafted by the Dallas Cowboys in the fourth round of the 1999 NFL Draft.  He played college football at the University of Texas.

Harry Schuh: Harry Frederick Schuh (September 25, 1942 – May 20, 2013) was an American football player.  He was an All-American tackle at the University of Memphis in 1963 and 1964.  He was the third player drafted overall in the 1965 American Football League draft, after Joe Namath and Larry Elkins.  He played for the American Football League's Oakland Raiders from 1965 through 1969 as the starting right tackle, winning the AFL Championship in 1967 and playing in the Second AFL-NFL World Championship Game.  Schuh was an AFL Western Division All-Star in 1967, an AFL All-League tackle in 1969, and an AFC selection for the AFC-NFC Pro Bowl in 1970 as a member of the NFL's Raiders.  But he was traded before the 1971 season for his replacement at right tackle, Bob Brown, an eventual member of the Pro Football Hall of Fame.  Schuh finished his career with the Green Bay Packers.  He was a member of the Raiders' All-Time Team.

Roy Williams (safety): Roy Lee Williams (born August 14, 1980), is a former American college and professional football player who was a safety in the National Football League (NFL) for nine seasons.  He played college football for the University of Oklahoma, and was recognized as a unanimous All-American.  He was drafted by the Dallas Cowboys eighth overall in the 2002 NFL Draft, and played professionally for the Cowboys and Cincinnati Bengals.  He earned five straight Pro Bowl selections from 2003 to 2007.  Williams is currently a sideline reporter for Oklahoma football games.

Russell Maryland: Russell James Maryland (born March 22, 1969) is a former professional American football player.  He played defensive tackle for ten seasons for the Dallas Cowboys, Oakland Raiders and Green Bay Packers of the National Football League (NFL).  He was drafted by the Cowboys first overall in the 1991 NFL Draft.  He played college football for the University of Miami Hurricanes.

Kevin Brooks (American football): Kevin Craig Brooks (born February 9, 1963) is a former American football player.  He played college football as a defensive tackle for the University of Michigan from 1981 to 1984 and was selected as a first-team All-Big Ten Conference player in 1983 and again in 1984.  He was selected by the Dallas Cowboys in the first round (17th overall pick) of the 1985 NFL Draft.  He played six seasons in the National Football League (NFL) as a defensive tackle for the Cowboys from 1985 to 1988 and as a defensive end for the Detroit Lions from 1989 to 1990.  He appeared in 69 NFL games and recorded 15.5 quarterback sacks.

La'el Collins: La'el Collins (born July 26, 1993) is an American football offensive tackle for the Dallas Cowboys of the National Football League (NFL).  He played college football at Louisiana State University (LSU) where he won the Jacobs Blocking trophy, recognizing Southeastern Conference's (SEC) top offensive lineman, in 2014.  Collins signed with the Dallas Cowboys as an undrafted free agent in 2015.

Horse-collar tackle: The horse-collar tackle is an American football maneuver in which a defender tackles another player by grabbing the back collar or the back-inside of an opponent's shoulder pads and pulling the ball carrier directly downward in order to pull his feet from underneath him.  The technique is most closely associated with Pro Bowl safety Roy Williams.  This kind of tackle was banned from the NFL during the 2005 off-season.  The rule forbidding it is often referred to in the press as "The Roy Williams Rule".  The rule, with modifications, was adopted in college football in 2008 and high school football in 2009.

Jason Garrett: Jason Calvin Garrett (born March 28, 1966) is an American football head coach of the Dallas Cowboys of the National Football League (NFL).  Garrett was the offensive coordinator and assistant head coach of the Cowboys before being promoted to interim head coach after the firing of Wade Phillips on November 8, 2010.  He is a former professional American football quarterback in the National Football League for the Dallas Cowboys, New York Giants, Tampa Bay Buccaneers and Miami Dolphins.  He played college football at Princeton University.

Question: The horse-collar tackle is an American football maneuver most closely associated with an American football player drafted by the Dallas Cowboys in what year? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the player associated with the maneuver."
    },
    "associated_maneuver": {
      "type": "string",
      "description": "The name of the football maneuver."
    },
    "draft_information": {
      "type": "object",
      "properties": {
        "team_drafted_by": {
          "type": "string",
          "description": "The NFL team that drafted the player."
        },
        "draft_year": {
          "type": "integer",
          "description": "The year the player was drafted."
        },
        "overall_pick": {
          "type": "integer",
          "description": "The overall pick number in the draft."
        }
      },
      "required": [
        "team_drafted_by",
        "draft_year",
        "overall_pick"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "associated_maneuver",
    "draft_information"
  ],
  "additionalProperties": false
}
