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
Jamestown, Virginia: The Jamestown settlement in the Colony of Virginia was the first permanent English settlement in the Americas.  William Kelso writes that Jamestown "is where the British Empire began".  It was established by the Virginia Company of London as "James Fort" on May 4, 1607 (O.S.; May 14, 1607 N.S.), and was considered permanent after brief abandonment in 1610.  It followed several failed attempts, including the Lost Colony of Roanoke.  Jamestown served as the capital of the colony of Virginia for 83 years, from 1616 until 1699.

Bartholomew Gosnold: Bartholomew Gosnold (1571 – 22 August 1607) was an English lawyer, explorer, and privateer who was instrumental in founding the Virginia Company of London, and Jamestown in colonial America.  He led the first recorded European expedition to Cape Cod.  He is considered by Preservation Virginia (formerly known as the Association for the Preservation of Virginia Antiquities) to be the "prime mover of the colonization of Virginia".

Christopher Newport University: Christopher Newport University, or CNU, is a public liberal arts university located in Newport News, Virginia, United States.  CNU is the youngest comprehensive university in the commonwealth of Virginia.  The institution is named after Christopher Newport, who was a buccaneer (or privateer) and captain of the "Susan Constant", the largest of three ships which carried settlers for the Virginia Company in 1607, on their way to found Jamestown in the Virginia Colony, which became the first permanent English settlement in North America.

Susan Constant: Susan Constant, captained by Christopher Newport, was the largest of three ships of the English Virginia Company (the others being "Discovery" and "Godspeed") on the 1606 - 1607 voyage that resulted in the founding of Jamestown in the new Colony of Virginia.

Popham Colony: The Popham Colony—also known as the Sagadahoc Colony—was a short-lived English colonial settlement in North America that was founded in 1607 and located in the present-day town of Phippsburg, Maine, near the mouth of the Kennebec River by the proprietary Virginia Company of Plymouth.  It was founded a few months after its more successful rival, the colony at Jamestown, which was established on May 4, 1607, by the Virginia Company of London in present-day James City County, Virginia.

John Brereton: John Brereton ("ca."  1571/1572 – "ca."  1632) was a gentleman adventurer and chronicler of the 1602 voyage to the New World led by Bartholomew Gosnold.

Matthew Scrivener: Matthew Scrivener (1580 – January 7, 1609) was an English colonist in Virginia.  He served briefly as acting governor of Jamestown, when he was succeeded by Captain John Smith.  Scrivener drowned with eight other colonists, half of them members of the governing Council, including Bartholomew Gosnold's brother Anthony, while attempting to cross to nearby Hog Island in a storm in 1609.

Godspeed (ship): Godspeed, under Captain Bartholomew Gosnold, was one of the three ships (along with "Susan Constant" and "Discovery") on the 1606-1607 voyage to the New World for the English Virginia Company of London.  The journey resulted in the founding of Jamestown in the new Colony of Virginia.

Christopher Newport: Christopher Newport (1561–1617) was an English seaman and privateer.  He is best known as the captain of the "Susan Constant", the largest of three ships which carried settlers for the Virginia Company in 1607 on the way to found the settlement at Jamestown in the Virginia Colony, which became the first permanent English settlement in North America.  He was also in overall command of the other two ships on that initial voyage, in order of their size, the "Godspeed" and the "Discovery".

Discovery (1602 ship): Discovery or Discoverie was a small 20-ton, 38 foot (12 m) long "fly-boat" of the British East India Company, launched before 1602.  It was one of the three ships (along with "Susan Constant" and "Godspeed") on the 1606-1607 voyage to the New World for the English Virginia Company of London.  The journey resulted in the founding of Jamestown in the new Colony of Virginia.

Question: What gentleman adventurer and chronicled the 1602 voyage to the New World led by Bartholomew Gosnold (1571 – 22 August 1607) who was an English lawyer, explorer, and privateer who was instrumental in founding the Virginia Company of London, and Jamestown in colonial America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the gentleman adventurer and chronicler."
    },
    "person_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Roles held by the person."
    },
    "voyage_details": {
      "type": "object",
      "properties": {
        "voyage_year": {
          "type": "integer",
          "description": "The year the voyage took place."
        },
        "voyage_leader": {
          "type": "object",
          "properties": {
            "leader_name": {
              "type": "string",
              "description": "The name of the leader of the voyage."
            },
            "leader_roles": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Roles held by the voyage leader."
            },
            "leader_founding_involvements": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Entities the leader was instrumental in founding."
            }
          },
          "required": [
            "leader_name",
            "leader_roles",
            "leader_founding_involvements"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "voyage_year",
        "voyage_leader"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "person_roles",
    "voyage_details"
  ],
  "additionalProperties": false
}
