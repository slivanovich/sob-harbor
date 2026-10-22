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
Dirty Dozen (American football): The Dirty Dozen were the rookies that made the Dallas Cowboys team in 1975.  These players were credited with helping the Cowboys advance to Super Bowl X and was a key foundation of the team's success during the latter half of the 1970s going into the early 1980s, as by 1979 many of these players would have replaced many of the Cowboys' aging starters of the 1960s.  The rookies came up with the nickname inspired by the film of the same name, and spent half of the season without shaving.

Barry Switzer: Barry Layne Switzer (born October 5, 1937) is a former American football player and coach.  He served for 16 years as head football coach at the University of Oklahoma and four years as head coach for the Dallas Cowboys of the National Football League (NFL).  He helped the Cowboys win Super Bowl XXX against the Pittsburgh Steelers.  He has one of the highest winning percentages of any college football coach in history, and is one of only three head coaches to win both a college football national championship and a Super Bowl, the others being Jimmy Johnson and Pete Carroll.

1996 Dallas Cowboys season: The 1996 Dallas Cowboys season would mark their 37th consecutive season in the NFL.  Following their victory in Super Bowl XXX, the Cowboys endured a tumultuous year.  Star receiver Michael Irvin was suspended by the league for the first five games and before the playoffs was accused with lineman Erik Williams of sexual assault (a charge subsequently proven inaccurate).  Controversy also took place when writer Skip Bayless published a scathing account of the Cowboys' 1995 season.  Long time trainer Mike Woicik also left the team after the season following a sideline dispute with coach Barry Switzer.

Josh Holliday: Josh Holliday (born September 14, 1976) is an American college baseball coach and former professional player in Minor League Baseball.  Currently the head coach of the Oklahoma State Cowboys baseball team, he was hired to this position prior to the 2013 season.  In 2014, Holliday was the Big 12 Conference Baseball Coach of the Year as OSU claimed the conference regular season championship.  Hollidays' Cowboys pulled OSU a little Cowboy baseball tradition out of the fire and faced Oklahoma on the final weekend of 2017.  The team was in danger of missing out of the postseason for the 1st time in Hollidays tenure at Oklahoma State.  The Cowboys swept the instate rival Oklahoma Sooners (#2 seed going into region play) to claim the last and final spot as the 8th seed in the BigXII Championship.  The Cowboys went back to their traditionion and won just the 2nd Big 12 tournament in schools rich baseball history.  The Cowboys won 16 straight Big 8 tournaments before the formation of the Big12.  The Cowboys became the 1st eight seed (last seed) to win the conference championship and by doing so Holliday got his team in the NCAA postseason for the 5th time in his 5 years at the school.  The season was full of injuries from top to bottom Holliday and is associated Head Coach and current (2016) assistant coach of the year Rob Walton put together a pitching staff that was nothing short of magical.  The Cowboys luck would run out as the were sent to the Arkansas Regional and went 0-2 losing game one to Regional champions Missouri State Bears on a two out bottom of the 9th walk off HR.  Garrett Benge hit for the cycle for Hollidays Cowboys but it wasn't enough.  Garrett McCain would be named 1st team all-American the 25th in Cowboys history he would one of five current Cowboys drafted in 2017 preceded by 11 from the 2016 College World Series club.  Giving Holliday 16 in 2 years.  The Cowboys went on the end of the year run the had seen them lose six games in a row and face being the 1st Oklahoma State team to finish under .500 in 40 years.The Cowboys finished 30-27 on the year.  The 6-5 victory of the Texas Longhorns would be Hollidays' 200th victory as the head man of Oklahoma State.

Jason Garrett: Jason Calvin Garrett (born March 28, 1966) is an American football head coach of the Dallas Cowboys of the National Football League (NFL).  Garrett was the offensive coordinator and assistant head coach of the Cowboys before being promoted to interim head coach after the firing of Wade Phillips on November 8, 2010.  He is a former professional American football quarterback in the National Football League for the Dallas Cowboys, New York Giants, Tampa Bay Buccaneers and Miami Dolphins.  He played college football at Princeton University.

List of Dallas Cowboys first-round draft picks: The Dallas Cowboys are professional American football team based in Dallas, Texas.  The Cowboys team is a franchise of the National Football League (NFL) and plays in the East Division of the National Football Conference.  The first draft in which the Cowboys participated was the 1961 NFL Draft.  Before their initial NFL Draft, the Cowboys franchise participated in the 1960 NFL Expansion Draft.  In the NFL Draft, each NFL franchise annually adds new players to its roster.  Teams are ranked in reverse order based on their records during the previous season, therefore the team with the worst record selects first.  There are two exceptions to this order: the Super Bowl champion from the previous season selects last, and the Super Bowl runner-up selects second to last.  Teams have the option of trading away their selections to other teams for different selections, players, cash, or any combination thereof.  It is common, therefore, for the actual draft selection of a team to differ from their initial assigned draft selection or for a team to have either extra selections or no selections in any round because of such trades.

Jerry Tubbs: Gerald J. Tubbs (January 23, 1935 – June 13, 2012) was an American football linebacker who played for ten seasons in the National Football League from 1957 to 1966, mainly for the Dallas Cowboys.  He was selected by the Dallas Cowboys in the 1960 NFL Expansion Draft.  After his retirement he stayed with the Cowboys as an assistant coach for 22 years.  He played college football at the University of Oklahoma.  In 1996, he was inducted into the College Football Hall of Fame.

1960 Washington Redskins season: The Washington Redskins involved the team's last-place finish in the NFL Eastern Conference, with a dismal 1–9–2 record under second-year head coach Mike Nixon.  The Redskins' only win that season was a 26–14 victory against the first-year expansionists Dallas Cowboys team on October 9 in Washington.

Jon Baker (placekicker): Jonathan David Baker (born August 13, 1972) is a former American football placekicker who played two seasons in the National Football League (NFL) with the Dallas Cowboys and Kansas City Chiefs.  He played college football at Arizona State University and attended Foothill High School in Bakersfield, California.  Baker was also a member of the Scottish Claymores of NFL Europe and the Hamilton Tiger-Cats, Edmonton Eskimos and BC Lions of the Canadian Football League.  He was a member of the Dallas Cowboys team that won Super Bowl XXX over the Pittsburgh Steelers.

Ken Gray (American football): Kenneth Don Gray (born March 10, 1936 in San Saba, Texas) was an offensive guard who played 13 seasons in the National Football League for the Chicago Cardinals/St. Louis Cardinals and the Houston Oilers.  Gray attended and played football for four seasons at Howard Payne University.  His first NFL contract, in 1958, paid him $6,000.00.  In those days the league was composed of 12 teams, split into two divisions.  After retiring as a player, earning six All-Pro awards, he served for three years as head coach at his high school alma mater, Llano High and offensive line coach for the 1977 AFC Champion Denver Bronco team that earned its way to Super Bowl XII, to play against the Dallas Cowboys.  In 2016, he was inducted into the Texas Sports Hall of Fame along with former University of Texas head football coach Fred Akers, former Dallas Cowboys offensive lineman Larry Allen and former Major League Baseball pitcher Andy Pettitte.  He earned a spot on the St. Louis Cardinals’ All-Time Team and the NFL All-1960s Team.  A Christian, Gray first and foremost considers himself blessed with his lovely and gracious wife, Shirley, who has stood by him through all the years of risking injury in high school, college and league play, and the unique challenges of his coaching years to the present.  They met and were wed back in their high school days at Llano High School.  Their union produced two fine sons, Shane and Boyd and a grand child, Garret.

Question: Where was the coach of the 1996 Dallas Cowboys team a college coach?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the head coach for the specified NFL team and season."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the NFL team coached."
    },
    "season_year": {
      "type": "integer",
      "description": "The year of the NFL season."
    },
    "college_coached": {
      "type": "string",
      "description": "The name of the university where the coach previously served as a college coach."
    }
  },
  "required": [
    "coach_name",
    "team_name",
    "season_year",
    "college_coached"
  ],
  "additionalProperties": false
}
