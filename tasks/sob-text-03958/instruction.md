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
Ralph Garcia: Ralph "Rafael" Garcia (born December 14, 1948 in Los Angeles, California) is a former Major League Baseball pitcher.  Garcia played for the San Diego Padres in and .  He batted and threw right-handed.  He then played in the Mexican League from 1976 through 1988, mainly for the Indios de Ciudad Juarez.  He was inducted into the Mexican Baseball Hall of Fame in 2005.

Fernando Alfredo Maldonado: Fernando Alfredo Maldonado Hernández (born 8 January 1966) is a Mexican politician and lawyer affiliated with the PRI.  He currently serves as Deputy of the LXII Legislature of the Mexican Congress representing the State of Mexico.

Frank Garcia (basketball): Frank F. Garcia (  1918 – January 24, 1956) was an American professional basketball player and minor league baseball player.  In basketball, Cihlar played in the National Basketball League for the Cleveland Chase Brassmen / Allmen Transfer between 1943 and 1946.  In baseball, Garcia played the Butler Yankees (1939) and Leaksville-Draper-Spray Triplets (1946).

Fernando Seguignol: Fernando Alfredo Seguignol Garcia (born January 19, 1975 in Bocas Del Toro, Panama) is a former Major League Baseball first baseman and outfielder.  Seguignol also played 8 years in Nippon Professional Baseball.  A switch hitter, Seguignol is regarded as the best switch-hitter ever to play in Japan, along with Orestes Destrade.

Teddy Garcia: Alfonso Teddy Garcia (born June 4, 1964) is a former American professional football player who was a placekicker in the National Football League (NFL) and the World League of American Football (WLAF).  He played for the New England Patriots, Minnesota Vikings and Houston Oilers of the NFL, and the San Antonio Riders and Barcelona Dragons of the WLAF.  Garcia played collegiately at the University of Louisiana at Monroe.

Luis García (shortstop): Luis Rafael Garcia (born May 20, 1975 in San Francisco de Macorís, Dominican Republic) is a retired Major League Baseball shortstop.  He played during one season at the major league level for the Detroit Tigers.  He was signed by the Tigers as an amateur free agent in .  Garcia played his first professional season (in American baseball) with their Rookie league Bristol Tigers in , and split his last season with the Triple-A teams of the Baltimore Orioles (Rochester Red Wings) and Pittsburgh Pirates (Nashville Sounds) in .

Joe Spinks: Joseph "Joe" Spinks (born June 20, 1972) is an American retired basketball player and coach.  He played 8 years for ABC Amsterdam in the Netherlands, and was head coach and assistant coach for the team for 2 years.  Spink's nickname was "The Bull".  In 2010, he was inducted into the Campbell Sports Hall of Fame.

Freddy García (infielder): Freddy Adrian Garcia Felix (born August 1, 1972) is a Dominican retired Major League Baseball infielder.  He played during four seasons at the major league level for the Pittsburgh Pirates and Atlanta Braves.  He was signed by the Toronto Blue Jays as an amateur free agent in .  Garcia played his first professional season (in American baseball) with their Rookie league Medicine Hat Blue Jays in , and his last season with the Boston Red Sox's Triple-A Pawtucket Red Sox in .

Fernando Kanapkis: Fernando Alfredo Kanapkis García (born June 6, 1966 in Montevideo) is a Uruguayan retired football defender of Greek and Spanish descent, who obtained twenty international caps for his national team, scoring five goals.  He made his debut on April 30, 1992, in a friendly against Brazil (2–1), and played his last international match for his native country on October 13, 1993, against Germany (0–5).

Nippon Professional Baseball: Nippon Professional Baseball (日本野球機構 , Nippon Yakyū Kikō ) or NPB is the highest level of baseball in Japan.  Locally, it is often called Puro Yakyū (プロ野球 ) , meaning "Professional Baseball".  Outside Japan, it is often just referred to as "Japanese baseball".  The roots of the league can be traced back to the formation of the "Greater Japan Tokyo Baseball Club" (大日本東京野球倶楽部 , Dai-Nippon Tōkyō Yakyū Kurabu ) in 1934 and the original Japanese Baseball League.  NPB was formed when that league reorganized in 1950.

Question: When did the league where Fernando Alfredo Seguignol Garcia played 8 years reorganize?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the player."
    },
    "league_name": {
      "type": "string",
      "description": "The name of the professional baseball league."
    },
    "years_played_in_league": {
      "type": "integer",
      "description": "The number of years the player played in the specified league."
    },
    "league_reorganization_year": {
      "type": "integer",
      "description": "The year the specified league reorganized."
    }
  },
  "required": [
    "player_name",
    "league_name",
    "years_played_in_league",
    "league_reorganization_year"
  ],
  "additionalProperties": false
}
