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
Cody Connelly: Cody Connelly is an American motorcycle builder, best known for his work at Orange County Choppers (OCC), the subject of the American TV show "American Chopper".  Cody left Orange County Choppers and joined V-Force Customs (a custom motorcycle shop in Rock Tavern, NY) where he works with friend and former colleague of Orange County Choppers Vincent DiMartino.  Cody has since made several appearances on the show "" alongside Paul Teutul, Jr. and DiMartino, helping out at Paul Jr.  Designs.

Michael Teutul: Michael Joseph Teutul (born November 26, 1978) is a television celebrity who appeared on the reality programs "Orange County Choppers" "American Chopper" and "".

Custom motorcycle: A custom motorcycle is a motorcycle with stylistic and/or structural changes to the 'standard' mass-produced machine offered by major manufacturers.  Custom motorcycles might be unique, or built in limited quantities.  While individual motorcyclists have altered the appearance of their machines since the very first days of motorcycling, the first individualized motorcycles specifically labeled 'Custom' appeared in the late 1950s, around the same time as the term was applied to custom cars.  In the 1960s, custom artisans like Arlen Ness and Ben Hardy created new styles of custom bikes, the chopper.  In the 1990s and early 2000s, very expensive customs such as those built by Orange County Choppers, Jesse James's West Coast Choppers, Roger Goldammer became fashionable status symbols.  There are also companies that are bringing back pin striping, such as Kenny Howard (also known as Von Dutch) and Dean Jeffries from the 1950s, with a continued effort to keep pin striping alive.  The choppers of the 1960s and 1970s fit into this category.

Paul Jr. Designs: Paul Jr.  Designs (PJD) is a lifestyle brand motorcycle customizer and clothing vendor based in Rock Tavern, New York, USA.  Paul Teutul Jr. founded the design firm in 2009 after waiting out a one-year non-compete clause with his former company, Orange County Choppers (OCC).

Paul Teutul Sr.: Paul John Teutul is the founder of Orange County Choppers, a manufacturer of custom motorcycles and the focus of the reality television series "American Chopper".  Teutul first appeared on the show with his sons Paul Teutul Jr., Michael Teutul.  In 2013 his new show "Orange County Choppers" premiered on CMT

Orange County Choppers bikes: Orange County Choppers bikes are motorcycles featured on the television series "American Chopper" built by Orange County Choppers (OCC) for a specific corporate or celebrity customer.  Theme bikes are motorcycles in which the theme of the motorcycle takes priority over everything else, influencing the frame dimensions, paint scheme, and overall 'feel' of the motorcycle.  The function of motorcycle usually takes a backseat to the presentation of the theme, and these motorcycles attract attention solely on the premise of the theme itself.  Customer bikes are built for and generally to the specifications of a particular customer.  Although the customers typically give OCC creative freedom to do what they will, some clients have a specific idea in mind and expect OCC to reproduce their mental picture literally.

American Chopper: American Chopper is an American reality television series that aired on Discovery Channel from 2003-2010, produced by Pilgrim Films & Television.  The series centers on Paul Teutul, Sr. (frequently called "Senior"), and his son Paul Teutul, Jr. (also known as "Paulie" or simply "Junior"), who manufacture custom chopper-style motorcycles.  Orange County Choppers is in Newburgh, New York.  The contrasting work and creative styles of the father and son team and their resulting verbal arguments were the series' hallmark until 2008 when an explosive argument led to Paul Jr.'s termination and departure to start a competing chopper company (Paul Jr.  Designs).

Vincent DiMartino: Vincent "Vinnie" DiMartino (born October 9, 1972) is an American motorcycle builder, best known for his work from 2002 to 2007 at Orange County Choppers (OCC), the subject of the American TV show "American Chopper".  In August 2007 DiMartino left Orange County Choppers and founded V-Force Customs, a custom motorcycle shop in Rock Tavern, NY.  Several months later, Cody Connelly, a friend and co-worker of DiMartino at Orange County Choppers also left to join him at V-force Customs.  In 2010, DiMartino returned to the show; however instead of rejoining his former employer, OCC, he joined Paul Jr.  Designs.

Paul Teutul Jr.: Paul Michael Teutul (born October 2, 1974) was one of the stars of the American reality television series "American Chopper".  He co-founded Orange County Choppers (OCC) with his father, Paul Teutul Sr. in 1999.  Teutul was the chief designer and fabricator of OCC.  Prior to this, Teutul was head of the rail shop at Orange County Ironworks.  He was also responsible for designing the logo for OCC.  He is the owner of Paul Jr.  Designs, which manufactures custom motorcycles and sells branded clothing.

Orange County Choppers: Orange County Choppers (OCC) is a motorcycle manufacturer and lifestyle brand company based in the town of Newburgh, located in Orange County, New York, that was founded in 1999 by Paul Teutul Sr., and Paul Teutul Jr. The company was featured on "American Chopper", a reality TV show that debuted in September 2002 on the Discovery Channel.  The series moved to Discovery Channel's sister channel TLC in 2007.  Following cancellation of the Discovery series, the company was also featured on "Orange County Choppers" on the CMT network in 2013.

Question: What show did Paul Teutul Sr. star in before Orange County Choppers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose show appearances are being queried."
    },
    "earlier_show": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the show the person starred in earlier."
        },
        "debut_year": {
          "type": "integer",
          "description": "The year the earlier show debuted."
        }
      },
      "required": [
        "name",
        "debut_year"
      ],
      "additionalProperties": false
    },
    "later_show": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the show the person starred in later, used for comparison."
        },
        "debut_year": {
          "type": "integer",
          "description": "The year the later show debuted."
        }
      },
      "required": [
        "name",
        "debut_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "earlier_show",
    "later_show"
  ],
  "additionalProperties": false
}
