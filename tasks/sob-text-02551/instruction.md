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
Reese's Fast Break: Reese's Fast Break (or, in Canada, Hershey Sidekick) is a chocolate bar produced by the Hershey Company.  Like Reese's Peanut Butter Cups, another Hershey product, Reese's Fast Break has a milk chocolate coating over a peanut butter filling.  However, the Fast Break also has a layer of nougat beneath the peanut butter.

Reese's Puffs: Reese's Puffs (formerly Reese's Peanut Butter Puffs) is a breakfast cereal manufactured by General Mills inspired by Reese's Peanut Butter Cups.  At its launch in 1994, the cereal consisted of grain puffs flavored with chocolate and peanut butter.  Later the format was revised to be a mixture of chocolate puffs and peanut butter puffs.

Joseph L. Rosefield: Joseph Louis Rosefield (18 Dec 1882 - 8 Nov 1958) was a California food businessman who invented modern, non-separating peanut butter in 1922 – 1923.  His family business, the Rosefield Packing Company, was based in Alameda.  His new production process was licensed to another company to make Peter Pan peanut butter in 1923.  Rosefield Packing later marketed Skippy peanut butter in 1932; both brands are still sold today.  It also introduced cylindrical "wide-mouth" jars for peanut butter in 1935.  Peanut butter then became a vast food industry.  Among other roles, Rosefield Packing provided emergency supplies of peanut butter to Hawaii during World War II.  Rosefield's family sold Rosefield Packing and the Skippy brand to Best Foods in 1955.

Reese's Pieces: Reese's Pieces are a peanut butter candy manufactured by The Hershey Company solely for the North American market; they are oblate spheroid in shape and covered in candy shells that are colored yellow, orange, or brown.  They can be purchased in plastic packets, cardboard boxes, or cup-shaped travel containers.  The candy was introduced in 1977, and introduced to Canada in 1980.  The then relatively new product became very popular with the 1982 release of "E.T. the Extra-Terrestrial", in which the candy is featured.

Peanut butter cup: A peanut butter cup is a molded chocolate candy with a peanut butter filling inside.  Peanut butter cups are one of the most popular kinds of candy confection in America.  They can be made at home, but like most candies, they are commonly mass-produced.  They may also be available in candy shops, produced by local or regional candymakers.

John H. Dowd: John H. Dowd (1922–2004) was a Hershey Chocolate Company brand manager, best known for negotiating the agreement that placed Reese's Pieces to tie in with Steven Spielberg's "E.T. the Extra-Terrestrial".

Reese's Peanut Butter Cups: Reese's Peanut Butter Cups are a popular American candy consisting of a milk, white, or dark chocolate cup filled with peanut butter, marketed by The Hershey Company.  They were created in 1928 by H. B. Reese, a former dairy farmer and shipping foreman for Milton S. Hershey.  Reese was inspired by Hershey and left dairy farming to start his own candy business.

Jif (peanut butter): Jif is an American brand of peanut butter made by The J.M. Smucker Company, which purchased the brand from Procter & Gamble in 2001.  In 1955, Procter & Gamble bought Big Top peanut butter from William T. Young of Kentucky and, in the ensuing years, reformulated and rebranded it to compete with Skippy and Peter Pan.  P. & G. named its product Jif, used oils other than peanut oil in its hydrogenation process, and sweetened the recipe, adding sugar and molasses.  The original "Creamy" and "Crunchy" style Jif peanut butters both debuted in 1958.  In 1974, "Extra Crunchy Jif" was introduced, followed in 1991 by "Simply Jif", a peanut butter variant with low sodium and less sugar than regular Jif.  "Reduced Fat Jif" was introduced three years later in 1994.  In 2014, "Jif Whips" was released as the first whipped peanut butter.

Justin's: Justin's is an American brand of natural and organic nut butters and peanut butter cups.  The Boulder-based company manufactures and markets jars and single-serve squeeze packs of nut butter, along with various kinds of organic peanut butter cups.  Justin's peanut butter cups are USDA-certified organic and use Rainforest Alliance Certified cocoa.  Both the peanut butter cups and nut butters are distributed through stores such as Whole Foods Market, Starbucks, and Target in the United States.

Swoops: Swoops were a Pringle-shaped chocolate candy manufactured by The Hershey Company.  They were produced in the following flavors: Hershey's Milk Chocolate, Reese's Peanut Butter, Almond Joy, York Peppermint Pattie, White Chocolate Reeses, and Toffee and Almond.  Limited edition varieties included White Chocolate Peppermint (available around Christmas), Special Dark with Almonds, and Strawberries & Creme.

Question: Who was best known for negotiating the agreement that placed a peanut butter candy manufactured by The Hershey Company in with Steven Spielberg's "E.T. the Extra-Terrestrial"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person."
        },
        "title": {
          "type": "string",
          "description": "The professional title or role of the person."
        },
        "known_for_summary": {
          "type": "string",
          "description": "A summary of what the person is best known for."
        }
      },
      "required": [
        "name",
        "title",
        "known_for_summary"
      ],
      "additionalProperties": false
    },
    "negotiation_event": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film involved in the product placement."
        },
        "film_director": {
          "type": "string",
          "description": "The director of the film."
        }
      },
      "required": [
        "film_title",
        "film_director"
      ],
      "additionalProperties": false
    },
    "product_involved": {
      "type": "object",
      "properties": {
        "product_name": {
          "type": "string",
          "description": "The name of the product placed in the film."
        },
        "product_category": {
          "type": "string",
          "description": "The general category of the product."
        },
        "manufacturer": {
          "type": "string",
          "description": "The company that manufactures the product."
        }
      },
      "required": [
        "product_name",
        "product_category",
        "manufacturer"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_of_interest",
    "negotiation_event",
    "product_involved"
  ],
  "additionalProperties": false
}
