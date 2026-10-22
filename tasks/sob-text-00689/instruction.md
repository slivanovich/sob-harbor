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
Gaetan Proulx: Gaétan Proulx is a bishop of Roman Catholic Archdiocese of Quebec.  Born 27 May 1947 in Saint-Denis-de-Brompton, Quebec, he became a Professed Member of the Order of Servants of Mary On 5 Sep 1969 and was ordained a priest on 8 Jun 1975.

Christopher Hirst: Christopher Halliwell Hirst (born 27 May 1947) is a former English cricketer and educator.  Hirst was a right-handed batsman who bowled right-arm off break.  He was born in Odsal, Bradford, Yorkshire.

David Russell, 5th Baron Ampthill: David Whitney Erskine Russell, 5th Baron Ampthill (born 27 May 1947) is the son of Geoffrey Russell, 4th Baron Ampthill, and was educated at Stowe School.  He served as a councillor on Rye Town Council from July 2003 until April 2013, and currently serves as a Conservative councillor on Rother District Council.  He previously served on East Grinstead Town Council and held the post of Mid-Sussex District Council Cabinet Member for Community Development.

Chan Kwan Lap: Eddy Chan Kwan Lap (; born 27 May 1947) is a modern Chinese ink painter.  He finished a certificate course in Modern Chinese Ink Painting, awarded a bachelor's degree in Fine Arts and the master's degree of Fine Arts.  He has been honored with different awards.  Moreover, his works are now in the collections of both local and overseas museums and art institutes, such as the Hong Kong Museum of Art, Shanghai Foreign Culture Exchange Association (China), Daegu Culture and Art Centre (South Korea), and the 1997 Mountain Lake Collection (United States).

Marta Vincenzi: Marta Vincenzi (born 27 May 1947) is an Italian politician and former Mayor of Genoa.  She was previously a Member of the European Parliament for the North-West of Italy with the Democrats of the Left (DS), part of the Socialist Group from 2004 until she resigned on 29 June 2007.

Riivo Sinijärv: Riivo Sinijärv (born 27 May 1947 in Tallinn) is an Estonian politician and a former Minister of Foreign Affairs.

ND Črnuče: Nogometno Društvo Črnuče, commonly referred to as ND Črnuče or simply Črnuče, is a Slovenian football club from the town of Črnuče, founded in 1971.  Their golden years came in the mid-1990s, when they were managed by Slovenian football legend Branko Oblak, who came to Črnuče as manager in 1994.  They have won the Slovenian Third League and finished in the third place in the 1995–96 Slovenian Second League, but then refused promotion.  They merged with nearby NK Factor in 1997 and the team moved to Factor's home ground in Ježica.  Črnuče then reestablished their own squad to play at domestic Črnuče Sports Park in lower divisions, but they never came higher than fourth level.

Peter Knight (folk musician): Peter Knight (born 27 May 1947) is a folk musician, a former member of British folk rock group Steeleye Span.  Born in London, as a child Knight learned the violin and mandolin before going to the Royal Academy of Music from 1960 to 1964.  The recordings of the Irish fiddler Michael Coleman inspired him to take part in Irish pub sessions.  He teamed up with guitarist and singer Bob Johnson until 1970 when he joined Steeleye Span.  The parting was short-lived, as Johnson himself also joined Steeleye Span in 1972.

John Ashton (public health director): Professor John Ashton CBE (born 27 May 1947 in Liverpool) is a former a lecturer and professor of public health at Southampton/London School of Hygiene and Tropical Medicine /and the University of Liverpool Medical School.  He was Regional Director of Public Health/Regional Medical Officer for the North West of England for 13 years and Director of Public Health/County Medical Officer for 6 years.

Branko Oblak: Branko Oblak (born 27 May 1947 in Ljubljana, PR Slovenia, FPR Yugoslavia) is a Slovenian football coach and former international player.  He usually played as an attacking midfielder or deep-lying playmaker.

Question: who is the coach for ND Črnuče in 1994 who was born 27 May 1947 ? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person identified."
    },
    "role": {
      "type": "string",
      "description": "The role of the person in relation to the football club."
    },
    "club_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "year_of_involvement": {
      "type": "integer",
      "description": "The year the person was involved with the club in the specified role."
    },
    "date_of_birth": {
      "type": "string",
      "description": "The birth date of the person in YYYY-MM-DD format."
    }
  },
  "required": [
    "person_name",
    "role",
    "club_name",
    "year_of_involvement",
    "date_of_birth"
  ],
  "additionalProperties": false
}
