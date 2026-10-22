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
2004 Brazilian Grand Prix: The 2004 Brazilian Grand Prix was a Formula One motor race held on 24 October 2004 at the Autódromo José Carlos Pace.  It was the final race of the 2004 season and the first time that a GP in Brazil was not one of the first three rounds of an F1 season, and local fans were delighted when Brazil's Rubens Barrichello took pole for his home race.  It would be Barrichello's first non-retirement at Interlagos in ten years, his previous finish at the circuit being at the season opener in 1994.  The early laps were held in changeable conditions, and the race ended up as a duel between Kimi Räikkönen and Juan Pablo Montoya, who were to be McLaren team-mates for 2005.  The Colombian took victory in his final race for Williams, which was also the last win for the Williams team until the 2012 Spanish Grand Prix.  Montoya's move to take the lead was brave even by his standards.  Elsewhere, Jaguar's final race was a failure of epic proportions, with their two drivers colliding, with Webber trying an optimistic-looking move on Klien whilst expecting his team-mate to move over.

2005 Brazilian Grand Prix: The 2005 Brazilian Grand Prix (formally the XXXIV Grande Prêmio do Brasil) was a Formula One motor race held on at the Autódromo José Carlos Pace in São Paulo, Brazil on 25 September 2005.  The 71-lap race was the seventeenth round of the 2005 Formula One season.  The race was won by McLaren driver Juan Pablo Montoya, who took the final race victory of his career, ahead of his team-mate, Kimi Räikkönen, who finished second.  Renault driver Fernando Alonso became the Drivers' Champion for the first time after he finished the race in third place.  Only he and Räikkönen had entered the race within mathematical contention of winning the title, and Alonso's podium ensured that he did with two rounds remaining.  Alonso also qualified in pole position for the race, but the fastest lap went to Räikkönen.

Survival Island: Survival Island, also known as Three, is a 2005 erotic thriller film written and directed by Stewart Raffill.  It stars Billy Zane, Kelly Brook, and Juan Pablo Di Pace.

2013 Toyota Owners 400: The 2013 Toyota Owners 400 was a NASCAR Sprint Cup Series stock car race that was held on April 27, 2013, at Richmond International Raceway in Richmond, Virginia, United States.  Contested over 406 laps-- extended from 400 laps due to a Green-white-checker finish on the 0.75-mile (1.20 km) D-shaped oval, it was the ninth race of the 2013 Sprint Cup Series championship.  Kevin Harvick of Richard Childress Racing won the race, his first win of the 2013 season, while Clint Bowyer finished second.  Joey Logano, Juan Pablo Montoya, and Jeff Burton rounded out the top five.

2016 Honda Indy Grand Prix of Alabama: The 2016 Honda Indy Grand Prix of Alabama was the 4th round of the 2016 IndyCar Series.  The race was contested over 90 laps at Barber Motorsports Park in Birmingham, Alabama.  It was the 7th time that the IndyCar Series had raced on the circuit.  In qualifying, Simon Pagenaud took pole position with a time of 1:06.7762, beating out his teammate Will Power.  Sébastien Bourdais set a new track record during the second round of qualifications with a time of 1:06.6001, but was unable to match that pace in the third round of qualifying, relegating him to a fifth place start.  Championship contender Juan Pablo Montoya struggled heavily in qualifying, placing 21st and last.

Centro Olímpico Juan Pablo Duarte: Centro Olímpico Juan Pablo Duarte (translation: Juan Pablo Duarte Olympic Center) is a multi-venued athletic complex in Santo Domingo, Dominican Republic.  It was initially built for the 1974 Central American and Caribbean Games, and also hosted multiple venues of the 2003 Pan American Games.

2013 FedEx 400: The 2013 FedEx 400 benefiting Autism Speaks was a NASCAR Sprint Cup Series stock car race held on June 2, 2013, at Dover International Speedway in Dover, Delaware, United States.  Contested over 400 laps on the 1–mile (1.6 km) oval, it was the thirteenth race of the 2013 Sprint Cup Series championship.  Tony Stewart won the race, his first win of the season, snapping a 30–race winless streak, while Juan Pablo Montoya finished second.  Jeff Gordon, Kyle Busch, and Brad Keselowski rounded out the top five.

Full House: Full House is an American sitcom created by Jeff Franklin for ABC.  The show chronicles the events of widowed father, Danny Tanner, who enlists his brother-in-law and best friend to help raise his three daughters.  It aired from September 22, 1987, to May 23, 1995, broadcasting eight seasons and 192 episodes.

Juan Pablo Di Pace: Juan Pablo Di Pace (born July 25, 1979) is an Argentine actor, singer and director.  Di Pace began his career in United Kingdom, performing in a number of musicals and appearing in films like "Survival Island" (2005) and "Mamma Mia! " (2008), and later moved to Spain, starring in several television series from 2009 to 2013.  In 2014, Di Pace began starring as Nicolas Treviño in the TNT drama series "Dallas".  Starting in 2016, he played the role of Kimmy Gibbler's estranged husband, Fernando, on "Fuller House", the sequel series to "Full House".

Nicolas Treviño: Nicolas Treviño (born Joaquin Reyes) is a fictional character on the TNT primetime soap opera, "Dallas".  He is portrayed by Juan Pablo Di Pace.

Question: Juan Pablo Di Pace had a role on the sequel series to what Jeff Franklin-created American sitcom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor in question."
    },
    "role_in_sequel_series": {
      "type": "string",
      "description": "The character played by the actor in the sequel series."
    },
    "sequel_series_name": {
      "type": "string",
      "description": "The name of the sequel series."
    },
    "original_series": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the original sitcom."
        },
        "creator": {
          "type": "string",
          "description": "The creator of the original sitcom."
        },
        "type": {
          "type": "string",
          "description": "The type of the original series (e.g., sitcom)."
        }
      },
      "required": [
        "name",
        "creator",
        "type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "role_in_sequel_series",
    "sequel_series_name",
    "original_series"
  ],
  "additionalProperties": false
}
