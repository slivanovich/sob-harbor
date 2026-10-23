{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPriory Church, South Queensferry: The Priory Church of St Mary of Mount Carmel, commonly called the Priory Church or St Mary's Episcopal Church, is a congregation of the Scottish Episcopal Church located in South Queensferry, near Edinburgh, Scotland.\n\nCranborne Priory: Cranborne Priory was a priory in Cranborne in Dorset, England.  The priory church survives as Cranborne's parish church, the Church of St Mary and St Bartholomew, and is a Grade I listed building, with parts of the building dating back to the 12th century.\n\nPoulton Priory: Poulton Priory or the Priory of St Mary was a Gilbertine priory in Poulton, Gloucestershire, England.  It was founded as a chantry chapel in 1337 by Sir Thomas Seymour and became a house of Gilbertine canons in 1350.  From 1539, with the Dissolution of the Monasteries, the priory was used as the parish church for Poulton.  It was demolished in 1873.\n\nSt Chad's Church, Poulton-le-Fylde: Soon after the Norman conquest, Poulton was granted to Lancaster Priory.  In the 15th century, the church was given by Henry V to Syon Monastery in Middlesex.  It returned to the Crown following the Dissolution of the Monasteries and from the 16th to the 20th century, the advowson (the right to appoint a parish priest) belonged to the Hesketh/Fleetwood family.\n\nListed buildings in St Bees: St Bees is a civil parish in the Borough of Copeland, Cumbria, England.  It contains 38 buildings that are recorded in the National Heritage List for England.  Of these, four are listed at Grade I, the highest of the three grades, two are at Grade II*, the middle grade, and the others are at Grade II, the lowest grade.  The parish includes the village of St Bees and the surrounding coastline and countryside.  In the 12th century a Benedictine priory was established in the parish.  Most of this disappeared after the Dissolution of the Monasteries apart from the priory church, most of which became the Church of St Mary and St Bega, the parish church of the village, while most of the chancel was modified for other uses.  Also in the village is St Bees School, an independent school.  The church, the school, and a number of associated structures are listed.  Most of the other listed buildings are houses and associated structures, and farmhouses and farm buildings.  The other listed buildings include a bridge, a signal box, and two war memorials.\n\nBungay Priory: Bungay Priory was a Benedictine nunnery in the town of Bungay in the English county of Suffolk.  It was founded in about 1160 by Roger de Glanville and his wife the Countess Gundreda and dissolved in about 1536 during the dissolution of the monasteries at which time it consisted of a prioress and 11 nuns.  The priory church, the Church of the Holy Cross, became the Church of St Mary, the parish church in Bungay.  Although ruins of the priory remain to the east of the church, any remaining intact buildings are likely to have been destroyed in the Bungay fire of 1688 which severely damaged the church itself.  The church and the ruins of the priory are a Grade I listed building.\n\nSt Mary and St Peter's Church, Wilmington: St Mary and St Peter's Church is in the village of Wilmington, East Sussex, England.  It is an active Anglican parish church on the deanery of Lewes and Seaford, the archdeaconry of Lewes and Hastings, and the diocese of Chichester.  Founded in the late 11th century to serve villagers in a rural area at the foot of the South Downs, it also functioned as a priory church for the monks from the adjacent Wilmington Priory, to which it was physically connected.  The building has \"benefited from sympathetic restoration\" over the centuries—including a series of works by prominent architects Paley and Austin in the Victorian era, and internal renovation after a fire in the early 21st century.  The church is recorded in the National Heritage List for England as a designated Grade I listed building.\n\nLancaster Priory: Lancaster Priory, formally the Priory Church of St Mary, is the Church of England parish church of the city of Lancaster, Lancashire, England.  It is located near Lancaster Castle and since 1953 has been designated a Grade I listed building.  It is in the deanery of Lancaster, the archdeaconry of Lancaster and the Diocese of Blackburn.  Its benefice is combined with that of St John and St Anne.\n\nMonmouth Priory: Monmouth Priory, Priory Street, Monmouth, Monmouthshire is a building that incorporates the remains of the monastic buildings attached to St Mary’s Priory Church.  The priory was a Benedictine foundation of 1075, and parts of the mediaeval buildings remain.  The buildings were substantially redeveloped in the nineteenth century for use as St Mary's National School, and now form a community centre.  The complex is a Grade II* listed building as of 27 June 1952.  It is one of 24 sites on the Monmouth Heritage Trail.\n\nBinham Priory: St Mary's Priory, Binham, or Binham Priory, is a ruined Benedictine priory located in the village of Binham in the English county of Norfolk.  Today the nave of the much larger priory church has become the \"Church of St. Mary and the Holy Cross\" and is still used as a place of worship.  The remains of the priory are in the care of English Heritage.\n\nQuestion: Who gave Poulton to the church ,formally the Priory Church of St Mary, In the 15th century?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"giver_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who granted the entity.\"\n    },\n    \"century_of_grant\": {\n      \"type\": \"integer\",\n      \"description\": \"The century in which the grant occurred.\"\n    },\n    \"granted_entity\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of entity that was granted (e.g., 'church').\"\n        },\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The specific name of the granted entity.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The location of the granted entity.\"\n        }\n      },\n      \"required\": [\n        \"type\",\n        \"name\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"recipient_institution_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the institution that received the grant.\"\n    }\n  },\n  \"required\": [\n    \"giver_name\",\n    \"century_of_grant\",\n    \"granted_entity\",\n    \"recipient_institution_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "giver_name": {
        "type": "string",
        "description": "The name of the person who granted the entity."
      },
      "century_of_grant": {
        "type": "integer",
        "description": "The century in which the grant occurred."
      },
      "granted_entity": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "description": "The type of entity that was granted (e.g., 'church')."
          },
          "name": {
            "type": "string",
            "description": "The specific name of the granted entity."
          },
          "location": {
            "type": "string",
            "description": "The location of the granted entity."
          }
        },
        "required": [
          "type",
          "name",
          "location"
        ],
        "additionalProperties": false
      },
      "recipient_institution_name": {
        "type": "string",
        "description": "The name of the institution that received the grant."
      }
    },
    "required": [
      "giver_name",
      "century_of_grant",
      "granted_entity",
      "recipient_institution_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
