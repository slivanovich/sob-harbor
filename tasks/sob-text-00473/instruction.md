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
Korean Air Cargo Flight 6316: Korean Air Cargo Flight 6316 (also known as KAL6316 and KE6316) was a scheduled Korean Air Cargo flight from Shanghai to Seoul.  On April 15, 1999, the McDonnell Douglas MD-11F operating the route, registered as HL7373, crashed in Xinzhuang, Shanghai shortly after taking off from Hongqiao Airport, killing all 3 crew on board, along with 5 on the ground.  It was the second MD-11 crash in just over six months, and as of 2014 remains the second-deadliest MD-11 crash behind Swissair Flight 111.

London Stansted Airport: London Stansted Airport (IATA: STN, ICAO: EGSS) is an international airport located at Stansted Mountfitchet in the local government district of Uttlesford in Essex, 30 mi northeast of Central London and 0.9 mi from the Hertfordshire border.

Korean Air Cargo Flight 8509: Korean Air Cargo Flight 8509 was a Boeing 747-2B5F, registered HL7451 and bound for Milano-Malpensa Airport, that crashed due to instrument malfunction and pilot error on 22 December 1999 shortly after take-off from London Stansted Airport.  The aircraft crashed into Hatfield Forest near the village of Great Hallingbury, close to but clear of some houses.  All four crew on board were killed.

Go (airline): Go Fly (styled and trading as Go) was the name of a British low-cost airline, founded by British Airways (BA) in 1998.  It operated flights between London Stansted Airport and destinations in Europe.  The airline was purchased from BA in a management buy-out backed by the private equity firm 3i in 2001.  In 2002 it was bought by its rival EasyJet, and was merged into the airline's operations.  Its head office was in the Enterprise House in London Stansted Airport in Stansted Mountfitchet, Essex.

Stansted, Kent: Stansted (referred to in older texts as Stanstead) is a village and rural parish in the Tonbridge and Malling district of the county of Kent in the United Kingdom (not to be confused with Stansted Mountfitchet or London Stansted Airport, both of which are in Essex).

KLM uk: KLM uk was the brand name of a British airline subsidiary of KLM, which operated services within the UK and between the UK and the Netherlands using ATR-72, Fokker 50 and Fokker 100 aircraft.  KLM uk had its headquarters in the Stansted House on the grounds of London Stansted Airport in Stansted Mountfitchet, Essex.

Centurion Air Cargo Flight 164: Centurion Air Cargo Flight 164 was a chartered international cargo flight, flying from Bogota's El Dorado International Airport while en route to Miami International Airport.  The flight was operated by Kalitta Air and the aircraft was wet leased by Centurion Cargo.  On 7 July 2008, the aircraft, a Boeing 747-209BSF registered as N714CK, crashed shortly after take off.  All aboard suffered injuries, but none killed.  However, two people on the ground were killed after the plane slammed into a farm.  The crash was the second crash of a Boeing 747 in 2008 in Kalitta Air service, after a previous accident at Brussels in May.

AB Airlines: AB Airlines was an airline with its head office in the Enterprise House on the property of London Stansted Airport in Uttlesford, Essex.  AB was one of the first 'low cost airlines' in England, preceding others such as EasyJet, Ryanair, and Go Fly.  It was created in 1993 by former Brymon Airways executives.  AB Airlines was formerly known as Air Bristol.  Initially the airline marketed itself as Air Belfast, reflecting its then principal route between Belfast International Airport and London Stansted.  Aircraft and crew were based at Belfast International Airport, London Stansted Airport and Bristol Filton Airport.  A base was then opened in 1994 at Shannon Airport to operate flights to London Gatwick Airport.  This operation was marketed as AB Shannon.

Korean Air incidents and accidents: The article describes accidents and incidents on Korean Air and its predecessor companies Korean National Airlines and KAL.  Korean Air had many fatal accidents between 1970 and 1999, during which time it wrote off 16 aircraft in serious incidents and accidents with the loss of 700 lives.  The last fatal accident, Korean Air Cargo Flight 8509 in December 1999 led to a review of how Korean cultural attitudes had contributed to its poor crash history.  Since then safety has greatly improved.

RAF Stansted Mountfitchet: RAF Stansted Mountfitchet was a Royal Air Force station during the Second World War located near the village of Stansted Mountfitchet in the District of Uttlesford in Essex, 48 km north-east of central London.  The airfield is now London Stansted Airport.

Question: Korean Air Cargo Flight 8509 was a Boeing 747-2B5F, registered HL7451 and bound for Milano-Malpensa Airport, that crashed due to instrument malfunction and pilot error on 22 December 1999 shortly after take-off from London Stansted Airport, an international airport located at Stansted Mountfitchet in which local government district, in Essex, 30 mi northeast of Central London?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "flight_number": {
      "type": "string",
      "description": "The flight number involved in the incident."
    },
    "airport_of_origin": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the airport."
        },
        "local_government_district": {
          "type": "string",
          "description": "The local government district where the airport is located."
        },
        "county": {
          "type": "string",
          "description": "The county where the airport is located."
        },
        "distance_from_central_london_miles": {
          "type": "integer",
          "description": "The distance of the airport from Central London in miles."
        }
      },
      "required": [
        "name",
        "local_government_district",
        "county",
        "distance_from_central_london_miles"
      ],
      "additionalProperties": false
    },
    "destination_airport": {
      "type": "string",
      "description": "The destination airport of the flight."
    }
  },
  "required": [
    "flight_number",
    "airport_of_origin",
    "destination_airport"
  ],
  "additionalProperties": false
}
