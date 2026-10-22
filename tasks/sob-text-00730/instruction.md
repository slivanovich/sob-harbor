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
Kingsland Road: Kingsland Road is the name of a road, part of the A10, in the London Borough of Hackney in England.  It runs from the junction with Old Street and Hackney Road (the section of the A10 south of this is Shoreditch High Street) north to the junction with Balls Pond Road and Dalston Lane, where it changes its name to Kingsland High Street.  Kingsland Road means the road "to" Kingsland, an old settlement that has been absorbed by modern Dalston.  It is one of the oldest roads in England and is thought to follow the route of the Roman Ermine Street, later known as the Old North Road.

A1260 road: The A1260 is a major road that serves the city of Peterborough in Eastern England.  The road is dual-carriageway from its southern terminus with the A15 at Hampton to its northern terminus with the A47 at Longthorpe.  The road is also known as the "Nene Parkway" and serves as major route from getting from the southern end of Peterborough to the Northern end without having to travel into to the centre of the city via the A15.  The road itself starts at Hampton at a small roundabout with the A15 where after it goes past Serpentine Green at another roundabout before it very quickly heads to a major junction where its meets the A1139.  After that junction the road takes on the form of a major dual-carriageway with its own grade separated junctions where it meets the A605 on a restricted junction before passing over the River Nene before meeting the A1179 on another junction.  After that junction the road quickly heads north before coming to a major junction with the A47 where the road terminates on a large roundabout with the A47 passing over on top.

Shoreditch High Street: Shoreditch High Street is the old main street of Shoreditch, London.  It is part of the A10 road and connects Norton Folgate to the south with Kingsland Road to the north.  It constitutes a segment of the Roman Ermine Street, which ran directly north from London to Lincoln and York.  The parish church of St Leonard's, Shoreditch is situated at the north-east end of the road at the crossroads where it meets with Hackney Road.  This part of the road is wholly within the London Borough of Hackney; below Boundary Street, the eastern side lies within the London Borough of Tower Hamlets.  The high street enters the City of London at Norton Folgate.

Crown Point Road: The Crown Point Road, or the Crown Point Military Road, is a historic road built in 1759-60, mostly in what is now the United States state of Vermont.  It was built by British Army and colonial militia forces to connect Fort Crown Point near the southern end of Lake Champlain to the Fort at Number 4 in what is now Charlestown, New Hampshire.  It was the first major road in Vermont, spurring development along its route after the French and Indian War.  Fragments of the road are still visible in largely period condition, or have been paved over, while others have disappeared into the forest.  Sections of the road located in Weathersfield have been listed on the National Register of Historic Places.

A19 road: The A19 is a major road in England running approximately parallel to and east of the A1 road, although the two roads meet at the northern end of the A19, the two roads originally met at the southern end of the A19 in Doncaster but the old route of the A1 was changed to the A638.  From Sunderland northwards, the route was formerly the A108.  In the past the route was known as the East of Snaith-York-Thirsk-Stockton-on-Tees-Sunderland Trunk Road.  Most traffic joins the A19, heading for Teesside, from the A168 at Dishforth Interchange.  The road also inspired a song called A19 by the North East band Maximo Park

Turf War (Banksy): "Turf War" was the first major exhibition by artist Banksy, staged in a warehouse on Kingsland Road in London's East End.  Artnet said the exhibition was "one of England's best -- and briefest" of the season.

Haggerston railway station: Haggerston is a station on the East London Line and connecting South London Line in Haggerston within the London Borough of Hackney, Greater London.  The station is located on the Kingsland Viaduct at the junction of Arbutus Street and Frederick Terrace, near Kingsland Road.  The main entrance is in Lee Street.  The station was built as part of the East London Line extension served by National Rail London Overground under the control of the London Rail division of Transport for London, however there is no standard red National Rail "double arrow" logo signage located at the station, instead only the Overground roundel.  The next station north is Dalston Junction and the next station south is Hoxton .  It is in Travelcard Zone 2.

A10 road (England): The A10 (in certain sections known as "Great Cambridge Road" or Old North Road) is a major road in England.  Its southern end is at London Bridge in the London Borough of Southwark, and its northern end is the Norfolk port town of King's Lynn.  From London to Royston it chiefly follows the line of Roman Ermine Street.

Thane–Belapur Road: Thane–Belapur road is a major road in the Mumbai Metropolitan Region connecting the city of Thane with Navi Mumbai.  The southern end of Thane–Belapur road starts at the Sion Panvel Highway near Turbhe.  The road passes through a busy Thane – Belapur region and generally runs in north-south direction.  During the stretch between Turbhe and Dighe, Thane–Belapur road runs completely parallel to the Trans-Harbour Line of Mumbai Suburban Railway and the stations of Airoli, Rabale, Ghansoli, Kopar Khairane and Turbhe all have direct access from this road.

Metropolitan Free Hospital: The Metropolitan Free Hospital was a London hospital, founded in 1836 and based for most of its existence in Kingsland Road, Hackney.  It became part of the NHS in 1948, and closed in 1977, with its residual functions transferring to Barts Hospital.

Question:  Kingsland Road is part of a major road that has it's southern end at which bridge ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "main_road_name": {
      "type": "string",
      "description": "The name of the road in question."
    },
    "part_of_major_road": {
      "type": "string",
      "description": "The identifier of the major road that the main road is a part of."
    },
    "major_road_terminus": {
      "type": "object",
      "properties": {
        "end_type": {
          "type": "string",
          "description": "The type of the terminus (e.g., bridge, town)."
        },
        "name": {
          "type": "string",
          "description": "The name of the terminus."
        },
        "location_borough": {
          "type": "string",
          "description": "The London Borough where the terminus is located."
        }
      },
      "required": [
        "end_type",
        "name",
        "location_borough"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "main_road_name",
    "part_of_major_road",
    "major_road_terminus"
  ],
  "additionalProperties": false
}
