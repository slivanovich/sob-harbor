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
Jerry Fodor: Jerry Alan Fodor ( ; born 1935) is an American philosopher and cognitive scientist.  He holds the position of State of New Jersey Professor of Philosophy, Emeritus, at Rutgers University and is the author of many works in the fields of philosophy of mind and cognitive science, in which he has laid the groundwork for the modularity of mind and the language of thought hypotheses, among other ideas.  He is known for his provocative and sometimes polemical style of argumentation and as "one of the principal philosophers of mind of the late twentieth and early twenty-first century.  In addition to having exerted an enormous influence on virtually every portion of the philosophy of mind literature since 1960, Fodor's work has had a significant impact on the development of the cognitive sciences."

Samuel Merrill Woodbridge: The Reverend Samuel Merrill Woodbridge, D.D., LL.D.  (April 5, 1819 – June 23, 1905) was an American clergyman, theologian, author, and college professor.  A graduate of New York University and the New Brunswick Theological Seminary, Woodbridge preached for sixteen years as a clergyman in the Reformed Church in America.  After settling in New Brunswick, New Jersey, he taught for 44 years as professor of ecclesiastical history and church government at the New Brunswick Theological Seminary, and for seven years as professor of "metaphysics and philosophy of the human mind" at Rutgers College (now Rutgers, The State University of New Jersey) in New Brunswick.  Woodbridge later led the New Brunswick seminary as Dean and President of the Faculty from 1883 to 1901.  He was the author of three books and several published sermons and addresses covering various aspects of Christian faith, theology, church history and government.

Mark Rowlands: Mark Rowlands (born 1962) is a Welsh writer and philosopher.  He is Professor of Philosophy at the University of Miami, and the author of several books on the philosophy of mind, the moral status of non-human animals, and cultural criticism.  He is known within academic philosophy as one of the principal architects of the view known as vehicle externalism, or the extended mind.  His works include "Animal Rights" (1998), "The Body in Mind" (1999), "The Nature of Consciousness" (2001), "Animals Like Us" (2002), and a personal memoir, "The Philosopher and the Wolf" (2008).

Paul Moser: Paul K. Moser (born 1957 in Bismarck, North Dakota) is an American analytic philosopher who writes on epistemology and the philosophy of religion.  He is Professor of Philosophy at Loyola University Chicago and past editor of the "American Philosophical Quarterly".  He is the author of many works in epistemology and the philosophy of religion, in which he has supported versions of epistemic foundationalism and volitional theism.  His work brings these two positions together to support volitional evidentialism about theistic belief, in contrast to fideism and traditional natural theology.  He draws from some epistemological and theological insights of the apostle Paul, Blaise Pascal, Kierkegaard, John Oman, and H. H. Farmer, but adds (i) a notion of purposively available evidence of God’s existence, (ii) a notion of authoritative evidence in contrast with spectator evidence, and (iii) a notion of personifying evidence of God whereby some willing humans become salient evidence of God's existence.  His most recent work emphasizes the importance of foundational evidence from the self-manifestation of God's moral character to cooperative humans.  An evidential role for "agapē", along the lines of Romans 5:5, is central to his theistic epistemology, as is his view that God is self-authenticating or self-evidencing via self-manifestation and conviction toward unselfish love.  One result is a distinctive approach to divine hiddenness.

The Mind of God: The Mind of God is a 1992 non-fiction book by Paul Davies.  Subtitled "The Scientific Basis for a Rational World", it is a whirlwind tour and explanation of theories, both physical and metaphysical, regarding ultimate causes.  Its title comes from a quotation from Stephen Hawking: "If we do discover a theory of everything...it would be the ultimate triumph of human reason—for then we would truly know the mind of God."

David Linden: David J. Linden (born November 3, 1961) is an American professor of neuroscience at Johns Hopkins University in Baltimore, Maryland, and the author of "The Accidental Mind: How Brain Evolution Has Given Us Love, Memory, Dreams, and God".

Henry James Clark: Henry James Clark, American naturalist; born in Easton, Massachusetts, July 22, 1826; graduated at New York University 1848; became a pupil of Asa Gray at the Cambridge botanical garden; graduated at the Lawrence Scientific School at Harvard 1854; assistant to Louis Agassiz till 1863, and also for three years adjunct Professor of Zoology at the Lawrence Scientific School; Professor of Natural Sciences in Pennsylvania State College, near Bellefonte, 1866–69; Professor of Natural History in University of Kentucky, Lexington, 1869–72; Professor of Veterinary Science in Massachusetts Agricultural College, Amherst, from 1872 until his death there July 1, 1873.  He contributed to the Smithsonian publications, to the Proceedings of the American Academy of Arts and Sciences, and to other learned periodicals.  Author of "Mind in Nature" (Cambridge, 1863) and of the "Mode of Development of Animals" (New York, 1865).  See A. S. Packard, Jr.'s Memoir in "Biographical Memoirs of the National Academy of Sciences" (Washington, 1877).

Hunter B. Shirley: Hunter B. Shirley (December 25, 1927 – November 1, 2010) born Hunter Barentine Shirley, was a longtime licensed clinical psychologist and a former Associate Professor at Wisconsin State University where he headed a psychological research laboratory devoted to evaluating the world's first analog model of the mind.  He was most recently the Director of the International Division of the American Institute of Applied Behavioral Research and Human Relations Training.  Formerly Director of Behavior Analysis, Inc. of St. Louis subsequently he was director of the Counseling and Testing Center at the University of Louisiana at Lafayette, and later served as the Chief Clinical Psychologist of the Lafayette Institute of Behavior Therapy and Crisis Management.  Author of a number of books, including the trail-blazing book "Mapping the Mind", and the popular self-help book "Your Mind May Be Programmed Against You!" .  He is credited with having developed the most sophisticated model of the human mind currently in existence.  With offices in Staré Splavy near Prague, Shirley was in charge of a "Think tank" performing behavioral science research for NGOs and government agencies.  His final work "The Human Mind: A Guided Tour", a comprehensive compilation of his theories on the emotional system and the human mind developed over a lifetime of clinical and field studies, is in the final phases of editing in preparation for publication.  This book includes over 300 diagrams of the emotional system based on a cybernetics approach as he first presented in his book "Mapping The Mind" and in numerous published articles.

Paul Davies: Paul Charles William Davies, AM (born 22 April 1946) is an English physicist, writer and broadcaster, a professor at Arizona State University as well as the Director of BEYOND: Center for Fundamental Concepts in Science.  He is affiliated with the Institute for Quantum Studies at Chapman University in California.  He has held previous academic appointments at the University of Cambridge, University College London, University of Newcastle upon Tyne, University of Adelaide and Macquarie University.  His research interests are in the fields of cosmology, quantum field theory, and astrobiology.  He has proposed that a one-way trip to Mars could be a viable option.

Robert Wilson (philosopher): Robert A. Wilson {'1': ", '2': ", '3': ", '4': "} (born 1964) has been professor of philosophy at the University of Alberta since 2000, after teaching previously at the University of Illinois, Urbana-Champaign (1996-2001), where he was a member of the Cognitive Science Group at the Beckman Institute for Advanced Science and Technology, and at Queen’s University (1992-1996).  His chief research and teaching expertise is in the philosophy of mind, cognitive science, and the philosophy of biology; he has also published on a broader range of topics outside of these areas, including disability, Locke on primary qualities, personal identity, constitution views in metaphysics, and kinship.  In general, his work draws on connections between philosophy and the various sciences.  He is the author or editor of six books, including Boundaries of the Mind (Cambridge, 2004) and Genes and the Agents of Life (Cambridge, 2005), and has a recently completed book in press, The Eugenic Mind Project (MIT Press, 2017).

Question: Where is the author of The Mind of God a professor?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author."
    },
    "book_title": {
      "type": "string",
      "description": "The title of the book mentioned."
    },
    "university_affiliation": {
      "type": "object",
      "properties": {
        "university_name": {
          "type": "string",
          "description": "The name of the university where the author is a professor."
        },
        "role": {
          "type": "string",
          "description": "The author's role or position at the university."
        }
      },
      "required": [
        "university_name",
        "role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "author_name",
    "book_title",
    "university_affiliation"
  ],
  "additionalProperties": false
}
