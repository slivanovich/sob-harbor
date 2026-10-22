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
2017 European Under-23 Baseball Championship: The 2017 European Under-23 Baseball Championship was an international baseball tournament held by the Confederation of European Baseball for players 23-year-old and younger.  The 2017 edition was be held in Austria (Wels), Czech Republic (Blansko and Brno) and Slovakia (Trnava).  The Dutch team won the first ever edition.

European Baseball Championship: The European Baseball Championship is the main championship tournament between national baseball teams in Europe, governed by the Confederation of European Baseball (CEB).  Italy won the inaugural European Baseball Championship in 1954 , and the competition has since been dominated by the Italian team and the Netherlands' team.  As of 2010, it is held every other year, in even-numbered years, with a total of thirty-four European Baseball Championships having been played.

America East Conference Baseball Tournament: The America East Conference Baseball Tournament, officially known as the America East Conference Baseball Championship, is the conference baseball championship of the NCAA Division I America East Conference.  The top four finishers in the regular season of the conference's six eligible teams advance to the double-elimination tournament, which is in the midst of a five-year residency at LeLacheur Park in Lowell, Massachusetts.  The winner of the tournament receives an automatic berth to the NCAA Division I Baseball Championship.  Prior to 1998, the tournament was a six-team double-elimination format.  After 2009, the conference also began allowing schools to host the championship on fields without lights.

European Under-23 Baseball Championship: The European Under-23 Baseball Championship is a biennial, under-23 international baseball tournament sanctioned and created by the Confederation of European Baseball (CEB).

Dwayne Kemp: Dwayne Kemp (born February 24, 1988 in Rotterdam) is a Dutch baseball player who played for the Netherlands national baseball team at the 2011 Baseball World Cup, 2010 European Baseball Championship, 2011 Baseball World Cup, 2013 World Port Tournament, 2015 World Port Tournament, 2016 Haarlem Baseball Week , , and the 2016 European Baseball Championship.

European Junior Baseball Championship: The European Junior Baseball Championship is a biennial, under-18 international baseball tournament sanctioned and created by the Confederation of European Baseball (CEB).  The tournament is conducted in the year prior to the 18U Baseball World Cup (formerly called the World Junior Baseball Championship), which is likewise held every other year.  The top 4 teams in the European Junior Baseball Championship qualify for the World Cup.

West Coast Conference Baseball Championship: The West Coast Conference Baseball Championship is the conference baseball championship of the Division I West Coast Conference.  As begun in 2013, the top four finishers in the regular season of the league's ten teams participate in the double-elimination tournament held at Banner Island Ballpark in Stockton, California.  The winner of the event earns the conference's automatic bid to the NCAA Division I Baseball Championship.

Sweden national under-23 football team: The Sweden national under-23 football team (also known as Sweden Olympic football team from 1992) is the football team representing Sweden in Olympics and is controlled by the Swedish Football Association.  Between 1952 and 1976, the Swedish U23 team was the main Swedish national youth team and represented Sweden in the UEFA European Under-23 Championship.  Sweden made their first and only European Under-23 Championship appearance in 1972 and was knocked out in the quarter-finals.  In 1976 the European Under-23 Championship was changed to be an Under-21 competition, so the Swedish U23 team became defunct and was replaced by the Sweden national under-21 football team.

Ivy League Baseball Championship Series: The Ivy League Baseball Championship Series is the conference baseball championship of the NCAA Division I Ivy League.  The regular season winners of each four team division participate in a best of three series held at campus sites, with the winner earning the conference's automatic bid to the NCAA Division I Baseball Championship.  In 2016, <a href="">Princeton Tigers

Wels: Wels (] ) is a city in Upper Austria, on the Traun River near Linz.  It is the county seat of Wels-Land.

Question: Which city in Upper Austria did 2017 European Under-23 Baseball Championship hold

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "championship_name": {
      "type": "string",
      "description": "The name of the baseball championship."
    },
    "championship_year": {
      "type": "integer",
      "description": "The year the championship was held."
    },
    "host_countries": {
      "type": "array",
      "description": "A list of countries that hosted the championship, along with the cities in each country.",
      "items": {
        "type": "object",
        "properties": {
          "country_name": {
            "type": "string",
            "description": "The name of the host country."
          },
          "cities_hosted": {
            "type": "array",
            "description": "A list of cities in this country that hosted the championship.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "country_name",
          "cities_hosted"
        ],
        "additionalProperties": false
      }
    },
    "city_in_upper_austria": {
      "type": "string",
      "description": "The specific city in Upper Austria where the championship was held."
    }
  },
  "required": [
    "championship_name",
    "championship_year",
    "host_countries",
    "city_in_upper_austria"
  ],
  "additionalProperties": false
}
