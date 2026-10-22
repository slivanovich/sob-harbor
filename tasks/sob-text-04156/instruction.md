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
Effingham Junction railway station: Effingham Junction railway station is just north of the far northern border of the village of Effingham, closer to the centre of East Horsley, homes of which it borders, in Surrey, England.  Although the station takes its name from the former town, and the immediate vicinity has itself become known as Effingham Junction, it is actually in the latter.  Effingham Junction is at the junction of the New Guildford Line, from London Waterloo to Guildford, and the line from Leatherhead, which carries trains from London Waterloo via Epsom.

Brookwood, Surrey: Brookwood is a village in Surrey, England, located about 5 km west of Woking, in a semi-rural location.  It lies on the western border of the Woking Borough (with a small part of the village in Guildford Borough).

Effingham, Surrey: Effingham is a large semi-rural and rural English village in the Borough of Guildford in Surrey, reaching from the gently sloping northern plain to the crest of the North Downs and with a medieval parish church.  The village has been chosen as the home of notable figures, such as Sir Barnes Wallis who was buried here and Toni Mascolo.  The M25 motorway is 4 mi north-west of the middle of the village which mostly consists of green space in the Metropolitan Green Belt.

Godstone railway station: Godstone railway station is on the Redhill to Tonbridge Line and serves Godstone in Surrey, England.  It is approximately two miles south of the centre of the large semi-rural village, at South Godstone, an even more rural settlement overall in the civil parish which was entirely farmland until the coming of the railway, with a few scattered woodlands.

Barnes Wallis: Sir Barnes Neville Wallis (26 September 1887 – 30 October 1979), was an English scientist, engineer and inventor.  He is best known for inventing the bouncing bomb used by the Royal Air Force in Operation Chastise (the "Dambusters" raid) to attack the dams of the Ruhr Valley during World War II.  The raid was the subject of the 1955 film "The Dam Busters", in which Wallis was played by Michael Redgrave.  Among his other inventions were his version of the geodetic airframe and the earthquake bomb.

Ockham, Surrey: Ockham is a rural and semi-rural village in the borough of Guildford in Surrey, England.  The village starts immediately east of the A3 but the lands extend to the River Wey in the west where it has a large mill-house.  Ockham is between Cobham (near Leatherhead) and East Horsley (near Guildford).

HMS Alderney (P416): HMS "Alderney" (P416), was an "Amphion"-class submarine of the Royal Navy, built by Vickers-Armstrongs at Barrow and launched 25 June 1945 by Mrs Molly Wallis, wife of Sir Barnes Wallis.  She was the 12th of the class and was scrapped in 1972.

Bransgore: Bransgore is a village and civil parish within the New Forest District, Hampshire, England.  The village developed in the 19th century when a church and a school were built.  It is technically classified as an urban area, although in some respects it still has the picturesque character of a rural English village.

Wyke, Surrey: Wyke is a rural and suburban village in Surrey, England.  Its local government district is the Borough of Guildford.  The nearest town is Aldershot, 2 mi west although the large village/town of Ash, Surrey is 1 mi west and has more shops than smaller Wyke and adjacent Normandy combined.  Normandy, Surrey is also dispersed yet is typically marked just 0.25 mi east, near its manors.  Normandy, Flexford and Christmas Pie share the parish church of Wyke, being relatively central to the four former hamlets. Wyke shares in the sports associations and community groups of Normandy.

Westcott, Surrey: Westcott is a semi-rural English village and former civil parish 1.5 mi west of the centre of Dorking on the A25 between the North Downs and Greensand Ridge, making it one of the 'Vale of Holmesdale' villages (greatly in Westcott an AONB) and is in Surrey in the direction of Guildford.  It is served by a local bus service and is 1 mi from Dorking West railway station on the North Downs Line.

Question: Effingham is a large semi-rural and rural English village in the Borough of Guildford in Surrey, the village has been chosen as the home of notable figures, such as Sir Barnes Wallis who was buried here and who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "village_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the village."
        },
        "classification": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Describes the type of village (e.g., rural, semi-rural)."
        },
        "location": {
          "type": "object",
          "properties": {
            "borough": {
              "type": "string",
              "description": "The borough the village is located in."
            },
            "county": {
              "type": "string",
              "description": "The county the village is located in."
            }
          },
          "required": [
            "borough",
            "county"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "classification",
        "location"
      ],
      "additionalProperties": false
    },
    "notable_residents": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the notable figure."
          },
          "connection_to_village": {
            "type": "string",
            "description": "The nature of their connection to the village (e.g., 'home', 'buried')."
          }
        },
        "required": [
          "name",
          "connection_to_village"
        ],
        "additionalProperties": false
      },
      "description": "A list of notable figures associated with the village."
    },
    "answer": {
      "type": "object",
      "properties": {
        "figure_name": {
          "type": "string",
          "description": "The name of the notable figure requested in the question."
        }
      },
      "required": [
        "figure_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "village_details",
    "notable_residents",
    "answer"
  ],
  "additionalProperties": false
}
