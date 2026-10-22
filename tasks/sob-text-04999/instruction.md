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
List of female Nobel laureates: The Nobel Prizes are awarded annually by the Royal Swedish Academy of Sciences, the Swedish Academy, the Karolinska Institute, and the Norwegian Nobel Committee to individuals who make outstanding contributions in the fields of Chemistry, Physics, Literature, Peace, Physiology or Medicine and Economics.  All but the economics prize were established by the 1895 will of Alfred Nobel, which dictates that the awards should be administered by the Nobel Foundation.  The Nobel prize in Economics, or The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel, was established in 1968 by the Sveriges Riksbank, the central bank of Sweden, for outstanding contributions in the field of Economics.  Each prize is awarded by a separate committee; the Royal Swedish Academy of Sciences awards the Prizes in Physics, Chemistry, and Economics, the Swedish Academy awards the Prize in Literature, the Karolinska Institute awards the Prize in Physiology or Medicine, and the Norwegian Nobel Committee awards the Prize in Peace.  Each recipient receives a medal, a diploma and a cash prize that has varied throughout the years.

Chandrasekhar virial equations: In astrophysics, the Chandrasekhar virial equations are a hierarchy of moment equations of the Euler equations, developed by the Indian American astrophysicist Subrahmanyan Chandrasekhar, the Physicist Enrico Fermi and Norman R. Lebovitz.

List of Nobel laureates in Chemistry: The Nobel Prize in Chemistry (Swedish: "Nobelpriset i kemi" ) is awarded annually by the Royal Swedish Academy of Sciences to scientists in the various fields of chemistry.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel, who died in 1896.  These prizes are awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members elected by the Royal Swedish Academy of Sciences.  The first Nobel Prize in Chemistry was awarded in 1901 to Jacobus Henricus van 't Hoff, of the Netherlands.  Each recipient receives a medal, a diploma and a monetary award prize that has varied throughout the years.  In 1901, van 't Hoff received 150,782 SEK, which is equal to 7,731,004 SEK in December 2007.  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.

List of Chinese Nobel laureates: Since 1957, there have been eight Chinese (including Chinese born) winners of the Nobel Prize (Swedish: "Nobelpriset" ).  The Nobel Prize is a Sweden-based international monetary prize.  The award was established by the 1895 will and estate of Swedish chemist and inventor Alfred Nobel.  It was first awarded in Physics, Chemistry, Physiology or Medicine, Literature, and Peace in 1901.  An associated prize, The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel, was instituted by Sweden's central bank in 1968 and first awarded in 1969.

Subrahmanyan Chandrasekhar: Subrahmanyan Chandrasekhar, FRS (Tamil: சுப்பிரமணியன் சந்திரசேகர் ; ; 19 October 1910 – 21 August 1995), was an Indian American astrophysicist who was awarded the 1983 Nobel Prize for Physics with William A. Fowler "for his theoretical studies of the physical processes of importance to the structure and evolution of the stars".  His mathematical treatment of stellar evolution yielded many of the best current theoretical models of the later evolutionary stages of massive stars and black holes.  The Chandrasekhar limit is named after him.

List of Nobel laureates in Literature: The Nobel Prize in Literature (Swedish: "Nobelpriset i litteratur") is awarded annually by the Swedish Academy to authors for outstanding contributions in the field of literature.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel, which are awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members elected by the Swedish Academy.  The first Nobel Prize in Literature was awarded in 1901 to Sully Prudhomme of France.  Each recipient receives a medal, a diploma and a monetary award prize that has varied throughout the years.  In 1901, Prudhomme received 150,782 SEK, which is equivalent to 7,731,004 SEK in December 2007.  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.

Nobel Prize in Physics: The Nobel Prize in Physics (Swedish: "Nobelpriset i fysik" ) is a yearly award given by the Royal Swedish Academy of Sciences for those who conferred the most outstanding contributions for mankind in the field of physics.  It is one of the five Nobel Prizes established by the will of Alfred Nobel in 1895 and awarded since 1901; the others being the Nobel Prize in Chemistry, Nobel Prize in Literature, Nobel Peace Prize, and Nobel Prize in Physiology or Medicine.

Nobel Prize in Literature: Since 1901, the Nobel Prize in Literature (Swedish: "Nobelpriset i litteratur" ) has been awarded annually to an author from any country who has, in the words of the will of Alfred Nobel, produced "in the field of literature the most outstanding work in an ideal direction" (original Swedish: "den som inom litteraturen har producerat det mest framstående verket i en idealisk riktning").  Though individual works are sometimes cited as being particularly noteworthy, here "work" refers to an author's work as a whole.  The Swedish Academy decides who, if anyone, will receive the prize in any given year.  The academy announces the name of the chosen laureate in early October.  It is one of the five Nobel Prizes established by the will of Alfred Nobel in 1895; the others are the Nobel Prize in Chemistry, Nobel Prize in Physics, Nobel Peace Prize, and Nobel Prize in Physiology or Medicine.

List of Nobel laureates in Physics: The Nobel Prize in Physics (Swedish: "Nobelpriset i fysik" ) is awarded annually by the Royal Swedish Academy of Sciences to scientists in the various fields of physics.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel (who died in 1896), awarded for outstanding contributions in physics.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members elected by the Royal Swedish Academy of Sciences.  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.  Each recipient receives a medal, a diploma and a monetary award prize that has varied throughout the years.

List of Nobel laureates in Physiology or Medicine: The Nobel Prize in Physiology or Medicine (Swedish: "Nobelpriset i fysiologi eller medicin" ) is awarded annually by the Swedish Karolinska Institute to scientists and doctors in the various fields of physiology or medicine.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel (who died in 1896), awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members and an executive secretary elected by the Karolinska Institute.  While commonly referred to as the Nobel Prize in Medicine, Nobel specifically stated that the prize be awarded for "physiology or medicine" in his will.  Because of this, the prize can be awarded in a broader range of fields.  The first Nobel Prize in Physiology or Medicine was awarded in 1901 to Emil Adolf von Behring, of Germany.  Each recipient receives a medal, a diploma and a monetary award that has varied throughout the years.  In 1901, von Behring received 150,782 SEK, which is equal to 7,731,004 SEK in December 2008.  In 2013, the prize was awarded to James E. Rothman, Randy W. Schekman and Thomas C. Südhof; they were recognised "after discovering how cells precisely transport material".  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.

Question: Who was the developer of the Chandrasekhar virial equations awarded the Nobel Prize for Physics with?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nobel_laureate_name": {
      "type": "string",
      "description": "The name of the Nobel laureate who developed the equations."
    },
    "nobel_prize_year": {
      "type": "integer",
      "description": "The year the Nobel Prize was awarded."
    },
    "nobel_prize_field": {
      "type": "string",
      "description": "The field for which the Nobel Prize was awarded."
    },
    "co_recipient_name": {
      "type": "string",
      "description": "The name of the person who shared the Nobel Prize with the laureate."
    },
    "award_reason": {
      "type": "string",
      "description": "The specific reason or citation for the Nobel Prize award."
    }
  },
  "required": [
    "nobel_laureate_name",
    "nobel_prize_year",
    "nobel_prize_field",
    "co_recipient_name",
    "award_reason"
  ],
  "additionalProperties": false
}
