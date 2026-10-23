{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWeeksville, Brooklyn: Weeksville is a neighborhood founded by African American freedmen in what is now Brooklyn, New York, United States, part of the present-day neighborhood of Crown Heights.\n\nMatthias Sention Jr.: Matthias Sention Jr. (also spelled Sension, and later as St. John) (November 20, 1628 – December 1728) was a founding settler of Norwalk, Connecticut.\n\nWilliam Dyer (settler): William Dyer (also Dyre) (1609–by 1677) was an early settler of the Colony of Rhode Island and Providence Plantations, a founding settler of both Portsmouth and Newport, and Rhode Island's first Attorney General.  He is best known for being the husband of the Quaker martyr, Mary Dyer, who was executed for her Quaker activism.  Sailing from England as a young man with his wife, Dyer first settled in Boston in the Massachusetts Bay Colony, but like many members of the Boston church became a supporter of the dissident ministers John Wheelwright and Anne Hutchinson during the Antinomian Controversy, and signed a petition in support of Wheelwright.  For doing this, he was disenfranchised and disarmed, and with many other supporters of Hutchinson, he signed the Portsmouth Compact, and settled on Aquidneck Island in the Narragansett Bay.  Within a year of arriving there, he and others followed William Coddington to the south end of the island where they established the town of Newport.\n\nMatthew Marvin Sr.: Matthew Marvin Sr. (March 26, 1600 – December 20, 1678) was a founding settler of Hartford and Norwalk, Connecticut.  He served as a deputy of the General Court of the Colony of Connecticut from Norwalk in the May 1654 session.  He served as a magistrate in 1659.\n\nMill Hill, Trenton, New Jersey: Mill Hill is a historic neighborhood located within the city of Trenton in Mercer County, New Jersey, United States.  It is considered to be part of Downtown Trenton and was added to the National Register of Historic Places in 1977.  The name Mill Hill refers to central New Jersey's first industrial site, a mill, erected in 1679, at the southeast corner of the present Broad Street crossing of the Assunpink Creek.  Mill Hill and its wooden mill were among the holdings of the first settler in the vicinity of Trenton, Mahlon Stacy, a Quaker who arrived in North America in 1678.  The mill was destroyed in a flood.\n\nMatthias Sention Sr.: Matthias Sention Sr. (also spelled Sangins,Sension, Senchion, and later as St. John) (August 9, 1601 – October 19, 1669) was a founding settler of Dorchester, Massachusetts, of Windsor, Connecticut, of Wethersfield, Connecticut and of Norwalk, Connecticut.\n\nStubbs Park–Stonewall Street Historic District: The Stubbs Park–Stonewall Street Historic District in Dublin, Georgia is a residential area that was listed on the National Register of Historic Places in 2002.  The district has been a long-standing residential neighborhood since the 1910s.  The historic neighborhood is bounded by West Moore Street, Lancaster Street, Marion Street, Academy Avenue and Roosevelt Street.  The Dublin Historic Neighborhood Association was formed in 1995 to preserve and improve the historic neighborhood.\n\nWalter Keeler (settler): Walter Keeler (also Keiler) (born 1615) was a founding settler of Norwalk, Connecticut.  There is very little information on him in the historical records.  He is listed among the \"Table of Estates\" settlers of 1655.  He is the brother of Ralph Keeler, the Norwalk settler who is listed among the \"Ludlow Agreement\" settlers of 1650.\n\nWilliam Greene (governor): William Greene Jr. (August 16, 1731November 29, 1809) was the second governor of the state of Rhode Island, serving in this capacity for eight years, five of which were during the American Revolutionary War.  From a prominent Rhode Island family, his father, William Greene Sr., had served 11 terms as a colonial governor of Rhode Island.  His great-grandfather, John Greene Jr. served for ten years as deputy governor of the colony, and his great-great-grandfather, John Greene Sr. was a founding settler of both Providence and Warwick.\n\nDorchester, Boston: Dorchester is a historic neighborhood comprising over 6 mi2 in Boston, Massachusetts, United States.  Originally, Dorchester was a separate town, founded by Puritans who emigrated in 1630 from Dorchester, Dorset, England.  This dissolved municipality, Boston's largest neighborhood by far, is often divided by city planners in order to create two planning areas roughly equivalent in size and population to other Boston neighborhoods.\n\nQuestion: Matthias Sention Sr. was a founding settler of a historic neighborhood founded by Puritans who emigrated in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"settler_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the founding settler.\"\n    },\n    \"neighborhood_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the historic neighborhood.\"\n    },\n    \"founding_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"founded_by_group\": {\n          \"type\": \"string\",\n          \"description\": \"The group that founded the neighborhood.\"\n        },\n        \"emigration_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the founding group emigrated.\"\n        },\n        \"original_location\": {\n          \"type\": \"string\",\n          \"description\": \"The location from which the founding group emigrated.\"\n        }\n      },\n      \"required\": [\n        \"founded_by_group\",\n        \"emigration_year\",\n        \"original_location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"settler_name\",\n    \"neighborhood_name\",\n    \"founding_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "settler_name": {
        "type": "string",
        "description": "The name of the founding settler."
      },
      "neighborhood_name": {
        "type": "string",
        "description": "The name of the historic neighborhood."
      },
      "founding_details": {
        "type": "object",
        "properties": {
          "founded_by_group": {
            "type": "string",
            "description": "The group that founded the neighborhood."
          },
          "emigration_year": {
            "type": "integer",
            "description": "The year the founding group emigrated."
          },
          "original_location": {
            "type": "string",
            "description": "The location from which the founding group emigrated."
          }
        },
        "required": [
          "founded_by_group",
          "emigration_year",
          "original_location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "settler_name",
      "neighborhood_name",
      "founding_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
