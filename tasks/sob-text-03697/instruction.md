{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGrupo Bimbo: Grupo Bimbo, S.A.B. de C.V., known as Bimbo, is a Mexican multinational bakery product manufacturing company headquartered in Mexico City, Mexico.  It is the world's largest baking company and operates the largest bakeries in the United States, Mexico, Canada, Chile and Spain, and has some of the widest distribution networks in Mexico and the United States.  It was also the ninth largest company of Mexico by revenues in 2013.\n\nGansito: Gansito (Spanish \"little goose\"), is a Mexican snack cake, which is similar to the Twinkie, with the exception of strawberry jelly along with the creamy filling and that it is covered in chocolate with chocolate sprinkle topping.  It was created in 1957 by Marinela (the pastries division of the breadmaking Bimbo brand).  Gansito is one of the first three products to emerge from this brand.  This specific snack cake is heavily marketed, possibly more than any other of Bimbo's products which include white and wheat bread, cereal bars, pound cakes and several other cakes, various pastries, cookies, and wafers.\n\nBubu Lubu: Bubu Lubu is a popular trademark for candies from Mexico, featuring a strawberry and marshmallow filling with a chocolate covering.  It is manufactured by Barcel (under the control of the Bimbo Company).  Bubulubu is accompanied by the trademark Ricolino, also property of Grupo Bimbo.  Bubulubu is currently available in some H.E.B. grocery stores and Wal-Mart stores in Texas, Mercado del Pueblo in Georgia, as well as in some Chicago, Los Angeles and Miami, Florida area Target stores, as well as NV gas stations and Mexican owned grocery stores in Colorado New Brunswick, NJ, and Dollar General stores in North Carolina.  Its packaging describes the candy as \"\"jalea y malvavisco cubiertos con sabor chocolate\"\" or \"jelly and marshmallow with chocolate flavored coating\".\n\nBrioche Dorée: Brioche Dorée is a French chain of Bakery/Café restaurants founded in 1976 and originally started in Brest.  The company was founded by Louis Le Duff, current president of Groupe Le Duff.  The chain has worldwide operations and is the second largest Bakery/Café chain in the world.  It serves over 200,000 customers every day and operates over 500 restaurants.  The name means \"Golden Brioche\" in French.\n\nLorenzo Servitje: Lorenzo Servitje Sendra, commonly known as Lorenzo Servitje, (November 20, 1918 – February 3, 2017) was a Mexican accountant, businessman magnate, and philanthropist who co-founded Grupo Bimbo, the world's largest bakery company, in 1945 with a group of four business partners, including Jaime Jorba, Jaime Sendra, Alfonso Velasco and José T. Mata.  Servitje is credited with expanding Bimbo from a small, Mexican baking company into a multinational conglomerate that has acquired several more than 100 domestic and international brands, including Thomas', Entenmann's, Stroehmann, Oroweat and Freihofer's.  Servitje served as Bimbo's president from 1945 to 1981 and remained chairman of its board of directors until 1994.\n\nBimbo Bakeries USA: Bimbo Bakeries USA (] ) is the American corporate arm of the Mexican multinational bakery product manufacturing company Grupo Bimbo.  It is the largest bakery company in the United States.  The company, headquartered in Horsham, Pennsylvania, a suburb of Philadelphia, owns six of the top twelve fresh bread brands in the United States, including Entenmann's, Sara Lee, and Thomas'.  It is also a top advertising sponsor for many major soccer teams around the globe.\n\nBoland's Bakery: 'Boland's Bakery' was the largest bakery in Dublin in the late 19th century.  It was founded by the Boland family.  The company would have sold a number of products such as bread, biscuits, cakes, confectionery and flour, although over the years the biscuit became the company's main product.\n\nNabisco: Nabisco (from the National Biscuit Company) is an American manufacturer of cookies and snacks headquartered in East Hanover, New Jersey.  The company is a subsidiary of Illinois-based Mondelēz International.  Nabisco's plant in Chicago, a 1800000 sqft production facility at 7300 S. Kedzie Avenue, is the largest bakery in the world, employing more than 1,200 workers and producing around 320 million pounds of snack foods annually.\n\nCountry Club Bakery: Country Club Bakery, located in Fairmont, West Virginia, USA, is a small family owned bakery that is significant because it is the home of the pepperoni roll.  The bakery is located on Country Club Road, but the original bakery (where the pepperoni roll was invented) was located on Robinson Street.  The pepperoni roll is a snack popular in West Virginia and some nearby regions of the Appalachian Mountains.  Ubiquitous in West Virginia (particularly in convenience stores), but typically little known elsewhere, it is arguably the food most closely associated with the state (a competitor for this distinction is the ramp).  The first pepperoni rolls were created at the Country Club Bakery in Fairmont, West Virginia by Giuseppe \"Joseph\" Argiro at the Country Club Bakery in Fairmont in 1927, some argue that it was not invented until the 1940s, but no one disputes that they originated at the Country Club Bakery.  Fairmont, West Virginia, claims the title of \"Pepperoni Roll Capital of the World.\"\n\nLa Brea Bakery: La Brea Bakery is a retail bakery, restaurant operator, and an industrial baking company started in Los Angeles, California.  Since opening its flagship store on 468 S La Brea Avenue in 1989, La Brea has opened two much larger bakeries in Van Nuys, California, and Swedesboro, New Jersey, to serve wholesale clients.  It also sells its products in the United Kingdom and Ireland.  La Brea is one of the USA's largest sellers of fresh bread.  Since 2001 La Brea has been owned by Aryzta AG, the largest bakery company in the world.\n\nQuestion: Gansito is a chocolate and strawberry snack created by Bimbo, the world's largest bakery. In which country are their headquarters?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company.\"\n    },\n    \"headquarters_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the company's headquarters are located.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the company's headquarters are located.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"is_world_largest_bakery\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the company is the world's largest bakery.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"headquarters_location\",\n    \"is_world_largest_bakery\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the company."
      },
      "headquarters_location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the company's headquarters are located."
          },
          "country": {
            "type": "string",
            "description": "The country where the company's headquarters are located."
          }
        },
        "required": [
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "is_world_largest_bakery": {
        "type": "boolean",
        "description": "Indicates if the company is the world's largest bakery."
      }
    },
    "required": [
      "company_name",
      "headquarters_location",
      "is_world_largest_bakery"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
