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
Clarence Park (St Albans): Clarence Park is a Victorian park used for sports and leisure in St Albans, England.  It is still largely in its original form and has a rich variety of trees and planting.  It is close to St Albans City railway station.

Hatfield and St Albans Railway: The Hatfield & St Albans Railway was a branch of the Great Northern Railway which connected the Hertfordshire towns of St Albans and Hatfield.  It opened in 1865 with the principal aim of allowing St Albans traffic to access the Great Northern's main line to London at , but soon came into difficulties when the Midland Railway inaugurated a direct route to London through St Albans.  Passenger receipts declined in the 1930s, resulting in the temporary withdrawal of services in 1939.  Passenger services were permanently withdrawn in 1951, leaving goods traffic to linger on until December 1968.  Much of the route of the line is now incorporated into the Alban Way, a footpath and cycleway.

Brighton main line: The Brighton Main Line (also known as the South Central Main Line) is a divided in the north into two sections running from London Victoria and London Bridge to Brighton.  It is about 51 miles (81 km) long, and is electrified throughout.  Nearly all passenger trains are provided by Govia Thameslink Railway which operates the Southern, Gatwick Express and Thameslink brands.  A small section has Great Western Railway services, currently sole operator of the line from Gatwick Airport to Reading, Berkshire known as the North Downs Line.  The many Sussex services to Central London use the line and generally its branches as do south London, East Surrey and Tonbridge, Kent services.

St Albans Abbey railway station: St Albans Abbey railway station in St Albans, Hertfordshire, England is about 0.6 mi south of the city centre in the St Stephen's area.  It is the terminus of the Abbey Line from Watford Junction, part of the London Midland franchise.  It is one of two stations in St Albans, the other being the much larger and busier St Albans City.

Abbey line: The Abbey line, also called the St Albans Abbey branch line, is a railway line from Watford Junction to St Albans Abbey.  The 6.5 mi route passes through town and countryside in the county of Hertfordshire, just outside the boundaries of the Oyster Card and London fare zones.  Its northern terminus in St Albans Abbey is located in the south of the city, around 1.2 km away from the larger St Albans City railway station on the Thameslink line.

St Albans City railway station: St Albans City railway station, also shortened to St Albans, is one of two railway stations in St Albans, Hertfordshire, England, the other being St Albans Abbey railway station.  City station is the more important of the two stations, as it serves London, Gatwick Airport, Luton Airport and Brighton.  It is located 0.5 mi east of the city centre, on the Midland Main Line and served by Thameslink trains on the Thameslink route.

Gatwick Airport railway station: Gatwick Airport station is the railway station at London Gatwick Airport which provides a direct rail connection to London 26+3/4 mi away.  The station platforms are located about 70 metres to the east of the airport's South Terminal, with the ticket office above the platforms.  The station was one of 18 in the United Kingdom to be managed by Network Rail, but on 29 January 2012 day-to-day management was transferred to Southern.

Gatwick Airport Up sidings: Gatwick Airport Up sidings are located near London Gatwick Airport, Crawley, England, situated on the Brighton Main Line south of Gatwick Airport station.  The sidings are accessed from the Up Platform Loop line.

Luton Airport Parkway railway station: Luton Airport Parkway railway station is on the Midland Main Line in England, serving Luton Airport in Bedfordshire.  It is 29 mi down-line from London St Pancras and is situated between to the south and to the north.  Its three-letter station code is LTN, the IATA code for Luton Airport.

South (Luton ward): South is the name for a ward in the southern part of Luton, England.  The ward includes New Town, Park Town, Chapel Langley and most of Luton town centre.  Junction 10 of the M1 is just outside the ward.  Both Luton Airport Parkway and Luton railway station are located within the ward.  London Luton Airport is close by.

Question: Which railway station in St Albans, England services London, Gatwick Airport, Luton Airport, and Brighton?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the railway station."
    },
    "city": {
      "type": "string",
      "description": "The city where the railway station is located."
    },
    "country": {
      "type": "string",
      "description": "The country where the railway station is located."
    },
    "is_major_station": {
      "type": "boolean",
      "description": "Indicates if this is considered the more important or major station in its city."
    },
    "served_destinations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of key destinations served by this railway station."
    },
    "other_stations_in_city": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of other railway stations located in the same city."
    }
  },
  "required": [
    "station_name",
    "city",
    "country",
    "is_major_station",
    "served_destinations",
    "other_stations_in_city"
  ],
  "additionalProperties": false
}
