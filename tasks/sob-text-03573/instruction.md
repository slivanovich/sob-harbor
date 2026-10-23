{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLlwytmor: Llwytmor is a satellite peak of Foel-fras, and forms a part of the Carneddau.  The summit has cairns and a shelter.  Good views of the Menai Strait, the Bera's and the Northern Carneddau.  The area is often frequented by the Carneddau mountain pony.  This peak is very unfrequented.  Its full name Llwytmor Uchaf means \"upper grey sea\".\n\nBuffalo Hill (Hong Kong): Buffalo Hill () is a hill located in Ma On Shan Country Park west of Sai Kung, in the eastern half of Hong Kong.  It is particularly well known for its peak resembling the head of a Buffalo when viewed from Sha Tin.  MacLehose trail passes within 225 metres from the peak of the hill, while smaller trails cut off the main MacLehose trail up to the peak of Buffalo Hill.  It is the sixteenth tallest peak in Hong Kong, with an altitude of 606 metres (1,988 ft), bordering Sha Tin and Sai Kung.\n\nBukit Tabur: Bukit Tabur is a hill located in Selangor, Malaysia.  It is also known locally as Bukit Hangus.  The hill is very prominent as it is part of Klang Gates Quartz Ridge and can be seen from the Kuala Lumpur Middle Ring Road 2.  The hill, which is less than 500 metres, is a quartz ridge.  Climbers enter the hiking trail via Kampung Klang Gates, 50 metres from the gates of the Klang Gates Dam, at the back of Taman Melawati for a 3-4 hour climb.  The Gombak Forest Reserve and Klang Gates Dam are beside the hill.  The peak offers view of the dam and panoramic views of Kuala Lumpur from the north.  Several endemic species of plant such as \"Aleisanthia rupestris\" are known to grow here.\n\nAnchor Crag: Anchor Crag ( ) is a rocky crag on the north side of Airy Glacier, 4 nmi north-northeast of Mount Gilbert, in the central part of the Antarctic Peninsula.  It was photographed from the air by the Ronne Antarctic Research Expedition on November 27, 1947, and surveyed by the Falkland Islands Dependencies Survey, November 4, 1958.  The United Kingdom Antarctic Place-Names Committee name is descriptive of a snow patch lodged on the face of the rock which, in 1958, closely resembled a ship's anchor.\n\nHundsheimer Berg: Hundsheimer Berg is a hill located in the Hundsheimer Berge hill range in Lower Austria, Austria close to the border with Slovakia.  Its peak is 481 m above sea level which makes it the highest hill in the Hundsheimer Berge.  The north slopes of the Hundsheimer Berg are covered with forests while the southern slopes have a steppe vegetation.  Since 1965, a nature reserve with the same name, \"Hundsheimer Berg\", is located on these southern slopes.\n\nPike of Stickle: Pike of Stickle, also known as Pike o’ Stickle, is a fell in the English Lake District.  It reaches a height of 709 metres (2,326 feet) and is situated in the central part of the national park in the valley of Great Langdale.  The fell is one of three fells which make up the picturesque Langdale Pikes (the others being Harrison Stickle and Loft Crag), one of the best-known areas in Lakeland.  A \"stickle\" is a hill with a steep prominent rocky top, while a \"pike\" is a hill with a peaked summit, the name being therefore partly tautological.\n\nTodd Crag: Todd Crag is a hill and a satellite peak of Loughrigg Fell at 224 m (735 ft) it is not classed as a fell but is a vantage point near Ambleside\n\nLoughrigg Fell: Loughrigg Fell is a hill in the central part of the English Lake District.  It stands on the end of the long ridge coming down from High Raise over Silver How towards Ambleside, and is separated from its neighbours by the depression of Red Bank.\n\nPapoose Peak Jumps: Papoose Peak Jumps was a ski jumping hill located at Squaw Valley Ski Resort in the US state of California.  The hill consisted of three jumps, with K-points of 80, 60 and 40 meters, respectively.  Constructed upon the hill-side of Little Papoose Peak, it was built for the 1960 Winter Olympics; the 80-meter hill hosted the ski jumping event and the 60-meter hill the Nordic combined event.  The jump was designed by Heini Klopfer and opened in 1958.  After the Olympics the venue saw little use; it was renovated for the 1976 US National Ski Jumping Championships, but has since fallen into disrepair and demolished to make room for a ski lift.\n\nWhoap: Whoap is a hill located near the western edge of the English Lake District, standing at 511 m.  It is part of the Lank Rigg group and is separated from this fell by an unnamed col.  Whoap is not listed as a Wainwright, although it is briefly mentioned in the chapters for Lank Rigg and Crag Fell in Volume 7: \"The Western Fells\".\n\nQuestion: Todd Crag is a hill and a satellite peak of a hill located in the central part of where?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"satellite_peak_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the satellite peak.\"\n    },\n    \"parent_peak_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the main peak that the satellite peak is part of.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"region\": {\n          \"type\": \"string\",\n          \"description\": \"The main geographical region where the parent peak is located.\"\n        },\n        \"part_of_region\": {\n          \"type\": \"string\",\n          \"description\": \"A more specific description of the location within the region.\"\n        }\n      },\n      \"required\": [\n        \"region\",\n        \"part_of_region\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"satellite_peak_name\",\n    \"parent_peak_name\",\n    \"location_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "satellite_peak_name": {
        "type": "string",
        "description": "The name of the satellite peak."
      },
      "parent_peak_name": {
        "type": "string",
        "description": "The name of the main peak that the satellite peak is part of."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "region": {
            "type": "string",
            "description": "The main geographical region where the parent peak is located."
          },
          "part_of_region": {
            "type": "string",
            "description": "A more specific description of the location within the region."
          }
        },
        "required": [
          "region",
          "part_of_region"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "satellite_peak_name",
      "parent_peak_name",
      "location_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
