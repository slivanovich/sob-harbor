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
Toyota TF102: The Toyota TF102 was the car with which the Toyota team competed in the 2002 Formula One season, the team's inaugural Championship campaign.  The car reflected the results of a year's testing in 2001 with the TF101, and was designed primarily by Gustav Brunner and Dago Rohrer.  As with the TF101, it was piloted during the season by Mika Salo and Allan McNish.

Toyota TF101: The Toyota TF101 was a Formula One car used solely for testing purposes during the 2001 season, in preparation for the team's full-scale assault on the series in 2002.  The car was designed by Toyota F1's chief of chassis Jean-Claude Martens and was driven by Mika Salo and Allan McNish.  The TF101 was unofficially called the "AM01" by Toyota until the name of its successor, the TF102 was announced.

Loïc Duval: Loïc Duval (] ; born 12 June 1982) is a French professional racing driver currently racing for Audi Sport as a factory driver in DTM and driving for Dragon Racing in Formula E.  He won the 2013 24 Hours of Le Mans with Allan McNish and Tom Kristensen driving the Audi R18 for Audi Sport.

Honda RA099: The Honda RA099 was a prototype Formula One racecar, commissioned by Honda, designed by ex-Ferrari and Tyrrell designer Harvey Postlethwaite and built by Dallara in 1999.  Its purpose was similar to the one surrounding the Toyota TF101 of 2001, in that it was supposed to be a working test car used in preparation for a full-scale assault on Grand Prix racing in the following year/s.

Toyota Racing: Panasonic Toyota Racing was a Formula One team owned by Japanese car manufacturer Toyota and based in Cologne, Germany.  Toyota announced their plans to participate in F1 in 1999, and after extensive testing with their initial car, dubbed the TF101, the team made their debut in 2002.  The new team grew from Toyota's long-standing Toyota Motorsport GmbH organisation, which had previously competed in the World Rally Championship and the 24 Hours of Le Mans.  Despite a point in their first-ever race, Panasonic Toyota Racing never won a Grand Prix, their best finish being 2nd position, which they achieved five times – in 2005, 2008 and 2009.

Allan McNish: Allan McNish (born 29 December 1969) is a British former racing driver, commentator, and journalist from Scotland.  He is a three-time winner of the 24 Hours of Le Mans, most recently in 2013, as well as a three-time winner of the American Le Mans Series, which he last won in 2007.  He won the FIA World Endurance Championship (FIA WEC) in 2013.  He has also been a co-commentator and pundit for BBC Formula One coverage on TV, radio and online.

Johnny Mowlem: Johnny Mowlem (born 12 February 1969) is a professional British racing driver.  Mowlem is considered to be among the world's elite sports car drivers, having competed in every class of world championship sports car racing.  He is the 2013 European Le Mans Series GT champion, having previously won the British Porsche Cup championship in 1996 and 1997.  He has class victories in both the 24 Hours of Daytona and the 12 Hours of Sebring, and has earned podiums at virtually all of the world's major sports car races, including the Le Mans 24 hours and the 1000 km Nürburgring.  He has also achieved overall podium finishes at the Daytona 24 hours as well as at the famous 10-hour Petit Le Mans race in the USA.  Mowlem began his career in single seaters racing up to Formula 3 level and got his big break when he was chosen personally by triple Formula One World Champion Jackie Stewart to join his "staircase of "talent" team in the junior single seater formula, alongside drivers of the calibre of Dario Franchitti, Allan McNish and Gil de Ferran.  He switched to sportscars in 1996, winning the Class 1 championship of the British Porsche Cup and then gained international recognition the following year when he won all 17 races of the British Porsche Cup to become British champion.  This launched his professional career in World Sportscars.  Later in his career he gained further international attention for his work as a driver of the hybrid-powered Ginetta Zytek prototype racer in the ALMS in 2008 and 2009.  In 2010, Mowlem was a Lotus Racing factory driver, driving the American Le Mans Series (ALMS) and in the International GT Open Series for sports cars in Europe.  His latest driving championship came in the European Le Mans Series in 2013.  Mowlem raced in the ALMS series every year that sanctioning body held races.  Mowlem also operates his own driving academy, working with both corporate clients and drivers wishing for a career in racing.

2010 8 Hours of Castellet: The 2010 8 Hours of Le Castellet ("8 Heures du Castellet") was the inaugural round of the 2010 Le Mans Series season.  It took place at the Circuit Paul Ricard, Le Castellet, France on 11 April 2010.  It was the first Le Mans Series race that is longer than the standard 1,000-km distance the LMS use since the 2007 Mil Milhas Brasil.  Audi Sport Team Joest won the race overall in their first use of the Audi R15 TDI in the Le Mans Series, with drivers Allan McNish and Rinaldo Capello.  Aston Martin Racing and Rebellion Racing completed the overall podium five laps behind the winning Audi.  Strakka Racing also brought Honda Performance Development a win on their debut in the LMP2 category, leading the OAK Racing Pescarolo by 33 seconds.  Applewood Seven won the Formula Le Mans category, the first event in which this class participated in the Le Mans Series.  Team Felbermayr-Proton dominated the GT2 category by finishing in the top two positions, ahead of the first of the AF Corse Ferraris.

2013 6 Hours of Silverstone: The 2013 6 Hours of Silverstone was an auto racing event held at the Silverstone Circuit, near Silverstone, England on 12–14 April 2013.  The event was the opening round of the 2013 FIA World Endurance Championship season, and served as the annual award for the Royal Automobile Club's Tourist Trophy.  Briton Allan McNish, Dane Tom Kristensen, and Frenchman Loïc Duval won the race for Audi, just over three seconds ahead of their teammates.  The British Delta-ADR team were victorious in the LMP2 category, while Aston Martin Racing secured both the LMGTE Pro and LMGTE Am classes.

Stéphane Ortelli: Stéphane Ortelli (born 30 March 1970 in Hyères, Var, France) is a Monegasque professional racing driver with three world championship titles.  He has won the 24 Hours of Le Mans race in 1998 with Allan McNish and Laurent Aïello and the Spa 24 Hours in 2003 with Romain Dumas and Marc Lieb.  He's also won the GT1 Class at the 12 Hours of Sebring in 2005 with David Brabham and Darren Turner.  Currently, he is an Emil Frey Racing driver competing and developing the Jaguar and Lexus GT racing cars in the Blancpain Endurance Series and the VLN series.

Question: What do a Toyota TF101 and Allan McNish have in comman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_element_type": {
      "type": "string",
      "description": "The type or category of the common element shared by the entities."
    },
    "common_element_name": {
      "type": "string",
      "description": "The specific name of the common element."
    },
    "entity_roles": {
      "type": "array",
      "description": "Details about each entity's specific role or relationship to the common element.",
      "items": {
        "type": "object",
        "properties": {
          "entity_name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "role": {
            "type": "string",
            "description": "The role or relationship of the entity to the common element."
          }
        },
        "required": [
          "entity_name",
          "role"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_element_type",
    "common_element_name",
    "entity_roles"
  ],
  "additionalProperties": false
}
