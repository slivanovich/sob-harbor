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
Rochester Institute of Technology Croatia: Rochester Institute of Technology Croatia, or formerly known as the American College of Management and Technology (ACMT) is a college of the Rochester Institute of Technology located in Dubrovnik, and in Zagreb, Croatia.  It is the only school in the country which grants both American and Croatian degrees.  Instruction is in English.

University of Bridgeport: The University of Bridgeport, commonly referred to as UB, is a private, independent, non-sectarian, coeducational National university located on the Long Island Sound in the South End neighborhood of Bridgeport, Connecticut.  The University is fully accredited by the New England Association of Schools and Colleges (NEASC-CIHE).  The University is known for its diverse student population, currently ranking as the tenth most racially diverse national university in the country by "U.S. News & World Report".  The students of the University of Bridgeport are from 80 countries and 46 states.  In 2010, the percentage of students graduating that had participated in an English as a foreign or second language (ESL) program was one of the nation's highest at 5%.

List of private universities in India: The higher education system in India include both private and public universities.  Public universities are supported by the Government of India and the state governments, while private universities are mostly supported by various bodies and societies.  Universities in India are recognized by the University Grants Commission (UGC), which draws its power from the "University Grants Commission Act, 1956".  In addition, 15 Professional Councils are established, controlling different aspects of accreditation and coordination.  Private universities in India are regulated under the UGC (Establishment and Maintenance of Standards in Private Universities) Regulations, 2003.  Per the UGC act and these regulations, private universities are established by an act of a local legislative assembly and listed by the UGC in the Gazette upon receiving the act.  As confirmed by ruling of the Supreme Court of India, recognition by the UGC is required for the university to operate.  Also per the 2003 regulations, the UGC sends committees to inspect the private universities and publishes their inspection report.

Mark W. Ellingson: Mark Ellingson (1905 – 1993) was the 5th president of the Rochester Institute of Technology, succeeding John A. Randall, from 1936 – 1969.  He rose from a teacher at the institute to the presidency, which he held for longer than anyone before or since, and in many ways he brought the institute into its modern form.  During Dr. Ellingson's lengthy tenure in office from 1936 to 1969, enrollment in day and evening classes rose from 2,250 to 16,000.  He also oversaw a major expansion of the RIT endowment; a 1937 merger with the Empire School of Printing; the 1944 renaming to "Rochester Institute of Technology" (formerly, Rochester Athenaeum and Mechanics Institute); the planning, construction, and 1968 transfer to the current campus in Henrietta.  He also spearheaded the drive to have RIT selected as the location for the National Technical Institute for the Deaf, which admitted its first students in 1968.

RIT Kosovo: The Rochester Institute of Technology Kosovo (or formerly known as the American University in Kosovo, RIT/AUK) is a private university located in the Germia district of Pristina, Kosovo.  The university was established in 2002 and is part of the Rochester Institute of Technology (RIT) in Rochester, New York.

Rochester Institute of Technology - Dubai: Rochester Institute of Technology - Dubai (RIT Dubai) is a satellite campus of Rochester Institute of Technology, New York, USA in Dubai, United Arab Emirates.  The college, is located in the Dubai Silicon Oasis and started offering part-time graduate courses in Fall 2008.  In 2009, the university began its full-time graduate program.  RIT Dubai's first graduating class was in 2010, with the graduation ceremony taking place in Rochester, NY.  In 2010, a full-time undergraduate program was started as part of the university's planned expansion.  In the fall of 2011, RIT Dubai moved its campus to a new premises to accommodate the growing student body.  By 2019, RIT plans to expand the campus to 1000000 sqft to provide facilities for 4,000 students.

Rochester Institute of Technology: Rochester Institute of Technology (RIT) is a private doctoral university within the town of Henrietta in the Rochester, New York metropolitan area.

Tora-Con: Tora-Con is an annual two-day anime convention held during April at the Rochester Institute of Technology in Rochester, New York.  The conventions name comes from the Japanese word 'tora' meaning tiger and is organized by the Rochester Institute of Technology Anime Club.  The event is family friendly.

Sandip University, Sijoul: Sandip University, Sijoul is a private university located in Sijoul, Madhubani district, Bihar, India.  The university was established in 2017 by Sandip Foundation under the "Bihar Private Universities Act, 2013", one of the two first private universities in Bihar, the other being K. K. University.  Both universities were approved by the Bihar Government in May 2017 following the passing of "Private Universities (Amendment) Bill, 2017" in March 2017 which relaxed the rules for establishment of private universities in Bihar.  This decision gave autonomous status to what was previously the Sandip Foundation Sijoul campus which houses the Shri.  Nityanand Jha College of Education (SNJCOE) and the Shri Ram Polytechnic (SRP).  This is the second university to be established by the foundation, following the establishment Sandip University, Nashik in 2015.

K. K. University: K. K. University (KKU) is a private university located in Beraunti, near Bihar Sharif in Nalanda district, Bihar, India.  The university was established in 2017 by Samajik Kalyan Sanstha under the "Bihar Private Universities Act, 2013", one of the two first private universities in Bihar, the other being Sandip University, Sijoul.  Both universities were approved by the Bihar Government in May 2017 following the passing of "Private Universities (Amendment) Bill, 2017" in March 2017 which relaxed the rules for establishment of private universities in Bihar.

Question: Are University of Bridgeport and Rochester Institute of Technology both private universities?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_private": {
      "type": "boolean",
      "description": "True if both universities are private, false otherwise."
    },
    "universities_checked": {
      "type": "array",
      "description": "Details for each university checked for its private status.",
      "items": {
        "type": "object",
        "properties": {
          "university_name": {
            "type": "string",
            "description": "The name of the university."
          },
          "is_private": {
            "type": "boolean",
            "description": "True if the university is private, false otherwise."
          }
        },
        "required": [
          "university_name",
          "is_private"
        ],
        "additionalProperties": false
      }
    },
    "reasoning_summary": {
      "type": "string",
      "description": "A summary of the reasoning for the answer."
    }
  },
  "required": [
    "is_both_private",
    "universities_checked",
    "reasoning_summary"
  ],
  "additionalProperties": false
}
