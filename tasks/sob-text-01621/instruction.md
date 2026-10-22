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
Carleton Ravens women's ice hockey: The Carleton Ravens are a collegiate women's ice hockey team based out of Ottawa, Ontario, Canada.  Competing as the women's ice hockey team of Carleton University, the Ravens play in the Quebec Student Sports Federation (RSEQ), as part of the Canadian Interuniversity Sport women's ice hockey championship.  The team plays its home games at the Carleton Ice House, typically on Saturday and Sunday afternoons.

China Dragon: The China Dragon () was a professional ice hockey team which played its home games in three different cities in China, including Harbin, Qiqihar, and Shanghai.  The team was a member of Asia League Ice Hockey between 2007 and 2017.  The team was formed in 1954 as two different clubs, Harbin and Qiqihar, as part of the China League.  In 2004, the clubs joined Asia League Ice Hockey and in 2007 they merged into a single club, China Sharks, backed by the National Hockey League's San Jose Sharks for financial reasons.  The team was renamed the China Dragon in 2009 when San Jose pulled out.  The team was dissolved following the 2016–17 Asia League Ice Hockey season.

Chuck Weber (ice hockey): Chuck Weber (born 1973) is an American ice hockey coach.  He is currently the head coach of the Atlanta Gladiators in the ECHL.

Truva Paten Spor Kulübü: Truva Paten Spor Kulübü, aka Ankara Truva, is a Turkish ice hockey club based in Ankara, Turkey.  Founded in 2005, the club's men's team play in the Turkish Ice Hockey Super League (TBHSL) and the women's team in the Turkish Ice Hockey Women's League (TBHBL).  The club with the colors yellow, white and black play their home matches at the GSIM Yenişehir Ice Hockey Hall.

Newcastle Northstars: The Newcastle Northstars are a semi-professional ice hockey team in the Australian Ice Hockey League (AIHL).  The team plays its home games at the Hunter Ice Skating Stadium (nicknamed 'HISS') in Warners Bay, a suburb of Lake Macquarie located about 15 kilometres south-west of Newcastle, New South Wales.  The Northstars are six times winners of the AIHL and with it, the historic Goodall Cup in 2003, 2005, 2006, 2008, 2015, and 2016.  The team is affiliated with the Newcastle Northstars Ice Hockey Club, Ice Hockey New South Wales and Ice Hockey Australia.

Angela Frautschi: Angela Frautschi (born 5 June 1987) is a Swiss female ice hockey player.  She is a member of the Switzerland women's national ice hockey team.  She played in the 2006 2010 and 2014 Winter Olympics.  She also competed for ZSC Lions Zurich in the Leistungsklasse A (the top women's ice hockey league in Switzerland).  In 2014 Frautschi accompanied the Swiss women's Ice Hockey Team to Sochi for the Winter Olympics.  Largely thought to have an outside chance at best to win a medal, Switzerland shocked Sweden in a remarkable 4-3 come from behind victory in the Bronze Medal Match, giving both Frautschi and her Swiss teammates their first ever Olympic Medal in Women's Ice Hockey History, and the countries first medal in Ice Hockey since the men won Bronze at home way back in 1948 at St. Moritz, Switzerland.

Gisele Marvin: Gisele Marie "Gigi" Marvin (born March 7, 1987) is an American ice hockey player for the Boston Pride of the National Women's Hockey League.  As a member of the United States national women's ice hockey team, Marvin won a silver medal at the 2010 Olympic Winter Games and the 2014 Winter Olympics.  Her grandfather is Cal Marvin, the coach of the 1958 United States Men's National Ice Hockey Team and the manager of the 1965 United States Men's National Ice Hockey Team, is a member of the United States Hockey Hall of Fame.  She hails from Warroad, Minnesota, in Roseau County, the same small town as 1960 gold medalists Bill and Roger Christian and 1980 gold medalist Dave Christian.

Minnesota Whitecaps: The Minnesota Whitecaps are a professional women's ice hockey team.  The team play its home games in the Minneapolis-St.  Paul, Minnesota area.  The Whitecaps do not have a home rink, and so must reach out to Minnesota youth hockey programs that can either afford to buy ice time at rinks suitable for Whitecaps home games or have had that ice time donated to them.  In exchange, the Whitecaps use part of that ice time to put on clinics for the youth players, who receive free tickets to the games and whose hockey associations receive 100 percent of the proceeds from ticket sales.  Some programs have raised more than $1,500 in a single night from the arrangement.

Aalborg Pirates: Aalborg Pirates is a professional ice hockey team (previously known as Aalborg Ishockey and AaB Ice Hockey) playing in the Danish ice hockey league, Metal Ligaen.  The ice hockey team first appeared in 1967 as AaB Ice Hockey organized under Aalborg Boldspilklub.  They play in the Danish national league and won the Danish league championship in 1981.  In 1997 AaB Ishockey merged with a smaller club, IK Aalborg.  The merged team was known as Aalborg Ishockey Klub (AIK) in the period 1997–2003, but following financial instability in the club, the professional license was transferred to Aalborg Boldspilklub ("'AaB’").  The team is located in Aalborg in the northern part of Jutland and ceased operations at the end of the 2011/12 season, where it was put up for sale.  In 2012 the team was bought by investors with the majority of the shares owned by entrepreneur and investor Magnus Kjøller.  The team was replaced by a whole new team and organisation launched a "Masterplan 2018”

Atlanta Gladiators: The Atlanta Gladiators are a professional minor league ice hockey team based in Duluth, Georgia (in the Atlanta metropolitan area).  The Gladiators play in the South Division of the ECHL's Eastern Conference.  The Gladiators play their home games at the Infinite Energy Arena.

Question: Where does Chuck Weber's ice hockey team play its home games?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "coach_name": {
      "type": "string",
      "description": "The name of the ice hockey coach."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the ice hockey team coached by the individual."
    },
    "team_league": {
      "type": "string",
      "description": "The league in which the team plays."
    },
    "home_arena": {
      "type": "string",
      "description": "The name of the arena where the team plays its home games."
    },
    "arena_location": {
      "type": "string",
      "description": "The city and state where the home arena is located."
    }
  },
  "required": [
    "coach_name",
    "team_name",
    "team_league",
    "home_arena",
    "arena_location"
  ],
  "additionalProperties": false
}
