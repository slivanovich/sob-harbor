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
1996–97 Detroit Pistons season: The 1996–97 NBA season was the Pistons' 49th season in the National Basketball Association, and 40th season in the city of Detroit.  During the offseason, the Pistons re-signed free agent Rick Mahorn, who was a member of the championship team in the 1989 NBA Finals.  The team also acquired Stacey Augmon and Grant Long from the Atlanta Hawks, but later on sent Augmon to the Portland Trail Blazers for Aaron McKie at midseason.  The Pistons got off to a fast start winning ten of their first eleven games on their way to a 20–4 start.  However, they went 34–24 for the remainder of the season finishing third in the Central Division with a 54–28 record.  Grant Hill averaged 21.4 points, 9.0 rebounds, 7.3 assists and 1.8 steals per game, while finishing third in MVP voting behind Karl Malone and Michael Jordan.  Hill along with Joe Dumars, and head coach Doug Collins represented the Eastern Conference during the 1997 NBA All-Star Game.

Odessa Jackalopes: The Odessa Jackalopes are a Tier II junior ice hockey team playing in the North American Hockey League (NAHL).  The team is based in Odessa, Texas and plays their home games at Ector County Coliseum.  Jackalopes games are broadcast on the radio on KFZX.

2008 Canadian Major Indoor Soccer League season: The 2008 Canadian Major Indoor Soccer League (CMISL) season had each team playing 10 games.  The schedule however was unbalanced as both the Edmonton Drillers and Saskatoon Accelerators played six home games and two road games and two at a neutral site, while the Calgary United FC played five home games and five road games.  The games held at the Stampede Corral were unique as they were featured in a round-robin style with all CMISL teams participating.  Due to scheduling concerns at the MTS Centre, the Winnipeg Alliance FC were a road-only franchise, playing all 10 of their games away from home.

Detroit Pistons: The Detroit Pistons are an American professional basketball team based in Detroit, Michigan.  The Pistons compete in the National Basketball Association (NBA) as a member club of the league's Eastern Conference Central Division.  The team plays its home games at Little Caesars Arena and was founded in Fort Wayne, Indiana as the Fort Wayne (Zollner) Pistons in 1941, a member of the National Basketball League (NBL).  The Pistons joined the Basketball Association of America (BAA) in 1948.  In 1949, the NBL and BAA merged to become the NBA, and the Pistons became part of the merged league.  Since moving to Detroit in 1957, the Pistons have won three NBA championships in 1989, 1990 and 2004.

Rick Mahorn: Derrick Allen "Rick" Mahorn (born September 21, 1958) is an American retired National Basketball Association (NBA) player who, at 6'10", played power forward and center.  He is currently a radio analyst for the Detroit Pistons and works as a co-host/analyst on SiriusXM NBA Radio.

Duluth Huskies: The Duluth Huskies are an amateur baseball team playing in the Northwoods League, a collegiate summer baseball league.  They have been operating in Duluth, Minnesota since 2003.  The Huskies play home games at Wade Stadium in Duluth, which was built in 1941.  The team plays 72 games throughout the summer, 36 home and 36 away.  The team mascot is Harley D. Huskie.  Huskies Games are streamed on Northwoods League TV.

SønderjyskE Ishockey: SønderjyskE (Ice hockey) is a professional ice hockey team playing in the top Danish ice hockey league Metal Ligaen.  The team is part of SønderjyskE which is a sports umbrella with football, handball and ice hockey teams.  The team plays home games in Vojens, a small town in the southernmost part of Jutland.  SønderjyskE is the only team in Denmark which home arena has a narrow sized rink (common in North America and the NHL), whereas all other rinks in the country are standard IIHF sized rinks.  Most of the clubs foreign players are also originating from North America.  "SønderjyskE Ishockey Support" is the fan club and the biggest icehockey fan club in Denmark with more than 800 members.

Dubuque Fighting Saints: The Dubuque Fighting Saints are a Tier I junior ice hockey team playing in the United States Hockey League (USHL) and are based in the city of Dubuque, Iowa, on the banks of the Mississippi River at the border intersects of Iowa, Illinois, and Wisconsin.  Home games are played at the Mystique Community Ice Center (capacity: 3,079).  Home and away games are broadcast live on KIYX, with Jordan Kuhns handling play-by-play with select games televised locally each season on KCRG-TV channel 9.2.

Orangefield Old Boys' Association F.C.: Orangefield Old Boys' Association Football Club (or Orangefield OB) is a Northern Irish, intermediate football club playing in Division 1A of the Northern Amateur Football League.  The club formed in 1966 and included past members and teachers of Orangefield High School.  The club joined the Amateur League in 1970, achieving intermediate status in 1987.  They currently play their home matches at the Cregagh Sports Club on Gibson Park Avenue, Belfast.  The first team is managed by Gary Cunningham with Stephen Carlisle serving as assistant manager.  Orangefield OB field six teams in total.  As well as the first team, there is a second team playing in NAFL Division 3B, a development team playing in Div 4 of BBOB league and junior teams for the Under 16's, Under 15's and Under 14's.

1997–98 Detroit Pistons season: The 1997–98 NBA season was the Pistons' 50th season in the National Basketball Association, and 41st season in the city of Detroit.  Despite signing free agents Brian Williams and Malik Sealy during the offseason, the Pistons got off to a slow start with a 6–11 record as Joe Dumars missed ten games due to hamstring and shoulder injuries.  In late December, they traded Theo Ratliff and Aaron McKie to the Philadelphia 76ers for Jerry Stackhouse and Eric Montross.  At midseason, head coach Doug Collins was fired after a 21–24 start, and was replaced with Alvin Gentry.  Collins would later on get a job as color analyst for the "NBA on NBC".  Despite another stellar season from Grant Hill, who was selected for the 1998 NBA All-Star Game, the Pistons missed the playoffs finishing sixth in the Central Division with a 37–45 record.  Following the season, Sealy signed as a free agent with the Minnesota Timberwolves, Grant Long re-signed with the Atlanta Hawks, and Rick Mahorn re-signed with the Philadelphia 76ers.

Question: Rick Mahorn is currently a radio analyst for the team playing its home games at which location?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "analyst_name": {
      "type": "string",
      "description": "The name of the radio analyst."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the team the analyst works for."
    },
    "team_league": {
      "type": "string",
      "description": "The league the team competes in."
    },
    "home_arena": {
      "type": "string",
      "description": "The name of the arena where the team plays its home games."
    },
    "team_city": {
      "type": "string",
      "description": "The city where the team is based."
    }
  },
  "required": [
    "analyst_name",
    "team_name",
    "team_league",
    "home_arena",
    "team_city"
  ],
  "additionalProperties": false
}
