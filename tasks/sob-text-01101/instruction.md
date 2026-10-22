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
Chanakya (TV series): Chanakya (Devanagari: चाणक्य) is a 47-part epic Indian television historical drama written and directed by Dr. Chandraprakash Dwivedi that was originally telecast on DD National from 8 September 1991 to 9 August 1992.  Produced by Prakash Dwivedi, the series is a fictionalized account of the life and times of 4th century BCE Indian economist, strategist and political theorist Chanakya (also known as Vishnugupta) and is based on events occurring between 340 BCE and 321/20 BCE, starting with Chanakya's boyhood and culminating in the coronation of Chandragupta Maurya.  Chandraprakash Dwivedi played the title role of Chanakya.

Nanda Empire: The Nanda dynasty originated from the region of Magadha in ancient India during the 4th century BCE and lasted between 345–321 BCE.  At its greatest extent, the empire ruled by the Nanda Dynasty extended from Bengal in the east, to the Punjab region in the west and as far south as the Vindhya Range.  The rulers of this dynasty were famed for the great wealth which they accumulated.  The Nanda Empire was later conquered by Chandragupta Maurya, who founded the Maurya Empire.

Maurya Empire: The Maurya Empire was a geographically extensive Iron Age historical power founded by Chandragupta Maurya which dominated ancient India between  322 and 187 BCE.  Originating from the kingdom of Magadha in the Indo-Gangetic Plain in the eastern side of the Indian subcontinent, the empire had its capital city at Pataliputra (modern Patna).  The empire was the largest to have ever existed in the Indian subcontinent, spanning over 5 e6km2 at its zenith under Ashoka.

Durdhara: Durdhara was the wife of Chandragupta Maurya, the founder of the 4th-century BCE Maurya Empire of ancient India, according to the 12th century CE Jain text "Parishishtaparvan" by Hemachandra.  She is stated by this text to be the mother of the second Mauryan emperor, Bindusara.

Chandragupta Maurya (TV series): Chandragupta Maurya (Devanagari: चन्द्रगुप्त मौर्य) is an Indian historical drama being broadcast on Dangal TV, based on the life of Chandragupta Maurya, one of the major Indian Emperors of ancient India.  It premiered on 20 December 2014.  It is being re-aired on Dangal TV after Imagine TV was shut-down for unknown reasons.  Chandragupta Maurya was first aired in March 2011 on Imagine TV.  Ashish Sharma played the role of Chandragupta Maurya.

Invasions of Afghanistan: Afghanistan is a mountainous landlocked country in Central Asia and South Asia.  The Afghanistan area has been invaded many times in recorded history, but no invader has been able to control all of its regions at the same time, and at some point faced rebellion.  Some of the invaders in the history of Afghanistan include the Maurya Empire of ancient India, Alexander the Great of Macedon, Umar, an Arab Caliphate, Genghis Khan of Mongolia, Timur of Persia and Central Asia, the Mughal Empire of India, various Persian Empires, the British Empire, the Sikh Empire, the Soviet Union, and most recently a coalition force of NATO troops, the majority from the United States, which entered the country in the first-ever invocation of NATO's Article 5 "an attack on one is an attack on all" following the September 11 attacks in the United States.  The country is now entitled the Islamic Republic of Afghanistan and has a democratically elected government.  A reduced number of NATO troops remain in the country in support of the government under the U.S.–Afghanistan Strategic Partnership Agreement.

Chandragupta Maurya: Chandragupta Maurya (reign: 321–298 BCE) was the founder of the Maurya Empire in ancient India.  He was born in a humble family, orphaned and abandoned, raised as a son by another pastoral family, then according to Buddhist texts, was picked up, taught and counselled by Chanakya, the author of the "Arthashastra".  Chandragupta thereafter built one of the largest empires ever in the Indian subcontinent.  According to Jain sources, he then renounced it all, and became a monk in the Jain tradition.  Chandragupta is claimed, by the historic Jain texts, to have followed Jainism in his life, by first renouncing all his wealth and power, going away with Jaina monks into the Deccan region (now Karnataka), and ultimately performing Sallekhana – the Jain religious ritual of peacefully welcoming death by fasting.  His grandson was emperor Ashoka, famous for his historic pillars and for his role in helping spread Buddhism outside of ancient India.  Chandragupta's life and accomplishments are described in ancient Hindu, Buddhist and Greek texts, but they vary significantly in details from the Jaina accounts.  Megasthenes served as a Greek ambassador in his court for four years.  In Greek and Latin accounts, Chandragupta is known as Sandrokottos and Androcottus.

Magadha: Magadha was an ancient Indian kingdom in southern Bihar, and was counted as one of the sixteen Mahajanapadas (Sanskrit: "Great Countries") of ancient India.  Magadha played an important role in the development of Jainism and Buddhism, and two of India's greatest empires, the Maurya Empire and Gupta Empire, originated in Magadha.

Ashoka: Ashoka ( ; IAST: "Aśoka " ; died 232 BCE) was an Indian emperor of the Maurya Dynasty, who ruled almost all of the Indian subcontinent from  268 to 232 BCE.  He was the grandson of the founder of the Maurya Dynasty, Chandragupta Maurya, who had created one of the largest empires in ancient India and then, according to Jain sources, renounced it all to become a Jain monk.  One of India's greatest emperors, Ashoka expanded Chandragupta's empire, and reigned over a realm that stretched from present-day Afghanistan in the west to Bangladesh in the east.  It covered the entire Indian subcontinent except for parts of present-day Tamil Nadu, Karnataka and Kerala.  The empire's capital was Pataliputra (in Magadha, present-day Patna), with provincial capitals at Taxila and Ujjain.

Morè (clan): The Morey / More (Marathi: मोरे ) is a Maratha clan found largely in the Indian state of Maharashtra that claims to have descended from the Somavanshi kings, the Morès of the Kashmir Region.  Some from the Morey clan claim descent from the Mauryan Dynasty of Patna (Bihar), which ruled over the Maurya Empire, located in present day India.  The Maurya Empire and many Morè, claim rulers such as Chandragupt Maurya Abhishek Kaushal and Ashoka.

Question: Who was the founder of the Maurya Empire in ancient India, whose coronation was featured in the 47-part Indian television historical drama Chanakya?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "founder_name": {
      "type": "string",
      "description": "The name of the founder of the empire."
    },
    "empire_name": {
      "type": "string",
      "description": "The name of the empire founded."
    },
    "tv_series_details": {
      "type": "object",
      "properties": {
        "series_title": {
          "type": "string",
          "description": "The title of the television series."
        },
        "parts_count": {
          "type": "integer",
          "description": "The total number of parts in the television series."
        },
        "coronation_featured": {
          "type": "boolean",
          "description": "Indicates if the coronation of the founder was featured in the TV series."
        }
      },
      "required": [
        "series_title",
        "parts_count",
        "coronation_featured"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "founder_name",
    "empire_name",
    "tv_series_details"
  ],
  "additionalProperties": false
}
