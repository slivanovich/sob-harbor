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
Jim Barr: James Leland Barr (born February 10, 1948) is a former right-handed pitcher in Major League Baseball who played for the San Francisco Giants (1971–1978, 1982–1983) and California Angels (1979–1980).  He is perhaps best known for setting a record for consecutive batters retired (41, later tied by Bobby Jenks in 2007, and then broken by Mark Buehrle on July 28, 2009 and again by Yusmeiro Petit on August 28, 2014).  Barr remains the only pitcher to retire as many as 41 consecutive batters in the course of only two games; his streak began in the third inning of a complete-game win and extended through the seventh inning of another complete-game win (Beurhle's streak included his perfect game and the starts before and after, while the streaks of Jenks and Petit included a number of relief appearances).

List of Detroit Tigers no-hitters: The Detroit Tigers are a Major League Baseball franchise based in Detroit, Michigan.  They play in the American League Central division.  Pitchers for the Tigers have thrown seven no-hitters in franchise history.  A no-hitter is officially recognized by Major League Baseball only "when a pitcher (or pitchers) allows no hits during the entire course of a game, which consists of at least nine innings.  In a no-hit game, a batter may reach base via a walk, an error, a hit by pitch, a passed ball or wild pitch on strike three, or catcher's interference."  No-hitters of less than nine complete innings were previously recognized by the league as official; however, several rule alterations in 1991 changed the rule to its current form.  A no-hitter is common enough that only one team in Major League Baseball has never had a pitcher accomplish the feat.  A perfect game, a special subcategory of no-hitter, has yet to be thrown in Tigers history.  As defined by Major League Baseball, "in a perfect game, no batter reaches any base during the course of the game."  This feat came closest on June 2, 2010 when Armando Galarraga lost his perfect game bid against the Cleveland Indians with two outs in the ninth due to the incorrect call made by a first base umpire Jim Joyce.  But there are two other times when the Tigers perfect game bids were lost with two outs in the ninth, one in 1932 and the other in 1983.  The Tigers lead all franchises with three perfect game bids lost with two outs in the ninth.

List of San Francisco Giants no-hitters: The San Francisco Giants are a Major League Baseball franchise based in San Francisco, California.  They play in the National League West division.  Also known in their early years as the "New York Gothams" (1883–84) and "New York Giants" (1885–1957), pitchers for the Giants have thrown 17 no-hitters in franchise history.  A no-hitter is officially recognized by Major League Baseball only "when a pitcher (or pitchers) retires each batter on the opposing team during the entire course of a game, which consists of at least nine innings".  No-hitters of less than nine complete innings were previously recognized by the league as official; however, several rule alterations in 1991 changed the rule to its current form.  A no-hitter is rare enough that one team in Major League Baseball has still never had a pitcher accomplish the feat, and teams may go decades without recording one.  A perfect game, a special subcategory of no-hitter, was finally thrown by Matt Cain on June 13, 2012.  As defined by Major League Baseball, "in a perfect game, no batter reaches any base during the course of the game."  Previously, this feat came closest on July 4, 1908 when Hooks Wiltse was hit by a pitch with two outs in the ninth and a scoreless tie.  The plate umpire, Cy Rigler, claimed he should have called the previous pitch strike three, that would have ended the inning with a perfection.  Wiltse would go on to retire all three in the tenth to end the game after the Giants scored a run in the top of the tenth.

List of Major League Baseball perfect games: Over the 140 years of Major League Baseball history, and over 210,000 games played, there have been 23 official perfect games by the current definition.  No pitcher has ever thrown more than one.  The perfect game thrown by Don Larsen in game 5 of the 1956 World Series is the only postseason perfect game in major league history and one of only two postseason no-hitters, the other being a no-hitter thrown by Roy Halladay in game 1 of the 2010 National League Division Series against the Cincinnati Reds.  The first two major league perfect games, and the only two of the premodern era, were thrown in 1880, five days apart.  The most recent perfect game was thrown on August 15, 2012 by Félix Hernández of the Seattle Mariners.  There were three perfect games in 2012, with no other year ever having more than two thrown.  By contrast, there have been spans of 23 and 33 consecutive seasons in which not a single perfect game was thrown.

Dennis Martínez's perfect game: On July 28, 1991, Dennis Martínez of the Montreal Expos pitched the 13th perfect game in Major League Baseball history, blanking the Los Angeles Dodgers 2-0 at Dodger Stadium.  A native of Granada, Nicaragua, Martínez became the first pitcher born outside of the United States to pitch a perfect game.  (He has since been joined by Venezuela native Félix Hernández, who pitched a perfect game in 2012.)  The perfect game also made the Dodgers, the losing team in Tom Browning's perfect game in 1988, the first team to be on the losing end of consecutive perfect games; they have since been joined by the Tampa Bay Rays, who were the losing team in Mark Buehrle's perfect game in 2009 and Dallas Braden's perfect game the following year.  After completing the perfect game, Martínez slowly walked into the Dodger stadium dugout, sat down by himself and cried.

List of Milwaukee Brewers no-hitters: The Milwaukee Brewers (formerly known as the "Seattle Pilots" in 1969) are a Major League Baseball franchise based in Milwaukee, Wisconsin.  Formed in 1969, they play in the National League Central division (formerly in the American League Central Division until 1997).  Juan Nieves threw the only no-hitter in franchise history on April 15, 1987.  A no-hitter is officially recognized by Major League Baseball only "when a pitcher (or pitchers) retires each batter on the opposing team during the entire course of a game, which consists of at least nine innings".  No-hitters of less than nine complete innings were previously recognized by the league as official; however, several rule alterations in 1991 changed the rule to its current form.  A no-hitter is rare enough that a Major League Baseball team, the San Diego Padres, has never had a pitcher accomplish the feat.  A perfect game, a special subcategory of no-hitter, has yet to be thrown in Brewers history.  As defined by Major League Baseball, "in a perfect game, no batter reaches any base during the course of the game."

List of Chicago White Sox no-hitters: The Chicago White Sox are a Major League Baseball franchise based in Chicago.  They play in the American League Central division.  Pitchers for the White Sox have thrown eighteen no-hitters in franchise history.  A no-hitter is officially recognized by Major League Baseball only “when a pitcher (or pitchers) allows no hits during the entire course of a game, which consists of at least nine innings.  In a no-hit game, a batter may reach base via a walk, an error, a hit by pitch, a passed ball or wild pitch on strike three, or catcher’s interference.”  No-hitters of less than nine complete innings were previously recognized by the league as official; however, several rule alterations in 1991 changed the rule to its current form.  A no-hitter is rare enough that one team in Major League Baseball has never had a pitcher accomplish the feat.  Three perfect games, a special subcategory of no-hitter, have been pitched in White Sox history, which equals the New York Yankees for the most perfect games pitched by any MLB franchise.  As defined by Major League Baseball, “in a perfect game, no batter reaches any base during the course of the game.”  These feats were achieved by Charlie Robertson in 1922, which was the first perfect game on the road in MLB history, Mark Buehrle in 2009, and Philip Humber in 2012.

DeWayne Wise: Larry DeWayne Wise (born February 24, 1978) is an American retired professional baseball outfielder.  He graduated from Chapin High School in 1997 and was selected by the Cincinnati Reds in the fifth round of the 1997 amateur draft.  He played in Major League Baseball (MLB) for the Toronto Blue Jays, Atlanta Braves, Cincinnati Reds, Chicago White Sox, Florida Marlins, and New York Yankees.  He is best known for robbing Gabe Kapler of a home run to preserve Mark Buehrle's perfect game in 2009.

Gabe Kapler: Gabriel Stefan "Gabe" Kapler (born July 31, 1975) is a former Major League Baseball outfielder.

List of Oakland Athletics no-hitters: The Oakland Athletics are a Major League Baseball franchise based in Oakland, California.  They play in the American League West division.  Also known in their early years as the “Philadelphia Athletics” (1901–54) and “Kansas City Athletics” (1954–67), pitchers for the Athletics have thrown eleven no-hitters in franchise history, five during the Philadelphia years and six after the move to Oakland but none during the Kansas City era.  A no-hitter is officially recognized by Major League Baseball only “when a pitcher (or pitchers) retires each batter on the opposing team during the entire course of a game, which consists of at least nine innings.”  No-hitters of less than nine complete innings were previously recognized by the league as official; however, several rule alterations in 1991 changed the rule to its current form.  A no-hitter is rare enough that one team in Major League Baseball has never had a pitcher accomplish the feat.  Two perfect games, a special subcategory of no-hitter, have been pitched in Athletics history.  As defined by Major League Baseball, “in a perfect game, no batter reaches any base during the course of the game.”  These feats were achieved by Catfish Hunter in 1968, which was the first perfect game in American League history since 1922, and Dallas Braden in 2010, which was the second perfect game in the majors – both against the same team – in ten months.

Question: When was the  former Major League Baseball outfielder which DeWayne Wise robbed of a home run to preserve Mark Buehrle's perfect game in 2009 born? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the former Major League Baseball outfielder."
    },
    "person_role": {
      "type": "string",
      "description": "The role of the person in Major League Baseball."
    },
    "event_context": {
      "type": "object",
      "properties": {
        "event_description": {
          "type": "string",
          "description": "Description of the event related to the person."
        },
        "pitcher_name": {
          "type": "string",
          "description": "The name of the pitcher who threw the perfect game."
        },
        "year_of_event": {
          "type": "integer",
          "description": "The year the perfect game occurred."
        }
      },
      "required": [
        "event_description",
        "pitcher_name",
        "year_of_event"
      ],
      "additionalProperties": false
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the person."
    }
  },
  "required": [
    "person_name",
    "person_role",
    "event_context",
    "birth_date"
  ],
  "additionalProperties": false
}
