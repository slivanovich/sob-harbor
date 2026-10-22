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
On the Harmony of Religions and Philosophy: Fasl al-Maqal fi ma bayn al-Hikma wa al-Shariah min Ittisal (Arabic: "فصل المقال في ما بين الحكمة و الشريعة من إتصال" often translated as On the Harmony of Religions and Philosophy or The Decisive Treatise, Determining the Nature of the Connection between Religion and Philosophy, with the latter often shortened to The Decisive Treatise) is an Islamic philosophical treatise written by Andalusian Muslim polymath and philosopher Ibn Rushd (Averroes) (1126–1198), in which the author "critically examine[s] the alleged tension between philosophy and religion" and concludes that philosophy (in particular, Aristotelian philosophy) is not in opposition toand in fact, works in tandem withIslamic thought.  In the work, Averroes argues that some Muslims have an obligation to study philosophy, and that the subject should be considered an Islamic science.  The work also contains several other unique ideas, including Averroes' assertion that the Qur’an should sometimes be read in a non-literal way.  According to William Theodore De Bary and Ainslie Embree, "On the Harmony of Religions and Philosophy" represents a "classic attempt to reconcile religion and philosophy."

Confraternity of Good Christians: The Society of True Christians ("c." 1530-1545), whose original name was "Confraternita dei Buoni Cristiani", was a philosophy study group in Malta which sought freedom of thought and action.  It was made up of both clerical and lay persons, and its members were Maltese as well as foreign.  Its area of specialisation in philosophy was chiefly ethics.  It also gave considerable importance to biblical studies.

Philosophy of computer science: The philosophy of computer science is concerned with the philosophical questions that arise with the study of computer science, which is understood to mean not just programming but the whole study of concepts and methods that assist in the development and maintenance of computer systems.  There is still no common understanding of the content, aim, focus, or topic of the philosophy of computer science, despite some attempts to develop a philosophy of computer science like the philosophy of physics or the philosophy of mathematics.

Medieval philosophy: Medieval philosophy is the philosophy in the era now known as medieval or the Middle Ages, the period roughly extending from the fall of the Western Roman Empire in the 5th century C.E. to the Renaissance in the 16th century.  Medieval philosophy, understood as a project of independent philosophical inquiry, began in Baghdad, in the middle of the 8th century, and in France, in the itinerant court of Charlemagne, in the last quarter of the 8th century.  It is defined partly by the process of rediscovering the ancient culture developed in Greece and Rome in the classical period, and partly by the need to address theological problems and to integrate sacred doctrine with secular learning.

Pythagoras: Pythagoras of Samos ( ; ; Greek: Πυθαγόρας ὁ Σάμιος  "Pythagóras ho Sámios"  "Pythagoras the Samian" , or simply Πυθαγόρας ; Πυθαγόρης in Ionian Greek; 495 BC ) was an Ionian Greek philosopher, mathematician, and putative founder of the Pythagoreanism movement.  He is often revered as a great mathematician and scientist and is best known for the Pythagorean theorem which bears his name.

Bush–Holley House: The Bush–Holley House is a National Historic Landmark and historic house museum at 39 Strickland Road in the Cos Cob section of Greenwich, Connecticut.  It was constructed circa 1730 and in the late nineteenth century was a boarding house and the center of the Cos Cob Art Colony, Connecticut’s first art colony.  From 1890 to 1920, the house was a gathering place for artists, writers and editors, and scores of art students came to study with leading American Impressionists John Henry Twachtman, J. Alden Weir, Theodore Robinson, and Childe Hassam.  It is currently operated as a historic site by the Historical Society of the Town of Greenwich, and is open for tours.

Timocrates of Lampsacus: Timocrates of Lampsacus (Greek: Τιμοκράτης ) was a renegade Epicurean who made it his life's mission to spread slander about Epicurus' philosophy and way of life.  He was the elder brother of Metrodorus, Epicurus' best friend and most loyal follower, who was born in Lampsacus in the late 4th century BC.  He studied with his brother in the school of Epicurus, but some time c. 290 BC, he broke with the school, apparently because he refused to accept that pleasure was the supreme good of life.  The dispute became quite bitter; Philodemus quotes Timocrates saying "that he both loved his brother as no one else did and hated him as no one else."  In a much quoted letter, Metrodorus, in exaggerated fashion, took Timocrates to task for not making the stomach the standard in everything relating to the prime good.  Metrodorus wrote at least one work against Timocrates; and Epicurus also wrote an "Opinions on the Passions, against Timocrates".  In response, Timocrates wrote a polemic against Epicurus, whereby he claimed that Epicurus was not a genuine Athenian citizen, and that he was slovenly, weak, ignorant, rude, and vomited twice a day from overindulgence.

Mianus, Connecticut: Mianus , formerly Mayamus and Upper Landing, is a neighborhood in the town of Greenwich in the U.S. state of Connecticut.  Unlike other Greenwich neighborhoods such as Cos Cob or Old Greenwich, Mianus does not have its own ZIP code or post office.  Mianus lies partly in the Cos Cob ZIP code, partly in the Riverside ZIP code area, and partly in the Old Greenwich ZIP code area.  It lies at an elevation of 23 feet (7 m) and is home to an elementary school.  Mianus was also home to the Mianus Motor Works, a marine-engine manufacturer.

Metrodorus of Cos: Metrodorus of Cos (Greek: Μητρόδωρος τῆς Κῶ ; fl.  c. 460 BC) was the son of Epicharmus.  Like several of his family he addicted himself partly to the study of Pythagorean philosophy, partly to the science of medicine.  He wrote a treatise upon the works of Epicharmus, in which, on the authority of Epicharmus and Pythagoras himself, he maintained that the Doric was the proper dialect of the Orphic hymns.

Cosmic Origins Spectrograph: The Cosmic Origins Spectrograph (COS) is a science instrument that was installed on the Hubble Space Telescope during Servicing Mission 4 (STS-125) in May 2009.  It is designed for ultraviolet (90–320 nm) spectroscopy of faint point sources with a resolving power of ≈1,550–24,000.  Science goals include the study of the origins of large scale structure in the universe, the formation and evolution of galaxies, and the origin of stellar and planetary systems and the cold interstellar medium.  COS was developed and built by the Center for Astrophysics and Space Astronomy (CASA-ARL) at the University of Colorado at Boulder and the Ball Aerospace and Technologies Corporation in Boulder, Colorado.

Question: Which philosophy study was Metrodorus of Cos partly addicted to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "philosopher_name": {
      "type": "string",
      "description": "The name of the philosopher."
    },
    "philosophy_study": {
      "type": "string",
      "description": "The specific philosophy study the philosopher was partly addicted to."
    },
    "related_field": {
      "type": "string",
      "description": "Another field the philosopher was partly addicted to, if mentioned."
    },
    "source_text_excerpt": {
      "type": "string",
      "description": "An excerpt from the text that supports the answer."
    }
  },
  "required": [
    "philosopher_name",
    "philosophy_study",
    "related_field",
    "source_text_excerpt"
  ],
  "additionalProperties": false
}
