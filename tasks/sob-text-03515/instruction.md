{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLigier JS29: The Ligier JS29 was a Formula One car designed by Michel Tétu and Michel Beaujon for the Ligier team for use in the season.  It was originally developed for use with an Alfa Romeo turbo power plant but prior to the start of the season, Ligier lost the use of the engine.  The car had to be re-designed around a Megatron Straight 4 turbo engine.  Redesignated the JS29B, it scored a single point during the season when driver Rene Arnoux finished 6th in the Belgian Grand Prix.  Later in the season, the car was further refined to a JS29C specification.\n\nEquipe Ligier: Equipe Ligier is a motorsport team, best known for its Formula One team that operated from to .  The team was founded in 1968 by former French rugby union player Guy Ligier as a sports car manufacturer.\n\nLigier JS23: The Ligier JS23 was a Formula One car designed by Michel Beaujon and Claude Galopin for the Ligier team for use in the 1984 Formula One season.  The car was powered by a turbocharged Renault V6 engine and ran on Michelin tyres.  Drivers of the car during 1984 were François Hesnault and Andrea de Cesaris.\n\nLigier JS17: The Ligier JS17 was a Formula One car designed by Gérard Ducarouge and Michel Beaujon for use by the Ligier team during the season.  Powered by a Talbot-badged Matra V12, the JS17 was driven to two Grand Prix wins by Jacques Laffite.  It was updated to JS17B specification for the season until it was replaced later that year by the JS19.\n\nZakspeed 881: The Zakspeed 881 was a Formula One car designed by Chris Murphy and Heinz Zollner and raced by Zakspeed in the 1988 Formula One season.  The car was the last to be powered by the team's own 1.5 litre straight 4 turbo engine, the 1500/4.  The car was driven by veteran Piercarlo Ghinzani and West German F1 rookie Bernd Schneider.\n\nToleman TG185: The Toleman TG185 was a Formula One racing car designed by Rory Byrne and was used by Toleman Motorsport during the majority 1985 Formula One season.  The car was powered by the 800 bhp Hart 415T Straight 4 turbocharged engine.  The car was late in arriving for the 1985 season for no other reason than a lack of tyres.  In Toleman started the season using tyres supplied by Italian company Pirelli.  Part way through the season though the team pulled out of their tyre contract with Pirelli and started using the French Michelins instead.  However, when Michelin pulled out of F1 at the end of 1984, the team were unable to come to an agreement to use Goodyear rubber.  They were also unable to get a deal with Pirelli who were reluctant to supply tyres for the team.  It was only after team sponsor Benetton bought Spirit Racing and transferred their Pirelli contract to Toleman that the team were able to run in 1985.\n\nLigier JS25: The Ligier JS25 was a Formula One car designed by Michel Beaujon and Claude Galopin for use by the Ligier team during the 1985 Formula One season.  Like its predecessor, the JS23, the JS25 was powered by a turbocharged Renault V6 engine although the car ran on Pirelli instead of Michelin tyres after the French company pulled out of Grand Prix racing at the end of .  Drivers of the car were initially their driver Andrea de Cesaris and veteran Jacques Laffite who returned to the team after two fruitless years at Williams, but after a series of crashes, de Cesaris was fired by team boss Guy Ligier and replaced by Philippe Streiff.\n\nLigier JS31: The Ligier JS31 was a Formula One car designed by Michel Tétu and Michel Beaujon for the Ligier team for use in the 1988 Formula One season.  It was powered by the new, normally aspirated, 3.5L Judd CV V8 engine and, like the rest of the F1 grid in 1988, ran on Goodyear tyres.  Drivers for the team were French veteran René Arnoux in his 3rd season driving for team boss Guy Ligier, and Swede Stefan Johansson who had finished 5th in the World Championship with Ferrari in and 6th with McLaren in .\n\nZakspeed 861: The Zakspeed 861 was a Formula One car designed by Paul Brown for the Zakspeed team and was used in both the and seasons.  In 1986 its drivers were Jonathan Palmer and Huub Rothengatter.  The team never employed a test driver as they simply couldn't afford one despite sponsorship from German tobacco brand West.  The lack of money also meant that the engine on the car, Zakspeed's own 4 cylinder 1500/4 turbo engine which were rated at about 850 bhp for the season, were also short on power and development compared to those at the front of the grid (Honda, Renault, BMW, TAG-Porsche and Ferrari).  The team used Goodyear tyres.\n\nZakspeed 871: The Zakspeed 871 was a Formula One car designed by Chris Murphy and Heinz Zollner and raced by Zakspeed in the 1987 Formula One season.  The car was powered by the team's own 1.5 litre, 1500/4 straight 4 turbo engine, which was rated at about 820 bhp for the season.  Martin Brundle had moved after 3 years at Tyrrell to be Zakspeed's lead driver, in a virtual driver swap with Jonathan Palmer, who had left Zakspeed after two seasons to drive for Tyrrell.  Brundle was joined by former Formula 3000 champion Christian Danner, who had moved from Arrows.\n\nQuestion: What is the name of the motorsport team, best known for Formula One, founded in 1968, and which uses a car designed by Michel Tetu and Michel Beaujon built with a Megatron Straight 4 turbo engine?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the motorsport team.\"\n    },\n    \"founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the team was founded.\"\n    },\n    \"best_known_for_sport\": {\n      \"type\": \"string\",\n      \"description\": \"The sport the team is best known for.\"\n    },\n    \"car_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the specific car matching the criteria.\",\n      \"properties\": {\n        \"car_model\": {\n          \"type\": \"string\",\n          \"description\": \"The model name of the car.\"\n        },\n        \"designers\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The names of the car designers.\"\n        },\n        \"engine_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of engine used in the car.\"\n        }\n      },\n      \"required\": [\n        \"car_model\",\n        \"designers\",\n        \"engine_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"team_name\",\n    \"founding_year\",\n    \"best_known_for_sport\",\n    \"car_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "team_name": {
        "type": "string",
        "description": "The name of the motorsport team."
      },
      "founding_year": {
        "type": "integer",
        "description": "The year the team was founded."
      },
      "best_known_for_sport": {
        "type": "string",
        "description": "The sport the team is best known for."
      },
      "car_details": {
        "type": "object",
        "description": "Details about the specific car matching the criteria.",
        "properties": {
          "car_model": {
            "type": "string",
            "description": "The model name of the car."
          },
          "designers": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The names of the car designers."
          },
          "engine_type": {
            "type": "string",
            "description": "The type of engine used in the car."
          }
        },
        "required": [
          "car_model",
          "designers",
          "engine_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "team_name",
      "founding_year",
      "best_known_for_sport",
      "car_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
