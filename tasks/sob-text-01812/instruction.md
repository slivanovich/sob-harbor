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
Colt Crag Reservoir: Colt Crag Reservoir is a relatively shallow reservoir in Northumberland, England adjacent to the A68 road, and 9 mi north of Corbridge.  The A68 road at this point runs along the course of Dere Street, a Roman road.

Bremenium: Bremenium was an ancient Roman fort (castra) located at Rochester, Northumberland, England.  The fort was one of the defensive structures built along Dere Street, a Roman road running from York to Corbridge and onwards to Melrose.  Significantly the fort is a long way north of Hadrian's Wall.

Luguvalium: Luguvalium was a Roman town in northern Britain in antiquity.  It was located within present-day Carlisle, Cumbria, and may have been the capital of the 4th-century province of Valentia.

Little Swinburne Reservoir: Little Swinburne Reservoir is a small reservoir in Northumberland, England less than 1 mi northeast of the A68 road, and about 9 mi north of Corbridge.  The A68 road generally follows the course of Dere Street, a Roman road, but has deviated at this point a little to the east, to facilitate a bridge crossing of the Swin Burn.

Dere Street: Dere Street or Deere Street is a modern designation of a Roman road which ran north from Eboracum (York), crossing Stanegate at Corbridge (Hadrian's Wall was crossed at the Portgate, just to the north) and continuing beyond into what is now Scotland, later at least as far as the Antonine Wall.  Portions of its route are still followed by modern roads, including the A1 (south of the River Tees) and the A68 north of Corbridge.

Portgate: The Portgate was a fortified gateway, constructed as part of the Roman Hadrian's Wall (Dere Street preceded Hadrian's Wall by around 50 years).  It was built to control traffic along Dere Street as it passed through Hadrian's Wall.  Its remains exist beneath the old B6318 Military Road to the south-west of the Stagshaw Roundabout (the B6318 was diverted slightly for the construction of the Stagshaw Roundabout, leaving two short sections of the existing road unlinked - the remains of the Portgate are buried beneath the western section).

Stanegate: The Stanegate, or "stone road" (Old Norse), was an important Roman road built in what is now northern England.  It linked two forts that guarded important river crossings; Corstopitum (Corbridge) in the east, situated on Dere Street, and Luguvalium (Carlisle) in the west.  The Stanegate ran through the natural gap formed by the valleys of the Tyne and Irthing.  It predated Hadrian's Wall by several decades; the Wall would later follow a similar route, slightly to the north.

Coria (Corbridge): Coria was a fort and town 2.5 mi south of Hadrian's Wall, in the Roman province of Britannia at a point where a big Roman north–south road (Dere Street) bridged the River Tyne and met another Roman road (Stanegate), which ran east–west between Coria and Luguvalium (the modern Carlisle) in the Solway Plain.  The full Latin name is uncertain and it is known as Corchester or Corbridge Roman Site, adjoining Corbridge in the English county of Northumberland.  It is in the guardianship of English Heritage and is partially exposed as a visitor attraction, including a site museum.

Rochester, Northumberland: Rochester is a small village and civil parish in north Northumberland, England.  It is five miles north-west of Otterburn on the A68 road between Corbridge and Jedburgh.  The village is the site of the Roman fort of Bremenium, built there to protect the important Roman road of Dere Street, which passes through the village.

Habitancum: Habitancum was an ancient Roman fort (castra) located at Risingham, Northumberland, England.  The fort was one of the defensive structures built along Dere Street, a Roman road running from York to Corbridge and onwards to Melrose.

Question: The Stanegate, or "stone road" (Old Norse), was an important Roman road built in what is now northern England, it linked two forts that guarded important river crossings; Corstopitum (Corbridge) in the east, situated on Dere Street, and Luguvalium (Carlisle) in the west, Luguvalium was a Roman town in which northern location, in antiquity?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "roman_town_name": {
      "type": "string",
      "description": "The name of the Roman town."
    },
    "modern_location": {
      "type": "string",
      "description": "The present-day location of the Roman town."
    },
    "ancient_northern_location": {
      "type": "string",
      "description": "The ancient northern location where the Roman town was situated."
    },
    "linked_roman_road": {
      "type": "string",
      "description": "The Roman road that linked this town to another fort."
    },
    "linked_fort_east": {
      "type": "string",
      "description": "The name of the fort linked to the east by the Roman road."
    }
  },
  "required": [
    "roman_town_name",
    "modern_location",
    "ancient_northern_location",
    "linked_roman_road",
    "linked_fort_east"
  ],
  "additionalProperties": false
}
