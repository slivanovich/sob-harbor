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
2014 Cotton Bowl Classic: The 2014 Cotton Bowl Classic was a college football bowl game between the #9 Missouri Tigers of the Southeastern Conference and the #13 Oklahoma State Cowboys of the Big 12 Conference.  The 78th edition of the Cotton Bowl Classic took place on January 3, 2014 at 8:00 p.m. EST and aired on FOX.  It was one of the 2013–14 bowl games that concluded the 2013 FBS football season.  AT&T Stadium, formerly known as Cowboys Stadium and located in Arlington, Texas, hosted the game for the sixth straight year.  The game was sponsored by telecommunications company AT&T, and was officially known as the AT&T Cotton Bowl Classic.

2004 Cotton Bowl Classic: The 2004 Cotton Bowl Classic was a post-season college football bowl game between the Ole Miss Rebels and the Oklahoma State Cowboys on January 2, 2004, at the Cotton Bowl in Dallas, Texas.  It was the final game of the 2003 NCAA Division I-A football season for each team and resulted in a 31-28 Ole Miss victory.  Ole Miss represented the Southeastern Conference (SEC) while Oklahome State represented the Big 12 Conference.  It was Ole Miss's first January bowl victory since the 1970 Sugar Bowl and first Cotton Bowl Classic appearance since 1962.

1998 Cotton Bowl Classic: The 1998 Southwestern Bell Cotton Bowl Classic was a college football bowl game played on January 1, 1998, at the Cotton Bowl in Dallas, Texas.  The Cotton Bowl Classic was part of the 1997 NCAA Division I-A football season.  The bowl game featured the UCLA Bruins from the Pac-10 and the Texas A&M Aggies from the Big 12.  The game was televised on CBS.

2015 Cotton Bowl Classic (December): The 2015 Cotton Bowl Classic was a college football bowl game played on December 31, 2015 at AT&T Stadium in Arlington, Texas.  The 80th Cotton Bowl Classic was a College Football Playoff semifinal between Alabama and Michigan State with the winner to compete in the 2016 College Football Playoff National Championship.  It was one of the 2015–16 bowl games that concluded the 2015 FBS football season.

2007 Cotton Bowl Classic: The 2007 AT&T Cotton Bowl Classic was a college football bowl game played on January 1, 2007, at the Cotton Bowl in Dallas, Texas, USA.  The Cotton Bowl Classic was part of the 2007 NCAA Division I FBS football season and one of 32 games in the 2006–07 bowl season.  The bowl game featured the Nebraska Cornhuskers versus the Auburn Tigers.

1997 Cotton Bowl Classic: The 1997 Southwestern Bell Cotton Bowl Classic was a college football bowl game played on January 1, 1997, at the Cotton Bowl in Dallas, Texas, USA.  The Cotton Bowl Classic was part of the 1996 NCAA Division I-A football season.  The bowl game featured the Kansas State Wildcats from the Big 12 and the BYU Cougars from the Western Athletic Conference.  The game was televised on CBS.

2008 Cotton Bowl Classic: The 2008 AT&T Cotton Bowl Classic was a college football bowl game played on January 1, 2008, at the Cotton Bowl in Dallas, Texas, USA.  The Cotton Bowl Classic was part of the 2007 NCAA Division I FBS football season and one of 32 games in the 2007–2008 bowl season.  The bowl game featured the Arkansas Razorbacks from the SEC and the Missouri Tigers from the Big 12 and was televised in the United States on FOX.  Senior RB Tony Temple of Mizzou set a single game rushing record for the Cotton Bowl Classic with 281 yards and 4 touchdowns.  His 281 rushing yards put him in second place all time for total rushing yards in a bowl game.

AT&amp;T Stadium: AT&T Stadium, formerly Cowboys Stadium, is a retractable roof stadium in Arlington, Texas, United States.  It serves as the home of the Dallas Cowboys of the National Football League (NFL) and was completed on May 27, 2009.  It is also the home of the Cotton Bowl Classic.  The facility, owned by the city of Arlington, can also be used for a variety of other activities such as concerts, basketball games, college and high school football contests, soccer matches, and motocross and Spartan races.  It replaced the partially covered Texas Stadium, which served as the Cowboys' home from 1971 through the 2008 season.

1996 Cotton Bowl Classic: The 1996 Southwestern Bell Cotton Bowl Classic was a college football bowl game played on January 1, 1996, at the Cotton Bowl in Dallas, Texas.  This was the 60th held game.  The Cotton Bowl Classic was part of the 1995 NCAA Division I-A football season.  The bowl game featured the Colorado Buffaloes from the Big Eight and the Oregon Ducks from the Pacific-10 Conference.  The game was televised on CBS.

2015 Cotton Bowl Classic (January): The 2015 Cotton Bowl Classic was a college football bowl game played on January 1, 2015 at AT&T Stadium in Arlington, Texas.  The 79th Cotton Bowl Classic was one of the "New Year's Six" bowls of the College Football Playoff.  It was one of the 2014–15 bowl games that concluded the 2014 FBS football season.  The game kicked off at 12:30 PM EST and was broadcast on ESPN, ESPN Deportes, ESPN Radio and XM Satellite Radio.  It was sponsored by the Goodyear Tire and Rubber Company and was officially known as the Goodyear Cotton Bowl Classic.

Question: Where is the stadium where 2015 Cotton Bowl Classic is played on located 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the Cotton Bowl Classic event."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the game was played."
    },
    "stadium_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the stadium is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the stadium is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the stadium is located."
        }
      },
      "required": [
        "city",
        "state",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_name",
    "stadium_name",
    "stadium_location"
  ],
  "additionalProperties": false
}
