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
Mikado (game): Mikado is a pick-up sticks game originating in Europe.  In 1936, it was brought from Hungary (where it was called Marokko) to the United States and named pick-up sticks.  It is a trivial game of India too, played in country side since it was named mikado.  This term is not very specific in respect to existing stick game variations.  Probably the "Mikado" name was not used because it was a brand name of a game producer.  The game got its name from the highest scoring (blue) stick "Mikado" (Emperor of Japan).  The buddhistic Chien Tung also contains a stick called "emperor".

2-8-2+2-8-2: Under the Whyte notation for the classification of steam locomotives by wheel arrangement, a 2-8-2+2-8-2 is an articulated locomotive using a pair of 2-8-2 power units back to back, with the boiler and cab suspended between them.  The 2-8-2 wheel arrangement has a single pair of leading wheels in a leading truck, followed by four coupled pairs of driving wheels and a pair of trailing wheels in a trailing truck.  Since the 2-8-2 type was known as Mikado, the corresponding Garratt and Modified Fairlie types were usually known as Double Mikado.

Sports memorabilia: The term sports memorabilia usually refers to a souvenir, memento, keepsake or token of remembrance that is directly connected to a famous athlete, sporting event or personality.  These items are generally collected by fans that find sentimental and/ or monetary value of the item(s).  There is no set parameter regarding the amount of items, type of sport, or even the era that an item may reflect.  A piece of certain kind may be considered a collectable item.

Stock keeping unit: In the field of inventory management, a stock keeping unit (SKU) ( , or ) is a distinct type of item for sale, such as a product or service, and all attributes associated with the item type that distinguish it from other item types.  For a product, these attributes could include, but are not limited to, manufacturer, description, material, size, color, packaging, and warranty terms.  When a business takes an inventory, it counts the quantity it has of each SKU.

Quadratic knapsack problem: The quadratic knapsack problem (QKP), first introduced in 19th century, is an extension of knapsack problem that allows for quadratic terms in the objective function: Given a set of items, each with a weight, a value, and an extra profit that can be earned if two items are selected, determine the number of item to include in a collection without exceeding capacity of the knapsack, so as to maximize the overall profit.  Usually, quadratic knapsack problems come with a restriction on the number of copies of each kind of item: either 0, or 1.  This special type of QKP forms the 0-1 quadratic knapsack problem, which was first discussed by Gallo et al.

St. Louis–San Francisco 4003: St. Louis–San Francisco 4003 is a 2-8-2, Mikado type, standard gauge steam railway locomotive built by the American Locomotive Company in 1919 as a standard USRA Light Mikado for the Pennsylvania Railroad.  The PRR, for unknown reasons, rejected 33 of 38 locomotives in the order.  The United States Railroad Administration reassigned 23 of them (road numbers 4000-4007 and 4017-4031) to the St. Louis–San Francisco Railway (SLSF), also known as the "Frisco".  The Frisco also received 10 sisters from the Indiana Harbor Belt Railroad (road numbers 4008-4016 and 4032), making 33 in all.  She is now on display at the Fort Smith Trolley Museum in Fort Smith, Arkansas.

Ladder match: A ladder match is a type of match in professional wrestling, most commonly one where an item (usually a title belt) is hung above the ring, and the winner is the contestant who climbs a ladder and retrieves the item.  The ladder itself becomes a key feature of the match, as wrestlers will use the ladder as a weapon to strike the opponent(s), as a launching pad for acrobatic attacks, and frequently these matches include impressive falls from the top of the ladder.  However, there were very few matches in which the hung item must be used in a special manner in order to win the match, such as striking the opponent with the item (see Bam Bam Bigelow Vs. Scott Hall taser match, where one must strike the opponent with the taser, regardless of who retrieved the taser first).

Kind (type theory): In the area of mathematical logic and computer science known as type theory, a kind is the type of a type constructor or, less commonly, the type of a higher-order type operator.  A kind system is essentially a simply typed lambda calculus "one level up", endowed with a primitive type, denoted formula_1 and called "type", which is the kind of any data type which does not need any type parameters.

Free response: Free response, usually referred to as essay, is a type of question used in tests in education, workplace, and government.  Most free response questions ask or require the test-taker to state a belief, opinion, or write a short essay and support it with facts, examples, or other evidence.  However, few tests solely rely on these types of problems, and tend to work in conjunction with other types, such as multiple choice.  Free response questions generally test more than straight knowledge and ask for a "big picture" type of response "(see example)".  Also, they usually allow the taker to choose an area in which they are familiar.  According to National Council on Measurement in Education, a free-response item is a test item in which the responders must create a response or product rather than choose a response from a set supplied with the item.  A short-answer item, mathematics problem, and writing sample are examples.

Zingo!: Zingo!  is a game inspired by Bingo released by ThinkFun in 2002.

Question: Zingo! and Mikado, is a type of which kind item?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "items_classified": {
      "type": "array",
      "description": "A list of items that are being classified.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the item."
          },
          "contextual_description": {
            "type": "string",
            "description": "A description of the item as found in the context, highlighting its type."
          }
        },
        "required": [
          "name",
          "contextual_description"
        ],
        "additionalProperties": false
      }
    },
    "common_category": {
      "type": "string",
      "description": "The common category that all listed items belong to."
    },
    "is_a_game": {
      "type": "boolean",
      "description": "Indicates whether the common category is 'game'."
    }
  },
  "required": [
    "items_classified",
    "common_category",
    "is_a_game"
  ],
  "additionalProperties": false
}
