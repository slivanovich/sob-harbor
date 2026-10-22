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
Anthony Pini: Carlos Antonio Pini OBE (15 April 1902 – 1 January 1989) was a cellist, known as a soloist, orchestral section leader and chamber musician.  He was principal cellist of five major British orchestras between 1932 and 1976, and a teacher at the Royal College of Music and the Guildhall School of Music and Drama.

Stockholm Academy of Dramatic Arts: On January 1, 2011 the two academies Dramatiska institutet (the Dramatic Institute/University College of Film, Radio, Television and Theatre) and Teaterhögskolan i Stockholm (Swedish National Academy of Dramatic Arts/Stockholm Academy of Dramatic Arts) founded a new academy: Stockholms dramatiska högskola, Stockholm Academy of Dramatic Arts (SADA).

Sodsai Pantoomkomol: Sodsai Pantoomkomol (Thai: สดใส พันธุมโกมล ; rtgs: Sotsai Phanthumkomon ;  ] ) née Vanijvadhana (วานิชวัฒนา ; rtgs: Wanitwatthana ; ] ; born 18 March 1934 in Bangkok, Siam) is a Thai actress and teacher of dramatic arts.  Also known as Sondi Sodsai from her acting career in the United States during her studies, she returned to Thailand to become a lecturer and associate professor at the Faculty of Arts of Chulalongkorn University, where she founded the Dramatic Arts Department, the first such school in the country.  She produced numerous theatrical works throughout her career, and was named National Artist in 2011.

Montclair Kimberley Academy: Montclair Kimberley Academy (MKA) is a co-educational private school for students in pre-kindergarten through twelfth grade located in Montclair in Essex County, New Jersey, United States.  One of New Jersey's largest independent day schools, Montclair Kimberley Academy recently celebrated the 125th anniversary of the establishment of its earliest component school.  The current school, established in 1974, is the result of the merger of three separate schools: Montclair Academy, a boys' school founded in 1887; The Kimberley School, a girls' school founded in 1906; and Brookside, a coed school founded in 1925.

USC School of Dramatic Arts: The USC School of Dramatic Arts (SDA) (formerly the USC School of Theatre) is the dramatic arts school at the University of Southern California.  It is ranked one of the top 10 dramatic arts schools in the world, according to The Hollywood Reporter's Top 25 Drama Schools.  The USC School of Dramatic Arts offers Bachelor of Arts degrees in theatre and visual & performing arts; Bachelor of Fine Arts degrees in acting, design, sound design, stage management and technical direction; and Master of Fine Arts degrees in acting and dramatic writing.

Lucy Moses School: Kaufman Music Center's Lucy Moses School is a community arts school located on the Upper West Side of Manhattan in New York City.  Founded in 1952 as The Hebrew Arts School for Music and Dance, it is now part of Kaufman Music Center, a performing arts complex that houses the Special Music School (P.S. 859) and Merkin Concert Hall.  It is the largest community arts school in the city, and offers lessons to 3,000 children and adults annually.

Mehdi Forough: Mehdi Forough (1911–2008) was an Iranian scholar, author, dramatist, writer on dramatic arts and culture, translator, and founder of the Academy of Dramatic Arts in Tehran.  A native of Esfahan, Mehdi Forough attended Danesh Sara-ye Aali in Tehran and went on to study at the Royal Academy of Dramatic Arts, London.  He did graduate studies at Columbia University, NYC, where he completed his thesis, "Comparative study of Abraham's sacrifice in Persian passion plays and Western mystery plays", 1954.  This work was later published by the Ministry of Culture, in Tehran.

Higher Institute for Dramatic Arts: Higher Institute of Dramatic Arts (Arabic: المعهد العالي للفنون المسرحية‎ ‎ ) was founded in Damascus, Syria in 1977.  The institute heralded a new phase in the development of Syrian theatre and drama which begun with the preparation of the next generation of actors on an academic basis.  The Institute includes three departments: Acting, Theatrical Critique and Dramatic Arts.  The Institute has succeeded in rapidly making its mark on the theatre and dramatic arts scene with world class performances being presented in Kuwait, Egypt, Jordan, Lebanon, Germany and many others.

Dixons City Academy: Dixons City Academy is an academy in Bradford, West Yorkshire, England.  The school was founded in 1990 as Dixons City Technology College which focused on a specialism of design and technology and product design.  In 2005, the school converted into an academy and changed its name to Dixons City Academy.  With the change of name was a change of focus as the school became a specialist performing arts school which allows it to select 10% of admissions purely based on talent in this area.  In 2007, the school received an "outstanding" Ofsted report.  The school founded the Dixons Academy Trust which includes Dixons Allerton Academy, Dixons Kings Academy, Dixons McMillan Academy and Dixons Trinity Academy.

Guildhall School of Music and Drama: The Guildhall School of Music and Drama is an independent music and dramatic arts school which was founded in 1880 in London, England.  Students can pursue courses in music, opera, drama and technical theatre arts.

Question: Who was a teacher at an independent music and dramatic arts school founded in 1880 in London?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "teacher_name": {
      "type": "string",
      "description": "The full name of the teacher."
    },
    "school_name": {
      "type": "string",
      "description": "The name of the school where the person was a teacher."
    },
    "school_founding_year": {
      "type": "integer",
      "description": "The year the school was founded."
    },
    "school_location": {
      "type": "string",
      "description": "The city and country where the school is located."
    },
    "teacher_role": {
      "type": "string",
      "description": "The role of the person at the school."
    }
  },
  "required": [
    "teacher_name",
    "school_name",
    "school_founding_year",
    "school_location",
    "teacher_role"
  ],
  "additionalProperties": false
}
