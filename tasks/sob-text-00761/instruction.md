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
Porsche Engineering: Porsche Engineering (Porsche Engineering Group GmbH) was established in 2001 as a wholly owned subsidiary of Porsche AG, with headquarters in Weissach, and traces its history back to 1931 when Porsche created its first engineering office subsidiary.  Porsche Engineering Group has been re-organized into Porsche Consulting (subsidiary of Porsche AG) and Porsche Engineering (subsidiary of Porsche SE).

Hennessey Venom GT: The Hennessey Venom GT is a high performance sports car manufactured by Texas-based Hennessey Performance Engineering.  The Venom is a modified version of a British sports car, the Lotus Exige.

Hennessey Viper Venom 1000 Twin Turbo: The Hennessey Viper Venom 1000 Twin Turbo is an upgraded version of the Dodge Viper offered for sale as a whole car or as an upgrade by Hennessey Performance Engineering, also known as HPE.  It comes in two variants, a coupe and a convertible.  It has a theoretical maximum production run of 24 vehicles.  HPE claims the Venom 1000 Twin Turbo is "The fastest and most powerful limited-edition street car in the world."

1st Assault Brigade Royal Engineers: The 1st Assault Brigade Royal Engineers was a specialisied armoured formation of the British Army active in World War II.  It was formed in mid-1943 and its structure was three Assault Regiments of the Royal Engineers.  It was assigned to the 79th Armoured Division in preparation for the Normandy invasion of 6 June 1944.  The unit comprised armoured vehicles modified for specialist roles (also known as Hobart's Funnies), intended to assist with the landing phase of the operation.

Hennessey Performance Engineering: Hennessey Performance Engineering is an American tuning house specializing in modifying sports and super cars from several brands like Ferrari, Porsche, McLaren, Chevrolet, Dodge, Cadillac, Lotus, Jeep, Ford, GMC, Lincoln and Lexus.  Established in 1991 by John Hennessey, their main facility is located west of Houston, Texas.  This firm focuses on mechanical component modification for creating high-powered cars.  Besides performance automobiles, they also tune sport utility vehicles such as Ford Raptors and Jeep Cherokees.  They also work on luxury cars like Bentleys and muscle cars like Dodge Charger and Challenger.

Hennessey Venom F5: The Hennessey Venom F5 is a proposed high-performance sports car manufactured by Texas-based Hennessey Special Vehicles, a division of Hennessey Performance Engineering.  This car will be the first in-house constructed vehicle from the tuner company.

Jeep: Jeep is a brand of American automobiles that is a division of FCA US LLC (formerly Chrysler Group, LLC), a wholly owned subsidiary of Fiat Chrysler Automobiles.  The former Chrysler Corporation acquired the Jeep brand, along with the remaining assets of its owner American Motors, in 1987.  The division is headquartered in Toledo, Ohio.  Jeep's current product range consists solely of sport utility vehicles and off-road vehicles, but has also included pickup trucks in the past.

79th Armoured Division (United Kingdom): The 79th Armoured Division was a specialist armoured division of the British Army created during World War II.  The division was created as part of the preparations for the Normandy invasion on 6 June 1944, D-Day.  The division operated armoured vehicles modified for specialist roles, intended to assist with the landings on the beaches.  The division remained in action during the North-west European Campaign, providing specialised support during assaults to the 21st Army Group and, occasionally, to American units.

FSE Engineering Group: FSE Engineering Group Ltd (FSEE) (Chinese: 豐盛創建機電 工程有限公司)is the Electrical Engineering & Mechanical Engineering business company.  It was established in 1997 when its predecessor, NWS Engineering Group Ltd, sold out to Fung Seng Enterprises, It become a part of enterprise.  Now, FSE Engineering Group Ltd (FSEE) is the largest E&M Building Services engineering companies in Hong Kong

Performance engineering: Performance engineering encompasses the techniques applied during a systems development life cycle to ensure the non-functional requirements for performance (such as throughput, latency, or memory usage) will be met.  It may be alternatively referred to as systems performance engineering within systems engineering, and software performance engineering or application performance engineering within software engineering.

Question: What division of Chrysler features vehicles modified by the Hennessey Performance Engineering group?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "modified_by_company": {
      "type": "string",
      "description": "The name of the engineering group that modifies vehicles."
    },
    "modified_vehicles_brand": {
      "type": "string",
      "description": "The brand of vehicles that are modified."
    },
    "parent_company_of_brand": {
      "type": "string",
      "description": "The parent company of the modified vehicle brand."
    },
    "brand_relationship_to_parent": {
      "type": "string",
      "description": "Describes the relationship of the brand to its parent company."
    }
  },
  "required": [
    "modified_by_company",
    "modified_vehicles_brand",
    "parent_company_of_brand",
    "brand_relationship_to_parent"
  ],
  "additionalProperties": false
}
