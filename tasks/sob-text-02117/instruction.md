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
Saint Stephen: Stephen (Greek: Στέφανος "Stéphanos", meaning "wreath, crown" and by extension "reward, honor", often given as a title rather than as a name), traditionally venerated as the Protomartyr or first martyr of Christianity, was according to the Acts of the Apostles a deacon in the early church at Jerusalem who aroused the enmity of members of various synagogues by his teachings.  Accused of blasphemy, at his trial he made a long speech denouncing the Jewish authorities who were sitting in judgment on him and was then stoned to death.  His martyrdom was witnessed by Saul of Tarsus, a Pharisee who would later himself become a follower of Jesus and known as Paul the Apostle.

Rufus of Ephesus: Rufus of Ephesus (Greek: Ῥοῦφος ὁ Ἐφέσιος , fl.  late 1st century AD) was a Greek physician and author who wrote treatises on dietetics, pathology, anatomy, and patient care.  He was to some extent a follower of Hippocrates, although he at times criticized or departed from that author's teachings.  His writings dealt with subjects often neglected by other authors, such as the treatment of slaves and the elderly.  Some of his works survive to this day.  He was particularly influential in the East, and some of his works survive only in Arabic.  His teachings emphasized the importance of anatomy, and sought pragmatic approaches to diagnosis and treatment.

Scattamek: Scattamek was a Lenape living in the Ohio Country during the 18th century.  He was a religious leader later termed a prophet who continued and built on the teachings of Neolin.  Their teachings influenced many of the surrounding tribes, including the Shawnee, the Miami, and Wea.  Scattamek is known to have been teaching during the 1770s.  The teachings were largely based on earlier traditions, but their teachings focused on the need to return to the tribe's ancestral ways, giving up European dress, liquor, and firearms.  They blamed their misfortunes on the gods anger with their adoption of European customs.  Scattamek had particular influence on Tenskwatawa, who led a nativist revival during the early 19th century that catalyzed tribal support for Tecumseh's War during the 1810s.

Behmenism: Behmenism, also Behemenism and similar, is the English-language designation for a 17th-century European Christian movement based on the teachings of German mystic and theosopher Jakob Böhme (1575-1624).  The term was not usually applied by followers of Böhme's theosophy to themselves, but rather was used by some opponents of Böhme's thought as a polemical term.  The origins of the term date back to the German literature of the 1620s, when opponents of Böhme's thought, such as the Thuringian antinomian Esajas Stiefel, the Lutheran theologian Peter Widmann and others denounced the writings of Böhme and the "Böhmisten".  When his writings began to appear in England in the 1640s, Böhme's surname was irretrievably corrupted to the form "Behmen" or "Behemen", whence the term "Behmenism" developed.  A follower of Böhme's theosophy is a "Behmenist".

Demosthenes Philalethes: Demosthenes Philalethes (Gr.  Δημοσθένης ὁ Φιλαλήθης ) was an ancient Greek physician of Asia Minor who was one of the pupils of Alexander Philalethes, a contemporary of Aristoxenus, and a follower of the teachings of Herophilos.  He succeeded Alexander as the head of the Herophilean school of medicine in Carura.  He probably lived around the beginning of the 1st century, and was especially celebrated for his skill as an oculist.  He was the author of the most influential ophthalmological work of antiquity, the "Ophthalmicus", on diseases of the eye, which appears to have been still extant in the Middle Ages, but of which nothing now remains, although some extracts are preserved by Aëtius Amidenus, Paul of Aegina, Rufus of Ephesus, and other later writers.  He also wrote a work on the pulse, which is quoted by Galen.  Demosthenes was the last known Herophilean in Asia Minor.

Finding Faith in Christ: Finding Faith in Christ (2003) is a 29-minute film produced by The Church of Jesus Christ of Latter-day Saints.  It depicts the ministry of Jesus Christ, showing some of his miracles and teachings as flashbacks, told by a believer to a skeptic and his family.  It was widely distributed in the April 2003 Ensign.

Aristoxenus (physician): Aristoxenus (Gr.  Ἀριστόξενος ) was a Greek physician of Asia Minor who was quoted by Caelius Aurelianus.  He was a pupil of Alexander Philalethes and contemporary of Demosthenes Philalethes, and must therefore have lived around the 1st century.  He was a follower of the teachings of Herophilos, and studied at the celebrated Herophilean school at the village of Men-Carus, between Laodicea and Carura.  He wrote a work Περὶ τῆς Ἡροφίλου Αἱρέσεως ("On the Herophilean Sect", Latin: "De Herophili Secta"), of which the thirteenth book is quoted by Galen, but which is no longer extant.

Samuel S. Snow: Samuel Sheffield Snow (1806–1890) was a skeptic turned Millerite preacher who calculated that the return of Christ was to take place on October 22, 1844.  His teaching sparked what became known as the "Seventh-month movement," which led to the Great Disappointment when Jesus did not return as expected.

Millerism: The Millerites were the followers of the teachings of William Miller, who in 1833 first shared publicly his belief that the Second Advent of Jesus Christ would occur in roughly the year 1843–1844.

Sefer Hasidim: The Sefer Hasidim or Sefer Chassidim (Hebrew: ספר חסדים‎ ‎ , Book of the Pious) is a text by Judah ben Samuel of Regensburg, a foundation work of the teachings of the Chassidei Ashkenaz ("Pious Ones of Germany").  It offers an account of the day-to-day religious life of medieval German Jews, and their customs, beliefs, and traditions.  It presents the combined teachings of the three leaders of German Hasidism during the 12th and 13th centuries: Samuel the Chassid, Judah the Chassid of Regensburg (his son), and Elazar Rokeach.

Question: Samuel Sheffield Snow was a skeptic then later a follower of the teachings of who ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "follower_name": {
      "type": "string",
      "description": "The name of the individual who became a follower."
    },
    "original_status": {
      "type": "string",
      "description": "The initial status or belief of the follower before adopting new teachings."
    },
    "leader_followed": {
      "type": "string",
      "description": "The name of the person whose teachings were followed."
    },
    "related_movement": {
      "type": "string",
      "description": "The name of the movement associated with the teachings followed."
    }
  },
  "required": [
    "follower_name",
    "original_status",
    "leader_followed",
    "related_movement"
  ],
  "additionalProperties": false
}
