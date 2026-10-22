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
Vegas Golden Knights: The Vegas Golden Knights are a professional ice hockey team based in the Las Vegas metropolitan area.  The team began play in the 2017–18 NHL season, and is a member of the Pacific Division of the Western Conference of the National Hockey League (NHL).  The team is owned by Black Knight Sports & Entertainment, a consortium led by Bill Foley, and plays its home games at T-Mobile Arena on the Las Vegas Strip in Paradise, Nevada.

Ireland men's national ice hockey team: The Irish national ice hockey team (Irish: "Foireann haca oighir náisiúnta na hÉireann" ) is the national ice hockey team of the Republic of Ireland run by the Irish Ice Hockey Association and a member of the International Ice Hockey Federation (IIHF) since 26 September 1996.  Ireland gained promotion to Division II of the IIHF in 2007, but after a poor performance in their Division II debut, the team has been relegated to Division III.  They have not played in a world championship since placing 4th with 6 points in 2013.  With the closure of the Dundalk Ice Dome and they no longer meet their minimum participation standards.  The team had members from both Northern Ireland and the Republic of Ireland and has a working relationship with the Belfast Giants of the Elite Ice Hockey League (EIHL) and new Irish clubs, Flyers Ice Hockey Club and Dundalk Bulls.

China Dragon: The China Dragon () was a professional ice hockey team which played its home games in three different cities in China, including Harbin, Qiqihar, and Shanghai.  The team was a member of Asia League Ice Hockey between 2007 and 2017.  The team was formed in 1954 as two different clubs, Harbin and Qiqihar, as part of the China League.  In 2004, the clubs joined Asia League Ice Hockey and in 2007 they merged into a single club, China Sharks, backed by the National Hockey League's San Jose Sharks for financial reasons.  The team was renamed the China Dragon in 2009 when San Jose pulled out.  The team was dissolved following the 2016–17 Asia League Ice Hockey season.

Chicago Cardinals (ice hockey): The Chicago Cardinals were a professional ice hockey team playing in the American Hockey Association.  The team only played one season in the league.  It was notable because it was founded by Eddie Livingstone, a Toronto businessman, who had owned an ice hockey team in the National Hockey Association (NHA) and whose actions led the owners of the NHA to disband the league and form the National Hockey League (NHL) in 1917.  The Cardinals were formed by Livingstone in an attempt to bring about a rival league to the NHL.  Because of the Cardinals, the NHL attacked the AHA and attempted to steal its players.  The Cardinals would fold under the pressure placed on the league and the team.  Livingstone would attempt to recoup his losses by selling the team, but this was denied.  He later tried to sue for damages.

Renata Fast: Renata Fast (born October 6, 1994) is a women's ice hockey player that currently competes for the Toronto Furies of the Canadian Women's Hockey League.  She was a member of the Clarkson Golden Knights squad that captured the 2014 National Collegiate women's ice hockey championship title.  She made her debut with the Canada women's national ice hockey team at the 2015 4 Nations Cup, held from November 4–8 in Sundsvall, Sweden.  She went on to represent the Canada women's national ice hockey team at the 2016 4 Nations Cup in Vierumäki, Finland, Nov. 1-5.  She competed in the 2017 Women's World Championships in Plymouth, Michigan, losing in overtime to the United States.  She was selected for the 2017/2018 centralization roster in preparation for the 2018 Olympic Games to take place from 9 to 25 February 2018 in Pyeongchang County, South Korea.

Tom Hirsch: Thomas William Hirsch (born January 27, 1963 in Minneapolis, Minnesota) is a retired professional ice hockey player, who played 31 games in the National Hockey League between 1984 and 1988 for the Minnesota North Stars.  He was also a member of the United States national hockey team in the 1984 Winter Olympics, 1984 Canada Cup and 1982 Ice Hockey World Championship tournaments.  His career was ended by persistent shoulder injury problems.  Tom's daughter Casey played forward and was the captain of the Maple Grove Senior High School Girls Hockey Team her senior year.  She also played for the Syracuse University Orange, Women's Hockey Team starting fall of 2011.

Gisele Marvin: Gisele Marie "Gigi" Marvin (born March 7, 1987) is an American ice hockey player for the Boston Pride of the National Women's Hockey League.  As a member of the United States national women's ice hockey team, Marvin won a silver medal at the 2010 Olympic Winter Games and the 2014 Winter Olympics.  Her grandfather is Cal Marvin, the coach of the 1958 United States Men's National Ice Hockey Team and the manager of the 1965 United States Men's National Ice Hockey Team, is a member of the United States Hockey Hall of Fame.  She hails from Warroad, Minnesota, in Roseau County, the same small town as 1960 gold medalists Bill and Roger Christian and 1980 gold medalist Dave Christian.

Ronald Petrovický: Ronald Petrovický (born February 15, 1977 in Žilina, Czechoslovakia) is a Slovak ice hockey right wing formerly playing for Kontinental Hockey League (KHL) team Dinamo Riga.  He is currently with the Springfield Falcons of the American Hockey League.  He has played professionally in Europe and in North America in the National Hockey League (NHL) as well as international play for the Slovak national ice hockey team.  Ronald last played in the NHL with the Vancouver Canucks in National Hockey League preseason games on the basis of a try-out to obtain a contract, he failed to make the cut and was released by the team on September 24, 2009.

Oscar Lindberg (ice hockey): Oscar Lindberg (born 29 October 1991) is a Swedish ice hockey player for the Vegas Golden Knights of the National Hockey League (NHL).  He represented Sweden in the 2011 World Junior Ice Hockey Championships.  He also represented Sweden on their gold medal-winning 2013 IIHF World Championship team.

Aalborg Pirates: Aalborg Pirates is a professional ice hockey team (previously known as Aalborg Ishockey and AaB Ice Hockey) playing in the Danish ice hockey league, Metal Ligaen.  The ice hockey team first appeared in 1967 as AaB Ice Hockey organized under Aalborg Boldspilklub.  They play in the Danish national league and won the Danish league championship in 1981.  In 1997 AaB Ishockey merged with a smaller club, IK Aalborg.  The merged team was known as Aalborg Ishockey Klub (AIK) in the period 1997–2003, but following financial instability in the club, the professional license was transferred to Aalborg Boldspilklub ("'AaB’").  The team is located in Aalborg in the northern part of Jutland and ceased operations at the end of the 2011/12 season, where it was put up for sale.  In 2012 the team was bought by investors with the majority of the shares owned by entrepreneur and investor Magnus Kjøller.  The team was replaced by a whole new team and organisation launched a "Masterplan 2018”

Question: Who owns the ice hockey team that Oscar Lindberg plays for in the 2017-2018 National Hockey League?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The name of the ice hockey team."
    },
    "league": {
      "type": "string",
      "description": "The league the team plays in."
    },
    "season": {
      "type": "string",
      "description": "The specific season mentioned in the question."
    },
    "owner_details": {
      "type": "object",
      "properties": {
        "owner_name": {
          "type": "string",
          "description": "The name of the entity that owns the team."
        },
        "owner_type": {
          "type": "string",
          "description": "The type of entity that owns the team (e.g., consortium)."
        },
        "lead_individual": {
          "type": "string",
          "description": "The name of the individual leading the ownership group, if specified."
        }
      },
      "required": [
        "owner_name",
        "owner_type",
        "lead_individual"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "team_name",
    "league",
    "season",
    "owner_details"
  ],
  "additionalProperties": false
}
