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
Round Table Pizza: Round Table Pizza is a large chain of pizza parlors in the western United States.  The company's headquarters are located in Concord, California.

Yellow Cab Pizza: Yellow Cab Pizza Company is a Filipino chain that retails fast food, primarily pizza.  In 2001, Yellow Cab Pizza Company was founded by Eric Puno, Henry Lee, and Albert Tan.  Max's Group, owner of restaurant chain Max's of Manila, owns the brand.  The restaurant also operates 145 branches in Qatar, United Arab Emirates, and China.

East German Round Table: Round table refers to the Central Round Table ("Zentraler Runder Tisch") that convened in East Berlin on December 7, 1989, the day after Egon Krenz, the new head of the Socialist Unity Party (SED) government, resigned.  This Round Table, modeled after the Polish Round Table convened in April 1989, was initiated by the group Democracy Now.  It was set up as a forum in which members of East German government organizations (such as the so-called block parties, trade unions, the women’s league, etc.) came together with representatives of the new citizens’ movements (such as Democracy Now, Democratic Awakening, and New Forum) to discuss and advance reforms in the German Democratic Republic (East Germany), advising the executive until new national elections could be held.  There were 39 representatives at the Central Round Table, 33 with voting rights.  Seventeen of them represented new oppositional groups and political parties, and 16 were from political parties and organizations that had been part of the official East German government.  Three, representing women, consumers and environmentalists, had observer status.  The final three members were the moderators, all clergymen, from the Protestant, Catholic and Methodist churches, who did not have the right to vote.  At first most participants hoped to reform the East German government and thus retain the country’s independence, but as popular opinion moved towards rapid unification with West Germany, these hopes were dashed.

Round Table: The Round Table is King Arthur's famed table in the Arthurian legend, around which he and his Knights congregate.  As its name suggests, it has no head, implying that everyone who sits there has equal status.  The table was first described in 1155 by Wace, who relied on previous depictions of Arthur's fabulous retinue.  The symbolism of the Round Table developed over time; by the close of the 12th century it had come to represent the chivalric order associated with Arthur's court, the Knights of the Round Table.

Menlo Park station: Menlo Park is a Caltrain station located in Menlo Park, California.  The station was originally built in 1867 by the San Francisco and San Jose Railroad and acquired by the Southern Pacific Railroad.  During the 1890s, Southern Pacific added Victorian ornamentation to the depot to make it appear more attractive to students and visitors to Stanford University.  The station was added to the National Register of Historic Places in 1974, and became a California Historical Landmark in 1983.  It is also within walking distance of the oldest Round Table Pizza.

Papa Murphy's: Papa Murphy's, a business based in Vancouver, Washington, United States, is a take-and-bake pizza company.  It began in 1995 as the merger of two take-and-bake pizza companies: Papa Aldo's Pizza (founded in 1981) and Murphy's Pizza (founded in 1981).  The company and its franchisees operate more than 1,300 outlets in the United States and Canada.  Papa Murphy's is the fifth-largest pizza chain in the United States.

Domino's Pizza Enterprises: Domino's Pizza Enterprises Limited (DPE) is the largest pizza chain in Australia in terms of network store numbers and network sales, as well as the largest franchisee for the Domino’s Pizza brand in the world.  DPE is the exclusive master franchise for the Domino’s brand network in Australia, New Zealand, France, Belgium, the Netherlands, the Principality of Monaco, Japan and Germany.  Across these markets, DPE has over 1900 stores.  In May 2005 DPE became the first publicly listed pizza company in Australia.

JS Food Plan: JS Food Plan Co, Ltd. (commonly referred to as "JS" (which is an acronym for the Korean name Jae Sang) (hangul:제이에스 푸드플랜) is a franchised Korean pizza company headquartered in Yeoeuido-Dong Yeongdeungpo-gu, Seoul, Korea, established in 1998 the company is currently CEO'd by Jeong Jae Sang (정재상).  Its brand name is Pizza Segyero.  (hangul:피자 세계로) In 2005, the company became an international franchise when it expanded to Beijing, China.  The company is comparable to pizza restaurant chains such as Hankook Pizza Hut, Hankook Mr. Pizza, Chicken Nara, Domino Pizza Korea, Pizza Etang and Reach Beam.

Massification: Massification is a strategy that some luxury companies use in order to attain growth in the sales of product.  Some luxury brands have taken and used the concept of massification to allow their brands to grow to accommodate a broader market.  As a method of implementing massification, companies have created diffusion lines.  Diffusion lines are an offshoot of a company or a designers original line that is less expensive in order to reach a broader market and gain a wider consumer base.  Another strategy used in massification is brand extensions, which is when an already established company releases a new product under their name.

Pizza Corner: Pizza Corner was an international franchise of pizzeria chains that offers a wide range of pizzas, pastas and side dishes from chicken wings to salads. Pizza Corner operated as both standalone restaurants or combined with other Global Franchise Architects brands such as Coffee World or Cream & Fudge.  Its service formats include: large dine-in restaurants, delivery outlets, express dine-ins, and express kiosks.

Question: Which pizza company has a broader market, Pizza Corner or Round Table Pizza

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "broader_market_company": {
      "type": "string",
      "description": "The name of the pizza company identified as having a broader market."
    },
    "companies_compared": {
      "type": "array",
      "description": "Details about the market presence of each pizza company being compared.",
      "items": {
        "type": "object",
        "properties": {
          "company_name": {
            "type": "string",
            "description": "The name of the pizza company."
          },
          "market_description": {
            "type": "string",
            "description": "A description of the company's market reach or operational scope."
          }
        },
        "required": [
          "company_name",
          "market_description"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why one company has a broader market than the other."
    }
  },
  "required": [
    "broader_market_company",
    "companies_compared",
    "reasoning"
  ],
  "additionalProperties": false
}
