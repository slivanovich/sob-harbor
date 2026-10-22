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
Toronto School of communication theory: The Toronto School is a school of thought in communication theory and literary criticism, the principles of which were developed chiefly by scholars at the University of Toronto.  It is characterized by exploration of Ancient Greek literature and the theoretical view that communication systems create psychological and social states.  The school originated from the works of Eric A. Havelock and Harold Innis in the 1930s, and grew to prominence with the contributions of Edmund Snow Carpenter, Northrop Frye and Marshall McLuhan.

Message design logic: Message design logic is a communication theory that makes the claim that individuals possess implicit theories of communication within themselves, called message design logics.  Referred to as a “theory of theories,” Message Design Logic offers three different fundamental premises in reasoning about communication.  As author Barbara O’Keefe describes, Message Design Logic is “the kind of communication-constituting belief system the message producer relies on in reasoning from the goals sought to the message design used.”  These three premises — Expressive Logic, Conventional Logic, and Rhetorical Logic — are belief systems that communicators might utilize when designing messages.  The message design logics, therefore, represent “internally consistent and developmentally ordered stages in the acquisition of working knowledge about the systematic properties of verbal messages.”  As O’Keefe describes further, each premise is “associated with a constellation of related beliefs: a communication-constituting concept, a conception of the functional possibilities of communication, unit formation procedures, and principles of coherence.”  The underlying idea behind O’Keefe’s work is that “communication is not necessarily a uniform process.”

Eric A. Havelock: Eric Alfred Havelock ( ; 3 June 1903 – 4 April 1988) was a British classicist who spent most of his life in Canada and the United States.  He was a professor at the University of Toronto and was active in the Canadian socialist movement during the 1930s.  In the 1960s and 1970s, he served as chair of the classics departments at both Harvard and Yale.  Although he was trained in the turn-of-the-20th-century Oxbridge tradition of classical studies, which saw Greek intellectual history as an unbroken chain of related ideas, Havelock broke radically with his own teachers and proposed an entirely new model for understanding the classical world, based on a sharp division between literature of the 6th and 5th centuries BC on the one hand, and that of the 4th on the other.

Metro Toronto School for the Deaf: The Metropolitan Toronto School for the Deaf is a division of the public school, Davisville Junior Public School / Metropolitan Toronto School for the Deaf, in Toronto, Ontario with day programs serving deaf and hard-of-hearing students from kindergarten to grade eight.  In this division, American Sign Language and Spoken English with the aid of Signed Exact English are used as the languages of communication.

Russian formalism: Russian formalism was an influential school of literary criticism in Russia from the 1910s to the 1930s.  It includes the work of a number of highly influential Russian and Soviet scholars such as Viktor Shklovsky, Yuri Tynianov, Vladimir Propp, Boris Eichenbaum, Roman Jakobson, Boris Tomashevsky, Grigory Gukovsky who revolutionised literary criticism between 1914 and the 1930s by establishing the specificity and autonomy of poetic language and literature.  Russian formalism exerted a major influence on thinkers like Mikhail Bakhtin and Yuri Lotman, and on structuralism as a whole.  The movement's members had a relevant influence on modern literary criticism, as it developed in the structuralist and post-structuralist periods.  Under Stalin it became a pejorative term for elitist art.

Loreen Olson: Loreen Olson is a well-known feminist scholar in the area of family communication, with an emphasis on gender, communication, and violence.  She is currently an assistant professor for the Communication Studies department at the University of North Carolina at Greensboro.  She teaches graduate and undergraduate classes on communication theory, gender communication, relational communication, family communication, qualitative research methods, and interpersonal communication theory.  Olson and co-authors Elizabeth A. Baiocchi-Wagner, Jessica M. Wilson-Kratzer, and Sarah E. Symonds published a book entitled "The Dark Side of Family Communication".  Loreen Olson is also the current Editor of the Journal of "Family Communication" (1/2012–present).

Chicago school (literary criticism): The Chicago School of literary criticism was a form of criticism of English literature begun at the University of Chicago in the 1930s, which lasted until the 1950s.  It was also called Neo-Aristotelianism, due to its strong emphasis on Aristotle’s concepts of plot, character and genre.  It was partly a reaction to New Criticism, a then highly popular form of literary criticism, which the Chicago critics accused of being too subjective and placing too much importance on irony and figurative language.  They aimed instead for total objectivity and a strong classical basis of evidence for criticism.  The New Critics regarded the language and poetic diction as most important, but the Chicago School considered such things merely the building material of poetry.  Like Aristotle, they valued the structure or form of a literary work as a whole, rather than the complexities of the language.  Despite this, the Chicago School is considered by some to be a part of the New Criticism movement.

Truman Capote Award for Literary Criticism: The Truman Capote Award for Literary Criticism is awarded for literary criticism by the University of Iowa on behalf of the Truman Capote Literary Trust.  The value of the award is $30,000 (USD), and is said to be the largest annual cash prize for literary criticism in the English language.  The formal name of the prize is the Truman Capote Award for Literary Criticism in Memory of Newton Arvin, commemorating both Capote and his friend Newton Arvin, who was a distinguished critic and Smith College professor until he lost his job in 1960 after his homosexuality was publicly exposed.

Alphabet effect: The alphabet effect is a group of hypotheses in communication theory arguing that phonetic writing, and alphabetic scripts in particular, have served to promote and encourage the cognitive skills of abstraction, analysis, coding, decoding, and classification.  Promoters of these hypotheses are associated with the Toronto School of Communication, such as Marshall McLuhan, Harold Innis, Walter Ong and more recently Robert K. Logan; the term "alphabet effect" comes from Logan's 1986 work (see the bibliography below which references the 2004 second edition).

Feminist literary criticism: Feminist literary criticism is literary criticism informed by feminist theory, or, more broadly, by the politics of feminism.  It uses feminist principles and ideology to critique the language of literature.  This school of thought seeks to analyze and describe the ways in which literature portrays the narrative of male domination by exploring the economic, social, political, and psychological forces embedded within literature.  This way of thinking and criticizing works can be said to have changed the way literary texts are viewed and studied, as well as changing the canon of what is taught.

Question: The Toronto School is a school of thought in communication theory and literary criticism, the principles of which were developed chiefly by scholars at the University of Toronto, the school originated from the works of Eric A. Havelock, was a British classicist who spent most of his life in Canada, and which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "school_name": {
      "type": "string",
      "description": "The name of the school of thought."
    },
    "school_type": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The fields of study associated with the school."
    },
    "originator_name": {
      "type": "string",
      "description": "The name of one of the originators of the school."
    },
    "originator_nationality": {
      "type": "string",
      "description": "The nationality of the originator."
    },
    "countries_lived_in": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Countries where the originator spent most of his life."
    }
  },
  "required": [
    "school_name",
    "school_type",
    "originator_name",
    "originator_nationality",
    "countries_lived_in"
  ],
  "additionalProperties": false
}
