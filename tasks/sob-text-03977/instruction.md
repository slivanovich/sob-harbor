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
Otto (company): Otto, legal name Ottomotto LLC is an American self-driving technology company established in January 2016 by Lior Ron and Anthony Levandowski.  The San Francisco-based team, which has 90 employees as of August 2016, retrofits semi trucks with radars, cameras and laser sensors to make them capable of driving themselves.  In August 2016 Otto was acquired by the transportation network company Uber.  Co-founder Lior Ron has stated that Otto will have self-driving fleets of trucks on the road by early 2017.

John Krafcik: John Krafcik (born September 18, 1961) is the chief executive officer (CEO) of Waymo Inc. Krafcik was the former president of True Car Inc. and President and CEO of Hyundai Motor America.  His current position was announced In December 2016, after Google separated its self-driving car project and transitioned it into a new company called Waymo, which is now housed under Google’s parent company Alphabet.

Now (The Tubes album): Now is the third album released by The Tubes.  It was produced by John Anthony.  Fed up with constant meddling from Bud Scoppa and Don Wood under the direction of Bill Spooner including surreptitiously remixing a track when John was not at the studio, John Anthony was advised to quit the project by Jerry Moss.  Head of A&M A&R Kip Cohen said they took advantage of John and believed they overran the budget to bump up their union fees.  Bill Spooner took over and completed the project with the help of engineer Don Wood and Bud Scoppa.  John believes in retrospect he should not have tried to be "one of the boys" with this band but remains proud of his idea to get the band playing again live in the studio liked they used to do in the Bay Area bars.  "My Head Is My Only House Unless It Rains" is a firm Anthony favourite and sonically shows what he was trying to achieve.

Basis of estimate: Basis of Estimate a tool used in the field of project management by which members of the project team, usually estimators, project managers, or cost analysts, calculate the total cost of the project.  Through carefully planned equations, hierarchical listing of elements, standard calculations, checklists of project elements and other methods, the project team adds in all expenses of a project, from labor to materials to administrative costs.  These calculations formulate a Basis of Estimate which is, when completed, a number that can be used to determine the ability of the firm or company to carry out the project, or used as a tool in competing for a contract bid or otherwise proposing the project to another.

CodeWeavers: CodeWeavers is a company that sells a proprietary version of Wine called CrossOver for running Windows applications on macOS and Linux.  The company was founded in 1996 as a consultancy, eventually moving entirely over to Wine development and support.  The CrossOver version of Wine is regularly refreshed with the latest free Wine patches; likewise, patches from the company are sent back to the Wine project almost immediately.  CodeWeavers is a major contributor to the Wine project, a free software / open-source software project that helps Windows applications run on different x86-based operating systems, hosts the project's website, and employs the project's maintainer, Alexandre Julliard, as their CTO.

Project finance: Project finance is the long-term financing of infrastructure and industrial projects based upon the projected cash flows of the project rather than the balance sheets of its sponsors.  Usually, a project financing structure involves a number of equity investors, known as 'sponsors', a 'syndicate' of banks or other lending institutions that provide loans to the operation.  They are most commonly non-recourse loans, which are secured by the project assets and paid entirely from project cash flow, rather than from the general assets or creditworthiness of the project sponsors, a decision in part supported by financial modeling.  The financing is typically secured by all of the project assets, including the revenue-producing contracts.  Project lenders are given a lien on all of these assets and are able to assume control of a project if the project company has difficulties complying with the loan terms.

Kolkata Metro Line 4: The Line 4, or Noapara Barasat Line of the Kolkata Metro.  It is a 18.50 km long metro from Noapara to Barasat is under construction, It is being built by RVNL.  It is a fully elevated corridor.  It will have an interchange station at the airport with line 6 of the Kolkata metro.  The future of the project beyond airport is still in darkness due to land problem.  After Kolkata airport the metro route will pass through a land owned by a private company.  When the project was sanctioned, then railway minister Mamtaa Banerjee vested this land for metro project but the company moved to High court against it making the future of the project beyond airport in darkness.  Till now so solution came.  The construction company L&T was given the tender for construction but due to no hope of getting rid of land problem beyond airport, they walked out from the construction.  In Barasat, heavy traffic jam is a burning problem for the citizens.  Metro project would have given them a breath.  But still now no hope arose to the citizens.  However, the future of the alignment beyond airport is still uncertain.

Anthony Levandowski: Anthony Levandowski (born March 15, 1980) is an American self-driving car engineer.  In 2016 he co-founded Otto, an autonomous trucking company, with Lior Ron, Claire Delaunay and Don Burnette.  Prior to Otto, he built the Google self-driving car while working as a co-founder and technical lead on the project, known as Waymo.  He is known for his work in the advancement of self-driving technology.

Lior Ron (business executive): Lior Ron (born March 16, 1977) is an Israeli-born businessman.  He served in the Israel Defense Forces from 1997 to 2004, before attending Stanford to pursue a MBA.  In 2016 he co-founded Otto, a self-driving truck company, with Anthony Levandowski, Claire Delaunay and Don Burnette.  Prior to Otto he was the Product Lead for Google Maps and then the Product Lead for Motorola Mobility, which was acquired by Google in 2011.

Waymo: Waymo is an autonomous car development company spun out of Google's parent company, Alphabet Inc., in December 2016.  It then took over the self-driving car project which Google had begun in 2009.  Alphabet describes Waymo as "a self-driving tech company with a mission to make it safe and easy for people and things to move around".  The new company, which will be headed by long-time automotive executive John Krafcik, is working towards making self-driving cars available to the public soon.  From the company's FAQ:

Question: Anthony Levandowski's project, Waymo, is from what company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company being described."
    },
    "company_type": {
      "type": "string",
      "description": "The primary type or focus of the company."
    },
    "parent_company_at_spin_out": {
      "type": "string",
      "description": "The name of the parent company from which the company spun out."
    },
    "original_project_developer": {
      "type": "string",
      "description": "The company that originally developed the project before it became a separate entity."
    },
    "spin_out_year": {
      "type": "integer",
      "description": "The year the company was spun out."
    },
    "ceo_at_spin_out": {
      "type": "string",
      "description": "The CEO appointed when the company was formed or spun out."
    }
  },
  "required": [
    "company_name",
    "company_type",
    "parent_company_at_spin_out",
    "original_project_developer",
    "spin_out_year",
    "ceo_at_spin_out"
  ],
  "additionalProperties": false
}
