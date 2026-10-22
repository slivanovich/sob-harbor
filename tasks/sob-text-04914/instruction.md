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
Bullhorn, Inc.: Bullhorn is a cloud computing company headquartered inBoston, Massachusetts.  The company provides customer relationship management (CRM) and operations software for the staffing industry.  As of 2017, the company reported more than 7,000 customers in more than 150 countries.  Besides its Boston headquarters, the company has operations in St. Louis, London, Vancouver and Sydney.

ServiceNow: ServiceNow, Inc. is a cloud computing company headquartered in Santa Clara, California.  It was founded in 2004 by Fred Luddy, the previous CTO of software companies Peregrine Systems and Remedy Corporation.  ServiceNow is listed on the New York Stock Exchange and is a constituent of the Russell 1000 index.

Salesforce.com: salesforce.com, inc. (styled in its logo as sales"ƒ"orce; abbreviated usually as "SF" or "SFDC") is an American cloud computing company headquartered in San Francisco, California.  Though its revenue comes from a customer relationship management (CRM) product, Salesforce also capitalizes on commercial applications of social networking through acquisition.  As of early 2016, it is one of the most highly valued American cloud computing companies with a market capitalization above $61 billion.  In August 2017, Salesforce announced that it had breached the $10 billion revenue run rate becoming the first enterprise cloud company to do so.

New South Wales: New South Wales (abbreviated as NSW) is a state on the east coast of :Australia.  It borders Queensland to the north, Victoria to the south, and South Australia to the west.  Its coast borders the Tasman Sea to the east.  The Australian Capital Territory is an enclave within the state.  New South Wales' state capital is Sydney, which is also Australia's most populous city.  In March 2014 , the estimated population of New South Wales was 7.5 million, making it Australia's most populous state.  Just under two-thirds of the state's population, 4.67 million, live in the Greater Sydney area.  Inhabitants of New South Wales are referred to as "New South Welshmen".

Velocify: Velocify, Inc. is a cloud computing company headquartered in El Segundo, California that provides cloud-based intelligent sales automation software designed for fast-paced sales environments.

Batoi Systems: Batoi Systems Private Limited is a global cloud computing company headquartered in Bhubaneswar, India.  Batoi has been profiled as one of the top 20 cloud computing companies by silicon review magazine and profiled among the 50 Most Promising Big Data Companies by CIO Review

Appland: Appland is a cloud computing company headquartered in Gothenburg, Sweden, that develops white label app store solutions for mobile operators, mobile devices, online communities, smart TVs, connected vehicles and internet of things.

Alibaba Cloud: Alibaba Cloud (; literally: Ali Cloud; formerly: Aliyun), a subsidiary of Alibaba Group, is a global cloud computing company headquartered in Hangzhou.  Alibaba Cloud provides a suite of cloud computing services that covers elastic computing, object storage, relational database, big data analysis, and artificial intelligence in eight geographical regions around the globe.  Established in September 2009, Alibaba Cloud began as a private cloud to serve the internal demands of Alibaba's e-commerce businesses, including Taobao, Tmall, and Alipay.

Rollbase: Rollbase is a platform as a service (PaaS) software solution.  It was founded by the eponymous software vendor based in Saratoga, California acquired by Progress Software (Nasdaq: PRGS) in June 2013, a global cloud computing company headquartered in Bedford, Massachusetts.  Founded in 2007, the Rollbase platform allows users to create Software as a Service (SaaS) business applications using point and click, drag and drop tools in a standard web browser with minimal programming.  In April 2013 Rollbase was recognized by Gartner as a "2013 Cool Vendor in PaaS".

Sydney: Sydney ( ) is the state capital of New South Wales and the most populous city in Australia and Oceania.  Located on Australia's east coast, the metropolis surrounds the world's largest natural harbour and sprawls about 70 km on its periphery towards the Blue Mountains to the west, Hawkesbury to the north and Macarthur to the south.  Sydney is made up of 658 suburbs, 40 local government areas and 15 contiguous regions.  Residents of the city are known as "Sydneysiders".  As at June 2016 Sydney's estimated population was 5,029,768.

Question: Bullhorn is a cloud computing company headquartered inBoston, Massachusetts, besides its Boston headquarters, the company has operations in St. Louis, London, Vancouver and which state capital of New South Wales and the most populous city in Australia and Oceania?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company."
    },
    "headquarters_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the company is headquartered."
        },
        "state": {
          "type": "string",
          "description": "The state where the company is headquartered."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "additional_operation_locations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other cities where the company has operations, excluding the headquarters."
    },
    "identified_location": {
      "type": "object",
      "properties": {
        "city_name": {
          "type": "string",
          "description": "The name of the city that matches the description in the question."
        },
        "is_state_capital_of": {
          "type": "string",
          "description": "The state or territory for which the city is the capital."
        },
        "is_most_populous_in_australia_oceania": {
          "type": "boolean",
          "description": "Indicates if the city is the most populous in Australia and Oceania."
        },
        "population_details": {
          "type": "object",
          "properties": {
            "count": {
              "type": "integer",
              "description": "The estimated population of the city."
            },
            "as_of_date": {
              "type": "string",
              "description": "The date as of which the population count was estimated."
            }
          },
          "required": [
            "count",
            "as_of_date"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "city_name",
        "is_state_capital_of",
        "is_most_populous_in_australia_oceania",
        "population_details"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "headquarters_location",
    "additional_operation_locations",
    "identified_location"
  ],
  "additionalProperties": false
}
