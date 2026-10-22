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
2014–15 WKU Lady Toppers basketball team: The 2014–15 WKU Lady Toppers basketball team represents Western Kentucky University during the 2014–15 NCAA Division I women's basketball season.  The Lady Toppers were led by second year head coach Michelle Clark-Heard.  They play their home games at E. A. Diddle Arena and were first year members of Conference USA.  They finished the season 30–5, 16–2 in C-USA play to win the Conference USA regular season and also won the Conference USA Tournament.  They received an automatic bid to the NCAA Women's Basketball Tournament where they were defeated by Texas in the first round.

Catholic Conference (MIAA): The Catholic Conference is a Massachusetts high school athletic conference whose member institutions arer located primarily in Eastern part of Massachusetts.  Its five members include only all-boys Catholic high schools.  The Catholic Conference participates in the Massachusetts Interscholastic Athletic Association (MIAA) Division I in sports competitions.

Eastern Intercollegiate Volleyball Association: The Eastern Intercollegiate Volleyball Association (EIVA) is a college athletic conference whose member schools compete in men's volleyball.  Its member institutions are located in the Northeast United States.

Conference Carolinas: Conference Carolinas, formerly known as the Carolinas-Virginia Athletic Conference (CVAC) or the Carolinas Conference, is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA) primarily in Division II, and as one of the four Division I conferences for men's volleyball.  Originally formed in 1930, the league reached its modern incarnation in 1994.  Member institutions are located in the southeastern United States in the states of Georgia, North Carolina, South Carolina, and Tennessee.  Conference Carolinas currently has 11 small college or university private institutions that make-up their membership.

Atlantic Coast Conference: The Atlantic Coast Conference (ACC) is a collegiate athletic conference in the United States of America in which its fifteen member universities compete in the National Collegiate Athletic Association (NCAA)'s Division I, with its football teams competing in the Football Bowl Subdivision (FBS), the highest levels for athletic competition in US-based collegiate sports.  The ACC sponsors competition in twenty-five sports with many of its member institutions' athletic programs held in high regard nationally.  Members of the conference are Boston College, Clemson University, Duke University, Georgia Tech, Florida State University, North Carolina State University, Syracuse University, the University of Louisville, the University of Miami, the University of North Carolina, the University of Notre Dame, the University of Pittsburgh, the University of Virginia, Virginia Tech, and Wake Forest University.

Big West Conference: The Big West Conference (BWC) is an American collegiate athletic conference whose member institutions participate in the National Collegiate Athletic Association's Division I.  The conference was originally formed in 1969 as the Pacific Coast Athletic Association (PCAA) and in 1988 was renamed the Big West Conference.  The conference stopped sponsoring college football after the 2000 season.

Ohio Community College Athletic Conference: The Ohio Community College Athletic Conference or OCCAC is a college athletic conference whose member institutions are community colleges in the state of Ohio.  It is a member of Region XII of the National Junior College Athletic Association.

Southeastern Conference: The Southeastern Conference (SEC) is an American college athletic conference whose member institutions are located primarily in the Southern part of the United States.  Its fourteen members include the flagship public universities of ten states, three additional public land grant universities, and one private research university.  The conference is headquartered in Birmingham, Alabama.  The SEC participates in the National Collegiate Athletic Association (NCAA) Division I in sports competitions; for football, it is part of the Football Bowl Subdivision (FBS), formerly known as Division I-A.

Conference USA: Conference USA (C-USA or CUSA) is a collegiate athletic conference whose member institutions are located within the Southern United States.  The conference participates in the NCAA's Division I in all sports.  C-USA's offices are located in the Las Colinas business district of the Dallas suburb of Irving, Texas.

Atlantic 10 Conference: The Atlantic 10 Conference (A-10) is a collegiate athletic conference whose schools compete in the National Collegiate Athletic Association's (NCAA) Division I.  The A-10's member schools are located in states mostly on the United States Eastern Seaboard, as well as some in the Midwest – Massachusetts, New York, North Carolina, Pennsylvania, Rhode Island, Virginia, Ohio, and Missouri as well as in the District of Columbia.  Although some of its members are state-funded, half of its membership is made up of private, Catholic institutions.  Despite the name, there are 14 full-time members, and two affiliate members that participate in women's field hockey only.

Question: Who was the head coach whose team were first year members in a collegiate athletic conference whose member institutions are located within the Southern United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the head coach."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team coached by the individual."
    },
    "season": {
      "type": "string",
      "description": "The athletic season during which the events occurred."
    },
    "conference_details": {
      "type": "object",
      "properties": {
        "conference_name": {
          "type": "string",
          "description": "The name of the collegiate athletic conference."
        },
        "first_year_member": {
          "type": "boolean",
          "description": "Indicates if the team was a first-year member of the conference."
        },
        "conference_location_region": {
          "type": "string",
          "description": "The primary geographical region where the conference's member institutions are located."
        }
      },
      "required": [
        "conference_name",
        "first_year_member",
        "conference_location_region"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "coach_name",
    "team_name",
    "season",
    "conference_details"
  ],
  "additionalProperties": false
}
