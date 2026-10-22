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
2005 Louisville Cardinals football team: The 2005 Louisville Cardinals football team represented the University of Louisville in the 2005 NCAA Division I-A football season.  The team, led by Bobby Petrino in his third year at the school, played their home games in Papa John's Cardinal Stadium.  They finished 9–3 in their first season as a member of the Big East Conference with a 5–2 conference record.

2004 Louisville Cardinals football team: The 2004 Louisville Cardinals football team represented the University of Louisville in the 2004 NCAA Division I-A football season.  The team, led by Bobby Petrino in his second year at the school, played their home games in Papa John's Cardinal Stadium.  They finished 11–1 and were the Conference USA champions with a perfect 8–0 conference record in their last season before leaving to join the Big East Conference.  They were invited to and won the Liberty Bowl, defeating Western Athletic Conference champion Boise State 44–40.

1978 Lamar Cardinals football team: The 1978 Lamar Cardinals football team represented Lamar University in the 1978 NCAA Division I-A football season as a member of the Southland Conference.  NCAA Division I split into Division I-A, the current Football Bowl Subdivision (FBS), and Division I-AA, the current Football Championship Subdivision (FCS), for football in 1978.  Lamar and the Southland Conference opted to compete at the Division I-A level.  The Cardinals played their home games at Cardinal Stadium now named Provost Umphrey Stadium in Beaumont, Texas.  Lamar finished the 1978 season with a 2–8–1 overall record and a 0–5 conference record.  The 1978 season marked Bob Frederick's final season as Lamar's head football coach.

2015 Louisville Cardinals football team: The 2015 Louisville Cardinals football team represented the University of Louisville in the 2015 NCAA Division I FBS football season.  The Cardinals were led by second-year head coach Bobby Petrino, who began his second stint at Louisville in 2014 season after eight years away.  The team played its 18th season at its current home of Papa John's Cardinal Stadium in Louisville, Kentucky.  They competed in the Atlantic Coast Conference in the Atlantic Division.  They finished the season 8–5, 5–3 in ACC play to finish in third place in the Atlantic Division.  They were invited to the Music City Bowl where they defeated Texas A&M.

2016 Louisville Cardinals football team: The 2016 Louisville Cardinals football team represents the University of Louisville in the 2016 NCAA Division I FBS football season.  The Cardinals are led by third-year head coach Bobby Petrino, who began his second stint at Louisville in 2014 after eight years away.  The team plays their home games at Papa John's Cardinal Stadium in Louisville, Kentucky.  The Cardinals compete as a member of the Atlantic Division in the Atlantic Coast Conference.

2014 Louisville Cardinals football team: The 2014 Louisville Cardinals football team represented the University of Louisville in the 2014 NCAA Division I FBS football season.  The Cardinals were led by head coach Bobby Petrino, who began his second stint at Louisville after eight years away, seven of which were spent as a head coach at other colleges and in the National Football League (NFL).  The team played its 17th season at Papa John's Cardinal Stadium in Louisville, Kentucky.  They were in their first season as members of the Atlantic Coast Conference, having replaced departed member Maryland in the Atlantic Division.  They finished the season 9–4, 5–3 in ACC play to finish in third place in the Atlantic Division.  They were invited to the Belk Bowl, where they lost to Georgia.

2006 Louisville Cardinals football team: The 2006 Louisville Cardinals football team represented the University of Louisville in the 2006 NCAA Division I FBS football season.  The team, led by Bobby Petrino in his fourth year at the school, played their home games in Papa John's Cardinal Stadium.  Playing in their second year in the Big East Conference, the team finished the regular season with eleven wins and one loss and were conference champions.  They represented the Big East in the 2007 Orange Bowl and with the win ended the season with a 12-1 record.  The team ended the season ranked fifth in the nation.

Bobby Petrino: Robert Patrick Petrino (born March 10, 1961) is an American football coach, former player

2002 Auburn Tigers football team: The 2002 Auburn Tigers football team represented Auburn University in the 2002 NCAA Division I-A football season.  Auburn, led by head coach Tommy Tuberville, finished with record of 9–4, including a 5–3 record in the Southeastern Conference.  Following a disappointing 7–5 finish the previous season, the coaching staff of the 2002 Tigers featured two prominent new members.  Bobby Petrino was hired as the new offensive coordinator, and Gene Chizik joined the staff as the Tigers' new defensive coordinator.  Petrino left following the season to assume the head coaching job at Louisville, while Chizik remained at Auburn through the 2004 season before leaving for the defensive coordinator position at Texas.  The Tigers finished the season ranked #14 in the AP Poll and #16 in the Coaches Poll.

2003 Louisville Cardinals football team: The 2003 Louisville Cardinals football team represented the University of Louisville in the 2003 NCAA Division I-A football season.  The team, led by Bobby Petrino in his first year at the school, played their home games in Papa John's Cardinal Stadium.

Question: The 2003 Louisville Cardinals football team represented the University of Louisville in the 2003 NCAA Division I-A football season, the team was led by Bobby Petrino in his first year at the school, is an American football coach,and former player, born on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "role": {
      "type": "string",
      "description": "The primary role or profession of the person."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the person in 'Month Day, Year' format."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the person."
    }
  },
  "required": [
    "person_name",
    "role",
    "birth_date",
    "birth_year"
  ],
  "additionalProperties": false
}
