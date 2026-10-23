{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAmerican Airlines C.R. Smith Museum: The American Airlines C.R. Smith Museum (CRSM) is located on the campus of the American Airlines Flight Academy, which is situated at the southern end of DFW International Airport and in close proximity to the world headquarters of American Airlines.  The location is at the midpoint between the city centers of Dallas and Fort Worth near the intersection of Highways 183 and 360.  The CRSM has an exhibit gallery of approximately 25000 sqft and a 10000 sqft hangar that houses the Flagship Knoxville, a fully restored DC-3 aircraft.  The museum also includes a 1500 sqft gift shop and a large-format theatre similar to IMAX.\n\nPSA Airlines: PSA Airlines, Inc. is an American regional airline headquartered at Dayton International Airport in Vandalia, Ohio, that flies under the American Eagle brand for American Airlines.  PSA is a wholly owned subsidiary of American Airlines Group.  PSA has crew bases in Washington, D.C.; Knoxville, Tennessee; Charlotte, North Carolina; Cincinnati, Ohio; and Dayton, Ohio.  It has maintenance bases in Charlotte, North Carolina; Cincinnati, Ohio; Dayton, Ohio and at the Akron–Canton Airport in Green, Ohio.\n\nAmerican Airlines Group: American Airlines Group, Inc. is an American publicly traded airline holding company headquartered in Fort Worth, Texas.  It was formed December 9, 2013, in the merger of AMR Corporation, the parent company of American Airlines, and US Airways Group, the parent company of US Airways.  The airline groups together form the largest airline in the world, with more than 6,700 daily flights to 336 locations in 56 countries worldwide, about $40 billion in operating revenue, over 100,000 employees, and plans to take delivery of 607 new aircraft, including 517 narrowbody aircraft and 90 widebody international aircraft.  The integration of American Airlines and US Airways was completed when the Federal Aviation Administration granted a single operating certificate for both carriers on April 8, 2015.\n\nAMR Corporation: AMR Corporation was a commercial aviation business and airline holding company based in Fort Worth, Texas, which was the parent company of American Airlines, American Eagle Airlines, AmericanConnection and Executive Airlines.  AMR filed for Chapter 11 bankruptcy in November 2011, and merged with US Airways Group on December 9, 2013 to form American Airlines Group, Inc.\n\nAmerican Eagle (airline brand): American Eagle is an American brand name for the regional branch of American Airlines, under which ten individual regional airlines operate short- and medium-haul feeder flights.  Three of these airlines, Envoy Air (formerly American Eagle Airlines), Piedmont Airlines and PSA Airlines, are wholly owned subsidiaries of American Airlines Group.  Just like the regional brands of the other two major airlines (Delta Connection and United Express), American Airlines' regional brand accounts for more than 60% of American Airlines flights.\n\nPedro Fábregas: Pedro Fábregas (born 12 April 1965) is an officer at American Airlines Group, the parent company of American Airlines, US Airways and Envoy Air.  Pedro Fábregas was named president and chief executive officer of Envoy Air Airlines in December 2013.  At Envoy Air, Fábregas oversees one of the world's largest regional airlines, with more than 14,000 employees and operating more than 220 regional aircraft on approximately 1,400 daily flights to nearly 150 cities throughout the United States, Canada, the Bahamas, Mexico and the Caribbean.\n\nIllumina (company): Illumina, Inc. is an American company incorporated in April 1998 that develops, manufactures and markets integrated systems for the analysis of genetic variation and biological function.  The company provides a line of products and services that serve the sequencing, genotyping and gene expression and proteomics markets.  Its headquarters are located in San Diego, California.\n\nThomas W. Horton: Thomas W. Horton (born 05/24/1961) was the Chairman, President, and Chief Executive Officer of AMR Corporation until it merged with US Airways Group to form American Airlines Group, Inc. and was the Chairman of American Airlines Group, Inc. and American Airlines.  He also served as Chairman of oneworld, the global airline alliance, until March 2014.\n\nDoug Parker: William Douglas \"'Doug\" Parker is an American businessman who is the current Chairman and CEO of American Airlines Group, Inc., the parent company of American Airlines.\n\nEnvoy Air: Envoy Air Inc. (formerly American Eagle Airlines) is an air carrier headquartered in Irving, Texas, in the Dallas-Fort Worth metroplex.  It is a wholly owned subsidiary of American Airlines Group that, along with several carriers outside the group, feeds the American Airlines route network under the American Eagle brand.  With over 1,800 flights a day, serving 159 cities across the United States, Canada, Mexico and the Caribbean, Envoy is considered to be the world's largest regional airline system.  Envoy is an affiliate member of the Oneworld airline alliance.\n\nQuestion: Which company headquarters is located in Texas, American Airlines Group or Illumina?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"companies_evaluated\": {\n      \"type\": \"array\",\n      \"description\": \"List of companies mentioned in the question with their headquarters information.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"company_name\": {\n            \"type\": \"string\",\n            \"description\": \"Name of the company.\"\n          },\n          \"headquarters_location\": {\n            \"type\": \"string\",\n            \"description\": \"The city and state where the company's headquarters is located.\"\n          }\n        },\n        \"required\": [\n          \"company_name\",\n          \"headquarters_location\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"company_with_texas_headquarters\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company identified as having its headquarters in Texas.\"\n    },\n    \"is_question_answered\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if a company with Texas headquarters was found, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"companies_evaluated\",\n    \"company_with_texas_headquarters\",\n    \"is_question_answered\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "companies_evaluated": {
        "type": "array",
        "description": "List of companies mentioned in the question with their headquarters information.",
        "items": {
          "type": "object",
          "properties": {
            "company_name": {
              "type": "string",
              "description": "Name of the company."
            },
            "headquarters_location": {
              "type": "string",
              "description": "The city and state where the company's headquarters is located."
            }
          },
          "required": [
            "company_name",
            "headquarters_location"
          ],
          "additionalProperties": false
        }
      },
      "company_with_texas_headquarters": {
        "type": "string",
        "description": "The name of the company identified as having its headquarters in Texas."
      },
      "is_question_answered": {
        "type": "boolean",
        "description": "True if a company with Texas headquarters was found, false otherwise."
      }
    },
    "required": [
      "question_asked",
      "companies_evaluated",
      "company_with_texas_headquarters",
      "is_question_answered"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
