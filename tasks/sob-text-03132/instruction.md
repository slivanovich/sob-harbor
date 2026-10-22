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
Rosedale Center: Rosedale Center, commonly known just as Rosedale, is a shopping center in Roseville, Minnesota.  The mall is considered a regional powerhouse as a shopping destination; surrounded by suburbs and close to major highways, it serves a trade area population almost 2 million people, and boasts 12 million visitors a year.

National Parks of New York Harbor: National Parks of New York Harbor is the name of an office of the National Park Service that coordinates administration of eleven NPS sites that include 23 unique destinations located in the New York metropolitan area.  National Parks of New York Harbor was formed in 2003 and administers properties ranging from the Statue of Liberty National Monument in New York Harbor to Gateway National Recreation Area in several locations and Saint Paul's Church National Historic Site in Mount Vernon, New York.  Despite its name, technically the office does not oversee any national parks, but rather national monuments, national memorials, national historic sites, and a large national recreation area.  Properties overseen by the office make up 27000 acre and attract more than 12 million visitors each year.  They are served by a visitor's center at Federal Hall National Memorial.

A Line (Minnesota): The A Line, previously known as the Snelling Avenue Bus Rapid Transitway, is a bus rapid transit line in Twin Cities in Minnesota operated by Metro Transit.  The A Line operates on the Snelling Avenue corridor, connecting to the Blue and Green light rail lines, as well as serving Hamline University, Macalester College, Highland Village, Rosedale Center, Har Mar Mall, Minnehaha Park and the Midway area.

Tourism in Chicago: In 2016, Chicago, Illinois set a visitation record of 54.1 million visitors; a 2.9 percent increase from 2015.  The prior record, set just the year before in 2015, estimated 50.1 million visitors, which was a 4.5 percent increase from 2014.  From 2010 through 2014, the tourism and hospitality industries have added 9,800 jobs, generating $13.7 billion in direct spending by visitors and $871 million in total tax revenue.

Tourism in Puerto Rico: Tourism in Puerto Rico attracted 4.2 million visitors in 2013 and 4 million visitors in 2011, a notable increase over 2010 at 3.68 million, tourism has been a money revenue industry for Puerto Rico for a number of decades given it is host to diverse natural wonders, cultural and historical buildings, concerts and sporting events.  The fact that visitors from the United States do not need a passport to enter Puerto Rico attracts a large number of tourists from the mainland United States each year.  Other groups of tourists that visit Puerto Rico in significant numbers include French, German, Spaniards, Canadians, Mexicans, Venezuelan, Brazilians and Asian tourists.

Mall of Abilene: Mall of Abilene is an enclosed shopping mall in Abilene, Texas.  It is located in the growing south side of the city, at the southwest corner of the busiest intersection in Abilene at Buffalo Gap Road and US 83/84 (Winters Freeway).  It serves a 22-county trade area.  Six stores anchor the mall JCPenney, Dillard's, Sears, Best Buy, Ulta, and Books-A-Million.  The mall also houses the 15000 sqft Premiere Cinema 10.  The mall's gross leasable area of nearly 1000000 sqft consists of a total of 80 stores, excluding the theater, 7 of which have a leasable area of at least 56000 sqft .  It also boasts an annual foot traffic of 19.2 million visitors.

Dubai World Central: Dubai World Central Name changed to the Dubai South Free Zone is the development currently under construction in Dubai, United Arab Emirates.  It will be an economic zone to support a number of activities including logistics, aviation, commercial, exhibition, humanitarian, residential and other related businesses around Al Maktoum International Airport with the planned annual capacity of 12 million tonnes of cargo and 160 million passengers.  The construction area is 140 square kilometres, almost two times the size of Hong Kong Island.  The location is estimated to be the future home of 900,000 people.  The Dubai World Central combined with the Al Maktoum International Airport is expected to draw additional tourism to the Middle East, designed to handle 20 million visitors a year by 2020.  The development has been designed on the basis of three key factors: Dubai's geographic location, increasing importance of airports in the Middle East region, and the region's booming aviation sector.  The Dubai International Central functions as the central hub for the MENASA market, serving nearly one quarter of the world's population and doing 3.6 trillion USD in business in the year 2009.

Mahamaham tank, Kumbakonam: Mahamaham Tank is a huge temple tank located in Kumbakonam, Tamil Nadu, India.  It is considered to be the foremost and one of the largest temple tanks in Tamil Nadu.  The Masimaham festival held in the tank has 0.1 million visitors and the 12 year Mahamaham festival has close to 2 million visitors.

Tourist attractions in Vienna: The tourist attractions of Vienna concentrate in three distinct areas.  The largest cluster, centred on Schönbrunn Palace, attracted around five million visitors in 2009, down from six million in 2008.  Museums and exhibitions of Hofburg Palace accounted for nearly two million visitors in 2008, with a significant decline in 2009.  The third, and the newest, cluster of modern art museums in Museumsquartier attracted less than one million visitors.  Nearby duo of Kunsthistorisches and Naturhistorisches museums, located halfway between Museumsquartier and Hofburg, also reported around one million visitors.  The Landstraße district, which lies south-east of the old city, is home to art exhibitions at the Belvedere Palace and the KunstHausWien.

Palisades Center: The Palisades Center Mall, often referred to as the Palisades Mall, in West Nyack, New York is the second-largest shopping mall in the New York metropolitan area, the eighth-largest in the United States by total area, and sixth-largest by gross leasable space.  Built in the industrial style, the mall houses more than 200 stores and receives 20 million visitors a year.  It is also one of the nation's most lucrative malls, producing $40 million in annual sales tax and $17 million in property taxes.

Question: Which mall that A Line serves has 12 million visitors a year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "mall_name": {
      "type": "string",
      "description": "The name of the shopping mall."
    },
    "annual_visitors": {
      "type": "integer",
      "description": "The number of visitors the mall receives annually."
    },
    "served_by_a_line": {
      "type": "boolean",
      "description": "Indicates if the mall is served by the A Line."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the mall is located."
        },
        "state": {
          "type": "string",
          "description": "The state where the mall is located."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "mall_name",
    "annual_visitors",
    "served_by_a_line",
    "location"
  ],
  "additionalProperties": false
}
