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
1943 World Series: The 1943 World Series matched the defending champion St. Louis Cardinals against the New York Yankees, in a rematch of the 1942 Series.  The Yankees won the Series in five games for their tenth championship in 21 seasons.  It was Yankees manager Joe McCarthy's final Series win.  This series was also the first to have an accompanying World Series highlight film (initially, the films were created as gifts to troops fighting in World War II, to give them a brief recap of baseball action back home), a tradition that still persists.

Tarzan (2013 film): Tarzan (also known as Tarzan 3D) is a 2013 English-language German 3D computer-animated motion capture action-adventure film written, directed and produced by German producer Reinhard Klooss which was released on October 17, 2013 in Russia.  The film was released across early 2014 in other countries.  The film stars the voices of Kellan Lutz, Spencer Locke, Anton Zetterholm, Mark Deklin, Joe Cappelletti, and Jaime Ray Newman.  The screenplay was written by Reinhard Klooss, Jessica Postigo and Yoni Brenner.  The film is based on the classic book "Tarzan of the Apes" (1912) by Edgar Rice Burroughs, and is one of many adaptations.  The film received predominantly negative reviews from critics, who panned the film's storyline and animation and grossed $44 million worldwide.  "Tarzan" was released on DVD and Blu-ray on August 5, 2014 by Highlight Film.

David M. Israel: David Michael Israel is an Emmy and Golden Globe award winning television producer and writer as well as a former sportscaster for the New York Mets.  ("Before moving to Los Angeles from New York, Israel was a writer, producer and editor for Major League Baseball, working on such projects as This Week in Baseball, the 1986 New York Mets Highlight Film, and several World Series Highlight Films.") .  He has worked on "The Tracy Morgan Show", "3rd Rock from the Sun", "Grounded for Life" and the Nickelodeon sitcom "How to Rock".  He is currently a writer and co-executive producer on the NBC show About a Boy.

1985–86 Atlanta Hawks season: The Hawks entered the season with rookies Jon Koncak and Spud Webb.  The Hawks were transformed into one of the youngest teams in the NBA.  The Hawks were led by "the Human Highlight Reel" Dominique Wilkins.  He would have an outstanding year as he led the NBA in scoring with an average of 30.3 points per game.  One of the highlights of the season came when Webb (measuring five feet, seven inches) won the NBA Slam Dunk contest during All-Star Weekend.  In the second half of the season, the Hawks would be one of the strongest teams in the league.  The club won 35 of their final 52 games to finish the season with a record of 50 wins and 32 losses.  In the playoffs, the Hawks would eliminate the Detroit Pistons in 4 games.  In the 2nd round, the Hawks would be defeated by the Boston Celtics in 5 games.

Dominique Wilkins: Jacques Dominique Wilkins (born January 12, 1960) is an American retired professional basketball player who primarily played for the Atlanta Hawks of the National Basketball Association (NBA).  Wilkins was a nine-time NBA All-Star, and is widely viewed as one of the best dunkers in NBA history, earning the nickname The Human Highlight Film.  In 2006, Wilkins was inducted into the Naismith Memorial Basketball Hall of Fame.

1976 New York Jets season: The 1976 New York Jets season was the 17th season for the team and the seventh in the National Football League.  It began with the team trying to improve upon its 3–11 record from 1975 under new head coach Lou Holtz.  The Jets again finished with a record of 3–11, which combined with the departure of Holtz before the end of the season, prompted John Facenda to say about the Jets during the NFL Films highlight film for that season "Perhaps the best thing to say about the 1976 New York Jets season is that it's over".

Bill Kunkel (baseball): Kunkel was born in Hoboken, New Jersey.  His major league pitching career consisted of two seasons with the Kansas City Athletics (1961–1962) and one with the New York Yankees (1963).  He officiated in the World Series in 1974 and 1980, and in the American League Championship Series in 1971, 1975, 1978 and 1982.  He also worked the All-Star Game in 1972 and 1977, calling balls and strikes for the second contest (Kunkel's experience as the plate umpire is documented in the MLB official highlight film of the 1977 All-Star Game).  He was the first base umpire on September 28, 1974 when Nolan Ryan pitched the third of his record seven no-hitters, and was behind the plate exactly one year later on September 28, 1975 when four Oakland Athletics pitchers – Vida Blue, Glenn Abbott, Paul Lindblad and Rollie Fingers – combined to no-hit the California Angels, 5–0.

1990–91 Atlanta Hawks season: The 1990–91 NBA season was the Hawks' 42nd season in the National Basketball Association, and 23rd season in Atlanta.  Under new head coach Bob Weiss, the Hawks won their first three games.  However, after a 4–1 start, they lost nine consecutive games in November, but went on to win 20 of their next 25 games including a 7-game winning streak.  The Hawks finished fourth in the Central Division with a 43–39 record.  Dominique Wilkins made the All-NBA Second Team averaging 25.9 points per game while being selected for the 1991 NBA All-Star Game.  In the first round of the playoffs, the Hawks faced the defending champion Detroit Pistons.  The Hawks won Game 1 at The Palace of Auburn Hills 103–98, but would lose the next two games.  After winning Game 4 at The Omni, they lost the series in five games.

America's Team: The term "America's Team" is a nickname that refers to the National Football League (NFL)'s Dallas Cowboys.  The nickname originated with the team's 1978 highlight film, where the narrator (John Facenda) opens with the following introduction:

The Human Highlight Reel: The Human Highlight Reel is a compilation album by American rock band Man Overboard, released on Run for Cover Records on 10 May 2011.

Question: Who was the coach of The Human Highlight Film in 1990-91?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_nickname": {
      "type": "string",
      "description": "The nickname of the player."
    },
    "player_name": {
      "type": "string",
      "description": "The full name of the player associated with the nickname."
    },
    "season": {
      "type": "string",
      "description": "The specific season being referred to."
    },
    "team": {
      "type": "string",
      "description": "The team the player played for during that season."
    },
    "coach_name": {
      "type": "string",
      "description": "The name of the coach for the specified team and season."
    }
  },
  "required": [
    "player_nickname",
    "player_name",
    "season",
    "team",
    "coach_name"
  ],
  "additionalProperties": false
}
