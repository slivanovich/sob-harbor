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
2008 Mississippi State Bulldogs baseball team: The 2008 Mississippi State Bulldogs baseball team represented Mississippi State University in the NCAA Division I baseball season of 2008.  The team was coached by Ron Polk, in his 35th year as a collegiate head coach, and his 29th at Mississippi State.  During mid-season, Coach Polk announced he would resign effective at the conclusion of the season.  Following the conclusion of the season, former MSU standout and University of Kentucky Head Baseball coach John Cohen was announced by incoming AD Greg Bryne as the new Mississippi State Baseball Coach for 2009.

Jim Krivacs: Jim Krivacs is a former college basketball player for The University of Texas at Austin.  Krivacs transferred to Texas from Auburn and was a three-year starter for the Longhorns under head coach Abe Lemons, beginning in Lemons' first year at Texas.  He twice earned All-America honors—as a first-team All-America selection as a junior in 1978 and as a second-team selection in 1979.  Krivacs led the Longhorns in scoring as a sophomore and junior and was second in scoring as a senior.  He scored an average of 22.0 points per game in 1978 and 19.5 points per game for his three-year Texas career.  His career point total and career scoring average remain eighth- and sixth-highest, respectively, in program history.  In 1978, Krivacs helped to lead Texas to a 26–5 overall record, a share of the Southwest Conference championship, the 1978 National Invitation Tournament championship, and a final ranking of No. 17 in the Associated Press Poll.  Along with teammate Ron Baxter, he was named co-MVP of the 1978 NIT.  As a senior, Krivacs helped to lead the 1979 Longhorns to a 21–8 overall record, a share of the Southwest Conference championship for the second consecutive season, an appearance in the 1979 NCAA Tournament, and a No. 15 final ranking in the Coaches Poll.  In 1979, he was the first Texas men's basketball player to receive recognition as a first-team Academic All-American. Krivacs was selected in the sixth round of the 1979 NBA draft by the Kansas City Kings.

Jim Yarbrough (basketball): Jim Yarbrough (born February 8, 1964) is a distinguished college basketball head coach with a 230-177 record over 14 seasons at Valdosta State University and Southeastern Louisiana University.  He was named Southeastern Louisiana's 11th head basketball coach on June 23, 2005, and was dismissed on March 17, 2014, after compiling a 133-135 record in nine seasons that made Yarbrough the second-winningest men's basketball coach in SLU history, with the second-highest winning percentage in school history.  His tenure included wins over Mississippi State, Penn State and Oregon State.  Prior to his SLU career, Yarbrough led Valdosta State to multiple seasons in the NCAA Division II postseason tournament, including two seasons in which he was named both NCAA Division II South Region Coach of the Year and Gulf South Conference Coach of the Year.  His 2003-04 Valdosta State team finished 25-4 and ranked No. 3 in the nation at the close of the season.  Before beginning his college head coaching career at Valdosta State, he served six years as an assistant coach and associate head coach under John Kresse in the storied College of Charleston basketball program that compiled a 153-28 record and six conference championships during Yarbrough's years as a top assistant.  At SLU, Yarbrough coached the Lions to five winning seasons and a school-record five winning campaigns in the Southland Conference, along with 11 players named to all-SLC teams.

Bobby Lackey: Bobby Lackey is a former American football player who was the starting quarterback for the Texas Longhorns in the late 1950s.  An all around athlete, he also played punter, kicker and defensive back and returned both punts and kick-offs.  He was the team's top scorer in 1958 and 1959 and helped Texas to win a share of the 1959 Southwest Conference championship, the first of the Darrell Royal era.  He was also the first Longhorn to ever appear on the cover of Sports Illustrated

Mississippi State Bulldogs men's basketball: The Mississippi State Bulldogs men's basketball program represents Mississippi State University in Starkville, Mississippi, in men's NCAA Division I basketball.  The Bulldogs play in the Southeastern Conference.  On March 23, 2015, Mississippi State named former UCLA head coach, Ben Howland as its 20th head basketball coach.

John Cohen (baseball): John Cohen (born September 21, 1966) is the former head baseball coach of Mississippi State University and Current Athletic Director.  He played college baseball at Mississippi State (1988–1990) after spending a single season at Birmingham Southern College in Alabama (1986).  He also played on the 1990 College World Series team his senior year at Mississippi State.  He then spent two years in the Minnesota Twins farm system (1990–1991).  He served as an assistant coach at the University of Missouri from 1992 to 97 before becoming head coach at Northwestern State University from 1998 to 2001, where he won two conference championships.  He moved on to the University of Florida for two seasons (2002–2003) as an assistant before accepting the head coaching job at the University of Kentucky.  On June 6, 2008, Cohen was announced as the head coach of his alma mater, Mississippi State.  He is originally from Tuscaloosa, Alabama.

Sylvester Croom: Sylvester Croom Jr. (born September 25, 1954) is an American football coach.  He is currently the running backs coach for the NFL's Tennessee Titans.  He was the head coach at Mississippi State University from 2004 to 2008, and the first African American head football coach in the Southeastern Conference.  His father, Sylvester Croom, Sr., was himself an All-American football player at Alabama A&M, later the team chaplain at the University of Alabama, and has been recognized by that school as one of the state's 40 pioneers of civil rights.  Since his time at Mississippi State, Croom, Jr. has served as running backs coach for three teams in the National Football League.

2016 Mississippi State Bulldogs football team: The 2016 Mississippi State Bulldogs football team represented Mississippi State University in the 2016 NCAA Division I FBS football season.  The Bulldogs played their home games at Davis Wade Stadium in Starkville, Mississippi and competed in the Western Division of the Southeastern Conference (SEC).  They were led by eighth-year head coach Dan Mullen.  Despite having a 5–7 record, the first losing season since 2009, Mississippi State qualified for a bowl bid due to their high APR score.  Mississippi State beat the Miami RedHawks in the St. Petersburg Bowl to finish the season at 6–7.

Scott Suber: Billie Scott Suber (born September 26, 1934) was an American football player.  Suber was born and raised in Calhoun County, Mississippi (first in Derman and then in Calhoun City), where his father worked in a saw mill.  He attended Mississippi State University and played college football at the guard position for the Mississippi State Bulldogs football team under head coach Darrell Royal.  Suber was selected by the Newspaper Enterprise Association as a first-team player on its 1955 College Football All-America Team.  After leaving Mississippi State, he served in the military and later had a career with what became Renesant Bank in Tupelo, Mississippi.  He was inducted into the Mississippi Sports Hall of Fame in 1993.

Darrell Royal: Darrell K Royal (July 6, 1924 – November 7, 2012) was an American football player and coach.  He served as the head coach at Mississippi State University (1954–1955), the University of Washington (1956), and the University of Texas (1957–1976), compiling a career college football record of 184–60–5.  In his 20 seasons at Texas, Royal's teams won three national championships (1963, 1969, and 1970), 11 Southwest Conference titles, and amassed a record of 167–47–5.  He won more games than any other coach in Texas Longhorns football history.  Royal also coached the Edmonton Eskimos of the Canadian Football League (CFL) for one season in 1953.  He never had a losing season as a head coach for his entire career.  Royal played football at the University of Oklahoma from 1946 to 1949.  He was inducted into the College Football Hall of Fame as a coach in 1983.  Darrell K Royal – Texas Memorial Stadium in Austin, Texas, where the Longhorns play their home games, was renamed in his honor in 1996.

Question: The head coach at Mississippi State University from 1954-1955 won a share in the Southwest Conference championship in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the head coach."
    },
    "coached_at_mississippi_state_years": {
      "type": "string",
      "description": "The years the coach served as head coach at Mississippi State University."
    },
    "championship_details": {
      "type": "object",
      "properties": {
        "championship_type": {
          "type": "string",
          "description": "The type of conference championship won."
        },
        "year_won": {
          "type": "integer",
          "description": "The year the championship was won."
        },
        "team_name": {
          "type": "string",
          "description": "The name of the team that won the championship."
        },
        "era_description": {
          "type": "string",
          "description": "A description of the championship's significance within the coach's tenure."
        }
      },
      "required": [
        "championship_type",
        "year_won",
        "team_name",
        "era_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "coached_at_mississippi_state_years",
    "championship_details"
  ],
  "additionalProperties": false
}
