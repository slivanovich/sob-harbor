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
Peach Belt Conference: The Peach Belt Conference (PBC) is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA)'s Division II level.  Since its inception in 1990-91, the Peach Belt has developed a consistent history of excellence which continues to this day with 30 national championships and 27 national finalists.  Starting with only two championships in 1991, in men's and women's basketball, the conference has expanded to 13 championship sports with the addition of women's golf in the fall of 2009.

Gulf South Conference: The Gulf South Conference (GSC) is a collegiate athletic conference affiliated at the National Collegiate Athletic Association (NCAA) Division II level which operates in the southeastern United States.

Northeast-10 Conference: The Northeast-10 Conference is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA)’s Division II level.  Member institutions are located in the northeastern United States in the states of Connecticut, Massachusetts, New Hampshire, New York, and Vermont.  It is the only Division II collegiate hockey conference in the United States.

Southern Conference: The Southern Conference (SoCon) is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA) Division I.  Southern Conference football teams compete in the Football Championship Subdivision (formerly known as Division I-AA).  Member institutions are located in the states of Alabama, Georgia, North Carolina, South Carolina, Tennessee, and Virginia.

North Alabama Lions football: The North Alabama Lions football team represents the University of North Alabama (UNA) in NCAA Division II competing as a member of the Gulf South Conference (GSC).  UNA plays its home games at Braly Municipal Stadium in Florence, Alabama.  They are currently coached by Chris Willis.

Men's National Collegiate Athletic Association: The Men's National Collegiate Athletic Association is an athletic association in the Philippines, and is the direct counterpart of the older Women's National Collegiate Athletic Association (founded in 1970).  The Men's National Collegiate Athletic Association (MNCAA) is exclusive for men.  The MNCAA was founded in 2004.  Competition is divided into three divisions: Seniors for college students, Juniors for high school students, and Midgets for grade school and first year high school students.  The competing sports of the tournament are Basketball, Volleyball, Futsal, Table Tennis, Badminton and Streetdance.

Heartland Conference: The Heartland Conference is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA)'s Division II level, which was founded in 1999.  The majority of members are in Texas, with additional members in Arkansas, Kansas, and Oklahoma.  The conference office is located in Waco, Texas.

Conference Carolinas: Conference Carolinas, formerly known as the Carolinas-Virginia Athletic Conference (CVAC) or the Carolinas Conference, is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA) primarily in Division II, and as one of the four Division I conferences for men's volleyball.  Originally formed in 1930, the league reached its modern incarnation in 1994.  Member institutions are located in the southeastern United States in the states of Georgia, North Carolina, South Carolina, and Tennessee.  Conference Carolinas currently has 11 small college or university private institutions that make-up their membership.

Ohio Collegiate Athletic Conference: The Ohio Collegiate Athletic Conference was a collegiate athletic conference affiliated with the United States Collegiate Athletic Association (USCAA) that began play as an athletic conference in 2009.

Central Atlantic Collegiate Conference: The Central Atlantic Collegiate Conference (or CACC) is a collegiate athletic conference affiliated with the National Collegiate Athletic Association (NCAA)'s Division II.  Member institutions are located in the northeastern United States in the states of Connecticut, Delaware, New Jersey, New York, and Pennsylvania.

Question: Which conference affiliated National Collegiate Athletic Association has a team coached by Chris Willis in it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "conference_name": {
      "type": "string",
      "description": "The name of the collegiate athletic conference."
    },
    "ncaa_affiliation_division": {
      "type": "string",
      "description": "The NCAA division the conference is affiliated with."
    },
    "team_coached_by_chris_willis": {
      "type": "string",
      "description": "The name of the team coached by Chris Willis."
    },
    "coach_name": {
      "type": "string",
      "description": "The name of the coach."
    }
  },
  "required": [
    "conference_name",
    "ncaa_affiliation_division",
    "team_coached_by_chris_willis",
    "coach_name"
  ],
  "additionalProperties": false
}
