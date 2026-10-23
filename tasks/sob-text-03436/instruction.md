{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHumanitarian aid: Humanitarian aid is material and logistic assistance to people who need help.  It is usually short-term help until the long-term help by government and other institutions replaces it.  A report published by the network of European Universities on Professionalization of Humanitarian Action noted that humanitarian aid is a \"fundamental expression of the universal value of solidarity between people and a moral imperative.\"  Among the people in need belong homeless, refugees, victims of natural disasters, wars and famines.  The primary purpose of humanitarian aid is to save lives, reduce suffering and respect to human dignity.  Humanitarian aid is material or logistical assistance provided for humanitarian purposes, typically in response to humanitarian crises including natural disasters and man-made disaster.  The primary objective of humanitarian aid is to save lives, alleviate suffering, and maintain human dignity.  It may therefore be distinguished from development aid, which seeks to address the underlying socioeconomic factors which may have led to a crisis or emergency.\n\nTactical Emergency Medical Services: Tactical Emergency Medical Services (TEMS) is out-of-hospital care given in hostile situations by specially trained practitioners.  It is distinct from the care given by medics in war zones, as TEMS generally refers to care rendered by civilians. Tactical Medics are Emergency medical technicians (EMT), paramedics, nurses, and physicians who are trained to provide life-saving care and, sometimes, transport in situations such as tactical police operations, active shooters, bombings, and natural disasters (though rarely the latter).\n\nDisaster Action: Disaster Action was founded as a charity in 1991 by survivors and bereaved people from UK and overseas disasters.  In the late 1980s, there were a number of serious incidents in which many lives were lost, such as the sinking of the MV Jupiter (1961), Hillsborough, the Herald of Free Enterprise, Lockerbie, the Marchioness, Piper Alpha and UTA Flight 772.  One individual from the Herald Families Association began to realise that the issues the Herald families were experiencing would almost certainly be encountered by others in similar disasters.  Maurice de Rohan therefore gathered together a group of people in circumstances that paralleled his, and so the charity Disaster Action was set up.  By 2014, members had personal experience of 29 disasters, including rail, air and maritime as well as natural disasters and terrorist attacks in the UK and overseas.\n\nAnn Curry: Ann Curry (born November 19, 1956) is an American television personality, news journalist and photojournalist.  Curry has been a reporter for more than 30 years, focused on human suffering in war zones and natural disasters.  Curry has reported from the wars in Syria, Palestine, Darfur, Congo, the Central African Republic, Kosovo, Lebanon, Israel, Afghanistan and Iraq, among others.  Curry has covered numerous disasters, including the tsunamis in Southeast Asia and the 2010 earthquake in Haiti, where her appeal via Twitter topped Twitter's 'most powerful' list, credited for helping speed the arrival of humanitarian planes.\n\nNatural disasters in Japan: Japan is one of the countries most affected by natural disasters. Two out of the five most expensive natural disasters in recent history have occurred in Japan, costing $181 billion in the years 2011 and 1995 only.  Japan has also been the site of some of the 10 worst natural disasters of the 21st century.  The types of natural disasters in Japan include tsunamis, floods, typhoons, earthquakes, cyclones and volcanic eruptions.  The country has gone through many years of natural disasters, affecting its economy, development, and social life.  One of the earth quakes Japan has suffered from is the Kobe earthquake\n\nGentleman's Intermission: \"Gentleman's Intermission\" is the of the fifth season of the American television comedy series \"30 Rock\", and the 86th overall episode of the series.  It was written by co-executive producer John Riggi and directed by series producer Don Scardino.  The episode originally aired on the National Broadcasting Company (NBC) network in the United States on November 4, 2010.  Elizabeth Banks and Buck Henry guest star in this episode, and there are cameo appearances by Ann Curry, Lester Holt, and Meredith Vieira.\n\nList of natural disasters in New Zealand: This list of natural disasters in New Zealand documents notable natural disasters and epidemics that have occurred in New Zealand since 1843.  Of these natural disasters, the 1918 flu pandemic resulted in the highest loss of life.\n\nList of disasters in Thailand: Many disasters have occurred in Thailand, leading to loss of life and economic damages.  Most natural disasters that have happened in the country are storm- and flood-related, while man-made disasters have also caused great losses.  This page lists by date accidents and disasters which have caused significant losses or been the focus of national public attention, grouped into natural and man-made disasters.\n\nCRESTA: CRESTA (Catastrophe Risk Evaluation and Standardizing Target Accumulations) was founded as a joint project of Swiss Reinsurance Company, Gerling-Konzern Globale Reinsurance Company, and Munich Reinsurance Company.  CRESTA has set itself the aim of establishing a globally uniform system for the accumulation risk control of natural hazards - particularly earthquakes, storms and floods.  Those risk zones are essentially based on the observed and expected seismic activity, as well as on other natural disasters, such as droughts, floods and storms.  CRESTA zones regard the distribution of insured values within a region or country for easier assessment of risks.  CRESTA Zones are the essential basis for reinsurance negotiation and portfolio analysis.  Nowadays, CRESTA sets widely accepted standards which apply throughout the international insurance industry.  CRESTA zone information is used by most insurers for assessing the insurance catastrophe premiums they will charge.\n\nList of natural disasters in Indonesia: Natural disasters in Indonesia can usefully be divided into major disasters, medium level disasters, and lesser disasters which although causing less damage are very common across Indonesia.  These can conveniently be considered as macro, mezzo, and micro events.  Policies to respond to natural disasters in Indonesia, which are still in an early stage of being developed, need to develop strategies to deal with each of these different types of disasters.\n\nQuestion: What reporter with 30 years of experience, focused on human suffering in war zones and natural disasters, had a cameo appearance in \"Gentleman's Intermission\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"reporter_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the reporter.\"\n    },\n    \"experience_years\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of years of experience the reporter has.\"\n    },\n    \"focus_areas\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Key areas of focus for the reporter's work.\"\n    },\n    \"episode_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"episode_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the episode where the appearance occurred.\"\n        },\n        \"appearance_type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of appearance in the episode (e.g., cameo).\"\n        }\n      },\n      \"required\": [\n        \"episode_title\",\n        \"appearance_type\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"reporter_name\",\n    \"experience_years\",\n    \"focus_areas\",\n    \"episode_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "reporter_name": {
        "type": "string",
        "description": "The name of the reporter."
      },
      "experience_years": {
        "type": "integer",
        "description": "The number of years of experience the reporter has."
      },
      "focus_areas": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Key areas of focus for the reporter's work."
      },
      "episode_details": {
        "type": "object",
        "properties": {
          "episode_title": {
            "type": "string",
            "description": "The title of the episode where the appearance occurred."
          },
          "appearance_type": {
            "type": "string",
            "description": "The type of appearance in the episode (e.g., cameo)."
          }
        },
        "required": [
          "episode_title",
          "appearance_type"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "reporter_name",
      "experience_years",
      "focus_areas",
      "episode_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
