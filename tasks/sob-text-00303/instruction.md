{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGet Schooled: The Get Schooled Foundation (also Get Schooled or getschooled.com) is a non-profit organization dedicated to using the power of media, technology and popular culture to motivate and inspire young people, their families and teachers to improve high school graduation rates and college-going rates.  Get Schooled combines powerful national content and programming (on-air, on-line and on the ground), with school-based engagement strategies to ensure both a broad reach and a measurable impact.\n\nEpule Jeffrey: Epule Jeffrey Ewusi, was born in Buea South west Region of Cameroon.  He is a Bakosian by tribe,he went to PNEU primary school in Bamenda, Bilingual Grammer School (Lycee) Molyko in Buea and obtained a decree in Public Law 2006 at the University of Yaounde II.\n\nIrish Institute: The Irish Institute (Spanish: \"Instituto Irlandés\" ) is a highly selective private school in Greater Mexico City.  Operated by the Legionaries of Christ, it has separate campuses for boys' and girls' schools and a preschool in Naucalpan, State of Mexico.  The school levels in total range from preschool to \"bachillerato\", equivalent to the American K-12.  The preschool is coeducational but other levels are separated into the boys' and girls' campuses.  It is one of the most prestigious and selective private schools in Mexico\n\nUniversity of Utah: The University of Utah (also referred to as the U, U of U, or Utah) is a public coeducational space-grant research university in Salt Lake City, Utah, United States.  As the state's flagship university, the university offers more than 100 undergraduate majors and more than 92 graduate degree programs.  The university is classified in the highest ranking: \"R-1: Doctoral Universities – Highest Research Activity\" by the Carnegie Classification of Institutions of Higher Education.  The Carnegie Classification also considers the university as \"selective\", which is its second most selective admissions category.  Graduate studies include the S.J. Quinney College of Law and the School of Medicine, Utah's only medical school.  As of Fall 2015, there are 23,909 undergraduate students and 7,764 graduate students, for an enrollment total of 31,673.\n\nSt. John's School (Texas): St. John's School (also known as St. John's or SJS) is a coeducational independent school in Houston, Texas, United States, presenting a 13-year sequence of university preparatory training.  The School was founded in 1946 and is a member of the Houston Area Independent Schools, the Independent Schools Association of the Southwest (ISAS), and the Southwest Preparatory Conference (SPC).  Though situated adjacent to St. John the Divine church, St. John's claims no religious affiliation.  It has been coeducational since its founding and has produced many notable alumni.  Noted for its selectivity and academic rigor, St. John's has been described by Forbes.com as one of \"America's Elite Prep Schools\" and listed by the \"Wall Street Journal\" as among schools in the United States with the largest percentages of graduates attending a handful of highly selective universities.\n\nQueen Elizabeth Grammar School, Penrith: Queen Elizabeth Grammar School (QEGS) is a coeducational selective grammar school in Penrith, Cumbria, England.\n\nSt. Ignatius College Prep: Saint Ignatius College Prep is a selective private, coeducational Jesuit high school located in the Near West Side neighborhood of Chicago, Illinois.  The school was founded in Chicago in 1869 by Fr.  Arnold Damen, S.J., a Belgian missionary to the United States.  The school is coeducational, Catholic, college preparatory, and sponsored by the Society of Jesus (the Jesuits).  The school enjoys a strong academic reputation within a faith-supportive school community.\n\nGerald Phizackerley: He was educated at Queen Elizabeth Grammar School, Penrith, University College, Oxford and Wells Theological College and ordained in 1955.  After a curacy at St Barnabas, Carlisle he was Chaplain of Abingdon School.  He was Rector of Gaywood from 1964 to 1978; and Rural Dean of Lynn from 1968 to 1978 before his time as Archdeacon and Priest in charge of Ashford-in-the-Water afterwards.\n\nParramatta High School: Parramatta High School (PHS) is a public, partially selective, co-educational high school located in Parramatta, a western suburb of Sydney, New South Wales, Australia.  Established in 1913, the school was the first co-educational school in the Sydney metropolitan area and was previously a selective high school.  Since 2010, it has been partially selective in the Parramatta region with a multicultural student base.  The school offers a broad curriculum including elective subjects, Vocational Education, and TAFE options for the Higher School Certificate.  The school is operated by the New South Wales Department of Education and Communities and has approximately 850 students in Years 7 to 12.\n\nSelective school (New South Wales): Selective schools in New South Wales, Australia are government high schools operated by the New South Wales Department of Education and Communities that have accepted their students based upon their academic merit.  Each year, approximately 13,000 Year 6 students from across the state of New South Wales optionally undertake the Selective High Schools Test to seek one of the 3,600 places offered for first-year entry into selective high schools.  For Years 8 to 12 entry into selective schools, students do not take an external test, but apply directly to a school for entry.  The application package is common to all government selective schools, with internal selection committees considering applications each year in August–September.\n\nQuestion: What is a coeducational selective grammer school and once schooled Gerald Phizackerley?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"school_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the school.\"\n    },\n    \"school_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of school, e.g., 'grammar school'.\"\n    },\n    \"is_coeducational\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the school is coeducational.\"\n    },\n    \"is_selective\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the school is selective.\"\n    },\n    \"notable_alumnus\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person schooled at this institution.\"\n    }\n  },\n  \"required\": [\n    \"school_name\",\n    \"school_type\",\n    \"is_coeducational\",\n    \"is_selective\",\n    \"notable_alumnus\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "school_name": {
        "type": "string",
        "description": "The name of the school."
      },
      "school_type": {
        "type": "string",
        "description": "The type of school, e.g., 'grammar school'."
      },
      "is_coeducational": {
        "type": "boolean",
        "description": "Indicates if the school is coeducational."
      },
      "is_selective": {
        "type": "boolean",
        "description": "Indicates if the school is selective."
      },
      "notable_alumnus": {
        "type": "string",
        "description": "The name of the person schooled at this institution."
      }
    },
    "required": [
      "school_name",
      "school_type",
      "is_coeducational",
      "is_selective",
      "notable_alumnus"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
