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
2013 Little Caesars Pizza Bowl: The 2013 Little Caesars Pizza Bowl is an American college football bowl game that was played on December 26, 2013 at Ford Field in Detroit, Michigan.  The 17th edition of Little Caesars Pizza Bowl featured the Pittsburgh Panthers from the Atlantic Coast Conference against the Bowling Green Falcons from the Mid-American Conference.  It was one of the 2013–14 bowl games that concluded the 2013 FBS football season.

Your Pie: Your Pie is an American fast casual pizza concept, that was started in Athens, Georgia in 2008 by Drew French, and operates as a restaurant franchise with 58 locations across the United States.  Your Pie provides customizable 10-inch pizzas and build-your-own panini sandwiches and bread bowl salads.  Your Pie uses brick ovens to cook pizzas at a high temperature for a short amount of time.  Gelato (Italian ice cream), craft beer and wine are also available.  The interior décor differs from store to store, but all locations blend “old Italian” style with a modern, artistic approach.

Little Caesars: Little Caesar Enterprises Inc. (doing business as Little Caesars) is the third-largest pizza chain in the United States, behind Pizza Hut and Domino's Pizza.  It operates and franchises pizza restaurants in the United States and internationally in Asia, the Middle East, Australia, Canada, Latin America and the Caribbean.  The company was founded in 1959 and is based in Detroit, Michigan, headquartered in the Fox Theatre building in Downtown.  Little Caesar Enterprises, Inc. operates as a subsidiary of Ilitch Holdings, Inc.

Ilitch Holdings: Ilitch Holdings, Inc. is an American company established in 1999 to provide all companies owned by Marian Ilitch with professional and technical services.  The couple's privately held businesses include Little Caesars Pizza, the National Hockey League (NHL) Detroit Red Wings, the Major League Baseball (MLB) Detroit Tigers, Motor City Casino, Olympia Entertainment, Olympia Development, Blue Line Foodservice Distribution, Champion Foods, Little Caesars Pizza Kit Fund raising Program, and a variety of venues within these entities.  Ilitch Holdings subsidiaries manage Detroit's Fox Theatre, City Theatre, Comerica Park, and the Joe Louis Arena.

Rabbe Grönblom: Rabbe Anders Grönblom (May 3, 1950 Helsinki, Finland – June 29, 2015) was a Finland-Swedish businessman who started a successful pizza business in Vaasa, Finland.  His first company—a pizzeria—was called "O sole mio" and it was founded in 1976 in the center of Vaasa.  From there he expanded to a pizza franchise chain first called "Pizzeria N:o 1".  He was known as the "Pizza-emperor" (Pizzakeisari in Finnish), because he was the founder of a well known pizza franchise chain called Kotipizza which was the new name of "Pizzeria N:o 1" which expanded fast outside of Vaasa.  The chain is said to be the biggest one in the Nordic countries.  He was also the founder of a shipping company called RG Line, a hotel chain called Omenahotelli and another pizza chain called Golden Rax Pizzabuffet.  Most of his companies are subsidiaries of Grönblom International LTD, where Rabbe Grönblom acted as director.  Golden Rax Pizzabuffet however is nowadays a part of Finland's largest hotel & restaurant company Restel Oy Ltd, where Rabbe Grönblom sat on the board.  He was also on the board of the Finnish tyre company Nokian Renkaat (since 2003).

Pizza delivery: Pizza delivery is a service in which a pizzeria or pizza chain delivers a pizza to a customer.  An order is typically made either by telephone or over the internet to the pizza chain, in which the customer can request pizza type, size and other products alongside the pizza, commonly including soft drinks.  Pizzas may be delivered in pizza boxes or delivery bags, and deliveries are made with either an automobile, motorized scooter, or bicycle.  Customers can, depending on the pizza chain, choose to pay online, or in person, with cash, credit or a debit card.  A delivery fee is often charged with what the customer has bought.

Freshslice Pizza: Freshslice Pizza is a Canadian franchised pizza chain in restaurants located throughout British Columbia, and one location in Toronto as of 2016.  The first restaurant opened in 1999 in Vancouver, British Columbia.  Today, Freshslice Pizza is the second-largest pizza chain in British Columbia behind Panago in terms of locations open.

Peppes Pizza: Peppes Pizza is a Norwegian pizza chain that serves American style and Italian style pizza.  Peppes is the largest pizza chain in Scandinavia.  The restaurant was founded by two Americans, Louis Jordan and his wife Anne from Hartford, Connecticut.  The restaurant chain is part of Umoe Catering As which consists of restaurants such as Burger King, TGI Fridays, La Baguette and Cafe Opus.  Peppes Pizza is one of the first restaurants that brought foreign food to Norway.  9 million pizzas are served by Peppes each year with deliveries in 11 cities in Norway.  Their menu was first put online in March 1995.  The servings have been described as enough for two people and that the pizza chain is "a cut above the rest".

Chicago Franchise Systems, Inc.: Chicago Franchise Systems, Inc. franchises operates Italian-based Chicago-style restaurants in Illinois, Georgia, California and Missouri which specialize in Chicago-style cuisine They have operated since 1990, when they took over the popular Nancy's Pizza chain of pizzerias.  Nancy's itself was started in 1971 by Nancy and Rocco Palese, a couple who claims to have invented the concept of stuffed pizza.  Today, there are 36 Nancy's locations in Chicago metropolitan area, as well as two location in the Atlanta, Georgia area, and one in the Los Angeles, CA area.  CFS, Inc. operates Al's Beef, a popular Italian beef restaurant that is extremely well known in downtown Chicago and is regarded as one of the best beef sandwiches in the country.  CFS, Inc. just launched Doughocracy Pizza + Brews, a fast casual pizza place that gives customers the "Freedom to Choose" their own toppings on a hand stretched pizza crust that can be paired with local craft beers.  There are two Doughocracy restaurants, one in Geneva, Illinois and one in University City, Missouri, a suburb of St. Louis.

Four Foods Group: Four Foods Group is an American company based in American Fork, Utah that helps to develop franchises of restaurants by developing new restaurant units, growing same store sales, providing restaurant management services, and training in-store managers.  Four Foods Group currently operates 96 restaurants across the United States, including Kneaders Bakery and Café, Salt Lake City-based restaurant, R&R Barbecue and Arizona-based beverage chain The Soda Shop.  In March 2017, Four Foods Group acquired 48 Little Caesars Pizza restaurants in Alabama and Louisiana in a $33 million deal.

Question: which pizza chain has the  restaurant franchise location Little Caesars: or Your Pie

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pizza_chain_name": {
      "type": "string",
      "description": "The name of the pizza chain."
    },
    "operates_as_franchise": {
      "type": "boolean",
      "description": "Indicates whether the pizza chain operates as a franchise."
    },
    "total_locations": {
      "type": "integer",
      "description": "The total number of restaurant locations for the chain."
    },
    "location_geography": {
      "type": "string",
      "description": "The geographical scope where the chain's locations are found."
    }
  },
  "required": [
    "pizza_chain_name",
    "operates_as_franchise",
    "total_locations",
    "location_geography"
  ],
  "additionalProperties": false
}
