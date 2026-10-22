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
HM Prison Pentonville: HM Prison Pentonville (informally "The Ville") is an English Category B/C men's prison, operated by Her Majesty's Prison Service.  Pentonville Prison is not in Pentonville, but is located further north, on the Caledonian Road in the Barnsbury area of the London Borough of Islington, north London.

HM Prison Rye Hill: HM Prison Rye Hill is a Category B men's private prison, operated by G4S.  Rye Hill has exclusively housed sex offenders since 2014.  The prison is situated next to HMP Onley, in the parish of Barby, Northamptonshire, England.  However, the postal address of the prison is Willoughby, Warwickshire; therefore, most sources list the prison as in Willoughby, Warwickshire.

HM Prison Bure: Her Majesty's Prison Bure, more commonly known as HM Prison Bure, and often abbreviated to HMP Bure, is a Category C men's prison, located in the parish of Scottow in Norfolk, England.  The prison is operated by Her Majesty's Prison Service, and became operational in November 2009.

HM Prison Wormwood Scrubs: HM Prison Wormwood Scrubs (informally "The Scrubs") is a Category B men's prison, located in the Wormwood Scrubs area of the London Borough of Hammersmith and Fulham, in inner west London, England.  The prison is operated by Her Majesty's Prison Service.

Kirkham, Lancashire: Kirkham (originally Kirkam-in-Amounderness) is a small town and civil parish in the Borough of Fylde in Lancashire, England, midway between Blackpool and Preston (11 miles west of Preston) and adjacent to the smaller town of Wesham.  It owes its existence to Carr Hill upon which it was built and which was the location of a Roman fort.  It has a population of 7,127, increasing to 7,194 at the Census 2011.

HM Prison Kirkham: HM Prison Kirkham is a Category D men's prison, located southwest of Kirkham in Lancashire, England.  The prison is operated by Her Majesty's Prison Service.

HM Prison Acklington: HM Prison Acklington was a Category C men's prison, located near the village of Acklington a few miles from Amble), in Northumberland, England.  Acklington Prison was operated by Her Majesty's Prison Service.  In 2011 Acklington was merged into the newly named HM Prison Northumberland.

HM Prison Isis: HM Prison Isis is a Category C male Young Offenders Institution, located in the Thamesmead area of the Royal Borough of Greenwich, in south-east London, England.  Isis Prison is operated by Her Majesty's Prison Service, and is situated next to Belmarsh Prison and Thameside Prison.

HM Prison Moorland: HM Prison Moorland (formerly HM Prison Moorland Closed) is a Category C men's prison and Young Offenders Institution, near Hatfield Woodhouse in South Yorkshire, England.  The prison is operated by Her Majesty's Prison Service, and is jointly managed with the nearby Hatfield Prison.

HM Prison Kennet: HM Prison Kennet is a Category C men's prison, located in Parkbourn, Maghull, in the Metropolitan Borough of Sefton in Merseyside, England.  The prison is operated by Her Majesty's Prison Service.  The prison is due to close in 2017.

Question: HM Prison Kirkham is a Category D men's prison, located southwest of which small town, and civil parish in the Borough of Fylde?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "prison_name": {
      "type": "string",
      "description": "The name of the prison."
    },
    "prison_category": {
      "type": "string",
      "description": "The category of the prison (e.g., Category D)."
    },
    "located_relative_to": {
      "type": "string",
      "description": "Description of the prison's location relative to the town."
    },
    "town_details": {
      "type": "object",
      "properties": {
        "town_name": {
          "type": "string",
          "description": "The name of the small town."
        },
        "is_civil_parish": {
          "type": "boolean",
          "description": "Indicates if the town is also a civil parish."
        },
        "borough": {
          "type": "string",
          "description": "The borough the town is located in."
        },
        "county": {
          "type": "string",
          "description": "The county the town is located in."
        }
      },
      "required": [
        "town_name",
        "is_civil_parish",
        "borough",
        "county"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "prison_name",
    "prison_category",
    "located_relative_to",
    "town_details"
  ],
  "additionalProperties": false
}
