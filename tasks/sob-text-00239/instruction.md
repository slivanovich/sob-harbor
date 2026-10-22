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
Philip the Arab and Christianity: Philip the Arab was one of the few 3rd-century Roman emperors sympathetic to Christians, although his relationship with Christianity is obscure and controversial.  Philip was born in Auranitis, an Arab district east of the Sea of Galilee.  The urban and Hellenized centers of the region were Christianized in the early years of the 3rd century via major Christian centers at Bosra and Edessa; there is little evidence of Christian presence in the small villages of the region in this period, such as Philip's birthplace at Philippopolis.  Philip served as praetorian prefect, commander of the Praetorian Guard, from 242; he was made emperor in 244.  In 249, after a brief civil war, he was killed at the hands of his successor, Decius.

Tigellinus: Ofonius Tigellinus, also known as Tigellinus Ofonius, Ophonius Tigellinus and Sophonius Tigellinus (c. 10–69), was a prefect of the Roman imperial bodyguard, known as the Praetorian Guard, from 62 until 68, during the reign of emperor Nero.  Tigellinus gained imperial favour through his acquaintance with Nero's mother Agrippina the Younger, and was appointed prefect upon the death of his predecessor Sextus Afranius Burrus, a position Tigellinus held first with Faenius Rufus and then Nymphidius Sabinus.

Lucius Seius Strabo: Lucius Seius Strabo or Lucius Aelius Strabo was a prefect of the Roman imperial bodyguard, known as the Praetorian Guard, during the rule of the emperors Augustus and Tiberius.  The length of Strabo's tenure as Praetorian prefect is unknown, but he held the position together with various colleagues until 15, after which he was appointed to the governorship of Egypt.  With this career Strabo distinguished himself by attaining the two highest offices open to men of the equestrian class in the Roman Empire.

Praetorian prefect: Praetorian prefect (Latin: "praefectus praetorio" , Greek: ) was the title of a high office in the Roman Empire.  Originating as the commander of the Praetorian Guard, the office gradually acquired extensive legal and administrative functions, with its holders becoming the Emperor's chief aides.  Under Constantine I, the office was much reduced in power and transformed into a purely civilian administrative post, while under his successors, territorially-defined praetorian prefectures emerged as the highest-level administrative division of the Empire.  The prefects again functioned as the chief ministers of the state, with many laws addressed to them by name.  In this role, praetorian prefects continued to be appointed until the reign of Heraclius in the 7th century AD, when wide-ranging reforms reduced its power and converted it to a mere overseer of provincial administration.  The last traces of the prefecture disappeared in the Byzantine Empire by the 840s.

Claudia Capitolina: Claudia Capitolina (Greek: η Κλαuδία Καπιτωλίνα ) was an Egyptian Greek woman who lived in the Roman Empire, in the 1st century and possibly in the 2nd century.  Capitolina came from a distinguished family of Equestrian rank.  She was born and raised in Alexandria, Egypt.  Capitolina was the daughter and only child of Tiberius Claudius Balbilus by his unnamed wife.  The cognomen "Capitolina", is probably from her maternal side.  Her father was one of the highest magistrates of Equestrian rank that served in Rome.  Balbilus was an astrologer and a learned scholar, who was later Prefect of Egypt.  Capitolina’s paternal grandfather, was an Egyptian Greek Grammarian and Astrologer called Thrasyllus of Mendes or Tiberius Claudius Thrasyllus, who was a friend of the Roman Emperor Tiberius, while her paternal grandmother was Greek Princess Aka II of Commagene, who was a great, granddaughter of King Antiochus I Theos of Commagene.  Her paternal cousin was Ennia Thrasylla who married the Praetorian prefect of the Praetorian Guard, Naevius Sutorius Macro.

Titus Petronius Secundus: Titus Petronius Secundus (40–97) was a prefect of the Roman imperial bodyguard, known as the Praetorian Guard, under emperor Domitian, from 94 until 96.  Prior to becoming Praetorian prefect, Petronius had served as governor of the Egypt province from 92 until 93.

Naevius Sutorius Macro: Quintus Naevius Cordus Sutorius Macro (21 BC – 38 AD) was a prefect of the Praetorian Guard, from 31 until 38, serving under the Roman Emperors Tiberius and Caligula.  Upon falling out of favor, he committed suicide.

Publius Atilius Aebutianus: Publius Atilius Aebutianus (died 188) was a prefect of the Roman imperial bodyguard, known as the Praetorian Guard, during the reign of emperor Commodus, from 185 until his death in 188.  Aebutianus acceded to the office upon the execution of his predecessor Sextus Tigidius Perennis.  According to ancient sources, Perennis was removed by the influential freedman and chamberlain of Commodus, Marcus Aurelius Cleander, and in 188 Aebutianus suffered a similar fate.  According to the "Historia Augusta", he was murdered by Cleander, who then assumed command of the Praetorian Guard himself.

Nymphidius Sabinus: Gaius Nymphidius Sabinus (c. 35–68) was a Prefect of the Praetorian Guard during the rule of Emperor Nero from 65 until his death in 68.  He shared this office together with Gaius Ophonius Tigellinus, replacing his previous colleague Faenius Rufus.  During the second half of the 60s, Nero grew increasingly unpopular with the people and the army, leading to a number of rebellions which ultimately caused his downfall and suicide in 68.  Nymphidius took part in the final conspiracy against Nero and persuaded the Praetorian Guard to desert him, but when he attempted to have himself declared emperor, he was killed by his own soldiers.

Caligula: Caligula ( ), properly Gaius Julius Caesar Augustus Germanicus (31 August AD 12 – 24 January AD 41) was Roman emperor from AD 37–41.  Born Gaius Julius Caesar Germanicus (not to be confused with Julius Caesar), Caligula was a member of the house of rulers conventionally known as the Julio-Claudian dynasty.  Caligula's biological father was Germanicus, and he was the great-nephew and adopted son of Emperor Tiberius.  The young Gaius earned the nickname "Caligula" (meaning "little soldier's boot", the diminutive form of "caliga", hob-nailed military boot) from his father's soldiers while accompanying him during his campaigns in Germania.

Question: What was the birth name of the emperor under whom Naevius Sutorius Macro served as prefect of the Praetorian Guard?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "emperor_details": {
      "type": "object",
      "properties": {
        "common_name": {
          "type": "string",
          "description": "The common name of the Roman emperor."
        },
        "birth_name": {
          "type": "string",
          "description": "The birth name of the Roman emperor."
        },
        "reign_start_ad": {
          "type": "integer",
          "description": "The year AD when the emperor's reign began."
        },
        "reign_end_ad": {
          "type": "integer",
          "description": "The year AD when the emperor's reign ended."
        }
      },
      "required": [
        "common_name",
        "birth_name",
        "reign_start_ad",
        "reign_end_ad"
      ],
      "additionalProperties": false
    },
    "praetorian_prefect_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the Praetorian prefect."
        },
        "service_start_ad": {
          "type": "integer",
          "description": "The year AD when the prefect's service began."
        },
        "service_end_ad": {
          "type": "integer",
          "description": "The year AD when the prefect's service ended."
        }
      },
      "required": [
        "name",
        "service_start_ad",
        "service_end_ad"
      ],
      "additionalProperties": false
    },
    "relationship_context": {
      "type": "string",
      "description": "A description of the relationship between the prefect and the emperor."
    }
  },
  "required": [
    "emperor_details",
    "praetorian_prefect_details",
    "relationship_context"
  ],
  "additionalProperties": false
}
