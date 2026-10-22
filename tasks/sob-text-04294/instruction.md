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
Clemson–South Carolina football brawl: The Clemson–South Carolina football brawl was an on-field altercation during an NCAA game between football players from the University of South Carolina and Clemson University.  The incident took place on November 20, 2004 at the Memorial Stadium in Clemson, South Carolina.  This disturbance led to serious repercussions handed down for those involved from the SEC (South Carolina's conference) and the ACC (Clemson's conference).  This took place the day after a notable brawl at an NBA game in Detroit," the "Malice at the Palace".

Technical foul: In basketball, a technical foul (also colloquially known as a "T" or a "Tech") is any infraction of the rules penalized as a foul which does not involve physical contact during the course of play between opposing players on the court, or is a foul by a non-player.  The most common technical foul is for unsportsmanlike conduct.  Technical fouls can be assessed against players, bench personnel, the entire team (often called a bench technical), or even the crowd.  These fouls, and their penalties, are more serious than a personal foul, but not necessarily as serious as a flagrant foul (an ejectable offense in leagues below the NBA, and potentially so in the NBA).

Bonus (basketball): In the sport of basketball, the bonus situation (also called the penalty situation) occurs when one team accumulates a requisite number of fouls, which number varies depending on the level of play.  When one team has committed the requisite number of fouls, each subsequent foul results in the opposing team's taking free throws regardless of the type of foul committed (i.e., whether the foul was a shooting foul).  Teams under the limit are commonly referred to as having fouls to give, and thus they can try to disrupt their opponents without being penalized free throws.  These fouls reset every quarter or half depending on the rules in use (i.e. FIBA, NBA, NCAA, etc.).

97th Grey Cup: The 97th Grey Cup was played on November 29, 2009, at McMahon Stadium in Calgary, Alberta, and decided the Canadian Football League (CFL) champion for the 2009 season.  The Montreal Alouettes came from behind to defeat the Saskatchewan Roughriders 28-27, on a 33-yard field goal by Damon Duval as time ran out.  Duval had actually missed a first attempt, but Saskatchewan was penalized for having too many men on the field, allowing Duval a second field goal attempt.

Backboard shattering: A backboard shattering is an accident or stunt in basketball.  It occurs when a player slam dunks the ball hard enough to break the 1/2" tempered safety glass of the backboard.  The stunt has caused games to be canceled or delayed, serious injuries to occur and expensive costs of cleanup and replacement.  Shattering a backboard is extremely dangerous, sending shards of glass flying over the players and fans.  In the National Basketball Association (NBA), shattering a backboard during a game is penalized with a non-unsportsmanlike conduct technical foul and a possible fine towards the player.  The player may not be ejected, nor shall the foul count towards a player's total towards either ejection or suspension.

Knicks–Nuggets brawl: The Knicks–Nuggets brawl was an on-court altercation at a National Basketball Association (NBA) game between the New York Knicks and Denver Nuggets at Madison Square Garden in New York City on December 16, 2006.  This altercation was the most penalized on-court fight in the NBA since the Pacers–Pistons brawl two years before.

Law of Political Responsibilities: The Law of Political Responsibilities ("Ley de Responsabilidades Políticas") was a law issued by the Francoist dictatorship on 13 February 1939 two months before the end of the Spanish Civil War.  The Law targeted all loyalist supporters of the Second Spanish Republic and penalized membership in the Popular Front of the defeated republic.

Sean Lucas: Sean Christopher Lucas (born December 8, 1983) is a retired Canadian football linebacker who played all six years of his career for the Saskatchewan Roughriders of the Canadian Football League.  He was a part of Saskatchewan's Grey Cup win in 2007 and was named a CFL West All-Star in 2009.  Lucas was widely regarded as the Saskatchewan player at the centre of the infamous 13th Man incident that cost the club the championship in 2009.  Lucas was named in football circles as the extra player who was on the field when Montreal kicker Damon Duval missed a 43-yard field goal as time expired, seemingly giving Saskatchewan the win.  But Duval got a second chance from 33 yards after the Riders were penalized for too many men.  Duval converted to give Montreal a thrilling 28-27 victory.  The Riders have never said who the extra man was, but video replays did show Lucas start off the field, then turn and stay on for Duval's attempt in the most heart-breaking finish in Grey Cup history.

Pacers–Pistons brawl: The Pacers–Pistons brawl (colloquially known as the Malice at the Palace or Basketbrawl) was an altercation that occurred in a National Basketball Association (NBA) game between the Indiana Pacers and the Detroit Pistons on November 19, 2004, at The Palace of Auburn Hills in Auburn Hills, Michigan.  The Associated Press (AP) called it "the most infamous brawl in NBA history".

Yasuaki Taiho: Yasuaki Taiho, also known by his Chinese name Chen Tai-feng, (15 November 1963 – 18 January 2015) was a Taiwanese professional baseball player in Nippon Professional Baseball for the Hanshin Tigers and Chunichi Dragons.  He was picked in the second round of the 1988 draft and debuted the next year.  In June 1997, Taiho was involved in an altercation with Mike DiMuro.  The American umpire had arrived in March to show Japanese leagues the Major League Baseball officiating standard.  Taiho disagreed with DiMuro's strike zone and was ejected.  Taiho pushed DiMuro in protest, and his teammates streamed onto the field.  No player was penalized for their actions.  DiMuro, surprised by this show of disrespect, resigned from NPB and returned to the United States.  After his retirement from baseball, Taiho worked as a scout and Little League coach.  He also ran Chinese restaurants in Kaizu and Nagoya, where he died of acute myeloid leukemia on 18 January 2015.

Question: Where was the second most penalized brawl in the NBA?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "brawl_name": {
      "type": "string",
      "description": "The name of the basketball brawl."
    },
    "location": {
      "type": "string",
      "description": "The venue where the brawl took place."
    },
    "league": {
      "type": "string",
      "description": "The sports league in which the brawl occurred."
    },
    "penalty_ranking_description": {
      "type": "string",
      "description": "A description of the brawl's ranking in terms of penalties within its league."
    }
  },
  "required": [
    "brawl_name",
    "location",
    "league",
    "penalty_ranking_description"
  ],
  "additionalProperties": false
}
