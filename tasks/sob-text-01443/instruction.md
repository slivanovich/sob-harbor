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
Bombardier Aerospace Emergency Services (Toronto): Bombardier Aerospace Emergency Services (Toronto) is responsible for fire and emergency services at Bombardier Aerospace's assembly and testing facility at Downsview Airport.

Downsview Airport: Downsview Airport or Toronto/Downsview Airport, (ICAO: CYZD) , is located in the North York district of Toronto, Ontario, Canada and has been exclusively owned and used as a testing facility by Bombardier Aerospace since 1994.

CFB Toronto: Canadian Forces Base Toronto (also CFB Toronto) is a former Canadian Forces base in Toronto, Ontario.  The airfield is currently operated as Toronto/Downsview Airport.

Downsview: Downsview is an area in the north end of Toronto, Ontario, Canada, located in the district of North York.  Downsview was originally a farm located in the 1870s near the present-day intersection of Keele Street and Wilson Avenue.  It now extends beyond the intersection of Sheppard Avenue and Dufferin Street, though it is popularly seen as including the areas to the north right up to the Toronto city limits at Steeles Avenue.  The area includes several large post-World War II subdivisions.  Within the area is Downsview Airport, the former site of Canadian Forces Base Downsview, which has since been largely converted following the end of the Cold War into an urban park known as Downsview Park.  However, the airport is still used as a manufacturing and testing facility for Bombardier Aerospace.

Denison Armoury: Lieutenant-Colonel George Taylor Denison III Armoury, commonly known as Denison Armoury, is a Canadian Forces facility located at 1 Yukon Lane in Toronto, Ontario, Canada.  It is in the northeastern corner of Downsview Airport just west of the W.R. Allen Expressway (Allen Road) on Sheppard Avenue West.  The Armoury is the headquarters of 4th Canadian Division (formerly Land Force Central Area), Joint Task Force Central, and the 32 Canadian Brigade Group.  It is also home to several units of the brigade.

Bombardier Transportation: Bombardier Transportation is the rail equipment division of the Canadian firm Bombardier Inc. Bombardier Transportation is one of the world's largest companies in the rail vehicle and equipment manufacturing and servicing industry.  The division is headquartered in Berlin, Germany, and has regional offices and major development facilities in Canada (Montreal and Toronto) and the United States (Plattsburgh, New York).  Bombardier Transportation has many minor production and development facilities worldwide.

Bombardier Aerospace: Bombardier Aerospace (French: "Bombardier Aéronautique" ) is a division of Bombardier Inc. It is headquartered in Dorval, Quebec, Canada.

Bombardier Recreational Products: Bombardier Recreational Products (BRP) is a Canadian company making various vehicles.  Once part of Bombardier Inc., it was founded in 1942 as "L'Auto-Neige Bombardier Limitée" (Bombardier Snow Car Limited) by Joseph-Armand Bombardier at Valcourt in the Eastern Townships, Quebec.

Can-Am Off-Road: Can-Am ATVs and side-by-side vehicles are manufactured by BRP / Bombardier Recreational Products a Canadian company, once part of Bombardier Inc.  Founded in 1942 as L'Auto-Neige Bombardier Limitée (Bombardier Snow Car Limited) by Joseph-Armand Bombardier in Valcourt Quebec Canada.

Toronto Aerodrome: Toronto Aerodrome, also known as Canadian Air Express Airport was an aerodrome located in Toronto, Ontario, Canada.  One of the historical airfields of Canada, operated from 1928 to 1939, it was situated at the current Downsview subway station on Dufferin Street and Sheppard Avenue West.  Toronto Aerodrome was one of the several small airfields, which were established in the Toronto area during the 1920s and 1930s.  This aerodrome served as the principal custom entry point for aircraft coming to Toronto until 1939, when Malton airfield, now Toronto Pearson International Airport, became operational.  The aerodrome shared the site with the Toronto Flying Club (located at Dufferin Street and Wilson Avenue).  The Toronto Flying Club's site is now the south end of Downsview Airport, TTC Wilson Complex.  Following the end of World War II into the 1960s, parts of former airfield and surrounding farmland were developed into the residential neighbourhood of Wilson Heights and mixed commercial-industrial area of Downsview.

Question: Where is the headquarters of the division of Bombardier Inc that owns Downsview Airport?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the parent company."
    },
    "division_name": {
      "type": "string",
      "description": "The name of the division that owns the airport."
    },
    "airport_name": {
      "type": "string",
      "description": "The name of the airport in question."
    },
    "ownership_details": {
      "type": "object",
      "properties": {
        "owner_division": {
          "type": "string",
          "description": "The division identified as the owner or exclusive user."
        },
        "ownership_start_year": {
          "type": "integer",
          "description": "The year ownership or exclusive use began."
        }
      },
      "required": [
        "owner_division",
        "ownership_start_year"
      ],
      "additionalProperties": false
    },
    "headquarters_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the division's headquarters is located."
        },
        "province_state": {
          "type": "string",
          "description": "The province or state where the division's headquarters is located."
        },
        "country": {
          "type": "string",
          "description": "The country where the division's headquarters is located."
        }
      },
      "required": [
        "city",
        "province_state",
        "country"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "company_name",
    "division_name",
    "airport_name",
    "ownership_details",
    "headquarters_location"
  ],
  "additionalProperties": false
}
