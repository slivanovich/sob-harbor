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
List of Miami Marlins seasons: The Miami Marlins (originally the Florida Marlins from 1993 until 2011) are a professional baseball team that has been based in Miami Gardens, Florida since becoming an expansion team in .  The Marlins are a member of both the Major League Baseball's (MLB) National League Eastern Division and the National League (NL) itself.  For the first 19 seasons, the Marlins played their home games at Sun Life Stadium.  Beginning with the season, the Marlins play home games at Marlins Park in Little Havana.

Billy the Marlin: Billy the Marlin is the official mascot of the Miami Marlins baseball franchise.  At 8 feet tall and 250 pounds, he is ""a natural-born clown and good-natured prankster"".  He appears at every Marlins home game at Marlins Park, and performs his own routine in the middle of the 5th inning.

2013 Miami Marlins season: The Miami Marlins’ 2013 season was the 21st season for the Major League Baseball franchise, and the second as the “Miami” Marlins.  The Marlins finished the season with a 62-100 record, easily their worst as an MLB franchise.

2012 Miami Marlins season: The 2012 Miami Marlins season was the 20th season for the Major League Baseball franchise.  The Marlins moved into Marlins Park for the 2012 season; as part of the agreement, they changed their name from the "Florida Marlins" to the "Miami Marlins".

Miami Marlins: The Miami Marlins are an American professional baseball team based in Miami, Florida.  The Marlins compete in Major League Baseball (MLB) as a member club of the National League (NL) East division.  Their home park is Marlins Park.  Though one of only two MLB franchises to have never won a division title (the other is the Colorado Rockies), the Marlins have won two World Series championships as a wild card team.

2017 Miami Marlins season: The Miami Marlins' 2017 season was the 25th season for the Major League Baseball (MLB) franchise, and the sixth as the "Miami" Marlins.  The club hosted the 2017 MLB All-Star Game, the first at Marlins Park.

2017 Major League Baseball All-Star Game: The 2017 Major League Baseball All-Star Game was the 88th edition of the Major League Baseball All Star Game.  The game was hosted by the Miami Marlins and was played at Marlins Park on July 11, 2017.  It was televised nationally by Fox.  The game was the first since 2002 whose outcome did not determine home-field advantage for the World Series; instead, the team with the better regular-season record will have home-field advantage.  The Marlins were announced as the hosts on February 10, 2015, by Major League Baseball Commissioner Rob Manfred; the game was the Marlins' first time hosting, leaving the Tampa Bay Rays as the only MLB franchise not to have hosted an All-Star game.

List of Miami Marlins first-round draft picks: The Miami Marlins are a Major League Baseball (MLB) franchise based in Miami, Florida.  They play in the National League East division.  Since the franchise was established in 1993 as the Florida Marlins, the Marlins have selected 32 players in the first round.  Officially known as the "First-Year Player Draft", the Rule 4 Draft is MLB's primary mechanism for assigning players from high schools, colleges, and other amateur clubs to its franchises.  The draft order is determined based on the previous season's standings, with the team possessing the worst record receiving the first pick.  In addition, teams which lost free agents in the previous off-season may be awarded compensatory or supplementary picks.  The First-Year Player Draft is unrelated to the 1992 expansion draft in which the Marlins filled their roster.

List of Miami Marlins no-hitters: The Miami Marlins are a Major League Baseball franchise based in Miami, Florida.  Formed in 1993, they play in the National League East division.  Pitchers for the Marlins have thrown six no-hitters in franchise history.  A no-hitter is officially recognized by Major League Baseball only “when a pitcher (or pitchers) retires each batter on the opposing team during the entire course of a game, which consists of at least nine innings”.  No-hitters of less than nine complete innings were previously recognized by the league as official; however, several rule alterations in 1991 changed the rule to its current form.  A no-hitter is rare enough that one team in Major League Baseball has never had a pitcher accomplish the feat.  No perfect games, a special subcategory of no-hitter, have been thrown in Marlins history.  As defined by Major League Baseball, “in a perfect game, no batter reaches any base during the course of the game.”

Marlins Park: The stadium is designed in a neomodern form of baseball architecture.  Marlins Park was also LEED certified as the greenest MLB park in 2012.  The building is the sixth MLB stadium to have a retractable roof.  With a seating capacity of 37,442, it is the third-smallest stadium in Major League Baseball by official capacity, and the smallest by actual capacity.

Question: Billy the Marlin is the official mascot of the Miami Marlins baseball franchise, and appears at every Marlins home game at which stadium designed in a neomodern form of baseball architecture, and also was LEED certified as the greenest MLB park in 2012?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mascot_name": {
      "type": "string",
      "description": "The name of the official mascot."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the baseball franchise the mascot represents."
    },
    "stadium_info": {
      "type": "object",
      "properties": {
        "stadium_name": {
          "type": "string",
          "description": "The name of the stadium where the mascot appears."
        },
        "design_style": {
          "type": "string",
          "description": "The architectural design style of the stadium."
        },
        "leed_certification_year": {
          "type": "integer",
          "description": "The year the stadium received LEED certification."
        },
        "leed_certification_description": {
          "type": "string",
          "description": "Description of the LEED certification received by the stadium."
        }
      },
      "required": [
        "stadium_name",
        "design_style",
        "leed_certification_year",
        "leed_certification_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "mascot_name",
    "team_name",
    "stadium_info"
  ],
  "additionalProperties": false
}
