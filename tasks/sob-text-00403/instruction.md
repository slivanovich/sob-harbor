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
Jazz (soft drink): Diet Pepsi Jazz was a brand of soda introduced by the Pepsi company in 2006 and discontinued in 2009.  It was a specifically named variant of Pepsi's popular Diet Pepsi product, combining several different flavors.

Crush (soft drink): Crush is a brand of carbonated soft drinks owned and marketed internationally by Dr Pepper Snapple Group, originally created as an orange soda.  Crush competes with Coca-Cola's Fanta, and Dr Pepper Snapple Group's Sunkist.  It was created in 1911 by California beverage and extract chemist Neil C. Ward.  Most flavors of Crush are caffeine-free.

Dr Pepper/Seven Up: Dr Pepper/Seven Up, Inc. (DPSU) was a Plano, Texas-based soft-drink manufacturing company created by the merger of Dr Pepper, Inc. and The 7 Up Company on May 19, 1986.  The merger was a result of the independent bailouts of both companies and the subsequent FTC blockage of a Dr Pepper merger with Coca-Cola.  The DPSU merger resulted in the breakup of international

ACC Championship Game: The Dr Pepper ACC Football Championship Game is an American college football game held on the first Saturday in December by the Atlantic Coast Conference (ACC) each year to determine its football champion.  The game pits the champion of the Coastal Division against the champion of the Atlantic Division in a game that follows the conclusion of the regular season.  The game's corporate sponsor is Dr Pepper.  The current champion are the Clemson Tigers of the Atlantic Division.

Dublin Dr Pepper: Dublin Dr Pepper was the popular name for a style of Dr Pepper soft drink made by the Dublin Dr Pepper Bottling Company in Dublin, Texas.  Dublin Dr Pepper followed the original recipe, using cane sugar as the sweetener as opposed to newer high fructose corn syrup (HFCS).  The Dublin plant formula's use of sugar made it popular among soda fans.  According to the corporate headquarters at Dr Pepper Snapple Group, this resulted in clashes with other bottlers and the parent company of Dr Pepper.  On 12 January 2012, it was announced that Dublin Dr. Pepper will no longer be produced, after the Dublin Dr Pepper Bottling Company settled the trademark dispute instigated by Dr Pepper Snapple Group.

Dr Pepper Ballpark: Dr Pepper Ballpark (formerly Dr Pepper/Seven Up Ballpark) is the home ballpark of the Frisco RoughRiders Class AA minor league baseball club.  Located in Frisco, Texas in the United States, the stadium has a capacity of 10,316.  The ballpark is host to numerous functions in addition to minor league baseball games, including corporate and charity events, wedding receptions, city of Frisco events, and church services.  Local soft drink manufacturer Dr Pepper Snapple Group holds naming rights and exclusive non-alcoholic beverage rights in the park.

Diet Dr Pepper: Diet Dr Pepper is a no-calorie Dr Pepper that was first introduced in 1986.  This version replaces the high fructose corn syrup found in the original with aspartame.  Diet Cherry Chocolate Dr Pepper (2007–2008) was introduced as a limited edition flavor on November 21, 2007.  It was discontinued in April 2008.  It became available in Canada in early January 2008.  A nondiet version was never created.  The taste is similar to Canfield's Diet Cherry Chocolate Fudge Soda, but with the distinctive Dr Pepper flavor.  It was featured in the song "Cherry Chocolate Rain" by YouTube celebrity Tay Zonday.  Upon ceasing production, it was replaced by Cherry Vanilla Dr Pepper.

Dr Pepper: Dr Pepper is a carbonated soft drink marketed as having a unique flavor.  The drink was created in the 1880s by Charles Alderton in Waco, Texas and first served around 1885.  Dr Pepper was first nationally marketed in the United States in 1904, and is now also sold in Europe, Asia, Canada, Mexico, Australia, and South America, as well as New Zealand and South Africa as an imported good.  Variants include a version without high fructose corn syrup, Diet Dr Pepper, as well as a line of additional flavors, first introduced in the 2000s.

Flaming Doctor Pepper: A Flaming Doctor Pepper is a flaming cocktail said to taste like the soft drink Dr Pepper, although Dr Pepper is not one of its ingredients.

Dr Pepper Snapple Bottling Group: Dr Pepper Snapple Bottling Group (formerly Dr Pepper/Seven Up Bottling Group and Cadbury Schweppes Bottling Group) is the third largest bottling company in the United States after Pepsi Beverages Company and Coca-Cola Enterprises.  The company is a wholly owned subsidiary of Dr Pepper Snapple Group.

Question: Jazz and Dr Pepper, are a type of what item?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "item_names": {
      "type": "array",
      "description": "The names of the items mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "common_category": {
      "type": "string",
      "description": "The common category that both items belong to."
    },
    "item_details": {
      "type": "array",
      "description": "Detailed information about each item mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the item."
          },
          "item_type": {
            "type": "string",
            "description": "The specific type of the item as described in the context (e.g., 'soda', 'carbonated soft drink')."
          },
          "attributes": {
            "type": "object",
            "description": "Specific attributes related to the item.",
            "properties": {
              "full_brand_name": {
                "type": "string",
                "description": "The full brand name of the item, if different from its common name."
              },
              "parent_company": {
                "type": "string",
                "description": "The company that owns or introduced the item."
              },
              "introduction_year": {
                "type": "integer",
                "description": "The year the item was introduced."
              },
              "discontinuation_year": {
                "type": "integer",
                "description": "The year the item was discontinued."
              },
              "creator": {
                "type": "string",
                "description": "The person who created the item."
              },
              "creation_location": {
                "type": "string",
                "description": "The location where the item was created."
              },
              "first_served_year": {
                "type": "integer",
                "description": "The year the item was first served."
              },
              "first_nationally_marketed_year": {
                "type": "integer",
                "description": "The year the item was first nationally marketed."
              },
              "description_detail": {
                "type": "string",
                "description": "A more detailed description or unique characteristic of the item."
              },
              "variants_mentioned": {
                "type": "array",
                "description": "A list of variants or additional flavors mentioned for the item.",
                "items": {
                  "type": "string"
                }
              }
            },
            "required": [],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "item_type",
          "attributes"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "item_names",
    "common_category",
    "item_details"
  ],
  "additionalProperties": false
}
