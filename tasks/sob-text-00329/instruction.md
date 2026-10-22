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
Bloody Mary (cocktail): A Bloody Mary is a cocktail containing vodka, tomato juice, and combinations of other spices and flavorings including Worcestershire sauce, Hot Sauce, piri piri sauce, beef consommé or bouillon, horseradish, celery, olives, salt, black pepper, cayenne pepper, lemon juice, lime juice and/or celery salt.

Cran-Apple juice: Cranapple is a trademark for a blend of cranberry juice and apple juice marketed by the Ocean Spray cooperative, styled as Cran•Apple.  The juice blend is marketed as combining the tartness of the cranberry with the sweet taste of the apple in a beverage that is fat and cholesterol free, low in sodium and is a source of vitamin C.  Until 1963, when the product was first developed, cranberries were sold in the form of cranberry juice and cranberry sauce primarily around Thanksgiving and Christmas time.  The Cranapple blend helped turn the cranberry into a year-round product.  Cranapple started a trend and was followed by other juice blends.

Japanese slipper: A Japanese slipper is a drink made from Midori, Cointreau, and lemon juice.  It was created in 1984 by Jean-Paul Bourguignon at Mietta's Restaurant in Melbourne.

Bay Breeze: The Bay Breeze is a cocktail which has a Cape Codder as its base.  This drink is also sometimes called a Downeaster, Hawaiian Sea Breeze or a Paul Joseph.  This cocktail is similar to the Sea Breeze, which is an IBA Official Cocktail with grapefruit juice instead of pineapple juice.

Sea Breeze (cocktail): A Sea Breeze is a cocktail containing vodka with cranberry juice and grapefruit juice.  The cocktail is usually consumed during summer months.  The drink may be shaken in order to create a foamy surface.  It is considered an IBA Official Cocktail.

Seifu: The seifu is a cocktail containing vodka, club soda and grapefruit juice.

Sea breeze: A sea breeze or onshore breeze is any wind that blows from a large body of water toward or onto a landmass; it develops due to differences in air pressure created by the differing heat capacities of water and dry land.  As such, sea breezes are more localised than prevailing winds.  Because land absorbs solar radiation far more quickly than water, a sea breeze is a common occurrence along coasts after sunrise.  By contrast, a land breeze or offshore breeze is the reverse effect: dry land also cools more quickly than water and, after sunset, a sea breeze dissipates and the wind instead flows from the land towards the sea.  Sea breezes and land breezes are both important factors in coastal regions' prevailing winds.  The term offshore wind may refer to any wind over open water.

Grapefruit juice: Grapefruit juice is the juice from grapefruits.  It is rich in Vitamin C and ranges from sweet-tart to very sour.  Variations include white grapefruit, pink grapefruit and ruby red grapefruit juice.

Rose Kennedy Cocktail: Rose Kennedy (also commonly known as a "VSS," "The Michele," "The White Girl," or "vodka soda splash") is a cocktail popular in the mid-Atlantic and Northeastern United States.  It consists of varying amounts of vodka and club soda with a splash of cranberry juice for color and taste.  The juice sweetens the taste and takes the edge off the alcohol.  The cocktail, typically garnished with a lemon or lime wedge, is based on the Cape Cod and named after Rose Kennedy, the matriarch of the Kennedy Family of Cape Cod and the mother of President John F. Kennedy from Massachusetts.

Grapefruit diet: The grapefruit diet, also known as the Hollywood Diet is a short-term fad diet that has existed in the United States since at least the 1930s.  The diet is based on the claim that grapefruit has a fat-burning enzyme or similar property.  The variations of the grapefruit diet that are too low in calories (below 800-1000 calories a day), too low in carbohydrates, or too low in essential micronutrients are considered unhealthy and potentially dangerous.  While eating half a grapefruit with every meal may be a good way to incorporate more fruit in the diet of a healthy person, grapefruit and grapefruit juice is harmful if the dieter is taking medicines that can interact with grapefruit juice or is allergic to citruses.  This diet will not be beneficial to anyone over a long time as the extremely low calorie intake could lead to malnutrition and many health problems.  The grapefruit diet also does not require exercise.

Question: What is a cocktail containing vodka with cranberry juice and grapefruit juice, Japanese slipper or Sea Breeze ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cocktail_name": {
      "type": "string",
      "description": "The name of the cocktail identified."
    },
    "main_ingredients": {
      "type": "array",
      "description": "A list of the primary ingredients in the cocktail.",
      "items": {
        "type": "string"
      }
    },
    "is_iba_official_cocktail": {
      "type": "boolean",
      "description": "Indicates if the cocktail is an IBA Official Cocktail."
    },
    "typical_consumption_period": {
      "type": "string",
      "description": "The period during which the cocktail is usually consumed."
    }
  },
  "required": [
    "cocktail_name",
    "main_ingredients",
    "is_iba_official_cocktail",
    "typical_consumption_period"
  ],
  "additionalProperties": false
}
