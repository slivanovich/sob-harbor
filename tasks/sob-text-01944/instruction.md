{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nOpel Rally Team: Opel Rally Team was an auto racing team by German car manufacturer Opel.  It competed at the World Rally Championship from 1982 to 1990.  Walter Röhrl won the drivers championship in 1982 with Opel.\n\nArmin Schwarz: Armin Schwarz (born 16 July 1963) is a German rally driver.  He competed in the World Rally Championship from 1988 to 2005, winning the 1991 Rally Catalunya and taking six other podium finishes.  Outside the WRC, he won the German Rally Championship (1987–88), the European Rally Championship (1996) and the \"Rally Masters\" event at the Race of Champions (2000).\n\n2018 FIA World Rally Championship: The 2018 FIA World Rally Championship will be the forty-fifth season of the World Rally Championship, an auto racing championship recognised by the Fédération Internationale de l'Automobile (FIA) as the highest class of international rallying.  Teams and crews will compete in fourteen events for the World Rally Championships for Drivers, Co-drivers and Manufacturers.  Crews are free to compete in cars complying with World Rally Car and Group R regulations; however, only Manufacturers competing with 2017-specification World Rally Cars are eligible to score points in the Manufacturers' championship.  The series will once again be supported by the WRC-2 and WRC-3 championships and the WRC Trophy at every round, and by the Junior World Rally Championship at selected rounds.\n\nChristian Geistdörfer: Christian Geistdörfer (born 1 February 1953 in Munich) is a German former rally co-driver.  His career in motorsport lasted from 1975 to 1990.  From 1977 to 1987, he co-drove to German rally driver Walter Röhrl, winning the World Rally Championship drivers' title in 1980 and 1982.  The pair also won the Monte Carlo Rally four times.  After Röhrl retired from the WRC, Geistdörfer co-drove to Hannu Mikkola in eight events in 1988 and 1989.\n\n2017 World Rally Championship: The 2017 FIA World Rally Championship is the forty-fourth season of the World Rally Championship, an auto racing championship recognised by the Fédération Internationale de l'Automobile (FIA) as the highest class of international rallying.  Teams and crews are competing in thirteen events—starting in Monte Carlo on 19 January and ending in Australia on 19 November—for the World Rally Championships for Drivers, Co-drivers and Manufacturers.  Drivers are free to compete in cars complying with World Rally Car and Group R regulations; however, only Manufacturers competing with 2017-specification World Rally Cars are eligible to score points in the Manufacturers' championship.  The series is once again supported by the WRC-2 and WRC-3 championships and the newly created WRC Trophy at every round, and by the Junior World Rally Championship at selected rounds.\n\nAchim Warmbold: Achim Warmbold (born 17 July 1941) is a German former rally driver.  He won the West German Rally Championship in 1971 and 1980, and scored two outright victories during the inaugural World Rally Championship season in 1973 at the Rally of Poland and Austrian Alpine Rally events.\n\nKaramjit Singh: Karamjit Singh (born 29 January 1962), also known as the Flying Sikh, is a Malaysian professional race driver in rallying, and was the first Asian driver to win the Fédération Internationale de l'Automobile (FIA) Production Car World Championship for Drivers, doing so on his first try.  He has been rallying professionally since 1985.  He has won the 2001 Asia Pacific Rally Championship for Drivers, the 2002 FIA Production Car World Championship for Drivers, as well as the 2002 and 2004 FIA Asia Pacific Rally Championship for Drivers.  He has raced for the Petronas EON Racing Team and Team Proton Pert Malaysia using Proton 4WD rally cars. His co-drivers have been (in chronological order) Ron Teoh, Allen Oh and John Bennie.  Karamjit is currently racing a 2WD Proton Satria Neo CPS R3 for the CUSCO Japan team in the Asia Pacific Rally Championships in 2011 after moving from the Proton R3 Malaysia Rally Team\n\nArmin Kremer: Armin Kremer (born December 4, 1968, Crivitz, East Germany) is a German rally driver who is currently competing in the 2013 World Rally Championship season in the WRC-2 class.  He began rallying in the WRC at the 1995 Rally de Portugal and has entered various rallies since.  He won the European Rally Championship in 2001 driving a Toyota Corolla WRC and the Asia-Pacific Rally Championship in 2003 in a Mitsubishi Lancer Evo VII.\n\n2016 World Rally Championship: The 2016 World Rally Championship was the forty-fourth season of the World Rally Championship, an auto racing championship recognised by the Fédération Internationale de l'Automobile (FIA) as the highest class of international rallying.  Teams and drivers competed in thirteen rounds—starting with the Rallye Monte Carlo in January and finishing with Rally Australia in November—for the World Rally Championships for Drivers and Manufacturers.\n\nWalter Röhrl: Walter Röhrl (born 7 March 1947) is a German rally and auto racing driver, with victories for Fiat, Opel, Lancia and Audi as well as Porsche, Ford and BMW.\n\nQuestion: Which German rally and auto racing driver won the drivers championship in 1982?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"driver_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the rally and auto racing driver.\"\n    },\n    \"driver_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the driver.\"\n    },\n    \"championship_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the championship was won.\"\n    },\n    \"championship_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of championship won (e.g., drivers championship).\"\n    },\n    \"winning_team\": {\n      \"type\": \"string\",\n      \"description\": \"The team the driver won the championship with.\"\n    }\n  },\n  \"required\": [\n    \"driver_name\",\n    \"driver_nationality\",\n    \"championship_year\",\n    \"championship_type\",\n    \"winning_team\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "driver_name": {
        "type": "string",
        "description": "The name of the rally and auto racing driver."
      },
      "driver_nationality": {
        "type": "string",
        "description": "The nationality of the driver."
      },
      "championship_year": {
        "type": "integer",
        "description": "The year the championship was won."
      },
      "championship_type": {
        "type": "string",
        "description": "The type of championship won (e.g., drivers championship)."
      },
      "winning_team": {
        "type": "string",
        "description": "The team the driver won the championship with."
      }
    },
    "required": [
      "driver_name",
      "driver_nationality",
      "championship_year",
      "championship_type",
      "winning_team"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
