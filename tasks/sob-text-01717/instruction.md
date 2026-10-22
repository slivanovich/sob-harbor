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
2015–16 Formula E season: The 2015–16 FIA Formula E season was the second season of the FIA Formula E championship, held from 24 October 2015 to 3 July 2016.  The season sees the introduction of eight manufacturers, who are allowed to develop new power trains, specifically the e-motor, the inverter, the gearbox and the cooling system.  Nelson Piquet Jr. was the defending Drivers' Champion and Renault e.dams successfully defended teams champion.  After ten rounds, Sebastien Buemi won the championship by just two points over Lucas di Grassi after setting the fastest lap in the final race, where neither driver finished following an opening lap crash and several attempts to set the fastest lap in their second cars.

2019–20 Formula E season: The 2019–20 FIA Formula E season will be the sixth season of the FIA Formula E Championship, a motor racing championship for electrically-powered vehicles recognised by the sport's governing body, the Fédération Internationale de l'Automobile (FIA), as the highest class of competition for electric racing cars.

Formula E car: The Formula E car is an open-wheel auto racing car, powered by an electric motor.  The Formula E car is designed to take part in the FIA Formula E Championship.

Roborace: Roborace will be a motorsport championship with autonomously driving, electrically powered vehicles.  The series will be held on the same tracks the FIA Formula E Championship uses.  It will be the first global championship for driverless cars.  As of September of 2017, the official CEO is 2016-17 Formula E champion, Lucas Di Grassi.

Team Aguri: Team Aguri, formerly Amlin Aguri and officially the Team Aguri Formula E Team, was an international motor racing team founded by former Formula One and 24 Hours of Le Mans driver Aguri Suzuki (Executive Chairman) and Mark Preston (Team Principal) to compete in the FIA Formula E Championship for electric cars.  The team was based in Tokyo, Japan, and was in a technical partnership with McLaren.  At the end of the 2015-16 Formula E season, the team was sold to China Media Capital and renamed Techeetah.

Techeetah: The Techeetah Formula E Team (pronounced ‘Ta-chi-ta’) is a Chinese motor racing team under ownership of SECA - China Media Capital that competes in the electric racing series, Formula E.

Formula E: Formula E, officially the FIA Formula E Championship, is a class of auto racing that uses only electric-powered cars.  The series was conceived in 2012, and the inaugural championship started in Beijing on 13 September 2014.  The series is sanctioned by the FIA.  Alejandro Agag is the current CEO of Formula E.

Trulli GP: Trulli GP (officially Trulli Formula E Team) was a Swiss motor racing team founded by former Formula One driver and Monaco Grand Prix winner Jarno Trulli to compete in the inaugural FIA Formula E Championship for electric cars.  The team competed in a technical partnership with Drayson Racing Technologies.  It was announced on 1 July 2014 that the team was operating with Super Nova Racing.  Trulli announced that he would drive for the team, while later Italian Auto GP driver Michela Cerruti was announced as the second driver for the team.

2016–17 Formula E season: The 2016–17 Formula E season was the third season of the Fédération Internationale de l'Automobile (FIA) Formula E motor racing.  It featured the 2016–17 FIA Formula E Championship, a motor racing championship for open-wheel electric racing cars, recognised by FIA, the sport's governing body, as the highest class of competition for electrically powered vehicles.  Twenty-five drivers representing ten teams contested twelve ePrix, starting in Hong Kong on 8 October 2016 and ending in Montreal on 30 July 2017 as they competed for the Drivers' and Teams' Championships.

Sébastien Buemi: Sébastien Olivier Buemi (born 31 October 1988) is a Swiss professional racing driver, who formerly competed for Scuderia Toro Rosso in Formula One.  Buemi is currently a reserve driver for Scuderia Toro Rosso's sister team, Red Bull Racing, as well as being a member of Toyota's FIA World Endurance Championship squad and e.dams Renault in the FIA Formula E Championship.  Along with teammate Anthony Davidson, Buemi became World Champion in the LMP1 class of the FIA World Endurance Championship, in 2014.  He won the second ever Formula E championship, the season held across 2015–2016, by two points for setting the fastest lap time in the final race despite not finishing the event.

Question: What kind of cars doTecheetah and other racers use in the Formula E Championship?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "championship_name": {
      "type": "string",
      "description": "The official name of the motor racing championship."
    },
    "car_details": {
      "type": "object",
      "properties": {
        "power_source": {
          "type": "string",
          "description": "The type of power source used by the cars."
        },
        "design_type": {
          "type": "string",
          "description": "The general design type of the racing car."
        }
      },
      "required": [
        "power_source",
        "design_type"
      ],
      "additionalProperties": false
    },
    "team_involved": {
      "type": "string",
      "description": "The name of the specific team mentioned in the question."
    }
  },
  "required": [
    "championship_name",
    "car_details",
    "team_involved"
  ],
  "additionalProperties": false
}
