{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCalico, San Bernardino County, California: Calico is a ghost town and former mining town in San Bernardino County, California, United States.  Located in the Calico Mountains of the Mojave Desert region of Southern California, it was founded in 1881 as a silver mining town, and today has been converted into a county park named \"Calico Ghost Town\".  Located off Interstate 15, it lies 3 mi from Barstow and 3 miles from Yermo.  Giant letters spelling \"CALICO\" can be seen on the Calico Peaks behind the ghost town from the freeway.  Walter Knott purchased Calico in the 1950s, architecturally restoring all but the five remaining original buildings to look as they did in the 1880s.  Calico received California Historical Landmark #782, and in 2005 was proclaimed by then-Governor Arnold Schwarzenegger to be California's Silver Rush Ghost Town.\n\nPoeville, Nevada: Poeville, also known as Peavine until 1863, is the site of a historical mining town, established in 1864.  John Poe, a professional promoter from Michigan allegedly related to Edgar Allan Poe, discovered rich gold and silver veins in 1862 on the slopes of Peavine Mountain.  After the discovery of ore, Poe announced that the veins comprised the next Comstock Lode; he presented extracted ore at the state fair of 1864 as rich in content.  As a result, the former mining camp, called Poe City (Poeville) or Podunk (Poedunk), grew to 200 people by 1864.  Ore production in the mining district and population peaked around 1873-1874 with several hundred people living in town, supported by three hotels and a post office.  The post office, named \"Poeville\", operated between September 1, 1874, and March 24, 1878.\n\nMogollon, New Mexico: Mogollon, also called the Mogollon Historic District, is a former mining town located in the Mogollon Mountains in Catron County, New Mexico, in the United States.  Located east of Glenwood and Alma, it was founded in the 1880s at the bottom of Silver Creek Canyon to support the gold and silver mines in the surrounding mountains.  A mine called \"Little Fannie\" became the most important source of employment for the town's populus.  During the 1890s Mogollon had a transient population of between 3,000 and 6,000 miners and, because of its isolation, had a reputation as one of the wildest mining towns in the West.  Today Mogollon is listed as Fannie Hill Mill and Company Town Historic District on the National Register of Historic Places.\n\nLittle Church in the Pines: The Little Church in the Pines is a c. 1902-1908 building in the former mining town of Salina in Boulder County, Colorado.  The church held regular Sunday School classes for children, and services whenever a traveling minister came to town.  As the mining boom came to an end and the town's population shrunk, the building fell into disuse, and briefly served as a mine office before being abandoned.  In 1948 it was purchased by a neighborhood group and has been used ever since for nondenominational worship and community events.  The Little Church in the Pines was placed on the National Register of Historic Places in 1989.\n\nSalina, Colorado: Salina is a former mining town in Boulder County, Colorado, United States approximately 7 mi west of Boulder.  Established in 1874, after Colorado's first gold discovery in 1859, Salina was founded by miners who migrated to Boulder from Salina, Kansas.  It is located at the junction of Four Mile Canyon and Gold Run roads.  The mining camp was originally accessible only by horseback or wagons pulled by mules but later became part of Colorado's Switzerland Trail when the Greeley, Salt Lake, & Pacific narrow gauge railroad was built in the early 1880s.  Today, most of Salina's original structures still stand, including the one-room schoolhouse, Salina School, and church, the Little Church in the Pines, despite the state's worst wildfire in 2010 and historic flooding during the 2013 Colorado floods.\n\nTlalpujahua: Tlalpujahua (    ; formally Tlalpujahua de Rayón) is a town and municipality located in the far northeast of the state of Michoacán in central Mexico.  It is a former mining town, home of the Dos Estrellas Mine, which was the leading producer of gold in the early 20th century.  A major landslide of mud and mining debris damaged this mine and buried about one-third of the town in 1937, effectively ending mining.  In the 1960s, a local by the name of Joaquín Muñoz Orta began making Christmas tree ornaments here.  This eventually grew into what is now one of the largest producers of ornaments called Adornos Navideños SA de CV.  In addition to this and another factory, there are about 150 small workshops dedicated to making Christmas items, with about 70% of the town’s economy based on it.  In 2005, the town, with its narrow stone streets and adobe/stone houses with red tile roofs, was made a Pueblo Mágico as part of its efforts to attract tourism.\n\nSunrise, Wyoming: Sunrise was a company mining town of the Colorado Fuel and Iron Company located in Platte County, Wyoming.  The entire site of the former mining district and town is on the National Register of Historic Places.\n\nSchladming: Schladming is a small former mining town in the northwest of the Austrian state of Styria that is now a popular tourist destination.  It has become a large winter sports resort and has held various skiing competitions, including most notably the FIS Alpine World Ski Championships 1982 and the FIS Alpine World Ski Championships 2013.  The shopping area has many cafes, restaurants and a variety of shops that cater to tourists.\n\nGolden Fleece Tunnel (California): The Golden Fleece Tunnel, is a gold mining site in the Westville gold mining district in Placer County, California.  The mine is located 2 miles northeast of the former mining town Westville, California, north to the Foresthill Divide Road.  It has a 3000 ft tunnel and was operated successfully by the Golden Fleece Mining and Milling Company (New York).  The mine is no longer in operation.  Other nearby mines are the Hogsback Tunnel and the Union Tunnel.\n\nRohrmoos-Untertal: Rohrmoos-Untertal is a former municipality in the district of Liezen in Styria, Austria.  Since the 2015 Styria municipal structural reform, it is part of the municipality Schladming.\n\nQuestion: Since 2015 Rohrmoos-Untertal is a part of a former mining town that is now a popular what?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former municipality.\"\n    },\n    \"year_of_reform\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the municipal structural reform took place.\"\n    },\n    \"new_municipality\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the municipality it became part of.\"\n        },\n        \"original_status\": {\n          \"type\": \"string\",\n          \"description\": \"The historical status of the new municipality.\"\n        },\n        \"current_status\": {\n          \"type\": \"string\",\n          \"description\": \"The current popular status of the new municipality.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the municipality is located.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"original_status\",\n        \"current_status\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"year_of_reform\",\n    \"new_municipality\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the former municipality."
      },
      "year_of_reform": {
        "type": "integer",
        "description": "The year the municipal structural reform took place."
      },
      "new_municipality": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the municipality it became part of."
          },
          "original_status": {
            "type": "string",
            "description": "The historical status of the new municipality."
          },
          "current_status": {
            "type": "string",
            "description": "The current popular status of the new municipality."
          },
          "country": {
            "type": "string",
            "description": "The country where the municipality is located."
          }
        },
        "required": [
          "name",
          "original_status",
          "current_status",
          "country"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "entity_name",
      "year_of_reform",
      "new_municipality"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
