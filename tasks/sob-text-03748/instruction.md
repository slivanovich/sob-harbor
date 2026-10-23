{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUnited Kingdom Infrared Telescope: UKIRT, the United Kingdom Infra-Red Telescope, is a 3.8 metre (150 inch) infrared reflecting telescope, the second largest dedicated infrared (1 to 30 micrometres) telescope in the world.  Until 2014 it was operated by the Joint Astronomy Centre in Hilo and located on Mauna Kea, Hawai'i as part of Mauna Kea Observatory.  It was owned by the United Kingdom Science and Technology Facilities Council.  UKIRT is currently being funded by NASA and operated under a Scientific Cooperation Agreement among Lockheed Martin Advanced Technology Center, the University of Hawaii, and the University of Arizona.  The telescope is set to be decommissioned after completion of the Thirty Meter Telescope as part of the Mauna Kea Comprehensive Management Plan.\n\nXinglong Station (NAOC): Xinglong Station () is an observatory (IAU code 327) situated south of the main peak of the Yanshan mountains in Hebei province, China.  Installed are seven telescopes: a Mark-III photoelectric astrolabe; a 60 cm reflector; an 85 cm reflector; a 60/90 cm Schmidt telescope; an 1.26-meter infrared telescope; and a 2.16-meter telescope.  The most recent telescope is the 4m LAMOST.  As of 2014 the observatory installed a 5.2-meter telescope as part of their Gamma-ray astronomy program, known colloquially as Sām Tām for its aggressive focal length.  It is a popular tourist site.\n\nThirty Meter Telescope: The Thirty Meter Telescope (TMT) is a proposed astronomical observatory with an extremely large telescope (ELT) that has become the source of controversy over its planned location on Mauna Kea in the US state of Hawaii.  Construction of the TMT on land which is sacred to Native Hawaiian culture and religion attracted international coverage after October 2014, when construction was temporarily halted voluntarily due to protests.  While construction of the telescope was set to resume on April 2 and later on June 24, 2015, it was blocked by further protests each time.  The Board of Land and Natural Resources approved the TMT project, but the State Supreme Court of Hawaii invalidated the building permits in December 2015, ruling that the board had not followed due process.  Roque de los Muchachos Observatory, La Palma, Canary Islands, Spain is the alternative site if construction cannot go forward in Hawaii.  The TMT would become the last area on Mauna Kea on which any telescope will ever be built.\n\nNative Hawaiians: Native Hawaiians (Hawaiian: \"kānaka ʻōiwi\", \"kānaka maoli\", and \"Hawaiʻi maoli\") are the indigenous Polynesian people of the Hawaiian Islands or their descendants.  Native Hawaiians trace their ancestry back to the original Polynesian settlers of Hawaii.\n\nHeinrich Hertz Submillimeter Telescope: The Submillimeter Telescope (SMT), formerly known as the Heinrich Hertz Submillimeter Telescope, is a submillimeter wavelength radio telescope located on Mount Graham, Arizona.  It is a 10-meter-wide parabolic dish inside a building to protect it from bad weather.  The building front doors and roof are opened when the telescope is in use.  The telescope's construction was finished in 1993.  Along with the 12 Meter Telescope on Kitt Peak, this telescope is maintained by the Arizona Radio Observatory, a division of Steward Observatory at the University of Arizona.\n\nHome Rule Party of Hawaii: As soon as the United States annexed the Hawaiian Islands and established the Territory of Hawaii, native Hawaiians became worried that both the Democratic Party of Hawai‘i and Hawai‘i Republican Party were incapable of representing them.  In 1900, native Hawaiians and their supporters created the Hawaiian Independent Party (later renamed the Independent Home Rule Party).\n\nOpposition to the Mauna Kea Observatories: Opposition to the Mauna Kea Observatories has existed since the first telescope was built in the late 1960s.  Originally part of research begun by Gerard Kuiper of the University of Arizona, the site has expanded into the world's largest observatory for infrared and submillimeter telescopes.  Opposition to the telescope from residents in the city of Hilo, Hawaii were concerned about the visual appearance of the mountain and Native Hawaiians voiced concerns over the site being sacred to the Hawaiian religion as the home of several deities.  Environmental groups and activists have been expressing concern over endangered species habitat.  The last proposal in 2006 was canceled after a court order to submit a completed Environmental Impact Statement.  A current proposal for one of the world's largest optical telescopes, the Thirty Meter Telescope is currently the focus of protests concerning the continued development of the mountain Hawaiians consider the most sacred peak in the island chain.\n\nCulture of the Native Hawaiians: The culture of the Native Hawaiians is about 1500 years old and has its origins in the Polynesians who voyaged to and settled Hawaii.  These Native Hawaiians developed culinary, artistic, and religious culture and practices.\n\nCalifornia Extremely Large Telescope: The California Extremely Large Telescope (CELT) was a proposal for an extremely large telescope design first proposed in the 1990s by a consortium of Californian Universities.  The design was for a segmented 30 m diameter astronomical telescope.  The CELT had a positive reception and continued to be developed, and was renamed The Thirty Meter Telescope around 2003-4.  The CELT was one of the earlier and more successful proposals for extremely large telescopes.\n\nThirty Meter Telescope protests: The Thirty Meter Telescope protests are a series of protests and demonstrations that began on the Island of Hawaii in the United States over the choosing of Mauna Kea for the site location of the Thirty Meter Telescope.  Mauna Kea is considered the most sacred mountain of Native Hawaiian religion and culture.  Protests began locally within the state of Hawaii on October 7, 2014 but went global within weeks of the April 2, 2015 arrest of 31 people who had blockaded the roadway to keep construction crews off the summit.\n\nQuestion: Due to concern in regards to the visual appearance of a sacred mountain to Native Hawaiians, the Thirty Meter Telescope has been considered to be built in which alternative site in Spain?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"telescope_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the telescope in question.\"\n    },\n    \"primary_location_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the primary planned location and the issues encountered.\",\n      \"properties\": {\n        \"location_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the primary planned location.\"\n        },\n        \"sacred_to_group\": {\n          \"type\": \"string\",\n          \"description\": \"The group for whom the primary location is sacred.\"\n        },\n        \"reasons_for_opposition\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"A list of reasons for opposition to the telescope's construction at the primary location.\"\n        },\n        \"construction_status\": {\n          \"type\": \"string\",\n          \"description\": \"The current status of construction at the primary location due to opposition.\"\n        }\n      },\n      \"required\": [\n        \"location_name\",\n        \"sacred_to_group\",\n        \"reasons_for_opposition\",\n        \"construction_status\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"alternative_site_details\": {\n      \"type\": \"object\",\n      \"description\": \"Details about the proposed alternative site.\",\n      \"properties\": {\n        \"site_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the alternative observatory site.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the alternative site is located.\"\n        },\n        \"island\": {\n          \"type\": \"string\",\n          \"description\": \"The island where the alternative site is located.\"\n        },\n        \"region\": {\n          \"type\": \"string\",\n          \"description\": \"The specific region or island group where the alternative site is located.\"\n        }\n      },\n      \"required\": [\n        \"site_name\",\n        \"country\",\n        \"island\",\n        \"region\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"telescope_name\",\n    \"primary_location_details\",\n    \"alternative_site_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "telescope_name": {
        "type": "string",
        "description": "The name of the telescope in question."
      },
      "primary_location_details": {
        "type": "object",
        "description": "Details about the primary planned location and the issues encountered.",
        "properties": {
          "location_name": {
            "type": "string",
            "description": "The name of the primary planned location."
          },
          "sacred_to_group": {
            "type": "string",
            "description": "The group for whom the primary location is sacred."
          },
          "reasons_for_opposition": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "A list of reasons for opposition to the telescope's construction at the primary location."
          },
          "construction_status": {
            "type": "string",
            "description": "The current status of construction at the primary location due to opposition."
          }
        },
        "required": [
          "location_name",
          "sacred_to_group",
          "reasons_for_opposition",
          "construction_status"
        ],
        "additionalProperties": false
      },
      "alternative_site_details": {
        "type": "object",
        "description": "Details about the proposed alternative site.",
        "properties": {
          "site_name": {
            "type": "string",
            "description": "The name of the alternative observatory site."
          },
          "country": {
            "type": "string",
            "description": "The country where the alternative site is located."
          },
          "island": {
            "type": "string",
            "description": "The island where the alternative site is located."
          },
          "region": {
            "type": "string",
            "description": "The specific region or island group where the alternative site is located."
          }
        },
        "required": [
          "site_name",
          "country",
          "island",
          "region"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "telescope_name",
      "primary_location_details",
      "alternative_site_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
