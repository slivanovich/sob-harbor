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
2014 Las Vegas Bowl: The 2014 Las Vegas Bowl was an American college football bowl game that was played on December 20, 2014 at Sam Boyd Stadium in Whitney, Nevada in the Las Vegas Valley.  The 23rd annual Las Vegas Bowl, it featured the Colorado State Rams of the Mountain West Conference against the Utah Utes from the Pac-12 Conference.  It was one of the 2014–15 bowl games that concluded the 2014 FBS football season.  The game started at 12:30 p.m. PST and aired on ABC and Sports USA Radio Network.  Sponsored by motor oil manufacturer Royal Purple, the game was officially known as the Royal Purple Las Vegas Bowl.

2016 Las Vegas Bowl: The 2016 Las Vegas Bowl was a college football bowl game that was played on December 17, 2016, at Sam Boyd Stadium in Las Vegas, Nevada.  The twenty-fifth annual Las Vegas Bowl is one of the 2016–17 bowl games that concludes the 2016 FBS football season.  The game aired on ABC.  Previously sponsored by lubricant manufactuer Royal Purple, the sponsorship ended in 2015, with the name of the bowl game reverting to the official name of the Las Vegas Bowl.

2015 Las Vegas Bowl: The 2015 Las Vegas Bowl was a post-season American college football bowl game played on December 19, 2015 at Sam Boyd Stadium in the Las Vegas suburb of Whitney, Nevada.  The 24th edition of the Las Vegas Bowl featured the BYU Cougars against the Utah Utes, earning the game the moniker the Holy War in Sin City (named for the "Holy War" rivalry game and the "Sin City" nickname for Las Vegas).  The game sold out 24 hours after the matchup was announced.  It began at 12:30 p.m. PST and aired on ABC.  It was one of the 2015–16 bowl games that concluded the 2015 FBS football season.  Sponsored by lubricant manufacturer Royal Purple, it was officially known as the Royal Purple Las Vegas Bowl.

2007 Las Vegas Bowl: The 2007 Pioneer Las Vegas Bowl was an NCAA-sanctioned Division I post-season college football bowl game between the UCLA Bruins and the Brigham Young University Cougars.  The Las Vegas Bowl gets its first choice of bowl-eligible teams from the Mountain West Conference (MWC) and the fourth/fifth choice (alternating every year) of bowl-eligible teams from the Pacific-10 Conference (Pac-10).  This bowl game was played on December 22, 2007 at 5 p.m. PST at 40,000-seat Sam Boyd Stadium in Whitney, Nevada, USA where this bowl game has been played since 1992.  It was broadcast on ESPN and ESPNHD.  Since 2001, the game has featured a matchup of teams from the MWC and Pac-10.

Sam Boyd Stadium: Sam Boyd Stadium is a football stadium in Whitney, Nevada, United States, an unincorporated community in the Las Vegas Valley.  It honors Sam Boyd (1910–1993), a major figure in the hotel and casino industry in Las Vegas.  The stadium consists of an uncovered horseshoe-shaped single-decked bowl, with temporary seating occasionally erected in the open north end zone.  The field has a conventional north-south orientation and is at an elevation of 1600 ft above sea level.

2006 Las Vegas Bowl: The 2006 Las Vegas Bowl was an NCAA-sanctioned Division I post-season college football bowl game between the Oregon Ducks and the Brigham Young University Cougars.  The Las Vegas Bowl gets its first choice of bowl-eligible teams from the Mountain West Conference (MWC) and the fourth/fifth choice (alternating every year) of bowl-eligible teams from the Pacific-10 Conference (Pac-10).  This bowl game was played on December 22, 2006 at 5 p.m. PST at 40,000-seat Sam Boyd Stadium in Whitney, Nevada, USA where this bowl game has been played since 1992.  It was broadcast on ESPN and ESPNHD.  Since 2001, the game has featured a matchup of teams from the MWC and Pac-10.

1992 Las Vegas Bowl: The 1992 Las Vegas Bowl was an American college football bowl game played at Sam Boyd Stadium in Whitney, Nevada on December 18, 1992.  It was inaugural Las Vegas Bowl and the first game of the bowl season that concluded the 1992 NCAA Division I-A football season.  The game featured the Bowling Green Falcons, champions of the Mid-American Conference (MAC), and the Nevada Wolf Pack, champions of the Big West Conference.  Bowling Green won the game by a score of 35–34.

2013 Las Vegas Bowl: The 2013 Las Vegas Bowl was an American college football bowl game that was played on December 21, 2013 at Sam Boyd Stadium in Whitney, Nevada in the Las Vegas Valley.  The 22nd annual Las Vegas Bowl, it featured the Mountain West Conference champion Fresno State Bulldogs against the USC Trojans of the Pac-12 Conference.  The game started at 12:30 p.m. PST and aired on ABC and Sports USA Radio.  It was one of the 2013–14 bowl games that concluded the 2013 FBS football season.  Sponsored by motor oil manufacturer Royal Purple, the game was officially known as the Royal Purple Las Vegas Bowl.  The Trojans won by a score of 45–20.

2007 UCLA Bruins football team: The 2007 UCLA Bruins football team represented the University of California, Los Angeles (UCLA) in the 2007 NCAA Division I FBS football season.  They played their home games at the Rose Bowl in Pasadena, California and were coached by Karl Dorrell for the regular season.  It was Dorrell's fifth, and final season as the UCLA head coach.  UCLA's season was marked by numerous injures, particularly at quarterback.  Original starting quarterback Ben Olson injured his knee early in the season and missed over four games.  Backup quarterback Patrick Cowan also suffered a knee injury but returned for two more games before suffering a collapsed lung against Arizona.  Coach Karl Dorrell was fired following the loss in the 77th UCLA-USC rivalry football game, the final regular season game for the Bruins.  Defensive coordinator DeWayne Walker became the interim coach for the 2007 Las Vegas Bowl, in which the Bruins lost to BYU, 17–16.  The Bruins finished 6–7 overall, 5–4 in the Pacific-10 Conference, where they were tied for fourth place.

2008 Las Vegas Bowl: The 2008 Pioneer Las Vegas Bowl was an NCAA-sanctioned Division I FBS post-season college football bowl game between the Arizona Wildcats, the fifth pick from the Pacific-10 Conference and the BYU Cougars, third place overall in the Mountain West Conference.  This bowl game was played on December 20, 2008 at 5 p.m. PST at 40,000-seat off campus Sam Boyd Stadium of the University of Nevada, Las Vegas in Whitney, Nevada and broadcast on ESPN.  Since 2001, the game has featured a matchup of teams from the MWC and Pac-10.  The announcers were Mike Patrick and Todd Blackledge with the sideline reporting by Holly Rowe.  The Wildcats stunned the 16th ranked Cougars in the coldest Las Vegas Bowl in history, 31-21.

Question: What is the elevation of the field at which the 2007 Las Vegas Bowl was held?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "bowl_game_year": {
      "type": "integer",
      "description": "The year the Las Vegas Bowl game was held."
    },
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium where the game was played."
    },
    "stadium_location": {
      "type": "string",
      "description": "The location of the stadium."
    },
    "field_elevation_feet": {
      "type": "integer",
      "description": "The elevation of the stadium's field in feet above sea level."
    }
  },
  "required": [
    "bowl_game_year",
    "stadium_name",
    "stadium_location",
    "field_elevation_feet"
  ],
  "additionalProperties": false
}
