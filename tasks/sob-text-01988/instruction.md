{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPlaxton President: The Plaxton President was a low floor double-decker bus body built at Northern Counties plant in Wigan, England and branded as a Plaxton product for its main production run.  It was unveiled in 1997 and built between 1999 and 2005.  When it became part of TransBus International, the body was sold under the TransBus name; strangely never got branded as the Alexander Dennis President after ADL bought Transbus.  The President was built on the Dennis/TransBus Trident, the DAF DB250 and the Volvo B7TL chassis.  It can be built as either a closed top bus or an open-top bus.\n\nOver Wyre: Over Wyre is the collective name given to a group of villages in Lancashire, England, situated on the Fylde, to the north of the River Wyre.  The group is usually considered to include Hambleton, Stalmine, Knott End-on-Sea, Preesall, Pilling and Out Rawcliffe.  The name distinguishes these villages from the larger southern part of the Fylde, between the Wyre and the Ribble, which includes the urban areas of Blackpool, Poulton-le-Fylde, Thornton, Cleveleys, Fleetwood and Lytham St Annes.\n\nLytham St Annes: Lytham St Annes ( ) is a conurbation in the Fylde district of Lancashire, England.  The neighbouring towns of Lytham and St. Annes-on-the-Sea (nearly always abbreviated to St Annes) have grown together and now form a seaside resort.  The towns are situated on the Fylde coast, south of Blackpool at the point where the coastline turns east to form the estuary of the River Ribble leading inland to Preston.  St Annes is situated on the northern side of the turning and, like Blackpool, overlooks the Irish Sea, whereas Lytham is on the eastern side and overlooks the Ribble Estuary.  The population of Lytham St Annes taken at the 2011 census was 42,954.\n\nFY postcode area: The FY postcode area, also known as the Blackpool postcode area, is a group of postcode districts around Blackpool, Thornton-Cleveleys, Lytham St Annes, Poulton-le-Fylde and Fleetwood in England.  The letters \"FY\" refer to the Fylde, which includes the whole postcode area.\n\nLytham St Annes Express: Lytham St Annes Express is a local weekly newspaper, named after Lytham St Annes largely serving the Fylde Borough.  It is published by the Blackpool Gazette and therefore owned by Johnson Press.\n\nVolvo B7L: The Volvo B7L was a fully low floor single-decker bus, double-decker bus and articulated bus chassis with a rear engine mounted vertically on the left of the rear overhang, it was built as a replacement for the Volvo B10L.  It was used as both a single-decker bus and a double-decker bus chassis largely in Continental Europe.\n\nLytham St Annes Art Collection: The Lytham St Annes Art Collection is a public art collection of over 240 artworks in Lytham St Annes, Lancashire.  Fylde Borough Council are the custodians of the paintings, sculptures, prints and artefacts that are mostly held within the Town Hall in St Annes.  The collection was started in 1925 by the donation of \"The Herd Lassie\", painted by Richard Ansdell, to the townspeople of Lytham St Annes, Lancashire.  It was donated by John Booth, son of the founder of the grocery store chain Booths.  The collection is now one of the largest public collections of Ansdell's paintings.\n\nEast Lancs Spryte: The East Lancs Spryte was a low floor single-decker bus body built by East Lancashire Coachbuilders.  It was designed to body the Dennis Dart SLF chassis, but a handful have been built on others, for example, the Volvo B6LE.  Mechanically and visually, it is the single-decker version of the East Lancs Lolyne.\n\nBlackpool Transport: Blackpool Transport Services Ltd. (BTS) is a bus and tram operator running within the boroughs of Blackpool and Fylde and into the surrounding area, including Fleetwood, Lytham St Annes, Poulton-le-Fylde and Cleveleys.  It is owned by Blackpool Borough Council.\n\nPlaxton Centro: The Plaxton Centro is a low floor single-decker bus body designed by Bluebird Vehicles and manufactured by Plaxton.  It was launched on the VDL SB120 in February 2006.  The Centro was also made available on the VDL SB200 chassis in 2006.  In 2007 the Centro was made available on the MAN 12.240 and the Volvo B7RLE chassis.  The first operator of the Volvo chassied example was Rotala subsidiary Wessex Bus for the Bristol Park & Ride service East Yorkshire Motor Services had 6 Centro bodied Volvo B7RLEs delivered in 2008.  In 2010, Blackpool Transport took delivery of Volvo examples.  Plaxton bodied the MAN 14.220 chassis in 2008 before this was replaced by the MAN 14.240 in 2009.  Users of the Centro include TM Travel, Arriva, Centrebus, GHA Coaches, Wessex Bus and Diamond Bus.  As of 2014, the Centro is no longer available from Plaxton as the parent company Alexander Dennis phased it out in favour of its own Enviro300.\n\nQuestion: The Plaxton Centro is a low floor single-decker bus body designed by Bluebird Vehicles and manufactured by Plaxton, in 2010, Blackpool Transport took delivery of Volvo examples, Blackpool Transport Services Ltd. (BTS) is a bus and tram operator running within the boroughs of Blackpool and Fylde and into the surrounding area, including Fleetwood, Lytham St Annes, Poulton-le-Fylde and Cleveleys, and is owned by which organization?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"bus_body_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the bus body.\"\n    },\n    \"designer\": {\n      \"type\": \"string\",\n      \"description\": \"The entity that designed the bus body.\"\n    },\n    \"manufacturer\": {\n      \"type\": \"string\",\n      \"description\": \"The entity that manufactured the bus body.\"\n    },\n    \"operator_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the bus and tram operator.\"\n        },\n        \"delivery_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the operator took delivery of Volvo examples of the bus body.\"\n        },\n        \"service_areas\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Areas where the operator runs services.\"\n        },\n        \"owner\": {\n          \"type\": \"string\",\n          \"description\": \"The organization that owns the operator.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"delivery_year\",\n        \"service_areas\",\n        \"owner\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"bus_body_name\",\n    \"designer\",\n    \"manufacturer\",\n    \"operator_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "bus_body_name": {
        "type": "string",
        "description": "The name of the bus body."
      },
      "designer": {
        "type": "string",
        "description": "The entity that designed the bus body."
      },
      "manufacturer": {
        "type": "string",
        "description": "The entity that manufactured the bus body."
      },
      "operator_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the bus and tram operator."
          },
          "delivery_year": {
            "type": "integer",
            "description": "The year the operator took delivery of Volvo examples of the bus body."
          },
          "service_areas": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Areas where the operator runs services."
          },
          "owner": {
            "type": "string",
            "description": "The organization that owns the operator."
          }
        },
        "required": [
          "name",
          "delivery_year",
          "service_areas",
          "owner"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "bus_body_name",
      "designer",
      "manufacturer",
      "operator_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
