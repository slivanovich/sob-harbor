{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGolden Arrow (car): Golden Arrow was a land speed record racer built in Britain to regain the world land speed record from USA.  Henry Segrave drove the car at Daytona Beach and exceeded the previous record by 24 mph or 39 km/h.\n\nCraig Breedlove: Craig Breedlove (born March 23, 1937) is an American professional race car driver and a five-time world land speed record holder.  He was the first person in history to reach 500 mi/h , and 600 mi/h , using several turbojet-powered vehicles, all named \"Spirit of America\".\n\nLand speed record: The land speed record (or absolute land speed record) is the highest speed achieved by a person using a vehicle on land.  There is no single body for validation and regulation; in practice the Category C (\"Special Vehicles\") flying start regulations are used, officiated by regional or national organizations under the auspices of the Fédération Internationale de l'Automobile.  The land speed record (LSR) is standardized as the speed over a course of fixed length, averaged over two runs (commonly called \"passes\").  Two runs are required in opposite directions within one hour, and a new record mark must exceed the previous one by at least one percent to be validated.\n\nValerie Thompson: Valerie Thompson (born April 17, 1967) is an American motorcycle drag and land speed racer.  She is a 7-time motorcycle land-speed record holder and charter member of the Mojave Magnum \"200 MPH Club.\"  In 2012, she was selected to drive the North American Eagle Project jet car in which she will be attempting to break the land speed record for a woman (currently 512 mph).  Valerie was later removed from this project and replaced by a different female rider, Jessi Combs.  This began the downward spiral of her career, including the loss of Harley Davidson and Monster Energy as race sponsors.\n\nBloodhound SSC: Bloodhound SSC is a British supersonic land vehicle currently in development.  Its goal is to match or exceed 1000 mph achieving a new world land speed record.  The pencil-shaped car, powered by a jet engine and a rocket engine is designed to reach 1050 mph .  It is being developed and built with the intention of breaking the land speed record by 33%, the largest ever margin.\n\nArt Arfons: Arthur Eugene \"Art\" Arfons (February 3, 1926 – December 3, 2007) was the world land speed record holder three times from 1964 to 1965 with his \"Green Monster\" series of jet-powered cars, after a series of \"Green Monster\" piston-engine and jet-engined dragsters.  He subsequently went on to field a succession of \"Green Monster\" turbine-engined pulling tractors, before returning to land speed record racing.  He was announced as a 2008 inductee in the International Motorsports Hall of Fame three days after his death.\n\nAndy Green: Wing Commander Andy D. Green OBE (born 30 July 1962) is a British Royal Air Force fighter pilot and World Land Speed Record holder.\n\nErnest Eldridge: Ernest Arthur Douglas Eldridge (18 July 1897 – 27 October 1937) was a British racing car driver who broke the world land speed record in 1924.  His was the last land speed record set on an open road.\n\nDorothy Levitt: Dorothy Elizabeth Levitt, (born Elizabeth Levi; 5 January 1882, died 17 May 1922) was the first British woman racing driver, holder of the world's first water speed record, the women's world land speed record holder, and an author.  She was a pioneer of female independence and female motoring, and taught Queen Alexandra and the Royal Princesses how to drive.  In 1905 she established the record for the longest drive achieved by a lady driver by driving a De Dion-Bouton from London to Liverpool and back over two days, receiving the soubriquets in the press of the Fastest Girl on Earth, and the Champion Lady Motorist of the World.\n\nSpirit of America (automobile): Spirit of America is the trademarked name used by Craig Breedlove for his land speed record-setting vehicles.\n\nQuestion: what is the trademarked name for the vehicles of the five time world land speed record holder?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"record_holder_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual who holds the land speed record.\"\n    },\n    \"number_of_records\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of times the individual held the world land speed record.\"\n    },\n    \"vehicle_trademarked_name\": {\n      \"type\": \"string\",\n      \"description\": \"The trademarked name used for the record holder's vehicles.\"\n    }\n  },\n  \"required\": [\n    \"record_holder_name\",\n    \"number_of_records\",\n    \"vehicle_trademarked_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "record_holder_name": {
        "type": "string",
        "description": "The name of the individual who holds the land speed record."
      },
      "number_of_records": {
        "type": "integer",
        "description": "The number of times the individual held the world land speed record."
      },
      "vehicle_trademarked_name": {
        "type": "string",
        "description": "The trademarked name used for the record holder's vehicles."
      }
    },
    "required": [
      "record_holder_name",
      "number_of_records",
      "vehicle_trademarked_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
