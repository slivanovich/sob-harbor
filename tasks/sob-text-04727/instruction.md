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
The Trouble with Physics: The Trouble with Physics: The Rise of String Theory, the Fall of a Science, and What Comes Next is a 2006 book by the theoretical physicist Lee Smolin about the problems with string theory.  Subtitled "The Rise of String Theory, the Fall of a Science, and What Comes Next", the book strongly criticizes string theory and its prominence in contemporary theoretical physics, on the grounds that string theory has yet to come up with a single prediction that can be verified using any technology that is likely to be feasible within our lifetimes.  Smolin also focuses on the difficulties faced by research in quantum gravity, and by current efforts to come up with a theory explaining all four fundamental interactions.  The book is broadly concerned with the role of controversy and diversity of approaches in scientific processes and ethics.

String theory: In physics, string theory is a theoretical framework in which the point-like particles of particle physics are replaced by one-dimensional objects called strings.  It describes how these strings propagate through space and interact with each other.  On distance scales larger than the string scale, a string looks just like an ordinary particle, with its mass, charge, and other properties determined by the vibrational state of the string.  In string theory, one of the many vibrational states of the string corresponds to the graviton, a quantum mechanical particle that carries gravitational force.  Thus string theory is a theory of quantum gravity.

Matrix string theory: In physics, matrix string theory is a set of equations that describe superstring theory in a non-perturbative framework.  Type IIA string theory can be shown to be equivalent to a maximally supersymmetric two-dimensional gauge theory, the gauge group of which is U("N") for a large value of "N".  This matrix string theory was first proposed by Luboš Motl in 1997 and later independently in a more complete paper by Robbert Dijkgraaf, Erik Verlinde, and Herman Verlinde.  Another matrix string theory equivalent to Type IIB string theory was constructed in 1996 by Ishibashi, Kawai, Kitazawa and Tsuchiya.  This version is known as the IKKT matrix model.

Swampland (physics): In physics, the term swampland is used in contrast to the term "landscape" to indicate physical theories or aspects of such theories that could be true if gravity were not an issue but are not compatible with string theory.  Recent developments in string theory suggest that the string theory landscape of False vacua is vast.

Light Railways Act 1896: The Light Railways Act 1896 (59 & 60 Vict.  c.48) was an Act of the Parliament of the United Kingdom of Great Britain and Ireland (as it then was).  Before the Act each new railway line built in the country required a specific Act of Parliament to be obtained by the company that wished to construct it, which greatly added to the cost and time it took to construct new railways.  The economic downturn of the 1880s had hit agriculture and rural communities in the United Kingdom especially hard and the government wished to facilitate the construction of railways in rural areas, especially to facilitate the transport of goods.  The 1896 Act defined a class of railways which did not require specific legislation to construct – companies could simply plan a line under the auspices of the new Act, and, having obtained a Light Railway Order, build and operate it.  By reducing the legal costs and allowing new railways to be built quickly the government hoped to encourage companies to build the new 'light railways' in areas of low population and industry that were previously of little interest to them.

String phenomenology: String phenomenology is a branch of theoretical physics that attempts to construct realistic or semi-realistic models of particle physics based on string theory.  The term "realistic" is usually taken to mean that the low energy limit of string theory yields a model which bears a resemblance to the Minimal Supersymmetric Standard Model (MSSM).

Cumrun Vafa: Cumrun Vafa (Persian: کامران وفا‎ ‎ ] ; born 1960) is an Iranian-American string theorist from Harvard University, which he first joined as a Harvard Junior Fellow.  He is the recipient of the 2008 Dirac Medal and the 2016 Breakthrough Prize in Fundamental Physics.

F-theory: F-theory is a branch of string theory developed by Cumrun Vafa.  The new vacua described by F-theory were discovered by Vafa and allowed string theorists to construct new realistic vacua — in the form of F-theory compactified on elliptically fibered Calabi–Yau four-folds.  The letter "F" supposedly stands for "Father".

Type 0 string theory: The Type 0 string theory is a less well-known model of string theory.  It is a superstring theory in the sense that the worldsheet theory is supersymmetric.  However, the spacetime spectrum is not supersymmetric and, in fact, does not contain any fermions at all.  In dimensions greater than two, the ground state is a tachyon so the theory is unstable.  These properties make it similar to the bosonic string and an unsuitable proposal for describing the world as we observe it, although a GSO projection does get rid of the tachyon and the even G-parity sector of the theory defines a stable string theory.  The theory is used sometimes as a toy model for exploring concepts in string theory, notably closed string tachyon condensation.  Some other recent interest has involved the two-dimensional Type 0 string which has a non-perturbatively stable matrix model description.

String theory landscape: The string theory landscape refers to the collection of possible false vacua in string theory, together comprising a collective "landscape" of choices of parameters governing compactifications .

Question: This Iranian-American developed a branch of string theory allowing theorists to construct new vacua?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the theoretical physicist."
    },
    "nationality": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The nationalities of the person."
    },
    "profession": {
      "type": "string",
      "description": "The primary profession of the person."
    },
    "contribution": {
      "type": "object",
      "properties": {
        "branch_developed": {
          "type": "string",
          "description": "The name of the branch of string theory developed."
        },
        "impact": {
          "type": "string",
          "description": "The main impact or result of developing this branch."
        },
        "related_concept": {
          "type": "string",
          "description": "A key concept related to the impact, such as 'vacua'."
        }
      },
      "required": [
        "branch_developed",
        "impact",
        "related_concept"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "nationality",
    "profession",
    "contribution"
  ],
  "additionalProperties": false
}
