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
Pacific Lutheran Theological Seminary: Pacific Lutheran Theological Seminary (PLTS) in Berkeley, California, is a seminary affiliated with the Evangelical Lutheran Church in America (ELCA) and California Lutheran University, and is a member school of the Graduate Theological Union (GTU).

ITM University (Gwalior): ITM University is a multidisciplinary university based in Gwalior, India with subjects spanning the sciences, engineering, management, fine arts, social sciences, arts, and nursing.  The University is established by the Act of State Legislature Madhya Pradesh and is notified in the Official Gazette (extraordinary) of the State Government.  The flagship Institutions under ITM Group of Institution (known as 'ITM Universe' – brand name) like Institute of Technology & Management (ITM) & Institute of Allied Science and Computer Applications (IASCA) at Gwalior are NBA & NAAC accredited respectively.

Marv Harshman: Marvel Keith Harshman (October 4, 1917 – April 12, 2013) was a college basketball coach, a head coach for forty years in the state of Washington at Pacific Lutheran University, Washington State University, and the University of Washington.

Pacific Lutheran University: Pacific Lutheran University (PLU), founded by Norwegian Lutheran pioneers in 1890, is a private university offering liberal arts and professional school programs located in Parkland, a suburb of Tacoma, Washington, United States.  PLU is sponsored by the 580 congregations of Region I of the Evangelical Lutheran Church in America.  PLU has approximately 3,100 students enrolled.  As of 2017, the school employs approximately 220 full-time professors on the 156-acre (630,000 m²) woodland campus.

Thomas W. Krise: Thomas W. Krise, Ph.D., (born 1961) is an American academic and university administrator.  He was the 13th president of Pacific Lutheran University in Tacoma, Washington, United States, (2012-17), where he is President Emeritus and Professor of English.

Graduate Theological Union: The Graduate Theological Union (GTU) is a consortium of eight private independent American theological schools and eleven centers and affiliates.  Seven of the theological schools are located in Berkeley, California.  The GTU was founded in 1962 and has established a relationship with the University of California, Berkeley that allows students from both institutions enjoying privileges accorded to their own students.  Additionally, some of the GTU consortial schools are part of other California universities such as Santa Clara University (Jesuit School of Theology) and California Lutheran University (Pacific Lutheran Theological Seminary).  Most of the GTU consortial schools are located in Berkeley around the campus of University of California, Berkeley, with the majority north of the campus in a neighborhood known as "Holy Hill" due to the cluster of GTU seminaries and centers located there.

Mike Dunbar: Mike Dunbar (December 31, 1948 – September 13, 2013) was an American football and baseball coach.  He served as the head football coach at Central Washington University in 1983 and from 1987 to 1991 and at the University of Northern Iowa from 1997 to 2000, compiling a career college football coaching record of 83–24–1.  Dunbar was also the head baseball coach at Central Washington for one season, in 1983, tallying mark of 25–20–1.  He graduated from the University of Washington in 1972 with a B.A. in education and from Pacific Lutheran University in 1979 with an M.A. in education.  Dunbar died of cancer on September 13, 2013, in his hometown of Dupont, Washington, at the age of 64.

Aaron Padilla (artist): Aaron Padilla (born 1974) is an American artist and art educator.  He was born in Wahiawa, Hawaii in 1974.  He received a BFA in painting and printmaking from Pacific Lutheran University in 1996, and an MFA in ceramics from the University of Hawaii at Manoa in 2001.  Padilla has taught at the University of Hawaii at Manoa, the Honolulu Museum of Art and the Hawaii Potters’ Guild.  He is currently Director of Spalding House, a branch of the Honolulu Museum of Art.  He has created paintings and utilitarian ceramics, as well as abstract and semi-abstract ceramic sculptures.  In his current body of work, small angled pieces of wood are assembled to give the illusion of wood being woven or tied into knots.

Bjug Harstad: Bjug Harstad (December 17, 1848 – June 20, 1933) was a Lutheran pastor, founding president of Pacific Lutheran University, and first president of the Evangelical Lutheran Synod.

Paul Fritts: Paul Fritts an American organ builder based in Tacoma, Washington who, following historical models, has created over thirty mechanical action instruments that have contributed to the revival of historically informed organ music.  The Fritts organ at St. Joseph Cathedral in Columbus, Ohio is his largest instrument to date, with three manuals (keyboards) and 66 stops.  Other recent Fritts instruments of note are located at the University of Notre Dame (2 man.  34 st.), Princeton Theological Seminary (2 man.  39), and Pacific Lutheran University (3 man.  54 st.).  The organ at PLU was the largest Fritts organ built before the organ in Columbus.

Question: ITM University and Pacific Lutheran University, both are located in the United States?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question asked by the user."
    },
    "universities_compared": {
      "type": "array",
      "description": "Details about the universities mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the university."
          },
          "location_country": {
            "type": "string",
            "description": "The country where the university is located."
          }
        },
        "required": [
          "name",
          "location_country"
        ],
        "additionalProperties": false
      }
    },
    "are_both_in_united_states": {
      "type": "boolean",
      "description": "True if both universities are located in the United States, false otherwise."
    }
  },
  "required": [
    "question_asked",
    "universities_compared",
    "are_both_in_united_states"
  ],
  "additionalProperties": false
}
