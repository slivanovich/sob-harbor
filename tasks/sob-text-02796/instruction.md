{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTom L. Ward: Tom L. Ward is a prominent Oklahoma City businessman and philanthropist.  He is currently the Chairman and CEO of Mach Resources, a privately owned energy company in Oklahoma City, OK.  He was the founder and former Chairman and CEO of Tapstone Energy and SandRidge Energy, Inc. and is the former President, Chief Operating Officer, and co-founder of Chesapeake Energy.\n\nJapan Energy: Japan Energy Corporation (株式会社ジャパンエナジー , Kabushiki-gaisha Japan Enajī ) was a Japanese petroleum company, a wholly owned subsidiary of Nippon Mining Holdings (新日鉱ホールディングス株式会社 , Shin-Nikkō Hōrudingsu Kabushiki-gaisha ) .  The petroleum products of Japan Energy Corporation were sold by filling stations under the brand name JOMO.\n\nChesapeake Energy: Chesapeake Energy Corporation is an American petroleum and natural gas exploration and production company headquartered in Oklahoma City, Oklahoma.  The company was founded in 1989 by Aubrey McClendon and Tom L. Ward with only a $50,000 initial investment.  McClendon named the company due to his love of the Chesapeake Bay region.  Ward later left the company to found SandRidge Energy.\n\nRomolo Nati: Romolo Valentino Benedetto Nati, (born February 14, 1968) known as Romolo Nati or RVN, is a multi-awarded Italian architect and businessman with interest in sustainable development (energy and real estate).  He is the current Executive Chairman and CEO of Italpinas Development Corporation (IDC), an Italian-Filipino real estate development firm which held its initial public offering (IPO) on Monday, December 7, 2015 that specializes in the design and development of sustainable buildings.  He is the Vice Chairman of the Philippine renewable energy company Constellation Energy Corporation (CEC).  Nati is also the Chairman of IDC’s official leasing company Damiani Property Management and Services, Inc.\n\nCohen &amp; Gresser: Cohen & Gresser LLP is an international law firm with offices in New York City, Paris, Washington D.C, and Seoul.  The firm represents clients in complex litigation and corporate transactions throughout the world.  Founded in 2002, the firm has grown to nearly seventy lawyers in six practice groups: Corporate; Employment; Intellectual Property & Technology; Litigation and Arbitration; Tax; White Collar Defense.  The firm’s clients include Fortune 500 companies and major financial institutions across a broad spectrum of industries throughout the world, and it has litigated and negotiated against some of the nation’s largest law firms.  Among Cohen & Gresser’s clients are Goldman Sachs, LG Electronics, Chesapeake Energy, Hyundai Rotem, Southwest Airlines, Bank of America, and L’Oréal.\n\nAubrey McClendon: Aubrey Kerr McClendon (July 14, 1959 – March 2, 2016) was an American businessman and the founder and chief executive officer of American Energy Partners, LP.  He also co-founded Chesapeake Energy, serving as its CEO and chairman.  He was an outspoken advocate for natural gas as an alternative to oil and coal fuels.  He was a pioneer in employing fracking, a controversial fuel extraction technique which has been widely criticized on environmental grounds.\n\nChesapeake Energy Arena: Chesapeake Energy Arena, originally known as the Ford Center from 2002 to 2010 and Oklahoma City Arena until 2011, is an arena located in downtown Oklahoma City, Oklahoma, United States.  It opened in 2002 and since 2008 has served as the home venue of the Oklahoma City Thunder of the National Basketball Association (NBA).  Previously, Chesapeake Energy Arena was home to the Oklahoma City Blazers of the Central Hockey League (CHL) from 2002 until the team folded in July 2009, and the Oklahoma City Yard Dawgz of AF2 from 2004 to 2009 when the team moved to the Cox Convention Center.  In addition to its use as a sports venue, Chesapeake Energy Arena hosts concerts, family and social events, conventions, ice shows, and civic events.  The arena is owned by the city and operated by the SMG property management company and has 18,203 seats in the basketball configuration, 15,152 for hockey, and can seat up to 16,591 for concerts.\n\nSouth African Nuclear Energy Corporation: The South African Nuclear Energy Corporation (Necsa) was established as a public company by the Republic of South Africa Nuclear Energy Act in 1999 and is wholly owned by the State.  The name is correctly indicated above, although the sequence of letters in the acronym may be taken as suggesting that the name should be the \"Nuclear Energy Corporation of South Africa\".\n\nSolar Energy Corporation of India: Solar Energy Corporation of India Ltd. (SECI) is a company of the Ministry of New and Renewable Energy, Government of India, established to facilitate the implementation of Jawaharlal Nehru National Solar Mission.  It is the only public sector undertaking dedicated to the solar energy sector.  The company's mandate has been broadened to cover the entire renewable energy domain and the company will be renamed to Renewable Energy Corporation of India (RECI).\n\nCenterPoint Energy: CenterPoint Energy is a Fortune 500 electric and natural gas utility serving several markets in the U.S. states of Arkansas, Louisiana, Minnesota, Mississippi, Oklahoma, and Texas.  It was formerly known as Reliant Energy (from which it is now separated), NorAm Energy, Houston Industries, and HL&P.  The company is headquartered in the CenterPoint Energy Tower at 1111 Louisiana Street in Downtown Houston.  Some of its notable subscribers include Retail Electric Providers (REPs), such as NRG Energy, Champion Energy, Dynowatt, Ambit Energy, Texas Power, Bounce Energy, MXenergy, Direct Energy, Stream Energy, First Texas Energy Corporation, Gexa Energy, Cirro Energy, and Kona Energy.\n\nQuestion: Where was Tom L. Ward a Prominent businessman and philanthropist, and the company he founded, Chesapeake Energy Corporation, located?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the prominent businessman and philanthropist.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person mentioned in the context.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"company\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the company founded by the person.\"\n        },\n        \"founder_relationship\": {\n          \"type\": \"string\",\n          \"description\": \"Describes the relationship of the person to the company.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founder_relationship\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"shared_location\": {\n      \"type\": \"string\",\n      \"description\": \"The city and state where both the person was prominent and the company was located.\"\n    }\n  },\n  \"required\": [\n    \"person\",\n    \"company\",\n    \"shared_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the prominent businessman and philanthropist."
          },
          "role": {
            "type": "string",
            "description": "The role of the person mentioned in the context."
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "company": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the company founded by the person."
          },
          "founder_relationship": {
            "type": "string",
            "description": "Describes the relationship of the person to the company."
          }
        },
        "required": [
          "name",
          "founder_relationship"
        ],
        "additionalProperties": false
      },
      "shared_location": {
        "type": "string",
        "description": "The city and state where both the person was prominent and the company was located."
      }
    },
    "required": [
      "person",
      "company",
      "shared_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
