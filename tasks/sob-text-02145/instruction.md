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
Pizza Land: Pizza Land is an independently owned pizzeria located at 260 Belleville Turnpike in North Arlington, New Jersey, which featured in the opening credits of "The Sopranos".  Additionally, in "Law & Order" episode 10.6, "Marathon" (1999), a pizza box from the restaurant was used by a suspect to transport and conceal firearms.  The pizzeria was opened in 1965 by Italian immigrant Frank Di Piazza, who died in 1991.  The pizzeria was built by Pietro Di Piazza.  It was owned by Frank's son Tony Di Piazza .  Tony and Debra Hunkele always had the pizzeria packed but later on sold to pizza maker Al Pawlowicz until his death in 2010, who purchased the restaurant from DiPiazza's son.  The store is now owned by Eddie Twdroos.

Donatos Pizza: Donatos Pizza is a pizza delivery restaurant chain headquartered in Columbus, Ohio.  It has nearly 200 locations in eight states, with the majority of locations in Ohio.  Donatos is also served at several venue outlets including Ohio Stadium and the Smithsonian National Air and Space Museum.

Big Mama's &amp; Papa's Pizzeria: Big Mama's & Papa's Pizzeria is a pizza restaurant chain primarily located in Southern California.  The chain is notable for its extremely large "Giant Sicilian" pizza, which is claimed to be the largest deliverable pizza in the world.  Additionally, the chain gained notoriety when, during the 2014 Academy Awards, host Ellen Degeneres had Big Mama's pizzas delivered onstage.

Uno Pizzeria &amp; Grill: Uno Pizzeria & Grill (formerly Pizzeria Uno and Uno Chicago Grill), or more informally as Unos, is a franchised pizzeria restaurant chain under the parent company Uno Restaurant Holdings Corporation.  Uno Pizzeria and Grill is best known for its Chicago-style deep dish pizza.  Ike Sewell opened the first Pizzeria Uno in 1943.

Tutta Bella Neapolitan Pizzeria: Tutta Bella Neapolitan Pizzeria is an Italian restaurant chain with five locations in Washington State.  The first location was founded in 2004.  The restaurant specializes in "authentic" Neapolitan pizza and is certified by the non-profit Associaziona Verace Pizza Napoletana ("True Neapolitan Pizza Association") which certifies pizzerias that use traditional ingredients and processes.  Tutta Bella was the first restaurant in the Pacific Northwest to receive such certification.

Peppes Pizza: Peppes Pizza is a Norwegian pizza chain that serves American style and Italian style pizza.  Peppes is the largest pizza chain in Scandinavia.  The restaurant was founded by two Americans, Louis Jordan and his wife Anne from Hartford, Connecticut.  The restaurant chain is part of Umoe Catering As which consists of restaurants such as Burger King, TGI Fridays, La Baguette and Cafe Opus.  Peppes Pizza is one of the first restaurants that brought foreign food to Norway.  9 million pizzas are served by Peppes each year with deliveries in 11 cities in Norway.  Their menu was first put online in March 1995.  The servings have been described as enough for two people and that the pizza chain is "a cut above the rest".

California-style pizza: California-style pizza (also known as California pizza or Gourmet pizza) is a style of single-serving pizza that combines New York and Italian thin crust with toppings from the California cuisine cooking style.  Its invention is generally attributed to chef Ed LaDou, and Chez Panisse, in Berkeley, California.  Wolfgang Puck, after meeting LaDou, popularized the style of pizza in the rest of the country.  It is served in a number of California Cuisine restaurants.  Such restaurant chains as California Pizza Kitchen, Extreme Pizza, and Sammy's Woodfired Pizza are three major pizza franchises associated with California-style pizza.  Nancy Silverton's Pizzeria Mozza is also a popular California-style pizza restaurant in Los Angeles.

Ledo Pizza: Ledo Pizza is a pizzeria restaurant chain in the Mid-Atlantic and Southeastern United States headquartered in Annapolis, Maryland.  Their first pizzeria was opened in Adelphi, Maryland, in 1955 on University Boulevard (Maryland Route 193) in Adelphi Shopping Center near the University of Maryland, College Park ( ).  The first franchise was granted to the Fireside Restaurant in Berwyn Heights, Maryland, in 1979.  Fireside Restaurant no longer exists.  There are now over 100 restaurants in Maryland, Virginia, West Virginia, South Carolina, and Florida.

Sarpino's Pizzeria: Sarpino's Pizzeria is a fast food restaurant chain specializing in pizza, with international operations headquartered in Singapore and U.S. operations headquartered in the Chicago suburb of Lincolnshire, Illinois.

Rabbe Grönblom: Rabbe Anders Grönblom (May 3, 1950 Helsinki, Finland – June 29, 2015) was a Finland-Swedish businessman who started a successful pizza business in Vaasa, Finland.  His first company—a pizzeria—was called "O sole mio" and it was founded in 1976 in the center of Vaasa.  From there he expanded to a pizza franchise chain first called "Pizzeria N:o 1".  He was known as the "Pizza-emperor" (Pizzakeisari in Finnish), because he was the founder of a well known pizza franchise chain called Kotipizza which was the new name of "Pizzeria N:o 1" which expanded fast outside of Vaasa.  The chain is said to be the biggest one in the Nordic countries.  He was also the founder of a shipping company called RG Line, a hotel chain called Omenahotelli and another pizza chain called Golden Rax Pizzabuffet.  Most of his companies are subsidiaries of Grönblom International LTD, where Rabbe Grönblom acted as director.  Golden Rax Pizzabuffet however is nowadays a part of Finland's largest hotel & restaurant company Restel Oy Ltd, where Rabbe Grönblom sat on the board.  He was also on the board of the Finnish tyre company Nokian Renkaat (since 2003).

Question: Which restaurant chain has a larger international presence, Sarpino's Pizzeria or Donatos Pizza?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "string",
      "description": "The name of the restaurant chain with the larger international presence."
    },
    "chains_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "chain_name": {
            "type": "string",
            "description": "The name of the pizza chain."
          },
          "has_international_operations": {
            "type": "boolean",
            "description": "Indicates if the chain has operations outside its primary domestic country."
          },
          "international_headquarters_location": {
            "type": "string",
            "description": "The location of the international headquarters, if applicable."
          },
          "domestic_locations_summary": {
            "type": "string",
            "description": "A summary of the chain's domestic presence."
          }
        },
        "required": [
          "chain_name",
          "has_international_operations"
        ],
        "additionalProperties": false
      },
      "description": "Details about each chain compared regarding their international presence."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why one chain has a larger international presence."
    }
  },
  "required": [
    "comparison_result",
    "chains_compared",
    "reasoning"
  ],
  "additionalProperties": false
}
