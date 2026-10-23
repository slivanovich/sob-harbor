{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDutton Cars: Dutton Cars, based in Worthing, Sussex, England, was a maker of kit cars between 1970 and 1989.  In terms of numbers of kits produced, it was the largest kit car manufacturer in the world.\n\nAries Motorsport: Aries MotorSport is a British kit car manufacturer based in Cardiff South Wales.  The company was created in April 2007 and is the distributor of the Stuart Taylor Locost and LocoBlade kits.  These are Lotus Seven replicas based either in car or bike engines.\n\nDiocesan Native Female Training School: Diocesan Native Female Training School (DNFTS, ) was a school under the Anglican Church of Hong Kong in the 19th century, founded in 1860 and closed down in 1868.  Its premises now belong to today's Bonham Road Government Primary School().  In 1869, another institution called Diocesan Home and Orphanage (DHO, later renamed Diocesan School and Orphanage, and now known as Diocesan Boys' School) was founded in the same place.  Due to the obvious differences in founding groups, vision of education, personnel arrangement and students’ background, DNFTS has been regarded only as a forerunner, and called ‘the First Foundation’ by DHO and later DBS.  Using 1869 as its founding year, DBS calls itself ‘the Second Foundation’.  As for Diocesan Girls' School, founded in Rose Villas near DSO in 1899, it claims to be the successor of DNFTS and traces the founding year back to 1860.\n\nRaw Striker: Raw Striker Ltd. (formerly Raw Engineering) is a kit car manufacturer established in 1999.  In 2002 they acquired the rights to the Sylva Striker kit car, which they have since modified and on which the Fulcrum is based.  It is based in Shelwick, just north of Hereford.  In August 2010 the company was purchased by Callum and Jeremy Bulmer from the original owner Mel Coppock.\n\nSylva Leader: The 2 seat Sylva Leader was derived from the Sylva Star kit car.  Slightly less extreme styling led to better sales.  Based on the ever popular Lotus 7 style of car there were many similar designs over the years.\n\nMarc Nordon Racing: Marc Nordon Racing (MNR Ltd) is a kit car manufacturer specialising in bike (motor cycle) engined cars or BECs and in particular, Lotus Seven Replicas.  They are based in Harrogate, England.\n\nSpex Design Corporation: Spex Design Corporation was a kit car manufacturer based in Montreal, Quebec, Canada.  The company was founded by Paul Deutchman (also known for the T-Rex, Porsche Spexter and Callaway cars like the C7 Corvette and CS Camaro) and Kell Warshaw in 1985.  The company made a kit called \"Spex Elf\" that was somewhere in the middle of a body kit and a kit car based on the first generation (1973-1979) Honda Civic.  By cutting off the roof and side panels and adding a steel subframe and fibreglass body it allowed a quite easy conversion of a Honda Civic into a roadster.  The kit used many parts from the donor Civic, but the front light came from the Honda Accord and the rear light from Mercury Capri.  The company made about 20 kits before selling the molds.\n\nRobin Hood Engineering: Robin Hood Engineering Ltd was a British kit car manufacturer based in Mansfield Woodhouse, Nottinghamshire.  The factory covered 30000 sqft and was on a one and a half acre site.\n\n1998 British Rally Championship: The 1998 Mobil 1 British Rally Championship was won by Manxman Martin Rowe in the Renault Megane Maxi Kit Car ahead of veteran Welsh driver Gwyndaf Evans in the SEAT Ibiza Kit Car and Alister McRae in The Volkswagen Golf Kit Car.  Reigning champion Mark Higgins had a very disappointing season in the new Nissan Almera Kit Car.  The ladies' cup was won by SEAT driver Barbara Armstrong ahead of Ford's Stephanie Simmonite.  The manufacturers' championship was won by Renault.\n\nSylva Autokits: Sylva Autokits is a kit car manufacturer based in Lincolnshire, England.  Sylva was founded in 1981 by Jeremy Phillips and has developed and produced a number of small and lightweight sports cars.  Sylva cars have proven very successful in competition, winning a number of 750 Motor Club Kit Car championships.\n\nQuestion: What is the founding year of this kit car manufacturer based in Lincolnshire, England from which the 2 seat Sylva Leader was derived?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"manufacturer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the kit car manufacturer.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the manufacturer was founded.\"\n        },\n        \"location\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"region\": {\n              \"type\": \"string\",\n              \"description\": \"The region or county where the manufacturer is based.\"\n            },\n            \"country\": {\n              \"type\": \"string\",\n              \"description\": \"The country where the manufacturer is based.\"\n            }\n          },\n          \"required\": [\n            \"region\",\n            \"country\"\n          ],\n          \"additionalProperties\": false\n        },\n        \"founder_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the founder of the manufacturer.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\",\n        \"location\",\n        \"founder_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"product_derived_from\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the kit car model from which the Sylva Leader was derived.\"\n    },\n    \"answer_founding_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The founding year of the identified kit car manufacturer.\"\n    }\n  },\n  \"required\": [\n    \"manufacturer\",\n    \"product_derived_from\",\n    \"answer_founding_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "manufacturer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the kit car manufacturer."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the manufacturer was founded."
          },
          "location": {
            "type": "object",
            "properties": {
              "region": {
                "type": "string",
                "description": "The region or county where the manufacturer is based."
              },
              "country": {
                "type": "string",
                "description": "The country where the manufacturer is based."
              }
            },
            "required": [
              "region",
              "country"
            ],
            "additionalProperties": false
          },
          "founder_name": {
            "type": "string",
            "description": "The name of the founder of the manufacturer."
          }
        },
        "required": [
          "name",
          "founding_year",
          "location",
          "founder_name"
        ],
        "additionalProperties": false
      },
      "product_derived_from": {
        "type": "string",
        "description": "The name of the kit car model from which the Sylva Leader was derived."
      },
      "answer_founding_year": {
        "type": "integer",
        "description": "The founding year of the identified kit car manufacturer."
      }
    },
    "required": [
      "manufacturer",
      "product_derived_from",
      "answer_founding_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
