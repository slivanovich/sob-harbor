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
Bernard Bate: Bernard Bate (1960 - 2016) was a linguistic anthropologist specializing in the Tamil language and the history of public speaking, and professor of anthropology at Yale University and at Yale-NUS College.  His best known work was the book "Tamil Oratory and Dravidian Aesthetic: Democratic Practice in South India" which describes the emergence of a tradition of public speaking in the Tamil language during the Indian independence movement.  He received his PhD in anthropology from the University of Chicago.  He taught at Yale for ten years before moving to the Yale-NUS College in Singapore, where he was instrumental in the development of the college's programs.  Bate died in his sleep on 11 March 2016.

Public speaking: Public speaking (also called oratory or oration) is the process or act of performing a speech to a live audience.  This type of speech is deliberately structured with three general purposes: to inform, to persuade and to entertain.  Public speaking is commonly understood as formal, face-to-face speaking of a single person to a group of listeners.

Brandon Learning Centre: The Brandon Learning Centre is the first school in Hong Kong to offer public speaking classes based around English Speaking Board assessments.  The English Speaking Board was founded in 1954 and the qualifications are regulated by the UK Office of Qualifications and Examinations Regulation <ref>

Florian Brody: Florian Brody is an Austrian/American digital media creator, inventor, writer, public speaker, academic, and global business consultant.  He is best known for his contributions to the invention and development of Expanded Books, an early form of E-books, at the Voyager Company, and for his writings and public speaking about digital media innovation and marketing, including multiple TEDx talks in Austria, as well as his 1999 essay "The Medium is the Memory," originally published in MIT Press's "The Digital Dialectic: New Essays on New Media", edited by Peter Lunenfeld.  Brody currently serves as principal at The Halo Agency, which supports European start-up businesses looking to enter the US market by counseling them on cultural and economic differences between their countries and the United States.

Public Speaking and Influencing Men in Business: Public Speaking and Influencing Men In Business (ISBN  ) is a public speaking book written by Dale Carnegie in 1937 and first published in 1926 as "Public Speaking: a Practical Course for Business Men", with several revised editions published later.  Dorothy Carnegie produced 2 separate revised editions: "How to Develop Self-Confidence and Influence People by Public Speaking" (1956), aimed at the general public, and "The Quick and Easy Way to Effective Speaking" (1962), as a replacement textbook for the Dale Carnegie Course.  A more recent revised edition is "Public Speaking for Success" (2005), revised by Arthur Pell, which restores content that was left out of the Dorothy Carnegie-revised works.

University of the South Pacific Solomon Islands: The University of the South Pacific (USP) Solomon Islands is a university campus of the University of the South Pacific, based in Honiara, Solomon Islands; apart from the Honiara Solomon Islands College of Higher Education (SICHE) a university in Honiara; and the Woodford International School.  The University of the South Pacific campus is located near Chinatown, about 75 m to the southwest of Lawson Tama Stadium.  It offers continuing and community education courses to the South Pacific member countries.  Some of the major disciplines in which courses are offered on semester basis are Arts, Law and Education, Business and Economics, Science, Technology and Environment and other disciplines with a gamut of subjects in each discipline.  The duration of courses varies from 10 to 32 hours of teaching spread over a number of weeks.  Subjects taught based on regional requirements could be in the fields of "computer skills, languages, bookkeeping, mathematics, business studies, economics, creative writing, community development skills, literature, handicrafts, floral arts, fabric arts, woodcarving, fine arts, carving, poetry, music, video production, leadership skills, health studies, public speaking, problem-solving and general literacy skills.”  An important programme that is advocated in the USP is to establish an education programme "through distance and flexible learning”, which the relevant texts to learn and teach are prepared in the Laucala Campus in Fiji and adopted in the campuses of all the USP universities across the South Pacific.

Nate Holzapfel: Nate Holzapfel (born Nathanael Reid Holzapfel, February 5, 1979) is an American entrepreneur most known for his appearance on ABC’s Shark Tank, where he successfully pitched the Mission Belt Co.  He has since gone on to pursue a career in consulting and public speaking, and contributes frequently to The Huffington Post as a business and motivational writer.

Dale Carnegie: Dale Harbison Carnegie ( ; spelled Carnagey until c. 1922; November 24, 1888 – November 1, 1955) was an American writer and lecturer and the developer of famous courses in self-improvement, salesmanship, corporate training, public speaking, and interpersonal skills.  Born into poverty on a farm in Missouri, he was the author of "How to Win Friends and Influence People" (1936), a bestseller that remains popular today.  He also wrote "How to Stop Worrying and Start Living" (1948), "Lincoln the Unknown" (1932), and several other books.

Warwick Speakers: Warwick Speakers is a public speaking society at the University of Warwick.  The society specialises in training students in improving their speaking skills before an audience.  From 2005-07, the Society was a Toastmasters International Gavel Club, before regaining membership in 2012.

Moonlighter Presents: Moonlighter Presents is a lecture series based in Brooklyn, New York dedicated to non-expertise and the art of public speaking.  Founded in September 2010, the series evolved as a reaction to the increased emphasis on professionalization in academia and the art world.  Event organizers invite scholars and professionals to address topics outside their fields of expertise or consider their work from unusual perspectives.  There are no topics or themes.  Participants are free to invent roles for themselves and to tamper with traditional lecture formatting.  Lectures have, for the most part, been held in an old funeral home in Williamsburg.  They have also taken place in other non-traditional speaking venues, such as a former Catholic high school in Soho, a bar in Greenpoint, and a corporate office space in Manhattan.

Question: When was the writer of "Public Speaking and Influencing Men In Business" born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author of the book."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book in question."
    },
    "author_birth_date": {
      "type": "string",
      "description": "The full birth date of the author."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the author."
    },
    "birth_month": {
      "type": "string",
      "description": "The birth month of the author."
    },
    "birth_day": {
      "type": "integer",
      "description": "The birth day of the author."
    }
  },
  "required": [
    "author_name",
    "book_title",
    "author_birth_date",
    "birth_year",
    "birth_month",
    "birth_day"
  ],
  "additionalProperties": false
}
