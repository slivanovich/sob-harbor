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
Heinz: The H. J. Heinz Company, or Heinz, was an American food processing company with world headquarters in Pittsburgh, Pennsylvania.  It was founded by Henry John Heinz in 1869.  The H. J. Heinz Company manufactures thousands of food products in plants on six continents, and markets these products in more than 200 countries and territories.  The company claims to have 150 number-one or number-two brands worldwide.  Heinz ranked first in ketchup in the US with a market share in excess of 50%; Ore-Ida label held 46% of the frozen potato sector in 2003.

Passionata: Passionata, a brand in the Chantelle Group, is a French lingerie brand founded in 1988.  Its target market is working women and its icon is the image of a woman who lives life to the full.  The brand enjoys a strong presence in Europe with a large distribution network: retailers, department stores, mass distribution and, since 2008, has stores in France and Germany.

Biba Apparels: Biba Apparels is an Indian fashion brand founded by Meena Bindra in 1988 from her home in New Delhi, India.  Biba is considered as one the best ethnical fashion brand in India.  It has more than 150 brand outlets and 225 multi-brand outlets .  Biba recorded sales of INR 600 crore in 2014-15.

Theatre Products: Theatre Products is a Japanese fashion brand founded in 2001 and currently based in Roppongi, Tokyo.  The brand's founders, and as of 2007, its main designers are Akira Takeuchi and Tayuka Nakanishi.  The brand has retail outlets in the Harajuku and Shibuya areas of Tokyo, known as centers of youth fashion.

Rami Ranger: Raminder Singh Ranger {'1': ", '2': ", '3': ", '4': "} is the founder of Sun Mark, an international marketing and distribution company.  He is also chairman and managing director of Sea Air and Land Forwarding Ltd.

Rue107: Rue107 is a women's clothing brand founded in 2011 by Marie Jean-Baptiste in New York City.  It specializes in a wide gamut of sizes of women's clothing, though it is notable for its selection of women's plus-sized clothing and swimwear lines.  Since its inception, the clothing brand has been worn by several celebrities, including Beyoncé, Nicki Minaj, and others.  The clothing brand has received praise for its clothing lines as well as the attention it has given to plus-sized women in terms of marketing and clothing options.  The brand has also received attention for its independent status, its plus-sized clothing options, and the fact that it was a company created by a black woman.

Supra (brand): Supra is an American shoe brand founded in California by Angel Cabada, in partnership with professional skateboarders such as Chad Muska, Jim Greco and Erik Ellington.  Muska has described the founding of the company as an "underground idea", shared between five people, that became a "crazy explosion".  The brand has released signature model shoes from team riders, such as Muska, Ellington, Jim Greco, Tom Penny, and Stevie Williams.  As of October 2014, the brand is distributed by One Distribution, the parent company of the KR3W clothing brand.

Sun Mark: Sun Mark was founded in 1995 by Rami Ranger and operates from its head office in Greenford, Middlesex.  Sun Mark, in partnership with its sister company Sea Air & Land Forwarding Ltd, was founded with the purpose to provide customers an end to end service for marketing and distribution of FMCG products.  Sun Mark focuses on approaching traditionally hard to reach markets around the world and provides both its own label and leading brands such as Heinz, Mondelez, Nestle and Unilever amongst others to certain territories worldwide.  Sun Mark is also a leading member of the Landmark Wholesale group.

CoEvolution Quarterly: CoEvolution Quarterly (1974–1985) is a descendant of Stewart Brand's "Whole Earth Catalog".  Stewart Brand founded the "CoEvolution Quarterly" in 1974 using proceeds from the "Whole Earth Catalog."  It evolved out of the original "Supplement to the Whole Earth Catalog".  Fred Turner notes that in 1985, Brand merged "CoEvolution Quarterly" with "The Whole Earth Software Review" (a supplement to "The Whole Earth Software Catalog") to create the "Whole Earth Review."

U2 Clothing: U2 Clothing was a casual-wear clothing brand founded by Michael Tien in 1980 in Hong Kong.  Tien founded G2000 at the same time, with both operating under the G2000 Apparel Limited brand.  In 2007, U2, G2000, and a third brand of the same company called UWoman consolidated into a single retail chain retaining the name G2000, which offers the pre-existing product lines under new labels---G2000, G2000 blù (formerly U2), and G2000 Pink (formerly UWoman).

Question: Sun Mark owns which brand founded in 1869?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "brand_name": {
      "type": "string",
      "description": "The name of the brand."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the brand was founded."
    },
    "relationship_to_sun_mark": {
      "type": "string",
      "description": "Describes the relationship between the brand and Sun Mark."
    },
    "sun_mark_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the company Sun Mark."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year Sun Mark was founded."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "brand_name",
    "founding_year",
    "relationship_to_sun_mark",
    "sun_mark_details"
  ],
  "additionalProperties": false
}
