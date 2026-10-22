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
Wallace Michael Ross: Wallace Michael Ross (19 September 1920 – 20 January 2010) was the founder of the Derby Bach Choir.  He was also the Master of Music at Derby Cathedral, assistant organist at several great English Cathedrals, teacher of languages and music at several schools including Sturgess School in Derby.  He also founded the Derby Cathedral Brass Ensemble and the Derby Sinfonia.

Carlisle Cathedral: The Cathedral Church of the Holy and Undivided Trinity, otherwise called Carlisle Cathedral, is the seat of the Anglican Bishop of Carlisle.  It is located in Carlisle, in Cumbria, North West England.  It was founded as an Augustinian priory and became a cathedral in 1133.

Alfred William Wilcock: Alfred William Wilcock (1887 – 1953) was an cathedral organist, who served in Derby Cathedral and Exeter Cathedral.

Cantoris: Cantoris (Latin: "of the cantor"; ) is the side of a church choir occupied by the Cantor.  In English churches this is typically the choir stalls on the north side of the chancel, although there are some notable exceptions, such as Durham Cathedral, Carlisle Cathedral and Southwell Minster.  The opposite side is known as Decani.

Diocese of Derby: The Diocese of Derby is a Church of England diocese in the Province of Canterbury, roughly covering the same area as the County of Derbyshire.  Its diocesan bishop is the Bishop of Derby who has his seat at Derby Cathedral.  The diocesan bishop is assisted by the suffragan bishop, the bishop of Repton.

Trinity School, Carlisle: Trinity School (formerly "Carlisle Grammar School") is a large mixed secondary school and sixth form in Carlisle, Cumbria, for students aged 11 to 18.  Since September 2011, it has been an academy.  It is a Church of England school with strong links to Carlisle Cathedral.

George Handel Heath-Gracie: George Handel Heath-Gracie BMus (Dunelm) FRCO was Head Teacher at Derby School of Music (1938–1944), he was also a composer and cathedral organist, who served in Derby Cathedral.

Dean of Carlisle: The Dean of Carlisle is based in Carlisle, UK and is the head of the Chapter of Carlisle Cathedral.  There have been 39 previous incumbents and the current holder of the post is Mark Boyling.

Dean of Derby: The Dean of Derby is the head ("primus inter pares" – first among equals) and chair of the chapter of canons, the ruling body of Derby Cathedral.  The dean and chapter are based at the "Cathedral Church of All Saints" in Derby.  Before 2000 the post was designated as a provost, which was then the equivalent of a dean at most English cathedrals.  The cathedral is the mother church of the Diocese of Derby of the Church of England and seat of the Bishop of Derby.

Derby Cathedral: Derby Cathedral, known as the Cathedral of All Saints, is a grade I listed cathedral church in the city of Derby, in the county of Derbyshire, England.  It was promoted from parish church status into a cathedral in 1927 in order to create a seat for the Bishop of Derby, which new see was created in that year.  The original church of All Saints was founded in the mid-10th century as a royal collegiate church, dedicated to All Saints.  It became a cathedral in 1927.  The main body of the church as it stands today is a Georgian rebuilding by James Gibbs, completed in 1725.  The tower dates from the 16th century, and a retrochoir was added in the 20th century.

Question: are Derby Cathedral and  Carlisle Cathedral in the same country

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cathedrals_compared": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Names of the cathedrals being compared."
    },
    "location_details": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "cathedral_name": {
            "type": "string",
            "description": "Name of the cathedral."
          },
          "country": {
            "type": "string",
            "description": "Country where the cathedral is located."
          },
          "region": {
            "type": "string",
            "description": "Region within the country."
          }
        },
        "required": [
          "cathedral_name",
          "country"
        ],
        "additionalProperties": false
      },
      "description": "Detailed location information for each cathedral."
    },
    "are_in_same_country": {
      "type": "boolean",
      "description": "True if both cathedrals are in the same country, false otherwise."
    },
    "common_country": {
      "type": "string",
      "description": "The common country if they are in the same one."
    }
  },
  "required": [
    "cathedrals_compared",
    "location_details",
    "are_in_same_country",
    "common_country"
  ],
  "additionalProperties": false
}
