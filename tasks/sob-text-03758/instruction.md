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
Newtownards: Newtownards, is a large town, townland and civil parish in County Down, Northern Ireland.  It lies at the most northern tip of Strangford Lough, 10 miles (16 km) east of Belfast, on the Ards Peninsula.  It is situated in the civil parish of Newtownards and the historic baronies of Ards Lower and Castlereagh Lower.  Newtownards is the largest town in the former Borough of Ards.  It is known colloquially by locals as "Ards".  It had a population of 28,039 people in the 2011 Census.

South Ormsby: South Ormsby, sometimes called South Ormesby, is a village in the East Lindsey district of Lincolnshire, England.  It is situated 1 mi west from the A16 road, 7 mi south from Louth and 7 miles north-east from Horncastle.  With the nearby hamlet of Ketsby, it forms the civil parish of South Ormesby with Ketsby.  The population is included in the civil parish of Brinkhill.

Greyabbey: Greyabbey or Grey Abbey is a small village, townland (of 208 acres) and civil parish located on the eastern shores of Strangford Lough, on the Ards Peninsula in County Down, Northern Ireland.  It lies 7 mi south of Newtownards.  Both townland and civil parish are situated in the historic barony of Ards Lower.  It is within the Borough of Ards.  It had a population of 939 people in the 2011 Census.

St Weonards: St Weonards (correctly pronounced 'wonnards') is a village and civil parish in Herefordshire, England, located 10 mi south of Hereford, 7 mi west of Ross-on-Wye and 7 mi north of Monmouth, on the A466 road.  Within the parish and also on the A466 is the hamlet of Sandyway.  St Weonards lies within the area known to the Saxons (and later English) as Archenfield, previously the kingdom of Ergyng, adjoining the modern border with Wales.  Ergyng was later reduced to a semi-autonomous cantref retaining Welsh language and customs until the early nineteenth century.

Walesby, Lincolnshire: Walesby is a village and civil parish in the West Lindsey district of Lincolnshire, England.  The population of the civil parish at the 2011 census was 249.  It lies in the Lincolnshire Wolds, 3 mi north-east from Market Rasen and 7 mi south from Caistor.  Tealby parish lies to the south-east.  The parish covers about 3600 acre and includes the hamlets of Risby and Otby.

Marbury, Cheshire: Marbury is a small village located at [ SJ560457] in the civil parish of Marbury cum Quoisley, within the unitary authority of Cheshire East and the ceremonial county of Cheshire, England.  It is administered jointly with the adjacent civil parishes of Norbury and Wirswall.  The village lies around 3 mi north east of Whitchurch in Shropshire and 7 mi south west of Nantwich in Cheshire.  Nearby villages include Malpas, No Man's Heath, Norbury, Wirswall and Wrenbury.  The civil parish is on the boundary with Shropshire, and also contains the small settlements of Hollins Lane, Marley Green and Quoisley, as well as parts of Hollyhurst and Willeymoor, with a total population in 2011 of 352.

Bridgemere: Bridgemere is a village (at [ SJ717454] ) and civil parish in the unitary authority of Cheshire East and the ceremonial county of Cheshire, England.  It is around 7 mi south east of Nantwich and 12 mi west of Stoke-on-Trent.  The southern boundary of the parish is on the border with Shropshire.  The civil parish also includes the small settlements of Admiral's Gorse, Parrah Green, Prince Hill, Seven Stars and Wheel Green.  The total population is a little under 150.  Nearby towns include Crewe in Cheshire, Market Drayton and Whitchurch in Shropshire, and villages include Blakenhall, Buerton and Hankelow in Cheshire, Madeley, Staffordshire and Woore, Shropshire.

Chipping Ongar: Chipping Ongar is a small market town in the civil parish of Ongar, in the Epping Forest district of the county of Essex, England.  It is located 6 mi east of Epping, 7 mi southeast of Harlow and 7 mi northwest of Brentwood.  For population details taken at the 2011 Census see under the civil parish of Ongar.

Normanton, Lincolnshire: Normanton, sometimes called Normanton on Cliffe, is a village and civil parish in the South Kesteven district of Lincolnshire, England.  It is situated on the A607 road, about 7 mi north from the town of Grantham and 18 mi south from the city and county town of Lincoln.  It is in the civil parish of Carlton Scroop.

Witham St Hughs: Witham St Hughs is a village and civil parish in the North Kesteven district of Lincolnshire, England.  The population of the civil parish (including Thurlby) was 2,356 at the 2011 census.  It is situated less than 0.5 mi south from the A46 road, geographically 8 mi south-west from the city and county town of Lincoln, and 7 mi north-east from the town of Newark-on-Trent.

Question: Greyabbey is 7mi south of the civil parish in what Northern Irish county?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "location_name": {
      "type": "string",
      "description": "The name of the primary location being described."
    },
    "distance_from_reference": {
      "type": "integer",
      "description": "The distance from the reference location."
    },
    "distance_unit": {
      "type": "string",
      "description": "The unit of measurement for the distance."
    },
    "reference_location": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the reference location."
        },
        "type": {
          "type": "string",
          "description": "The type of the reference location (e.g., civil parish, town)."
        },
        "county": {
          "type": "string",
          "description": "The county where the reference location is situated."
        },
        "country_region": {
          "type": "string",
          "description": "The country or region where the reference location is situated."
        }
      },
      "required": [
        "name",
        "type",
        "county",
        "country_region"
      ],
      "additionalProperties": false
    },
    "answer_county": {
      "type": "string",
      "description": "The county that answers the question."
    }
  },
  "required": [
    "location_name",
    "distance_from_reference",
    "distance_unit",
    "reference_location",
    "answer_county"
  ],
  "additionalProperties": false
}
