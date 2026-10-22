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
Ruler X (Rio Azul): Ruler X (also Governor X) is the designation given by archaeologists to a pre-Columbian Maya ruler at the site of Rio Azul, whose name glyphs have otherwise not been satisfactorily deciphered.  Ruler X is associated with Tomb 1 located in Structure C-1, where a mural inscription on the walls of the tomb carries the Long Count date of 8.19.1.9.13.  This date, equivalent to September 27, 417 CE in the proleptic Gregorian calendar, has been interpreted as the birth date of this ruler.

Hippolytus (archbishop of Gniezno): Hippolytus or Hipolit (died c. 1027) was an early medieval archbishop of Gniezno.  His place and date of birth date are unknown but the medieval historian Jan Długosz claims that he was of noble birth and a Roman citizen.  Modern scholars generally agree that he was not Polish.

Astro Boy (2003 TV series): Astro Boy (アストロボーイ・鉄腕アトム , Asutoro Bōi: Tetsuwan Atomu , lit.  "Astro Boy: Mighty Atom") is a remake of the 1960s anime series of the same name created by Osamu Tezuka, which was produced by his company, Tezuka Productions, Sony Pictures Entertainment Japan, Dentsu, and Fuji Television network.  It was also shown on Animax, who have broadcast the series across its respective networks worldwide, including Japan, Southeast Asia, South Asia, East Asia, and other regions.  It was created to celebrate the birth date of Atom/Astro Boy (as well as the 40th anniversary of the original TV series).  Under the original English name (instead of "Mighty Atom"), it kept the same classic art style as the original manga and anime, but was revisioned and modernized with more lush, high-quality, near-theatrical animation and visuals.  It combined the playfulness of the early anime with the darker, more serious and dramatic Science fiction themes of the manga and the 1980 series.  The anime broadcast in Japan on the same date as Atom's/Astro's birth in the manga (April 6, 2003) across Animax and Fuji Television.  It was directed by Kazuya Konaka and written by Chiaki J. Konaka at the beginning of the series.  Other writers included were Keiichi Hasegawa, Sadayuki Murai, Ai Ohta, Hirotoshi Kobayashi, Kenji Konuta, and Marc Handler, who was also executive story editor.

Thomas D. Singleton: Thomas Day Singleton (Birth date unknown – November 25, 1833) was a United States Representative from South Carolina.  He was born near Kingstree, South Carolina but his birth date is unknown.

Cédula de identidad (Costa Rica): In Costa Rica, in recent years, a cédula de identidad, has been a credit card-sized plastic card.  On one side, it includes a photo of the person, a personal identification number, and the card's owner personal information (complete name, gender, birth date, and others), and the user's signature.  On the reverse, it may include additional information such as the date when the ID card was granted, expiration date of the ID card, and other such as their fingerprints, and all the owner's information in matrix code.  Every Costa Rican citizen must carry an ID card immediately after turning 18.

Akhund Mullah Mohammad Kashani: Akhund Mullah Mohammad Kashani, known as lunar tiles in 1833 was born in Kashan.  In place of his birth date and age of his birth is not mentioned during the 84 years of his life, to guess.  According to Syed Jalaluddin Homai, he, along with Jahangir Khan Qashqai as two distinguished professor in philosophy and jurisprudence, literature and jurisprudence have.  He taught for fifty years and foster outstanding students in the fields of intellectual and traditional sciences.  He died in 1914 in Isfahan and was buried in Takht-e Foulad.

Junaid Khan: Junaid Khan (Pashto/Urdu: ‎ ; born 24 December 1989, Swabi District) is a Pakistani international cricketer who bowls left arm fast.  He is the first player from Swabi to qualify for the Pakistan national cricket team, and his cousin, the leg-spinner Yasir Shah, followed his path later on.

Saint David: Saint David (Welsh: Dewi Sant , Latin: "Davidus" ; 500 c. 589) was a Welsh bishop of Mynyw (now St Davids) during the 6th century; he was later regarded as a saint.  He is the patron saint of Wales.  David was a native of Wales, and a relatively large amount of information is known about his life.  However, his birth date is uncertain: suggestions range from 462 to 512.  He is traditionally believed to be the son of Saint Non and the grandson of Ceredig ap Cunedda, king of Ceredigion.  The Welsh annals placed his death 569 years after the birth of Christ, but Phillimore's dating revised this to 601.

Dil-e-Beqarar: Dil-e-Beqarar (Urdu: ‎ ;lit:The Quiet Heart), is a Pakistani romantic television drama serial that was first aired on Hum TV on 13 April 2016 replacing "Maana Ka Gharana".  It airs every Wednesday at 8:00 pm PST.  It stars Junaid Khan, Mansha Pasha and Hareem Farooq.

Charles C. Smith (boxer): Smith was born in Macon, Georgia, likely into slavery, and he and his mother moved north in 1865.  His birth date is given as 3 May 1860, but since he supposedly did not begin boxing until he was 19 and claimed the title in 1876, the birth year likely is spurious.  Some sources cite 1869 as the year his boxing career began, and others 1879, which would have been three years after he claimed the championship.

Question: State the birth date of one of Dil-e-Beqara's stars ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person whose birth date is being provided."
    },
    "person_role": {
      "type": "string",
      "description": "The role of the person in the context of the question (e.g., 'actor')."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the television series the person starred in."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the person in 'Day Month Year' format."
    }
  },
  "required": [
    "person_name",
    "person_role",
    "series_name",
    "birth_date"
  ],
  "additionalProperties": false
}
