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
Northern Demons SC: Virtus Soccer Club, playing in modern times as the Northern Demons is a soccer club from Port Pirie, South Australia.  Northern Demons play in the Football Federation of South Australia (FFSA) State League.  Their home ground is Byrne Park, situated on Magor Road, Port Pirie.  Together with their three senior teams (Seniors, Reserves and Under 18s), the club has an Under 12,14, and 15 team competing in the Football Federation of South Australia Junior Premier League.  Their cross-town rivals are the Savoy Soccer Club, formerly known as Port Pirie City, who play in the South Australian Amateur Soccer League (SAASL).

Columbus Crew SC: Columbus Crew Soccer Club is an American professional soccer club based in Columbus, Ohio.  The Crew competes in Major League Soccer (MLS) as a member club of the league's Eastern Conference.  The Crew began play in 1996 as one of the ten charter clubs of the league.  The team is owned by Anthony Precourt and Precourt Sports Ventures LLC.  Precourt became the second owner in the history of the club on July 30, 2013.  The club's head coach is Gregg Berhalter, a former player of the United States men's national soccer team.

Donnay (sports): Donnay Sports is a sporting goods brand owned by the British retailer Sports Direct International.  The company was founded in 1913 by Emile Donnay and was based in Couvin, Belgium.  Donnay manufactured wooden tennis rackets from 1934, and by the 1970s was the largest manufacturer of tennis rackets in the world.  However, the company failed to adapt to the new market for graphite rackets, and entered administration in 1988.  After a succession of owners, the brand was eventually sold to Sports Direct, who continue to license the use of the brand worldwide.

Sports Direct: Sports Direct International plc is a British retailing group.  Established in 1982 by Mike Ashley, the company is the United Kingdom's largest sports-goods retailer and operates roughly 670 stores worldwide.  The company owns a large number of sporting brands and trades predominantly under the SportsDirect.com brand.  Other retailers owned by the company include USC and Lillywhites.  The company operates under low margins.

Mike Ashley (businessman): Michael James Wallace "Mike" Ashley (born 9 September 1964) is an English billionaire retail entrepreneur in the sporting goods market.  He is also the owner of Newcastle United after paying around £135 million to buy the club.

Bardon Latrobe FC: Bardon Latrobe Football Club, based at Bardon in Brisbane, Queensland, is one of the larger soccer clubs in Brisbane, with over 400 registered players.  This iteration of the club was formed with the merging in 1970 of the Latrobe Soccer Club and the Bardon Soccer Football Club, two of the oldest clubs in the Brisbane football competition (the two clubs had previously merged for the 1941 season, as 'Latrobe-Bardon Soccer Club').

Cairnlea FC: Cairnlea FC is a football (soccer) club based in Cairnlea, Victoria, Australia.  The club was formerly known as the Albion Rovers Soccer Club which was formed by the amalgamation of Royal Park Soccer Club and Albion Rovers Soccer Club in 1982.  Since this time, the club has enjoyed success playing at the highest levels in Victorian football including finals campaigns in the Victorian Premier League (VPL), a host of Victorian State League titles and many League Cups.  A combined five league titles between the Men and Women's team have given the club the most successful record of any Turkish backed club in Australian history.  Currently the club's Senior Men team play in the Victorian State League Division 2 N/W competition.

Morley-Windmills SC: Morley-Windmills Soccer Club is an Australian semi-professional soccer club based in Morley, Perth, Western Australia.  The club was founded 1973 from a merger of Windmills Soccer Club and Morley Soccer Club.  The club currently (2016) competes in the Football West State League Division 2.

Houston Dutch Lions: The Dutch Lions FC is an American soccer club based in The Woodlands, Texas.  Founded in 2011, the team plays in the National Premier Soccer League, the fourth tier of the American soccer pyramid, playing home games at the team owned Houston Dutch Lions FC Soccer Facility located in Conroe, Texas.  The Dutch Lions FC is a soccer club that operates all months of the year, the club partners with the Conroe Youth Soccer League (member of STYSA) and plays a fall season, spring season and summer season (Super Summer League).  The club also hosts soccer camps such as a Thanksgiving break camp, Spring break camp and camps during the summer months.  Since September, 2015 there is pick up soccer for Men and Women on Tuesday and Thursday evening making the club open to all ages and becoming a big factor in The Woodlands / Conroe community.

Sydney Olympic FC: Sydney Olympic Football Club is an Australian semi-professional soccer club, based in Belmore, Sydney, New South Wales, that plays in the National Premier Leagues NSW.  The Club was founded as Pan-Hellenic Soccer Club in 1957 by Greek immigrants.  In 1977, the Club changed its name to Sydney Olympic and became a founding member of the Phillips Soccer League, later named the National Soccer League (NSL), the inaugural national football league of Australia, remaining a member of the competition until its demise in 2004.

Question: Sports Direct is owned by an English billionaire that owns which football/soccer club?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "owner_name": {
      "type": "string",
      "description": "The name of the English billionaire who owns Sports Direct."
    },
    "owner_nationality": {
      "type": "string",
      "description": "The nationality of the owner."
    },
    "owned_football_club": {
      "type": "string",
      "description": "The name of the football/soccer club owned by the billionaire."
    },
    "club_acquisition_cost_gbp": {
      "type": "integer",
      "description": "The cost in GBP to acquire the football club."
    }
  },
  "required": [
    "owner_name",
    "owner_nationality",
    "owned_football_club",
    "club_acquisition_cost_gbp"
  ],
  "additionalProperties": false
}
