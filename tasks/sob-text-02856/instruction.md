{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMount Sugarloaf (New South Wales): Mount Sugarloaf, also known as \"Great Sugar Loaf\", is a mountain in the lower Hunter Region of New South Wales, Australia, overlooking the cities of Newcastle, Lake Macquarie, Cessnock and Maitland.  The summit of the mountain is in the Lake Macquarie suburb of West Wallsend and access to the summit is gained via this suburb.  However, the mountain itself is also part of the city of Cessnock suburbs Mulbring and Richmond Vale.  It is home to television transmitters that broadcast to the lower Hunter region.  On 18 and 19 July 1965, the mountain received 10 cm of snow.  It also snowed on the summit in the winter of 1975.\n\nHunter Valley cannabis infestation: The Hunter Valley cannabis infestation was an infestation of the marijuana plant, \"Cannabis sativa\" in the Hunter Valley in New South Wales, Australia.  At its peak, the infestation covered about 30 km2 .  It took nine years for the New South Wales government to eradicate it.\n\nHunter Valley Grammar School: Hunter Valley Grammar School is an independent, co-educational, non-denominational day school located in Ashtonfield, a suburb of Maitland, in the lower Hunter Region of New South Wales, Australia.\n\nTelarah railway station: Telarah railway station is located on the North Coast line in New South Wales, Australia.  It serves the northern Maitland suburb of Telarah.  It is served by NSW TrainLink Hunter line services.\n\nWalka Water Works: Walka Water Works is a 19th-century pumping station located near Maitland, New South Wales, Australia.  Originally built in 1887 to supply water to Newcastle and the lower Hunter Valley, it has since been restored and preserved and is part of Maitland City Council's \"Walka Recreation and Wildlife Reserve\".\n\nMaitland, New South Wales: Maitland is a city in the Lower Hunter Valley of New South Wales, Australia and the seat of Maitland City Council, situated on the Hunter River approximately 166 km by road north of Sydney and 35 km north-west of Newcastle.  It is on the New England Highway about 17 km from its start at Hexham.\n\nTelarah, New South Wales: Telarah is a suburb in the City of Maitland, New South Wales, Australia.  The suburb was formerly known as Homeville, however use of this name was abandoned in the 1950s.  It is located on the New England Highway and is also the site of a major rail junction, where the North Coast line and the once extensive, privately owned South Maitland Railway system meet the Main North line.  A station on the North Coast line opened in 1911 and is served by NSW TrainLink's Hunter Line, with services to Newcastle and Dungog.  Telarah has its own fire brigade as well as bowling club, supermarket, pharmacy, takeaway shop and newsagents.\n\nPokolbin, New South Wales: Pokolbin is a rural locality in the Hunter Region of New South Wales Australia.  It is part of the Singleton Council local government area and the city of Cessnock.  The area is the centre of the Lower Hunter Valley wine region.  Pokolbin lies within the Hunter Valley Important Bird Area.\n\nHunter Valley Coal Chain: The Hunter Valley Coal Chain (HVCC) is the chain of coal delivery in New South Wales, Australia from (mainly open-cut) coal mines in the Hunter Region to the Port of Newcastle and domestic coal-fired power stations in the Hunter Valley.  The HVCC essentially follows the path of the Hunter River travelling south-east from the mining areas in the Hunter Valley to Newcastle.\n\nTocal, New South Wales: Tocal (meaning 'plenty' in the local Aboriginal language) is a locality situated in the lower Hunter Valley, of New South Wales, Australia.  Located approximately 11 km north of Maitland, and about 180 km north of Sydney it is located at the junction of the Paterson River and Webbers Creek.\n\nQuestion: Which  city in the Lower Hunter Valley of New South Wales did Telarah railway station  serves the northern of ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"station_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the railway station.\"\n    },\n    \"city_served\": {\n      \"type\": \"string\",\n      \"description\": \"The city that the railway station serves.\"\n    },\n    \"region\": {\n      \"type\": \"string\",\n      \"description\": \"The broader geographical region where the city is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the city is located.\"\n    }\n  },\n  \"required\": [\n    \"station_name\",\n    \"city_served\",\n    \"region\",\n    \"state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "station_name": {
        "type": "string",
        "description": "The name of the railway station."
      },
      "city_served": {
        "type": "string",
        "description": "The city that the railway station serves."
      },
      "region": {
        "type": "string",
        "description": "The broader geographical region where the city is located."
      },
      "state": {
        "type": "string",
        "description": "The state where the city is located."
      }
    },
    "required": [
      "station_name",
      "city_served",
      "region",
      "state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
