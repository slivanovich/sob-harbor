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
Jonathan Cochet: Jonathan Cochet (born 4 January 1977 in Alençon, France) is a French racing driver.  He won the Championnat de France Formule Renault in 1997.  He was a test driver for Prost Grand Prix in 2001, and he was also a test driver with the Renault Formula One team in 2006.

José Dolhem: Louis José Lucien Dolhem (26 April 1944 – 16 April 1988) was a racing driver from France, and the half brother of Formula One driver Didier Pironi (they had the same father and their mothers were sisters).

Esteban Ocon: Esteban Ocon (born 17 September 1996) is a French racing driver who currently drives in Formula One for Force India.  He made his Formula One debut for Manor Racing in the 2016 Belgian Grand Prix, replacing Rio Haryanto.  Ocon is part of the Mercedes-Benz driver development programme.

Jimmy Clairet: Jimmy Clairet (born 20 December 1990) is a French racing driver currently competing in the TCR International Series.  Having previously competed in the French Renault Clio Cup & French Peugeot 208 Racing Cup.

Matthieu Vaxivière: Matthieu Vaxivière is a French racing driver.  He was born on 3 December 1994 in Limoges, France.  He was the 2011 French F4 champion.  In 2012 he raced in the V de V Endurance Cup, French GT, and 2e Grand Prix Èlectrique.  In addition, he was 14th in the 2012 Formula Renault 2.0 Alps season and 29th in the Formula Renault 2.0 Eurocup, driving for Tech 1 Racing.  In 2013 he finished 10th in the Formula Renault 2.0 Eurocup and 18th in the Formula Renault 2.0 Alps.  In 2014 he was assigned as one of the drivers for the Lotus F1 Junior team, while competing in the Formula Renault 3.5 series alongside Filipino-Swiss driver Marlon Stöckinger.

André Rossignol: André Rossignol was a French racing driver who became the first driver to win the 24 Hours of Le Mans twice, winning in consecutive years.  Rossignol was a driver for the French Lorraine-Dietrich automobile company, and had been on their driving team since the inaugural Le Mans in 1923 .  After having finished eighth and third the first two years, Rossignol and teammate Gérard de Courcelles won the event overall in 1925 .  The following year, Robert Bloch was assigned to drive with Rossignol, and the race was won once again, with all three Lorraine-Dietrichs finishing on the podium.

Jean-Louis Schlesser: Jean-Louis Schlesser (born 12 September 1948) is a French racing driver with experience in circuit racing and cross-country rallying.  He is known for his wins of many different competitions.  He is the nephew of Jo Schlesser, a former Formula One driver.

Pescarolo Sport: Pescarolo Sport was a motorsport team based in Le Mans, France and founded in February 2000 by French racing driver Henri Pescarolo and his friend and partner, French publisher François Granet.  They race in the Le Mans Series and the 24 Hours of Le Mans.  In October 2007, Henri Pescarolo purchased Jacques Nicolet's Saulnier Racing and created Pescarolo Automobiles, with the racing team becoming a division of the new company.  The Pescarolo Automobiles went into receivership on 15 June 2010.  Following a liquidation sale, the company was resold back to Henri Pescarolo and rebranded as Pescarolo Team for the 2011 season.  However, the team's financial situation did not improve, and was wound up in January 2013.

Henri Fournier: Henri Fournier (14 April 1871 – 18 December 1919) was a French racing driver.  Born in 1871 in Le Mans, Fournier began his career on motorcycles and tricycles.  In 1901 he came to the Mors racing team and was the most successful driver of this year, as he won both the Paris–Bordeaux and Paris–Berlin races.  In addition to his racing career, he did well in speed tests and in the United States set a new record for the mile with his car.  At the 1902 Paris-Vienna race he also dominated the first leg with an average speed of 114 km/h, but later had to give up with transmission failure.  In the autumn of that year he set the then land speed record at 123 km/h.

Didier Pironi: Didier Joseph Louis Pironi (26 March 1952 – 23 August 1987) was a French racing driver.  During his career he competed in 72 Formula One World Championship Grands Prix, driving for Tyrrell (1978–1979), Ligier (1980) and Ferrari (1981–1982).  He won the 24 Hours of Le Mans in 1978 driving a Renault Alpine A442B.

Question: When was the  French racing driver who has  José Dolhem as a half brother born? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "driver_name": {
      "type": "string",
      "description": "The name of the French racing driver."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the driver."
    },
    "relationship_to_dolhem": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of relationship to Jos\u00e9 Dolhem."
        },
        "related_driver_name": {
          "type": "string",
          "description": "The name of the driver Jos\u00e9 Dolhem is related to."
        }
      },
      "required": [
        "type",
        "related_driver_name"
      ],
      "additionalProperties": false
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the driver."
    }
  },
  "required": [
    "driver_name",
    "nationality",
    "relationship_to_dolhem",
    "birth_date"
  ],
  "additionalProperties": false
}
