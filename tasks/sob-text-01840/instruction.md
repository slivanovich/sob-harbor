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
Backford Cross: Backford Cross is a village on the Wirral Peninsula, Cheshire, England.  It is a suburb of the town of Ellesmere Port and part of Cheshire West and Chester.  Backford Cross is located around the A41/A5117 junction, south of Great Sutton and about 1.5 mi north of the village of Backford, near Chester.  Backford Cross is largely made up of residential homes built from 1990 onwards and serves as a commuter village to Ellesmere Port and Chester, although inhabitants show no allegiance to either locality.  The area is split between postcode districts, with parts of the village in Great Sutton, Ellesmere Port CH66 and other areas in Backford, Chester CH1.

A5117 road: The A5117 is a road in Cheshire, England.  It runs between Shotwick ( ) and Helsby ( ) and connects the A550 at Woodbank to the M56.  As such it forms a northerly bypass to Chester and a shorter route between the North West and North Wales than the A55.  The road is dualled west of the M56.  There is roundabout with the A540 and at Dunkirk at the western terminus of the M56.  East of the junction the road is single carriageway and crosses the A41 by way of a roundabout at Backford Cross.  The A5117 intersects the M53 at Junction 10.  This junction is just east of Cheshire Oaks Designer Outlet.  The road then continues almost parallel to the M56, which it intersects at Junction 14, at which there is a Motorway service area.  The road then continues south east to terminate where it joins the A56 at Helsby.

Grand Junction Road: Grand Junction Road is the longest east–west thoroughfare in the Adelaide metropolitan area, and is located approximately 9 kilometres north of the city centre.  Travelling from the Port Adelaide region, it is mostly a double-lane sealed road (becoming a single-lane road past Tolley Road intersection at Hope Valley, South Australia) running 21 kilometres to the base of the Adelaide Hills.  The western terminus is at the intersection of Old Port Road, 300 metres east of a causeway, which separates the Port River from West Lakes.  The 2.4 kilometre section of road that continues west of Old Port Road to Semaphore South is named Bower Road.  The eastern terminus of Grand Junction Road is in the suburb of Hope Valley, at the intersection of Hancock Road and Lower North East Road, just before the latter proceeds into the Adelaide Hills, past Anstey Hill Recreation Park and on towards the towns of Houghton and Inglewood.

A227 road: The A227 road in England runs from Gravesend in Kent in a generally south-south-westerly direction to Tonbridge.  It is about 19.9 mi in length.

Cheshire Oaks Designer Outlet: Cheshire Oaks Designer Outlet is an outlet centre in Ellesmere Port, Cheshire, England.

Listed buildings in Thornton-le-Moors: Thornton-le-Moors is a civil parish in Cheshire West and Chester, England.  It contains nine buildings recorded in the National Heritage List for England as designated listed buildings. Of these, one is listed at Grade I, the highest of the three grades, and the others are at Grade II, the lowest grade.  Apart from the village of Thornton-le-Moors, the parish is rural, other than the area north of the A5117 road, which is occupied by an oil refinery.  The listed buildings consist of the village church and associated structures, houses, farmhouses, and farm buildings.

Mollington, Cheshire: Mollington is a small village and civil parish in the unitary authority of Cheshire West and Chester and the ceremonial county of Cheshire, England, It is located two miles north of the city of Chester, with approximate boundaries formed by the A41 Liverpool-Chester trunk road and Shropshire Union Canal to the east and southeast, the A540 Wirral Peninsula trunk road (Parkgate Rd) to the south and west and the A5117 Dunkirk link road to the north.  According to the 2001 census, the village has a population of 663, reducing to 626 at the 2011 Census.

Hapsford: Hapsford is a village and civil parish in the unitary authority of Cheshire West and Chester and the ceremonial county of Cheshire, England.  It is located on the A5117 road, with Helsby to the east and the village of Elton, near Ellesmere Port, to the north west.  Junction 14 of the M56 motorway and Chester services motorway service station are sited nearby.

Tarvin in the English Civil War: During the first English Civil War, Tarvin, a village in Cheshire England was garrisoned by both sides and was attacked by both sides, because its proximity to Chester which was a major Royalist (Cavalier) port city, made it strategically important.  Tarvin changed hands several times; initially it was garrisoned by Parliament and troops of both sides at different times were quartered in and around the village, which was not fortified.  In September 1644 the Parliamentarians (Roundheads) fortified the village and garrisoned the place with sufficient troops to withstand a large attack and it remained in their hands until the end of the war.

Enola Branch: The Enola Branch is a railroad segment of the Port Road Branch and it was a rail line; the Enola Branch railroad segment and the rest of the Port Road Branch is owned and operated by the Norfolk Southern Railway in the U.S. state of Pennsylvania.  The railroad segment runs from Washington Boro northwest to Marysville and it is a former Pennsylvania Railroad rail line.  Its south end is at a former junction with the Atglen and Susquehanna Branch, where the main segment of the Port Road Branch continues southeast.  Its north end is at the Pittsburgh Line.  Along the way, it meets the York Secondary at Wago Junction (near York Haven) and goes under the Lurgan Branch at Lemoyne.  Norfolk Southern labels the Enola Branch as part of the Port Road Branch, officially ending the Enola Branch's existence as a rail line, the main segment of the Port Road Branch runs from Marysville, Pennsylvania south to Perryville, Maryland.  The line goes through the Enola Yard.

Question: A5117 road of Cheshire England runs just east of with Ellesmore Port outlet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "road_name": {
      "type": "string",
      "description": "The name of the road in question."
    },
    "outlet_name": {
      "type": "string",
      "description": "The name of the designer outlet."
    },
    "outlet_town": {
      "type": "string",
      "description": "The town where the outlet is located."
    },
    "outlet_county": {
      "type": "string",
      "description": "The county where the outlet is located."
    },
    "relative_position_of_outlet_to_road": {
      "type": "string",
      "description": "The directional position of the outlet relative to the road."
    }
  },
  "required": [
    "road_name",
    "outlet_name",
    "outlet_town",
    "outlet_county",
    "relative_position_of_outlet_to_road"
  ],
  "additionalProperties": false
}
