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
Cutex: Cutex is a brand of nail care products, the most prevalent of which is a cuticle extract.  The original product was developed and established in 1911 by Northam Warren Company, based in Stamford, Connecticut.  Though the brand has changed hands numerous times, "Cutex Brands" is the current owner.

Barnacle (slang): The word barnacle is a slang term used in electrical engineering to indicate a change made to a product on the manufacturing floor that was not part of the original product design.  A barnacle is typically used to correct a defect in the product or as a way of enhancing the product with new functionality.  A barnacle is normally a quick fix that is used until the product design can be redone incorporating the barnacle into the actual product so that when manufactured, the barnacle step in manufacturing is no longer required.

Tampax: Tampax (a portmanteau of tampon and pack) is a brand of tampon currently owned by Procter & Gamble and sold in over 100 countries.  Both the brand and the product were invented by Dr. Earle Haas, who filed a patent in 1931.  The original product was designed from the start as flushable and biodegradeable.

Realistic (brand): Realistic is a brand produced by RadioShack, a division of Tandy Corporation, to market audio and video products for home use.  The brand name was phased out in the mid 1990s and discontinued in 2000, then returned briefly in 2016.

Chlorodehydromethyltestosterone: Chlorodehydromethyltestosterone (CDMT; brand name Oral Turinabol) is an anabolic-androgenic steroid (AAS).  It is the 4-chloro-substituted derivative of metandienone (dehydromethyltestosterone; Dianabol).  CDMT was the first original product of Jenapharm, an East German pharmaceutical company.  The patent registration took place in 1961.  The idea of combining the structures of 4-chlorotestosterone (clostebol) and metandienone originated from the chemist Albert Stachowiak.  At the time this represented a unique dissociation of anabolic and androgenic effects after oral administration.  The product had been introduced for clinical use in 1965.

Anti-plug molding law: An anti-plug molding law is a statute, usually a state law, that prohibits the use of an original product, such as a boat hull, as a "plug" for making a mold to use to make copies of the original product.  The "plug" is the core around which the walls of the mold are formed and the contours of which the mold replicates in reverse.

Burger King Specialty Sandwiches: The Burger King Specialty Sandwiches are a line of sandwiches developed by the international fast-food restaurant chain Burger King in 1978 and introduced in 1979 as part of a new product line designed to expand Burger King's menu with more sophisticated, adult oriented fare beyond hamburgers.  Additionally, the new line was intended to differentiate the company from other fast food hamburger restaurants at the time.  Since the line's introduction, the other sandwiches have been discontinued, leaving the chicken offering, the Original Chicken Sandwich (abbreviated as OCS), as the primary product left.  Additionally, other sandwiches that utilize the same roll as the chicken sandwich have been introduced to the company's menu both domestically and internationally since the original product line was introduced.

Drumstick (ice cream): Drumstick is the brand name, owned by Nestlé since 1991, for a variety of ice cream-filled ice cream cones sold in the United States, Australia, Canada, Malaysia, and other countries across the world.  The original product was invented by I.C. Parker of The Drumstick Company of Fort Worth, Texas in 1928.

Biosimilar: A biosimilar (also known as follow-on biologic or subsequent entry biologic) is a biologic medical product which is almost an identical copy of an original product that is manufactured by a different company.  Biosimilars are officially approved versions of original "innovator" products, and can be manufactured when the original product's patent expires.  Reference to the innovator product is an integral component of the approval.

Tandy Corporation: Tandy Corporation was an American family-owned leather goods company based in Fort Worth, Texas.  Tandy Leather was founded in 1919 as a leather supply store and acquired a number of craft retail companies, including RadioShack in 1963.  In 2000, the Tandy Corporation name was dropped and the entity became the RadioShack Corporation.

Question: What was the original product of the company which owned the Realistic brand?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that owned the brand."
    },
    "brand_owned": {
      "type": "string",
      "description": "The brand name in question."
    },
    "original_product_of_company": {
      "type": "string",
      "description": "The original product of the identified company."
    },
    "company_founding_year": {
      "type": "integer",
      "description": "The year the company was founded."
    }
  },
  "required": [
    "company_name",
    "brand_owned",
    "original_product_of_company",
    "company_founding_year"
  ],
  "additionalProperties": false
}
