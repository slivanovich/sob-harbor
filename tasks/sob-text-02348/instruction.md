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
Ada Yonath: Ada E. Yonath (Hebrew: עדה יונת‎ ‎ , ] ) (born 22 June 1939) is an Israeli crystallographer best known for her pioneering work on the structure of the ribosome.  She is the current director of the Helen and Milton A. Kimmelman Center for Biomolecular Structure and Assembly of the Weizmann Institute of Science.  In 2009, she received the Nobel Prize in Chemistry along with Venkatraman Ramakrishnan and Thomas A. Steitz for her studies on the structure and function of the ribosome, becoming the first Israeli woman to win the Nobel Prize out of ten Israeli Nobel laureates, the first woman from the Middle East to win a Nobel prize in the sciences, and the first woman in 45 years to win the Nobel Prize for Chemistry.  However, she said herself that there was nothing special about a woman winning the Prize.

Arthur Leonard Schawlow: Arthur Leonard Schawlow (May 5, 1921 – April 28, 1999) was an American physicist and co-inventor of the laser with Charles Townes.  His central insight, which Townes overlooked, was the use of two mirrors as the resonant cavity to take MASER action to visible wavelengths.  He shared the 1981 Nobel Prize in Physics with Nicolaas Bloembergen and Kai Siegbahn for his work on lasers.

List of Danish Nobel laureates: This is a list of Danish Nobel laureates.  Since the Nobel Prize was established per the will of Swedish inventor Alfred Nobel in 1895, 12 of the prize winners have been from Denmark.  The first Danish Nobel laureate was Niels Ryberg Finsen, who won a Nobel Prize for medicine in 1903 for his work in using light therapy to treat diseases.  The most recent Danish Nobel Prize winner was Jens Skou who won the prize in chemistry for his discovery over the enzyme, Na+/K+-ATPase in 1997.  To date, of the 13 Nobel Prizes won by Danish people, 5 have been for medicine, 3 have been for physics, 3 have been for literature, 1 has been for chemistry and one has been for peace.

Frederick Sanger: Frederick Sanger ( ; 13 August 1918 – 19 November 2013) was a British biochemist who twice won the Nobel Prize in Chemistry, one of only two people to have done so in the same category (the other is John Bardeen in physics), the fourth person overall with , and the third person overall with two Nobel Prizes in the sciences.  In 1958, he was awarded a Nobel Prize in chemistry "for his work on the structure of proteins, especially that of insulin".  In 1980, Walter Gilbert and Sanger shared half of the chemistry prize "for their contributions concerning the determination of base sequences in nucleic acids".  The other half was awarded to Paul Berg "for his fundamental studies of the biochemistry of nucleic acids, with particular regard to recombinant DNA".

List of Nobel laureates in Physiology or Medicine: The Nobel Prize in Physiology or Medicine (Swedish: "Nobelpriset i fysiologi eller medicin" ) is awarded annually by the Swedish Karolinska Institute to scientists and doctors in the various fields of physiology or medicine.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel (who died in 1896), awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members and an executive secretary elected by the Karolinska Institute.  While commonly referred to as the Nobel Prize in Medicine, Nobel specifically stated that the prize be awarded for "physiology or medicine" in his will.  Because of this, the prize can be awarded in a broader range of fields.  The first Nobel Prize in Physiology or Medicine was awarded in 1901 to Emil Adolf von Behring, of Germany.  Each recipient receives a medal, a diploma and a monetary award that has varied throughout the years.  In 1901, von Behring received 150,782 SEK, which is equal to 7,731,004 SEK in December 2008.  In 2013, the prize was awarded to James E. Rothman, Randy W. Schekman and Thomas C. Südhof; they were recognised "after discovering how cells precisely transport material".  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.

Abdus Salam: Mohammad Abdus Salam {'1': ", '2': ", '3': 'NI, SPk, KBE', '4': "} (Punjabi, Urdu: ‎ ; ] ; 29 January 192621 November 1996), was a Pakistani theoretical physicist.  A major figure in 20th century theoretical physics, he shared the 1979 Nobel Prize in Physics with Sheldon Glashow and Steven Weinberg for his contribution to the electroweak unification theory.  He was the first Pakistani and first Muslim to receive a Nobel Prize in science and the second from an Islamic country to receive any Nobel Prize (after Anwar Sadat of Egypt).

Nikolay Basov: Nikolay Gennadiyevich Basov (Russian: Никола́й Генна́диевич Ба́сов ; 14 December 1922 – 1 July 2001) was a Soviet physicist and educator.  For his fundamental work in the field of quantum electronics that led to the development of laser and maser, Basov shared the 1964 Nobel Prize in Physics with Alexander Prokhorov and Charles Hard Townes.

Maser: A maser ( , an acronym for "microwave amplification by stimulated emission of radiation") is a device that produces coherent electromagnetic waves through amplification by stimulated emission.  The first maser was built by Charles H. Townes, James P. Gordon, and H. J. Zeiger at Columbia University in 1953.  Townes, Nikolay Basov and Alexander Prokhorov were awarded the 1964 Nobel Prize in Physics for theoretical work leading to the maser.  Masers are used as the timekeeping device in atomic clocks, and as extremely low-noise microwave amplifiers in radio telescopes and deep space spacecraft communication ground stations.

Aage Bohr: Aage Niels Bohr (] ; 19 June 1922 – 8 September 2009) was a Danish nuclear physicist who shared the Nobel Prize in Physics in 1975 with Ben Mottelson and James Rainwater "for the discovery of the connection between collective motion and particle motion in atomic nuclei and the development of the theory of the structure of the atomic nucleus based on this connection".  Starting from Rainwater's concept of an irregular-shaped liquid drop model of the nucleus, Bohr and Mottelson developed a detailed theory that was in close agreement with experiments.  Since his father, Niels Bohr, had won the prize in 1922, he and his father were one of the six pairs of fathers and sons who have both won the Nobel Prize and one of the four pairs who have both won the Nobel Prize in Physics.

Charles H. Townes: Charles Hard Townes (July 28, 1915 – January 27, 2015) was an American physicist and inventor of the maser and laser.  Townes worked on the theory and application of the maser, for which he obtained the fundamental patent, and other work in quantum electronics associated with both maser and laser devices.  He shared the Nobel Prize in Physics during 1964 with Nikolay Basov and Alexander Prokhorov.  Charles was an advisor to the United States Government, meeting every US President from Harry Truman (1945) to Bill Clinton (1999).

Question: Maser was first built by the physiciat who shared the Nobel Prize in 1964 with which two other people?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "nobel_prize_year": {
      "type": "integer",
      "description": "The year the Nobel Prize was awarded."
    },
    "nobel_prize_category": {
      "type": "string",
      "description": "The category of the Nobel Prize."
    },
    "maser_inventor_laureate": {
      "type": "string",
      "description": "The name of the physicist who first built the maser and was a laureate."
    },
    "other_laureates": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the other laureates who shared the prize with the maser inventor."
    },
    "total_laureates": {
      "type": "integer",
      "description": "The total number of laureates for this specific Nobel Prize."
    }
  },
  "required": [
    "nobel_prize_year",
    "nobel_prize_category",
    "maser_inventor_laureate",
    "other_laureates",
    "total_laureates"
  ],
  "additionalProperties": false
}
