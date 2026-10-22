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
Peter Beilharz: Peter Beilharz (born 13 November 1953, Melbourne, Australia) is an Australian sociologist.  He is currently Professor of Culture and Society at Curtin University, Perth, Western Australia.  Previously he was Professor of Sociology at La Trobe University, Melbourne.  Beilharz is also a co-founder and editor of the international journal of social theory "Thesis Eleven" published by Sage.

Stephen K. Sanderson: Stephen K. Sanderson (born November 15, 1945) is an American sociologist.  His area of focus includes comparative sociology, historical sociology, sociological theory and sociocultural evolution.  He is a specialist in sociological theory and comparative and historical sociology and is one of the leading sociologists to develop a Darwinian understanding of human society.  He has written or edited ten books and about sixty peer-reviewed articles, and is the author of numerous articles and many books, including Evolutionism and Its Critics.

Critical theory: Critical theory (or "social critical theory") is a school of thought that stresses the reflective assessment and critique of society and culture by applying knowledge from the social sciences and the humanities.  As a term, "critical theory" has two meanings with different origins and histories: the first originated in sociology and the second originated in literary criticism, whereby it is used and applied as an umbrella term that can describe a theory founded upon critique; thus, the theorist Max Horkheimer described a theory as critical insofar as it seeks "to liberate human beings from the circumstances that enslave them".

Omar Lizardo: Omar Lizardo (born 1974) is a sociologist, Professor of Sociology at the University of Notre Dame, and the co-editor, with Rory McVeigh and Sarah Mustillo, of the American Sociological Review, the flagship journal for the American Sociological Association.  According to one commentator, he "has a history of grappling with important ideas in an innovative and insightful fashion" and is a widely cited author in numerous sub-fields of sociology.  He is specifically known for his work at the intersection of cognitive science and sociology of culture, but also social networks, organizational sociology and sociological theory.  He is a regular contributor to the popular sociology group blog, orgtheory.net.  Among many other accolades, in 2013 he won the Lewis Coser Award for Theoretical Agenda Setting and in 2014, the Charles Tilly Best Article Award for Comparative and Historical Sociology.

Journal of Historical Sociology: This peer-reviewed journal is edited by an international panel of historians, anthropologists, geographers and sociologists, the "Journal of Historical Sociology" is both interdisciplinary in approach and innovative in content.  The "Journal of Historical Sociology" was founded in 1988 and presents review essays and commentary in its "Issues and Agendas" section, and aims to provoke discussion and debate.

Georgy Fotev: Georgy Fotev (Bulgarian: Георги Фотев ) (born August 24, 1941) is a Bulgarian sociologist.  His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology.  The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science.  Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology.  Georgy Fotev has publications in the fields of historical sociology, sociology of politics, ethnosociology, the crisis of legitimacy, sociology of values, etc.  His books "The long night of communism in Bulgaria" and "Bulgarian melancholy" throw light on the dramatic fate of the Bulgarian national society.  Georgy Fotev was Minister of Education and Science (1991 - 1992).  He is professor emeritus of New Bulgarian University.  In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria.

György Márkus: György Márkus (13 April 1934 – 5 October 2016) was a Hungarian philosopher, belonging to the small circle of critical theorists closely associated with György Lukács, usually referred to as the "Budapest School".  He completed his philosophical training at Lomonosov University in Moscow in 1957.  Due to ideological disputes, he was removed from his teaching positions in Hungary in 1973, and fled in 1977 to Australia, where from 1978 he taught at the University of Sydney.  Following political liberalisation in Hungary, Markus was reassimilated and taught regularly in his homeland, although he remained resident in Sydney.  He was external member of the Hungarian Academy of Sciences (1990).  He was also on the editorial board of the academic journal "Thesis Eleven: Critical Theory and Historical Sociology".

La Trobe University: La Trobe University is an Australian, multi-campus, public research university with its flagship campus located in the Melbourne suburb of Bundoora.  The university was established in 1964, becoming the third university in the state of Victoria and the twelfth university in Australia.  La Trobe is a verdant university and a member of the Innovative Research Universities.

Critical international relations theory: Critical international relations theory is a diverse set of schools of thought in international relations (IR) that have criticized the theoretical, meta-theoretical and/or political status quo, both in IR theory and in international politics more broadly — from positivist as well as postpositivist positions.  Positivist critiques include Marxist and neo-Marxist approaches and certain ("conventional") strands of social constructivism.  Postpositivist critiques include poststructuralist, postcolonial, "critical" constructivist, critical theory (in the strict sense used by the Frankfurt School), neo-Gramscian, most feminist, and some English School approaches, as well as non-Weberian historical sociology, "international political sociology", "critical geopolitics", and the so-called "new materialism" (partly inspired by actor–network theory).  All of these latter approaches differ from both realism and liberalism in their epistemological and ontological premises.

Thesis Eleven: Thesis Eleven: Critical Theory and Historical Sociology is a peer-reviewed academic journal that publishes papers four times a year in the field of Sociology.  The journal's editors are Peter Beilharz (La Trobe University, Victoria (Australia)), Trevor Hogan (La Trobe University) and Peter Murphy (Monash University, Melbourne, Victoria).  It has been in publication since 1980 and is currently published by SAGE Publications.

Question: Two of the editors of the journal Thesis Eleven: Critical Theory and Historical Sociology are affiliated with a university founded in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "journal_name": {
      "type": "string",
      "description": "The name of the academic journal."
    },
    "affiliated_university_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the university affiliated with the journal editors."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the university was established."
        }
      },
      "required": [
        "name",
        "founding_year"
      ],
      "additionalProperties": false
    },
    "editors_from_affiliated_university": {
      "type": "array",
      "description": "A list of editors of the journal who are affiliated with the specified university.",
      "items": {
        "type": "object",
        "properties": {
          "editor_name": {
            "type": "string",
            "description": "The name of the editor."
          },
          "role": {
            "type": "string",
            "description": "The role of the person (e.g., editor)."
          }
        },
        "required": [
          "editor_name",
          "role"
        ],
        "additionalProperties": false
      }
    },
    "answer_founding_year": {
      "type": "integer",
      "description": "The final answer to the question: the founding year of the university."
    }
  },
  "required": [
    "journal_name",
    "affiliated_university_details",
    "editors_from_affiliated_university",
    "answer_founding_year"
  ],
  "additionalProperties": false
}
