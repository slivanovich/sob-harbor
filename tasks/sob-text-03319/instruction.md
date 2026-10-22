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
Wade Phillips: Harold Wade Phillips (born June 21, 1947) is an American football coach who is the defensive coordinator for the Los Angeles Rams of the National Football League (NFL).  He is the former head coach and Defensive Coordinator of the NFL's Denver Broncos, Buffalo Bills, and Dallas Cowboys.  He was also an interim head coach for the New Orleans Saints, Atlanta Falcons, and the Houston Texans.  His career winning percentage as a head coach is .562.  He was a part of the Denver Broncos Super Bowl 50 championship team over the Carolina Panthers.

Campbell Fighting Camels football: The Campbell Fighting Camels football program is the intercollegiate American football team for Campbell University located in the U.S. state of North Carolina.  The team competes in the NCAA Division I Football Championship Subdivision (FCS) and are members of the Pioneer Football League, one of two members in North Carolina (the other being Davidson).  Campbell's first football team was fielded in 2008.  The team plays its home games at the 5,000 seat Barker–Lane Stadium in Buies Creek, North Carolina.  The Fighting Camels were coached by Dale Steele from 2008–2012.  Campbell announced on November 5, 2012 that they would not retain head coach Dale Steele following the conclusion of the 2012 season.  Steele was the head coach for the Camels for six years compiling a 14–41 record.  On November 27, 2012, it was announced that Mike Minter, former safety for the National Football League's Carolina Panthers would be the head coach.

Michael Bates (American football): At the 1992 NFL draft combine, Bates ran a 4.4 40, a full tenth of a second faster than top RB prospect Vaughn Dunbar and almost 2 tenths of a second than any of the other 34 halfbacks tested.  Bates was the 150th overall selection by the Seattle Seahawks in the 1992 NFL Draft, but due to contract negotiations, he did not sign with Seattle and held out the 1992 season.  In March of 1993 Bates signed an incentive laden contract including a $15k workout bonus, $10k playoff percentage time bonus and over $50k in performance bonus.  In 1995 Bates was an exclusive rights free agent where Seattle ended up agreeing to terms with him on a 1 year $700k deal in July after new head coach Dennis Erickson traded for Ricky Proehl and drafted Joey Galloway, Bates became expendable and was waived August 28.  The Carolina Panthers claimed Bates off waivers only to turn around and trade him the next day to the Cleveland Browns for Travis Hill.  Bates spent the end of the 95 season on the inactive list and was not retained.  1996 began his great run of seasons where he signed with the Carolina Panthers, he had 9,154 total yards in kick returns and five kick-return touchdowns (the NFL record for kickoff return touchdowns in a career is six).  In one of his best seasons, 1996, he returned 33 kicks for 998 yards - a remarkable average of 30.2 yards per return - and one kick return touchdown.  Bates was selected to the NFL 1990s All-Decade Team.  After five seasons in Carolina, Bates was let go and the Redskins signed Bates to a 2-year $1.33million contract.  Bates was let go after just one season and Carolina picked Bates back up for the 2002 season.  His season was cut short that year however due to a broken ankle in the preseason.  Bates was re-signed for the 2003 season with Carolina but was let go in the final cut down process for the regular season.  After that Bates was signed by the Jets but once again injuries placed Bates on injured reserve in November of 2003.  Bates was subsequently waived by the Jets and was able to sign with the Cowboys in late December and play for the Cowboys in their playoff run.

Mike Shula: Mike Shula (born June 3, 1965) is an American football coach who is the offensive coordinator for the Carolina Panthers of the National Football League (NFL).  Shula has been with the Panthers since 2011, when he was hired as their quarterbacks coach.  He was promoted to offensive coordinator after Rob Chudzinski was hired to be the head coach of the Cleveland Browns.  Shula served as the head football coach at the University of Alabama, his alma mater, for four seasons, from 2003 to 2006.

Brett Maxie: Brett Derrell Maxie (born January 13, 1962) is an American football coach and former player who is the defensive backs coach for the Tampa Bay Buccaneers of the National Football League (NFL).  He has been a defensive back for 13 seasons for the NFL's New Orleans Saints, Atlanta Falcons, Carolina Panthers, and San Francisco 49ers.  He spent the 2007-08 NFL season as a defensive assistant with the Miami Dolphins.  On February 11, 2008 Maxie was named the assistant defensive coach with the Dallas Cowboys under Dave Campo.  Maxie played college football at Texas Southern University.

2016 Carolina Panthers season: The 2016 Carolina Panthers season was the franchise's 22nd season in the National Football League and the sixth under head coach Ron Rivera.  It was also the team's 20th season at Bank of America Stadium.  The previous year, the Panthers achieved their highest win total in franchise history with a 15–1 record.  They entered the 2016 season as the defending NFC champions and NFC South champions and hope to repeat as NFC champions, but after a 1–5 start, their worst since 2004 (where they also were defending NFC Champions), the Panthers finished the season at 6–10, missing the playoffs for the first time since 2012.  The Panthers struggled throughout the 2016 season with injuries and lost of star players via Free Agency and retirement.  The Panthers became the first team in NFL history to go 15–1 and miss the playoffs the following year, the first runners up in the Super Bowl to miss the playoffs the next year since the 2008 Patriots, and failed to win the NFC South for the first time in three seasons.  This was also the first team to have at least 15 wins and finish last in their division the following season.

2012 Carolina Panthers season: The Carolina Panthers season was the franchise's 18th season in the National Football League and the second under head coach Ron Rivera.  A day after the Panthers loss to Dallas, general manager Marty Hurney was fired.  Until a new general manager was hired (that hire eventually being Dave Gettleman), director of football operations Brandon Beane served as interim GM.  In a statistical rarity, the team lost the first 13 of their coin tosses, an event with a 1 in 8,192 probability.  In the thirteenth game, the Panthers asked fans on Facebook to make the call, but the vote ended in a 50/50 tie.

2017 Carolina Panthers season: The 2017 Carolina Panthers season is the franchise's 23rd season in the National Football League and the seventh under head coach Ron Rivera.  The Panthers will come off of a disappointing 2016 campaign where they finished 6–10 and last in the NFC South.  For the first time since 2011, the Panthers will not play the Seattle Seahawks during the regular season.  During the offseason, the team's notable free agent signings included Matt Kalil, Captain Munnerlyn, and Julius Peppers.  The latter spent his first eight seasons with the Panthers.  On July 17, 2017, the team announced Dave Gettleman had been relieved as general manager.

Gil Haskell: Gil Haskell (born September 24, 1943) is a long time National Football League (NFL) coach and the former offensive coordinator of the Seattle Seahawks.  He began his career in the NFL as a ball boy with the San Francisco 49ers while his uncle Dr. William O’Grady was a part owner of the franchise.  Coach Haskell grew up in St. Brendan's Parish in San Francisco, graduated from St. Ignatius High School in 1961, played at San Francisco State, and then was head coach at St. Ignatius from 1973–1977.  Haskell then left for USC, spending 5 seasons as an assistant coach.  He broke into the NFL as a coach in 1983 with the Los Angeles Rams, coaching special teams, running backs and tight ends for 9 seasons.  In 1992, he joined the Green Bay Packers where he became part of Mike Holmgren's staff for the first time as a running back coach and wide receiver coach.  When Holmgren left Green Bay for the Seattle Seahawks in 1998 Haskell accepted the Offensive Coordinator position with the Carolina Panthers.  The next season, he reunited with Holmgren in Seattle in the same role.  He has indicated that he would like to be a head coach in the NFL and even launched a low key campaign for the Oakland Raiders position when the Raiders fired Norv Turner after the 2005 season.  That position was eventually filled with the hiring of Art Shell.

Ron Rivera: Ronald Eugene Rivera (born January 7, 1962) is an American football coach and former player who is the head coach of the Carolina Panthers of the National Football League (NFL).

Question: What coach, born January 7, 1962 was head coach of the Carolina Panthers when they managed to lose the first 13 of their coin tosses?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the American football coach."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the coach in YYYY-MM-DD format."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the coach was associated with during the specified event."
    },
    "coach_role": {
      "type": "string",
      "description": "The role of the coach for the specified team."
    },
    "season_year": {
      "type": "integer",
      "description": "The year of the season when the event occurred."
    },
    "event_details": {
      "type": "string",
      "description": "A description of the specific event related to the team's coin tosses."
    }
  },
  "required": [
    "coach_name",
    "birth_date",
    "team_name",
    "coach_role",
    "season_year",
    "event_details"
  ],
  "additionalProperties": false
}
