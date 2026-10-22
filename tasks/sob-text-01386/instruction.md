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
Dennis Firestone: Dennis Firestone (born 22 July 1944 in Townsville, Australia) is a former CART driver from 1979 to 1987.  He was the Rookie of the year in CART 1980 season finishing in 12th in season points, his best season.  His best finish in a CART race was a pair of 5th places that year.  He made 5 starts in the Indianapolis 500 with a best finish of 10th in 1981, his next best finish being a 12th in 1984.  An accident at Indianapolis in 1987 resulted in a broken neck and ended his racing career.  Since his driving days, he has run a California trucking company.

2002 Gran Premio Telmex-Gigante: The 2002 Gran Premio Telmex-Gigante was the nineteenth and final round of the 2002 CART FedEx Champ Car World Series season, held on November 17, 2002 at the Autódromo Hermanos Rodríguez in Mexico City, Mexico.  It was the first Champ Car race at the track since the 1981 season.  The race preceded a mass exodus of significant drivers and teams who all competed in their final Champ Car event, most of whom knew beforehand that they would not return.  Most rued the fact that they were leaving for the rival Indy Racing League, wishing to continue in CART rather than endure a more stable future in the IRL.  CART's winningest driver (42 wins), Michael Andretti, along with Kenny Brack, Scott Dixon, Dario Franchitti, Tony Kanaan, and Japan's most successful driver in U.S. open wheel racing Tora Takagi would all bid CART adieu in favor of the IRL.  Other entities leaving CART included 1996-1999 champions Chip Ganassi Racing, 1995 champions Team KOOL Green, and Mo Nunn Racing permanently switched to the IRL, and Japanese automotive industry giants Honda and Toyota likewise left CART for the IRL.  Season champion Cristiano da Matta was set to leave CART for Formula One with his engine supplier's F1 team, and Christian Fittipaldi attempted a stock car career.

Harry MacDonald (racing driver): Harry MacDonald (born September 27, 1940 in Windsor, Ontario, Canada) is a retired racecar driver.  He raced in the UK Formula Super Vee series from 1977 to 1979 and in 1978 won a race at Texas World Speedway and finished third in the championship.  In 1981 he attempted to qualify for the Indianapolis 500 but failed to do so, then competed in the USAC "Gold Crown" Championship Car race at Pocono Raceway where he finished 5th in a field of very few top drivers, then competed in the CART race at Michigan International Speedway and finished 21st after an engine failure.  He resurfaced in 1983 to attempt to qualify for the Indy 500 but again failed to do so.

2003 German 500: The 2003 German 500 was the fifth round of the 2003 CART World Series season, held on May 11, 2003 on the oval track at EuroSpeedway Lausitz in Klettwitz, Brandenburg, Germany.  The race also featured the return of Alex Zanardi to a Champ Car racing cockpit, about a year and a half after he lost both his legs in a nearly fatal crash at the 2001 CART race at the track.

Jeff Wood (racing driver): Jeff Wood (born January 20, 1957) is an American former race car driver born in Wichita, Kansas.  He was Formula Atlantic Rookie of the Year in 1977.  He drove in the CanAm series for Carl Haas in 1981 and finished 5th in the series behind Danny Sullivan.  In 1982, driving for Bob Garnetson Racing, finished 3rd place in the 24 Hours of Daytona.  He then made his CART debut in 1983 at the Caesars Palace Grand Prix driving for Dan Gurney.  He then drove in the Formula Atlantic West Series where he won the 1985 championship.  He returned to CART in 1987 and made 4 starts for Dick Simon with his best finish being 10th.  He was away from the series in 1988, then returned in 1989 to make 5 starts for Gohr Racing, where he finished 12th at the Michigan 500.  In 1990 he drove for a new team, Todd Walther Racing, where he made his first attempt to qualify for the Indianapolis 500, but crashed in practice.  He made 10 other starts, with a 10th-place finish at Phoenix, finishing 22nd in points.  In 1991 he made 8 starts for Dale Coyne Racing, Arciero Racing, and Euromotorsports with the best finish being 13th.  7 starts in '92 for Arciero netted Wood a 12th-place finish and a single point.  In 1993 Wood attempted a nearly full season for Andrea Moda Formula/Euromotorsports but failed to qualify for 6 races and only made 8 starts and again failed to score points.  He made four more unsuccessful starts in 1994 for Euromotorsports in what would be his final races in the series.  He was named to an entry for the 1996 Indianapolis 500, but the car failed to appear.  His best finish in his 49 CART races was an 8th place that came in his second series start back in 1983 at Laguna Seca Raceway.

1996 Molson Indy Toronto: The 1996 Molson Indy Toronto was a CART race held on the street course at Exhibition Place in Toronto, Ontario, Canada on July 14, 1996.  The race was won by Adrian Fernandez, driving the #32 Lola/Honda for Tasman Motorsports, but was marred by an accident late in the race which resulted in the death of rookie driver Jeff Krosnoff.

Caesars Palace Grand Prix: The Caesars Palace Grand Prix was a car race held between 1981 and 1984.  For the first two years, the race was part of the Formula One World Championship, before becoming a round of the CART series in 1983.  Nissan/Datsun was a presenting sponsor of both races.

2001 Miller Lite 225: The 2001 Miller Lite 225 was a Championship Auto Racing Teams (CART) motor race held on June 3, 2001 at the Milwaukee Mile in West Allis, Wisconsin, USA.  It was the 6th round of the 2001 CART FedEx Championship Series season.  Team Rahal's Kenny Bräck scored his second career and second consecutive CART race win ahead of a resurgent Michael Andretti and rookie Scott Dixon.

Idiotarod: The Idiotarod is a shopping cart race in which teams of five "idiots" tie themselves to a (sometimes modified) grocery store shopping cart and run through the streets of a major metropolitan area.  The race usually features people in costumes and themed floats.  The races are fun competitions where sabotage, costume, and presentation are rewarded.  Sabotage, such as tripping competitors, throwing marbles or large obstacles in their paths, and the spreading of misinformation such as false route information, is common.

Robert Kubica: Robert Józef Kubica (; born 7 December 1984) is a Polish current rally and former Formula 1 racing driver.  He became the first Polish driver to compete in Formula One.  Between 2006 and 2009 he drove for the BMW Sauber F1 team, promoted from test driver to race driver during 2006.  In June 2008, Kubica took his maiden Formula One victory in the Canadian Grand Prix, becoming the first Polish driver to win a Formula One race.

Question: What Former Formula One turned cart race did Jeff Woods compete in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "driver_name": {
      "type": "string",
      "description": "The name of the racing driver."
    },
    "race_name": {
      "type": "string",
      "description": "The name of the race that fits the criteria."
    },
    "race_series_transition": {
      "type": "object",
      "properties": {
        "original_series": {
          "type": "string",
          "description": "The original racing series the event was part of."
        },
        "transition_year": {
          "type": "integer",
          "description": "The year the race transitioned to the new series."
        },
        "new_series": {
          "type": "string",
          "description": "The new racing series the event became part of."
        }
      },
      "required": [
        "original_series",
        "transition_year",
        "new_series"
      ],
      "additionalProperties": false
    },
    "driver_participation_year": {
      "type": "integer",
      "description": "The year the driver competed in this specific race."
    }
  },
  "required": [
    "driver_name",
    "race_name",
    "race_series_transition",
    "driver_participation_year"
  ],
  "additionalProperties": false
}
