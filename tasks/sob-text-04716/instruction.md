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
Matt Hyde: Matt Hyde (born June 19, 1964) is an American producer, engineer, mixer and musician.  From 1982 to 1985 he attended Berklee College of Music in Boston.  While still at Berklee (1984) he obtained an internship at Pyramid Recording Studio in Boston.  After two semesters at Berklee, Hyde took a break from classes to tour for the Department of Defense overseas entertainment program, playing guitar and keyboards in several top 40 cover bands that played shows at U.S. military bases in foreign countries throughout Europe and the Pacific.  When he returned to the U.S., he began working at recording studios, first in Boston and from 1989 in Los Angeles.

Matthew Sweet: Sidney Matthew Sweet (born October 6, 1964) is an American rock singer-songwriter and musician.  He was part of the burgeoning music scene in Athens, Georgia, during the 1980s before gaining commercial success in the 1990s.  His twelfth album, "Tomorrow Forever", was released in June 2017.

Berklee Performance Center: The Berklee Performance Center is a 1,215-seat theatre located on Massachusetts Ave. in the Back Bay area of Boston, Massachusetts.  It is the largest theatre space on the Berklee College of Music campus and is used primarily for college-affiliated activities.  Presenters from outside the Berklee community also rent it for performances of all kinds.  In 2009, the Berklee Performance Center hosted a total of 200 events.

Lee Eliot Berk: Lee Eliot Berk (born 1942) was President and namesake of the Berklee College of Music (founded as Schillinger House in 1945 by his father, Lawrence Berk, who renamed the school after Lee in 1954) from 1979 to 2004.  Under the younger Berk’s leadership, the college underwent significant changes.  Berklee expanded its curriculum to create new majors, including Film Scoring, Music Production and Engineering, Music Synthesis, Songwriting, Music Business/Management, and Music Therapy.  Educational applications of music technology expanded, the college administration was reorganized, more student services were added, and non-music academic offerings increased.  In 1992, he established the Berklee International Network that includes music schools with a shared mission around the globe.

Berklee College of Music: Berklee College of Music, located in Boston, Massachusetts, United States, is the largest independent college of contemporary music in the world.  Known for the study of jazz and modern American music, it also offers college-level courses in a wide range of contemporary and historic styles, including rock, flamenco, hip hop, reggae, salsa, and bluegrass.  Since 2012, Berklee College of Music has also operated a campus in Valencia, Spain.

Berklee method: In music performance and education, the Berklee method is the music theory, terminology, and practice taught at Berklee College of Music, the largest independent college of contemporary music in the world.  The "Berklee method" was founded by Lawrence Berk after study with Joseph Schillinger regarding the latter's, "elaborate system of composition that employed mathematical permutation and combination process to generate rhythms, harmonies, and melodies".  Later, attempting to codify jazz and popular music practice, the Berklee method often differs from common practice harmony and voice-leading rules or guidelines.

Birth in Reverse: "Birth in Reverse" is a song written and performed by St. Vincent, issued as the lead single from her fourth album, "St. Vincent".  A video featuring the audio was released on  9, 2013 (2013--) , one day prior to the single's official release.  A music video was released on December 16, 2014.  On  17, 2014 (2014--) , St. Vincent performed the song on the season finale of "Saturday Night Live".

St. Vincent Declaration: The St. Vincent Declaration is a set of goals for the health care of people with diabetes mellitus published as the product of an international conference held in St. Vincent, Italy, on 10–12 October 1989.  Representatives of government health departments and patients' organizations from all European countries met with diabetes experts under the aegis of the World Health Organization (WHO) Europe and the International Diabetes Federation (IDF) Europe.  General standards for diabetes care were agreed on, as well as plans for improving care in participating countries toward the goals.  Twenty years later, in 2009, it was stated in an editorial in the British Journal of Diabetes and Vascular Disease that 'despite the progress made following the St. Vincent Declaration and the UN Resolution, significant gaps still exist and urgent action is needed to stem this rising epidemic'.

Shirish Korde: Shirish Korde (born June 18, 1945), is a composer who was born in Uganda to Indian parents.  He is the Chair of the Music Department at the College of the Holy Cross (Worcester, MA) and has previously been on the faculty of the Berklee College of Music, the New England Conservatory, and Brown University.  Korde studied jazz and composition at the Berklee College of Music, analysis and composition at the New England Conservatory, and ethnomusicology at Brown University.

St. Vincent (musician): Anne Erin "Annie" Clark (born September 28, 1982), better known by her stage name St. Vincent, is an American musician, singer-songwriter, and multi-instrumentalist.  After studying at Berklee College of Music for three years, she began her music career as a member of the Polyphonic Spree.  Clark was also a member of Sufjan Stevens's touring band before forming her own band in 2006.

Question: Who went to Berklee College of Music for three years, Matthew Sweet or St. Vincent?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_context_institution": {
      "type": "string",
      "description": "The educational institution central to the question."
    },
    "candidates": {
      "type": "array",
      "description": "A list of individuals mentioned in the question as potential attendees.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the candidate."
          },
          "attended_institution": {
            "type": "boolean",
            "description": "True if the candidate attended the institution, false otherwise."
          },
          "duration_of_attendance_years": {
            "type": "integer",
            "description": "The number of years the candidate attended the institution, if specified in the context."
          }
        },
        "required": [
          "name",
          "attended_institution"
        ],
        "additionalProperties": false
      }
    },
    "person_matching_criteria": {
      "type": "string",
      "description": "The name of the person who matches the specified attendance duration at the institution."
    },
    "matched_attendance_duration_years": {
      "type": "integer",
      "description": "The specific duration in years that was matched for the answer."
    }
  },
  "required": [
    "question_context_institution",
    "candidates",
    "person_matching_criteria",
    "matched_attendance_duration_years"
  ],
  "additionalProperties": false
}
