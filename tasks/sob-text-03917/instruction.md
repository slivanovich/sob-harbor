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
1972 NBA draft: The 1972 NBA draft was the 26th annual draft of the National Basketball Association (NBA).  The draft was held on April 10 and 15, 1972 before the 1972–73 season.  In this draft, 17 NBA teams took turns selecting amateur U.S. college basketball players and other eligible players, including international players.  The first two picks in the draft belonged to the teams that finished last in each conference, with the order determined by a coin flip.  The Portland Trail Blazers won the coin flip and were awarded the first overall pick, while the Buffalo Braves were awarded the second pick.  The remaining first-round picks and the subsequent rounds were assigned to teams in reverse order of their win–loss record in the previous season.  As a result of last year's supplemental hardship draft, the Cincinnati Royals, the Atlanta Hawks, the Golden State Warriors and the Baltimore Bullets forfeited their first round picks, while the Los Angeles Lakers forfeited their fourth round pick.  Prior to the start of the season, the Cincinnati Royals relocated and became the Kansas City-Omaha Kings.  The draft consisted of 18 rounds comprising the selection of 198 players.

Zaid Abdul-Aziz: Zaid Abdul-Aziz (born Donald A. Smith on April 7, 1946) is a retired American professional basketball player.  Donald Smith changed his name to Zaid Abdul-Aziz in 1976 after he converted to Islam.  The 6'9" Abdul-Aziz starred at Iowa State University before being drafted by the NBA's Cincinnati Royals in 1968.  He played ten seasons in the league as a member of the Royals, Milwaukee Bucks, Seattle SuperSonics, Houston Rockets, Buffalo Braves, and Boston Celtics.  Nicknamed "The Kangaroo", he had his finest season in 1971–1972, when he averaged 13.8 points and 11.3 rebounds for Seattle.  He retired in 1978 with career totals of 4,557 points and 4,065 rebounds.

Wayne Embry: Wayne Richard Embry (born March 26, 1937) is a retired American basketball player & basketball executive.  Embry's 11-year playing career as a center/forward spanned from 1958 to 1969 playing for the Cincinnati Royals, Boston Celtics and Milwaukee Bucks, all of the NBA.  After his playing career, Embry transitioned to a career as a professional basketball executive, becoming the first African-American general manager & team president in NBA history.

Bill Dinwiddie: Bill Dinwiddie (born July 15, 1943) is a retired American basketball player who played in the National Basketball Association.  Dinwiddie signed as a free agent with the Cincinnati Royals in 1966 and began playing with the team in 1967.  In 1969, he was traded to the Boston Celtics for Bob Cousy.  He was later traded to the Milwaukee Bucks for a sixth-round draft pick.

Wilma Rudolph: Wilma Glodean Rudolph (June 23, 1940 – November 12, 1994) was an American sprinter from Clarksville, Tennessee, who became a world-record-holding Olympic champion and international sports icon in track and field following her successes in the 1956 and 1960 Olympic Games.  Rudolph competed in the 200-meter dash and won a bronze medal in the 4 × 100-meter relay at the 1956 Summer Olympics at Melbourne, Australia.  She also won three gold medals in the 100- and 200-meter individual events and the 4 x 100-meter relay at the 1960 Summer Olympics in Rome, Italy.  Rudolph was acclaimed the fastest woman in the world in the 1960s and became the first American woman to win three gold medals in a single Olympic Games.  Due to the worldwide television coverage of the 1960 Summer Olympics, Rudolph became an international star along with other Olympic athletes such as Cassius Clay (later known as Muhammad Ali), Oscar Robertson, and Rafer Johnson who competed in Italy.

Rich Niemann: Richard W. "Rich" Niemann (born July 2, 1946) is a former American basketball player who played at center in the National Basketball Association and American Basketball Association.  Niemann was originally drafted in the fourth round of the 1968 NBA draft by the Detroit Pistons.  That season, he was traded from the Pistons to the Milwaukee Bucks along with cash for Dave Gambee.  Later that year, he was claimed by the Boston Celtics after he was waived by the Bucks.  After his time with the Celtics, he played the rest of his career in the American Basketball Association.  He now helps coach and instruct the girls varsity team for Kennedy Catholic High School.

Collis Jones: J. Collis Jones (born July 3, 1949) is a former college and professional basketball player.  Born in Washington, D.C., he attended the University of Notre Dame.  He currently ranks 17th on the Notre Dame all-time scoring list with 1,367 points.  Throughout his career, he has averaged 16.1 points per game, which ranks 19th in school history.  He also stands at eighth place in Fighting Irish history in rebounds (884), ninth in rebounding average (10.4 rpg), 13th in field goals attempted (1,242), 15th in field goals made (567), and 22nd in free throws attempted (360).  He led the 1969–70 and 1970–71 squads in rebounding with averages of 12.4 and 13.1 rpg, respectively.  He was selected in the first round of the 1971 NBA draft by the Milwaukee Bucks and also in the 1971 American Basketball Association player draft by the Dallas Chaparrals.  He played exclusively in the American Basketball Association, including for the Kentucky Colonels, Memphis Sounds and Baltimore Claws.

Bob Boozer: Robert Louis Boozer (April 26, 1937 – May 19, 2012) was an American professional basketball player in the National Basketball Association (NBA).  He won a gold medal in the 1960 Summer Olympics and won an NBA Championship as a member of the Milwaukee Bucks in 1971.

George Patterson (basketball): George Patterson (November 26, 1939 – December 22, 2003) was an American basketball player who played in the National Basketball Association.  Patterson was originally drafted in the twelfth round of the 1961 NBA draft by the Cincinnati Royals.  He would finally play in the NBA with the Detroit Pistons from 1967 to 1968.  Later, he was selected by the Milwaukee Bucks in the 1968 NBA Expansion Draft.

Oscar Robertson: Oscar Palmer Robertson (born November 24, 1938), nicknamed "The Big O", is an American former National Basketball Association player who played for the Cincinnati Royals and Milwaukee Bucks.  The 6 ft , 205 lb Robertson played point guard and was a 12-time All-Star, 11-time member of the All-NBA Team, and one-time winner of the MVP award in 14 professional seasons.  In 1962, he became the first of only two players in NBA history to average a triple-double for a season.  In the 1970–71 NBA season, he was a key player on the team that brought the Bucks their only NBA title.  His playing career, especially during high school and college, was plagued by racism.

Question: During the 1960 Summer Olympics, Wilma Rudolph became a world renowned star along with which former National Basketball Association player who played for the Cincinnati Royals and Milwaukee Bucks? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "olympic_games": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year the Olympic Games took place."
        },
        "name": {
          "type": "string",
          "description": "The full name of the Olympic Games event."
        }
      },
      "required": [
        "year",
        "name"
      ],
      "additionalProperties": false
    },
    "primary_athlete_of_question": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the athlete mentioned in the question."
        },
        "status_achieved": {
          "type": "string",
          "description": "The status or recognition achieved by the athlete during the event."
        }
      },
      "required": [
        "name",
        "status_achieved"
      ],
      "additionalProperties": false
    },
    "associated_nba_player": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the NBA player associated with the primary athlete."
        },
        "nba_teams_played_for": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of NBA teams the player played for, relevant to the question."
        },
        "became_star_at_event": {
          "type": "string",
          "description": "The event at which the NBA player became a star, alongside the primary athlete."
        }
      },
      "required": [
        "name",
        "nba_teams_played_for",
        "became_star_at_event"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "olympic_games",
    "primary_athlete_of_question",
    "associated_nba_player"
  ],
  "additionalProperties": false
}
