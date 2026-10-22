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
2002–03 Manchester City F.C. season: The 2002–03 season was Manchester City Football Club's first season back playing in the Premier League again after having been relegated from it at the end of the 2000–01 season.  This was the club's sixth season playing in the Premier League since its initial formation as the top tier of English football ten years earlier, with Manchester City as one of its original 22 founding member clubs.  Overall, this was Manchester City's 111th season playing in any division of English football, most of which have been spent in the top flight.

List of Manchester City F.C. players: Manchester City Football Club, then known as Ardwick, first entered the Football League in the 1892–83 season.  Since that time the club's first team has competed in numerous nationally and internationally organised competitions, and all players who have played in 100 or more such matches are listed below, which encompasses all players who have been inducted into the Manchester City Hall of Fame.  Also included are all winners of the "Player of the Year" award which has been awarded annually since 1967 by the Manchester City Official Supporters Club based on a ballot of the supporters.

1997–98 Manchester City F.C. season: The 1997–98 season was Manchester City's second in the First Division following relegation from the Premier League in 1995–96.  The 1996–97 season had been a turbulent one; Five different managers took charge of the team over the course of the season (three permanent appointments and two caretakers), including Steve Coppell, who resigned after just 32 days as manager.  Frank Clark became manager in December 1996 and was in charge for the start of the 1997-98 season.

History of Manchester City F.C. (2001–present): This page chronicles the history of English football team Manchester City Football Club in further detail from 2001 to the present day.  See "History of Manchester City F.C." for a history overview of Manchester City.

Steve Coppell: Stephen James Coppell (born 9 July 1955) is an English football coach and former player, who is the head coach of the Jamshedpur FC in the Indian Super League.

Blue Moon Rising (film): Blue Moon Rising is a British sport documentary film released on 17 September 2010.  The film title is a play on words referring to Manchester City's fan anthem, "Blue Moon" and chronicles the fortunes of Manchester City Football Club through the 2009-2010 football season with insight from Manchester City supporters.  Shot and produced by Endemol in conjunction with the club, and features exclusive interviews with staff, players, board members and fans throughout the season.

Manchester City F.C. ownership and finances: The Ownership of Manchester City Football Club traces back to 1894, when "Ardwick A.F.C." dissolved and were reformed as "Manchester City Football Club Ltd." Over recent years, the ownership and finances of Manchester City Football Club have been tumultuous with various owners of contrasting fortunes much in line with their inconsistent trend on the pitch and the club's hierarchy maintain the club is in a period of ""significant transformation"".

2009–10 Manchester City F.C. season: The 2009–10 season is Manchester City Football Club's eighth consecutive season playing in the Premier League, the top division of English football, and its thirteenth season since the Premier League was first created with Manchester City as one of the its original 22 founding member clubs.  Overall, it is the team's 118th season playing in a division of English football, most of which have been spent in the top flight.  The club started the season under the management of Mark Hughes who was controversially sacked in mid-December after the team notched up seven consecutive draws in the Premier League.  He was replaced by the Italian manager Roberto Mancini.

Manchester City F.C.: Manchester City Football Club is a football club in Manchester, England.  Founded in 1880 as St. Mark's (West Gorton), they became Ardwick Association Football Club in 1887 and Manchester City in 1894.  The club moved to the City of Manchester Stadium in 2003, having played at Maine Road since 1923.

Manchester City F.C. league record by opponent: Manchester City Football Club is an English association football club based in Manchester, which competes in the Premier League.  Founded as West Gorton (St Marks) in 1880, the club after several changes of identity adopted the name 'Manchester City' in 1894.  During the 1891–92 season, Manchester City joined the Football Alliance.  The team was elected to The Football League in 1892, where the club remained until 1992, when the League's First Division was replaced as the top level of English football by the Premier League.

Question: After how many days did the manager born in July of 1955 resign from the Manchester City Football Club?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "manager_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the manager."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the manager."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "club_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "event_type": {
      "type": "string",
      "description": "The type of event related to the manager's tenure."
    },
    "duration_in_days": {
      "type": "integer",
      "description": "The number of days the manager was in charge before the event."
    }
  },
  "required": [
    "manager_details",
    "club_name",
    "event_type",
    "duration_in_days"
  ],
  "additionalProperties": false
}
