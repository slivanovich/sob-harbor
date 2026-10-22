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
Twizell Castle: Twizell Castle (also spelt Twizel) is a Grade II* listed building and a Scheduled Ancient Monument which stands on a bend of the River Till at Tillmouth Park, Northumberland, northern England.  Below it, the medieval Twizell bridge spans the river.  It is located 10 mi south-west of Berwick Upon Tweed.  The site is visible from a public footpath, which passes the castle from the road.  The gardens of the castle contain the earthwork remains of the once lost medieval village of Twizell, whilst the massive ruin presents the remains of an 18th-century castle which was never completed.

Yealand Redmayne: Yealand Redmayne is a village and civil parish in the English county of Lancashire.

Listed buildings in Yealand Conyers: Yealand Conyers is a civil parish in Lancaster, Lancashire, England.  It contains 28 buildings that are recorded in the National Heritage List for England as designated listed buildings. Of these, two are at Grade II*, the middle grade, and the others are at Grade II, the lowest grade.  The parish contains the village of Yealand Conyers, and is otherwise rural.  Most of the listed buildings are houses within the village.  The other listed buildings include a country house, two churches, and a Quaker Meeting House.  The Lancaster Canal passes through the edge of he parish, and a bridge crossing it is listed.

Grand Western Canal: The Grand Western Canal ran between Taunton in Somerset and Tiverton in Devon in the United Kingdom.  The canal had its origins in various plans, going back to 1796, to link the Bristol Channel and the English Channel by a canal, bypassing Lands End.  An additional purpose of the canal was the supply of limestone and coal to lime kilns along with the removal of the resulting quicklime, which was used as a fertiliser and for building houses.  This intended canal-link was never completed as planned, as the coming of the railways removed the need for its existence.

Jonglei Canal: The Jonglei Canal is a canal project that has been proposed, started but never completed to divert water through the vast Sudd wetlands of South Sudan so as to deliver more water downstream to Sudan and Egypt for use in agriculture.

South Dakota-class battleship (1920): The first "South Dakota" class was a class of six American battleships that were laid down in 1920 but never completed.  They would have been the last dreadnoughts in the Naval Act of 1916 to be commissioned had the Washington Naval Treaty not caused their cancellation one-third of the way through their construction.  They would have been the largest, most heavily armed and armored battleships in the U.S. Navy and, designed to achieve 23 kn , represented an attempt to abandon its 21 kn standardized fleet speed and catch up with the increasing fleet speeds of its main rivals, the British Royal Navy and Imperial Japanese Navy.  In this, size and secondary armament, they represented a break from the Standard-type battleship that had dominated American capital ship design for the prior five ship classes, while their use of standardized bridges, lattice masts and other features was a continuation of this practice and the increase in the number of main guns from the preceding "Colorado" class had long been standard U.S. naval policy.  The main restriction to which they had to adhere was the ability to pass through the Panama Canal.

Listed buildings in Yealand Redmayne: Yealand Redmayne is a civil parish in Lancaster, Lancashire, England.  It contains 15 buildings that are recorded in the National Heritage List for England as designated listed buildings. Of these, one is at Grade II*, the middle grade, and the others are at Grade II, the lowest grade.  The parish contains the village of Yealand Redmayne, and is otherwise rural.  Most of the listed buildings are houses, farmhouses and farm buildings, many of them on the main street of the village.  The Lancaster Canal passes through the parish, and two bridges crossing it are listed, together with a milestone on its towpath.

Ellesmere Canal: The Ellesmere Canal was a waterway in England and Wales that was planned to carry boat traffic between the Mersey and Severn rivers.  The proposal would create a link between the Port of Liverpool and the mineral industries in north east Wales and the manufacturing centres in the West Midlands.  However, the canal was never completed as intended because of its rising costs and failure to generate the expected commercial traffic.

Lancaster Canal: The Lancaster Canal is a canal in North West England, originally planned to run from Westhoughton in Lancashire to Kendal in south Cumbria (then in Westmorland).  The section around the crossing of the River Ribble was never completed, and much of the southern end leased to the Leeds and Liverpool Canal, of which it is now generally considered part.

Glasgow, Paisley and Johnstone Canal: The Glasgow, Paisley and Ardrossan Canal, later known as the Glasgow, Paisley and Johnstone Canal, was a canal in the west of Scotland, running between Glasgow, Paisley and Johnstone which later became a railway.  Despite the name, the canal was never completed down to Ardrossan, the termini being Port Eglinton in Glasgow and Thorn Brae in Johnstone.  Within months of opening, the canal was the scene of a major disaster.

Question: What section of the canal that passes through Yealand Redmayne was never completed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "canal_name": {
      "type": "string",
      "description": "The name of the canal."
    },
    "location_passed_through": {
      "type": "string",
      "description": "The specific location mentioned in the question that the canal passes through."
    },
    "uncompleted_section": {
      "type": "string",
      "description": "The description of the section of the canal that was never completed."
    }
  },
  "required": [
    "canal_name",
    "location_passed_through",
    "uncompleted_section"
  ],
  "additionalProperties": false
}
