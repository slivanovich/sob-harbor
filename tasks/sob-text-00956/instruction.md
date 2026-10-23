{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAir Wisconsin: Air Wisconsin Airlines is a regional airline based at Appleton International Airport in the town of Greenville, Wisconsin, United States, near Appleton.  Air Wisconsin is the largest privately held regional airline in the United States.  It currently operates regional jet flights as American Eagle under contract to American Airlines via a code sharing agreement, serving cities in the U.S. and Canada with hubs at Boston Logan International Airport (BOS), Charlotte Douglas International Airport (CLT), Philadelphia International Airport (PHL) and Ronald Reagan Washington National Airport (DCA) .  Air Wisconsin previously operated United Express service on behalf of United Airlines followed by US Airways Express service on behalf of US Airways prior to becoming an American Eagle regional air carrier.  The company has announced it will once again partner with United Airlines as a United Express code sharing air carrier with primary hubs to be located at Chicago O'Hare International Airport (ORD) and Washington Dulles International Airport (IAD) beginning in September 2017 and will be \"exclusively operating\" as United Express by March 2018.\n\nJim French (businessman): James French CBE (born 4 July 1953) is the former chairman and CEO of the airline Flybe.  He owned approximately 7% of the overall business.\n\nAir Costa: Air Costa was an Indian regional airline headquartered in Vijayawada and based out of Chennai Airport.  It was owned by Indian business company LEPL Group.  The airline commenced operations as a regional airline in October 2013 using two Embraer E-170 aircraft with the first flight taking off from Chennai on 16 October 2013.  The airline got a permit for pan India operations in October 2016.  The airline focused on connectivity between tier II and tier III cities in the country and invested as of 2015.  Air Costa operated 32 daily flights to nine destinations from its focus cities Chennai and Vijayawada as of 2015.  The airline had a maintenance center in Chennai.  On 28 February 2017, it suspended operations until further notice.\n\nHorizon Air: Horizon Air Industries, Inc., operating as Horizon Air, is a regional airline based in SeaTac, Washington, United States.  Horizon Air and its sister carrier Alaska Airlines are subsidiaries of Alaska Air Group and all Horizon-operated scheduled flights are marketed and sold by Alaska Airlines.  Planes operated by Horizon are now co-branded as \"Alaska \" in recognition of the Horizon brand and to differentiate aircraft from those operated by Alaska's other regional airline partner, SkyWest Airlines.\n\nNortheast Express Regional Airlines: Northeast Express Regional Airlines was a regional airline based in Manchester, New Hampshire.  The airline was originally known as Valley Airlines started by Maine businessman Roland Martin it capitalized on the US government essential air service by flying intrastate Maine to small communities that otherwise would not have access to airline services.  Then the airline was brought by Allen Caruso of Bar Harbor Airlines fame.  They rebranded and became Northeast Express Regional Airlines and became a Northwest Airlines codeshare affiliate dba Northwest Airlink.  The airline declared bankruptcy and was liquidated, along with its sister company Precision Airlines, in 1995.\n\nAirlinair: Société Airlinair is a French regional airline based in Rungis, France, operating scheduled regional flights (some of which are on behalf of Air France), and aircraft lease services.  The airline has set up bases at Paris-Orly Airport and Lyon-Saint Exupéry Airport.  As an Air France regional partner, it also offers flights from Paris-Charles de Gaulle Airport\n\nRegional Airline Association: The Regional Airline Association (RAA) is a business association founded in 1975 that represents 31 North American regional airlines and 280 associate, non-airline members.  This includes manufacturers of products and services supporting the regional airline industry.  The RAA is the collective bargaining voice for its members' interests and lobbies on their behalf before the United States Congress, Department of Transportation, Federal Aviation Administration and other federal agencies.  The RAA represents the financial and economic interests of regional airline employers and regional airline support industry employers.  The Regional Airline Association does not represent financial or economic interest of airline employees, either union or other.  The RAA is headquartered in Washington DC.\n\nFlybe: Flybe (pronounced ) is the largest independent regional airline in Europe, based in Exeter, operating more UK domestic flights than any other airline.  It flies 7 million passengers a year on 149 routes, from 62 destinations in 9 countries, connecting to long-haul hubs in Manchester, Birmingham, Paris, Dublin and Amsterdam.  It is a member of the European Regions Airline Association.  Flybe's parent company Flybe Group PLC (formerly known as Walker Aviation Limited) is listed on the London Stock Exchange.\n\nAer Arann: Aer Arann (styled as Aer Arann Regional) was a regional airline based in Dublin, Ireland.  The airline operated scheduled services on behalf of Aer Lingus Regional.  The airline had three bases in Cork, Dublin and Shannon which operated under the Aer Lingus Regional brand.\n\nIan Lang Livingstone: Ian Lang Livingstone, CBE, DL (born 23 February 1938) is a Scottish businessman; former Chairman of the board of Motherwell College; former Chairman of Motherwell Football Club; former Chairman of Lanarkshire Health Board; and former Chairman of the Lanarkshire Development Agency.\n\nQuestion: Where is the regional airline based that Jim French is the former chairman and CEO of?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_of_interest\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person mentioned in the context.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in the associated airline.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"airline_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the airline.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of airline, e.g., regional.\"\n        },\n        \"base_city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the airline is based.\"\n        },\n        \"base_country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the airline is based.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"type\",\n        \"base_city\",\n        \"base_country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The final answer to the question, which is the base city of the airline.\"\n    }\n  },\n  \"required\": [\n    \"person_of_interest\",\n    \"airline_details\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_of_interest": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person mentioned in the context."
          },
          "role": {
            "type": "string",
            "description": "The role of the person in the associated airline."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "airline_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the airline."
          },
          "type": {
            "type": "string",
            "description": "The type of airline, e.g., regional."
          },
          "base_city": {
            "type": "string",
            "description": "The city where the airline is based."
          },
          "base_country": {
            "type": "string",
            "description": "The country where the airline is based."
          }
        },
        "required": [
          "name",
          "type",
          "base_city",
          "base_country"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The final answer to the question, which is the base city of the airline."
      }
    },
    "required": [
      "person_of_interest",
      "airline_details",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
