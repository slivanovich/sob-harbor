{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nDrambuie: Drambuie is a golden coloured, 40% ABV liqueur made from scotch whisky, honey, herbs and spices.  The brand had been owned by the MacKinnon family for a hundred years but was bought by William Grant & Sons in 2014.  It has been produced under contract at the Morrison Bowmore Distillers facility at Springburn Bond, Glasgow since 2010.\n\nRusty Nail (cocktail): A Rusty Nail is made by mixing Drambuie and Scotch whisky.  The drink was included in Difford's Guide Top 100 Cocktails.\n\nCashew pie: Cashew pie is a pie prepared with cashews as a primary ingredient.  Whole or chopped cashews may be used, or both.  It may be prepared with a sweet filling base prepared with corn syrup, sugar and eggs, similar to how pecan pie filling is prepared.  It may be prepared using chocolate and fruits such as raspberry as an ingredient, and may be served topped with whipped cream or caramel.  It may be served hot.\n\nList of banana dishes: This is a list of banana dishes and foods in which banana or plantain is used as a primary ingredient.  Foods prepared with banana or plantain as a primary ingredient are also included in this list.  A banana is an edible fruit produced by several kinds of large herbaceous flowering plants in the genus \"Musa\".  (In some countries, bananas used for cooking may be called plantains.)  The fruit is variable in size, color and firmness, but is usually elongated and curved, with soft flesh rich in starch covered with a rind which may be green, yellow, red, purple, or brown when ripe.  The fruits grow in clusters hanging from the top of the plant.\n\nBean dip: Bean dip is a type of dipping sauce made using beans or refried beans as a primary ingredient.  It is typically served with tortilla chips, and can also be served with other foods such as crackers and crudités.  Various types of beans are used, and fresh-cooked, canned or flaked beans can be used.  Various additional ingredients are used in its preparation, such as onion, garlic, chili peppers and spices, and it is sometimes garnished with some ingredients.  Bean dip can be served cold, at room temperature, or hot.  Bean dip is sometimes used as an ingredient in the preparation of other dishes such as burritos and quesadillas.\n\nAnchovy paste: Anchovy paste is a fish paste food product prepared using anchovies as a primary ingredient.  It is used as a condiment and as an ingredient in various dishes, such as Scotch woodcock, and is a mass-produced product.  It has been used for centuries to provide flavor to foods and as a source of nutrients, and it is a part of the cuisines of Great Britain, Italy, the Philippines and Vietnam.  It is a major export product of Morocco.\n\nList of coffee dishes: This is a list of coffee dishes, which includes foods that use coffee as a primary ingredient, and for which coffee is an essential ingredient.  Coffee beverages are omitted from this list.\n\nList of strawberry dishes: This is a list of strawberry dishes, foods and beverages, which use strawberry as a primary ingredient.  Several desserts use strawberries as a main ingredient, and strawberries are also used as a topping on some foods, such as French toast, waffles and pastries.\n\nMushroom ketchup: Mushroom ketchup is a style of ketchup (also spelled \"catsup\") that is prepared with mushrooms as its primary ingredient.  Originally, ketchup in the United Kingdom was prepared with mushrooms as a primary ingredient, instead of tomato, the main ingredient in contemporary preparations of ketchup.  Historical preparations involved packing whole mushrooms into containers with salt.  It is used as a condiment and may be used as an ingredient in the preparation of other sauces and other condiments.  Several brands of mushroom ketchup were produced and marketed in the United Kingdom, some of which were exported to the United States, and Geo Watkins Mushroom Ketchup continues to exist in contemporary times as a commercially mass-produced product.\n\nList of fruit dishes: This is a list of fruit dishes.  Fruit dishes are those that use fruit as a primary ingredient.  Condiments prepared with fruit as a primary ingredient are also included in this list.\n\nQuestion: Where has the Rusty Nail's primary ingredient, Drambuie, been produced since 2010?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"product_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the product being produced.\"\n    },\n    \"production_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"facility_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the production facility.\"\n        },\n        \"specific_address_detail\": {\n          \"type\": \"string\",\n          \"description\": \"Specific detail about the address or area within the city.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the production facility is located.\"\n        }\n      },\n      \"required\": [\n        \"facility_name\",\n        \"specific_address_detail\",\n        \"city\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"production_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year production started at this location.\"\n    },\n    \"is_cocktail_ingredient\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the product is an ingredient in a cocktail mentioned in the context.\"\n    },\n    \"cocktail_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the cocktail for which this product is an ingredient.\"\n    }\n  },\n  \"required\": [\n    \"product_name\",\n    \"production_location\",\n    \"production_start_year\",\n    \"is_cocktail_ingredient\",\n    \"cocktail_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "product_name": {
        "type": "string",
        "description": "The name of the product being produced."
      },
      "production_location": {
        "type": "object",
        "properties": {
          "facility_name": {
            "type": "string",
            "description": "The name of the production facility."
          },
          "specific_address_detail": {
            "type": "string",
            "description": "Specific detail about the address or area within the city."
          },
          "city": {
            "type": "string",
            "description": "The city where the production facility is located."
          }
        },
        "required": [
          "facility_name",
          "specific_address_detail",
          "city"
        ],
        "additionalProperties": false
      },
      "production_start_year": {
        "type": "integer",
        "description": "The year production started at this location."
      },
      "is_cocktail_ingredient": {
        "type": "boolean",
        "description": "Indicates if the product is an ingredient in a cocktail mentioned in the context."
      },
      "cocktail_name": {
        "type": "string",
        "description": "The name of the cocktail for which this product is an ingredient."
      }
    },
    "required": [
      "product_name",
      "production_location",
      "production_start_year",
      "is_cocktail_ingredient",
      "cocktail_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
