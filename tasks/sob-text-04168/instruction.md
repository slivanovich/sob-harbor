{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n2012 FFSA Super League: The 2012 FFSA Super League was the seventh and final edition of the FFSA Super League, the top level domestic association football competition in South Australia.  10 teams competed, all playing each other twice for a total of 18 rounds, with the top five at the end of the year qualifying for the McIntyre final five finals system to determine 1st to 5th place.  The FFSA Super League became defunct at the end of the season, with the FFSA Premier League becoming the top level of domestic football in South Australia, consisting of all teams in the 2012 FFSA Super League, plus the top four teams from the 2012 FFSA Premier League.\n\n2016 Indian Super League finals: The 2016 Indian Super League finals was the third finals series in the 2016 ISL season, the 2016 edition of the men's professional football league in India.  The finals began on 10 December and concluded with the final on 18 December.  The top four teams from the 2016 ISL regular season qualified for the finals with the semi-finals taking place over two-legs before the final in Kochi.\n\n2014 ISL Inaugural International Draft: The 2014 ISL Inaugural International Draft is the second draft in the Indian Super League, the new franchise domestic football league in India.  The draft featured 49 foreign players who were selected by the eight franchises in the ISL.\n\nKerala Blasters FC results by opponent: The Kerala Blasters FC is an Indian football team founded in 2014, after the state of Kerala was awarded a Indian Super League (ISL) franchise.  The team began playing competitive football in the 2014 Indian Super League season.  They plays their home games at the Jawaharlal Nehru Stadium in Kochi.\n\n2015 Kerala Blasters FC season: The 2015 season was Kerala Blasters' second season in Hero Indian Super League since its inception in 2014.  The club were the runner-up in the 2014 ISL tournament where they lost to Atlético de Kolkata 0-1 in the final.  The team management appointed former England-U20 manager Peter Taylor as its new manager for the 2015 season after the departure of David James.\n\nIndian Super League Golden Glove: The Indian Super League Golden Glove is an award recognizing the best goalkeeper in the Indian Super League (ISL) for a given season.  The ISL was founded in 2013; the first Golden Glove was awarded in 2014.  There are 3 winner's so far.\n\n2016 Indian Super League Final: The 2016 Indian Super League Final was a football match between Atlético de Kolkata and Kerala Blasters on 18 December 2016 at the Jawaharlal Nehru Stadium in Kochi, Kerala.  It was the final match of the 2016 Indian Super League season, the third season of the Indian Super League.  The match was the second time these two teams played each other in the Indian Super League final after both sides met in the inaugural 2014 final.  Atlético de Kolkata won that final 1–0.\n\n2014 ISL Inaugural Domestic Draft: The 2014 ISL Inaugural Domestic Draft was the first ever draft from the Indian Super League, the new franchise domestic football league in India.  The draft featured eighty-four Indian domestic players.  They were drafted by six out of the eight franchises featured in the Indian Super League to form the domestic core of the teams.  NorthEast United FC and Goa were the two non-participating teams as they selected their Indian players from both I-League teams, Dempo and Shillong Lajong respectively.  Forty of the eighty-four players up for selection have either played for the India national team or have attended a camp for the national team.\n\nIndian Super League: The Indian Super League (ISL) is a men's professional football league in India.  For sponsorship reasons, the league is officially known as the Hero Indian Super League.  One of the top football leagues in the country, it currently shares the top spot in the Indian football league system with the I-League.  The league comprises 10 teams and will run for five months from November to March starting with the 2017–18 season.\n\n2015 ISL Domestic Draft: The 2015 ISL domestic draft was the second domestic draft from the Indian Super League, the franchise domestic football league in India.  The draft featured 114 players, of which only 40 were picked.  The draft took place in Mumbai on 10 July 2015.\n\nQuestion: The 2015 ISL domestic draft was the second domestic draft for what franchise domestic football league in India officially known as the Hero Indian Super League?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"draft_event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific draft event.\"\n    },\n    \"draft_edition_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the draft's edition relative to others of its type.\"\n    },\n    \"football_league\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The common name of the football league.\"\n        },\n        \"official_name\": {\n          \"type\": \"string\",\n          \"description\": \"The official name of the football league, often including sponsorship.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of the football league, e.g., 'franchise domestic football league'.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the football league is based.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"official_name\",\n        \"type\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"draft_event_name\",\n    \"draft_edition_description\",\n    \"football_league\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "draft_event_name": {
        "type": "string",
        "description": "The name of the specific draft event."
      },
      "draft_edition_description": {
        "type": "string",
        "description": "A description of the draft's edition relative to others of its type."
      },
      "football_league": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The common name of the football league."
          },
          "official_name": {
            "type": "string",
            "description": "The official name of the football league, often including sponsorship."
          },
          "type": {
            "type": "string",
            "description": "The type of the football league, e.g., 'franchise domestic football league'."
          },
          "country": {
            "type": "string",
            "description": "The country where the football league is based."
          }
        },
        "required": [
          "name",
          "official_name",
          "type",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "draft_event_name",
      "draft_edition_description",
      "football_league"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
