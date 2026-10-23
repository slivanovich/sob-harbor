{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUniversity of Mary Hardin–Baylor: The University of Mary Hardin–Baylor (UMHB) is a Christian co-educational institution of higher learning located in Belton, Texas, United States.  UMHB was chartered by the Republic of Texas in 1845 as \"Baylor Female College,\" the female department of what is now Baylor University.  It has since become its own institution and grown to 3,898 students and awards degrees at the baccalaureate, master's, and doctoral levels.  It is affiliated with the Baptist General Convention of Texas.\n\nWesley Englehorn: Wesley Theodore \"Moose\" Englehorn (January 21, 1890 – September 3, 1993) was an American football player and coach.  Born in Helena, Montana, Englehorn first gained fame as a football player for Spokane High School.  While he was a junior in high school, he was reportedly recruited by Princeton University to come east to play football for the school.  A newspaper account in 1907 reported: \"It is expected that Wesley Englehorn, the giant left tackle of the high school team, will also enter the Eastern college.  If this materializes the Spokane high school will be weakened next year by the loss of two of its greatest players.  ... Englehorn is also a strong basket ball player and track athlete.\"  Englehorn did not enroll at Princeton and instead played for two years on the All Star Pacific Northwest football and basketball teams.  He began his collegiate career at Washington State College.  After playing one year of football at Washington State, Englehorn enrolled at Dartmouth College, where he played two years at the tackle position.  He was elected team captain for the 1913 season, but he was declared ineligible under \"the so-called three-year rule\" because of his year at Washington State.  Though ineligible to play, Englehorn served as the team's assistant coach in 1913 and was elected class president.  He was selected as a first-team All-American in 1912.  He graduated from Dartmouth in 1914 and worked as a football coach for several years thereafter.  From 1914 to 1916, he was the football coach at Case School of Applied Science in Cleveland, Ohio.  In 1917, he was hired as the line coach and first assistant football coach at Colgate University.  In 1920, he was an assistant coach under Frank Cavanaugh at Boston College.  In 1921, he was hired as the head football coach at Amherst College.  In January 1922, Englehorn announced his retirement from coaching.  Shortly before his death at age 103, Englehorn said, \"It's the football I remember best ... the teammates . .  the teamwork.\"  Prior to his death in 1993, he was living at Stapeley Hall, a home for the elderly in the Germantown section of Philadelphia, Pennsylvania, and was the oldest living All-American football player.\n\nDal Shealy: Dal Shealy (born August 1, 1938) is a former American football player and coach.  He served as the head coach at Mars Hill College in 1969, Carson–Newman College from 1970 to 1973, and at the University of Richmond from 1980 to 1988, compiling a career college football record of 79–74.  Shealy also served as an assistant coach at Baylor University, the University of Tennessee, Auburn University, and Iowa State University.  Shealy's son, Vic Shealy, is currently the head football coach at Houston Baptist University.\n\nPete Fredenburg: Pete Fredenburg (born September 15, 1949) is an American football coach and former player.  He is currently the head coach at the University of Mary Hardin–Baylor in Belton, Texas, a position he has held since the 1998 season when the program began play.  Fredenburg led Mary Hardin–Baylor to the NCAA Division III Football Championship in 2016.  His 2004 squad finished as runners-up, losing to Linfield.  Before coming to Mary Hardin–Baylor, Fredenburg served as an assistant coach at Baylor University (1982–1993), Louisiana State University (1994), and Louisiana Tech University (1995–1996).  He played football at Southwest Texas State University—now known as Texas State University–San Marcos—from 1968 to 1970.\n\nArt Baker (coach): Art Baker (born November 30, 1929) is a former American football coach.  He served as the head coach at Furman University (1973–1977), The Citadel, The Military College of South Carolina (1978–1982) and East Carolina University (1985–1988).  Baker is a 1948 graduate of Edmunds High School (now Sumter High School) in Sumter, S. C. and a 1953 Presbyterian College graduate and also was a former assistant football coach there.  Baker played football for the \"Blue Hose\" from 1950 to 1952, starting at halfback his last two years.  He was a member of Mu chapter of Pi Kappa Alpha fraternity.  Baker is a recipient of Presbyterian's Bob Waters Award.  He was an assistant coach for Frank Howard at Clemson from 1965 to 1969.  From 1970 to 1972, Baker was an assistant coach at Texas Tech.  Baker succeeded Bob King at Furman for the 1973 season.  As head coach at Furman Baker hired Dick Sheridan, Jimmy Satterfield and Bobby Johnson as assistants and all later became head coaches at Furman.  Baker was an assistant coach in 1984 for Bobby Bowden at Florida State.  He was Associate Athletics Director for Development and Gamecock Club Director at the University of South Carolina for 6 and a half years, retiring on June 30, 1995.\n\nBaylor University: Baylor University (BU) is a private Baptist university in Waco, Texas.  Chartered in 1845 by the last Congress of the Republic of Texas, it is the oldest continuously-operating university in Texas and one of the first educational institutions west of the Mississippi River in the United States.  Located on the banks of the Brazos River next to I-35, between the Dallas-Fort Worth Metroplex and Austin, the university's 1,000-acre campus is the largest Baptist university campus in the world.\n\nJerrell Freeman: Jerrell Alexander Freeman (born May 1, 1986) is an American football linebacker for the Chicago Bears of the National Football League (NFL).  He was signed as an undrafted free agent by the Tennessee Titans in 2008.  He played three seasons of football in the Canadian Football League for the Saskatchewan Roughriders.  In the 2011 season, he led the CFL in tackles.  In 2012, he signed with the Indianapolis Colts of the NFL.  Freeman played college football for the Mary Hardin-Baylor Crusaders under the direction of Coach Pete Fredenburg, and was twice named a D3football.com All-American, including being honored as the 2007 D3football.com Defensive Player of the Year.\n\nMorley Jennings: Morley \"Jopsey\" Jennings (January 23, 1890 – May 13, 1985) was an American football, basketball, and baseball player, coach, and college athletics administrator.  He attended college at Mississippi State University, where he participated in baseball, basketball, football, and track.  Jennings served as the head football coach at Ouachita Baptist University from 1912 to 1925 and at Baylor University from 1926 to 1940, compiling a career college football record of 153–77–18.  He was also the head baseball coach at Baylor from 1928 to 1939, tallying a mark of 120–79.  From 1941 to 1951, Jennings served as the athletic director at Texas Tech University.  He was inducted into the College Football Hall of Fame as a coach in 1973.\n\nFrank Kimbrough (American football): Frank H. Kimbrough (June 24, 1904 – February 4, 1971) was an American football player, coach of football and basketball, and college athletics administrator.  He served as the head football coach at Hardin–Simmons University (1935–1940), Baylor University (1941–1942, 1945–1946), and West Texas State University—now West Texas A&M University (1947–1957).  Kimbrough was also the head basketball coach at Hardin–Simmons from 1936 to 1941, tallying a mark of 29–50.  He was the brother of former Texas A&M star football player John Kimbrough.\n\nFrank Bridges: Frank B. Bridges (July 4, 1890 – June 10, 1970) was an American football, basketball, and baseball coach.  He served as the head football coach at Baylor University from 1920 to 1925, at Simmons University—now Hardin–Simmons University—from 1927 to 1929, and at St. Mary's University in San Antonio, Texas during the 1930s.  Bridges was also the head basketball coach at Baylor from 1920 to 1926, at Simmons from 1927 to 1929, and at St. Mary's from 1935 to 1939, tallying a career college basketball mark of 104–135.  In addition, he was Baylor's head baseball coach from 1920 to 1927, amassing a record of 95–73, and the head baseball coach at St. Mary's in 1938.  In 1944, Bridges served as the co-head coach with Pete Cawthon and Ed Kubale for the Brooklyn Tigers of the National Football League (NFL).\n\nQuestion: Pete Fredenburg, is an American football coach and former player, before coming to Mary Hardin–Baylor, Fredenburg served as an assistant coach at which private Baptist university in Waco, Texas, chartered in 1845 by the last Congress of the Republic of Texas, it is the oldest continuously-operating university in Texas and one of the first educational institutions west of the Mississippi River in the United States?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university.\"\n    },\n    \"university_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of university, e.g., 'private Baptist university'.\"\n    },\n    \"location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where the university is located.\"\n    },\n    \"charter_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the university was chartered.\"\n    },\n    \"chartering_authority\": {\n      \"type\": \"string\",\n      \"description\": \"The entity that chartered the university.\"\n    },\n    \"is_oldest_continuously_operating_in_texas\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the university is the oldest continuously-operating university in Texas.\"\n    },\n    \"is_one_of_first_educational_institutions_west_of_mississippi\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the university is one of the first educational institutions west of the Mississippi River.\"\n    },\n    \"coach_affiliation\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"coach_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the coach affiliated with the university.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role the coach held at the university.\"\n        },\n        \"start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the coach's tenure.\"\n        },\n        \"end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the coach's tenure.\"\n        }\n      },\n      \"required\": [\n        \"coach_name\",\n        \"role\",\n        \"start_year\",\n        \"end_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"university_type\",\n    \"location\",\n    \"charter_year\",\n    \"chartering_authority\",\n    \"is_oldest_continuously_operating_in_texas\",\n    \"is_one_of_first_educational_institutions_west_of_mississippi\",\n    \"coach_affiliation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the university."
      },
      "university_type": {
        "type": "string",
        "description": "The type of university, e.g., 'private Baptist university'."
      },
      "location": {
        "type": "string",
        "description": "The city and state where the university is located."
      },
      "charter_year": {
        "type": "integer",
        "description": "The year the university was chartered."
      },
      "chartering_authority": {
        "type": "string",
        "description": "The entity that chartered the university."
      },
      "is_oldest_continuously_operating_in_texas": {
        "type": "boolean",
        "description": "Indicates if the university is the oldest continuously-operating university in Texas."
      },
      "is_one_of_first_educational_institutions_west_of_mississippi": {
        "type": "boolean",
        "description": "Indicates if the university is one of the first educational institutions west of the Mississippi River."
      },
      "coach_affiliation": {
        "type": "object",
        "properties": {
          "coach_name": {
            "type": "string",
            "description": "The name of the coach affiliated with the university."
          },
          "role": {
            "type": "string",
            "description": "The role the coach held at the university."
          },
          "start_year": {
            "type": "integer",
            "description": "The start year of the coach's tenure."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the coach's tenure."
          }
        },
        "required": [
          "coach_name",
          "role",
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "university_name",
      "university_type",
      "location",
      "charter_year",
      "chartering_authority",
      "is_oldest_continuously_operating_in_texas",
      "is_one_of_first_educational_institutions_west_of_mississippi",
      "coach_affiliation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
