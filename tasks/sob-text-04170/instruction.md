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
Malakonda: Sri Malyadri Lakshmi Narasimha Swamy Vari Devasthanam is a Hindu Narasimha (avatar of Vishnu) with a temple in Malakonda, Valetivari Palem, Prakasham district, Andhra Pradesh, India.  He is Lord of Malyadri (Malakonda).  A large number of devotees visit the sacred shrine of Lord Lakshmi Narasimha to pay their homage to him.  Malyadri is one of the NavaNarasimhas (Nine Narasimhas).

Lakshmi Narasimhar Temple, Narasinghapuram: Sri Lakshmi Narasimhar Temple (Tamil: ஸ்ரீ லக்ஷ்மி நரசிம்ஹர் பெருமாள்) is located about 55 km from Chennai and 21 km from Arakkonam, in Narasingapuram, Thiruvallur.  The temple is dedicated to Hindu deity Narasimha, who is avatar of Vishnu and his consort Lakshmi.  From the days of glory and grandeur that prevailed in South India the temple of Lakhsmi Narasimha at Narasingapuram still boasts the era of Cholas and Vijayanagara Rayas.  The Lakshmi Narasimha Temple is situated in the village of Narasingapuram believed to be named after the temple.

Suthivelu: Suthivelu (Telugu: సుత్తి వేలు ) (born Kurumaddali Lakshmi Narasimha Rao; 7 August 1947 – 16 September 2012) was an Indian film character actor, and comedian known for his works in Telugu cinema.  Regarded as one of the finest comic actors in Telugu, He has acted in more than 200 films, and has garnered four state Nandi Awards.

Eluka Majaka: Eluka Majaka is a Telugu comedy film directed by Relangi Narasimha Rao.  The film stars Vennela Kishore, Brahmanandam, Raghu Babu and Pavani.  The film is the jointly produced by Marella Narasimha Rao and Vaddempudi Srinivasa Rao under the production company Naa Friends Art Movies.  This is the 75th film of Relangi Narasimha Rao.

Ayodhya 6 December 1992: Ayodhya 6 December 1992 (ISBN  ) is a book written by P. V. Narasimha Rao, the tenth Prime Minister of India, and published on 1 August 2006 .  Narasimha Rao had decreed that the book be published after his death, and accordingly it was published in August 2006.  He claims that the book is not an "“exercise in self-righteousness or justification”", the content of the book indicate an attempt by him to absolve himself and his government of the responsibility for the failure to prevent the removal of the controversial structure known as "Babri Masjid".  Narasimha Rao had assumed office in June 1991, and by that time the Ramjanamabhoomi-Babri Masjid issue was already in a state of serious alarm requiring intervention, including state intervention, to resolve the issue.

Novel: A novel is any relatively long, written work of narrative fiction, normally in prose, and typically published as a book.

Panuganti Lakshminarasimha Rao: Panuganti Lakshmi Narasimha Rao (Telugu - పానుగంటి లక్ష్మీ నరసింహా రావు) (2 november

Parrikal: Parrikal is a small village about 40 kilometers from Villupuram, Tamil Nadu.  Parrikal is famous for its ancient temple which houses Shri Lakshmi Narasimha (the fourth Avatar of Vishnu).  Lots of Madhva Brahmin families of the Shri Vyasaraja Mutt(Sosale) order owe allegiance to Parrikal Lakshmi Narasimha as their "Kula Devata" (God being worshiped ancestrally).  Lore has it that the idols here are very ancient "prathisthapane" (installation) dating back to 1500 BC.

Kovvali Lakshmi Narasimha Rao: Kovvali was a popular novelist of Telugu language in the early 20th century.  He is one of the most prolific writer of modern Telugu language.  His complete name is Kovvali Lakshmi Narasimha Rao (1912–1975), born in Tanuku.  He wrote about thousand Novels, which is a record not surpassed by any Telugu writer till now.  Though they are not of high standard, they are very popular with public and known as "Railway Literature".

Vinjamuri Venkata Lakshmi Narasimha Rao: Vinjamuri Venkata Lakshmi Narasimha Rao (Telugu: వింజమూరి వెంకట లక్ష్మీ నరసింహారావు) (born 1887, date of death unknown) was an Indian stage actor, Telugu-Sanskrit pandit and author.

Question: Which books which is relatively long written work of fiction did Kovvali Lakshmi Narasimha Rao write?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The full name of the author."
    },
    "book_type": {
      "type": "string",
      "description": "The type of written work that is a relatively long work of fiction."
    },
    "number_of_books_written": {
      "type": "integer",
      "description": "The total number of books of this type written by the author."
    }
  },
  "required": [
    "author_name",
    "book_type",
    "number_of_books_written"
  ],
  "additionalProperties": false
}
