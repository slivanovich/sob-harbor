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
Nathan Boone: Nathan Boone (1780–1857) was a veteran of the War of 1812, a delegate to the Missouri constitutional convention in 1820, and a captain in the 1st United States Regiment of Dragoons at the time of its founding, eventually rising to the rank of lieutenant colonel.  Nathan was the youngest son of Daniel Boone.

Fort Cap au Gris: Fort Cap au Gris, also called Capo Gray, was a temporary fort built in September 1814 near Troy, Missouri during the War of 1812 by Missouri Rangers under the direction of Nathan Boone, son of Daniel Boone.  After the defeat of Fort Johnson, U.S. Army soldiers under the command of Zachary Taylor retreated to Cap au Gris in October 1814.

Nathan Boone Homestead State Historic Site: Nathan Boone Homestead State Historic Site is located in southwest Missouri, United States, near Ash Grove.  The site was established in 1991 to preserve Nathan Boone's home.  Nathan was the youngest child of Daniel Boone.  The site offers an interpretive trail plus tours of the home and cemetery.

Mealy machine: In the theory of computation, a Mealy machine is a finite-state machine whose output values are determined both by its current state and the current inputs.  (This is in contrast to a Moore machine, whose output values are determined solely by its current state.)

Boonslick Bridge: The Boonslick Bridge is a series of girder bridges on U.S. Route 40, Route 5, and Route 87 across the Missouri River between Cooper County, Missouri and Howard County, Missouri at Boonville, Missouri.  It is named for Nathan Boone (rather than his father Daniel Boone which is popularly reported), who built a road between St. Louis, Missouri and a salt lick northwest of the bridge, which was the first departure location on the Santa Fe Trail.

Excitation table: In electronics design, an excitation table shows the minimum inputs that are necessary to generate a particular next state (in other words, to "excite" it to the next state) when the current state is known.  They are similar to truth tables and state tables, but rearrange the data so that the current state and next state are next to each other on the left-hand side of the table, and the inputs needed to make that state change happen are shown on the right side of the table.

Daniel Boone Home: The Daniel Boone Home is a historic site in Defiance, Missouri, United States.  The house was built by Daniel Boone's youngest son Nathan Boone, who lived there with his family until they moved further south in 1837.  The Boones had moved there from Kentucky in late 1799.  Nathan later said, "In the summer of 1800, I erected a good substantial log house, and several years after that I replaced it with a commodious stone building.  My father, Daniel Boone, built himself a shop and had a set of tools, and when at home he would make and repair traps and guns.  In fact he did all the needed smith work for the family and sometimes for neighbors to oblige them.  But after a few years he disposed of his tools.”  Daniel and his wife Rebecca lived primarily with their son Nathan from at least 1804 to 1813, and then for much of the time from late 1816 to his death in 1820.

Jourian: Jourian Town was established by Sh Mustafa Khan, Jagirdhar of RakhDhok which is approximately 5 to 6 km north of Jourian.  The Jagirdhar had their land limit up to Jourian which is north side of mighty River Chenab is plain and fertile as compare to Rakhdhok which is Kandi Area and less fertile.  In 1903, the north Punjab was engulfed with the havoc of plague and it also effected adjoining areas.  It was in the end of Apr /Beginning of May 1903 when there was a big rain falls with hailstorms (Aan)which destroyed the wheat crops resulting the rats died insides the huts/kacha houses with the results plague spread.  The GrandMother of Sh Mustafa Khan came to Jourian where they have already a temporary (Kula) Shelter in order to avoid havoc of plague.  The temporary shelter came into permanent shelter as the land of Jourian was more fertile and near the River, so there was no scarcity of water.  Sh Mustafa Khan constructed the pucca Well few feet east of Masjid near to his house and decided to live at Jourian.  That was the beginning of a town which is called Jourian.  Later, when it was felt by young Sh Mustafa Khan to create the Jourian a Town.  He called Shri Nand Shah(Father of Bhagwan Shah),Father of Munshi Shah,Roulu Shah (father of Krishan Shah, Ganesh,Rama,Kaindu and Rattan) from Kaleeth to settle at Jourian and start business.  Shri Nand Shah was the friend of Sh Mustafa Khan.  Sh Nandu Bhagat, Lambardar who also belongs from Rakhdhok shifted to Jourian on the request of Sh Mustafa Khan.  It is very interesting that our Patwar is Rakhdhok though Patwari office is in Jourian.  Sh Moti Bhagat Father of Sh Shatu Ram, Sh Sangaru, Sh Guran Ditta and Sh Khikru called from Ajjal Mallal.  Sh Nanku Bhagat Father of Sh Kartar Chand also from Panjigrain was called to settle at Jourian.  Sh Manna Ram Chamar father of Munshi Ram from Potha which is hardly less than 2 km was also called to settle at Jourian.  Sh Ishwar Dass and Badri Nath called from Setrial.  Sh Nanku Mahajan Father of Sh Banarsi and Birta Ram also called from Potha.  Sh Billo and Basanata Lohar were called from Chamb.  Some Banias which are still called Bakoria came from Bakore.  In addition to this Nandu Barawala also called from Gher.  Jourian town and a notified area committee in Jammu district in the Indian state of Jammu and Kashmir.

State transition table: In automata theory and sequential logic, a state transition table is a table showing what state (or states in the case of a nondeterministic finite automaton) a finite semiautomaton or finite state machine will move to, based on the current state and other inputs.  A "state table" is essentially a truth table in which some of the inputs are the current state, and the outputs include the next state, along with other outputs.

Daniel Boone: Daniel Boone (November 2, 1734 [O.S. October 22] September 26, 1820) was an American pioneer, explorer, woodsman, and frontiersman, whose frontier exploits made him one of the first folk heroes of the United States.  Boone is most famous for his exploration and settlement of what is now Kentucky, which was then part of Virginia but on the other side of the mountains from the settled areas.  As a young adult, Boone supplemented his farm income by hunting and trapping game, and selling their pelts in the fur market.  Through this occupational interest, Boone first learned the easy routes to the area.  Despite some resistance from American Indian tribes such as the Shawnee, in 1775, Boone blazed his Wilderness Road through the Cumberland Gap in the Appalachian Mountains from North Carolina and Tennessee into Kentucky.  There, he founded the village of Boonesborough, Kentucky, one of the first American settlements west of the Appalachians.  Before the end of the 18th century, more than 200,000 Americans migrated to Kentucky/Virginia by following the route marked by Boone.

Question: What current state did the father of Nathan Boone settle?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who settled the location."
        },
        "relationship_to_nathan_boone": {
          "type": "string",
          "description": "The relationship of the person to Nathan Boone."
        }
      },
      "required": [
        "name",
        "relationship_to_nathan_boone"
      ],
      "additionalProperties": false
    },
    "settlement_details": {
      "type": "object",
      "properties": {
        "current_state": {
          "type": "string",
          "description": "The current state where the person settled."
        },
        "original_territory_status": {
          "type": "string",
          "description": "The status of the territory at the time of settlement."
        },
        "specific_settlement_name": {
          "type": "string",
          "description": "The name of the specific village or settlement founded."
        }
      },
      "required": [
        "current_state",
        "original_territory_status",
        "specific_settlement_name"
      ],
      "additionalProperties": false
    },
    "reasoning_source": {
      "type": "string",
      "description": "The context section from which the information was extracted."
    }
  },
  "required": [
    "person_of_interest",
    "settlement_details",
    "reasoning_source"
  ],
  "additionalProperties": false
}
