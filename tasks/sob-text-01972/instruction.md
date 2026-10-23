{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nIPlant Collaborative: The iPlant Collaborative is a virtual organization created by a cooperative agreement funded by the US National Science Foundation (NSF) to create cyberinfrastructure for the plant sciences (botany).  The NSF compared cyberinfrastructure to physical infrastructure, \"... the distributed computer, information and communication technologies combined with the personnel and integrating components that provide a long-term platform to empower the modern scientific research endeavor\".  In September 2013 it was announced that the National Science Foundation had renewed iPlant’s funding for a second 5-year term with an expansion of scope to all non-human life science research.\n\nLExEN: LExEN is an acronym for Life in Extreme Environments.  It was originally developed by G. Michael Purdy in 1997 as an area of research in which scientists could seek funding for activities in the polar regions, and overseen by the National Science Foundation as a highly interdisciplinary, integrated research program.  Participating were the Directorates for Biological Sciences, Mathematical and Physical Sciences, Engineering, Geosciences, and the Office of Polar Programs of the National Science Foundation.  The program sought to place a strong emphasis upon those life-supporting environments that exist near the extremes of planetary conditions.  The study of extreme habitats, both planetary and extra-planetary, was underpinned by the idea that \"deep understanding of certain earth-bound microbial systems would provide important insights into life-sustaining processes and the origin of life on our own planet, while illuminating the search for life in other planetary environments.\"\n\nNational Science Board: The National Science Board (Board, NSB) of the United States establishes the policies of the National Science Foundation (NSF) within the framework of applicable national policies set forth by the President and the Congress.  The NSB also serves as an independent policy advisory body to the President and Congress on science and engineering research and education issues.  The Board has a statutory obligation to \"...render to the President and to the Congress reports on specific, individual policy matters related to science and engineering and education in science engineering, as Congress or the President determines the need for such reports,\" (e.g. Science and Engineering Indicators; Report to Congress on Mid-scale Instrumentation at the National Science Foundation).  The President appoints the 24 Board members.  NSF's director serves as an ex officio 25th member and is appointed by the President and confirmed by the Senate.\n\nNSF-GRF: The National Science Foundation Graduate Research Fellowship Program (NSF-GRFP) is an annual grant awarded by the National Science Foundation to approximately 2,000 students pursuing research-based Master's and doctoral degrees in the natural, social, and engineering sciences at US institutions.  The fellowship provides an honorarium of $12,000 to be placed towards the cost of tuition and fees at the university the fellow attends; it also awards the student directly with an annual $34,000 stipend for three years.  Each recipient could previously apply for a one time only travel award for $1,000.  This travel award was previously for international research activities or presenting at an international scientific conference.  However, in 2010, this opportunity was converted to the Nordic Research Opportunity, which is intended to facilitate collaborations between U.S. graduate fellows and scholars at Finnish, Swedish, Danish, and Norwegian research institutions.\n\nNational Science Foundation: Under the Microscope: National Science Foundation: Under the Microscope was a 73-page report released on May 26, 2011 by US Senator Tom Coburn, a conservative Republican from Oklahoma), accusing the National Science Foundation of poor management and practices, various research projects, and the social sciences. Mainstream press coverage generated a public controversy and a stir in academia.\n\nFrank T. Rothaermel: Frank T. Rothaermel is a professor in the Scheller College of Business at the Georgia Institute of Technology and an Alfred P. Sloan Industry Studies Fellow.  He holds the Russell and Nancy McDonough Chair of Business and received a National Science Foundation CAREER Award which \"is a Foundation-wide activity that offers the National Science Foundation's most prestigious awards in support of the early career-development activities of those teacher-scholars who most effectively integrate research and education within the context of the mission of their organization.\"  Frank is also the area coordinator for Strategic Management at the Scheller College of Business.  Frank authored the textbook \"Strategic Management.  Concepts & Cases\" published by McGraw-Hill.  Frank maintains an active social media presence with a Strategy Blog at https://www.facebook.com/ftrStrategy and Twitter feed at https://twitter.com/ftrStrategy.\n\nNational Science Foundation CAREER Awards: The \"National Science Foundation CAREER awards\" are the National Science Foundation's most prestigious awards in support of junior faculty who exemplify the role of teacher-scholars through research, education and the integration of education and research within the context of the mission of their organizations.  The award comes with a federal grant for research and education activities for five consecutive years.  NSF grants these awards once a year.  The reviewing, award and selection process is one of the most competitive within the NSF.\n\nDragonfly Project: Project Dragonfly is an American educational project.  It was initially designed to give children opportunities in inquiry based learning in the sciences.  The project was started as a magazine and website produced by professors in the Western College Program at Miami University and the National Science Teachers Association with a grant from the National Science Foundation and assistance from the Center for Human Development, Learning, and Teaching at Miami University.  Project Dragonfly now reaches millions of people each year through inquiry-driven learning media, public exhibits and graduate programs worldwide.  Project Dragonfly's partnership programs have generated an Emmy-Award-winning PBS television series, teacher workshops, master's degrees, public science exhibits, and conservation and education programs worldwide.  Supported by the National Science Foundation, the project began in 1994 with the first national magazine to feature children's science investigations and discoveries.  Project Dragonfly's programs include Earth Expeditions global graduate courses for educators and other professionals, the Global Field Program (GFP) and Advanced Inquiry Program (AIP) master's degrees, and iSaveSpecies, which engages zoo visitors throughout the country in science and conservation action.  Project Dragonfly is based in the biology department at Miami University, a state university in Oxford, Ohio.  Miami was established in 1809 and is listed as one of the eight original Public Ivies.  Public Engagement Projects include: iSaveSpecies, Wild Research, DragonflyTV.  Graduate Credit Workshops include Earth Expeditions, Zoo Expeditions, and iDiscovery.  Master's Degree Programs include Global Field Program (GFP) and Advanced Inquiry Program (AIP), and Earth Expeditions (EE).\n\nTom Coburn: Thomas Allen \"Tom\" Coburn (born March 14, 1948) is an American politician and medical doctor.  A member of the Republican Party, he was the junior United States Senator from Oklahoma.\n\nKevin Zhu: Kevin Zhu is a full professor of innovation and technology at the Rady School of Management, University of California, San Diego (UCSD).  A Stanford University alumnus, Zhu is a recipient of the U.S. National Science Foundation's CAREER Award and a similar award from the NSF of China in 2008.  He has also received several Best Paper Awards in his field, with papers published in the top academic journals such as \"Management Science\", \"Information Systems Research\", \"Marketing Science\", and \"MIS Quarterly\", as well as in a book \"Global E-Commerce\" (Cambridge University Press).  He serves on National Science Foundation research proposal review panels and holds editorial positions at the top academic journals.  His research has often focused on information technology, with prior emphasis on the economic impacts to firms and industries and more recent emphasis on especially wireless technology in healthcare.\n\nQuestion: When did a Republican, junior, US Senator from Oklahoma accuse the National Science Foundation of poor management and research?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_description\": {\n      \"type\": \"string\",\n      \"description\": \"Description of the event where the accusation was made.\"\n    },\n    \"accuser_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"Name of the person making the accusation.\"\n        },\n        \"political_party\": {\n          \"type\": \"string\",\n          \"description\": \"Political party of the accuser.\"\n        },\n        \"senator_status\": {\n          \"type\": \"string\",\n          \"description\": \"Status of the senator (e.g., junior).\"\n        },\n        \"state_represented\": {\n          \"type\": \"string\",\n          \"description\": \"US state the senator represented.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"political_party\",\n        \"senator_status\",\n        \"state_represented\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"accused_entity\": {\n      \"type\": \"string\",\n      \"description\": \"The entity that was accused.\"\n    },\n    \"accusation_details\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Specific details of the accusations made.\"\n    },\n    \"event_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The date when the accusation was made or report released.\"\n    }\n  },\n  \"required\": [\n    \"event_description\",\n    \"accuser_details\",\n    \"accused_entity\",\n    \"accusation_details\",\n    \"event_date\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_description": {
        "type": "string",
        "description": "Description of the event where the accusation was made."
      },
      "accuser_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the person making the accusation."
          },
          "political_party": {
            "type": "string",
            "description": "Political party of the accuser."
          },
          "senator_status": {
            "type": "string",
            "description": "Status of the senator (e.g., junior)."
          },
          "state_represented": {
            "type": "string",
            "description": "US state the senator represented."
          }
        },
        "required": [
          "name",
          "political_party",
          "senator_status",
          "state_represented"
        ],
        "additionalProperties": false
      },
      "accused_entity": {
        "type": "string",
        "description": "The entity that was accused."
      },
      "accusation_details": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Specific details of the accusations made."
      },
      "event_date": {
        "type": "string",
        "format": "date",
        "description": "The date when the accusation was made or report released."
      }
    },
    "required": [
      "event_description",
      "accuser_details",
      "accused_entity",
      "accusation_details",
      "event_date"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
