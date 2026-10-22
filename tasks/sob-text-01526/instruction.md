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
Cocktails with cachaça: There are many cocktails made with cachaça, the national spirit of Brazil.  Caipirinha is by far the most popular and internationally well-known.

RalliSport Challenge: RalliSport Challenge is a 2002 rally racing video game for Microsoft Windows and the Xbox.  It allows a career with up to 29 cars including the Mitsubishi Lancer Evo 6 and the Suzuki Grand Vitara.  Four race types that are included in the game are Rally, Hillclimb, Ice Racing, and Rallycross.  A sequel, "RalliSport Challenge 2", was released in 2004 for the Xbox.

The Fine Art of Mixing Drinks: The Fine Art of Mixing Drinks is a book about cocktails by David A. Embury, first published in 1948.  The book is noteworthy for its witty, highly opinionated and conversational tone, as well as its categorization of cocktails into two main types: aromatic and sour; its categorization of ingredients into three categories: the base, modifying agents, and special flavorings and coloring agents; and its 1:2:8 ratio (1 part sweet, 2 parts sour, 8 parts base) for sour type cocktails.

Batida: Batida is a Brazilian cocktail, and is one of several Brazilian cocktails that are made with the national alcoholic drink "cachaça".  In Portuguese "batida" means "shaken" or "milkshake", and the word also means a crash, usually used when referring to a car crash.  This beverage is made with cachaça, fruit juice (or coconut milk), and sugar.  It is blended or shaken with ice.  In Rio de Janeiro and São Paulo, batidas are traditionally served with the Brazilian national dish, feijoada.

Cheryl Charming: Cheryl Charming (born November 19, 1960) is an American bar professional and published author of 16 books on cocktails and bartending.  She currently works as the Bar Director at the Bourbon "O” Bar in New Orleans, Louisiana, and in 2014 was named the "New Orleans Magazine" Mixologist of the Year.

Brooklyn (cocktail): The Brooklyn is one of five cocktails named for the boroughs of New York City, along with the Bronx, the Manhattan, the Queens and the Staten Island Ferry.  It resembles a Manhattan, but with a specific type of bitters (several types of bitters can be used in a Manhattan) and the addition of Maraschino liqueur.  It largely fell into obscurity after the end of Prohibition, but experienced a resurgence in the 1990s.

Hand Grenade (cocktail): The specialty cocktail drink known as the Hand Grenade is sold frozen or on-the-rocks exclusively by 721 Bourbon, Inc. through five licensed nightclub bars in the New Orleans French Quarter.  Pam Fortner and Earl Bernhardt, owners of the Tropical Isle bar founded during the 1984 Louisiana World Exposition, created the melon-flavored Hand Grenade as their signature cocktail.  Since 1987, the federally registered trademark "Hand Grenade" has been used to uniquely identify the cocktail and its packaging.  Since January 1992, the Hand Grenade has been served in a green, translucent, plastic yard glass container with a bulbous, textured base shaped like an oversized hand grenade.  The grenade has anthropomorphic features, including black oval eyes and an upturned smile.  Printed in bold, black lettering, the legend extends vertically down the neck, with the cocktail name and a reference to its high alcohol content: "Hand Grenade® New Orleans Most Powerful Drink".  Consumers purchasing Hand Grenade cocktails in these containers receive discounts on refills at the licensed establishments.  In January 2012, a lower-calorie "Skinny Hand Grenade" was announced.

Watershed Distillery: Watershed Distillery is a microdistillery in Columbus, Ohio founded in 2010 by business partners Greg Lehman and Dave Rigo.  The distillery was the second distillery opened in Central Ohio after prohibition, and Watershed brought to market the first legally distilled bourbon whiskey in Central Ohio post-prohibition in 2012.  The distillery offers tours to the public and will also be the first distillery in Ohio to open a restaurant on-site in February 2017, following the passage of Ohio House Bill 351 in 2016.  The distillery offers six spirits, Vodka, two types of American style Gin, Bourbon, Nocino and a bottled Old Fashioned cocktail.

Bourbon Lancer: The "Bourbon lancer" is a type of cocktail made by mixing Bourbon whiskey with Champagne.  These are mixed with bitters and served on the rocks.

Manhattan (cocktail): A Manhattan is a cocktail made with whiskey, sweet vermouth, and bitters.  Commonly used whiskeys include rye (the traditional choice), Canadian whisky, bourbon, blended whiskey, and Tennessee whiskey.  The cocktail is often stirred and strained into a cocktail glass, where it is garnished with a Maraschino cherry with a stem.  A Manhattan can also be served on the rocks in a lowball glass.  The whiskey-based Manhattan is one of five cocktails named for one of New York City's five boroughs, but is perhaps most closely related to the Brooklyn cocktail, a mix utilizing dry vermouth and Maraschino liqueur in place of the Manhattan's sweet vermouth, as well as Amer Picon in place of the Manhattan's traditional bitters.

Question: Bourbon Lancer and Cocktails with cachaça, are types of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_category": {
      "type": "string",
      "description": "The overarching category that both items belong to."
    },
    "categorized_items": {
      "type": "array",
      "description": "A list of the items from the question, with their key characteristics.",
      "items": {
        "type": "object",
        "properties": {
          "item_name": {
            "type": "string",
            "description": "The name of the item being categorized."
          },
          "main_spirit": {
            "type": "string",
            "description": "The primary alcoholic spirit used in the item."
          },
          "main_spirit_origin_country": {
            "type": "string",
            "description": "The country of origin for the main spirit, if specified in the context."
          }
        },
        "required": [
          "item_name",
          "main_spirit"
        ],
        "additionalProperties": false
      }
    },
    "cocktail_categorization_types": {
      "type": "array",
      "description": "Types of cocktails as categorized in 'The Fine Art of Mixing Drinks'.",
      "items": {
        "type": "string"
      }
    },
    "cocktail_ingredient_categories": {
      "type": "array",
      "description": "Categories of ingredients for cocktails as defined in 'The Fine Art of Mixing Drinks'.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "common_category",
    "categorized_items",
    "cocktail_categorization_types",
    "cocktail_ingredient_categories"
  ],
  "additionalProperties": false
}
