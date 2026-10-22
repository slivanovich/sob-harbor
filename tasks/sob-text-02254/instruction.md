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
JetSmart: JetSmart is an ultra low-cost Chilean airline created by US investment fund Indigo Partners, which also controls US airline Frontier Airlines, Mexico's Volaris and Hungarian airline Wizz Air.  Its primary base of operations is Comodoro Arturo Merino Benítez International Airport, in Santiago, Chile.  The airline commenced scheduled operations on 25 July 2017 with a Santiago-Calama service.

Haugesund Airport, Karmøy: Haugesund Airport, Karmøy (Norwegian: "Haugesund lufthavn, Karmøy" ; IATA: HAU, ICAO: ENHD ) is an international airport serving the Haugesund region in Norway.  It is located on the Hauganes peninsula on the island of Karmøy in the municipality of Karmøy, Rogaland county, Norway.  The airport features a 2120 m runway aligned 13/31.  Scandinavian Airlines (SAS) and Norwegian Air Shuttle provide services to Oslo, while Widerøe flies to Bergen and Copenhagen.  Haugesund Airport also offers discounts on international routes and acts as a "low-cost" airport for Ryanair and Wizz Air.  The airport handled 694,005 passengers in 2014.

Norport Handling: Norport Handling AS is an aircraft ground handling company that operates at four Norwegian airports: Bergen Airport, Flesland, Stavanger Airport, Sola, Haugesund Airport, Karmøy and Moss Airport, Rygge.  The company has 320 employees and more than 110 customers.  Revenue was NOK 120 million in 2008.  The company handles 800 weekly movements.

Haugesund Airport, Storesundsskjær: Haugesund Airport, Storesundsskjær (Norwegian: "Haugesund sjøflyhavn, Storesundsskjær" ) was a water aerodrome which served Haugesund, Norway, from 1936 to 1956.  The airport consisted of a barge anchored at Midtre Storesundsskjær in Haugesund's port.  Affixed was a floating dock and a terminal building.

Charles de Gaulle Airport: Paris Charles de Gaulle Airport (French: "Aéroport de Paris-Charles-de-Gaulle" , IATA: CDG, ICAO: LFPG ), also known as Roissy Airport (name of the local district), is the largest international airport in France.  It is named after Charles de Gaulle (1890–1970), leader of the Free French Forces during the Second World War, founder of the French Fifth Republic and President of France from 1959 to 1969.  Charles de Gaulle Airport is located within portions of several communes 25 km to the northeast of Paris.  Charles de Gaulle Airport serves as the principal hub for Air France as well as a European hub for fellow SkyTeam alliance partner Delta Air Lines.  Additionally, the airport serves as a focus city for low-cost carriers Vueling and Norwegian Air Shuttle.

Nordsjøfly: Nordsjøfly A/S was an airline which operated from 1977 to 1983 out of Haugesund Airport, Karmøy.  Based in Avaldsnes in Karmøy, Norway, the airline used a mix of aircraft to operate scheduled and charter flights.  It was started at the time of Haugesund Airport opening and commenced a taxi route service to Bergen and Stavanger, at first using the Piper PA-31 Chieftain and a Beechcraft 99 Queenliner.

Sandefjord Airport, Torp: Sandefjord Airport, Torp (Norwegian: "Sandefjord lufthavn, Torp" ; IATA: TRF, ICAO: ENTO , marketed as TORP Sandefjord lufthavn) is an international airport located 4 NM northeast of Sandefjord, Norway and 110 km south of Oslo.  The airport features a 2989 m runway aligned 18/36.  Torp partially serves as a regional airport for Vestfold and in part as a low-cost airport for Eastern Norway and the capital of Oslo.  Widerøe have a base at Torp, serving both domestic and international destinations.  It also sees scheduled flights by Norwegian Air Shuttle, Ryanair, Wizzair and KLM Cityhopper.  The airport served 1,851,181 passengers in 2013.

Coast Aero Center: Coast Aero Center A/S was a regional airline based Haugesund Airport, Karmøy in Karmøy, Norway.  It had only small-plane operations and mechanical services until 1984, when it acquired concessions to operate at the new Stord Airport, Sørstokken, Geilo Airport, Dagali, and eventually from Haugesund to Aberdeen.  It soon turned out that the company was not profitable and it filed for bankruptcy in 1988.  The estate continued on as Coast Air.

Wizz Air: Wizz Air, legally incorporated as "Wizz Air Hungary Ltd." (Hungarian: "Wizz Air Hungary Légiközlekedési Kft. " ), is a Hungarian low-cost airline with its head office in Budapest.  The airline serves many cities across Europe, Israel and the United Arab Emirates.  It has the largest fleet of any Hungarian airline, although it is not a flag carrier, and currently serves 42 countries.  Its Jersey based parent company, Wizz Air Holdings Plc, is listed on the London Stock Exchange and is a constituent of the FTSE 250 Index.

Coast Air: Coast Air AS was a regional airline based at Haugesund Airport, Karmøy in Norway.  It was Norway's fourth largest airline and operated domestic services within Norway, in addition to international services.  Routes were concentrated along the West Coast, as well as some public service obligation contracts in Southern Norway.  The company had a fleet of de Havilland Canada Twin Otter aircraft, later replaced with Jetstream 31s and ATR 42s.

Question: Haugesund Airport serves as a low-cost airport for which Hungarian airline?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airport_name": {
      "type": "string",
      "description": "The name of the airport that serves as a low-cost hub."
    },
    "airline": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Hungarian airline."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the airline is based."
        },
        "is_low_cost_carrier": {
          "type": "boolean",
          "description": "Indicates if the airline is a low-cost carrier."
        }
      },
      "required": [
        "name",
        "country_of_origin",
        "is_low_cost_carrier"
      ],
      "additionalProperties": false
    },
    "serves_as_low_cost_airport_for_this_airline": {
      "type": "boolean",
      "description": "Indicates whether the specified airport acts as a low-cost airport for the identified airline."
    }
  },
  "required": [
    "airport_name",
    "airline",
    "serves_as_low_cost_airport_for_this_airline"
  ],
  "additionalProperties": false
}
