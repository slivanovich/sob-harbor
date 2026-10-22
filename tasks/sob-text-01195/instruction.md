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
Henry Hammond (footballer): Henry Edward Denison Hammond (26 November 1866 – 16 June 1910) was an English footballer who played as a Right back.  Hammond played club football for Oxford University and earned one cap for the national team in 1889.  After his football career ended, Hammond became a folk music historian.

Occupational closure: In sociology, an occupational closure (or professional demarcation) is the process whereby a trade or occupation transforms itself into a true profession by closing off entry to the profession to all but those suitably qualified.  The profession then becomes closed to entry from outsiders, amateurs and the unqualified.  This can be achieved by licensure, through barring entry to all except those who have passed certain entrance examinations and grades of training, or by allowing entry only to those who have gained membership of a specific professional body.  In most professions all three methods are in regular use.  What this means in practical terms, is that an architect or physician, for example, will firstly be a university graduate in their main subject, second, will have passed entrance examinations to join a recognised professional body and thirdly, will also be licensed to practise medicine or architecture, usually also obtained through sitting examinations.  Therefore, such professions are open only to those who satisfy these requirements and are closed to everyone else.  It is thus illegal for any other person to practice medicine or to pose as an architect.

Eileen Power: Eileen Edna LePoer Power (9 January 18898 August 1940) was a British economic historian and medievalist.

Bona of Pisa: Bona of Pisa (c. 1156–1207) was a member of the Third order of the Augustinian nuns who helped lead travellers on pilgrimages.  In 1962, she was canonized a saint in the Catholic Church by Pope John XXIII.  She is considered the patron saint of travellers, and specifically couriers, guides, pilgrims, flight attendants, and the city of Pisa.

Professional: A professional is a member of a profession or any person who earns their living from a specified professional activity.  The term also describes the standards of education and training that prepare members of the profession with the particular knowledge and skills necessary to perform their specific role within that profession.  In addition, most professionals are subject to strict codes of conduct, enshrining rigorous ethical and moral obligations. Professional standards of practice and ethics for a particular field are typically agreed upon and maintained through widely recognized professional associations, such as the IEEE.  Some definitions of "professional" limit this term to those professions that serve some important aspect of public interest and the general good of society.

Edward Denison (bishop): Edward Denison the elder (1801–1854) was an English bishop of Salisbury.

Edward Compton (cricketer): Edward Denison Compton (11 April 1872 – 11 October 1940) played first-class cricket for Somerset and Oxford University between 1894 and 1907.  He was born at Frome, Somerset and died at Rye, East Sussex.

Edward Denison Ross: Sir Edward Denison Ross (6 June 1871 – 20 September 1940) was an Orientalist and linguist, specializing in languages of the Far East.  He could read 49 languages, and speak 30 of them.  He was director of the British Information Bureau for the Near East.  Along with Eileen Power, he wrote and edited a 26 volume series published by George Routledge & Sons, The Broadway Travellers.  The series included the diary of the 17th century naval chaplain Henry Teonge.  In 1934 Edward Denison Ross attended Ferdowsi Millenary Celebration in Tehran.

Edward D. Easton: Edward Denison Easton (1856-1915) was the founder and president of the Columbia Phonograph Company.  Under Easton's leadership, Columbia developed from one of many regional subsidiaries of the North American Phonograph Company to one of the United States' three major record companies (along with Edison Records and Victor Talking Machine Co.) in the early part of the 20th century.

Edward Denison (philanthropist): Edward Denison (September 1840–26 January 1870) was an English philanthropist, known for his self-denying benevolent labours in the East End of London and a Liberal politician who sat in the House of Commons from 1868 to 1870.

Question: What was the profession of the person who helped Edward Denison Ross write The Broadway Travellers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose profession is being identified."
    },
    "profession": {
      "type": "string",
      "description": "The profession of the identified person."
    },
    "collaboration_details": {
      "type": "object",
      "properties": {
        "collaborator_name": {
          "type": "string",
          "description": "The name of the person with whom the identified person collaborated."
        },
        "work_title": {
          "type": "string",
          "description": "The title of the work they collaborated on."
        }
      },
      "required": [
        "collaborator_name",
        "work_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "profession",
    "collaboration_details"
  ],
  "additionalProperties": false
}
