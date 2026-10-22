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
Bahauddin Zakariya: Baha-ud-din Zakariya (Urdu and Persian: بہاؤ الدین زکریا‎ ‎ ) (1170-1267), also spelled as Bahauddin Zakariya, and also known as Baha-ul-Haq and Hazrat Bahauddin Zakariya Multani (Rahmatullah Alaih), was a Sufi of Suhrawardiyya order (tariqa).  His full name was Abu Muhammad Bahauddin Zakariya.  He was from the lineage of Hadhrat Asad Ibn Hashim hence Hashmi.

Makerere University School of Medicine: The Makerere University School of Medicine (MUSM), also known as the Makerere University Medical School, is the school of medicine of Makerere University, Uganda's oldest and largest public university.  The medical school has been part of Makerere University since 1924.  The school provides medical education at diploma, undergraduate, and postgraduate levels.

M. Jaffar-ur-Rehman: He topped Quaid-i-Azam University by setting an all-time Computer Science Department record of a cumulative grade point average (CGPA) of 4.9 on a scale of 5.0.  In result, he was awarded the Quaid-e-Azam Scholarship for higher studies abroad, which he used to receive his Master of Science (M.Sc) degree and his Ph.D. in computer science in the United States.  He completed his M.Sc.  in just one year at the University of Pennsylvania by securing a CGPA of 3.9 on a scale of 4.0.  He taught in Australia for around three years during his Ph.D.  He came back to Pakistan after fully completing his Ph.D., where he taught at Quaid-e-Azam University, Bahauddin Zakariya University, Lahore University of Management Sciences (LUMS), and then Mohammad Ali Jinnah University.

Shrine of Bahauddin Zakariya: The Shrine of Bahauddin Zakariya (Urdu: بہاؤ الدین زکریا درگاہ‎ ) is a 13th century shrine located in the city of Multan, in Pakistan's Punjab province.  The tomb is dedicated to the Muslim mystic Bahauddin Zakariya, founder of the Suhrawardiyya order of Sufism.  It considered to be one of the most important shrines in southern Punjab province, and is the prototype for Multan's distinct architectural style.

Muhammad Zafarullah: Muhammad Zafarullah is a former professor of management science in Bahauddin Zakariya University, Multan, Pakistan, where he was the Director of the Institute of Management Sciences.  He is currently serves as Pro Rector, University of Central Punjab, UCP.  its top administrative position.

Bahauddin Zakariya University: Bahauddin Zakariya University (BZU) (Urdu: ‎ ) is a public research university with main campus in Multan, Pakistan.  BZU was founded in 1975.  It is one of the largest universities in Punjab.  Bahauddin Zakariya University was formerly known as Multan University.  It was renamed in honor of a Sufi saint Hazrat Baha-ud-din Zakariya (1171-1262).  As a degree awarding government university, it offers degree courses in more than 60 majors, including pharmacy, medical, engineering, humanities, business administration, law, art, music, IT, agriculture and languages.  According to newly published 2016-2017,Times Higher Education (THE) Ranking System, Bahauddin Zakariya University is ranked within Top 800 most powerful universities worldwide.  In 2014, The university was also ranked 8th nationally by General Universities Category of Higher Education Commission of Pakistan (HEC).

Makerere University School of Biomedical Sciences: The Makerere University School of Biomedical Sciences (MUSBS) is one of the four schools that comprise the Makerere University College of Health Sciences (MUCHS), a semi-autonomous constituent college of Makerere University, Uganda's oldest university.  Between 1924 and 2007, the school was part of the Makerere University School of Medicine and constituted the pre-clinical departments of anatomy, biochemistry, physiology, pharmacology, microbiology, and pathology.  In 2007, those departments were organized into a separate school.  MUSBS provides biomedical education at the undergraduate and postgraduate levels.

Anwaar Ahmad: Anwaar Ahmad (b. 11 June 1947 Multan) is an Urdu short story writer, scholar and academician from Pakistan.  Presently, he is serving as the Director General at University of Gujrat's Sialkot Campus.He has been associated with Bahauddin Zakariya University, Multan, and Government College University, Faisalabad as a teacher, researcher, and departmental head (Urdu) for over 35 years.  He has also served as a visiting professor at Ankara University in Ankara, Turkey and the Urdu department at Osaka University of Foreign Studies in Osaka, Japan.

Makerere University: Makerere University Kampala ( ; MUK) is Uganda's largest and third-oldest institution of higher learning, first established as a technical school in 1922.  In 1963, it became the University of East Africa, offering courses leading to general degrees from the University of London.  It became an independent national university in 1970 when the University of East Africa was split into three independent universities: University of Nairobi (Kenya), University of Dar es Salaam (Tanzania), and Makerere University.  Today, Makerere University is composed of nine colleges and one school offering programmes for about 36,000 undergraduates and 4,000 postgraduates.

Mohammed Naseer Khan: Mohammed Naseer Khan (Urdu: محمد نصیر خان‎ ; 1941 – 10 July 2006) was a Pakistani physicist and academic administrator, the former Rector of the Ghulam Ishaq Khan Institute of Engineering Sciences and Technology and Vice-Chancellor of Bahauddin Zakariya University.

Question: Which University has more accalaides' Bahauddin Zakariya University or Makerere University?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "winning_university_name": {
      "type": "string",
      "description": "The name of the university identified as having more accolades."
    },
    "comparison_summary": {
      "type": "string",
      "description": "A brief summary explaining why one university has more accolades based on the provided context."
    },
    "universities_data": {
      "type": "array",
      "description": "Detailed information about each university compared, including their specific accolades and rankings.",
      "items": {
        "type": "object",
        "properties": {
          "university_name": {
            "type": "string",
            "description": "The full name of the university."
          },
          "accolades": {
            "type": "array",
            "description": "A list of general achievements or descriptive honors for the university.",
            "items": {
              "type": "string"
            }
          },
          "rankings": {
            "type": "array",
            "description": "A list of specific ranking achievements for the university.",
            "items": {
              "type": "object",
              "properties": {
                "ranking_type": {
                  "type": "string",
                  "description": "The type of ranking (e.g., 'global', 'national')."
                },
                "rank_value": {
                  "type": "string",
                  "description": "The specific rank or range (e.g., 'Top 800', '8th')."
                },
                "source": {
                  "type": "string",
                  "description": "The source or organization that published the ranking."
                },
                "year": {
                  "type": "string",
                  "description": "The year or period the ranking applies to."
                }
              },
              "required": [
                "ranking_type",
                "rank_value",
                "source",
                "year"
              ],
              "additionalProperties": false
            }
          }
        },
        "required": [
          "university_name",
          "accolades"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "winning_university_name",
    "comparison_summary",
    "universities_data"
  ],
  "additionalProperties": false
}
