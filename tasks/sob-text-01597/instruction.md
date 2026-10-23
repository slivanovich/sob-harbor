{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTrient Hut: The Trient hut (French: Cabane du Trient) is a mountain hut in the Swiss alps, near the Swiss town of Martigny and the French town of Chamonix.  The hut sits at an altitude of 3,170 m (10,400 ft), on a rock perched above the Trient Glacier.  It can be reached on foot by mountaineers and strong hikers with experience of glacier travel.  From the hut you can walk to the Albert Premier and Argentière huts in France, as well as the Cabane de Saleina (Switzerland) at the foot of the Aiguille d'Argentière.  The hut is run by the SAC, the Swiss Alpine Club, and has 130 beds.  It is a popular base for mountaineers exploring the area, e.g. Aiguille du Tour etc.\n\nKleiner Mythen: The Kleiner Mythen is a mountain in the Schwyzer Alps of Central Switzerland.  The mountain lies in the canton of Schwyz, to the east of the town of Schwyz, to the south of the village of Alpthal in the valley of the Alp river, and to the north of the Grosser Mythen.\n\nGrosser Mythen: The Grosser Mythen (also \"Grosse Mythe\") is a mountain in the Schwyzer Alps of Central Switzerland.  The mountain lies in the canton of Schwyz, to the east of the town of Schwyz, and to the south of the village of Alpthal in the valley of the river Alp.\n\nQuartiere: A quartiere (] ; plural: quartieri) is a territorial subdivision of certain Italian towns.  The word derives from \"quarto\", or fourth, and was thus properly used only for towns divided into four neighborhoods by the two main roads.  It has been later used as a synonymous of neighbourhood, and an Italian town can be now subdivided into a greater number of \"quartieri\".  The Swiss town of Lugano (in the Italian-speaking canton of Ticino) is subdivided into quarters also.\n\nLocarno: Locarno (] , ] ; Ticinese: \"Locarn\" ] ; formerly in German: \"Luggárus\" ] ) is a southern Swiss town and municipality in the district Locarno (and its capital), located on the northern shore of Lake Maggiore at its northeastern tip in the canton of Ticino at the southern foot of the Swiss Alps.  It has a population of about 16,000 (proper), and about 56,000 for the agglomeration of the same name including Ascona besides other municipalities.\n\nMatterhorn: The Matterhorn (German: Matterhorn , ] ; Italian: Cervino , ] ; French: Le Cervin , ] ) is a mountain of the Alps, straddling the main watershed and border between Switzerland and Italy.  It is a large, near-symmetrical pyramidal peak in the extended Monte Rosa area of the Pennine Alps, whose summit is 4478 m high, making it one of the highest summits in the Alps and Europe.  The four steep faces, rising above the surrounding glaciers, face the four compass points and are split by the \"Hörnli\", \"Furggen\", \"Leone\", and \"Zmutt\" ridges.  The mountain overlooks the Swiss town of Zermatt, in the canton of Valais, to the north-east and the Italian town of Breuil-Cervinia in the Aosta Valley to the south.  Just east of the Matterhorn is Theodul Pass, the main passage between the two valleys on its north and south sides, and a trade route since the Roman Era.\n\nSchwyz: The town of Schwyz (] ; French: \"Schwytz\" ; Italian: \"Svitto\" ) is the capital of the canton of Schwyz in Switzerland.\n\nEinsiedlerhaus: Einsiedlerhaus is a historic building with an adjoint garden which is part of the former town wall of the medieval Swiss town of Rapperswil in the Canton of St. Gallen.\n\nAlp (river): The Alp is a river in the Swiss canton of Schwyz and a tributary of the Sihl.  It has a length of 19.3 km .  The river rises on the northwestern flanks of the Brünnelistock and the northern flanks of the Kleiner and Grosser Mythen mountains near Brunni, and flows in generally northerly direction through the village of Alpthal, the village of Trachslau, the town of Einsiedeln and the village of Biberbrugg.  At Biberbrugg, the river Biber joins the Alp.  Some 2 km north of Biberbrugg, at Dreiwässern the Alp flows into the Sihl.\n\nMetro Alpin: The Metro Alpin is an underground funicular situated above the Swiss town of Saas Fee, in the canton of Valais.  Opened in 1984, it links the Felskinn cable-car station (2980 m MSL) on the shore of the Fee Glacier to the Mittelallalin (3456 m ) in the north flank of the Allalinhorn.  The Felskinn–Mittelallalin Tunnel has a length of 1,749 m , with an altitude difference of 476 m between the two stations.\n\nQuestion: What Swiss town near the Kleiner Mythen is also the name of the canton it's located in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Swiss town.\"\n    },\n    \"canton_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the canton where the town and mountain are located.\"\n    },\n    \"mountain_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the mountain near the town.\"\n    },\n    \"is_canton_capital\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the town is the capital of its canton.\"\n    },\n    \"location_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the town's location relative to the mountain.\"\n    }\n  },\n  \"required\": [\n    \"town_name\",\n    \"canton_name\",\n    \"mountain_name\",\n    \"is_canton_capital\",\n    \"location_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "town_name": {
        "type": "string",
        "description": "The name of the Swiss town."
      },
      "canton_name": {
        "type": "string",
        "description": "The name of the canton where the town and mountain are located."
      },
      "mountain_name": {
        "type": "string",
        "description": "The name of the mountain near the town."
      },
      "is_canton_capital": {
        "type": "boolean",
        "description": "Indicates if the town is the capital of its canton."
      },
      "location_description": {
        "type": "string",
        "description": "A description of the town's location relative to the mountain."
      }
    },
    "required": [
      "town_name",
      "canton_name",
      "mountain_name",
      "is_canton_capital",
      "location_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
