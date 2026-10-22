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
Ben Petrick: Benjamin Wayne Petrick (born April 7, 1977) is a former Major League Baseball player.  A native of Oregon, he grew-up in Hillsboro, Oregon, in the Portland metropolitan area.  After reaching the Majors, he was diagnosed with Parkinson's disease and retired in 2004 and returned to Hillsboro to coach at his old high school.  As of 2013 he has been a consultant for the Hillsboro Hops, a minor-league affiliate of the Arizona Diamondbacks, helping the team's young players acclimatize to life as a professional baseball player.

Salem Senators: The Salem Senators was the longest lasting name used by several minor league baseball teams based in Salem in the U.S. state of Oregon.  The team name derived from Salem being the capital of Oregon.  The team was founded in 1940.  A later incarnation started in 1977 remains in the Northwest League as the current Hillsboro Hops.

Trade (sports): In North American professional sports, a trade is a sports league transaction between sports clubs that involves an exchange of players from one club/team to another.  Though players are the primary trading assets, draft picks and/or cash are other assets that may be supplemented to consummate a trade, either packaged alongside players' contracts to be transferred to another team, or as standalone assets in exchange for players' contracts and/or draft picks in return.  In Major League Baseball, a player to be named later can be used to finalize the terms of a trade at a later date, but draft picks are not admissible as trading assets (with one exception).  In Major League Soccer, besides current MLS players and draft picks, clubs may also trade MLS rights to non-MLS players, allocation money, allocation rankings, and international player slots.  Typically, trades are completed between two clubs, but there are instances where trades are consummated among three or more clubs.

Ron Tonkin Field: Ron Tonkin Field, originally Hillsboro Ballpark, is a baseball park in Hillsboro in the U.S. state of Oregon.  The stadium has a capacity of 4,500 spectators (3,534 seats) and is the home for the Hillsboro Hops, a team in the short season Northwest League.  Groundbreaking for the $15.55 million venue was held on September 21, 2012, with the first game played on June 17, 2013.

Yakima Bears: The Yakima Bears were a minor league baseball team in the northwest United States, located in Yakima, Washington.  They were in the short-season Class A Northwest League and had been a farm team of the Arizona Diamondbacks from 2001 until moving to Hillsboro, Oregon after the 2012 season and becoming the Hillsboro Hops.  The Bears were previously affiliated with the Los Angeles Dodgers from the team's creation in 1990 when the Salem Dodgers were moved to Yakima.  The Bears played their home games at Yakima County Stadium, which opened in 1993 and succeeded Parker Field.

Yakima Valley Pippins: The Yakima Valley Pippins are a collegiate wood bat baseball team based in Yakima, Washington.  They are member of the West Coast League and began play in 2014 at the 3,000-seat Yakima County Stadium.  They replaced the Yakima Bears of the Northwest League, who relocated to Hillsboro, Oregon, and were renamed the Hillsboro Hops.  They were named for the pippin apple.  On August 6, 2014, the Pippins were the first WCL expansion franchise to win a divisional pennant, beating the Cowlitz Black Bears 6-5 in the bottom of the 9th inning.  After missing the playoffs in 2015, the Pippins returned to post season play, winning the 2nd Half South Division Title.  The Pippins hold the West Coast League record for most wins in their first two seasons going 64-44 in 2014-2015.

Professional sports in Canada: There are professional teams based in Canada in several professional sports leagues.  The National Hockey League has seven Canadian franchises and is the most popular professional sports league in Canada.  The second most popular sports league in Canada is the Canadian Football League.  Major League Baseball, the National Basketball Association and Major League Soccer are also popular in Canada, more so in Ontario than the rest of the country.

2004–05 NHL lockout: The 2004–05 NHL lockout was a lockout that resulted in the cancellation of what would have been the 88th season of play of the National Hockey League (NHL).  It was the first time the Stanley Cup was not awarded since 1919, and the first time a major professional sports league in North America canceled a complete season because of a labor dispute and the second time after the 1994–1995 MLB strike that the Playoffs of a major professional sports league in North America were cancelled.  The lockout lasted 10 months and 6 days starting September 16, 2004, the day after the collective bargaining agreement (CBA) between the NHL and the NHL Players Association (NHLPA) that resolved the 1994–95 lockout expired.  The lockout of the 2004–2005 season resulted in 1,230 unplayed games.  The negotiating teams reached an agreement on July 13, 2005, and the lockout officially ended 9 days later on July 22, after both the NHL owners and players ratified the CBA.

Minor League Baseball: Minor League Baseball is a hierarchy of professional baseball leagues in the Americas that compete at levels below Major League Baseball (MLB) and provide opportunities for player development and a way to prepare for the major leagues.  All of the minor leagues are operated as independent businesses.  Most are members of the umbrella organization known as Minor League Baseball (MiLB), which operates under the Commissioner of Baseball within the scope of organized baseball.  Several leagues, known as independent baseball leagues, do not have any official links to Major League Baseball.

Hillsboro Hops: The Hillsboro Hops are a minor league baseball team in the northwest United States, located in Hillsboro, Oregon, a suburb west of Portland.  The team was founded in 2013 after the Yakima Bears moved to Hillsboro after the 2012 season.

Question: The Hillsboro Hops prepare players for what professional American sports league?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The name of the minor league team."
    },
    "league_type": {
      "type": "string",
      "description": "The type of league the team belongs to (e.g., Minor League Baseball)."
    },
    "prepares_for_league": {
      "type": "string",
      "description": "The name of the professional American sports league for which players are prepared."
    },
    "parent_league_type": {
      "type": "string",
      "description": "The general category of the league for which players are prepared (e.g., Professional American Sports League)."
    },
    "parent_team_affiliation": {
      "type": "string",
      "description": "The specific Major League Baseball team the minor league team is affiliated with."
    }
  },
  "required": [
    "team_name",
    "league_type",
    "prepares_for_league",
    "parent_league_type",
    "parent_team_affiliation"
  ],
  "additionalProperties": false
}
