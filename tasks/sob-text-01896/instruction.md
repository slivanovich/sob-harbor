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
HB Ice Cream: HB Ice Cream (originally an acronym for both Hughes Brothers and Hazelbrook Farm) is an ice cream brand in Ireland and is part of the Unilever Group's Heartbrand ice cream brand.

Peters Ice Cream: Peters Ice Cream is an Australian ice cream brand, now a subsidiary of European food firm R&R Ice Cream.  It was originally developed by an expatriate American, Frederick (Fred) Augustus Bolles Peters in 1907, using his mother's recipe.  The company was established in 1907 at Paddington, New South Wales as the "Peters' American Delicacy Company".  New works to manufacture 'The Health food of a Nation' was opened at neighbouring Redfern in 1923.  Business flourished, in 1927 he set up Peters' Arctic Delicacy Co. Ltd in Brisbane and a branch in Newcastle; followed by, in 1929, associated companies were established in Victoria, Western Australia and at Townsville with manufacturing branch at Queensland.  Peters was largely responsible for introducing to Australia the small refrigerated cabinet, which he hired out to retailers.  The red and cream corporate identity was adopted in New South Wales and Queensland, whilst green and cream were used in Victoria and Western Australia .  The hub of the company, in Australia was a food firm known as Petersville Australia Limited, in the Melbourne suburb of Mulgrave, which later became the factory, which remains the production centre for most of its ice-cream products.

Blue Bell Creameries: Blue Bell Creameries is an American food company that manufactures ice cream.  It was founded in 1907 in Brenham, Texas.  For much of its early history, the company manufactured both ice cream and butter locally.  In the mid-20th century, it abandoned butter production and expanded to the entire state of Texas and soon much of the Southern United States.  The company's corporate headquarters are located at the "Little Creamery" in Brenham, Texas.  Since 1919, it has been in the hands of the Kruse family.  Despite being sold in a limited number of states, as of 2015 Blue Bell is the fourth highest-selling ice cream brand in the United States as a whole.

Rhino Foods: Rhino Foods Incorporated, founded in 1981 by Anne and Ted Castle, is a specialty ice cream novelty and ice cream ingredient manufacturer located in Burlington, Vermont, United States.  Rhino Foods has grown from a small ice cream shop, Chessy's Frozen Custard, into a business with over 100 employees.  In 2013, the company became a certified B Corporation joining over a 1000 companies worldwide in the unified goal to use business as a force for good for people and the planet.  The company is best known locally for their ice cream sandwich, the Chesster.  In 1991, the company worked with Ben & Jerry's to develop the first cookie dough for use in ice cream.  The company produces cookie dough and baked pieces for most major brands in the ice cream industry .  The company also co-packs ice cream cookie sandwiches for national and international companies .

Reuben and Rose Mattus: Reuben and Rose Mattus were Polish Jewish entrepreneurs who founded the Häagen-Dazs ice cream business.

General Mills: General Mills, Inc., is an American multinational manufacturer and marketer of branded consumer foods sold through retail stores.  It is headquartered in Golden Valley, Minnesota, a suburb of Minneapolis.  The company markets many well-known North American brands, including Annie's Homegrown, Betty Crocker, Yoplait, Colombo, Totino's, Pillsbury, Old El Paso, Häagen-Dazs, Cheerios, Trix, Cocoa Puffs, and Lucky Charms.  Its brand portfolio includes more than 89 other leading U.S. brands and numerous category leaders around the world.

Häagen-Dazs: Häagen-Dazs is an American ice cream brand, established by Reuben and Rose Mattus in the Bronx, New York, in 1961.  Starting with only three flavors: vanilla, chocolate, and coffee, the company opened its first retail store in Brooklyn, New York, on November 15, 1976.  The business now has franchises throughout the United States and many other countries around the world including the United Kingdom, India, China, Lebanon and Brazil.

Bonnie Doon Ice Cream: Bonnie Doon Ice Cream was an American ice cream brand established in 1938 by three brothers by the last name of Muldoon.  Bonnie Doon was named after the daughter of one of the brothers, Bonnie Muldoon Witt.  The company was sold in 1990.

Bulla Dairy Foods: Bulla Family Dairy is a major Australian dairy company that manufactures a national and export range of ice cream, table cream, yogurt, sour cream, cottage cheese, and imitation cream under various brands.  The business was established in 1910 and subsequently became a partnership among three inter-related families, who still own and operate the business to this day.  In 1930, the company acquired the Colac Ice Works and the Regal Cream brand which continued as a local ice cream route brand until 2004 when it was re-badged as Bulla.  The company employs over 450 people across three manufacturing sites in Colac, Victoria, Dandenong, Victoria, and also in Mulgrave, Victoria, and a head office and distribution centre in Derrimut, Melbourne.

HB Wall's: HB Wall's is an ice cream brand in Northern Ireland and is part of the Unilever Group's heartbrand ice cream brand.

Question: The ice cream brand established by Reuben and Rose Mattus is now marketed by a company headquartered in what city and state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "ice_cream_brand": {
      "type": "string",
      "description": "The name of the ice cream brand."
    },
    "founders": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the founders of the ice cream brand."
    },
    "marketing_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the company that markets the ice cream brand."
        },
        "headquarters_city": {
          "type": "string",
          "description": "The city where the marketing company is headquartered."
        },
        "headquarters_state": {
          "type": "string",
          "description": "The state where the marketing company is headquartered."
        }
      },
      "required": [
        "name",
        "headquarters_city",
        "headquarters_state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "ice_cream_brand",
    "founders",
    "marketing_company"
  ],
  "additionalProperties": false
}
