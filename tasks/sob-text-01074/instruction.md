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
Michael Tyler (DNC spokesman): Michael Tyler was named, April 2017, as the spokesman (non-gender specific Spokesperson), for the Democratic National Committee under the leadership of Tom Perez.  Tyler previously served as the communications director of Russ Fiengold.  In August 2017 and after Steve Bannon's departure from the Donald J. Trump's administration, Tyler stated that is "one less white supremacist in the White House".  After the accusation that the DNC's data was flawed and contributed to the defeat of Clinton in the 2016 presidential race; Tyler conveyed that the party was in the process of overhauling its data and technological operations.

Andrew Tyler: Andrew Tyler (8 September 1946 - 28 April 2017) was the director of Animal Aid, the UK's second largest animal rights organization (after PETA) until 2016.  Tyler was an animal rights campaigner and journalist for 30 years.

Nicol Perez: Nicol Perez (born April 22 1993) is the 5th and former United States Youth Observer to the United Nations.  Perez has extensive experience working on youth issues at the local, regional and international level having previously worked in various international organizations as well as starting her own initiatives.  In her term as Youth Observer, Perez focused on the global refugee crisis, youth unemployment, and the U.N.’s Sustainable Development Goals for 2030.  In 2017, Perez founded Girlzftw, a mentorship program that pairs women under 30 with high school and college girls that need the support and encouragement of another girl to achieve their goals.

New Democratic Party leadership election, 2017: The 2017 New Democratic Party leadership election will take place between September 18 and October 15, 2017 due to incumbent Tom Mulcair having lost a vote on a leadership review at the New Democratic Party (NDP)'s federal convention held in Edmonton, Alberta on April 10, 2016.  Fifty-two per cent of delegates voted in favour of holding a new leadership election, compared to forty-eight per cent who voted for Mulcair's leadership to continue.  Under the party's constitution, the leadership election was to be held by April 10, 2017; however, the delegates present passed a motion to give the party up to 24 months to organize a leadership election.  Mulcair remained leader until the election of his successor.  The election was won by Jagmeet Singh in the first ballot, after winning a majority of the vote.

Ty Hensley: Michael Tyler Hensley (born July 30, 1993) is an American professional baseball pitcher for the Tampa Bay Rays' organization.  A first-round draft pick of the New York Yankees in the 2012 Major League Baseball Draft, Hensley plays in Minor League Baseball.

Maurice Tyler: Maurice Michael Tyler (born July 19, 1950 in Baltimore, Maryland) was an American football defensive back in the National Football League for the Buffalo Bills, Denver Broncos, San Diego Chargers, Detroit Lions, New York Jets, and the New York Giants.  He also spent the 1983 season with the Chicago Blitz and the Denver Gold of the United States Football League USFL.

Tom Perez: Thomas Edward Perez (born October 7, 1961) is an American Democratic Party politician and attorney who has served as the Chairman of the Democratic National Committee since February 2017.  Perez was the United States Secretary of Labor from 2013 to 2017.  Prior to that he worked as a consumer advocate and civil rights lawyer before serving as the Assistant Attorney General for Civil Rights from 2009 to 2013.

Deputy Chair of the Democratic National Committee: The Deputy Chair of the Democratic National Committee is a position within the United States Democratic Party that was re-established by Tom Perez in February 2017 after the 2017 DNC Chair race, won by Perez.

Jacob Perez: Jacob Perez (born April 21, 1996) professionally known as Princeton Perez, is an American singer-songwriter, professional dancer, and actor.  Born and raised in Downey, California, near Los Angeles, Perez began his career at a young age when he appeared in television advertisements for companies such as Nike, McDonald's, and Sketchers.  He was included in two Gym Class Heroes music videos, including Shoot Down the Stars (as a young school child), and Cupid's Chokehold (as Cupid Boy).  Perez rose to fame as a member of the boy band Mindless Behavior, in which he remained from 2008 until the groups disbandment in 2017.

James Michael Tyler: James Michael Tyler (born May 28, 1962) is an American actor best known for his role as Gunther on the NBC sitcom "Friends".

Question: Michael Tyler was named, April 2017, as the spokesman, for which organization, under the leadership of Tom Perez?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "role": {
      "type": "string",
      "description": "The role the person was named to."
    },
    "organization": {
      "type": "string",
      "description": "The organization the person was named spokesman for."
    },
    "leader_name": {
      "type": "string",
      "description": "The name of the leader of the organization at the time of appointment."
    },
    "appointment_year": {
      "type": "integer",
      "description": "The year the person was appointed to the role."
    },
    "appointment_month": {
      "type": "string",
      "description": "The month the person was appointed to the role."
    }
  },
  "required": [
    "person_name",
    "role",
    "organization",
    "leader_name",
    "appointment_year",
    "appointment_month"
  ],
  "additionalProperties": false
}
