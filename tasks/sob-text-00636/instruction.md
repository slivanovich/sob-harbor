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
Charles Barkley: Charles Wade Barkley (born February 20, 1963) is an American retired professional basketball player who is currently the analyst on "Inside the NBA".  Nicknamed "Chuck", "Sir Charles", and "The Round Mound of Rebound", Barkley established himself as one of the National Basketball Association's dominant power forwards.  An All-American center at Auburn, he was drafted as a junior by the Philadelphia 76ers with the 5th pick of the 1984 NBA draft.  He was selected to the All-NBA First Team five times, the All-NBA Second Team five times, and once to the All-NBA Third Team.  He earned eleven NBA All-Star Game appearances and was named the All-Star MVP in 1991.  In 1993, he was voted the league's Most Valuable Player and during the NBA's 50th anniversary, named one of the 50 Greatest Players in NBA History.  He competed in the 1992 and 1996 Olympic Games and won two gold medals as a member of the United States' "Dream Team".  Barkley is a two-time inductee into the Naismith Memorial Basketball Hall of Fame, being inducted in 2006 for his individual career, and in 2010 as a member of the "Dream Team".

Bob Cousy Award: The Bob Cousy Award presented by The College of the Holy Cross (or Bob Cousy Collegiate Point Guard of the Year Award) is an annual basketball award given by the Naismith Memorial Basketball Hall of Fame to the top men's collegiate point guard.  It is named after six-time National Basketball Association (NBA) champion Bob Cousy, who played point guard for the Boston Celtics from 1950 to 1963.  Cousy won six championships with the Celtics.

Michael Stockton: Michael Stockton (born May 7, 1989) is an American professional basketball player for BG Göttingen of the Basketball Bundesliga (BBL).  He played college basketball for Westminster College and is the son of long time Utah Jazz point guard John Stockton.

Hust Stockton: John Houston "Hust" Stockton (September 23, 1901 – April 27, 1967) was a professional football player, a back in the late 1920s in the National Football League.  He played with the Frankford Yellow Jackets from 1925 until 1928, and was a member of Yellow Jackets' 1926 NFL Championship team.  During his final season in 1929, Stockton split time between the Boston Bulldogs and the Providence Steamroller.  He was the grandfather of basketball Hall of Fame inductee, John Stockton, who played point guard for the National Basketball Association's Utah Jazz from 1984 to 2003.

Clyde Drexler: Clyde Austin "The Glide" Drexler (born June 22, 1962) is an American retired professional basketball swingman.  During his career, he was a ten-time All-Star, and named one of the 50 Greatest Players in NBA History.  Drexler won an Olympic gold medal in 1992 as part of the 1992 United States men's Olympic basketball team ("The Dream Team") and an NBA Championship in 1995 with the Houston Rockets.  He is a two-time Naismith Memorial Basketball Hall of Fame inductee (being inducted 2004 for his individual career, and in 2010 as a member of the "Dream Team") He currently serves as a color commentator for Houston Rockets home games.

Bernard King: Bernard King (born December 4, 1956) is an American retired professional basketball player at the small forward position in the National Basketball Association (NBA).  He played 14 seasons with the New Jersey Nets, Utah Jazz, Golden State Warriors, New York Knicks and the Washington Bullets.  He was inducted into the Naismith Memorial Basketball Hall of Fame on September 8, 2013.  His younger brother, Albert, has also played in the NBA during his career.

Shandon Anderson: Shandon Rodriguez Anderson (born December 31, 1973) is an American retired professional basketball player who played in the National Basketball Association (NBA) from 1996 to 2006.  Growing up in Atlanta, Anderson attended the University of Georgia and played for four teams during his ten-year NBA career after being drafted by the Utah Jazz in 1996: the Jazz, Houston Rockets, New York Knicks, and Miami Heat.  He played the shooting guard and small forward positions.

Magic Johnson: Earvin "Magic" Johnson Jr. (born August 14, 1959) is an American retired professional basketball player and current president of basketball operations of the Los Angeles Lakers of the National Basketball Association (NBA).  He played point guard for the Lakers for 13 seasons.  After winning championships in high school and college, Johnson was selected first overall in the 1979 NBA draft by the Lakers.  He won a championship and an NBA Finals Most Valuable Player Award in his rookie season, and won four more championships with the Lakers during the 1980s.  Johnson retired abruptly in 1991 after announcing that he had contracted HIV, but returned to play in the 1992 All-Star Game, winning the All-Star MVP Award.  After protests from his fellow players, he retired again for four years, but returned in 1996, at age 36, to play 32 games for the Lakers before retiring for the third and final time.

Karl Malone: Karl Anthony Malone (born July 24, 1963) is an American retired professional basketball player.  Nicknamed "The Mailman", Malone played the power forward position and spent his first 18 seasons (1985–2003) in the National Basketball Association (NBA) with the Utah Jazz and formed a formidable duo with his teammate John Stockton.  Malone also played one season for the Los Angeles Lakers.  Malone was a two-time NBA Most Valuable Player, a 14-time NBA All-Star, and an 11-time member of the All-NBA first team.  He scored the second most career points in NBA history (36,928) (second behind Kareem Abdul-Jabbar), and holds the records for most free throws attempted and made, in addition to co-holding the record for the most first team All-NBA elections in history (tied with Kobe Bryant and LeBron James).  He is considered one of the best power forwards in NBA history.

John Stockton: John Houston Stockton (born March 26, 1962) is an American retired professional basketball player.  He spent his entire professional playing career as a point guard for the Utah Jazz of the National Basketball Association (NBA), from 1984 to 2003.  Stockton is regarded as one of the best point guards of all time, holding the NBA records for most career assists and steals by considerable margins.  He is a ten-time NBA All-Star, and a two-time Naismith Memorial Basketball Hall of Fame inductee (in 2009 for his individual career, and in 2010 as a member of the 1992 United States men's Olympic basketball team ("Dream Team").  Stockton was previously an assistant coach for the Montana State University women's basketball team.

Question: John Houston "Hust" Stockton, was a professional football player, a back in the late 1920s in the National Football League, and was the grandfather of which basketball Hall of Fame inductee, an American retired professional basketball player, who played point guard for the NBA's Utah Jazz from 1984 to 2003?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "basketball_player": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "position": {
          "type": "string"
        },
        "nba_team": {
          "type": "string"
        },
        "nba_career_start_year": {
          "type": "integer"
        },
        "nba_career_end_year": {
          "type": "integer"
        },
        "is_hall_of_fame_inductee": {
          "type": "boolean"
        },
        "hall_of_fame_induction_years": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        }
      },
      "required": [
        "name",
        "position",
        "nba_team",
        "nba_career_start_year",
        "nba_career_end_year",
        "is_hall_of_fame_inductee",
        "hall_of_fame_induction_years"
      ],
      "additionalProperties": false
    },
    "relationship_type": {
      "type": "string",
      "description": "The relationship of the basketball player to Hust Stockton"
    },
    "related_person_name": {
      "type": "string",
      "description": "The full name of the related person (Hust Stockton)"
    }
  },
  "required": [
    "basketball_player",
    "relationship_type",
    "related_person_name"
  ],
  "additionalProperties": false
}
