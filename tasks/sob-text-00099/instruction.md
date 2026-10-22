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
PureVia: PureVia is a stevia-based low calorie sugar substitute developed jointly by Pepsico and Whole Earth Sweetener Company which is a wholly owned subsidiary of artificial sweetener manufacturing company Merisant.

Equal (sweetener): Equal is a brand of artificial sweetener containing aspartame, acesulfame potassium, dextrose and maltodextrin.  It is marketed as a tabletop sweetener by Merisant, a global corporation which also used to own the well-known NutraSweet brand when it was a subsidiary of Monsanto and which has headquarters in Chicago, Illinois, Switzerland, Mexico, and Australia.  In French Canada, Equal is known as "Égal".

Sweetener (disambiguation): A sweetener is a substance, most commonly a sugar substitute (artificial sweetener), added to food to give it the basic taste of sweetness.

Siamenoside I: Siamenoside is a cucurbitane.  It is natural sweetener found in the fruit of "Siraitia grosvenorii", together with neomogroside.  The mix of the two chemicals is about 300 times sweeter than sucrose.  It is used as a natural sweetener in China.

Neotame: Neotame is an artificial sweetener made by NutraSweet that is between 7,000 and 13,000 times sweeter than sucrose (table sugar).  In the European Union, it is known by the E number E961.  It is moderately heat-stable, extremely potent, rapidly metabolized, completely eliminated, and does not appear to accumulate in the body.

Acesulfame potassium: Acesulfame potassium ( ), also known as acesulfame K (K is the symbol for potassium) or Ace K, is a calorie-free sugar substitute (artificial sweetener) often marketed under the trade names Sunett and Sweet One.  In the European Union, it is known under the E number (additive code) E950.  It was discovered accidentally in 1967 by German chemist Karl Clauss at Hoechst AG (now Nutrinova).  In chemical structure, acesulfame potassium is the potassium salt of 6-methyl-1,2,3-oxathiazine-4(3"H")-one 2,2-dioxide.  It is a white crystalline powder with molecular formula C4H4KNO4S and a molecular weight of 201.24 g/mol.

Dulcin: Dulcin is an artificial sweetener about 250 times sweeter than sugar, discovered in 1884 by Joseph Berlinerbau.  It was first mass-produced about seven years later.  Despite the fact that it was discovered only five years after saccharin, it never enjoyed the latter compound’s market success.  Still, it was an important sweetener of the early 20th century and had an advantage over saccharin in that it did not possess a bitter aftertaste.  It is not known to occur as a natural product.

Nutrisoda: Nutrisoda (formerly known as "airforce Nutrisoda") was the brand name of a nutrient-enhanced soda sold in the United States by the Ardea Beverage Company.  Nutrisoda contained zero sugar, zero sodium, zero aspartame, and zero to ten calories.  It was sweetened with Sucralose, an artificial sweetener made by chlorinating sucrose.

Sucralose: Sucralose is an artificial sweetener and sugar substitute.  The majority of ingested sucralose is not broken down by the body, so it is noncaloric.  In the European Union, it is also known under the E number E955.  Sucralose is about 320 to 1,000 times sweeter than sucrose, three times as sweet as aspartame, twice as sweet as sodium saccharin and three times as sweet as acesulfame potassium.  Evidence of benefit is lacking for long-term weight loss with some data supporting weight gain and heart disease risks.

Sodium cyclamate: Sodium cyclamate (sweetener code 952) is an artificial sweetener.  It is 30–50 times sweeter than sucrose (table sugar), making it the least potent of the commercially used artificial sweeteners.  It is often used with other artificial sweeteners, especially saccharin; the mixture of 10 parts cyclamate to 1 part saccharin is common and masks the off-tastes of both sweeteners.  It is less expensive than most sweeteners, including sucralose, and is stable under heating.

Question: What is the European Union's name for the artificial sweetener found in Nutrisoda?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "sweetener_name": {
      "type": "string",
      "description": "The common name of the artificial sweetener."
    },
    "eu_designation": {
      "type": "string",
      "description": "The E number or European Union's name for the sweetener."
    },
    "sweetener_type": {
      "type": "string",
      "description": "The type of sweetener (e.g., artificial, natural)."
    },
    "product_containing_sweetener": {
      "type": "string",
      "description": "The product in which the sweetener was found."
    }
  },
  "required": [
    "sweetener_name",
    "eu_designation",
    "sweetener_type",
    "product_containing_sweetener"
  ],
  "additionalProperties": false
}
