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
Flixborough: Flixborough is a village and civil parish in North Lincolnshire, England.  The population of the civil parish at the 2011 census was 1,664.  It is situated near to the River Trent, approximately 3 mi north-west from Scunthorpe.  The village is noted for the 1974 Flixborough disaster.

East Stockwith: East Stockwith is a village within the civil parish of East Stockwith, in the West Lindsey district of Lincolnshire, England.  It lies on the River Trent, 3 mi north-west of Gainsborough.  The River Trent Aegir, a tidal bore, reaches the village.  In 2001 it had a total resident population of 209, increasing to 314 at the 2011 census.

Langford, Nottinghamshire: Langford is a village and civil parish in Nottinghamshire, England.  It is located 4 miles north-east of Newark-on-Trent and two miles East from The River Trent.  Population details are included in the civil parish of Holme.  It is based on A1133 which comes off of the A46.  Although Langford is currently located two miles from The River Trent it has not always been this way.  In "1575 there was a cataclysmic flood" which altered the course of the Trent which meant Langford and Holme were now on the same side of the river.  Before this change in the rivers course the Trent used to flow next to St Bartholomew's church and Holme was on the opposite side of the bank.

Amcotts: Amcotts is a village and civil parish in the North Lincolnshire district of Lincolnshire, England, and on the Isle of Axholme.  The village is situated north-west from Scunthorpe, and on the west bank of the River Trent facing Flixborough on the east bank.  The 2001 Census recorded a population of 219 for the parish, increasing to 262 at the 2011 census.

Wilford: Wilford is a village close to the centre of the city of Nottingham, UK.  It is in the Clifton North Ward of Nottingham Unitary Authority.  The village is bounded to the north and west by the River Trent and to the east by the embankment of the now closed Great Central Railway.  The now demolished Wilford Power Station was located on the north bank of the River Trent.

The Meadows, Nottingham: The Meadows is an area of Nottingham, England located south of city centre, close to the River Trent and connected to West Bridgford in the Borough of Rushcliffe by Trent Bridge and the Wilford Suspension Bridge.  Victoria Embankment runs alongside the River Trent to the south of the Meadows and is home to the Nottingham War Memorial Gardens.

Torksey Castle: Torksey Castle is a manor house located in the centre of the village of Torksey on the east bank of the River Trent in Lincolnshire, England.  It is 12 miles northwest of Lincoln on the A156 road.  Seven miles to the north is Gainsborough Old Hall and 10 miles southeast is Lincoln Castle.  It is a 16th-century Tudor stone-built fortified manor house founded by the Jermyn family of Suffolk.  The building is on the Buildings at Risk Register.  The site is strictly private, with no public access and is only visible from the A156 road and a public footpath, on the west bank of the River Trent.

Derwent Mouth: Derwent Mouth is a location on the River Trent, which at that point forms the border between the English counties of Derbyshire and Leicestershire.  It is both the confluence of the River Derwent with the River Trent, and the point at which the Trent and Mersey Canal joins the natural River Trent.

Bole, Nottinghamshire: Bole is a village and civil parish in the Bassetlaw district of Nottinghamshire, England.  It is close by the River Trent, on the eastern side of which is Gainsborough in Lincolnshire.  At one time the village stood – like the neighbouring parish of West Burton – very near to an oxbow lake, known as Bole Round.  However flooding led to the original course of the River Trent being diverted after 1792.  The parish now lies within a landscape largely dominated by the West Burton power stations.  According to the 2001 census Bole had a population of 140, increasing to 247 at the 2011 Census.

Trent, Ancholme and Grimsby Railway: The Trent, Ancholme and Grimsby Railway was a railway line in north Lincolnshire which commenced at an end on junction with the South Yorkshire Railway where that railway crossed the River Trent near the village of Gunhouse.  This was known as Gunhouse Junction but the village has become known as "Gunness".  The line ran for about 14 miles (22.5 km) through Frodingham to Wrawby Junction near Barnetby and included railway stations at Appleby, and Elsham.  The line also included two branches to Gunness and Gunhouse Wharf on the River Trent.  The line was opened on 1 October 1866.

Question: Where is the village which River Trent face located 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "village_name": {
      "type": "string",
      "description": "The name of the village."
    },
    "location": {
      "type": "string",
      "description": "The administrative location of the village."
    },
    "river_bank_position": {
      "type": "string",
      "description": "The bank of the River Trent the village is located on."
    },
    "facing_entity": {
      "type": "string",
      "description": "The entity (e.g., another village) that the village faces across the river."
    }
  },
  "required": [
    "village_name",
    "location",
    "river_bank_position",
    "facing_entity"
  ],
  "additionalProperties": false
}
