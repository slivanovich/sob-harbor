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
Sweetener (disambiguation): A sweetener is a substance, most commonly a sugar substitute (artificial sweetener), added to food to give it the basic taste of sweetness.

Peace Iced Tea: Peace Iced Tea (often labeled Peace Tea) is a brand of assorted iced tea beverages produced by the Monster Beverage Corporation.  The product launched on December 21, 2009.  Peace Tea contains no artificial flavors or coloring, although it does contain an artificial sweetener, sucralose.  The only flavor not to include sucralose was the Unsweetened Tea (also branded as High Tea), but it was discontinued in early 2012.  Peace tea is served in 23 oz cans, and is distributed across the United States.

Neotame: Neotame is an artificial sweetener made by NutraSweet that is between 7,000 and 13,000 times sweeter than sucrose (table sugar).  In the European Union, it is known by the E number E961.  It is moderately heat-stable, extremely potent, rapidly metabolized, completely eliminated, and does not appear to accumulate in the body.

Chocolate milk: Chocolate milk is sweetened chocolate-flavored milk.  It can be made by mixing chocolate syrup (or chocolate powder) with milk (from cows, goats, soy, rice, etc.).  It can be purchased pre-mixed with milk or made at home by blending milk with cocoa powder and a sweetener (such as sugar or a sugar substitute), melted chocolate, chocolate syrup, or a pre-made powdered chocolate milk mix.  Other ingredients, such as starch, salt, carrageenan, vanilla, or artificial flavoring are sometimes added.

Nutrisoda: Nutrisoda (formerly known as "airforce Nutrisoda") was the brand name of a nutrient-enhanced soda sold in the United States by the Ardea Beverage Company.  Nutrisoda contained zero sugar, zero sodium, zero aspartame, and zero to ten calories.  It was sweetened with Sucralose, an artificial sweetener made by chlorinating sucrose.

Truvia: Truvia (marketed and stylized as truvía) is a stevia-based sugar substitute developed jointly by The Coca-Cola Company and Cargill.  It is distributed and marketed by Cargill as a tabletop sweetener as well as a food ingredient.  Truvia is made of rebiana, erythritol, and natural flavors.  Because it comes from the stevia plant, Cargill classifies it as a natural sweetener in addition to being a non-nutritive sweetener, although Cargill has settled lawsuits alleging deceptive marketing of Truvia as "natural".  Since its launch in 2008, Truvia natural sweetener has become the second best-selling sugar substitute in units in the U.S. behind Splenda, surpassing Equal and Sweet'n Low.  Truvia competes with Stevia In The Raw, the #2 brand of stevia and with PepsiCo's PureVia, the #3 brand of stevia.

Sodium cyclamate: Sodium cyclamate (sweetener code 952) is an artificial sweetener.  It is 30–50 times sweeter than sucrose (table sugar), making it the least potent of the commercially used artificial sweeteners.  It is often used with other artificial sweeteners, especially saccharin; the mixture of 10 parts cyclamate to 1 part saccharin is common and masks the off-tastes of both sweeteners.  It is less expensive than most sweeteners, including sucralose, and is stable under heating.

PureVia: PureVia is a stevia-based low calorie sugar substitute developed jointly by Pepsico and Whole Earth Sweetener Company which is a wholly owned subsidiary of artificial sweetener manufacturing company Merisant.

Sucralose: Sucralose is an artificial sweetener and sugar substitute.  The majority of ingested sucralose is not broken down by the body, so it is noncaloric.  In the European Union, it is also known under the E number E955.  Sucralose is about 320 to 1,000 times sweeter than sucrose, three times as sweet as aspartame, twice as sweet as sodium saccharin and three times as sweet as acesulfame potassium.  Evidence of benefit is lacking for long-term weight loss with some data supporting weight gain and heart disease risks.

Acesulfame potassium: Acesulfame potassium ( ), also known as acesulfame K (K is the symbol for potassium) or Ace K, is a calorie-free sugar substitute (artificial sweetener) often marketed under the trade names Sunett and Sweet One.  In the European Union, it is known under the E number (additive code) E950.  It was discovered accidentally in 1967 by German chemist Karl Clauss at Hoechst AG (now Nutrinova).  In chemical structure, acesulfame potassium is the potassium salt of 6-methyl-1,2,3-oxathiazine-4(3"H")-one 2,2-dioxide.  It is a white crystalline powder with molecular formula C4H4KNO4S and a molecular weight of 201.24 g/mol.

Question: Nutrisoda (formerly known as "airforce Nutrisoda") was the brand name of a nutrient-enhanced soda sold in the United States by which company, it was sweetened with Sucralose, an artificial sweetener made by chlorinating sucrose, and sugar substitute ? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string",
      "description": "The brand name of the product."
    },
    "company_name": {
      "type": "string",
      "description": "The company that sold the product."
    },
    "sweetener_details": {
      "type": "object",
      "properties": {
        "sweetener_name": {
          "type": "string",
          "description": "The name of the sweetener used in the product."
        },
        "sweetener_types": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Categories or classifications of the sweetener."
        },
        "manufacturing_process": {
          "type": "string",
          "description": "The method by which the sweetener is made."
        }
      },
      "required": [
        "sweetener_name",
        "sweetener_types",
        "manufacturing_process"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "product_name",
    "company_name",
    "sweetener_details"
  ],
  "additionalProperties": false
}
