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
John Brownlee (basketball): John Brownlee (born in Fort Worth, Texas) is a former American professional basketball player.  He is listed at 6'10" and 230 lbs.  He played his first two years of college basketball at the University of North Carolina at Chapel Hill.  He played just 13 games in his freshman year, averaging 0.7 points per game.  In his sophomore season, however, he played 33 games and averaged 1.3 points per game as the designated back up to center Sam Perkins as the Tar Heels won the 1981-82 NCAA Men's Basketball championship.  He then transferred to The University of Texas at Austin.  He played 28 games in his third season of college basketball, averaging 13.8 points per game.  In his final year, he took part in 31 games for the Longhorns and led the team in scoring with a 17.0 points per game average.  This earned him the 1986 Southwest Conference Player of the Year.  Brownlee was selected in the fourth round (78th pick overall) of the 1986 NBA Draft by the Los Angeles Clippers.  During rookie-free agent camp, Brownlee suffered an injury when he dislocated his little finger during scrimmage.  He never got his chance to play in the NBA.  He then travelled overseas to France and Belgium to play professionally for 4 years.

Providence Friars: The Providence Friars is the name of the athletic teams of Providence College.  They compete in the Big East Conference (NCAA Division I) for every sport except for ice hockey, where they compete in Hockey East.  The Big East Conference was founded in 1979 by former athletic director and men's basketball coach Dave Gavitt.  On December 15, 2012, Providence and the other seven Catholic, non-FBS schools announced that they were departing the Big East for a new conference; on March 7, 2013, it was officially confirmed that Providence's new conference would operate under the Big East name.  The women's volleyball team, which had been an associate member of the America East Conference before the Big East split, remained in that conference for one more season before joining the Big East for the 2014 season.

2006 Big East Men's Basketball Tournament: The 2006 Big East Men's Basketball Championship was played from March 8 to March 11, 2006.  The tournament took place at Madison Square Garden in New York City.  It was a single-elimination tournament with four rounds.  Villanova and Connecticut tied for the best regular season conference record.  Based on tie-breakers, Connecticut was awarded the #1 seed. <br>

2005 Big East Men's Basketball Tournament: The 2005 Big East Men's Basketball Championship was played from March 9 to March 12, 2005.  The tournament took place at Madison Square Garden in New York City.  The Syracuse Orange won the tournament and were awarded an automatic bid to the 2005 NCAA Men's Division I Basketball Tournament.

Kemba Walker: Kemba Hudley Walker (born May 8, 1990) is an American professional basketball player for the Charlotte Hornets of the National Basketball Association (NBA).  Walker was drafted ninth overall by the Charlotte Bobcats in the 2011 NBA draft.  Walker grew up in The Bronx, New York, and graduated from Rice High School in 2008.  Walker played college basketball for the Connecticut men's basketball team.  In the 2010–11 season, Walker was unanimously selected for the All-Big East first team, Walker was the second-leading college basketball scorer in the United States and led the Huskies to the 2011 Big East championship and 2011 NCAA championship and was named as the tournament's most outstanding player for both championships.

Luke Harangody: Luke Harangody (born January 2, 1988) is an American professional basketball player for ratiopharm Ulm of the German Basketball Bundesliga.  He completed his college career at the University of Notre Dame in 2010.  He is the only men's player in the history of the Big East Conference to average 20 points and 10 rebounds per game in conference play for his career.  He was the 2008 Big East Player of the Year, and was named to the second team on the 2008 Associated Press All-America team.  He is also the first Notre Dame men's player to be a three-time first-team All-Big East selection (and just 11th overall) (2008–2010), and the first men's player to lead the conference in both scoring and rebounding in consecutive seasons (2008 and 2009).

1986–87 Georgetown Hoyas men's basketball team: The 1986–87 Georgetown Hoyas men's basketball team represented Georgetown University in the 1986–87 NCAA Division I basketball season.  John Thompson, Jr., coached them in his 15th season as head coach.  They played their home games at the Capital Centre in Landover, Maryland.  They were members of the Big East Conference and finished the season with a record of 29-5, 12-4 in Big East play.  They shared the conference regular season championship with Pittsburgh and Syracuse and won the 1987 Big East Men's Basketball Tournament, defeating Syracuse in the final game for the fifth Big East Tournament championship in Georgetown men's basketball history.  They advanced to the East Region final of the 1987 NCAA Tournament before losing to Providence.  Nicknamed "Reggie and the Miracles," the team was ranked No. 4 in the season' s final Associated Press Poll and Coaches' Poll.

2007 Big East Men's Basketball Tournament: The 2007 Big East Men's Basketball Championship was played from March 7 to March 10, 2007.  The tournament took place at Madison Square Garden in New York City and was sponsored by Aéropostale.  The Georgetown Hoyas won the tournament for the first time since 1989 and the seventh time overall, and were awarded an automatic bid to the 2007 NCAA Men's Basketball Tournament.  Jeff Green of Georgetown was given the Dave Gavitt Trophy, awarded to the tournament's most outstanding player.

Big East Men's Basketball Tournament: The Big East Men's Basketball Tournament is the championship tournament of the Big East Conference in men's basketball.  The winner receives the conference's automatic bid to the NCAA Men's Division I Basketball Championship.  Since 1983, the tournament has been held in Madison Square Garden, New York City.  As such, the tournament is the longest running conference tournament at any one site in all of college basketball.

Jeff Green (basketball): Jeffrey Lynn Green (born August 28, 1986) is an American professional basketball player for the Cleveland Cavaliers of the National Basketball Association (NBA).  He played three seasons of college basketball for Georgetown, before entering the 2007 NBA draft, where he was selected fifth overall by the Boston Celtics.  He was subsequently traded to the Seattle SuperSonics (now known as the Oklahoma City Thunder).  He spent four seasons with the franchise before being traded back to the Celtics during the 2010–11 season, where he played until 2015 before being traded to the Memphis Grizzlies.  In 2016, he was traded to the Los Angeles Clippers.  He spent half a season with the Clippers before joining the Magic following the 2015–16 season.

Question: What American professional basketball player born in 1986 was awarded the Dave Gavitt Trophy during the 2007 Big East Men's Basketball Championship? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the professional basketball player."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the player."
    },
    "award_name": {
      "type": "string",
      "description": "The name of the award received by the player."
    },
    "tournament_year": {
      "type": "integer",
      "description": "The year the tournament took place."
    },
    "college_team": {
      "type": "string",
      "description": "The college team the player represented when receiving the award."
    }
  },
  "required": [
    "player_name",
    "birth_year",
    "award_name",
    "tournament_year",
    "college_team"
  ],
  "additionalProperties": false
}
