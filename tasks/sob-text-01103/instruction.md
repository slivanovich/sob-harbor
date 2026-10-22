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
Marc Dos Santos: Marc Dos Santos (born May 26, 1977) is a Canadian soccer manager with experience in the United Soccer League, North American Soccer League, and Major League Soccer.  He currently is the manager of the San Francisco Deltas of the North American Soccer League, beginning play in the 2017 season.  Most recently, he was the manager of the Swope Park Rangers of the United Soccer League, an affiliate of Sporting Kansas City of Major League Soccer.  The North American Soccer League Coach of the Year in 2015, Dos Santos led the Ottawa Fury FC to the NASL Championship Final after a first-place finish in the Fall Season.  Previously, he focused on youth initiatives in Brazil with FC Primeira Camisa (U-20's) and SE Palmeiras (U-15's), culminating with a Copa do Brasil Sub-15 championship and a technical director position with Desportivo Brasil.  The Montreal native was first hired by the Montreal Impact in January 2007 to lead the club's reserve team, Trois-Rivieres Attak FC, in the Canadian Soccer League.  After leading the squad to titles in their initial two seasons – first as 2007 Open Canada Cup champions, then as 2008 CSL National Division champions – Dos Santos was added to the Impact's technical staff as an assistant coach in June 2008 and became head coach in May 2009.  During his tenure, the Impact won the inaugural Canadian Championship in 2008 to claim the Voyageurs Cup and a berth in the 2008-09 CONCACAF Champions League.  Dos Santos then led Montreal through three different leagues in consecutive campaigns, winning the USL First Division title in 2009 before transitioning into USSF Division 2 in 2010 and the North American Soccer League in 2011.

Edson Buddle: Edson Michael Buddle (born May 21, 1981) is an American soccer player who last played for LA Galaxy in Major League Soccer.

John Doyle (soccer): John Joseph Doyle (born March 16, 1966) is a retired American soccer player who played professionally in both Europe and the United States including the Western Soccer League, American Professional Soccer League and Major League Soccer.  He was the 1995 A-League Defender of the Year and the 1996 MLS Defender of the Year.  He also earned fifty-three caps with the U.S. national team between 1987 and 1994 including two games at the 1990 FIFA World Cup.  He was a member of the U.S. team at the 1988 Summer Olympics and was most recently the general manager of the San Jose Earthquakes of Major League Soccer before being fired on August 29, 2016.

Real Salt Lake: Real Salt Lake (RSL) is an American professional soccer franchise that competes as a member club of Major League Soccer (MLS)' Western Conference.  RSL began play in 2005 as an expansion team of the league.  The club was founded in 2004 when the club's first owner and founder was awarded an expansion berth in Major League Soccer.

Zoran Savic (soccer): Zoran Savic (] ) is a retired Yugoslavian soccer player who played at the forward position.  He played professionally in the first Major Indoor Soccer League.  He later played in the second and third American Soccer League then the American Professional Soccer League and the American Indoor Soccer Association.  He is a professional coach and is currently an assistant coach at Sporting Kansas City of Major League Soccer.

LA Galaxy: The LA Galaxy, also known as the Los Angeles Galaxy, is an American professional soccer franchise based in the Los Angeles suburb of Carson, California, that competes in Major League Soccer (MLS), as a member of the Western Conference of the league.  The club began play in 1996 as a charter team in the league.

Omid Namazi: Omid Namazi (Persian: امید نمازی‎ ‎ ) is a retired Iranian-American soccer defender and currently head coach of the United States men's national under-18 soccer team.  Namazi played professionally in the American Soccer League, American Professional Soccer League, Major League Soccer, USISL and National Professional Soccer League where he was the 2001 Defender of the Year.  He is a two-time Coach of the Year in the Major Indoor Soccer League and coached in the Women's United Soccer Association.  As assistant coach of Iran, he led the team to qualification to the 2014 FIFA World Cup and the 2015 AFC Asian Cup.

Seattle Sounders (1994–2008): Seattle Sounders was an American professional soccer team founded in 1994 as a member of the American Professional Soccer League.  In 1997, the team became a member of the USL First Division, the second tier of the United States soccer pyramid, until 2008, after which the majority of the team's staff and resources were directed to the new Major League Soccer franchise, Seattle Sounders FC.

Peter Bridgwater: Peter Bridgwater (7 March 1935 – 21 June 2005) was the first president of the San Jose Clash—later known as the San Jose Earthquakes—Major League Soccer franchise.  Prior to arriving in the Bay Area, Bridgwater was an executive of the Vancouver Whitecaps franchise in the North American Soccer League.  He had been involved with professional soccer in San Jose since 1984, when he was named general manager of the NASL's San Jose Earthquakes.  Bridgwater purchased the Earthquakes later, but the NASL ceased operations in 1985.  After the NASL went under, Bridgwater became a founder of the Western Soccer Alliance, which later became the USL First Division. " Soccer America" called him "one of the men most responsible for keeping professional outdoor soccer alive [in the U.S.] after the collapse of the North American Soccer League".  Bridgwater was also a venue director for the 1994 FIFA World Cup at Stanford Stadium in Palo Alto, California.  Two years after the World Cup, the MLS was launched; Bridgwater served as the Clash's first president.  He remained the general manager through the 1998 season, and played a role in having San Jose host matches for the 1999 FIFA Women's World Cup.

Oscar Draguicevich: Oscar Draguicevich (born August 19, 1969, in Pflugerville, Texas) is a retired American soccer player who spent three seasons in Major League Soccer.  He also played in the American Professional Soccer League, Continental Indoor Soccer League, National Professional Soccer League and the German third division.  He was a member of the United States U-20 national team at the 1989 FIFA World Youth Championship.

Question: Which American professional soccer franchise in California that competes in Major League Soccer, for which American soccer player Edson Buddle played?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "franchise_name": {
      "type": "string",
      "description": "The name of the American professional soccer franchise."
    },
    "league": {
      "type": "string",
      "description": "The league in which the franchise competes."
    },
    "location_state": {
      "type": "string",
      "description": "The state where the franchise is based."
    },
    "player_name": {
      "type": "string",
      "description": "The name of the player who played for this franchise."
    }
  },
  "required": [
    "franchise_name",
    "league",
    "location_state",
    "player_name"
  ],
  "additionalProperties": false
}
