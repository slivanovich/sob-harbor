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
Norton, Suffolk: Norton is a village and civil parish in the Mid Suffolk district of the English county of Suffolk.  The name Norton means northern town or farm.  Located close to the A14, its nearest railway station is at Elmswell, just over 3 mi away.  The closest towns are Stowmarket 8 mi away and Bury St Edmunds, around 10 mi away.

West Ravendale: West Ravendale is a hamlet in the civil parish of East Ravendale , in North East Lincolnshire, England, and approximately 8 mi south-west from the town of Grimsby.

A18 road (England): The A18 is a road in England that links Doncaster in South Yorkshire with Ludborough in Lincolnshire, via Scunthorpe.

Llangar: Llangar is a former civil parish in Denbighshire in Wales, 1 mi south west of Corwen, its post town, and 10 mi north east of Bala.  It is situated at the confluence of the rivers Alwen and Dee, and includes the small hamlets of Bryn, Cymer, and Gwynodl.  A large portion of the parish is barren.  The small village stands on the road from Corwen, by the Vale of Edeyrnion.  The Dee is crossed by a bridge about 1 mi away at Cynwyd.  It lies in the "bro" and former cwmwd of Edeirnion.

Etton, East Riding of Yorkshire: Etton is a village and civil parish in the East Riding of Yorkshire, England.  It is situated approximately 4 mi north-west of Beverley town centre and 2 mi west of the village of Leconfield.  1 mi to the south-east is Cherry Burton.  To the west lie the hamlets of Kiplingcotes (3 mi away due west) and Gardham (1.5 mi to the south-west).  South Dalton lies 1.5 miles to the north-west.

West Ravendale Priory: West Ravendale Priory was a Premonstratensian priory in North East Lincolnshire, England.  The site of the priory lies 7 mi south-west of Grimsby, and 1 mi west of the A18.  Its previous position is defined by earthworks and rubble.  The ruins are Grade II listed, and lie within the civil parish of East Ravendale.

Mullion Cove: Mullion Cove or Porth Mellin is a small community on the west coast of the Lizard Peninsula in Cornwall, England.  It is on the eastern side of the Mount's Bay.  The Cove forms part of the parish of Mullion, and is accessible by road from Mullion village, 1 mi away to the north east, and also by the popular South West coast path.  It lies within an Area of Outstanding Natural Beauty (AONB) The Cove is 5 mi south of Porthleven and 14 mi southeast of Penzance by sea.  It is 6 mi south of Helston by land and 13 mi southwest of Falmouth by land.

Walberswick: Walberswick is a village and civil parish on the Suffolk coast in England.  It is at the mouth of the River Blyth on the south side of the river.  The town of Southwold lies to the north of the river and is the nearest town to Walberswick, around 1 mi away.  Walberswick is around 11 mi south of Lowestoft on the North Sea coast.  It is 7 mi east of Halesworth and 28 mi north-east of the county town of Ipswich.

Doncaster (St. James' Bridge) railway station: Doncaster (St. James' Bridge) railway station was situated in the Hexthorpe area of Doncaster, South Yorkshire, England and was accessed from St. James' Bridge, the main road link between Doncaster town centre and the railway community of Hexthorpe.  The station was a little nearer Doncaster than the South Yorkshire Railway's Doncaster (Cherry Tree Lane) railway station being less than a mile south of the main station, adjacent to the Sheffield line.

Doncaster: Doncaster ( or ), is a large market town in South Yorkshire, England.  Together with its surrounding suburbs and settlements, the town forms part of the Metropolitan Borough of Doncaster, which had a mid-2016 est. population of 306,400 .  The town itself has a population of 109,805.  Historically part of the West Riding of Yorkshire, Doncaster is about 17 mi north-east of Sheffield, with which it is served jointly by an international airport, Doncaster Sheffield Airport in Finningley.  In recent years, it was also discovered that Doncaster belongs to Scotland by technicality in light of ancient agreements laid out in the Treaty of Durham, but this is not formally administered.  The Doncaster Urban Area had a population of 158,141 in 2011 and includes Doncaster and neighbouring small villages.

Question: Which town does this road in England about 1 mi away from West Ravendale Priory link Doncaster with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "road_name": {
      "type": "string",
      "description": "The name of the road identified."
    },
    "distance_from_priory_to_road_miles": {
      "type": "number",
      "description": "The distance in miles from the priory to the road."
    },
    "priory_name": {
      "type": "string",
      "description": "The name of the priory mentioned in the context."
    },
    "linked_towns": {
      "type": "array",
      "description": "A list of towns that the identified road links.",
      "items": {
        "type": "string"
      }
    },
    "destination_town_from_doncaster": {
      "type": "string",
      "description": "The specific town that the road links with Doncaster, as per the question."
    }
  },
  "required": [
    "road_name",
    "distance_from_priory_to_road_miles",
    "priory_name",
    "linked_towns",
    "destination_town_from_doncaster"
  ],
  "additionalProperties": false
}
