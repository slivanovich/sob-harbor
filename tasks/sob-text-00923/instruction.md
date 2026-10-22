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
2016 Portland State Vikings football team: The 2016 Portland State Vikings football team represented Portland State University during the 2016 NCAA Division I FCS football season.  They were led by second-year head coach Bruce Barnum and played their home games at Providence Park.  They were a member of the Big Sky Conference.  They finished the season 3–8, 2–6 in Big Sky play to finish in a four way tie for ninth place.

List of sports venues in Portland, Oregon: The following is a list of sports venues in Portland, Oregon, specifically the metro area, that are currently in operation or defunct.  The city features two major sports franchises, the Portland Timbers of Major League Soccer (MLS) and the Portland Trail Blazers of the National Basketball Association (NBA).  The Portland Winterhawks, who are major junior ice hockey franchise in the Western Hockey League, have played in the city since 1976 when the Edmonton Oil Kings were relocated.  They are a unique team in that they have two venues, the Moda Center and the Veterans Memorial Coliseum.  Providence Park, a 20,323 seat open-air stadium which is the home of the Timbers and the Portland State Vikings football team, is the largest non-auto sports venue in Portland.  The Moda Center, formerly the Rose Garden, is a close second with 19,980 seats for basketball games and slightly less for hockey match-ups.  Portland International Raceway in Hayden Meadows has the largest seating capacity (30,000) of any sporting venue in Portland.  There are several golf courses in the Portland metro area, including the Portland Golf Club where the 1946 PGA Championship was held.

2014 Portland State Vikings football team: The 2014 Portland State Vikings football team represented Portland State University in the 2014 NCAA Division I FCS football season.  They were led by fifth year head coach Nigel Burton and played their home games at Providence Park.  They were a member of the Big Sky Conference.  They finished the season 3–9, 2–6 in Big Sky play to finish in a three way tie for tenth place.

2015 Portland State Vikings football team: The 2015 Portland State Vikings football team represented Portland State University during the 2015 NCAA Division I FCS football season.  They were led by head coach Bruce Barnum and played their home games at Providence Park, with one home game at Hillsboro Stadium.  They were a member of the Big Sky Conference.  They finished the season 9–3, 6–2 in Big Sky play to finish in a tie for second place.  They received an at-large bid to the FCS Playoffs where they lost in the second round to Northern Iowa.

Portland Timbers: The Portland Timbers are an American professional soccer club based in Portland, Oregon.  The Timbers compete in Major League Soccer (MLS) as a member club of the league's Western Conference. The Timbers play their home games at Providence Park since 2011 when the team began play as an expansion team in the league.

Providence Steam Roller: The Providence Steam Roller (also referred to as the Providence Steam Rollers, the Providence Steamroller and the Providence Steamrollers) was a professional American football team based in Providence, Rhode Island in the National Football League from 1925 to 1931.  Providence was the first New England team to win an NFL championship.  The Steam Roller won the league's championship in 1928.  They are the last team to win a championship and no longer be in the league.  Most of their home games were played in a 10,000-seat stadium that was built for bicycle races called the Cycledrome.

2014–15 Villanova Wildcats men's basketball team: The 2014–15 Villanova Wildcats men's basketball team represented Villanova University in the 2014–15 NCAA Division I men's basketball season.  Led by the school's 14th head coach Jay Wright, the Wildcats participated in the Big East Conference and played their home games at The Pavilion, with some select home games at the Wells Fargo Center.  They finished the season 33–3, 16–2 in Big East play to win the Big East regular season championship.  They defeated Marquette, Providence, and Xavier to become champions of the Big East Tournament.  They received an automatic bid to the NCAA Tournament, gaining the #1 seed in the East Regional, where they defeated Lafayette in the second round before getting upset in the third round by NC State.  With their 31st win of the season, a 63–61 win over Providence in the semifinals of the 2015 Big East Tournament, the Wildcats set a single season record for wins, which would eventually finish at 33.  That record last only one year after the 2015–16 team won 35 games.

2017 Portland State Vikings football team: The 2017 Portland State Vikings football team represent Portland State University during the 2017 NCAA Division I FCS football season.  They are led by third-year head coach Bruce Barnum and play their home games at Providence Park, with one home game at Hillsboro Stadium.  They are a member of the Big Sky Conference.

Portland State Vikings football: The Portland State Vikings football program is the intercollegiate American football team for the Portland State University located in the U.S. state of Oregon.  The team competes in the NCAA Division I Football Championship Subdivision (FCS) and are members of the Big Sky Conference.  The school's first football team was fielded in 1947.  The team plays its home games at the 20,483 seat Providence Park.  Viking football practice takes place on campus at the Peter W. Stott Field.

Kevin Goldthwaite: Kevin Goldthwaite (born December 9, 1982 in Sacramento, California) is a former American soccer player who last played for Portland Timbers of Major League Soccer.

Question: The team Kevin Goldthwaite last played for play their home games at Providence Park since what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_name": {
      "type": "string",
      "description": "The name of the sports team."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the team plays home games."
    },
    "start_year": {
      "type": "integer",
      "description": "The year the team started playing home games at the specified stadium."
    }
  },
  "required": [
    "team_name",
    "stadium_name",
    "start_year"
  ],
  "additionalProperties": false
}
