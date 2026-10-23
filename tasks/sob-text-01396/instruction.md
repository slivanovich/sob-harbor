{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUniversal McCann: Universal McCann (UM) is a global media and advertising agency.  UM's global clients include ABInBev, Cathay Pacific, Chrysler, Coca-Cola, Hershey's, Johnson & Johnson, and Sony.  UM is a member of Interpublic Group, operating under the IPG Mediabrands branch.  Some of its regional offices are known as \"Universal Media\" rather than \"Universal McCann\", but generally all known as UM.\n\n4th &amp; B'way Records: 4th & B'way Records (pronounced and spelled out completely as Fourth and Broadway Records in the UK) was a US-based subsidiary of Island Records that specialized in street-oriented music such as hip hop.  Established in 1984, it was the flagship label of the Island Trading Company, the independent-distribution parent company of Island's other record labels that operated in the US.  However, 4th & B'way was not distributed through major-label channels—the flagship Island label was distributed by Atlantic Records at that time—until the label and distribution company were acquired by PolyGram Records in 1989, when Island Trading became a unit of PolyGram Group Distribution and was renamed Independent Label Sales (ILS).  It was also one of several US-based Island labels that were named after nearby New York City streets when Island's US headquarters were located at 14 East 4th Street in Manhattan, the same building that held the legendary Greenwich Village branch of Tower Records, and also nearby at 400 Lafayette Street.  When Island moved its headquarters to the Worldwide Plaza Building at 825 8th Avenue in 1995, where PolyGram's US headquarters were also located, the empty 4th Street offices became the headquarters of V2 Records.\n\nMichigan City Area Schools: Michigan City Area Schools is a school district based in Michigan City, Indiana in LaPorte County.  It serves students in Michigan City and several adjacent towns and villages.  It operates one high school, two middle schools, and eight elementary schools.  Two schools, Elston Middle School and Niemann Elementary School, closed at the end of the 2013/2014 school year.\n\nMichigan City Transit: Michigan City Transit is a municipal bus service in Michigan City, Indiana.  It was known as Michigan City Municipal Coach until 2007.  The service was created in 1955, when Michigan City assumed control of bus routes operated by Michigan City Transit Lines, a private bus system.  Michigan City Transit Lines, in turn, was a successor of Michigan City's streetcar system.\n\nIlan Shiloah: Ilan Shiloah (born in 1957) is an Israeli businessman, and former CEO of McCann Erickson-Kesher-Barel, Israel's largest advertising firm.  He is the active Chairman of McCann WorldGroup, Israel, which consists of McCann Erickson, Universal McCann and McCann Digital.  He is also the Chairman of the performance marketing company Matomy Media Group, and Chairman of The Time; a technology startups investment company.  Since 2003, Mr. Shiloah has served on the Executive Board of McCann Erickson EMEA.\n\nHaskell and Barker Historic District: Haskell and Barker Historic District is a national historic district located at Michigan City, LaPorte County, Indiana.  The district encompasses 205 contributing buildings, 3 contributing structures, and 1 contributing object in a predominantly residential section of Michigan City.  The district is named for the Haskell and Barker manufacturing company.  It developed between about 1860 and 1960, and includes examples of Italianate, Gothic Revival, Queen Anne, Colonial Revival, Tudor Revival, and Bungalow / American Craftsman style architecture.  Located in the district are the separately listed John H. Barker Mansion and First Congregational Church of Michigan City.  Other notable buildings include the St. Stanislaus Koska Church (1922-1926), Rectory (1938), and Convent (1938), Consumer Service Company (1922), Michigan City School of Fine Arts (1908), Gilmore-Gardner Building (1925), Porter-Carrigan House (1895), Hutchinson House (1875), St Mary of the Immaculate Conception Catholic Church (1868) and Convent (1905), and Hartke House (c. 1860).\n\nIndiana State Road 520: State Road 520 is a four-lane connector about 1,000 feet (305 m) in length.  It exists solely to connect U.S. Route 12 and U.S. Route 20 in Pines, about 3 miles (5 km) west of Michigan City.  U.S. 12 and U.S. 20 do not cross at this point — they parallel each other for another 22 miles (35 km) westbound and overlap in Gary; U.S. 20 is generally considered the faster of the two, while U.S. 12 is the scenic Dunes Highway.  Eastbound, U.S. 12 travels through Michigan City and northeast into Michigan where it forks east from the Red Arrow Highway.  U.S. 20 stays in Indiana and runs around Michigan City as a bypass to the south.\n\nMichigan City White Caps: The Michigan City White Caps were a minor league baseball team that played in Michigan City, Indiana from 1956 to 1959.  The team had been the Hannibal Stags, moving to Michigan City to become a charter member of the Midwest League in 1956.  The White Caps were affiliated with the Giants, who played in New York from 1956–57 and San Francisco from 1958-59.  The franchise folded after the 1959 season, but the nickname name was restored to the region when today's West Michigan White Caps began play in the Midwest League in 1994.  Baseball Hall of Fame Inductee Juan Marichal pitched for Michigan City in 1958.\n\nChrysler: FCA US LLC (also called Fiat Chrysler or Chrysler) ( ) is the American subsidiary of Fiat Chrysler Automobiles N.V., an Italian controlled automobile manufacturer registered in the Netherlands with headquarters in London, U.K., for tax purposes.  FCA US is one of the \"Big Three\" American automobile manufacturers.  FCA US has its headquarters in Auburn Hills, Michigan and sells vehicles worldwide under its flagship Chrysler brand, as well as the Dodge, Jeep, and Ram Trucks.  Other major divisions include Mopar, its automotive parts and accessories division, and SRT, its performance automobile division.\n\nCoast Guard Station Michigan City: Coast Guard Station Michigan City is a United States Coast Guard station located in Michigan City, Indiana.  The station is the only Coast Guard Station located on Lake Michigan in Indiana.  Station Michigan City is a multi-mission unit that conducts missions in search and rescue, maritime law enforcement, homeland security and marine environmental protection.  The station responds to an average of 125 search and rescue cases a year, assisting nearly two million dollars in property.\n\nQuestion: Universal McCann has a client in the company that has US headquarters in what Michigan city?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"client_company\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the client company of Universal McCann.\"\n    },\n    \"headquarters_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the company's US headquarters are located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the company's US headquarters are located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_universal_mccann_client\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the company is a client of Universal McCann.\"\n    }\n  },\n  \"required\": [\n    \"client_company\",\n    \"headquarters_location\",\n    \"is_universal_mccann_client\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "client_company": {
        "type": "string",
        "description": "The name of the client company of Universal McCann."
      },
      "headquarters_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the company's US headquarters are located."
          },
          "state": {
            "type": "string",
            "description": "The state where the company's US headquarters are located."
          }
        },
        "required": [
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "is_universal_mccann_client": {
        "type": "boolean",
        "description": "True if the company is a client of Universal McCann."
      }
    },
    "required": [
      "client_company",
      "headquarters_location",
      "is_universal_mccann_client"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
