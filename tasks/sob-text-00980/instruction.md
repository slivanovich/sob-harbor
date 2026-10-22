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
New England Collegiate Conference (Division II): The New England Collegiate Conference (NECC) was an NCAA Division II college athletic conference based in the Northeastern United States that dissolved during the late 1990s after most of its members either moved to Division I or joined Division II leagues such as the Northeast-10 Conference or the New York Collegiate Athletic Conference, now known as the East Coast Conference.

Mackenzie Stadium: Mackenzie Stadium is a baseball venue located in Holyoke, Massachusetts.  It was home to the Holyoke Millers and today is used by both the Valley Blue Sox of the New England Collegiate Baseball League (since 2008) and the Elms College Blazers of the New England Collegiate Conference (since 2005).  It was built in 1933 and has a capacity of 4,100 people.

Elms College: The College of Our Lady of the Elms, often called Elms College, is a Catholic liberal arts college located in Chicopee, Massachusetts, near Springfield.  The campus is located in the Springfield Street Historic District, near the Chicopee city-center.

AMCC Men's Basketball Tournament: The Allegheny Mountain Collegiate Conference Men's Basketball Tournament is the annual conference basketball championship tournament for the NCAA Division III Allegheny Mountain Collegiate Conference.  The tournament has been held annually since the AMCC was founded in 1998.  It is a single-elimination tournament and seeding is based on regular season records.

List of CHA Men's Ice Hockey Tournament champions: College Hockey America (CHA) is a National Collegiate Athletic Association (NCAA) Division I ice hockey-only conference based in Detroit, Michigan that was formed in mid-1999 after the dissolution of Division II ice hockey.  CHA was originally a men's and women's ice hockey conference, but has been a women's-only conference since 2010 when Niagara and Robert Morris joined Atlantic Hockey, Bemidji State joined the Western Collegiate Hockey Association, and Alabama–Huntsville became an independent school.  After the completion of each regular season, it held the CHA Men's Ice Hockey Tournament to determine its men's conference champion.  In 2001, CHA commissioned the Bruce M. McLeod Trophy, named after its first commissioner, which was awarded to the tournament champion.  In 2003, CHA was granted an annual automatic bid to the NCAA Men's Ice Hockey Championship for its tournament champion.  Before this, the only CHA team to have played in the national championship tournament was Niagara, which received an at-large bid into the 2000 tournament.  No CHA team won a national championship, and until 2009, Niagara was the only CHA team to have advanced past the first round.  In the 2009 tournament, Bemidji State became the only CHA team and 16th ranked seed to ever advance to the Frozen Four.

Western Collegiate Cycling Conference: The WCCC or Western Collegiate Cycling Conference is a collegiate cycling conference based in the western United States.  The conference is composed of 29 schools from California, Northern Nevada, and even Hawaii.  Schools include current Road National Champions UC Davis as well as former champions Stanford and UC Berkeley.  The schools in the conference compete in bicycle racing with road cycling races in the spring and mountain bike racing in the fall.  The conference is governed by the National Collegiate Cycling Association, a division of USA Cycling.  The conference is split up into two divisions.

Metropolitan Collegiate Conference: The Metropolitan Collegiate Conference (MCC) was a college athletic conference that exited from 1965 until 1969.  The conference was also known as the Middle Eastern Collegiate Conference (MECC).  The participating schools were exclusively from New York and New Jersey.  The 10 founding members of the conference in 1965 were: Manhattan, Long Island University, New York University, Hofstra, Fairleigh Dickinson, Saint Peter's, Seton Hall, Iona, Wagner and St. Francis.

New England Collegiate Conference: The New England Collegiate Conference (NECC) is an NCAA Division III college athletic conference based in the Northeastern United States.

Wisconsin Collegiate Conference: The Wisconsin Collegiate Conference (WCC) is an athletic conference made up of the two year campuses in the University of Wisconsin System.  The teams compete in soccer, volleyball, basketball, tennis, and golf.  Baseball is also offered at some campuses.  The campuses also compete in the Wisconsin Junior College Athletic Association (WJCAA), which is a combination of the Wisconsin Collegiate Conference and the Wisconsin Technical College Conference.  All teams are considered junior colleges and athletes are only eligible for 2 years.

Heartland Collegiate Conference: The Heartland Collegiate Conference (HCC) was a football-only intercollegiate athletic conference that evolved out of the Indiana Collegiate Conference (ICC) and competed between 1978 and 1989.  Originally comprising the football-playing arm of the ICC, the HCC became its own separate entity after the ICC was dissolved in 1979.  The HCC continued for ten more seasons before its own collapse in 1989.  When formed in 1978, the conference had members in the states of Indiana, Ohio, and Kentucky.

Question: Elms College Blazers plays in a collegiate conference based in which location ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "college_name": {
      "type": "string",
      "description": "The name of the college."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the athletic team."
    },
    "conference_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the collegiate conference."
        },
        "division": {
          "type": "string",
          "description": "The NCAA division of the conference."
        },
        "location": {
          "type": "string",
          "description": "The general geographic location where the conference is based."
        }
      },
      "required": [
        "name",
        "division",
        "location"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "college_name",
    "team_name",
    "conference_info"
  ],
  "additionalProperties": false
}
