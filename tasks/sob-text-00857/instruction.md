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
Ohio University Aquatic Center: Ohio University's Aquatic Center is the swimming and diving facility of the Ohio Bobcats.  It has been home to Ohio Bobcats swimming and diving since it was opened on January 27, 1984 before a dual meet against the Youngstown State University Penguins.

Chessa Field: Chessa Field is the women's soccer field of the Ohio Bobcats.  It was opened under the name of "Ohio Soccer Field" on September 6, 1997.  On that day, Ohio defeated the Youngstown State University Penguins 2-0 in what was also the first home varsity women's soccer game in the history of Ohio University.

Bill Hess: William R. Hess (February 5, 1923 – June 10, 1978) was an American football coach.  He served as the head football coach at Ohio University from 1958 to 1977.  In his tenure as head coach for the Ohio Bobcats football team, Hess compiled a 108–91–4 record, ranking him second only to coach Don Peden on Ohio's all-time victories list.  Hess's teams won four Mid-American Conference (MAC) championships (1960, 1963, 1967, and 1968) and won a National Small College Championship in 1960 after having an undefeated season.  Hess also led the Bobcats to two bowl games, losing 15–14 to West Texas State in the 1962 Sun Bowl and losing 49–42 to Richmond in the 1968 Tangerine Bowl.  His 1968 team is the only team in school history to finish ranked in the major polls.  Hess was a native of Columbus, Ohio.  He coached high school football in Portsmouth and Grandview Heights, Ohio before joining Woody Hayes's staff at Ohio State University in 1951.

1948 Ohio Bobcats football team: The 1948 Ohio Bobcats football team was an American football team that represented Ohio University in the Mid-American Conference (MAC) during the 1948 college football season.  In their second and final season under head coach Harold Wise, the Bobcats compiled a 3–6 record (2–3 against MAC opponents), finished in fourth place in the MAC, and were outscored by all opponents by a combined total of 179 to 98.  Three Ohio players received All-MAC honors: end John Marco (first team); halfback Jim McKenna (second team); and offensive guard Milt Taylor (second team).

2011–12 Ohio Bobcats men's basketball team: The 2011–12 Ohio Bobcats men's basketball team represented Ohio University during the 2011–12 NCAA Division I men's basketball season.  The Bobcats, led by fourth year head coach John Groce, played their home games at the Convocation Center and are members of the East Division of the Mid-American Conference.  They finished the season 29–8, 11–5 in MAC play to finish in third place in the East Division.  They were champions of the MAC Basketball Tournament and earned an automatic bid into the 2012 NCAA Tournament where the 13th seeded Bobcats defeated Michigan in the second round and South Florida in the third round to advance to school's first "Sweet Sixteen" since 1964.  They lost in the "Sweet Sixteen" to North Carolina in overtime.

Ohio Bobcats baseball: The Ohio Bobcats baseball team is a varsity intercollegiate athletic team of Ohio University in Athens, Ohio, United States.  The team is a member of the Mid-American Conference East division, which is part of the National Collegiate Athletic Association's Division I.  Ohio's first baseball team was fielded in 1892.  The team plays its home games at Bob Wren Stadium in Athens, Ohio.  The Bobcats are coached by Rob Smith.

2012 Ohio Bobcats football team: The 2012 Ohio Bobcats football team represented Ohio University in the 2012 NCAA Division I FBS football season.  They were led by eighth-year head coach Frank Solich and played their home games at Peden Stadium.  They were a member of the East Division of the Mid-American Conference (MAC).  After defeating Akron on October 13 to become 7–0 the Bobcats were ranked #25 in the AP Poll; Ohio had not been ranked nationally since 1968.  On October 21, 2012, the Bobcats peaked at #23 in both the Coaches Poll and AP Poll, and #24 in the BCS standings.  They finished the season 9–4, 4–4 in MAC play to finish in third place in the East Division.  They were invited to the Independence Bowl where they defeated Louisiana–Monroe for their second consecutive bowl victory.

1949 Ohio Bobcats football team: The 1949 Ohio Bobcats football team was an American football team that represented Ohio University in the Mid-American Conference (MAC) during the 1949 college football season.  In their first season under head coach Carroll Widdoes, the Bobcats compiled a 4–4–1 record (2–2 against MAC opponents), finished in third place in the MAC, and were outscored by all opponents by a combined total of 120 to 114.  Three Ohio players received All-MAC honors: offensive tackle Al Scheider (first team); offensive guard Milt Taylor (first team); and end John Marco (second team).

Jim Snyder (coach): James E. Snyder (June 29, 1919 – April 27, 1994) was head coach of the Ohio Bobcats men's basketball team for 26 years (1949–1974).  He amassed 20 winning seasons and led his teams to 7 NCAA Tournament appearances (1960, 1961, 1964, 1965, 1970, 1972, and 1974) and one National Invitation Tournament appearance (1969).  Snyder's teams compiled a 355-255 record, good for a .581 winning percentage.  He was also an Ohio graduate (Class of 1941), and was a football and basketball star as an undergraduate in the late 1930s and early 1940s.  One of his most memorable wins came against the University of Kentucky in the 1964 NCAA tournament, advancing the Ohio Bobcats to the Elite 8.  One interesting aspect of this game was that Ohio had an integrated team while Kentucky had one of its last all white teams.  Snyder was widely admired throughout the college basketball coaching fraternity as being a coach with great integrity and an engaging personality; he was often referred to as "Gentleman Jim."

Youngstown State University: Youngstown State University (YSU), founded in 1908, is an urban research university located in Youngstown, Ohio, United States.  As of fall 2010, there were 15,194 students and a student-faculty ratio of 19:1.  The fall 2010 enrollment figure is the highest since 1990, when the number of students on campus was 15,454.  Records show that 11,803 of the students are undergraduates.  Beyond its current student body, YSU claims more than 94,000 alumni.

Question: Where was the dual placed between Ohio Bobcats and a university team of Youngstown, Ohio, United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_type": {
      "type": "string",
      "description": "The type of athletic event."
    },
    "participating_teams": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "team_name": {
            "type": "string",
            "description": "Name of the participating team."
          },
          "university_name": {
            "type": "string",
            "description": "Name of the university the team represents."
          }
        },
        "required": [
          "team_name",
          "university_name"
        ],
        "additionalProperties": false
      },
      "description": "List of teams that participated in the event."
    },
    "location": {
      "type": "string",
      "description": "The venue where the event took place."
    },
    "opening_date_of_location": {
      "type": "string",
      "description": "The date the location was opened."
    }
  },
  "required": [
    "event_type",
    "participating_teams",
    "location"
  ],
  "additionalProperties": false
}
