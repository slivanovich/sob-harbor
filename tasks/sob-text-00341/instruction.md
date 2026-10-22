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
American Journal of Sociology: The American Journal of Sociology was established in 1895 by Albion Small and is the oldest academic journal of sociology in the United States.  The journal is attached to the University of Chicago's sociology department and it is published bimonthly by The University of Chicago Press.  Its editor-in-chief is Elisabeth Clemens (University of Chicago).  The journal presents work on the theory, methods, practice, and history of sociology.  It also publishes sociology-related papers by scholars from outside sociology, speaking to sociologists, social scientists, and the general sociological reader.  According to the "Journal Citation Reports", the journal has a 2015 impact factor of 2.574, ranking it 7th out of 142 journals in the category "Sociology".

Poverty, A Study of Town Life: Poverty, A Study of Town Life is the first book by the sociological researcher, social reformer and industrialist, Seebohm Rowntree, published in 1901.  The study, widely considered a seminal work of sociology, details Rowntree's investigation of poverty in York, England and the subsequent implications that arise from the findings, in regard to the nature of poverty at the start of the 20th century.  It also marks the first usage of a poverty line in sociological research.

The Souls of Black Folk: The Souls of Black Folk is a classic work of American literature by W. E. B. Du Bois.  It is a seminal work in the history of sociology, and a cornerstone of African-American literary history.

Georgy Fotev: Georgy Fotev (Bulgarian: Георги Фотев ) (born August 24, 1941) is a Bulgarian sociologist.  His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology.  The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science.  Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology.  Georgy Fotev has publications in the fields of historical sociology, sociology of politics, ethnosociology, the crisis of legitimacy, sociology of values, etc.  His books "The long night of communism in Bulgaria" and "Bulgarian melancholy" throw light on the dramatic fate of the Bulgarian national society.  Georgy Fotev was Minister of Education and Science (1991 - 1992).  He is professor emeritus of New Bulgarian University.  In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria.

Omar Lizardo: Omar Lizardo (born 1974) is a sociologist, Professor of Sociology at the University of Notre Dame, and the co-editor, with Rory McVeigh and Sarah Mustillo, of the American Sociological Review, the flagship journal for the American Sociological Association.  According to one commentator, he "has a history of grappling with important ideas in an innovative and insightful fashion" and is a widely cited author in numerous sub-fields of sociology.  He is specifically known for his work at the intersection of cognitive science and sociology of culture, but also social networks, organizational sociology and sociological theory.  He is a regular contributor to the popular sociology group blog, orgtheory.net.  Among many other accolades, in 2013 he won the Lewis Coser Award for Theoretical Agenda Setting and in 2014, the Charles Tilly Best Article Award for Comparative and Historical Sociology.

Sociology of sociology: Sociology of sociology is an area of sociology that combines social theories with analysis of the effect of socio-historical contexts in sociological intellectual production.  For the French sociologist Pierre Bourdieu, the task of the sociology of sociology is to debrief accepted truths, focusing on the questioning of canons and acting towards new epistemologies.  In the history of British sociology, A. H. Halsey suggests an evoking connection between political economic regimes in the 20th century and the development of sociology as an academic discipline.

Victor Lieberman: Victor B. Lieberman (born 22 July 1945) is an historian of early modern Southeast Asia and Eurasia.  He presently serves as the Raoul Wallenberg Distinguished University Professor of History and Professor of Asian and Comparative History at the University of Michigan, where he began teaching in 1984.  That year he published a seminal work, "Burmese Administrative Cycles: Anarchy and Conquest, c.1580-1760" (Princeton University Press), which profoundly impacted scholarship on mainland Southeast Asia through an analysis of alternating governance patterns in 16th- to 18th-century Burma.  Totaling some 1500 pages, his more recent two-volume study "Strange Parallels: Southeast Asia in Global Context, c. 800-1830" (Cambridge University Press) argued that in terms of basic dynamics, chronology, and trajectory, patterns of political and cultural integration in mainland Southeast Asia over several centuries resembled those in much of Europe and Japan, and to a lesser extent, in China and South Asia.  A lead featured review in "The American Historical Review" in 2012 (vol.  117, no. 4) claimed that "Lieberman's two-volume magnum opus is the most important work of history produced so far this century."  Two international conferences, in London and Osaka, have been held to discuss Lieberman's scholarship, and each of the two chief journals of Asian studies, "Modern Asian Studies" (1997) and "The Journal of Asian Studies" (2011), has devoted a special edition to his work.  In 2014 he won the Golden Apple Award, conferred by student ballot, as the best teacher at the University of Michigan.

Towards a Sociology of the Novel: Towards a Sociology of the Novel (French: "Pour une sociologie du roman" ) is a 1963 book by Lucien Goldmann.  The book was a seminal work for Goldmann.  In it, he lays out his theory of the novel.

Akosua Adoma Owusu: Akosua Adoma Owusu (born January 1, 1984) is a Ghanaian-American avant-garde filmmaker and producer whose films have screened worldwide in prestigious film festivals, museums, galleries, universities and microcinemas since 2005.  “Owusu uses various production techniques to visualize a state of "triple consciousness", a term she coined in reference to a central tenet of the sociologist and civil rights activist W. E. B. Du Bois’s landmark text "The Souls of Black Folk" (1903).  Du Bois' double consciousness accounts for the experience of black Americans negotiating a sense of selfhood in the face of discrimination and cultural dislocation.  As part of the first generation in her family to be born in the United States, Owusu extends Du Bois’s concept to speak to the crisis of heritage and assimilation for African expatriates and their US-born children."  Owusu has stated that “instead of ‘Africanizing’ Western stories, I’m interested in reclaiming African history rendering them into what is happening in the present day.”

John Grady (sociologist): John Marshall Grady (born 1950s) is an American sociologist, and Professor of Sociology at Wheaton College, known for his seminal work in the field of visual sociology.

Question: Owusu referenced what seminal work from the history of sociology?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "referenced_work": {
      "type": "string",
      "description": "The title of the seminal work referenced."
    },
    "author": {
      "type": "string",
      "description": "The author of the referenced work."
    },
    "significance": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Key areas of significance or impact of the referenced work."
    }
  },
  "required": [
    "referenced_work",
    "author",
    "significance"
  ],
  "additionalProperties": false
}
