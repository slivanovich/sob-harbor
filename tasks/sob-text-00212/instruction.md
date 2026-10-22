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
Bernie Williams (basketball): Bernard "Bernie" Williams (December 30, 1945 – c. 2002 ) was an American basketball player who attended DeMatha Catholic High School, a college preparatory high school in Hyattsville, Maryland near Washington, D.C.  In 1965 he was a senior and a starter on the DeMatha team that beat New York City's Power Memorial Academy 46-43 on January 30.  Power, led by 7' 1" senior Lew Alcindor (later Kareem Abdul-Jabbar) had won 71 games in a row.  Sports writers at the time and later called it the greatest high school basketball game ever.

Long Island Lutheran Middle and High School: Long Island Lutheran Middle and High School is a Lutheran college preparatory school in Brookville, New York.  Founded and built in 1960 on a 32-acre estate, Long Island Lutheran, commonly known as LuHi, has a student body of approximately 600 students in grades 6-12, with students coming from more than 50 school districts throughout Long Island and New York City.  The school is accredited by the Middle States Association of Colleges and Schools and is a member of the New York State Association of Independent Schools.

Lutheran High School of San Antonio: Lutheran High School of San Antonio (LHSSA), an accredited college preparatory Christian high school in the Lutheran education tradition, nurtures faith and discipleship and promotes academic excellence to cultivate Christian servant leaders.  The School is located in San Antonio in the U.S. state of Texas.  As the city’s only Lutheran high school, LHSSA is supported by six congregations of the Lutheran Church–Missouri Synod forming the Lutheran High School Association.

Northeast College Preparatory School: Northeast College Preparatory School is a public high school located in Rochester, Monroe County, New York, U.S.A., and is one of eighteen high schools operated by the Rochester City School District.  It shares the Douglass Campus with the Northwest College Preparatory School.

Northwestern Preparatory School: Northwestern Preparatory School was a four-year Lutheran high school founded in 1865 and located in Watertown, Wisconsin.  The school merged with Martin Luther Preparatory School in 1995 to become Luther Preparatory School.  It was affiliated with Northwestern College of Watertown, which merged with Dr. Martin Luther College of New Ulm, Minnesota in 1995 to become Martin Luther College.

St. Francis Preparatory School: St. Francis Preparatory School, commonly known as St. Francis Prep, is a private, independent Catholic college preparatory school in the Fresh Meadows neighborhood of the New York City Borough of Queens, in the State of New York.  It is the largest non-diocesan Catholic high school in the United States.  St. Francis is run by the Franciscan Brothers of Brooklyn, who maintain a residence on the top floor of the school.  The school has a student body of about 2,750 students and graduates between 600 and 700 students annually.

Dalton School: The Dalton School, originally the Children's University School, is a private, coeducational college preparatory school on New York City's Upper East Side and a member of both the Ivy Preparatory School League and the New York Interschool.  The school is located in three buildings within Manhattan.

Horace Mann School: Horace Mann School (also known as Horace Mann or HM) is an independent college preparatory school in the Bronx, founded in 1887.  Horace Mann is a member of the Ivy Preparatory School League, educating students from the New York metropolitan area from nursery school to the twelfth grade.  The Upper, Middle, and Lower Divisions are located in Riverdale, a neighborhood of the Bronx, while the Nursery School is located in Manhattan.  The John Dorr Nature Laboratory, a 275 acre campus in Washington Depot, Connecticut, serves as the school's outdoor and community education center.  Tuition for the 2014–15 school year is $43,300 from nursery through twelfth grade, making it the second most expensive private school in New York City.  Niche (company) ranks Horace Mann #1 in its list of 2017 Best Private High Schools in New York.

Reggie Carter: Reginald "Reggie" Carter (October 10, 1957 – December 24, 1999) was an American basketball player.  At 6'3" (1.90 m) and 175 lb (79 kg), he played as a guard.  Born in New York City, he played collegiately for the St. John's University and the University of Hawaii after spending his schoolboy years starring for Long Island Lutheran High School in Brookville, New York.  He was selected by the National Basketball Association's New York Knicks in the 2nd round (27th pick overall) of the 1979 NBA Draft.  He played with the Knicks from 1980 to 1982 for 135 games.  Reggie became an assistant principal at Mineola High School before dying of a heart attack.

St. Paul's Lutheran School: St. Paul's Lutheran Elementary School is a private school located in East Northport, New York.  It is a member of the Long Island Lutheran Middle and High School Congregation Association.

Question: Reginald "Reggie" Carter, was an American basketball player, born in New York City, he played his schoolboy years starring for Long Island Lutheran High School, a Lutheran college preparatory school in which city in New York?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the basketball player."
    },
    "school_name": {
      "type": "string",
      "description": "The name of the high school the player attended."
    },
    "school_type": {
      "type": "string",
      "description": "The type of school."
    },
    "school_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the school is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the school is located."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "answer_city": {
      "type": "string",
      "description": "The specific city requested in the question."
    }
  },
  "required": [
    "player_name",
    "school_name",
    "school_type",
    "school_location",
    "answer_city"
  ],
  "additionalProperties": false
}
