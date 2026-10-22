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
Wilmington Waves: The Wilmington Waves were a minor league baseball team in Wilmington, North Carolina.  They were a Low-A class team that played in the South Atlantic League, and were a farm team of the Los Angeles Dodgers for the franchise’s only year in Wilmington.  They played all of their home games at Brooks Field, on the campus of the University of North Carolina at Wilmington.  However, because Brooks Field was not easy to spot on campus, attendance for the Waves' home games was substantially low.  Because of this handicap, the Waves were given a limited amount of time to find a new stadium or build a new one.  But the deadline was not met and, prior to the 2002 season, the Wilmington Waves were sold and moved to Albany, Georgia, where the franchise became the South Georgia Waves.

Independent baseball league: An independent baseball league is a professional baseball organization located in the United States and Canada that is not operated in conjunction with either a Major League Baseball team or an affiliated Minor League Baseball team.  Being independent allows teams to be located close to major league teams without their consent.  Such leagues have been around for many years and were once known as "outlaw leagues" due to their position outside the rules of affiliated minor league baseball.

Albany Giants: The Albany Giants were a minor league Negro league baseball team.  They played in the city of Albany, Georgia as a member of the Negro Southern League during 1926.

Lethbridge Black Diamonds: The Lethbridge Black Diamonds were a minor league baseball team located in Lethbridge, Alberta, Canada.  The team was previously known as the Lethbridge Mounties from 1992–1995 before becoming the Lethbridge Black Diamonds from 1996–1998.  They were one of the first two farm clubs of the Arizona Diamondbacks.  Only 16 months after Arizona was granted a major league baseball franchise, the first farm club — the Lethbridge Black Diamonds — took the field.  The team started playing two years before their parent club even played a game.  The team played their first game in June 1996, whereas the Arizona Diamondbacks started playing in April 1998.  The team played in the Pioneer League, which is a rookie league, with a shortented season, in Minor League Baseball.  Their home stadium was Henderson Stadium.  In 1999, the team was moved and became the Missoula Osprey.

Albany Polecats: The Albany Polecats were a minor league baseball team in Albany, Georgia.  They were a low-A class team that played in the South Atlantic League, and were a farm team of both the Montreal Expos and the Baltimore Orioles during the franchise's tenure in Albany.  They played all of their home games at the Paul Eames Sports Complex.  While at Paul Eames Sports Complex during their tenure, the stadium was dubbed "Polecat Park", albeit the stadium was named after Paul Eames, a minor league baseball legend.  During the team’s four years in the South Atlantic League, the Polecats never finished higher than eighth overall in the fourteen-team league.  Coupled with poor attendance by the Polecats, this proved too much to bear for the struggling franchise.  Prior the 1996 season, the Albany Polecats were sold and moved north to Salisbury, Maryland, where the franchise became the current-day Delmarva Shorebirds.

Paul Eames Sports Complex: The Paul Eames Sports Complex is a minor league baseball stadium, located in Albany, Georgia.  The stadium was the home of the South Georgia Peanuts, of the South Coast League, prior to the folding of the league in 2008.  It was the former home of the Albany Polecats, the Albany Alligators and the South Georgia Waves before the team moved to Columbus, Georgia to become the Columbus Catfish.  The complex was known as 'Polecat Park' when the Polecats team played there.

Waycross Moguls: The Waycross Moguls were a minor league baseball team, based in Waycross, Georgia as a representative of the Florida–Alabama–Georgia League in 1915.  However the team originated in 1906 as the Waycross Machinists of the Georgia State League for one season.  Waycross' minor league baseball team was then revived in 1913 as the Waycross Blowhards of the Empire State League.  In 1914 they were known as the Waycross Grasshoppers before changing their name to the Moguls during the season.

Albany Babies: The Albany Babies were a Class C league minor league baseball team located in Albany, Georgia.  The team played in the South Atlantic League from 1911 to 1916 .

Salisbury, Maryland: Salisbury is a city in and the county seat of Wicomico County, Maryland, United States, and the largest city in the state's Eastern Shore region.  The population was 30,343 at the 2010 census.  Salisbury is the principal city of the Salisbury, Maryland-Delaware Metropolitan Statistical Area.  The city is the commercial hub of the Delmarva Peninsula, which was long devoted to agriculture and had a southern culture.  It calls itself "The Comfortable Side of Coastal".

Columbia Fireflies: The Columbia Fireflies are a Minor League Baseball team based in Columbia, South Carolina.  The team plays in the Class A South Atlantic League and is an affiliate of the New York Mets of the National League in Major League Baseball.  The home stadium is Spirit Communications Park.  The team was formerly known as the Savannah Sand Gnats (1995–2015); they relocated from Savannah, Georgia, after the 2015 season.  It is the only professional baseball team in Columbia, and the first since the Capital City Bombers moved to Greenville, South Carolina, after the 2004 season.

Question: The Albany Polecats were a minor league baseball team in Albany, Georgia, the Albany Polecats were sold and moved north to Salisbury, a city in and the county seat of which county in Maryland, United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city where the team relocated."
    },
    "state_name": {
      "type": "string",
      "description": "The state where the city is located."
    },
    "county_name": {
      "type": "string",
      "description": "The name of the county where the city is located."
    },
    "previous_team_name": {
      "type": "string",
      "description": "The name of the team before relocation."
    },
    "new_team_name_after_relocation": {
      "type": "string",
      "description": "The name of the team after relocation."
    },
    "relocation_direction": {
      "type": "string",
      "description": "The direction of the team's relocation."
    }
  },
  "required": [
    "city_name",
    "state_name",
    "county_name",
    "previous_team_name",
    "new_team_name_after_relocation",
    "relocation_direction"
  ],
  "additionalProperties": false
}
