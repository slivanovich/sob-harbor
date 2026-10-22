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
Acta Zoologica: Acta Zoologica is a peer-reviewed scientific journal published by Wiley-Blackwell on behalf of the Royal Swedish Academy of Sciences and the Royal Danish Academy of Sciences and Letters.  It was established in 1920 as Acta Zoologica and obtained its current name in 2002.  It is one of the world's leading zoological journals and focuses on animal development, structure, and function, including physiological organization.  It primarily publishes original research papers, but occasionally also publishes review articles.

Robert Ledley: Robert Steven Ledley (June 28, 1926 – July 24, 2012), Professor of Physiology and Biophysics and Professor of Radiology at Georgetown University School of Medicine, pioneered the use of electronic digital computers in biology and medicine.  In 1959, he wrote two influential articles in "Science": "Reasoning Foundations of Medical Diagnosis" (with Lee B. Lusted) and "Digital Electronic Computers in Biomedical Science".  Both articles encouraged biomedical researchers and physicians to adopt computer technology.  In 1960 he established the National Biomedical Research Foundation (NBRF), a non-profit research organization dedicated to promoting the use of computers and electronic equipment in biomedical research.  At the NBRF Ledley pursued several major projects: the early 1960s development of the Film Input to Digital Automatic Computer (FIDAC), which automated the analysis of chromosomes; the invention of the Automatic Computerized Transverse Axial (ACTA) whole-body CT scanner in the mid-1970s; managing the "Atlas of Protein Sequence and Structure" (created in 1965 by Margaret O. Dayhoff); and the establishment of the Protein Information Resource in 1984.  Ledley also served as editor of several major peer-reviewed biomedical journals.  In 1990, Ledley was inducted into the National Inventors Hall of Fame.  He was awarded the National Medal of Technology in 1997.  He retired as president and research director of the NBRF in 2010.

Alliance for California Traditional Arts: Alliance for California Traditional Arts (ACTA) is a private nonprofit organization that provides advocacy, connections, grants, and other resources for folk and traditional artists in California to preserve the health and longevity of California’s diverse cultural communities.  Amy Kitchener, a public folklorist, is the co-founder, founding director, and current Executive Director.

Mississippi Philosophical Association: The Mississippi Philosophical Association is a philosophical organization whose purpose is to advance the study of philosophy in Mississippi.  The organization sponsors an annual conference.  The association sponsors a student essay contest, where first and second prize winners present papers at the annual conference. " Addresses of the Mississippi Philosophical Association" are published by Rodopi Publishers.

Acta Astronautica: Acta Astronautica is a monthly peer-reviewed scientific journal covering all fields of physical, engineering, life, and social sciences related to the peaceful scientific exploration of space.  The journal was established in 1955 under the name "Astronautica Acta", obtaining its current title in 1974, with volume-numbering simultaneously restarting at 1.  The journal is published by Elsevier, sponsored by the International Academy of Astronautics.

Anne D. Neal: Anne deHayden Neal is the former president of the American Council of Trustees and Alumni (ACTA), a non-profit organization with a stated mission of advancing academic quality, accountability and affordability at colleges and universities in the United States.

International Academy of Astronautics: The International Academy of Astronautics (IAA) is a non-governmental organisation of experts committed to expanding the frontiers of space.  It was established in Stockholm (Sweden) on August 16, 1960.

United States Academic Decathlon: The Academic Decathlon (also called AcaDec, AcaDeca or AcDec) is the only annual high school academic competition organized by the non-profit United States Academic Decathlon Association (USAD).  The competition consists of seven multiple choice tests, two performance events, and an essay.  Academic Decathlon was created by Robert Peterson in 1968 for local schools in Orange County, California and expanded nationwide in 1981 by Robert Peterson, William Patton, first President of the new USAD Board and Phillip Bardos, Chairman of the new USAD Board.  That year, 17 states and the District of Columbia participated, a number that has grown to include most of the United States and some international schools.  Mr. Patton and Mr. Bardos served on the board in these two executive positions for the first 10 years of the USAD and not only personally contributed significantly both financially and in personal effort to the organization in those early day when there were no corporate sponsors they, along with Robert Peterson, were the major three factors in bringing corporate sponsors to the program during these challenging growth years eventually resulting in a financially self sustaining organization.  In 2015 Academic Decathlon held its first ever International competition in Shanghai, China.  Once known as United States Academic Decathlon, on March 1, 2013, it began operating as the Academic Decathlon.

American Council of Trustees and Alumni: The American Council of Trustees and Alumni (ACTA) is an American non-profit organization whose stated mission is to "support liberal arts education, uphold high academic standards, safeguard the free exchange of ideas on campus, and ensure that the next generation receives a philosophically rich, high-quality college education at an affordable price."

Anti-Counterfeiting Trade Agreement: The Anti-Counterfeiting Trade Agreement (ACTA) is a multinational treaty for the purpose of establishing international standards for intellectual property rights enforcement.  The agreement aims to establish an international legal framework for targeting counterfeit goods, generic medicines and copyright infringement on the Internet, and would create a new governing body outside existing forums, such as the World Trade Organization, the World Intellectual Property Organization, and the United Nations.

Question: When was the organization that sponsors Acta Astronautica formed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "journal_name": {
      "type": "string",
      "description": "The name of the scientific journal."
    },
    "sponsoring_organization": {
      "type": "object",
      "properties": {
        "organization_name": {
          "type": "string",
          "description": "The name of the organization that sponsors the journal."
        },
        "establishment_date": {
          "type": "string",
          "description": "The date when the sponsoring organization was established."
        },
        "establishment_location": {
          "type": "string",
          "description": "The location where the sponsoring organization was established."
        }
      },
      "required": [
        "organization_name",
        "establishment_date",
        "establishment_location"
      ],
      "additionalProperties": false
    },
    "answer_date": {
      "type": "string",
      "description": "The final answer to the question: the establishment date of the sponsoring organization."
    }
  },
  "required": [
    "journal_name",
    "sponsoring_organization",
    "answer_date"
  ],
  "additionalProperties": false
}
