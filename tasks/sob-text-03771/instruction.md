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
Glowtini: The Glowtini is a cocktail inspired by the Year of a Million Dreams celebration at Walt Disney World Resort, and some Disneyland Resort locations.  Served at restaurants all over Disney World, it consists of Skyy Citrus Vodka, Blue Curacao, peach schnapps, Sweet-N-Sour and pineapple juice, garnished with a souvenir glow cube.

Breakfast martini: A breakfast martini is a form of cocktail created by bartender Salvatore Calabrese.  The most famous "marmalade cocktail", it is a gin martini with marmalade, orange liqueur, and lemon juice in place of vermouth.

20th Century (cocktail): The 20th Century is a cocktail created in 1937 by a British bartender named C.A. Tuck, and named in honor of the celebrated "Twentieth Century Limited" train which ran between New York City and Chicago from 1902 until 1967.  The recipe was first published in 1937 in the "Café Royal Cocktail Book" by William J Tarling, President of the United Kingdom Bartenders' Guild and head bartender at the Café Royal.

Chris McMillian: Chris McMillian is a New Orleans bartender and a co-founder of The Museum of the American Cocktail.  Imbibe Magazine mentioned McMillian as one of the top 25 most influential cocktail personalities of the last century.

Curacao Punch: Curacao Punch is a cocktail that comes from Harry Johnson's New and Improved Bartender's Manual (1882).  Dale DeGroff, a notable bartender and author of The Craft of the Cocktail (Clarkson Potter, 2002), holds this to be his favorite forgotten potation.

Bartender: A bartender (also known as a barkeep, barman, barmaid, bar chef, tapster, mixologist, alcohol server, flairman or a alcohol chef) is a person who formulates and serves alcoholic or soft drink beverages behind the bar, usually in a licensed establishment.  Bartenders also usually maintain the supplies and inventory for the bar.  A bartender can generally mix classic cocktails such as a Cosmopolitan, Manhattan, Old Fashioned, and Mojito.  The bartending profession was generally a second occupation, used as transitional work for students to gain customer experience or to save money for university fees.  This however is changing around the world and bartending has become a profession by choice rather than necessity.  Cocktail competitions such as World Class and Bacardi Legacy have recognised talented bartenders in the past decade and these bartenders, and others, spread the love of cocktails and hospitality throughout the world.

Hanky-Panky cocktail: The Hanky-Panky cocktail was the brainchild of Ada Coleman (known as "Coley") who began as a bartender at the Savoy Hotel in 1903.  Her benefactor was Rupert D'Oyly Carte, a member of the family that first produced Gilbert and Sullivan operas in London and that built the Savoy Hotel.  When Rupert became chairman of the Savoy, Ada was given a position at the hotel's American Bar, where she eventually became the head bartender and made cocktails for the likes of Mark Twain, the Prince of Wales, Prince Wilhelm of Sweden, and Sir Charles Hawtrey.

Robert Hess (cocktail expert): Robert B. Hess is a cocktail expert, a co-founder of the Museum of the American Cocktail, and a technology evangelist for Microsoft.  Hess is the author of "The Essential Bartender's Guide: How to Make Truly Great Cocktails" published by Mud Puddle Books in 2008.  He is also the host of "The Cocktail Spirit," an online video series published by the Small Screen Network.  In late 2008, Hess, along with several other well-known cocktail personalities, founded The Chanticleer Society, a "Worldwide Organization of Cocktail Enthusiasts."  Hess also writes a column entitled "Classic Cocktails" for the bi-monthly fine beverage publication, Mutineer Magazine.

Screwdriver (cocktail): A screwdriver is a popular alcoholic highball drink made with orange juice and vodka.  While the basic drink is simply the two ingredients, there are many variations; the most common one is made with one part vodka, one part of any kind of orange soda, and one part of orange juice.  Many of the variations have different names in different parts of the world.  The International Bartender Association has designated this cocktail as an IBA Official Cocktail.

Bronx (cocktail): The Bronx Cocktail is essentially a Perfect Martini with orange juice added.  It was ranked number three in "The World's 10 Most Famous Cocktails in 1934", making it a very popular rival to the Martini (#1) and the Manhattan (#2).  Today, it remains a popular choice in some markets, and was formerly designated as an Official Cocktail by the International Bartender Association.  Like the Manhattan, the Bronx is one of five cocktails named for one of New York City's five boroughs, but is perhaps most closely related to the Queens, which substitutes pineapple for the Bronx's orange.

Question: Which cocktail was inspired by a bartender, Hanky-Panky cocktail or Glowtini?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cocktail_name": {
      "type": "string",
      "description": "The name of the cocktail that was inspired by a bartender."
    },
    "inspired_by_bartender": {
      "type": "boolean",
      "description": "True if the cocktail was inspired by a bartender, false otherwise."
    },
    "bartender_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the bartender who inspired the cocktail."
        },
        "role": {
          "type": "string",
          "description": "The role or title of the bartender."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "other_inspiration_source": {
      "type": "string",
      "description": "The source of inspiration if not a bartender."
    }
  },
  "required": [
    "cocktail_name",
    "inspired_by_bartender",
    "bartender_details"
  ],
  "additionalProperties": false
}
