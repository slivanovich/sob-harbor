{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNorwegian Young Conservatives: Norwegian Young Conservatives (Norwegian: Unge Høyres Landsforbund, UHL, normally referred to as Unge Høyre) is a Norwegian youth party.  Its ideology is liberal conservatism.  Kristian Tonning Riise succeeded Paul Joakim Sandøy as leader in 2014.\n\nMount Prestrud: Mount Prestrud ( ) is an Antarctic peak over 2,400 m which rises from the southwestern part of the massif at the head of Amundsen Glacier, in the Queen Maud Mountains.  In November 1911, a number of mountain peaks in this general vicinity were observed and rudely positioned by the South Pole Party under Roald Amundsen.  Amundsen named one of them for Lieutenant Kristian Prestrud, first officer of the \"Fram\" and leader of the Norwegian expedition's Eastern Sledge Party to the Scott Nunataks.  The peak described was mapped by the United States Geological Survey (USGS) from surveys and U.S. Navy aerial photography, 1960-64.  For the sake of historical continuity, the Advisory Committee on Antarctic Names (US-ACAN) has selected this feature to be designated Mount Prestrud.\n\nBattle of Høland: The Battle of Høland were two minor skirmishes fought on Mars 9, 1716 in Høland, Norway during the Norwegian campaign of the Great Northern War.  Charles XII of Sweden rode with a force of 650 men in order to capture a Norwegian party stationed at Høland.  The Norwegian troop was completely surprised and 75 men were forced to yield, while only a few managed to escape.  After having received news of the accruing, Norwegian general Ulrik Christian Kruse decided to send a force of his own consisting of 216 troops in order to aid the ones captured at Høland.  He managed to surprise the troops under Charles XII but was, however repulsed after a while of fighting as the Swedish troops realized what was happening and started to actively outnumber the Norwegians.  The Swedes had suffered at least 28 killed and wounded.  In the Norwegian lines Kruse got captured along with 10 of his men, another 31 Norwegians were killed and 47 wounded.  After the victory a good opportunity presented itself for Charles XII to quickly march further into Norway in order to end the campaign in a victory for Sweden.  However, a snow blizzard would end this opportunity and he would instead be stuck in Høland for some days.\n\nKristian Norheim: Kristian Norheim (born 19 April 1976) is a Norwegian politician who has been a member of the Stortinget as an alternate for State Secretary Bård Hoksrud.  He is a member of the Progress Party and an expert on international relations.\n\nKjersti Horn: Kjersti Horn (born 30 June 1977) is a Norwegian theater director and storyboard artist, the daughter of scenographer Per Kristian Horn (born 1941) and the actor, theater director and politician for the Norwegian Labour Party (AP), Ellen Horn (b. Stoesen in 1951), partner with Sound designer and composer Erik Hedin (born 1974, two children), and half sister of Jazz singer and actor Emilie Stoesen Christensen (born 1986).  She was born with the bone disease \"spondylo-epyphyfyseal-dysplasi\".\n\nAlfred Vågnes: Alfred Leonard Kristian Vågnes (13 April 1880 – 12 October 1970) was a Norwegian politician for the Labour Party and later the Communist Party.\n\nKristian Prestrud: Kristian Prestrud (22 October 1881 – 11 November 1927) was a Norwegian naval officer and polar explorer who participated in Amundsen's South Pole expedition between 1910 and 1912.  Prestrud was first officer of the \"Fram\" and leader of the Norwegian expedition's Eastern Sledge Party to the Scott Nunataks.\n\nMinerva (Norwegian periodical): Minerva is a Norwegian liberal conservative periodical that started publishing in 1924.  It was started by members of the Conservative Students' association in Oslo.  In 2017, Nils August Andresen is executive editor, Torbjørn Røe Isaksen editor on society, Kristian Meisingset on culture and Fredrik Gierløff on politics.  Magnus Thue is Chief executive officer.  It receives financial support from Liberal Science Institute, Norwegian Agency for Development Cooperation and the Conservative Party of Norway.\n\nHans Kristian Seip: Hans Kristian Seip (6 November 1881 - 25 March 1945) was a Norwegian road engineer and politician for the Liberal Party.  He spent most of his professional career in the Norwegian Public Roads Administration.  As a politician he was Mayor of Bergen and County Governor of Sogn og Fjordane, and served two terms in the Norwegian Parliament.  He is also known as the father of political scientist Jens Arup Seip.\n\nProgress Party (Norway): The Progress Party (Bokmål: \"Fremskrittspartiet\" , Nynorsk: \"Framstegspartiet\" , FrP) is a political party in Norway which identifies as classical liberal (libertarian) and conservative-liberal.  Academics broadly categorise the party as neoliberal populist, while the party itself, Norway's Prime Minister Erna Solberg, centrist parties, and some scholars reject any comparison with foreign right-wing populist parties.  In coalition with the Conservative Party, the party won the 2013 parliamentary election and entered into its first ever government.\n\nQuestion: Kristian Norheim is a member of a Norwegian party that identifies itself as what ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the politician.\"\n    },\n    \"political_party\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the political party the person is a member of.\"\n    },\n    \"party_ideologies\": {\n      \"type\": \"array\",\n      \"description\": \"A list of ideologies the political party identifies with.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    },\n    \"main_ideology_identified\": {\n      \"type\": \"string\",\n      \"description\": \"The primary ideology the party identifies itself as, as per the question.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"political_party\",\n    \"party_ideologies\",\n    \"main_ideology_identified\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the politician."
      },
      "political_party": {
        "type": "string",
        "description": "The name of the political party the person is a member of."
      },
      "party_ideologies": {
        "type": "array",
        "description": "A list of ideologies the political party identifies with.",
        "items": {
          "type": "string"
        }
      },
      "main_ideology_identified": {
        "type": "string",
        "description": "The primary ideology the party identifies itself as, as per the question."
      }
    },
    "required": [
      "person_name",
      "political_party",
      "party_ideologies",
      "main_ideology_identified"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
