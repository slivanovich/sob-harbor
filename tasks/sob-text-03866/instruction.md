{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCaterham CT01: The Caterham CT01 is a Formula One racing car produced by the British-based Caterham F1 Team which competed in the 2012 Formula One season.  The car, designed under the leadership of the team's technical director Mike Gascoyne, is the third car to be produced by the team and the first to carry the team's new name, following their renaming from Team Lotus at the end of 2011.  The CT01 was the first car launched for the 2012 season, when an online launch initially planned for 26 January, was cancelled and the car was released a day earlier instead.  The car was driven by Heikki Kovalainen and Vitaly Petrov, who replaced Jarno Trulli after the first test at Jerez.\n\nHispania F110: The Hispania F110, also known as the HRT F110, is a Formula One motor racing car designed and built by Dallara for Hispania Racing, for the season.  It was driven by Karun Chandhok, Bruno Senna, Christian Klien and Sakon Yamamoto and was unveiled in Murcia, Spain, on 4 March 2010.  It was the first car Hispania Racing entered in Formula One.\n\nWilliams FW34: The Williams FW34 was a Formula One racing car designed by Williams F1 for the 2012 Formula One season.  Following their worst season in their thirty-year history—in which they finished ninth in the World Constructors' Championship with just five points—the team underwent a technical review, employing former McLaren designer Mike Coughlan (having served his suspension for his role in the 2007 Formula One espionage controversy) as Chief Designer, and promoting Jason Somerville to Head of Aerodyamics.  The FW34 used the Renault RS27-2012 engine; the team had previously used Renault engines between 1989 and 1997.  The car, which was launched on the 7 February 2012, was driven by Pastor Maldonado and Bruno Senna.\n\nBruno Senna: Bruno Senna Lalli (] , born 15 October 1983) is a Brazilian professional racing driver currently racing for Rebellion Racing in the FIA World Endurance Championship.  He is the nephew of the late Ayrton Senna, three-time Formula One world champion.  Senna raced in Formula One from 2010–12.  He made his début driving for Hispania Racing in 2010, raced for Renault from August 2011 as a replacement for Nick Heidfeld, and drove for the Williams team in 2012.  Between 2014–16, he drove for Mahindra Racing in Formula E.  His mother is Ayrton's older sister, Viviane.  His father, Flávio Lalli, died in a motorcycle crash in 1996.  The colour scheme of Bruno's helmet is a slightly modified version of that used by his uncle Ayrton Senna.\n\nLotus E20: The Lotus E20 is a Formula One racing car designed and produced by the Enstone-based Lotus F1 Team for the 2012 Formula One season.  The E20 was the twentieth Formula One car to be designed at Enstone since 1992, and was named in tribute to the contribution made by the facility and its personnel in their twenty-year history.  The car was also the first from Enstone to carry the Lotus name, since the team ceased using the Renault name following their renaming from Lotus Renault GP at the end of 2011.  The team continued to use Renault engines for the car.  The car, which was launched by the team on its website on 5 February 2012, was driven by 2007 World Drivers' Champion Kimi Räikkönen and 2011 GP2 Series champion Romain Grosjean, both of whom returned to Formula One after a two-year absence.\n\nToleman TG183: The Toleman TG183 was a Formula One racing car designed by Rory Byrne and built and raced by Toleman Motorsport.  The car first raced in the last two races of the 1982 Formula One season driven by Derek Warwick.  In the 1983 Formula One season an updated version of the car, designated TG183B, was introduced and Warwick was joined at Toleman by Bruno Giacomelli.  The car also raced in the first four races of the 1984 Formula One season when Ayrton Senna made his debut in the Formula 1 championship alongside former FIM 350cc and Formula 750 motorcycle World Champion Johnny Cecotto from Venezuela.\n\nLucas di Grassi: Lucas Tucci di Grassi (born 11 August 1984) is a Brazilian professional racing driver who currently competes for Audi Sport ABT in Formula E and is the 2016-17 World Champion.  In 2014, di Grassi became the first driver in motorsport history to win a motor race in an all-electric single-seater racing car at the 2014 Beijing ePrix.  He was also runner-up in the 2007 GP2 Series, 2015-16 FIA Formula E and 2016 FIA World Endurance Championship, and drove for Virgin Racing in the 2010 Formula One season.\n\nVirgin VR-01: The Virgin VR-01 was a Formula One motor racing car designed by Nick Wirth for Virgin Racing in the season.  It was driven by former Toyota driver Timo Glock and Brazilian ex-GP2 driver Lucas di Grassi.  The car was the first Formula One racing car designed entirely with computational fluid dynamics.  The car was due to be launched online through the official team website on 3 February 2010, but technical issues prevented the live internet broadcast from taking place.\n\nInstituto Ayrton Senna: The Instituto Ayrton Senna (English: Ayrton Senna Institute; abbreviated IAS) is a Brazilian non-governmental organization founded by Ayrton Senna's family in November 1994, six months after Senna's death.  It is presided by Viviane Senna da Silva Lalli, Ayrton's sister and mother of Formula One driver Bruno Senna.\n\nViviane Senna: Viviane Senna da Silva Lalli (born 14 June 1958) is a Brazilian entrepreneur and philanthropist.  She is sister of the racing driver and three-times Formula 1 world champion Ayrton Senna (1960–1994), and mother of the driver Bruno Senna (1983–).\n\nQuestion: What was the name of the Formula One racing car launched in February 2012 driven by Brazilian professional racing driver Bruno Senna?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"car_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Formula One racing car.\"\n    },\n    \"car_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"launch_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the car was launched.\"\n        },\n        \"season\": {\n          \"type\": \"integer\",\n          \"description\": \"The Formula One season the car competed in.\"\n        },\n        \"team_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team that designed the car.\"\n        }\n      },\n      \"required\": [\n        \"launch_date\",\n        \"season\",\n        \"team_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"driver_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"driver_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the driver.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the driver.\"\n        }\n      },\n      \"required\": [\n        \"driver_name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"car_name\",\n    \"car_details\",\n    \"driver_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "car_name": {
        "type": "string",
        "description": "The name of the Formula One racing car."
      },
      "car_details": {
        "type": "object",
        "properties": {
          "launch_date": {
            "type": "string",
            "description": "The date the car was launched."
          },
          "season": {
            "type": "integer",
            "description": "The Formula One season the car competed in."
          },
          "team_name": {
            "type": "string",
            "description": "The name of the team that designed the car."
          }
        },
        "required": [
          "launch_date",
          "season",
          "team_name"
        ],
        "additionalProperties": false
      },
      "driver_details": {
        "type": "object",
        "properties": {
          "driver_name": {
            "type": "string",
            "description": "The name of the driver."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the driver."
          }
        },
        "required": [
          "driver_name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "car_name",
      "car_details",
      "driver_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
