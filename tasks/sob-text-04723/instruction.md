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
American Geriatrics Society: The American Geriatrics Society (AGS) is a professional society founded on June 11, 1942 for physicians practicing geriatric medicine.  Among the founding physicians were Dr. Ignatz Leo Nascher, who coined the term "geriatrics," Dr. Malford W. Thewlis, who was named the first executive secretary of the Society, and Dr. Lucien Stark who was appointed the first AGS president.

Australian Institute of Building: The Australian Institute of Building(AIB) is a professional society founded in 1951, incorporated in 1955 and granted a Royal Charter in 1969.  The Institute is an association of building professionals, associate professionals and technicians engaged in building practice, teaching, or research throughout Australia and overseas.  It has chapter offices in Hong Kong and Singapore and had a chapter office in New Zealand until the formation of the New Zealand Institute of Building in 1984.

Knowledge Management Professional Society: The Knowledge Management Professional Society (KMPro) is a non-profit organization and was founded in 2001 as the main professional body for those working in the broad field of Knowledge Management (KM) throughout the world and it is a society created by KM professionals for KM professionals.  It is the only international, non-profit membership organization in the field of KM.  Its purpose is to encourage the practice of KM, promote best practice and to provide a community for those who are active in KM or who have an interest in KM.  As a professional society KMPro encourages collaboration, co-operation, networking and fellowship amongst individuals working in this field.

Marine Technology Society: The Marine Technology Society (MTS) is a professional society that serves the international community of approximately 3,800 ocean engineers, technologists, policy-makers, and educators.  The goal of the society, which was founded in 1963, is to promote awareness, understanding, advancement and application of marine technology.  The association is based in Washington, District of Columbia, United States.  Former executive directors include Martin Finnerty, Judith T. Krauthamer and Richard Lawson.

David J. Lockwood: David J. Lockwood is a Canadian physicist and Researcher Emeritus at the National Research Council of Canada (NRC).  He is also Adjunct Professor at the University of Windsor in Windsor, Ontario, Editor of the journal Solid State Communications, and Secretary-Treasurer of the Canadian Association of Physicists.  Dr Lockwood is a Fellow of the Royal Society of Canada, the American Physical Society, the Electrochemical Society, and the Institute of Physics.

Canadian Association of Physicists: The Canadian Association of Physicists (CAP), or in French Association canadienne des physiciens et physiciennes (ACP) is a Canadian professional society that focuses on creating awareness amongst Canadians and Canadian legislators of physics issues, sponsoring physics related events, physics outreach, and publishes Physics in Canada.  The organization was founded in 1945 and currently has over 1,600 members.  CAP is bilingual and functions in both English and French.

Tsunami Society: The Tsunami Society, also known as the International Tsunami Society, is a professional society for the research of and dissemination of knowledge about tsunamis.  The society was founded in Honolulu, Hawaii in 1982.  The society sponsors professional level meetings with local government officials to promote public safety awareness, disaster preparedness and the implementation of early warning systems.  Every two years, the society holds its International Scientific Symposium, where researchers and scientists attend sessions at the symposia.

Independent Theatre: The Independent Theatre (from 1934 The Independent Theatre Ltd), was an Australian dramatic society founded in 1930 by Dame Doris Fitton, and was also the name given to the building it occupied from 1938.  It was named for London's Independent Theatre Society founded by J. T. Grein and was one of several amateur drama groups of high standard which sprang up in Sydney, Australia in the 1930s to fill the gap left by the closure of all but two professional theatres (the last spoken-word theatre to close was The Criterion in 1936, leaving only the Tivoli, which ran vaudeville, and the Theatre Royal, which played musicals and ballets).  The range of plays essayed was impressive – from classics to avant-garde pieces, from recent West End and Broadway successes (sometimes the Australian premiere) to offerings from local dramatists.  The death of Doris Fitton's co-producer Peter Summerton in 1969 put extra strain on her deteriorating health, and with no-one able or willing to fill her shoes, the Independent closed in 1977.  It was to reopen in 1998, continuing its tradition as a training ground for young actors and playwrights.

Business History Conference: The Business History Conference is a scholarly organization devoted to encouraging all aspects of research, writing, and teaching about business history and about the environment in which businesses operate.  Founded in 1954, the organization is now international in scope, with approximately 30 percent of its membership residing outside North America.  The BHC is based at the Center for the History of Business, Technology, and Society at the Hagley Library and relies on Center Director Roger Horowitz and Center Coordinator Carol Lockman to manage the BHC's annual meetings, finances, membership, and other business.  Horowitz also serves as the BHC's Secretary-Treasurer and Lockman as Managing Editor of "Enterprise & Society".  In addition to its refereed quarterly journal, "Enterprise & Society", the BHC publishes an online collection of abstracts and selected papers from its annual meeting, "BEH On-Line".  The organization also operates H-Business, one of the earliest H-Net discussion lists, and maintains an on-line full-text archives of its print proceedings journal, "Business and Economic History".  It also publishes The Exchange, a blog devoted to news of interest to business and economic historians.  The BHC holds an annual meeting that provides a forum for discussing current research in business history and related fields and offers an opportunity for people with similar interests to meet and exchange ideas.  Participation from overseas scholars is especially encouraged, and joint meetings with the European Business History Association are held regularly.  The BHC sponsors a number of awards and prizes, including the Hagley Prize in Business History and the Cambridge Journals Article Prize; it endeavors to support scholars entering the field through its travel-to-meeting grants, its Doctoral Dissertation Colloquium, and its Krooss Dissertation Prize.  Sub-groups within the organization promote the interests of women in business history, business historians teaching at business schools, and emerging scholars.

American Society of Mammalogists: The American Society of Mammalogists (ASM) was founded in 1919.  Its primary purpose is to encourage the study of mammals, and professions studying them.  There are over 4,500 members of this society, and they are primarily professional scientists who emphasize the importance of public policy and education.  There are several ASM meetings held each year and the society manages several publications such as "The Journal of Mammalogy", "Special Publications", "Mammalian Species", and "Society Pamphlets".  The most well known of these is "The Journal of Mammalogy".  The ASM also maintains "The Mammal Image Library" which contains more than 1300 mammal slides.  A president, vice president, recording secretary, secretary-treasurer, and journal editor are all elected by the members to be officers of the society.  In addition, ASM is composed of thirty one committees, including the Animal Care and Use Committee, the Conservation Awards Committee, the International Relations Committee, and the Publications Committee.  It also provides numerous grants and awards for research and studies on mammals.  These awards can go to both scientists and students.  The ASM also lists employment opportunities for their members.

Question: David J. Lockwood serves as Secretary-Treasurer of which Canadian professional society founded in 1945?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "society_name": {
      "type": "string",
      "description": "The name of the professional society."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the society was founded."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the society is based or primarily operates."
    },
    "officer_role": {
      "type": "string",
      "description": "The role held by the specified individual in the society."
    },
    "officer_name": {
      "type": "string",
      "description": "The name of the individual holding the officer role."
    }
  },
  "required": [
    "society_name",
    "founding_year",
    "country_of_origin",
    "officer_role",
    "officer_name"
  ],
  "additionalProperties": false
}
