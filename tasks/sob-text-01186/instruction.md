{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRIT Ambulance: RIT Ambulance (RITA) is a community run, 911 dispatched, volunteer collegiate New York State Certified Basic Life Support Ambulance Agency, run under the Rochester Institute of Technology Student Health Center.  The ambulance serves the entire Rochester Institute of Technology campus.\n\nMadanapalle Institute of Technology and Science: Madanapalle Institute of Technology and Science also known as MITS is established in 1998 in Madanapalle, Chittoor district of Andhra Pradesh, India.  MITS is Affiliated to JNTUA, approved by AICTE, New Dehli.  Also a Recognised Research Center, Recognised by UGC under the sections 2(f) and 12 (B) of the UGC act 1956.  MITS campus is recognised as 'Green Technology Campus'.  IBM Center of Excellence was inaugurated in MITS on December, 2010.,\n\nBritish Columbia Institute of Technology: The British Columbia Institute of Technology (also referred to as BCIT), is a public polytechnic institution of higher education.  The post-secondary institute has five campuses located in the Metro Vancouver region, with its main campus in Burnaby, British Columbia, Canada.  There is also the Aerospace Technology Campus in Richmond, the Marine Campus in the City of North Vancouver, Downtown campus in Vancouver, and Annacis Island Campus in Delta.  It is provincially chartered through legislation in the \"College and Institute Act.\"  The school operates as a vocational and technical school, offering apprenticeships for the skilled trades and diplomas and degrees in vocational education for skilled technicians and workers in professions such as engineering, accountancy, business administration, nursing, medicine, architecture, and law.\n\nPeter Shirtcliffe: George Peter Shirtcliffe, {'1': \", '2': \", '3': 'CMG', '4': \"} (born 28 July 1931), is a New Zealand businessman.  He was the chairman of Telecom New Zealand, New Zealand's largest listed company, from 1990 to 1999.  He was appointed a Companion of the Order of St Michael and St George in the 1988 Queen's Birthday Honours, for services to marketing and business management.  He received the New Zealand 1990 Commemoration Medal.  He is also a Laureate of the New Zealand Business Hall of Fame, a fellow of the New Zealand Institute of Chartered Accountants (honorary retired) and a Distinguished Fellow of the Institute of Directors.  He was the founding chairman of the Enterprise Education Foundation and later a trustee of the Enterprise New Zealand Trust.  He was an active member of the Royal New Zealand Naval Volunteer Reserve from 1953 to 1967, reaching the rank of Lieutenant Commander.\n\nBharathidasan Institute of Technology: Bharathidasan Institute of Technology (or BIT) (formerly the School of Engineering and Technology) was established by Bharathidasan University in 1999.  BIT was located in the downtown Khajamalai Campus and was moved to the South Campus (Technology Campus) in 2001.  In addition to the academic blocks, the campus houses the Indoor Sports Complex and residential complex.  Bharathidasan University operates shuttle services to the adjacent Main Campus.\n\nNew Zealand Initiative: The New Zealand Initiative is a think tank and business membership organisation in Wellington, New Zealand.  It was formed in 2012 out of the merger of the New Zealand Business Roundtable (NZBR) and the New Zealand Institute.  Its executive director is Oliver Hartwich, who joined The New Zealand Initiative from the Australian Centre for Independent Studies.\n\nZealand Institute of Business and Technology: Zealand Institute of Business and Technology (Danish: Erhvervsakademi Sjælland, EASJ) or Zibat is a school of higher education operating five campuses in Region Zealand to the west and south of Copenhagen, Denmark.  The campuses, with a total of some 3,200 students, are located in Roskilde, Køge, Næstved, Slagelse and Nykøbing Falster.  The school is an idenpendent self-owning institution subordinated to the Ministry of Science, Innovation and Higher Education.  Degree programmes offerered are mainly applied degrees, especially in technology, IT and business.  The academy grant undergraduate and academic degrees but not master's or doctoral degrees.  In addition to full-time studies the academy offers supplemental education, part-time programmes at bachelor's level and short-term courses for people who need to strengthen their qualifications.\n\nRoskilde: Roskilde (] ), located 30 km west of Copenhagen on the Danish island of Zealand, is the main city in Roskilde Municipality.  With a population of 50,046 (as of 01 2016 ), the city is a business and educational centre for the region and the 10th largest city in Denmark.  Roskilde is governed by the administrative council of Roskilde Municipality.\n\nPete Bossley: Peter James \"Pete\" Bossley (born 1950) is a New Zealand architect based in Auckland, most recognised for his role leading the design team for the Museum of New Zealand Te Papa Tongarewa.  Bossley was an adjunct professor at the Unitec Institute of Technology School of Architecture.  He has received numerous awards, including the New Zealand Institute of Architects (NZIA) Gold Medal in 2012 for outstanding contributions to the practice of architecture.\n\nGaven Martin: Gaven John Martin (born October 8, 1958) is a New Zealand mathematician.  He is a Distinguished Professor of Mathematics at Massey University, the head of the New Zealand Institute for Advanced Study, the former president of the New Zealand Mathematical Society (from 2005 to 2007), and the editor-in-chief of the \"New Zealand Journal of Mathematics\".  He is Vice President of the Royal Society of New Zealand [Mathematical, Physical Sciences Engineering and Technology.  His research concerns quasiconformal mappings, regularity theory for partial differential equations, and connections between the theory of discrete groups and low-dimensional topology.\n\nQuestion: Which Zealand Institute of Business and Technology campus is located in a city with a population of 50,046?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"institute_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the educational institute.\"\n    },\n    \"campus_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific campus.\"\n    },\n    \"city_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the city where the campus is located.\"\n        },\n        \"population\": {\n          \"type\": \"integer\",\n          \"description\": \"The population of the city.\"\n        },\n        \"population_as_of_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date as of which the population was recorded.\"\n        }\n      },\n      \"required\": [\n        \"city_name\",\n        \"population\",\n        \"population_as_of_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"institute_name\",\n    \"campus_name\",\n    \"city_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "institute_name": {
        "type": "string",
        "description": "The name of the educational institute."
      },
      "campus_name": {
        "type": "string",
        "description": "The name of the specific campus."
      },
      "city_details": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "The name of the city where the campus is located."
          },
          "population": {
            "type": "integer",
            "description": "The population of the city."
          },
          "population_as_of_date": {
            "type": "string",
            "description": "The date as of which the population was recorded."
          }
        },
        "required": [
          "city_name",
          "population",
          "population_as_of_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "institute_name",
      "campus_name",
      "city_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
