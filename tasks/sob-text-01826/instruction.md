Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Drambuie: Drambuie is a golden coloured, 40% ABV liqueur made from scotch whisky, honey, herbs and spices.  The brand had been owned by the MacKinnon family for a hundred years but was bought by William Grant & Sons in 2014.  It has been produced under contract at the Morrison Bowmore Distillers facility at Springburn Bond, Glasgow since 2010.

Rusty Nail (cocktail): A Rusty Nail is made by mixing Drambuie and Scotch whisky.  The drink was included in Difford's Guide Top 100 Cocktails.

Cashew pie: Cashew pie is a pie prepared with cashews as a primary ingredient.  Whole or chopped cashews may be used, or both.  It may be prepared with a sweet filling base prepared with corn syrup, sugar and eggs, similar to how pecan pie filling is prepared.  It may be prepared using chocolate and fruits such as raspberry as an ingredient, and may be served topped with whipped cream or caramel.  It may be served hot.

List of banana dishes: This is a list of banana dishes and foods in which banana or plantain is used as a primary ingredient.  Foods prepared with banana or plantain as a primary ingredient are also included in this list.  A banana is an edible fruit produced by several kinds of large herbaceous flowering plants in the genus "Musa".  (In some countries, bananas used for cooking may be called plantains.)  The fruit is variable in size, color and firmness, but is usually elongated and curved, with soft flesh rich in starch covered with a rind which may be green, yellow, red, purple, or brown when ripe.  The fruits grow in clusters hanging from the top of the plant.

Bean dip: Bean dip is a type of dipping sauce made using beans or refried beans as a primary ingredient.  It is typically served with tortilla chips, and can also be served with other foods such as crackers and crudités.  Various types of beans are used, and fresh-cooked, canned or flaked beans can be used.  Various additional ingredients are used in its preparation, such as onion, garlic, chili peppers and spices, and it is sometimes garnished with some ingredients.  Bean dip can be served cold, at room temperature, or hot.  Bean dip is sometimes used as an ingredient in the preparation of other dishes such as burritos and quesadillas.

Anchovy paste: Anchovy paste is a fish paste food product prepared using anchovies as a primary ingredient.  It is used as a condiment and as an ingredient in various dishes, such as Scotch woodcock, and is a mass-produced product.  It has been used for centuries to provide flavor to foods and as a source of nutrients, and it is a part of the cuisines of Great Britain, Italy, the Philippines and Vietnam.  It is a major export product of Morocco.

List of coffee dishes: This is a list of coffee dishes, which includes foods that use coffee as a primary ingredient, and for which coffee is an essential ingredient.  Coffee beverages are omitted from this list.

List of strawberry dishes: This is a list of strawberry dishes, foods and beverages, which use strawberry as a primary ingredient.  Several desserts use strawberries as a main ingredient, and strawberries are also used as a topping on some foods, such as French toast, waffles and pastries.

Mushroom ketchup: Mushroom ketchup is a style of ketchup (also spelled "catsup") that is prepared with mushrooms as its primary ingredient.  Originally, ketchup in the United Kingdom was prepared with mushrooms as a primary ingredient, instead of tomato, the main ingredient in contemporary preparations of ketchup.  Historical preparations involved packing whole mushrooms into containers with salt.  It is used as a condiment and may be used as an ingredient in the preparation of other sauces and other condiments.  Several brands of mushroom ketchup were produced and marketed in the United Kingdom, some of which were exported to the United States, and Geo Watkins Mushroom Ketchup continues to exist in contemporary times as a commercially mass-produced product.

List of fruit dishes: This is a list of fruit dishes.  Fruit dishes are those that use fruit as a primary ingredient.  Condiments prepared with fruit as a primary ingredient are also included in this list.

Question: Where has the Rusty Nail's primary ingredient, Drambuie, been produced since 2010?

Respond with JSON matching this schema:
{
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
}
