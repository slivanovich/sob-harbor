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
Manchester United F.C.: Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England, that competes in the Premier League, the top flight of English football.  Nicknamed "the Red Devils", the club was founded as Newton Heath LYR Football Club in 1878, changed its name to Manchester United in 1902 and moved to its current stadium, Old Trafford, in 1910.

List of Manchester United F.C. managers: Manchester United Football Club is an English professional football club based in Old Trafford, Greater Manchester.  The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup.  The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.

Old Trafford Cricket Ground: Old Trafford, known for sponsorship reasons as Emirates Old Trafford, is a cricket ground in Old Trafford, Greater Manchester, England.  It opened in 1857 as the home of Manchester Cricket Club and has been the home of Lancashire County Cricket Club since 1864.

Old Trafford: Old Trafford is a football stadium in Old Trafford, Greater Manchester, England, and the home of Manchester United.  With a capacity of 75,643, it is the largest club football stadium in the United Kingdom, the second-largest football stadium, and the eleventh-largest in Europe.  It is about 0.5 mi from Old Trafford Cricket Ground and the adjacent tram stop.

History of Manchester United F.C. (1945–69): Manchester United Football Club is an English professional football club, based in Old Trafford, Greater Manchester, that plays in the Premier League.  Founded as Newton Heath LYR Football Club in 1878, and changed its name to Manchester United in 1902.

Old Trafford tram stop: Old Trafford is a tram stop on the Metrolink light rail system in Old Trafford, Greater Manchester, England.  Before 1991, it was a railway station called Warwick Road; it reopened as a tram stop on 15 June 1992 with its current name.  The stop is regularly used by crowds going to Old Trafford Football Ground and Old Trafford Cricket Ground which are both nearby.

Saidy Janko: Saidy Janko (born 22 October 1995) is a Swiss footballer who plays for French club Saint-Étienne.  Although he is primarily recognised as a right-back, he is equally capable of playing on the right wing.  Born in Zürich to a Gambian father and a Swiss/Italian mother, Janko began his career with FC Zürich before signing for Manchester United in 2013.  After a loan spell with Bolton Wanderers, Janko moved to Scottish club Celtic in 2015.  He spent the 2016–17 season on loan to Barnsley before moving to Saint-Étienne permanently in July 2017.  He has played international football for Switzerland up to under-21 level.

List of Manchester United F.C. seasons: Manchester United Football Club is an English professional football club based in Old Trafford, Greater Manchester.  The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup.  The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.

Sir Matt Busby Way: Sir Matt Busby Way is a road in Old Trafford, Greater Manchester, England.  It is the location of Manchester United's Old Trafford football ground.  Formerly known as Warwick Road North, it was renamed in honour of the legendary Manchester United manager, Sir Matt Busby, in 1993.  Busby died less than a year later on 20 January 1994, aged 84.  A bronze statue of Sir Matt Busby, erected in 1996, stands on the exterior of the East Stand of the Old Trafford stadium, overlooking Sir Matt Busby Way.

List of Manchester United F.C. players: Manchester United Football Club is an English professional football club based in Old Trafford, Greater Manchester.  The club was formed in Newton Heath in 1878 as Newton Heath LYR F.C., and played their first competitive match in October 1886, when they entered the First Round of the 1886–87 FA Cup.  The club was renamed Manchester United F.C. in 1902, and moved to Old Trafford in 1910.  Since playing their first competitive match, exactly 900 players have made a competitive first-team appearance for the club, of whom 205 players have made at least 100 appearances (including substitute appearances).

Question: What club did  a Swiss footballer primarily recognised as a right-back who signed for a professional football club in 2013 based in Old Trafford, Greater Manchester, England ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "footballer_name": {
      "type": "string",
      "description": "The name of the Swiss footballer identified in the question."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the footballer."
    },
    "primary_position": {
      "type": "string",
      "description": "The primary playing position of the footballer."
    },
    "club_signed_in_2013": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the club the footballer signed for in 2013."
        },
        "location": {
          "type": "string",
          "description": "The location of the club signed in 2013."
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "current_or_most_recent_club": {
      "type": "string",
      "description": "The club the footballer currently plays for or most recently played for permanently, as per the context."
    }
  },
  "required": [
    "footballer_name",
    "nationality",
    "primary_position",
    "club_signed_in_2013",
    "current_or_most_recent_club"
  ],
  "additionalProperties": false
}
