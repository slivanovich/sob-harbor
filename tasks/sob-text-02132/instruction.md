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
1983 British Grand Prix: The 1983 British Grand Prix (formally the XXXVI Marlboro British Grand Prix) was a Formula One motor race held at Silverstone on 16 July 1983.  It was the ninth race of the 1983 Formula One season.  The 67-lap race was won by Renault driver Alain Prost after he started from third position.  Nelson Piquet finished second for the Brabham team and Ferrari driver Patrick Tambay came in third.

1981 Argentine Grand Prix: The 1981 Argentine Grand Prix was the third motor race of the 1981 Formula One season and was held at the Buenos Aires circuit in Argentina on 12 April 1981.  This was the last Argentine Grand Prix until 1995.  Thanks to designer Gordon Murray's alternative solution to flexible side skirts, the Brabham cars of Nelson Piquet and Héctor Rebaque were dominant in this race, with Piquet (who took pole at an average speed of 130.029 mph (209.261 km/h)) taking the lead immediately from Alan Jones on the back straight and Rebaque climbing up from 5th to 2nd over 23 laps.

1988 Brazilian Grand Prix: The 1988 Brazilian Grand Prix was a Formula One motor race held on April 3, 1988, at the renamed Autódromo Internacional Nelson Piquet in Rio de Janeiro.  Following his 3rd World Drivers Championship in the Jacarepaguá Circuit was named after local hero Nelson Piquet.  It was the first race of the Formula One season.

1983 European Grand Prix: The 1983 European Grand Prix was a Formula One motor race held at Brands Hatch on 25 September 1983.  The race, contested over 76 laps, was the fourteenth race of the 1983 Formula One season and was won by Nelson Piquet, driving a Brabham-BMW.  Piquet's Drivers' Championship rival Alain Prost was second in a factory Renault, while Nigel Mansell was third in a Lotus-Renault.  With the win, Piquet moved within two points of Prost at the top of the championship with one race remaining.

Brabham BT50: The Brabham BT50 was a Formula One racing car designed by Gordon Murray and powered by a turbo BMW engine.  It was raced by the Brabham team, owned by Bernie Ecclestone, during the 1982 Formula One season.  Driven by Nelson Piquet and Riccardo Patrese, it made its debut at the South African Grand Prix before being withdrawn for further development of its engine while the team reverted to the previous year's car, the Brabham BT49.  On the reintroduction of the BT50, Piquet finished fifth in the Belgian Grand Prix.  A few races later he drove it to a win in the Canadian Grand Prix.  Later in the year it achieved three more finishes in the points for the team.  During the second half of the season, Brabham implemented the strategy of mid-race refueling.  This allowed Piquet and Patrese to start the races relatively light and use their reduced weight to gain track position over their competitors before stopping to refuel.  The poor reliability of the BT50 meant that they had only a few opportunities to demonstrate the strategy in practice.

Alain Prost: Alain Marie Pascal Prost, OBE, Chevalier de la Légion d'honneur (born 24 February 1955) is a French former racing driver.  A four-time Formula One Drivers' Champion, only Sebastian Vettel (four championships), Juan Manuel Fangio (five championships), and Michael Schumacher (seven championships) have equalled or surpassed his number of titles.  From 1987 until 2001 Prost held the record for most Grand Prix victories and is considered as one of the greatest F1 drivers ever.  Schumacher surpassed Prost's total of 51 victories at the 2001 Belgian Grand Prix.  In 1999, Prost received the "World Sports Awards of the Century" in the motor sport category.

1986 Italian Grand Prix: The 1986 Italian Grand Prix was a Formula One motor race held at Monza on 7 September 1986.  The race, contested over 51 laps, was the thirteenth race of the 1986 Formula One season and was won by Nelson Piquet, driving a Williams-Honda, with team-mate and Drivers' Championship rival Nigel Mansell second and Stefan Johansson third in a Ferrari.  With fellow championship rivals Alain Prost and Ayrton Senna both failing to score, Piquet moved into second in the championship, five points behind Mansell.

2001 Rio de Janeiro motorcycle Grand Prix: The 2001 Rio de Janeiro motorcycle Grand Prix was the sixteenth and latest round of the 2001 Grand Prix motorcycle racing season.  It took place on the weekend of 1–3 November 2001 at the Autódromo Internacional Nelson Piquet.  It was also the final 500cc race in Grand Prix motorcycle racing history.  This also marked the final Grand Prix win in the career of Daijiro Kato before his death caused by a crash in the 2003 Japanese motorcycle Grand Prix race.

Ángel Nieto: Ángel Nieto Roldán (25 January 1947 – 3 August 2017) was a Spanish professional Grand Prix motorcycle racer.  He was one of the most accomplished motorcycle racers in the history of the sport, winning 13 World Championships and 90 Grand Prix victories in a racing career that spanned twenty-three years from 1964 to 1986.  His total of 90 Grand Prix victories ranks him third only to the 122 by Giacomo Agostini, and the 115 for Valentino Rossi.

Pedro Piquet: Pedro Piquet is a Brazilian racing driver.  He is the son of three-time Formula One world champion Nelson Piquet and younger half brother of Formula E champion Nelson Piquet, Jr. He is known for his successes in single-seater junior categories, including winning the 2014 and 2015 Brazilian Formula 3 Championships.

Question: At what race did this driver surpass the driver who rivals Nelson Piquet in most Grand Prix victories?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "surpassing_driver_name": {
      "type": "string",
      "description": "The name of the driver who surpassed the record."
    },
    "surpassed_driver_name": {
      "type": "string",
      "description": "The name of the driver whose record for Grand Prix victories was surpassed."
    },
    "rival_to_surpassed_driver_name": {
      "type": "string",
      "description": "The name of the driver who was a championship rival to the surpassed driver."
    },
    "record_description": {
      "type": "string",
      "description": "A description of the record that was surpassed."
    },
    "surpassing_event": {
      "type": "object",
      "properties": {
        "race_name": {
          "type": "string",
          "description": "The formal name of the Grand Prix where the record was surpassed."
        },
        "year": {
          "type": "integer",
          "description": "The year the Grand Prix took place."
        }
      },
      "required": [
        "race_name",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "surpassing_driver_name",
    "surpassed_driver_name",
    "rival_to_surpassed_driver_name",
    "record_description",
    "surpassing_event"
  ],
  "additionalProperties": false
}
