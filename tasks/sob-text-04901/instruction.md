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
2010–11 Norwich City F.C. season: The 2010–11 season was the 109th season in the history of Norwich City.  It was the club's first season back in the Football League Championship (second tier of the English football pyramid), following promotion from League One in 2009–10.  Norwich finished as runners-up to Queens Park Rangers, confirming promotion to the Premier League in the penultimate match of the season with a 1–0 victory against Portsmouth at Fratton Park.  Thus they became the first side since Manchester City in the 1999–2000 season to win successive promotions to the top flight.  This article shows statistics and details of all matches played by the club during the season.

David Nicholls (footballer): David Clarkson Nicholls (born 5 April 1972 in Bellshill) is a Scottish association football player, who played for Clydebank, Falkirk and Dunfermline Athletic (where he scored once against St Johnstone) amongst other clubs.  Nicholls played for Gretna in the 2006 Scottish Cup Final and helped them secure three successive promotions.

A.F.C. Sudbury: A.F.C. Sudbury is a semi-professional football club based in Sudbury, Suffolk, England.  The club was formed in 1999 by the merger of Sudbury Town and Sudbury Wanderers, the process giving rise to the name Amalgamated Football Club Sudbury.  and went on to win the Eastern Counties League Premier Division five seasons in a row as well as reaching the final of the FA Vase in three successive seasons, records for both competitions.  They are currently members of the Isthmian League North Division and play at the King's Marsh Stadium in the Ballingdon-Brundon area of Sudbury.

Highfield R.F.C.: Highfield Rugby Football Club is a rugby union club based in Cork, Ireland, playing in Division 2A of the All-Ireland League.  The club was founded in 1930 and was elevated to senior status in the province of Munster in 1953.  Before moving to its present grounds, at Woodleigh Park, it was based in fields off Magazine Road, between Highfield Avenue and Highfield West.  Hence the name...Although the current ground is also located near a park called Highfield Lawn.  They are currently playing in Division 2A of the All-Ireland League after two successive promotions.  Highfield's Youth Section has an enviable record of success over the last 34 or so years.

Ivybridge RFC: Ivybridge Rugby Club is an English rugby union club based in Ivybridge, Devon.  The first XV team currently play in South West Premier, having reached the national levels of the sport for the first time in 2015 after two successive promotions, both via play-offs.

List of Oxford United F.C. seasons: Oxford United F.C. is an English association football club originally formed in 1893 under the name Headington United.  The club adopted its present name in 1960, and played in local Oxfordshire leagues until being elected into the Southern League in 1949.  It was at this time the club turned professional.  Oxford was elected into the Football League in 1962, replacing Accrington Stanley.  Promotion to the Third Division in 1965, the club were promoted again 3 years later and enjoyed an eight-year spell in the Football League Second Division, before being relegated.  "The U's" reached the top tier of English football in 1985 after successive promotions, where they stayed for 3 years.  During this time United won their only piece of major silverware, the 1986 Football League Cup.

F.C. United of Manchester: F.C. United of Manchester is a semi-professional football club based in Moston, Manchester, England.  The club competes in the National League North , the sixth tier of the English football league system, and play their home matches at Broadhurst Park.

Sutton Athletic F.C.: Sutton Athletic F.C. is an English football club in Sutton-at-Hone, near Dartford in Kent.  The club plays in the Southern Counties East League Division One .  Sutton Athletic has been playing football at a county level in Kent since the 1960s, winning leagues and cups in the Kent County Football League system, particularly during the late 1960s and early 1970s, when they won three successive league-and-cup doubles.  Sutton were accepted into the newly formed Kent Invicta Football league for the inaugural 2011–12 season.  The club is affiliated to the Kent County Football Association

Kings Langley F.C.: Kings Langley Football Club are a semi-professional association football club in the village and civil parish of Kings Langley, Hertfordshire, England.  The club have spent the majority of their history in the Hertfordshire County League, they joined the Spartan South Midlands Football League in 2001, winning the Premier Division in the 2015-16 season and are currently members of the Southern League Premier Division - the seventh tier of the English football league system, following a third consecutive promotion in 2016 when they became champions of the Southern League Division One South.  In doing so, Kings Langley join Truro F.C., Chester F.C., F.C. United of Manchester and Gretna F.C. as the only clubs in the United Kingdom with three or more successive promotions.  They are also unofficially the highest-ranked village football club in England.

Kotoku Royals F.C.: Kotoku Royals F.C. (previously known as Kotoku Royals Academy) is a professional football team from Akim Oda, Eastern Region in Ghana, currently playing in Ghana Division One.  Founded in 2003 and given permission to play professional matches in 2005, the club made successive promotions through the Ghana League system to their current place in Division One.

Question: Kings Langley F.C. has three successive promotions, similar to the football club based in what Manchester town?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "club_name": {
      "type": "string",
      "description": "The name of the football club that matches the promotion criteria."
    },
    "club_location_city": {
      "type": "string",
      "description": "The city where the club is based."
    },
    "club_location_town": {
      "type": "string",
      "description": "The specific town within the city where the club is based."
    },
    "promotion_details": {
      "type": "object",
      "properties": {
        "number_of_successive_promotions": {
          "type": "integer",
          "description": "The number of successive promotions achieved by the club."
        },
        "comparison_club_name": {
          "type": "string",
          "description": "The name of the club used for comparison in the question."
        }
      },
      "required": [
        "number_of_successive_promotions",
        "comparison_club_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "club_name",
    "club_location_city",
    "club_location_town",
    "promotion_details"
  ],
  "additionalProperties": false
}
