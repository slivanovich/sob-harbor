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
California-style pizza: California-style pizza (also known as California pizza or Gourmet pizza) is a style of single-serving pizza that combines New York and Italian thin crust with toppings from the California cuisine cooking style.  Its invention is generally attributed to chef Ed LaDou, and Chez Panisse, in Berkeley, California.  Wolfgang Puck, after meeting LaDou, popularized the style of pizza in the rest of the country.  It is served in a number of California Cuisine restaurants.  Such restaurant chains as California Pizza Kitchen, Extreme Pizza, and Sammy's Woodfired Pizza are three major pizza franchises associated with California-style pizza.  Nancy Silverton's Pizzeria Mozza is also a popular California-style pizza restaurant in Los Angeles.

Pizza 73: Pizza 73 is a Canadian restaurant chain that offers a number of different styles of pizza, along with chicken wings.  It has been operated by Pizza Pizza since 2007.  Toronto-based Pizza Pizza had acquired the restaurant for a total of $CAN70.2 million.  There are 89 locations throughout Western Canada, which include the provinces of British Columbia, Alberta, and Saskatchewan.  The restaurant's name originates from its original phone number: 473–7373.  Founded by David Tougas and Guy Goodwin in 1985, Pizza 73 is headquartered in Edmonton, Alberta, Canada.

Co-op Food: Co-op Food, previously trading as The Co-operative Food, is a brand devised for the food retail business of the consumer co-operative movement in the United Kingdom.  When looking at food retail, the brand is commonly understood to represent one food retail business, though this is not true as it is used by over 15 different co-operative societies which operate over 4,000 outlets.  Successor to Co-op Welcome and a range of regional formats, the latest version of the brand was introduced in 2016 with a significant advertising campaign.  Customers of many of the larger UK co-operative societies can earn an annual share of the profits at any "Co-operative" branded stores in proportion to purchases through The Co-operative Membership scheme.

Aurelio's Pizza: Aurelio's Pizza is an Illinois restaurant chain which centers its business around the thin crust variety of Chicago-style pizza.  Aurelio's Pizza has three corporate owned stores and 37 franchised locations in 6 states.  Aurelio's Pizza is the oldest Chicago pizza franchise restaurant, franchising since 1974.

Agile retail: Agile retail is a direct-to-consumer retail model that uses big data to try to predict trends, manage efficient production cycles, and faster turnaround on emerging styles.  Agile retail applies concepts from Agile and Lean in the retail business, and aims to respond faster to customer needs.  This retail model is used by Amazon.  The concept turns e-commerce retailers into on-demand platforms that identify stock and deliver desired products directly to the consumer, thereby reducing costs.  The main focus of Agile retail is to identify trends that are popular with consumers at a given moment and deliver those products using Agile production concepts.

Peppes Pizza: Peppes Pizza is a Norwegian pizza chain that serves American style and Italian style pizza.  Peppes is the largest pizza chain in Scandinavia.  The restaurant was founded by two Americans, Louis Jordan and his wife Anne from Hartford, Connecticut.  The restaurant chain is part of Umoe Catering As which consists of restaurants such as Burger King, TGI Fridays, La Baguette and Cafe Opus.  Peppes Pizza is one of the first restaurants that brought foreign food to Norway.  9 million pizzas are served by Peppes each year with deliveries in 11 cities in Norway.  Their menu was first put online in March 1995.  The servings have been described as enough for two people and that the pizza chain is "a cut above the rest".

Bullwinkle's Restaurant: Bullwinkle's Restaurant, also known as Family Fun Center, is a chain of family entertainment centers.  Similar to Chuck E. Cheese's, most locations feature a sit-down restaurant, complemented by arcade games, go-karts, bumper boats, mini golf, laser tag, ropes course, zip line, and small rides for children, themed after its namesake, "The Rocky and Bullwinkle Show".

Greek pizza: This style of pizza may be referred to as "Greek pizza" even when it has non-Greek toppings, since it is typical of pizzerias owned by Greek immigrants.  (These pizzas are similar to the pizzas served in Italian-style restaurants in Greece itself.)  These establishments often also sell Greek specialties, such as Greek salads and gyros, and tend to brand themselves as "Pizza and Pasta" or as a "House of Pizza"; a code signifying that it is not an Italian restaurant, but a Greek restaurant serving Italian-style food.  In the United States, the latter usage is common in New England cuisine.

Pizza Fusion: Pizza Fusion is a Deerfield Beach, Florida-based pizza restaurant chain.  Using mostly organic ingredients and emphasizing green building methods, the restaurants operate under the tagline Saving the Earth, One Pizza at a Time.

TigerDirect: TigerDirect is an El Segundo, California-based online retailer dealing in electronics, computers, and computer components that caters to business and corporate customers.  Previously owned by Systemax, which is known for its acquisitions of the intellectual property of the defunct U.S. retail chains Circuit City and CompUSA, and relaunching them as online retailers.  The two brands were subsequently shuttered and consolidated into the TigerDirect site.  In 2015, TigerDirect phased out all of its remaining brick-and-mortar retail operations, and PCM Inc. acquired Systemax's online North American technology retail business.

Question: What type of retail business does Bullwinkle's Restaurant and Pizza Fusion have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_retail_type": {
      "type": "string",
      "description": "The type of retail business that both entities have in common."
    },
    "entities_involved": {
      "type": "array",
      "description": "A list of the entities for which the common retail type was identified.",
      "items": {
        "type": "string"
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the common retail type was determined from the context."
    }
  },
  "required": [
    "common_retail_type",
    "entities_involved",
    "reasoning"
  ],
  "additionalProperties": false
}
