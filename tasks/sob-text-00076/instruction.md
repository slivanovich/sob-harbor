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
Kane County Dawgs: The Kane County Dawgs were a professional indoor American football team based in Kane County, Illinois.  The team joined the Continental Indoor Football League in 2013 as an expansion team.  The Dawgs were one of three indoor football teams based in the Chicago metropolitan area.  The Chicago Rush of the Arena Football League are based in Rosemont, and the Chicago Slaughter of the Indoor Football League are based in Hoffman Estates.  The CIFL has had the Chicago Pythons (in 2012) which replaced the Chicago Knights (in 2011), formerly the Chicago Cardinals (in 2010), as the Illinois-based CIFL team, which replaced the Slaughter after they left for the Indoor Football League after a dispute with CIFL management.  The Owners of the Dawgs are Mike Dortch and Macey Brooks.  The Dawgs played their home games at the Seven Bridges Ice Arena in 2013.

Chicago Pythons: The Chicago Pythons were a professional indoor football team based in Homer Glen, Illinois.  The team was a member of the Continental Indoor Football League (CIFL).  The Pythons joined the CIFL in 2012 as an expansion team under the name "Chicago Vipers".  They changed their name to the "Chicago Pythons" four weeks into the season.  The Pythons were the third indoor football team based in the Chicago area.  The Chicago Rush of the Arena Football League were based in Rosemont, and the Chicago Slaughter of the Indoor Football League are based in Hoffman Estates.  The Pythons replaced the Chicago Knights, formerly the Chicago Cardinals, as the Illinois-based CIFL team, which replaced the Slaughter after they left for the Indoor Football League after a dispute with CIFL management.  The Owner of the Pythons was Michael Duran.  The Pythons were supposed to play their home games at The Megaplex in Homer Glen, Illinois, but the team never hosted a home game.

List of Fulham F.C. players (1–24 appearances): Fulham Football Club is an English professional football team based in Fulham in the London Borough of Hammersmith and Fulham.  The club was formed in West Kensington in 1879 as Fulham St Andrew's Church Sunday School F.C., before shortening it to Fulham F.C. in 1888.  They initially played at Fulham Fields before a move to Craven Cottage in 1896.  They played their first match as a professional football club in December 1898 and made their FA Cup debut in the 1902–1903 season.  The club also competed in the Southern Football League until 1907, when they were accepted into the Football League Second Division.  Having spent much of their history outside the top division, the team gained promotion to the Premier League in 2001.  They have since spent more than ten years in the top flight and reached the final of the UEFA Europa League in 2010.  In 2014 they were relegated to the Football League Championship.

Austin Turfcats: The Austin Turfcats were a professional indoor football team based in Austin, Texas.  The Turfcats were a member of the Indoor Football League (IFL) during the 2010 season, after being a charter member of the Southern Indoor Football League (SIFL) during their inaugural 2009 season.  The Turfcats played their home games at Luedecke Arena at the Travis County Exposition Center.  This was Austin's fourth attempt at an indoor football team; the prior three were the Indoor Professional Football League's Texas Terminators (1999), the National Indoor Football League's Austin Knights/Rockers (2002–2003), and the Arena Football League (later af2's) Austin Wranglers (2004–2008) (the former two of which played in Luedecke Arena before the Turfcats).

Maryland Maniacs: The Maryland Maniacs were a professional Indoor Football team based in College Park, Maryland, and a member of the Indoor Football League.  The team began play in 2009 as an expansion team in the Indoor Football League.  The Maniacs were the second indoor football team to be based in Maryland, following the Chesapeake Tide of the Continental Indoor Football League, who played in the same market.  The owner of the Maniacs was Messay Hailermariam.  The Maniacs played its home games at Cole Field House.  Inaugural season home games were held at The Show Place Arena.  They left the Indoor Football League in 2011, and have been rumored to be in discussion with American Indoor Football about joining their league.

Detroit Thunder: The Detroit Thunder was a professional indoor football team based in Fraser, Michigan.  The team was a member of the Continental Indoor Football League.  The Thunder were the third indoor football team to have called the Motor City home, following two Arena Football League teams: the four-time ArenaBowl champion Detroit Drive (1988 Arena Football League season-1993) and the Detroit Fury (2001 Arena Football League season-2004 Arena Football League season).  In addition, a team called the Motor City Reapers was proposed for the 2007 CIFL season, but the team folded before ever playing a single game.  The Thunder were owned by Terrence and Lawrence Foster.

Crystal Palace F.C.: Crystal Palace Football Club is a professional football club based in Selhurst, London, that plays in the Premier League, the top tier of English football.

Dayton Sharks: The Dayton Sharks were a professional indoor football team based in Dayton, Ohio.  The team was a member of the Continental Indoor Football League (CIFL).  The franchise started as an expansion team in the CIFL during the 2013 season.  The Sharks were the fifth indoor football team to be based in Dayton, the first being the Dayton Skyhawks of the original Indoor Football League.  The Skyhawks were followed by the Dayton Warbirds, who later became the Dayton Bulldogs, of the National Indoor Football League the third being the Cincinnati Marshals who played their 2007 season in Dayton and the fourth being the Dayton Silverbacks who played from 2006 to 2012.  The Owner of the Sharks was CA Sports Entertainment LLC.  The Sharks played their home games at Hara Arena in nearby Trotwood, Ohio.

Alan Deakin: Alan Deakin (born 27 November 1941 in Balsall Heath, Birmingham) was an English footballer during the 1960s.  He was the captain of Aston Villa and also played for Walsall.  He is the younger brother of Mike Deakin who also played in the Football League, most notably for Crystal Palace.

Knoxville NightHawks: The Knoxville NightHawks were a professional indoor football team based in Knoxville, Tennessee.  The team was a member of the Professional Indoor Football League (PIFL).  The NightHawks joined the PIFL in 2012 as an expansion team.  The NightHawks were the second indoor/arena football team based in Knoxville, following the Tennessee ThunderCats which played in the Indoor Professional Football League for the 2001 season before joining the National Indoor Football League where they played the 2002 and 2003 seasons (the latter of which they played as the Tennessee Riverhawks) before moving to Greenville, South Carolina.  The Owner of the NightHawks was Southern Sports Entertainment, LLC.  The NightHawks played their home games at the James White Civic Coliseum in Knoxville, Tennessee.

Question: Mike Deakin played in the football league for a team based in which part of London ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the football player."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the player played for."
    },
    "team_location": {
      "type": "string",
      "description": "The specific part of London where the team is based."
    },
    "city": {
      "type": "string",
      "description": "The city where the team is located."
    }
  },
  "required": [
    "player_name",
    "team_name",
    "team_location",
    "city"
  ],
  "additionalProperties": false
}
