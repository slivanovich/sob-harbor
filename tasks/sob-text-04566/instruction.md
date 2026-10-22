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
Grant Sasser: Grant Sasser (born February 13, 1964 in Portland, Oregon) is an American retired professional ice hockey player who played three games in the National Hockey League.  He played for the Pittsburgh Penguins and was the first Oregon native to participate in an NHL game.  Sasser played junior hockey for the hometown Portland Winterhawks. 

Mathew Dumba: Mathew Dumba (born July 25, 1994) is a Canadian ice hockey defenceman.  He is currently playing for the Minnesota Wild of the National Hockey League (NHL).  The Wild selected him with the seventh overall pick in the first round of the 2012 NHL Entry Draft.  Dumba previously played junior with the Red Deer Rebels and briefly for the Portland Winterhawks of the Western Hockey League (WHL).

Artis Ābols: Artis Ābols (born January 3, 1973) is a retired Latvian ice hockey forward who is currently the head coach of Lada Togliatti in the Kontinental Hockey League.  His son, Rodrigo Ābols, is also an ice hockey player currently with the Portland Winterhawks of the major junior Western Hockey League and was selected by the Vancouver Canucks in the 2016 NHL Entry Draft.

Portland Winterhawks: The Portland Winterhawks are an American major junior ice hockey team based in Portland, Oregon, playing in the Western Hockey League (WHL), one of three leagues making up the Canadian Hockey League (CHL).  The Winterhawks split their home games between the Moda Center (most games) and the Memorial Coliseum.  They are one of the most successful teams in terms of producing National Hockey League (NHL) alumni, a list that includes Sven Baertschi, Joe Morrow, Ryan Johansen, Braydon Coburn, Adam Deadmarsh, Rob Klinkhammer, Brandon Dubinsky, Tyler Wotherspoon, Andrew Ference, Paul Gaustad, Jannik Hansen, Marian Hossa, Seth Jones, Brenden Morrow, Nino Niederreiter, Mike Vernon, Glen Wesley and Hall of Famers Mark Messier and Cam Neely.

Nino Niederreiter: Nino Niederreiter (born 8 September 1992), nicknamed El Niño, is a Swiss ice hockey player currently playing for the Minnesota Wild of the National Hockey League (NHL).  He was selected fifth overall by the New York Islanders in the 2010 NHL Entry Draft, making him the highest-drafted Swiss hockey player in NHL history at the time until Nico Hischier was drafted first overall.  Niederreiter made his NHL debut with the Islanders early in the 2010–11 season before being returned to his junior club, the Portland Winterhawks of the Western Hockey League (WHL).  Prior to coming over to North America Niederreiter had played in the junior system of the Swiss team HC Davos, and appeared in three playoff games for the senior club in 2010.  He was traded to the Minnesota Wild on 30 June 2013 for Cal Clutterbuck and a third round pick in the 2013 NHL Entry Draft.

Mike Johnston (ice hockey): Mike Johnston (born February 19, 1957) is the head coach and general manager of the Portland Winterhawks hockey team of the Western Hockey League.  He previously coached the Pittsburgh Penguins of the NHL from 2014-15.  He was relieved of his duties on December 12, 2015.  He was replaced by Wilkes-Barre/Scranton Penguins (AHL) Head Coach Mike Sullivan.  Johnston performed duties as the coach and general manager of the Winterhawks previously from 2008 to 2014, before taking over as coach of the Penguins for the 2014-15 NHL season.  Before his tenure with Portland, he was an assistant coach for the Los Angeles Kings and the Vancouver Canucks. .  He is the uncle of the NHL hockey player, Ryan Johnston.

Wes Walz: Wesley Walz (born May 15, 1970) is a retired Canadian professional ice hockey player and former assistant coach with the Tampa Bay Lightning of the National Hockey League (NHL).  Wes currently works as a sports analyst on Fox Sports North for the Minnesota Wild Hockey Club.  Walz volunteered as head coach with the Raptors of East Ridge High School, Woodbury, Minnesota.  There he coached his son, Kelvin, on the boys varsity ice hockey team and a few years later he coached his daughter, Jaedyn, on the girls varsity hockey team.  Previously, he played centre for the Minnesota Wild of the NHL and served as team captain.  Walz played in 607 NHL games in 11 seasons with Boston, Philadelphia, Calgary, Detroit, and Minnesota.  He had 260 points (109 goals, 151 assists) and 343 penalty minutes and earned 40 career multi-point games.

Kieffer Bellows: Kieffer Bellows (born June 10, 1998) is an American ice hockey player, currently playing for the Portland Winterhawks of the Western Hockey League (WHL).  He is the son of former Canadian NHL All-Star Brian Bellows.  He was drafted in the first round (19th overall) of the 2016 NHL Entry Draft by the New York Islanders.

List of sports venues in Portland, Oregon: The following is a list of sports venues in Portland, Oregon, specifically the metro area, that are currently in operation or defunct.  The city features two major sports franchises, the Portland Timbers of Major League Soccer (MLS) and the Portland Trail Blazers of the National Basketball Association (NBA).  The Portland Winterhawks, who are major junior ice hockey franchise in the Western Hockey League, have played in the city since 1976 when the Edmonton Oil Kings were relocated.  They are a unique team in that they have two venues, the Moda Center and the Veterans Memorial Coliseum.  Providence Park, a 20,323 seat open-air stadium which is the home of the Timbers and the Portland State Vikings football team, is the largest non-auto sports venue in Portland.  The Moda Center, formerly the Rose Garden, is a close second with 19,980 seats for basketball games and slightly less for hockey match-ups.  Portland International Raceway in Hayden Meadows has the largest seating capacity (30,000) of any sporting venue in Portland.  There are several golf courses in the Portland metro area, including the Portland Golf Club where the 1946 PGA Championship was held.

2013 Memorial Cup: The 2013 Memorial Cup was a four-team, round-robin format ice hockey tournament played from May 17–26, 2013.  It was the 95th Memorial Cup championship and determined the champion of the Canadian Hockey League (CHL).  The tournament featured the London Knights, champions of the Ontario Hockey League, the Halifax Mooseheads, champions of the Quebec Major Junior Hockey League, the Portland Winterhawks, champions of the Western Hockey League, and the Saskatoon Blades, who won the right to host the tournament over bids by the Kelowna Rockets and the Red Deer Rebels.  This was the first Memorial Cup to be held in Saskatoon since the Blades hosted it in 1989.  The Halifax Mooseheads won the Memorial Cup for the first time in franchise history, beating the Portland Winterhawks 6-4 in the final.  The Halifax Mooseheads joined the Saint John Sea Dogs in 2011, and the Shawinigan Cataractes in 2012, as the third straight team from the QMJHL to capture the trophy.

Question: The Portland Winterhawks have produced alumni which include the Swiss hockey player for the Minnesota Wild nicknamed what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the ice hockey player."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the player."
    },
    "current_nhl_team": {
      "type": "string",
      "description": "The current NHL team the player is playing for."
    },
    "junior_team_alumni": {
      "type": "string",
      "description": "The junior team the player was an alumni of."
    },
    "player_nickname": {
      "type": "string",
      "description": "The nickname of the player."
    }
  },
  "required": [
    "player_name",
    "nationality",
    "current_nhl_team",
    "junior_team_alumni",
    "player_nickname"
  ],
  "additionalProperties": false
}
