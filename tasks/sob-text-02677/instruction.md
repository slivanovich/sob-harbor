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
Zacarías Ferreíra: Zacarías Ferreira is a Bachata artist from the Dominican Republic.  He was born in the 1970s in the Dominican Republic.  He is the uncle of professional basketball player Karl-Anthony Towns, who currently plays on the Minnesota Timberwolves, of the NBA.

Ralph Sampson: Ralph Lee Sampson Jr. (born July 7, 1960) is an American retired basketball player.  A 7-foot-4 phenom, three-time College Player of the Year, and first selection in the 1983 NBA draft, Sampson brought heavy expectations with him to the National Basketball Association (NBA).  The NBA Rookie of the Year, Sampson averaged 20.7 points and 10.9 rebounds for his first three seasons with the Houston Rockets before injuries began to take their toll.  Three knee surgeries later he retired as a four-time All-Star, an NBA Rookie of the Year, and an NBA All-Star Game MVP ().  One of his many career highlights was a buzzer-beating shot to dethrone the Los Angeles Lakers as Western Conference champions in 1986, derailing their hopes for coveted back-to-back NBA titles, and sending the Rockets to their second NBA Finals in the team's history.

Alvan Adams: Alvan Leigh Adams (born July 19, 1954) is an American retired professional basketball player.  After starring at the University of Oklahoma, the 6'9" (2.06 m) power forward/center was selected by the Phoenix Suns with the 4th pick of the 1975 NBA draft.  Adams was a rookie on a Suns team whose season included an improbable playoff run that took them all the way to the 1976 NBA Finals.  In the same year, he was selected to play in the All-Star Game and won the NBA Rookie of the Year Award as well as being named to the All-NBA Rookie Team.  Adams spent his entire career with the Suns and retired in 1988 as the second all-time Suns scorer with 13,910 career points.

Karl-Anthony Towns: Karl-Anthony Towns Jr. (born November 15, 1995) is a Dominican-American professional basketball player for the Minnesota Timberwolves of the National Basketball Association (NBA).  He played college basketball for the University of Kentucky.  Towns was named to the Dominican Republic national basketball team Olympic squad as a 16-year-old, although the Dominican Republic ultimately did not qualify for the 2012 Olympics.  He was selected with the first overall pick in the 2015 NBA draft by the Minnesota Timberwolves, and went on to be named NBA Rookie of the Year for the 2015–16 season.

Jerry Lucas: Jerry Ray Lucas (born March 30, 1940) is an American former basketball player and memory education expert.  He was a nationally-awarded high school player, national college star at Ohio State, and 1960 gold medal Olympian and international player before starring as a professional player in the National Basketball Association (NBA).  As a collegian, Lucas led the Ohio State Buckeyes to the 1960 college national championship and three straight NCAA finals.  He remains today the only three-time Big Ten Player of the Year, and was also twice named NCAA Player of the Year.  As a professional, Lucas was named All-NBA First Team three times, a NBA All-Star seven times, was 1964 NBA Rookie of the Year, and was named Most Valuable Player of the 1965 NBA All-Star Game among other honors and awards.  He was inducted to the Naismith Memorial Basketball Hall of Fame in 1980.

Kevin Calabro: Kevin Paul Calabro (born June 27, 1956) is an American sportscaster based in Seattle, Washington.  The longtime voice of the former Seattle SuperSonics NBA franchise, Calabro has primarily called NBA basketball but has also announced collegiate football (alongside Yogi Roth) and basketball as well as MLS soccer.  Starting with the 2016–2017 NBA season, he is the television play-by-play voice for the Portland Trail Blazers.  As of the 2015–16 season, Calabro is the lead play-by-play announcer for NBA on ESPN Radio, including NBA Finals games in 2007, 2014 and 2016 alongside personalities like Jack Ramsay and Hubie Brown.  Calabro has done ESPN radio play-by-play for the NBA Conference Finals for a decade in addition to being a regular contributor to TNT's NBA broadcasts.  Calabro worked college basketball and football games for the Pac-12 Network and postseason college basketball for Westwood One Sports, including NCAA tournament action.

Malcolm Brogdon: Malcolm Moses Adams Brogdon (born December 11, 1992) is an American professional basketball player for the Milwaukee Bucks of the National Basketball Association (NBA).  He played college basketball for the Virginia Cavaliers under Tony Bennett.  As a senior in 2015–16, he was named the ACC Player of the Year and ACC Defensive Player of the Year, becoming the first player in conference history to earn both honors in the same season.  He was selected in the second round of the 2016 NBA draft by the Bucks with the 36th overall pick.  He went on to win the NBA Rookie of the Year Award, becoming the first second-round pick in the NBA draft lottery era to do so.

2000–01 Philadelphia 76ers season: The 2000–01 NBA season was the 76ers 52nd season in the National Basketball Association, and 38th season in Philadelphia.  Allen Iverson had his best season in 2001—he led his team to win their first ten games, he started and won All-Star MVP honors at the All Star Game.  The Sixers also posted a 56–26 record, which was best in the Eastern Conference that season.  It was the 76ers' best regular season record since 1984–85.  Iverson averaged a then-career high 31.1 points, winning his second NBA scoring title in the process.  He also won the NBA steals title at 2.5 per game.  Iverson was named NBA Most Valuable Player for his accomplishments, beating Tim Duncan and Shaquille O'Neal by a wide margin.  In addition, coach Larry Brown was named NBA Coach of the Year, Dikembe Mutombo (who was acquired from the Atlanta Hawks) won his fourth NBA Defensive Player of the Year Award, and Aaron McKie won the NBA Sixth Man of the Year Award.

Michael Carter-Williams: Michael Carter-Williams (born October 10, 1991) is an American professional basketball player for the Charlotte Hornets of the National Basketball Association (NBA).  He was drafted 11th overall in the 2013 NBA draft by the Philadelphia 76ers, after playing college basketball for the Syracuse Orange.  He was named NBA Rookie of the Year in 2014, and has also played for the Milwaukee Bucks and Chicago Bulls.

Kyrie Irving: Kyrie Andrew Irving ( , born March 23, 1992) is an American professional basketball player for the Boston Celtics of the National Basketball Association (NBA).  He was named NBA Rookie of the Year after being selected by the Cleveland Cavaliers with the first overall pick in the 2011 NBA draft.  A four-time NBA All-Star, Irving was selected to the All-NBA Third Team in 2015.  He won an NBA Championship with the Cavaliers in 2016.

Question: What NBA basketball player was named NBA Rookie of the Year for the 2015–16 season and has an uncle who is a Bachata artist?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the NBA player."
    },
    "player_team": {
      "type": "string",
      "description": "The NBA team the player plays for."
    },
    "rookie_of_the_year_season": {
      "type": "string",
      "description": "The NBA season in which the player won the Rookie of the Year award."
    },
    "player_draft_details": {
      "type": "object",
      "properties": {
        "draft_year": {
          "type": "integer",
          "description": "The year the player was drafted."
        },
        "draft_pick_overall": {
          "type": "integer",
          "description": "The overall pick number in the draft."
        }
      },
      "required": [
        "draft_year",
        "draft_pick_overall"
      ],
      "additionalProperties": false
    },
    "uncle_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the player's uncle."
        },
        "profession": {
          "type": "string",
          "description": "The profession of the player's uncle."
        },
        "origin": {
          "type": "string",
          "description": "The country of origin of the player's uncle."
        }
      },
      "required": [
        "name",
        "profession",
        "origin"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_team",
    "rookie_of_the_year_season",
    "player_draft_details",
    "uncle_details"
  ],
  "additionalProperties": false
}
