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
Jed Hoyer: Jed D. Hoyer (born December 7, 1973), is the executive vice-president and general manager of the Chicago Cubs.  He has been the general manager of the San Diego Padres and the assistant general manager of the Boston Red Sox.  He joined the Red Sox in 2002, after the ownership of John W. Henry, Tom Werner, and Larry Lucchino took over the team from John Harrington.  He worked under the title of assistant to the general manager until December 2005.  He then was given the title of assistant general manager.  Hoyer briefly served as co-general manager of the Red Sox from December 12, 2005 to January 19, 2006 and then returning to his previous job of assistant general manager.  In November 2003, he accompanied general manager Theo Epstein to Arizona to persuade pitcher Curt Schilling to accept a trade to the Red Sox, spending Thanksgiving at Schilling's home in what was eventually a successful effort.

Rich Cho: Richard Cho (born August 10, 1965), more commonly known by his nickname "Trader Cho" is a Burmese American basketball executive, currently serving as the general manager of the Charlotte Hornets of the National Basketball Association.  Prior to the Hornets, Cho was the general manager of the Portland Trail Blazers and the assistant general manager of the Oklahoma City Thunder.  Cho is the first Asian American general manager in NBA history.

Djuan Rivers: Djuan Rivers is the Vice President of Disney's Animal Kingdom at Walt Disney World.  He previously served as Vice President for Hotels and Business Solutions at Disneyland Paris after having been General Manager of the Disney Aulani Resort & Spa in Hawaii.

Jim Lentz: Jim Lentz is the chief executive officer for Toyota North America; president and chief operating officer of Toyota Motor North America, Inc. (TMA); and a senior managing officer of the parent company Toyota Motor Corporation (TMC) which is located in Japan.  In that role Lentz manages all of Toyota’s North American affiliate companies which include TMA, Toyota Motor Sales, U.S.A., Inc. (TMS), and Toyota Motor Engineering & Manufacturing, North America, Inc. (TEMA), which includes responsibilities for Toyota Motor Manufacturing Canada Inc. (TMMC), and oversight for Toyota Canada, Inc. (TCI).  Lentz also serves as the chairman of the North American Executive Committee.  This is composed of the top leaders from the affiliate companies.  Most recently Lentz was the president and chief executive officer of TMS and senior vice president of TMA and served in a global advisory capacity as the managing officer for TMC.  Before that he served as president and chief operating officer and executive vice president of TMS.  Lentz previously held several executive positions including Toyota division group vice president and general manager where he oversaw all sales, logistics and marketing activities for Toyota and Scion regional sales offices and distributors.  He also served as the group vice president of marketing for the Toyota division and vice president of Scion, and was responsible for the initial launch of a new line of vehicles.  Lentz spent several years in the field as vice president and general manager of the Los Angeles region and before that general manager of the San Francisco region.  Prior to his role as general manager Lentz was vice president of marketing services for CAT in Maryland.  He has also held several other TMS positions, including field training manager, sales administration manager and truck sales team member.  Lentz joined Toyota in 1982 as the merchandising manager for its Portland, Oregon region where he later became the distribution manager and field operations manager.  He serves as chairman on the board of directors of The Global Automakers and is also a member of the executive advisory board for Daniels College of Business at the University of Denver (DU), his alma mater.  He was named “Marketer of the Year” by Advertising Age in 2006, an Automotive News “All Star” in 2007 and honored at Industry Leader of the year.

Ted Thompson: Ted Thompson (born January 17, 1953) is the current general manager of the National Football League's Green Bay Packers.  Thompson was named to the post on January 14, 2005, by former Packers president and CEO Bob Harlan.  Thompson took over the general manager duties from Mike Sherman, who had been serving as both head coach and general manager.  Prior to becoming the Packers' general manager, Thompson served with the Seattle Seahawks as their vice president of operations from 2000 to 2004.  Thompson had previously worked for the Packers organization from 1992 to 1999, serving as their assistant director of pro personnel in 1992, their director of pro personnel from 1993 to 1997, and their director of player personnel from 1997 to 1999.  Thompson also had a 10-year playing career in the NFL as a linebacker and special teams player with the Houston Oilers from 1975 to 1984.

Randy Sexton: Randy Sexton (born July 24, 1959) is a Canadian ice hockey executive, businessman and former athlete.  He is currently the assistant general manager for the Buffalo Sabres of the National Hockey League (NHL) and general manager of the Rochester Americans of the American Hockey League.  He most recently was the director or amateur scouting for the Pittsburgh Penguins.  Prior to that, he was general manager of the Florida Panthers of the NHL.  He was one of the founders of the Ottawa Senators NHL club in Ottawa, Ontario.  He later became the Senators' second general manager.

Maurice Filion: Maurice Filion (February 12, 1932 – July 28, 2017) was a Canadian ice hockey coach and general manager.  He served as general manager for the Quebec Nordiques throughout most of their time in the World Hockey Association (WHA), and briefly served as coach on three separate occasions.  His tenure as general manager ended in 1988 when he was promoted to an executive role and was replaced by Martin Madden, but served as interim general manager for a few months in 1990 when Madden was fired.

Jeff Gorton: Jeff Gorton is the current General Manager of the New York Rangers of the National Hockey League (NHL).  Previously, he served four seasons as Assistant General Manager of the Rangers.  Prior to becoming assistant general manager, Gorton spent three seasons with the Rangers as Assistant Director of Player Personnel after serving one season as a professional scout.  Gorton was the Interim General Manager of the Boston Bruins during the 2005–06 season replacing Mike O'Connell who was fired on March 25, 2006.

Al Coates (ice hockey): Al Coates (born December 3, 1945) is an executive in the National Hockey League who most recently served as the Executive Director of 2012 IIHF World Junior Championship.  Coates is a former General Manager of the Calgary Flames, a post he held from November 1995 until the end of the 1999–2000 NHL season.  He then was named the Vice President of Hartford Sports and Entertainment for the New York Rangers from 2000–03.  He later served as interim General Manager of the Ducks in 2004–05 before becoming the Senior Advisor to the General Manager.  He then served as the Director of Player Personnel for the Toronto Maple Leafs in 2008.  He won the Stanley Cup in 1989 with Calgary as Assistant to the President, and in 2007 with Anaheim as Senior Advisor to the General Manager.

Aulani: Aulani, a Disney Resort & Spa is a beachside hotel, resort and vacation destination offering complimentary children's activities and programs at the Ko Olina Resort & Marina in Kapolei on the Hawaiian island of Oahu.  Part of the Disney Vacation Club, it is the third Disney Vacation Club Resort located outside of a Disney theme park property.  The resort opened on August 29, 2011.

Question: When did the resort at which Djuan Rivers served as a General Manager open? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "resort_name": {
      "type": "string",
      "description": "The name of the resort."
    },
    "general_manager_name": {
      "type": "string",
      "description": "The name of the person who served as General Manager at the resort."
    },
    "opening_date": {
      "type": "string",
      "description": "The date the resort opened."
    },
    "resort_location": {
      "type": "string",
      "description": "The location of the resort."
    }
  },
  "required": [
    "resort_name",
    "general_manager_name",
    "opening_date",
    "resort_location"
  ],
  "additionalProperties": false
}
