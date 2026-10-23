{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHero Hunk: The Hero Hunk is a 150 cc motorcycle launched by Hero Honda in October 2007.  It is offered in two variants, kick-start and self-start.  The new 2011 model is offered with either rear disc brake, or rear drum brake.\n\nSuzuki FXR150: The Suzuki FXR150 is a sport bike made in Malaysia by Lion Suzuki Motor.  It is powered by a four-valve, DOHC four-stroke 147 cc single-cylinder engine.  Lion Suzuki Motor produces the motorcycle with 75% local content.  It replaced the slightly larger in size two-stroke Suzuki RG150/RGV150.  It features a full digital dash which displayed fuel, RPM, speed and gear.  The frame is made of box cut steel and had a banana-shaped rear swingarm.  It has a single mono shock on the rear with a single disc brake.  The front suspension is a traditional telescopic fork also with a single disc brake.  The wheels are five-spoke Enkei mag type wheels.  The engine has a six-speed close-ratio gearbox with both kick-start and electric start systems.  The engine features a small oil cooler to aid cooling (the Suzuki advanced cooling system).  It also features the TWIRL system at the combustion chamber.\n\nHonda CB360: The Honda CB360 is a twin cylinder four-stroke motorcycle produced by Honda from 1974 to 1976.  It succeeded the Honda CB350 and provided an alternative to the four cylinder CB350F and CB400F.  The CB360 was a new design.  The 356 cc engine was tuned for broad range torque, and drove the rear wheel through a six-speed gearbox.  The base CB360 model was equipped with front and rear drum brakes, while the CB360t version had a front hydraulic disc brake.\n\nHonda Bali (SJ 100): The Honda Bali is a 100 cc two-stroke twist and go scooter from Honda.  The scooter has self-starter and autolub system to mix two-stroke oil with fuel.  The top speed with 85 kg load is around 80 km/h.  Front brake is disc while rear is drum.\n\nSuper Splendor: The SuperSplendor is a standard lightweight motorcycle produced since 2005 by Hero Honda.  Since it was released, this motorcycle has gone through numerous changes.  It is the ultimate edition in the series Hero Honda Splendor manufactured by Hero Honda.  Later, it was re-modeled by Hero MotoCorp, giving it new functions like digital speedometer, a front disc brake replacing the drum brake, and a new look with alloy wheels.\n\nHayes Brake: Hayes Brake is a Milwaukee, Wisconsin designer and manufacturer of disc brakes and disc brake systems for non-automotive applications, including Hayes Disc Brake specialising in disc brakes for bikes.  In 2005 the company's nine-member management team bought Hayes Brake with Nautic Partners, a private equity firm, and renamed the company HB Performance Systems Inc.\n\nAusco Lambert disc brake: The Ausco-Lambert disc brake is an unusual brake where an axially-expanding shoe assembly is sandwiched between two linked rotating discs.  It may be thought of as an \"inside out\" disc brake: instead of pads pinching a disc, the pads expand inside a hollow disc.\n\nDisc brake: A disc brake is a type of brake that uses calipers to squeeze pairs of pads against a rotor (or \"disc\") in order to create friction that retards the rotation of a shaft, such as a vehicle axle, either to reduce its rotational speed or to hold it stationary.  The energy of motion is converted into waste heat which must be dispersed.  Hydraulic disc brakes are the most commonly used form of brake for motor vehicles but the principles of a disc brake are applicable to almost any rotating shaft.\n\nHonda CB250RS: The Honda CB250RS is a 250 cc motorcycle designed for road use.  It was produced until the mid-1980s.  It has a high-compression four-stroke, four-valve, air-cooled, single-cylinder engine, which was an upgrade of the engine built for the earlier XL250S trail bike.  The RS is known for its slim build, with a dry weight of only 128 kg, and nimble handling.  The engine featured counter rotating balancers, which reduced vibration and allowed a lighter frame.  Further weight savings were achieved by making the engine a stressed component.  Early models were kick-started (with an automatic decompression lever), while later Deluxe models (designated RS-D / RSZ) came with electric start and different paintwork.  The bike has a front disc brake and rear drum brake, and while it had only a single cylinder, it had twin exhausts; one for each port.\n\nHonda CM450A: The CM450A was a motorcycle made by Honda in 1982 and 1983.  It was based on the CB400 and CM400 models (1978-1981), especially the CM400A Hondamatic (1980-1981).  It had a 447 cc SOHC parallel twin engine with two carburettors and a 2-speed transmission with a torque converter.  It was not a full automatic, however, because the rider had to manually shift between low and high.  It is called automatic because there is no clutch required due to the torque converter, and shared the Hondamatic trade name with Honda cars that had true automatic transmissions.  The chain-driven CM450A had a top speed of 90 mph and weighed 413 lb .  Both models had a front disc brake and a rear drum brake.  The suspension consisted of two shocks in the rear and telescoping shock-absorbing front forks.  The gas tank had a 3.4 gal capacity.  The exhaust was routed through a separate pipe and baffle on each side of the motorcycle, although both exhaust pipes shared a plenum under the motor.  It had an electric start with a kick start as well.\n\nQuestion: What kind of rate does Honda Bali and Disc brake have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_rate_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of rate that Honda Bali and Disc brake have in common.\"\n    },\n    \"honda_bali_rate_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"rate_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the rate for Honda Bali.\"\n        },\n        \"rate_value\": {\n          \"type\": \"integer\",\n          \"description\": \"The numerical value of the rate for Honda Bali.\"\n        },\n        \"rate_unit\": {\n          \"type\": \"string\",\n          \"description\": \"The unit of the rate for Honda Bali.\"\n        }\n      },\n      \"required\": [\n        \"rate_description\",\n        \"rate_value\",\n        \"rate_unit\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"disc_brake_rate_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"rate_description\": {\n          \"type\": \"string\",\n          \"description\": \"Description of the rate related to Disc brake's function.\"\n        },\n        \"action_on_rate\": {\n          \"type\": \"string\",\n          \"description\": \"The action a disc brake performs on the related rate.\"\n        }\n      },\n      \"required\": [\n        \"rate_description\",\n        \"action_on_rate\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"common_rate_type\",\n    \"honda_bali_rate_details\",\n    \"disc_brake_rate_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_rate_type": {
        "type": "string",
        "description": "The type of rate that Honda Bali and Disc brake have in common."
      },
      "honda_bali_rate_details": {
        "type": "object",
        "properties": {
          "rate_description": {
            "type": "string",
            "description": "Description of the rate for Honda Bali."
          },
          "rate_value": {
            "type": "integer",
            "description": "The numerical value of the rate for Honda Bali."
          },
          "rate_unit": {
            "type": "string",
            "description": "The unit of the rate for Honda Bali."
          }
        },
        "required": [
          "rate_description",
          "rate_value",
          "rate_unit"
        ],
        "additionalProperties": false
      },
      "disc_brake_rate_details": {
        "type": "object",
        "properties": {
          "rate_description": {
            "type": "string",
            "description": "Description of the rate related to Disc brake's function."
          },
          "action_on_rate": {
            "type": "string",
            "description": "The action a disc brake performs on the related rate."
          }
        },
        "required": [
          "rate_description",
          "action_on_rate"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "common_rate_type",
      "honda_bali_rate_details",
      "disc_brake_rate_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
