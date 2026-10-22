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
Catherine Belsey: Catherine Belsey (born 1940) is a British literary critic and academic.  She chaired the Centre for Critical and Cultural Theory at Cardiff University (1988-2003) before moving to Swansea University (2006–14).  Her book "Critical Practice" (1980) was an influential poststructuralist text in suggesting new directions for literary studies.  She is currently Visiting Professor of English at the University of Derby and Fellow of the English Association and Fellow of the Learned Society of Wales.  She has consistently aligned herself with international innovations in the theory and practice of criticism.

John Beer: John Bernard Beer, FBA (born 31 March 1926) is a British literary critic.  He is Emeritus Professor of English Literature at the University of Cambridge and a Fellow of Peterhouse, Cambridge.  Best known as a scholar and critic of Romantic poets – especially William Blake, Samuel Taylor Coleridge, and William Wordsworth – he has also published on E. M. Forster.  He was elected a Fellow of the British Academy in 1994.

Sergey Andreyevsky: Sergey Arkadievich Andreyevsky (Сергей Аркадьевич Андреевский, December 29, 1847 in Alexandrovka village, Yekaterinoslav Governorate, Russian Empire), – November 9, 1918 in Petrograd, Soviet Russia) was a Russian writer, poet, literary critic and lawyer, best known for his "The Book About Death" (Kniga o smerti), published posthumously in 1922.  As a literary critic Andreevsky is credited with being the first to positively review Fyodor Dostoyevsky.  His essay "Karamazov Brothers" (1888) is regarded as one of the best of its kind.  Andreyevsky did a lot to revive interest in early 19th-century Russian poetry, notably Yevgeny Baratynsky whom he for the first time introduced to the general readership.

Frank Kermode: Sir John Frank Kermode, FBA (29 November 1919 – 17 August 2010) was a British literary critic best known for his work "", published in 1967 (revised 2000), and for his extensive book-reviewing and editing.

Ian Robinson (author): Ian Robinson (born 1937) is a British literary critic and English professor.  He was educated at King Edward VI Grammar School, Retford, and Downing College, Cambridge (he earned firsts in both parts of the English Tripos) where he was a pupil of F. R. Leavis.  Robinson served as lecturer and senior lecturer in the English Department at University College of Swansea from 1961 to 1997 Best known for his 1973 book "The Survival of English", Robinson has been a champion of traditional English literature and a critic of what he alleges to be the degeneration of the English language across all departments of modern life.  With David Sims, he co-founded The Brynmill Press Ltd, in 1970, a company devoted to serious criticism which began with the quarterly review "The Human World" (1970–4) and went on to publish works of literary criticism, philosophy (including Ludwig Wittgenstein’s "Remarks on Frazer’s “Golden Bough”") fiction and poetry.

The Resistance to Theory: "The Resistance to Theory" is an essay by Paul de Man (1919–83), a renowned literary critic and theorist belonging to the Yale School of Deconstruction, which appeared in "Yale French Studies" 63 (1982) and was widely anthologized.  The essay later became part of the book by the same name.  The essay remains a key statement in poststructuralist approaches to literary studies.

The Criterion: The Criterion was a British literary magazine published from October 1922 to January 1939.  "The Criterion" (or the "Criterion") was, for most of its run, a quarterly journal, although for a period in 1927-28 it was published monthly.  It was created by the poet, dramatist, and literary critic T. S. Eliot who served as its editor for its entire run.

The Philosophy of Chance: The Philosophy of Chance, with subtitle ""Literature in the Light of Empiricism"" (Polish: "Filozofia przypadku.  Literatura w świetle empirii" ) is an essay by Polish author Stanisław Lem on the literary theory and the influence of literature on the modern culture.  However, as literary critic Henryk Markiewicz noted, the subtitle is somewhat misleading: starting with Lem's take on literary theory, the essay turns into the "General Theory of Everything": of the Universe, evolution, and culture, based on a premise that chance, eventuality is the universal factor.

Samuel Johnson: A Life: Samuel Johnson: A Life is a prize-winning biography of 18th-century English lexicographer Samuel Johnson by British literary critic David Nokes.  It was published on October 27, 2009, shortly before the author's death.  Building on earlier work by scholars Robert DeMaria, Walter Jackson Bate, Lawrence Lipking and Peter Martin, many critics lauded "Samuel Johnson: A Life" as a significant step forward in Johnsonian biography and criticism.  In the biography, Nokes challenges James Boswell's significance in Dr. Johnson's life, writing that "Johnson wished to keep...his acknowledged biographer at a distance" and even second-guessed his "annointment" of Boswell as his official biographer.

Stephen Booth (academic): Stephen Booth (born April 20, 1933) is a professor emeritus of English literature at the University of California, Berkeley.  He was a Marshall Scholar and studied at the University of Cambridge.  He first attracted attention with his controversial 1969 essays "On the Value of Hamlet" and "An Essay on Shakespeare's Sonnets", in which he reread the works in a manner considerably different from contemporary Anglo-American readings.  Frank Kermode praised the former essay in the New York Review of Books in 1970 as being worth several full books of Shakespeare studies.

Question: What british literary critic lauded Stephen Booth's essay "On the Value of Hamlet"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "critic_name": {
      "type": "string",
      "description": "The name of the literary critic."
    },
    "critic_nationality": {
      "type": "string",
      "description": "The nationality of the literary critic."
    },
    "lauded_work_title": {
      "type": "string",
      "description": "The title of the essay that was praised."
    },
    "praise_details": {
      "type": "object",
      "properties": {
        "publication": {
          "type": "string",
          "description": "The publication where the praise appeared."
        },
        "year": {
          "type": "integer",
          "description": "The year the praise was published."
        },
        "description": {
          "type": "string",
          "description": "A description of the praise given."
        }
      },
      "required": [
        "publication",
        "year",
        "description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "critic_name",
    "critic_nationality",
    "lauded_work_title",
    "praise_details"
  ],
  "additionalProperties": false
}
