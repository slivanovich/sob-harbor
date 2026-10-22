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
2017 Mexico City ePrix: The 2017 Mexico City ePrix (formally the 2017 FIA Formula E Julius Baer Mexico City ePrix) was a Formula E motor race held on 1 April 2017 before a crowd of 36,000 people at the Autódromo Hermanos Rodríguez, Mexico City, Mexico.  It was the fourth round of the 2016–17 Formula E season, and the second running of the event.  The 45-lap race was won by Audi Sport ABT driver Lucas di Grassi after starting from 15th position.  Jean-Éric Vergne finished second for the Techeetah team and Virgin driver Sam Bird came in third.

2017 Berlin ePrix: The 2017 Berlin ePrix (formally the 2017 FIA Formula E Berlin ePrix) were a pair of Formula E motor races held on 10 and 11 June 2017 at the Tempelhof Airport Street Circuit in Berlin before a crowd of 24,000 people.  They were the seventh and eighth rounds of the 2016–17 Formula E season season and the third running of the event.  The 44-lap race contested on 10 June was won by Mahindra driver Felix Rosenqvist after starting from second place.  Lucas di Grassi finished second for Audi Sport ABT and Rosenqvist's teammate Nick Heidfeld came in third.  The longer 46-lap event on 11 June was won by e.Dams-Renault driver Sébastien Buemi who started from second position.  Rosenqvist finished in second and di Grassi was third.

2017 New York City ePrix: The 2017 New York City ePrix (formally the 2017 FIA Formula E Qualcomm New York City ePrix) were a pair of Formula E motor races held on July 15 and 16, 2017 at the Brooklyn Street Circuit in Red Hook, Brooklyn before a two-day crowd of 20,000 people.  There were the ninth and tenth races of the 2016–17 Formula E season and the inaugural running of the event.  The first race, contested over 43 laps on 15 July, was won by Virgin driver Sam Bird after starting from fourth place.  Jean-Éric Vergne finished second for Techeetah, and his teammate Stéphane Sarrazin came in third.  The longer 49-lap race held the following day was won by Bird from a pole position start.  Mahindra teammates Felix Rosenqvist and Nick Heidfeld took second and third places.

2017 Montreal ePrix: The 2017 Montreal ePrix (formally the 2017 FIA Formula E Hydro-Québec Montréal ePrix) were a pair of Formula E races held on 29 and 30 July 2017 at the Montreal Street Circuit in Montreal, Quebec before an two-day crowd of 45,000 people.  There were the eleventh and twelfth races of the 2016–17 Formula E season and the inaugural running of the event.  The first race, contested over 35 laps on 29 July, was won by Audi Sport ABT driver Lucas di Grassi after starting from pole position.  Jean-Éric Vergne finished second for the Techeetah team and his teammate Stéphane Sarrazin came in third.  The longer 37-lap race held the following day was won by Vergne from a third place start.  Felix Rosenqvist took second for the Mahindra team and Virgin driver José María López secured a third-place finish.

Colin Fleming (racing driver): Colin Fleming (born April 21, 1984 in San Diego, California) is an American former racing driver who completed in the Formula Renault 2.0 Eurocup, Formula Renault 2000 Germany and Formula Renault 3.5 in 2005 and 2006 with Jenzer Motorsport and Carlin Motorsport, he was also a member from the Red Bull Junior Team, Fleming finished 4th in the Formula Renault 2.0 Eurocup in 2004 and was rookie of the year in the Formula Renault 2000 Germany also in that year.  He also raced against fellow American and Californian and future Formula One Driver Scott Speed.  In 2005 he switched to the Formula Renault 3.5 with Swiss team Jenzer Motorsport, despite three DNS in the first 3 and missing one race of that season he finished 13th with 34 points with a best finish of 3rd in the second race in the Bugatti Circuit, to 2006 he switched to Carlin where he finished 6th in the first race of the season in Zolder, however he failed to qualify to the Second Race of the weekend and he finished 4th in Circuit de Monaco and 8th in both races in Istanbul Park, after this round he asked to leave Carlin and the Red Bull Junior Team, Red Bull officially released him and he was replaced by fellow Red Bull Junior Team member and Future Formula One Champion Sebastian Vettel, after leaving Red Bull, he returned to the United States to complete in the Atlantic Championship mid-season and he finished 20th with 45 points and since then has not raced anymore in a Major Series, until he decided to retire.  Now Colin is a high-level executive with Salesforce.

2017 Monaco ePrix: The 2017 Monaco ePrix (formally the 2017 FIA Formula E Monaco ePrix) was a Formula E motor race held on 13 May 2017 at the Circuit de Monaco in Monte Carlo before a crowd of 18,000 people.  It was the fifth round of the 2016–17 Formula E season and the second running of the event.  The 51-lap race was won by e.Dams-Renault driver Sébastien Buemi after starting from pole position.  Lucas di Grassi finished second for Audi Sport ABT and Mahindra driver Nick Heidfeld came in third.

2017 Buenos Aires ePrix: The 2017 Buenos Aires ePrix (formally the 2017 FIA Formula E Buenos Aires ePrix) was a Formula E motor race held on 18 February 2017 at the Puerto Madero Street Circuit in Puerto Madero, Buenos Aires, Argentina in front of a crowd of 21,000 people.  It was the third round of the 2016–17 Formula E season and the third running of the event.  The 37-lap race was won by e.Dams-Renault driver Sébastien Buemi after starting from third position.  Jean-Éric Vergne finished second for the Techeetah team and Audi Sport ABT driver Lucas di Grassi came in third.

Felix Rosenqvist: Felix Rosenqvist (born 7 November 1991 in Värnamo) is a Swedish racing driver currently racing in Formula E for Mahindra Racing and Super Formula for SUNOCO Team LeMans.  He holds the record of being the only driver ever to win the Macau Grand Prix (twice), Masters of Formula 3 (twice), Grand Prix de Pau and the FIA Formula 3 European Championship.

2017 Paris ePrix: The 2017 Paris ePrix (formally the 2017 FIA Formula E Qatar Airways Paris ePrix) was a Formula E motor race held on 20 May 2017 at the Circuit des Invalides in the Les Invalides building complex before a crowd of 46,000 people.  It was the sixth race of the 2016–17 Formula E season and the second running of the event.  The 49-lap race was won by e.Dams-Renault driver Sébastien Buemi after starting from pole position.  José María López finished second for the Virgin team and Mahindra driver Nick Heidfeld came in third.

2016 Hong Kong ePrix: The 2016 Hong Kong ePrix (formally the 2016 FIA Formula E HKT Hong Kong ePrix) was a Formula E motor race held on 9 October 2016, before a crowd of 30,000 people at the Hong Kong Central Harbourfront Circuit in Hong Kong.  It was the first race of the 2016–17 Formula E season and the inaugural running of the event as part of the championship.  The 45-lap race was won by e.Dams-Renault driver Sébastien Buemi who started from seventh place.  Lucas di Grassi finished second for Audi Sport ABT and Mahindra driver Nick Heidfeld came in third.

Question: What is the nationality of the driver who finished second in the second race in the 2017 Montreal ePrix ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the Formula E event."
    },
    "race_number": {
      "type": "integer",
      "description": "The specific race number within the event (e.g., 1 for the first race, 2 for the second)."
    },
    "driver_name": {
      "type": "string",
      "description": "The name of the driver who finished in the specified position."
    },
    "team_name": {
      "type": "string",
      "description": "The team the driver was racing for."
    },
    "finish_position": {
      "type": "integer",
      "description": "The finishing position of the driver in the race."
    },
    "driver_nationality": {
      "type": "string",
      "description": "The nationality of the driver."
    }
  },
  "required": [
    "event_name",
    "race_number",
    "driver_name",
    "team_name",
    "finish_position",
    "driver_nationality"
  ],
  "additionalProperties": false
}
