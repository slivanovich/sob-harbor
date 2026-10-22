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
Storables: Storables is a specialty retail chain that carries a variety of products aimed at helping consumers organize their homes and work spaces in the West Coast of the United States.  Its products are categorized into departments including Audio, Baskets, Bath, Closets, Furniture, Kids, Kitchen, Laundry, Novelty, Office, and Utility.  The company's motto is "Make Room for Living."

The Container Store: The Container Store Group, Inc. is an American specialty retail chain company that operates The Container Store, which offers storage and organization products.

Hold Everything (store): Hold Everything was a specialty retail chain in the United States that sold home organization and storage solutions.  Its parent company, Williams-Sonoma, closed the chain's 11 existing stores in 2006.

Organized Living: Organized Living, formerly known as Schulte Corp., is a company that manufactures storage and organization products for the home, sold through independent dealers in the United States and Canada.  Prior to 2007, Organized Living was a specialty retail chain in the United States that sold storage solutions for home and office.

The Collection at RiverPark: The Collection at RiverPark is an outdoor lifestyle center located east of the 101 Freeway in Oxnard, California.  The shopping center held its grand opening on November 15, 2012; and is anchored by Target, Whole Foods Market, REI, The Container Store, and a sixteen-screen Cinemark cinema.  Originally meant to open in 2008, The Collection was delayed over several years due to the Great Recession.

Deb Shops: Deb Shops is a catalog and online retailer, formerly a specialty retail chain store in the United States that sold women's clothing and accessories under its own private labels as well as other labels.  The company was based in Philadelphia, Pennsylvania and principally served junior and plus-sized women in their early teens through their late twenties.  At its peak, Deb Shops operated 337 stores across 42 states.  They have moved to become exclusively a plus-size store.

Chain store: Chain store(s) or retail chain are retail outlets that share a brand and central management, and usually have standardized business methods and practices.  In retail, dining, and many service categories, chain businesses have come to dominate the market in many parts of the world.  A franchise retail establishment is one form of chain store.  In 2004, the world's largest retail chain, Wal-Mart, became the world's largest corporation based on gross sales.

Hachette Distribution Services: Hachette Distribution Services is the distribution arm of French media group Hachette.  In Canada and the United States, they operate a specialty retail chain under the name HDS Retail.  HDS Retail chains are found in airports, hotels, and malls across North America.  HDS is a wholly owned subsidiary of Lagardere Services, which is the largest travel retailer, with over 1,600 stores in 18 countries covering 4 continents.

Schurman Retail Group: Schurman Retail Group is an American stationery, greeting card, gifts, and paper products company based in Fairfield, California.  The company operates brands and retail stores under the names PAPYRUS, NIQUEA.D, and Paper Destiny.  It also sells the American Greetings brand and manages its subsidiaries, including Carlton Cards (in Canada and the U.S.) and Clintons (in the U.K.).  Schurman Retail Group now operates over 450 retail stores across the United States and Canada and manages an additional 400 in the U.K.  It is currently the second-largest American specialty retailer in the greeting card industry.

Tank blanketing: Tank blanketing, also referred to as tank padding, is the process of applying a gas to the empty space in a storage container.  The term storage container here refers to any container that is used to store products, regardless of its size.  Though tank blanketing is used for a variety of reasons, it typically involves using a buffer gas to protect products inside the storage container.  A few of the benefits of blanketing include a longer life of the product in the container, reduced hazards, and longer equipment life cycles.

Question: Which of those that anchored "The Collection at RiverPark" is an American specialty retail chain company that operates The Container Store, which offers storage and organization products?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "retail_chain_name": {
      "type": "string",
      "description": "The name of the specialty retail chain."
    },
    "operating_company": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the company that operates the retail chain."
        },
        "is_american": {
          "type": "boolean",
          "description": "Indicates if the operating company is American."
        }
      },
      "required": [
        "name",
        "is_american"
      ],
      "additionalProperties": false
    },
    "product_offerings": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of product categories offered by the retail chain."
    },
    "anchors_collection_at_riverpark": {
      "type": "boolean",
      "description": "Indicates if the retail chain anchors The Collection at RiverPark."
    }
  },
  "required": [
    "retail_chain_name",
    "operating_company",
    "product_offerings",
    "anchors_collection_at_riverpark"
  ],
  "additionalProperties": false
}
