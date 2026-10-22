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
Washington City Canal: The Washington City Canal operated from 1815 until the mid-1850s in Washington, D.C. The canal connected the Anacostia River, called the "Eastern Branch" at that time, to Tiber Creek, the Potomac River, and later the Chesapeake and Ohio Canal (C&O).  The canal fell into disuse in the late 19th century and the city government covered over or filled in various sections.

Whitewater Canal: The Whitewater Canal, which was built between 1836 and 1847, spanned a distance of seventy-six miles and stretched from Lawrenceburg, Indiana on the Ohio River to Hagerstown, Indiana.

Tiber Creek: Tiber Creek or Tyber Creek is a tributary of the Potomac River in Washington, D.C. In the 19th century it was modified to become part of the Washington City Canal, and subsequently was enclosed in a tunnel.

Lake Union: Lake Union is a freshwater lake entirely within the Seattle, Washington city limits and a major portion of the Lake Washington Ship Canal.  Its easternmost point is the Ship Canal Bridge, which carries Interstate 5 over the eastern arm of the lake and separates Lake Union from Portage Bay.  Lake Union is the namesake of the neighborhoods located on its east and west shores: Eastlake and Westlake, respectively.  The northern shore of the lake is home to Gas Works Park.  Notable features of the southern portion of the lake—collectively known as the South Lake Union district—include Lake Union Park, Museum of History & Industry (MOHAI), and the Center for Wooden Boats.

Metamora, Indiana: Metamora is an unincorporated town and census-designated place in Metamora Township, Franklin County, Indiana.  The town was once a stop along the Whitewater Canal and is now primarily dependent on tourism.  As of the 2010 census, it had a population of 188.

Duck Creek Aqueduct: Duck Creek Aqueduct, also known as the Metamora Aqueduct and Whitewater Canal Aqueduct, is a historic aqueduct carrying the Whitewater Canal over Duck Creek in Metamora Township, Franklin County, Indiana.  It is the only surviving covered wood aqueduct in the United States as such it is a form of covered bridge.  It is a single-span Burr through truss aqueduct and measures approximately 90 feet long, 25 feet wide, and 25 feet deep.  The original aqueduct was built between 1839 and 1843.  The present structure was built in 1846, after the original aqueduct was washed out in a flood.  It was strengthened in 1868, and repaired in 1901.  After abandonment and deterioration, the Duck Creek Aqueduct was restored to its present appearance in 1946-1949.

Cincinnati and Whitewater Canal Tunnel: The Cincinnati and Whitewater Canal Tunnel is a historic yet abandoned canal tunnel in the southwestern corner of the U.S. state of Ohio.  Located within the village of Cleves near Cincinnati, it was constructed in 1837 as part of the Whitewater Canal system.  Since the canal's closure, it has largely been forgotten, but it has been designated a historic site.

Whitewater River (Great Miami River): The Whitewater River is a 101 mi southerly flowing right tributary of the Great Miami River in southeastern Indiana and southwestern Ohio in the United States.  It is formed by the confluence of two forks, the West Fork and East Fork.  The name is a misnomer, as there is no true white water on the river.  However, there are many rapids due to the steep gradient present - the river falls an average of 6 ft/mile .  The gradient rendered upstream navigation impossible, and in the mid-nineteenth century resulted in the construction of the Whitewater Canal paralleling the river from north of Connersville, Indiana, to the Ohio River.

Brandenburg City Canal: The Brandenburg City Canal, or Brandenburger Stadtkanal in German, is a canal in the German state of Brandenburg.  It provides a 4 km route through the centre of the city of Brandenburg an der Havel.

Tiber Island (District of Columbia): Tiber Island was a man-made island in Washington, D.C. formed when the Washington City Canal was dug to connect the stream beds of Tiber Creek and James Creek, creating an island out of an existing peninsula southwest of the Capitol.  The canals have since been filled in, rejoining the island to the mainland.  The Southwest Waterfront, Buzzard Point, National Mall, and L'Enfant Plaza areas were once on the island; at that time, their isolation from "the mainland" led to the area's colloquial nickname as "The Island."

Question: Which came first Washington City Canal or Whitewater Canal?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "canals_compared": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "canal_name": {
            "type": "string"
          },
          "construction_start_year": {
            "type": "integer"
          },
          "construction_end_year": {
            "type": "integer"
          }
        },
        "required": [
          "canal_name",
          "construction_start_year"
        ],
        "additionalProperties": false
      }
    },
    "earlier_canal_name": {
      "type": "string"
    },
    "earlier_canal_start_year": {
      "type": "integer"
    },
    "question_canal_one_came_first": {
      "type": "boolean",
      "description": "True if the first canal mentioned in the question (Washington City Canal) came first, false otherwise."
    }
  },
  "required": [
    "canals_compared",
    "earlier_canal_name",
    "earlier_canal_start_year",
    "question_canal_one_came_first"
  ],
  "additionalProperties": false
}
