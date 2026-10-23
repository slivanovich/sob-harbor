{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPatjuk: Patjuk (팥죽 ) or red bean porridge is a type of juk (Korean porridge) consisting of red beans and rice.  The food is traditionally eaten on \"dongji\" (winter solstice).\n\nJuba (food): Juba was a food that was traditionally eaten by slaves in the United States colonies who worked on plantations.  It was made up of a mixture of leftovers and was cooked in a large pot.\n\nWake (ceremony): A wake is a social gathering associated with death, usually held before a funeral.  Traditionally, a wake takes place in the house of the deceased with the body present; however, modern wakes are often performed at a funeral home or another convenient location.  In the United States and Canada it is synonymous with a viewing.  It is often a social rite that highlights the idea that the loss is one of a social group and affects that group as a whole.\n\nDead-cakes: A dead-cake is a type of food that is traditionally eaten at a wake to honour the deceased individual.  It is closely related to the folklore of funeral customs.\n\nSongpyeon: Songpyeon (송편 ) is a traditional Korean food made of glutinous rice.  It is a type of \"tteok\", small rice cakes, traditionally eaten during the Korean autumn harvest festival, Chuseok.  It became a popular symbol of traditional Korean culture.  The earliest records of songpyeon date from the Goryeo period.\n\nHot cross bun: A hot cross bun is a spiced sweet bun made with currants or raisins, marked with a cross on the top, and traditionally eaten on Good Friday in the British Isles, Australia, Canada, India, Ireland, New Zealand, South Africa and some parts of America.  The buns mark the end of Lent and different parts of the hot cross bun have a certain meaning, including the cross representing the crucifixion of Jesus, and the spices inside signifying the spices used to embalm him at his burial.  They are now available all year round in some places.  Hot cross buns may go on sale in the United Kingdom, Australia and New Zealand as early as New Year's Day or after Christmas.\n\nSteamed bread: Steamed bread is a kind of bread, typically made from wheat, that is prepared by steaming instead of baking.  Steamed bread is produced and consumed all around the world.  In Chinese cuisine, \"mantou\" is a staple food of northern China, where up to 70% of flour production in the region is used to make it.  There are now many variations of mantou in China, for example wholemeal mantou, milk mantou, and sweet potato mantou.  Wotou is another steamed bread found in northern China.  In South African cuisine, a number of groups produce steamed bread, such as the Zulu \"ujeqe\" which can be eaten alone or with tomato soup.  South African steamed breads are typically made at home for consumption on the same day, but research on commercial production continues to advance, aided by earlier developments in the mass production of Chinese steamed bread.  In the cuisine of the United States, one example of steamed bread is Boston brown bread, a sweet food which may be eaten as a dessert.\n\nU.S. Amateur Public Links: The U.S. Amateur Public Links Championship, often referred to as the Public Links or the Publinx, was a men's amateur golf tournament, one of 10 individual amateur championships organized by the United States Golf Association.  The USGA typically called the event the U.S. Amateur Public Links, which it has registered as a service mark.  The tournament was devised as a championship for golfers who played on public courses, as members of private clubs were barred from entry.  In February 2013, the USGA announced that the event would be discontinued after its 2014 edition, and would be replaced by a new men's amateur four-ball championship.\n\nMoist county: In the United States, a moist county is a county in between a \"dry county\" (where the sale of alcoholic beverages is prohibited) and a \"wet county\" (where alcohol is sold).  The term is typically used for any county that allows alcohol to be sold in certain situations, but has limitations on alcohol sales that a normal \"wet\" county would not have.  Some historically \"dry\" counties are switching to this system to avoid losing money to businesses in other counties, but do not wish to become completely \"wet.\"  The term in itself does not have any specific meaning, just that the county is not completely \"wet\" but is not \"dry\", either.  The terms are applicable in states in which each county makes its own rules on alcohol sales.  A \"dry\" county that contains one or more \"wet\" cities is typically called \"moist\".\n\nViewing (funeral): In funeral services, a viewing (sometimes referred to as calling hours, reviewal, funeral visitation or a wake in the United States, Canada and Ireland) is the time that the family and friends come to see the deceased after they have been prepared by a funeral home.  It is generally recommended that any body to be viewed be embalmed in order to create the best possible presentation of the deceased.  A viewing may take place at the funeral parlor, in a family home or at a church or chapel prior to the actual funeral service.  Some cultures, such as the Māori of New Zealand, often take the body to the Marae or tribal community hall.\n\nQuestion: What is a type of food traditionally eaten at an event before a funeral, typically called a viewing in the United States and Canada?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"food_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the food traditionally eaten.\"\n    },\n    \"event_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"event_type\": {\n          \"type\": \"string\",\n          \"description\": \"The primary name of the event where the food is eaten.\"\n        },\n        \"synonyms_in_us_canada\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Other names for the event in the United States and Canada.\"\n        },\n        \"event_timing\": {\n          \"type\": \"string\",\n          \"description\": \"When the event typically takes place relative to a funeral.\"\n        }\n      },\n      \"required\": [\n        \"event_type\",\n        \"synonyms_in_us_canada\",\n        \"event_timing\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"food_purpose\": {\n      \"type\": \"string\",\n      \"description\": \"The reason or purpose for eating the food at the event.\"\n    }\n  },\n  \"required\": [\n    \"food_name\",\n    \"event_details\",\n    \"food_purpose\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "food_name": {
        "type": "string",
        "description": "The name of the food traditionally eaten."
      },
      "event_details": {
        "type": "object",
        "properties": {
          "event_type": {
            "type": "string",
            "description": "The primary name of the event where the food is eaten."
          },
          "synonyms_in_us_canada": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Other names for the event in the United States and Canada."
          },
          "event_timing": {
            "type": "string",
            "description": "When the event typically takes place relative to a funeral."
          }
        },
        "required": [
          "event_type",
          "synonyms_in_us_canada",
          "event_timing"
        ],
        "additionalProperties": false
      },
      "food_purpose": {
        "type": "string",
        "description": "The reason or purpose for eating the food at the event."
      }
    },
    "required": [
      "food_name",
      "event_details",
      "food_purpose"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
