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
Evan Oberg: Evan Oberg (born February 16, 1988) is a Canadian professional ice hockey defenceman.  He currently plays for the Lacombe Generals of the Allan Cup Hockey West (ACHW), a semi-professional league in Alberta, Canada.  Prior to that he played with the Augsburger Panther of the Deutsche Eishockey Liga (DEL).  Oberg played junior for the Camrose Kodiaks of the Alberta Junior Hockey League (AJHL), before spending two seasons at the University of Minnesota-Duluth.  Unselected in the NHL Entry Draft, Oberg was signed by the Vancouver Canucks of the National Hockey League (NHL) as a free agent in 2009.  He played two seasons with the Canucks American Hockey League (AHL) affiliate, the Manitoba Moose, appearing in four games for the Canucks.  Oberg was then traded to the Florida Panthers in 2011, and spent the remainder of the season with their AHL affiliate, the Rochester Americans.  Oberg moved to the Panthers new affiliate, the San Antonio Rampage, and was subsequently traded to the Tampa Bay Lightning, who assigned Oberg to their affiliate, the Norfolk Admirals.

New York Rangers: The New York Rangers are a professional ice hockey team based in New York City.  They are members of the Metropolitan Division of the Eastern Conference of the National Hockey League (NHL).  The team plays its home games at Madison Square Garden, located in the borough of Manhattan.  The Rangers are one of three NHL franchises in the New York metropolitan area, along with the New Jersey Devils and New York Islanders.  The club is also one of the oldest teams in the NHL, having joined in 1926 as an expansion franchise.  They are part of the group of teams referred to as the Original Six, along with the Boston Bruins, Chicago Blackhawks, Detroit Red Wings, Montreal Canadiens and Toronto Maple Leafs.  The Rangers were the first NHL franchise in the United States to win the Stanley Cup, which they have done four times, most recently in 1993–94.

Edward Leier: Edward "Eddie" Leier (born 3 November 1927) is a Polish-born former baseball player, track athlete, and ice hockey player.  He played two seasons with the Chicago Black Hawks of the National Hockey League.  He was named to the Manitoba Junior Hockey League Second All-Star Team in 1948.  On 29 September 1948 he signed as a free agent to the Saskatoon Quakers of the Western Canada Senior Hockey League.

Mike Walsh (ice hockey, born 1962): Michael Walsh (born April 3, 1962) is an American former professional ice hockey player who played in the National Hockey League (NHL).  After four seasons playing for Colgate University's men's ice hockey team, Walsh spent the first two seasons of his professional career with Malmö IF in Sweden.  Towards the end of the 1985–86 season he returned to North America, playing in two games for the Springfield Indians of the American Hockey League (AHL).  Walsh signed a contract in the off-season with Springfield's parent team, the New York Islanders, and played the next four seasons with the organization.  He played in 14 games over parts of two NHL seasons with the Islanders.  After the 1989–90 season, during which he was a member of Springfield's Calder Cup winning team, Walsh played a season in Italy for SG Cortina.  He played two more seasons in the AHL before retiring after the 1992–93 season.  Following his playing career Walsh became a head coach, coaching at the Tilton School and currently Proctor Academy.

Julien Hernandez: Julien Hernandez (born November 28, 1987) is an American professional ice hockey goalie.  He is currently an unrestricted free agent after last playing with Colorado Eagles of the East Coast Hockey League (ECHL).  He previously played two seasons of New England Prep School Hockey with Vermont Academy then started his collegiate career at St. Norbert College, winning the National Championship at Herb Brooks Arena in Lake Placid, New York.  Julien then turned professional, playing for Nijmegen Devils of the Netherlands where he helped the team win the championship in the Dutch Eredivisie.  The following season he joined the Steaua Rangers of the Hungarian (MOL Liga).  Later in his career he joined the Vail Yeti of the Mountain West Hockey League.  (MWHL)

Eric Vail: Eric "Big Train" Vail (born September 16, 1953) is a Canadian former ice hockey player who played nine seasons in the National Hockey League (NHL) for the Atlanta Flames, Calgary Flames and Detroit Red Wings.  He won the Calder Memorial Trophy in 1975 as the NHL's rookie of the year and played in the 1977 NHL All-Star Game.  Also in 1977, Vail played with Team Canada at the World Ice Hockey Championship.  At the time of his 1981 trade to Detroit, Vail was the Flames' franchise leader in goal scoring.

Michael Grabner: Michael-René Grabner (born 5 October 1987) is an Austrian professional ice hockey player for the New York Rangers of the National Hockey League (NHL).  Grabner grew up playing for the local team in Villach, EC VSV.  He moved to North America at the age of 17 and joined the Spokane Chiefs of the major junior Western Hockey League (WHL) to further his hockey career.  After his second season with the Chiefs, he was selected 14th overall by the Vancouver Canucks in the 2006 NHL Entry Draft.  Grabner played one more season in the WHL before moving to the American Hockey League (AHL), where he played two seasons in the Canucks' farm system.  He was traded during the 2010 NHL Entry Draft to the Florida Panthers, but was claimed by the New York Islanders after Florida placed him on waivers with the intention of assigning him to their AHL affiliate.  Grabner spent five seasons with the Islanders before being traded to the Maple Leafs in 2015.  Internationally Grabner has appeared for Austria in both junior and senior tournaments, and played in the 2014 Winter Olympics.

Vladislav Bulin: Vladislav Boulin (born May 18, 1972 in Penza, U.S.S.R.) is a defenceman currently playing for Neftekhimik Nizhnekamsk in the Kontinental Hockey League.  Boulin was drafted 103rd overall in the 5th round by the Philadelphia Flyers in the 1992 NHL Entry Draft.  Boulin began his career with HC Dynamo Moscow of the Russian Super League, where he played two seasons.  He then spent three seasons in the American Hockey League, two with the Hershey Bears, and one with the Philadelphia Phantoms.  He split the 1997-98 season with Star Bulls Rosenheim of the Deutsche Eishockey Liga and Michigan K-Wings of the International Hockey League.  He returned to the RSL for the 1998-99 season, playing for SKA Saint Petersburg, then went back to the DEL for 1999-2000.  He played with Augsburger Panther that season, and the Hannover Scorpions the next.  He finally returned once again to the RSL for 2001-02, playing two seasons for Lada Togliatti.  He spent the 2003-04 and 2004-05 seasons once again with HC Dynamo Moscow, and has been with Metallurg Magnitogorsk every season since.

Melville Vail: Melville Arthur "Sparky" Vail (July 5, 1906 in Meaford, Ontario - January 29, 1983) was a professional ice hockey player in the National Hockey League for the New York Rangers.  He played a total of 50 games over two seasons, 1928–29 and 1929–30, scoring four goals and five points.

Jason Garrison: Jason John Maxwell Garrison (born November 13, 1984) is a professional ice hockey player currently playing for the Vegas Golden Knights of the National Hockey League (NHL).  Garrison played two years of Junior A with the Nanaimo Clippers of the British Columbia Hockey League (BCHL), during which time he earned a scholarship to play college hockey with the University of Minnesota Duluth.  Following his third NCAA year, he signed with the Florida Panthers as an undrafted free agent in 2008.  Garrison spent four years with the Panthers organization, setting franchise records for single-season goals and power play goals by a defenceman in 2011–12.  In July 2012, he signed a six-year deal with his hometown team, the Vancouver Canucks.  After two seasons with Vancouver, he was traded to Tampa Bay, just prior to the 2014 NHL Entry Draft.

Question: What year was the National Hockey League team, in which Melville Vail played two seasons with, founded?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the ice hockey player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the NHL team the player played for."
    },
    "seasons_played_with_team": {
      "type": "integer",
      "description": "The number of seasons the player played with the specified team."
    },
    "team_founding_year": {
      "type": "integer",
      "description": "The year the NHL team was founded."
    }
  },
  "required": [
    "player_name",
    "team_name",
    "seasons_played_with_team",
    "team_founding_year"
  ],
  "additionalProperties": false
}
