{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMOBTV: MOBTV (MediaCorp Online Broadband Television) was Singapore's first subscription-based video on demand service that provides viewers with access to various TV programmes via immediate digital streaming or download from an Internet connection.  From 30 March 2010, MOBTV merged with xinmsn.com as a free video on demand service, together with Podcast.sg and xin.sg.  In other words, MOBTV has ceased to exist.  However, MOBTV Select is still available on mio TV on Channel 312 till 12 September 2012 and was shifted to Channel 509 as of 13 September 2012 and MobTV Select on Singtel mio TV service using Channel 509 will ceased transmission from 7 January 2014 at 2359hrs.  MobTV Select was removed from mio TV Service with effect from 8 October at 3:00 PM.MobTV and MobTV Select names do not exist any more.\n\nMiniverse: Miniverse is a documentary film that was released on the subscription video on demand service CuriosityStream, in partnership with production company Flight 33 Productions.  \"Miniverse\" is hosted by former International Space Station Commander Colonel Chris Hadfield.  The concept of the film is to bring the expanse of the Solar System down to the scale of the continental United States.  In the film, Hadfield drives on a cross-country journey exploring planets and celestial bodies with a rotating passenger seat of famous astronomers, traveling from New York to California.  The film premiered on April 17, 2017.\n\nDavid Florida Laboratory: The David Florida Laboratory is the Canadian Space Agency's spacecraft assembly, integration and testing centre, in Shirleys Bay, just west of Ottawa.  It is operated by the Canadian Space Agency and rented out to Canadian and foreign aerospace and telecommunications companies and organizations for qualifying space bound equipment such as communication or scientific satellites, or components made to be placed on satellites or installed in a space station.  The laboratory was named to honour C. David Florida, a leading Canadian pioneer in space research.\n\nCanadian Space Society: The Canadian Space Society (CSS) is a national non-profit organization made up of professionals and enthusiasts pursuing the human exploration and development of the Solar System and beyond.  Its principal objective is to stimulate the Canadian space industry through its technical and outreach projects and promote the involvement of Canadians in the development of space.\n\nChris Hadfield: Chris Austin Hadfield {'1': \", '2': \", '3': \", '4': \"} (born 29 August 1959) is a retired Canadian astronaut who was the first Canadian to walk in space.  An engineer and former Royal Canadian Air Force fighter pilot, Hadfield has flown two space shuttle missions and served as commander of the International Space Station.\n\nMarc Garneau: Joseph Jean-Pierre Marc Garneau, {'1': \", '2': \", '3': \", '4': \"} (born February 23, 1949) is a Canadian politician and the Minister of Transport in the Government of Canada.  He is a retired military officer, former astronaut, and engineer; Garneau was the first Canadian in space taking part in three flights aboard NASA Space shuttles in 1984, 1996 and 2000.  Garneau was the president of the Canadian Space Agency from 2001 to 2006, and in 2003 was installed as the ninth Chancellor of Carleton University in Ottawa.\n\nCASSIOPE: CASSIOPE, or \"CAS\"cade, \"S\"mallsat and \"IO\"nospheric \"P\"olar \"E\"xplorer, is a Canadian Space Agency (CSA) multi-mission satellite operated by MacDonald, Dettwiler and Associates (MDA).  The mission is funded through CSA and the Technology Partnerships Canada program.  It was launched September 29, 2013, on the first flight of the SpaceX Falcon 9 v1.1 launch vehicle.  CASSIOPE is the first Canadian hybrid satellite to carry a dual mission in the fields of telecommunications and scientific research.  The main objectives are to gather information to better understand the science of space weather, while verifying high-speed communications concepts through the use of advanced space technologies.\n\nBIGFlix: BIGFLIX is a Reliance Entertainment owned movie on demand service in 2008.  It is India’s first movie on demand service.  It allows users to stream or download movies at any time.  It generates its revenues from subscription fees and does not rely on advertisements.\n\nCanadian Astronaut Corps: The Canadian Astronaut Corps is a unit of the Canadian Space Agency (CSA) that selects, trains, and provides astronauts as crew members for U.S. and Russian space missions.  The Canadian Space Agency was established in 1989.\n\nCanadian Space Agency: The Canadian Space Agency (CSA; French: \"Agence Spatiale Canadienne\" , ASC) was established by the Canadian Space Agency Act which received Royal Assent on May 10, 1990.  The agency reports to the federal Minister of Innovation, Science, and Economic Development.  The current president of the Canadian Space Agency is Sylvain Laporte, who took the position March 9, 2015 following the announcement of his appointment on February 27, 2015.\n\nQuestion: The first Canadian space walker hosts the show \"Miniverse\" which airs on what on demand service?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the show.\"\n    },\n    \"host_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"host_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the host of the show.\"\n        },\n        \"host_nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the host.\"\n        },\n        \"is_first_canadian_spacewalker\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the host was the first Canadian to walk in space.\"\n        }\n      },\n      \"required\": [\n        \"host_name\",\n        \"host_nationality\",\n        \"is_first_canadian_spacewalker\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"on_demand_service\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the on-demand service where the show airs.\"\n    },\n    \"service_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the on-demand service.\"\n    }\n  },\n  \"required\": [\n    \"show_title\",\n    \"host_details\",\n    \"on_demand_service\",\n    \"service_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_title": {
        "type": "string",
        "description": "The title of the show."
      },
      "host_details": {
        "type": "object",
        "properties": {
          "host_name": {
            "type": "string",
            "description": "The name of the host of the show."
          },
          "host_nationality": {
            "type": "string",
            "description": "The nationality of the host."
          },
          "is_first_canadian_spacewalker": {
            "type": "boolean",
            "description": "Indicates if the host was the first Canadian to walk in space."
          }
        },
        "required": [
          "host_name",
          "host_nationality",
          "is_first_canadian_spacewalker"
        ],
        "additionalProperties": false
      },
      "on_demand_service": {
        "type": "string",
        "description": "The name of the on-demand service where the show airs."
      },
      "service_type": {
        "type": "string",
        "description": "The type of the on-demand service."
      }
    },
    "required": [
      "show_title",
      "host_details",
      "on_demand_service",
      "service_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
