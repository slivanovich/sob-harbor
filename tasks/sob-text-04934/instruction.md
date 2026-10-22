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
Ethanol fuel: Ethanol fuel is ethyl alcohol, the same type of alcohol found in alcoholic beverages, used as fuel.  It is most often used as a motor fuel, mainly as a biofuel additive for gasoline.  The first production car running entirely on ethanol was the Fiat 147, introduced in 1978 in Brazil by Fiat.  Ethanol is commonly made from biomass such as corn or sugarcane.  World ethanol production for transport fuel tripled between 2000 and 2007 from 17e9 L to more than 52e9 L .  From 2007 to 2008, the share of ethanol in global gasoline type fuel use increased from 3.7% to 5.4%.  In 2011 worldwide ethanol fuel production reached 8.46e10 L with the United States of America and Brazil being the top producers, accounting for 62.2% and 25% of global production, respectively.  US ethanol production reached 57.54e9 L in 2017-04.

Bartender DS: Bartender DS (バーテンダーDS ) is a simulation video game released for the Nintendo DS on September 27, 2007, by Electronic Arts of Japan.  The game is a Japan-only release, published to help provide individuals mixing alcoholic beverages with recipes for their cocktails.  The game includes over 850 recipes, as well as background information and history for each beverage.  The beverages are arranged in categories including necessary ingredients, and even the type of glass used to increase its ease of use.

Alcohol congener analysis: Alcohol congener analysis of blood and urine is used to provide an indication of the type of alcoholic beverage consumed.  The analysis involves investigating compounds called congeners that give the beverage a distinctive appearance, aroma, and flavour, not including water and ethanol.  The theory of discovering one’s drinking habits has been investigated since the late 1970s, predominantly in Germany, for "hip-flask" defence type cases (after-drinking).  Alcohol congener analysis can play a crucial role in these cases where the driver is apprehended some time after a motor vehicle incident who, when returning a positive alcohol reading then claim that this is due to drinking an alcoholic beverage only after the incident.  This traditional methodology for congener analysis has focused solely on the detection of fermentation by-product congeners that are found in all alcoholic beverages.  By comparing the ratios of a set standard of congeners, the ingested alcoholic beverage type is proposed.

Congener (alcohol): In the alcoholic beverages industry, congeners are substances, other than the desired type of alcohol, ethanol, produced during fermentation.  These substances include small amounts of chemicals such as methanol and other alcohols (known as fusel alcohols), acetone, acetaldehyde, esters, tannins, and aldehydes (e.g. furfural).  Congeners are responsible for most of the taste and aroma of distilled alcoholic beverages, and contribute to the taste of non-distilled drinks.  It has been suggested that these substances contribute to the symptoms of a hangover.  Congeners are also used by forensic toxicologists to determine what a person drank in a sub-discipline called alcohol congener analysis.

Jagertee: Jagertee (also Jägertee) is an alcoholic beverage made by mixing overproof rum with black tea, red wine, plum brandy, orange juice and various spices.  It is served warm and is typically consumed during winter in the cold parts of Central Europe.

Phosphate soda: Phosphate soda is a type of beverage that has a tangy or sour taste.  These beverages became popular among children in the 1870s in the United States.  Phosphate beverages were made with fruit flavorings, egg, malt, or wine.  In the 1900s, the beverages became popular, and fruit-flavoured phosphate sodas were served at soda fountains, before losing popularity to ice cream based treats in the 1930s.  Phosphoric acid is used in many bottled soft drinks, including Coca-Cola.  The original acid phosphate, made by the Horsford Chemical Company, was a mixture of calcium, magnesium and potassium phosphate salts with a small amount of phosphoric acid producing a liquid mixture with a pH of around 2.0, the same as freshly squeezed lime juice.

Coffeehouse: A coffeehouse, coffee shop or café (sometimes spelled cafe) is an establishment which primarily serves hot coffee, related coffee beverages (e.g., café latte, cappuccino, espresso), tea, and other hot beverages.  Some coffeehouses also serve cold beverages such as iced coffee and iced tea.  Many cafés also serve some type of food, such as light snacks, muffins or pastries.  Coffeehouses range from owner-operated small businesses to large multinational corporations.

Herbsaint: Herbsaint is a brand name of anise-flavored liqueur originally created as an absinthe-substitute in New Orleans, Louisiana in 1934, and currently produced by the Sazerac Company.

Alcohol (drug): Alcohol, also known by its chemical name ethanol, is a psychoactive drug found as the active ingredient in alcoholic beverages such as beer, wine, and distilled spirits.  It is one of the oldest and most common recreational drugs, causing the characteristic effects of alcohol intoxication or "drunkenness".  Among other effects, alcohol produces euphoria, decreased anxiety, increased sociability, sedation, impairment of cognition, memory, and motor function, and generalized depression of central nervous system function.  Ethanol is the only type of alcohol that is found in alcoholic beverages and is commonly used for recreational purposes; other alcohols such as methanol and isopropyl alcohol are toxic and potentially lethal.

Artisanal food: Artisanal food encompasses breads, cheeses, fruit preserves, cured meats, beverages, oils, and vinegars that are made by hand using traditional methods by skilled craftworkers, known as food artisans.  The foodstuff material from farmers and backyard growers can include fruit, grains and flours, milks for cheese, cured meats, fish, beverages, oils, and vinegars.  The movement is focused on providing farm to fork type foods with locally sourced products that benefit the consumer, small scale growers and producers, and the local economy.

Question: Herbsaint and Jagertee, are what type of beverages?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "beverage_category": {
      "type": "string",
      "description": "The common category that both beverages belong to."
    },
    "beverages": {
      "type": "array",
      "description": "Details for each beverage mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the beverage."
          },
          "is_alcoholic": {
            "type": "boolean",
            "description": "Indicates if the beverage is alcoholic."
          },
          "description_excerpt": {
            "type": "string",
            "description": "A direct quote or summary from the context describing the beverage's nature."
          }
        },
        "required": [
          "name",
          "is_alcoholic",
          "description_excerpt"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why both beverages fall into the identified category."
    }
  },
  "required": [
    "beverage_category",
    "beverages",
    "reasoning"
  ],
  "additionalProperties": false
}
