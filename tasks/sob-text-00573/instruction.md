{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSmokey the Cannon: Smokey the Cannon is a famous replica Civil War artillery cannon that has served as part of the pageantry of college football games at the University of Texas at Austin since 1954.  Smokey the Cannon is owned and operated by the Texas Cowboys (an honorary men's service organization at Texas) and is stationed in the left corner of the south endzone at Darrell K Royal–Texas Memorial Stadium during every Texas Longhorns home football game.  After each football season, Smokey the Cannon is generally displayed in the Red McCombs Endzone atrium for the spring semester.  In addition to all home football games, Smokey the Cannon is present at the annual Texas vs. Oklahoma Red River Rivalry game in Dallas, Texas every October, as well as at other select football games outside of Austin, Texas (barring local and stadium permission).  Recently, Smokey the Cannon was present at the 2011 Holiday Bowl, in which the Texas Longhorns beat the Cal Golden Bears 21-10 on December 29, 2011; former Texas Cowboy Oldman, Blaine Irby caught 1 pass for 30 yards in the win.\n\nThe Pride of the South: The Pride of the South is the name of the marching band at The University of Mississippi in Oxford, Mississippi.  The full band plays at all Ole Miss home football games, and a smaller pep band is sent to most away games.  The full band also travels to Ole Miss bowl games and Starkville, Mississippi when Mississippi State University hosts the Egg Bowl. The University of Mississippi Band has been giving outstanding performances in concert and in support of Ole Miss athletic events since it was organized in 1928.  In addition to performing at all home football games and many away games, the marching band has attended numerous bowl games including the Sugar Bowl, the Gator Bowl, the Liberty Bowl, the Independence Bowl, the Peach Bowl, the Cotton Bowl, and more recently the Motor City Bowl in 1997, the Music City Bowl in 2000, the Independence Bowl in 1998, 1999 and 2002, the Cotton Bowl in 2004, 2009 and 2010, the Chick-fil-a Classic in 2014, the Peach Bowl in 2014, and the Sugar Bowl in 2016.\n\nMississippi Veterans Memorial Stadium: Mississippi Veterans Memorial Stadium is an outdoor football stadium in Jackson, Mississippi, United States.  Veterans Memorial Stadium is the home field of the Jackson State Tigers football team.  The stadium was originally known as War Veterans Memorial Stadium then later as Hinds County War Memorial Stadium before finally being christened with its current moniker.  In the past it has served as an alternate home stadium for The University of Mississippi, Mississippi State University, and the University of Southern Mississippi.  From 1973 to 1990 the Egg Bowl was played there and from 1992 to 2013 it hosted the Mississippi High School Activities Association state championship football games.  In addition to college and high school games it has hosted several National Football League (NFL) preseason games.\n\n2009 Texas Bowl: The 2009 Texas Bowl was the fourth edition of the college football bowl game, and was played at Reliant Stadium in Houston, Texas.  The game started at 2:30 PM US CST on Thursday, December 31, 2009.  The game was telecast on ESPN for the first time in bowl history after being televised by the NFL Network for the first three games.  The Texas Bowl matched the Big 12 Conference sixth-place Missouri Tigers against independent Navy Midshipmen.  Navy defeated Missouri 35–13.\n\nCrump Stadium: Crump Stadium was a sports stadium in Memphis, Tennessee, built in 1934 and largely demolished in 2006.  It was built as a Works Progress Administration (WPA) project with a capacity of 7,500.  In 1939 it was enlarged to hold 25,000 spectators.  In 1948 and 1949 it staged the Delta Bowl, a college football bowl game.  In 1947 the Arkansas–Texas football game was played there.  The annual Ole Miss–Tennessee game was also held there in 1960s.  Memphis State University (now University of Memphis) home football games were played there until the completion of Memphis Memorial Stadium (now Liberty Bowl Memorial Stadium) in the mid-1960s.  The stadium was named for the late Memphis political boss E. H. Crump.  It is now home to Central High School.\n\nKiwanis Field: Kiwanis Field (formerly called Municipal Field) is a ballpark in Salem, Virginia which was opened in 1932.  The ballpark has a capacity of 5,000 people and is primarily used for baseball.  Kiwanis Field was the home of a Carolina League team currently known as the Salem Red Sox; at the time, they were the Salem Rebels (which had previously played in the Appalachian League), Salem Pirates, Salem Redbirds, and Salem Buccaneers.  The Salem Avalanche played here briefly in 1995 until they moved to the Salem Memorial Baseball Stadium.  The stadium has commanding views of the Blue Ridge Mountains, particularly Twelve O'clock Knob.  Until the Salem Football Stadium opened in 1985, Kiwanis Field served as the home football field for Salem High School and its predecessor Andrew Lewis High School.  The stadium was known as Salem Municipal Field prior to 1995.  Kiwanis Field is currently used for high school, American Legion, and Roanoke College baseball games.\n\nCampbell Field (Colorado): Campbell Field, officially Marv Kay Stadium at Harry D. Campbell Field, is an American college football stadium located in Golden, Colorado.  The stadium serves as the home field of the Colorado Mines Orediggers football team representing the Colorado School of Mines.  Campbell Field is one of the oldest football fields in existence, the oldest west of the Mississippi River and the oldest in NCAA Division II.  Originally it was a dirt surface all-purpose athletic field in exactly its current configuration, built within a clay pit, a fitting mined-out home for the Orediggers.  Its first athletic contest, held on May 20, 1893, was the first annual Colorado Inter-Collegiate Athletic Association Field Day, featuring many athletic contests between the University of Colorado, Colorado A&M, Colorado School of Mines, and the University of Denver, in which Mines claimed the most medals.  Its first football game took place on October 7, 1893, a 6-0 Mines victory over the University of Denver.  It has been home to the football Orediggers through all but the first five seasons of their existence (their previous home were the now-destroyed grounds at the southeast corner of 19th and Illinois streets in Golden), and has been renovated several times throughout its existence.  The field was originally called Athletic Park, renamed Brooks Field after Mines trustee and benefactor Ralph D. Brooks in 1922, and renamed Campbell Field after 1939 undefeated team member and benefactor Harry D. Campbell in 2010.  Campbell Field is the oldest football field in the west, the oldest in NCAA Division II football and the 5th oldest college football field in the nation.\n\nVeterans Memorial Stadium (League City): Veterans Memorial Stadium, often referred to simply as District Stadium, is a multi-purpose stadium located in League City, Texas on the campus of Clear Creek High School.  It is currently the only stadium in the Clear Creek Independent School District (CCISD) and is the home football field of all five 6A high schools in the district.  The stadium also hosts some of the district's soccer games.  Veterans Memorial Stadium is also home to the high school's powder puff football games.\n\nRockwell Field (Kent State): Rockwell Field was a multi-purpose athletic field on the campus of Kent State University in Kent, Ohio, United States.  It was the first home venue for the Kent State Golden Flashes football and the first permanent home for the KSU baseball program.  The field, sometimes referred to as \"Normal Field\", also hosted football games for the Kent State University School.  Rockwell Field served as the home field for Kent State football from the team's inception in 1920 through the 1940 season, the baseball team from circa 1920 through the 1941 season, and the men's track team from their foundation in 1922 through the 1940 season.  It was replaced by a new athletic complex that included a field for football with a track and an adjacent baseball field.  The new football field and track, later to become Memorial Stadium by 1950, were ready for the 1941 football and 1942 track seasons, while the baseball field opened in 1942.\n\n2009 Missouri Tigers football team: The 2009 Missouri Tigers football team, represented the University of Missouri in the 2009 NCAA Division I FBS football season.  The team was coached by Gary Pinkel, who returned for his ninth season with Mizzou, and played their home games at Faurot Field at Memorial Stadium.  Changes to Memorial Stadium for the 2009 season included a new scoreboard and expanded seating capacity following a reconfiguration of the student seating section.\n\nQuestion: In 2009, what Bowl did the University that calls their home football field Memorial Stadium play in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university.\"\n    },\n    \"home_stadium_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university's home football stadium.\"\n    },\n    \"bowl_game_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"bowl_game_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the bowl game played.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the bowl game was played.\"\n        },\n        \"opponent_team\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the opposing team in the bowl game.\"\n        },\n        \"university_score\": {\n          \"type\": \"integer\",\n          \"description\": \"The score of the university's team in the bowl game.\"\n        },\n        \"opponent_score\": {\n          \"type\": \"integer\",\n          \"description\": \"The score of the opponent team in the bowl game.\"\n        },\n        \"outcome\": {\n          \"type\": \"string\",\n          \"enum\": [\n            \"win\",\n            \"loss\"\n          ],\n          \"description\": \"The outcome of the bowl game for the university's team.\"\n        }\n      },\n      \"required\": [\n        \"bowl_game_name\",\n        \"year\",\n        \"opponent_team\",\n        \"university_score\",\n        \"opponent_score\",\n        \"outcome\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"home_stadium_name\",\n    \"bowl_game_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the university."
      },
      "home_stadium_name": {
        "type": "string",
        "description": "The name of the university's home football stadium."
      },
      "bowl_game_details": {
        "type": "object",
        "properties": {
          "bowl_game_name": {
            "type": "string",
            "description": "The name of the bowl game played."
          },
          "year": {
            "type": "integer",
            "description": "The year the bowl game was played."
          },
          "opponent_team": {
            "type": "string",
            "description": "The name of the opposing team in the bowl game."
          },
          "university_score": {
            "type": "integer",
            "description": "The score of the university's team in the bowl game."
          },
          "opponent_score": {
            "type": "integer",
            "description": "The score of the opponent team in the bowl game."
          },
          "outcome": {
            "type": "string",
            "enum": [
              "win",
              "loss"
            ],
            "description": "The outcome of the bowl game for the university's team."
          }
        },
        "required": [
          "bowl_game_name",
          "year",
          "opponent_team",
          "university_score",
          "opponent_score",
          "outcome"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "university_name",
      "home_stadium_name",
      "bowl_game_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
