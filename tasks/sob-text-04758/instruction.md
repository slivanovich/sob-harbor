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
Dean of Chelmsford: The Dean of Chelmsford is the head ("primus inter pares" – first among equals) and chair of the Cathedral Chapter, the governing body of Chelmsford Cathedral, the Cathedral Church of St Mary the Virgin, St Peter and St Cedd.  Before 2000 the post was designated as a provost, which was then the equivalent of a dean at most English cathedrals.  The cathedral is the mother church of the Diocese of Chelmsford and seat of the Bishop of Chelmsford.  The Dean of Chelmsford is also responsible for the Chapel of St Peter-on-the-Wall at Bradwell-on-Sea, founded by St Cedd, among the oldest church buildings in regular use in England.

Truro Cathedral: The Cathedral of the Blessed Virgin Mary, Truro is a Church of England cathedral in the city of Truro, Cornwall.  It was built between 1880 and 1910 to a Gothic Revival design by John Loughborough Pearson on the site of the parish church of St Mary.  It is one of only three cathedrals in the United Kingdom with three spires.

Chelmsford Cathedral: Chelmsford Cathedral in the city of Chelmsford, Essex, England, is dedicated to St Mary the Virgin, St Peter and St Cedd.  It became a cathedral when the Anglican Diocese of Chelmsford was created in 1914 and is the seat of the Bishop of Chelmsford.

Dean of Truro: The Dean of Truro is the head ("primus inter pares" – first among equals) and chair of the chapter of canons, the ruling body of Truro Cathedral.  The dean and chapter are based at the "Cathedral Church of the Blessed Virgin Mary" in Truro.  The cathedral is the mother church of the Diocese of Truro and seat of the Bishop of Truro.  The current dean is Roger Bush.

Michael Yorke: Michael Leslie Yorke was an Anglican priest in the last decades of the 20th century and the first years of the 21st.  He was born on 25 March 1939 and educated at Midhurst Grammar School and Magdalene College, Cambridge.  Ordained in 1965 his first post was a curacy at Croydon Parish Church after which he served as Succentor, Precentor and Chaplain at Chelmsford Cathedral.  Following this he was Rector of Hadstock, a Canon Residentiary at Chelmsford Cathedral, Vicar of St Margaret’s with St Nicholas, King’s Lynn and Provost of Portsmouth Cathedral.  In 1999 he became Dean of Lichfield, and is now in retirement as Dean Emeritus.

Truro Cathedral School: Truro Cathedral School was a Church of England school for boys in Truro, Cornwall.  An ancient school refounded in 1549 as the Truro Grammar School, after the establishment of Truro Cathedral in the last quarter of the 19th century it was responsible for educating the cathedral's choristers and became known as the Cathedral School.

John Dykes Bower: Sir John Dykes Bower CVO (13 August 19051981) was an English cathedral organist, who served in Truro Cathedral, Durham Cathedral and St Paul's Cathedral.

Convent of the Epiphany: The Convent of the Epiphany, Truro, Cornwall, UK, was the home of the Community of the Epiphany, founded in 1883.  The founder of the community was George Wilkinson, Bishop of Truro.  George Wilkinson was afterwards Bishop of St Andrews, Dunkeld and Dunblane.  The sisters were involved in pastoral and educational work, the care of Truro Cathedral and St Paul's Church, and church needlework.  The head of the community was the Mother Superior and there was a branch house at Penzance.

Hubert Stanley Middleton: Hubert Stanley Middleton (11 May 1890 – 13 August 1959) was a cathedral organist, who served at Truro Cathedral and Ely Cathedral before an appointment to Trinity College, Cambridge.

Three-spired cathedrals in the United Kingdom: There are only three cathedrals in the United Kingdom with three spires. Lichfield Cathedral, dating from the 13th and early 14th centuries is the only medieval cathedral.  Between the 14th and 16th centuries Lincoln Cathedral also had three spires, but the central spire collapsed in a storm and was not rebuilt thereafter.  Both Truro Cathedral, Cornwall (late 19th–early 20th century) and St Mary's Episcopal Cathedral, Edinburgh (late 19th century) were built in the Gothic Revival style and also have three spires.

Question: Are both, Chelmsford Cathedral and Truro Cathedral, in the same country ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_in_same_country": {
      "type": "boolean",
      "description": "Indicates whether both cathedrals are located in the same country."
    },
    "cathedrals_involved": {
      "type": "array",
      "description": "Details of the cathedrals mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the cathedral."
          },
          "location_country": {
            "type": "string",
            "description": "The country where the cathedral is located."
          }
        },
        "required": [
          "name",
          "location_country"
        ],
        "additionalProperties": false
      }
    },
    "common_country": {
      "type": "string",
      "description": "The name of the country if both cathedrals are located in the same one."
    }
  },
  "required": [
    "are_in_same_country",
    "cathedrals_involved",
    "common_country"
  ],
  "additionalProperties": false
}
