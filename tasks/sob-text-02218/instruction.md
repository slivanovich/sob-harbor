{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJeep Wagoneer (SJ): The Jeep Wagoneer is the first luxury 4x4, sold and produced for Jeep through numerous marques from 1963 to 1991.  A \"sport utility vehicle\" (SUV) for decades before the term was coined, the 4WD Wagoneer saw only minor mechanical changes during its 28-year plus production run, the third longest in U.S. automotive history.\n\nJeep Cherokee (SJ): The SJ series Jeep Cherokee is a full-size SUV that was produced from 1974 through 1983 by Jeep.  It was based on the Wagoneer that was originally designed by Brooks Stevens in 1963.\n\nJeep Liberty (KK): The Jeep Liberty (KK), or Jeep Cherokee (KK) outside North America, is a compact SUV that was produced by Jeep.  Introduced for the 2008 model year as a successor for the first generation Liberty.  The Liberty featured unibody-construction.  It was assembled at the Toledo North Assembly Plant in the United States, as well as in other countries including Egypt and Venezuela.  In 2010 estimates by Jeep were that 70% of Liberty buyers were new to the marque.  The second generation Liberty ceased production on August 16, 2012.  For its followup, the name of Liberty was retired; the next generation restored the name of \"Cherokee\".  The model remains on sale in Venezuela as of early 2016 having yet to be replaced by FCA Venezuela with the KL model Cherokee.\n\nJeep Cherokee: The Jeep Cherokee is a line of vehicles sold by Jeep under various vehicle classes.  Originally sold as a variant of the popular Jeep Wagoneer, the Cherokee has evolved from a full-size SUV to one of the first compact SUVs and eventually into its current incarnation as a crossover SUV.  The nameplate has been in continuous use in some form since 1974 and also spawned Jeep's most successful vehicle, the Jeep Grand Cherokee, which was originally slated to be part of the Cherokee's lineup.  The vehicle is named after the Cherokee tribe of Native Americans.\n\nRichard A. Teague: Richard A. (Dick) Teague (December 26, 1923 – May 5, 1991), born in Los Angeles, California, was an American industrial designer in the North American automotive industry.  He held automotive design positions at General Motors, Packard, and Chrysler before becoming Vice President of Design for American Motors Corporation (AMC), and designed several notable show cars and production vehicles including AMC's Pacer, Gremlin and Hornet models, as well as the Jeep Cherokee XJ and even had a hand in designing/assisted in the designing of later cars for Chrysler after American Motor's buyout such as the Jeep Grand Cherokee and Neon.\n\nJeep Liberty (KJ): The Jeep Liberty (KJ), or Jeep Cherokee (KJ) outside North America, is a compact SUV that was produced by Jeep and designed by Bob Boniface through early 1998.  Introduced in May 2001 for the 2002 model year as a replacement for the Cherokee (XJ), the Liberty was priced between the Wrangler and Grand Cherokee.  It was the smallest of the 4-door Jeep SUVs up until the car platform based 4-door Compass and Patriot arrived for 2007.  The Liberty featured unibody-construction.  It was assembled at the Toledo North Assembly Plant in the United States, as well as in other countries including Egypt and Venezuela.\n\nJeep Liberty: The Jeep Liberty, or Jeep Cherokee (KJ/KK) outside North America, is a compact SUV that was produced by Jeep for the model years 2002–2012.  Introduced as a replacement for the Cherokee (XJ), the Liberty was priced between the Wrangler and Grand Cherokee.  It was the smallest of the 4-door Jeep SUVs until the car based 4-door Compass and Patriot arrived for 2007.  The Liberty featured unibody-construction.  It was assembled at the Toledo North Assembly Plant in the United States, as well as in other countries including Egypt and Venezuela.  The Liberty ceased production on August 16, 2012.  The next generation restored the previous nameplate of Jeep Cherokee that was always used outside of North America.\n\nJeep Cherokee (KL): The Jeep Cherokee (KL) is a mid-size crossover SUV produced by Jeep.  It was introduced for the 2014 model year at the 2013 New York International Auto Show and the sales started in November 2013.  The Cherokee is the first Jeep vehicle to be built on the Fiat Compact/Compact U.S. Wide platform, co-developed by Chrysler and Fiat.  The Jeep Cherokee is built at Belvidere Assembly Plant in Belvidere, Illinois.\n\nDisappearance of Leah Roberts: On March 18, 2000, joggers along a road near the Mount Baker Highway in Whatcom County, Washington, United States, reported seeing a wrecked vehicle at the bottom of an embankment near Canyon Creek, a tributary of the North Fork of the Nooksack River.  Deputy sheriffs found a white 1993 Jeep Cherokee with North Carolina license plates.  They traced the car to Leah Roberts (born July 23, 1976) who had abruptly left her home in Durham, North Carolina, nine days earlier.  A man called police claiming his wife saw her in an Everett, Washington, gas station, disoriented, shortly after the car was found; she has otherwise remained missing.\n\nJeep Cherokee (XJ): The Jeep Cherokee (XJ) is a sport utility vehicle that was manufactured and marketed by Jeep from 1983 to 2001.  Sharing the name of the original full-size SJ model, but without a traditional body-on-frame chassis, the XJ instead featured a light-weight unibody design, The models were originally marketed as Sportwagons and became the precursor to the modern sport utility vehicle (SUV) as that term was not yet in use.\n\nQuestion: Jeep Cherokee was a variant of a popular car that was sold between what years ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"original_car_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the popular car that the Jeep Cherokee was originally a variant of.\"\n    },\n    \"cherokee_relationship\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the relationship of the Cherokee to the original car.\"\n    },\n    \"production_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The start year of the original car's production.\"\n    },\n    \"production_end_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The end year of the original car's production.\"\n    },\n    \"production_duration_years\": {\n      \"type\": \"integer\",\n      \"description\": \"The total number of years the original car was in production.\"\n    }\n  },\n  \"required\": [\n    \"original_car_name\",\n    \"cherokee_relationship\",\n    \"production_start_year\",\n    \"production_end_year\",\n    \"production_duration_years\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "original_car_name": {
        "type": "string",
        "description": "The name of the popular car that the Jeep Cherokee was originally a variant of."
      },
      "cherokee_relationship": {
        "type": "string",
        "description": "Describes the relationship of the Cherokee to the original car."
      },
      "production_start_year": {
        "type": "integer",
        "description": "The start year of the original car's production."
      },
      "production_end_year": {
        "type": "integer",
        "description": "The end year of the original car's production."
      },
      "production_duration_years": {
        "type": "integer",
        "description": "The total number of years the original car was in production."
      }
    },
    "required": [
      "original_car_name",
      "cherokee_relationship",
      "production_start_year",
      "production_end_year",
      "production_duration_years"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
