{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohnny Mowlem: Johnny Mowlem (born 12 February 1969) is a professional British racing driver.  Mowlem is considered to be among the world's elite sports car drivers, having competed in every class of world championship sports car racing.  He is the 2013 European Le Mans Series GT champion, having previously won the British Porsche Cup championship in 1996 and 1997.  He has class victories in both the 24 Hours of Daytona and the 12 Hours of Sebring, and has earned podiums at virtually all of the world's major sports car races, including the Le Mans 24 hours and the 1000 km Nürburgring.  He has also achieved overall podium finishes at the Daytona 24 hours as well as at the famous 10-hour Petit Le Mans race in the USA.  Mowlem began his career in single seaters racing up to Formula 3 level and got his big break when he was chosen personally by triple Formula One World Champion Jackie Stewart to join his \"staircase of \"talent\" team in the junior single seater formula, alongside drivers of the calibre of Dario Franchitti, Allan McNish and Gil de Ferran.  He switched to sportscars in 1996, winning the Class 1 championship of the British Porsche Cup and then gained international recognition the following year when he won all 17 races of the British Porsche Cup to become British champion.  This launched his professional career in World Sportscars.  Later in his career he gained further international attention for his work as a driver of the hybrid-powered Ginetta Zytek prototype racer in the ALMS in 2008 and 2009.  In 2010, Mowlem was a Lotus Racing factory driver, driving the American Le Mans Series (ALMS) and in the International GT Open Series for sports cars in Europe.  His latest driving championship came in the European Le Mans Series in 2013.  Mowlem raced in the ALMS series every year that sanctioning body held races.  Mowlem also operates his own driving academy, working with both corporate clients and drivers wishing for a career in racing.\n\nAlex Zanardi: Alessandro \"Alex\" Zanardi (] ; born 23 October 1966) is an Italian professional racing driver and paracyclist.\n\nSébastien Bourdais: Sébastien Olivier Bourdais (born 28 February 1979) is a French professional racing driver, who resides in St. Petersburg, Florida.  He is one of the most successful drivers in the history of American Championship car racing, having won 36 races.  He won four successive championships under Champ Car World Series sanction from 2004 to 2007.  s of March 2017 he had won 75 races.\n\nAlain Ferté: Alain Ferté (born 8 October 1955 in Falaise, Calvados) is a professional racing driver.  He is the elder brother of Michel Ferté, who is also a professional racing driver.\n\nMax Papis: Massimiliano \"Max\" Papis (born October 3, 1969) is an Italian professional stock car racing driver who has competed in several top-level motorsports events such as Le Mans 24 Hours, Formula One and Champ Car.  He has three Champ Car victories.  He is the son-in-law of Emerson Fittipaldi.  His sons' godfather is fellow Italian Alex Zanardi.  Papis also currently drives in the NASCAR Whelen Euroseries.\n\n2005 FIA WTCC Race of Germany: The 2005 FIA WTCC Race Of Germany was the seventh round of the 2005 World Touring Car Championship season.  It was held at the Motorsport Arena Oschersleben.  Andy Priaulx took his first win of the season in the first race for BMW, and the second race was won by Alex Zanardi, also for BMW, at a track close to the one where he lost his legs in a crash in 2001.\n\nMichel Ferté: Michel Ferté (born 8 December 1958 in Falaise, Calvados) is a professional racing driver.  He is the younger brother of Alain Ferté, who is also a professional racing driver.\n\nPatrick Pilet: Patrick Pilet (born October 8, 1981) is a French professional racing driver currently racing for Porsche Motorsport as a factory driver in the FIA World Endurance Championship and other racing series.  He has competed in major sports car endurance races like the 24 Hours of Le Mans, 24 Hours of Daytona, 24 Hours of Spa, 12 Hours of Sebring and Petit Le Mans.\n\nDave Steele: David (Dave) Steele (May 7, 1974 – March 25, 2017) was an American professional racing driver who won numerous sprint car racing championships and also competed in IndyCar and NASCAR races.  Steele last drove a winged sprint car in the Southern Sprintcar Shootout Series, where he won the first 5 races in series history.  Steele was killed in a crash at Desoto Speedway on March 25, 2017.\n\nJim Richards (racing driver): Jim Richards (born 2 September 1947) is a New Zealand racing driver who has spent most of his racing life in Australia.  While retired from professional racing, Richards continues to compete in the Touring Car Masters series.  After seven Bathurst 1000 victories and four Australian Touring Car Championships, Richards was inducted into the V8 Supercars Hall of Fame in 2006 and the Australian Motorsports Hall of Fame in 2015.  He is the father of racing driver Steven Richards, and between them they have achieved 11 Bathurst 1000 wins, most recently in 2015.\n\nQuestion: The Italian professional racing driver and paracyclist born October 23, 1966 races for which car company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"driver_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the racing driver.\"\n    },\n    \"driver_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the racing driver.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the driver.\"\n    },\n    \"driver_roles\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professional roles held by the driver.\"\n    },\n    \"car_company\": {\n      \"type\": \"string\",\n      \"description\": \"The car company the driver races for.\"\n    }\n  },\n  \"required\": [\n    \"driver_name\",\n    \"driver_nationality\",\n    \"birth_date\",\n    \"driver_roles\",\n    \"car_company\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "driver_name": {
        "type": "string",
        "description": "The full name of the racing driver."
      },
      "driver_nationality": {
        "type": "string",
        "description": "The nationality of the racing driver."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the driver."
      },
      "driver_roles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professional roles held by the driver."
      },
      "car_company": {
        "type": "string",
        "description": "The car company the driver races for."
      }
    },
    "required": [
      "driver_name",
      "driver_nationality",
      "birth_date",
      "driver_roles",
      "car_company"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
