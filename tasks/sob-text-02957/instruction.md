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
Augustalia: The Augustalia, also known as the Ludi Augustales ("Augustan Games"), was a festival celebrated October 12 in honor of Augustus, the first Roman emperor.  It was established in conjunction with an altar to Fortuna Redux to mark the return of Augustus from Asia Minor to Rome in 19 BC.  The pontiffs and Vestals conducted sacrifices, and the date became a holiday "(feriae)" on the official religious calendar of Rome.

America's Freedom Festival at Provo: America's Freedom Festival at Provo (also America's Freedom Festival or Freedom Festival) is a private, non-profit, non-political foundation known for organizing more than 25 annual patriotic events in and around Provo, Utah.  It is one of the largest and longest (usually May - July) patriotic celebrations in the nation.  The organization's stated mission is to "celebrate, teach, honor, and strengthen the traditional American values of family, freedom, God, and country."  America's Freedom Festival sponsors one of the nation's largest Fourth of July celebrations, Stadium of Fire, held each year at LaVell Edwards Stadium on the campus of Brigham Young University.  Recent performers at Stadium of Fire include Journey (band), Cirque du Soleil, Carrie Underwood, Brad Paisley, and the Blue Man Group.  The United States Department of Defense has chosen to broadcast parts of the festival to millions of servicemen and women serving abroad in the Armed Forces for the past several years.

Volpi Cup for Best Actress: The Volpi Cup (Italian: "Coppa Volpi alla miglior attrice" or "Coppa Volpi per la miglior interpretazione femminile") is the principal award given to actresses at the Venice Film Festival and is named in honor of Count Giuseppe Volpi di Misurata, the founder of the festival.  The award winner is selected by the festival jury from the films in the competition slate.  The official name of the award has changed several times over the course of the years.  The awards given from 1983 to 1987 were not "Coppa Volpis" but rather square plaques.  The award can be given for lead or supporting performances.  There are additional awards given within the festival that recognize acting performances.  From 1993 to 1995 the festival awarded a Best Supporting Actress prize that is included below.

Rabindra Jayanti: Rabindra Jayanti (রবীন্দ্র জয়ন্তী) is an annually celebrated cultural festival, prevalent among Bengalis around the world, in the remembrance of Rabindranath Tagore's birthday anniversary.  It is celebrated in early May, on the 25th day of the Bengali month of Boishakh (২৫শে বৈশাখ), since Tagore was born on this day of the year 1268 (২৫শে বৈশাখ, ১২৬৮) of the Bengali calendar.  Every year, numerous cultural programmes & events, such as : "Kabipranam" (কবিপ্রণাম) – the songs (Rabindra Sangeet), poetries, dances and dramas, written and composed by Tagore, are organised in this particular day, by various schools, colleges & universities of Bengal, and also celebrated by different groups abroad, as a tribute to Tagore and his works.  Throughout the globe, Tagore's birth anniversary is largely celebrated at Santiniketan, Birbhum in West Bengal, chiefly in Visva-Bharati University, the institution founded by Tagore himself for the cultural, social and educational upliftment of the students as well as the society.  Government of India Issued 5 Rupees coin in 2011 to mark the 150 Birth Anniversary in the honor of Rabindranath Tagore.

Sanja Matsuri: Sanja Matsuri (三社祭 , literally "Three Shrine Festival") , or Sanja Festival, is one of the three great Shinto festivals in Tokyo.  It is considered one of the wildest and largest.  The festival is held in honor of Hinokuma Hamanari, Hinokuma Takenari, and Hajino Nakatomo, the three men who established and founded Sensō-ji.  Sanja Matsuri is held on the third weekend of every May at Asakusa Shrine.  Its prominent parades revolve around three "mikoshi" (portable shrines referenced in the festival's name), as well as traditional music and dancing.  Over the course of three days, the festival attracts 1.5 to 2 million locals and tourists every year.

Wat Phra That Phanom: Wat Phra That Phanom is the sacred precinct of the Phra That Phanom chedi, located in the district of the same name, in the southern part of Nakhon Phanom Province, northeastern Thailand.  According to legend, this structure contains The Buddha's breast bone, and as such, it is one of the most important Theravada Buddhist structures in the region.  It was originally built in the 16th century by the Laotian King Setthathirath of Lanxang.  Each year, a festival is held in That Phanom to honor the temple.  This festival lasts for one week, during which thousands of people make pilgrimages to honor the shrine.

Jigme Namgyel Wangchuck: Jigme Namgyel Wangchuck (born 5 February 2016) is the first child and heir apparent of King Jigme Khesar Namgyel Wangchuck.  His name was announced on 16 April 2016.  Prior to the announcement, he was known only as The Gyalsey, which means "prince".  Before his birth his paternal uncle Prince Jigyel Ugyen of Bhutan was the heir presumptive to King Jigme Khesar Namgyel of Bhutan.  In honor of his birth, 108,000 trees were planted by thousands of volunteers in Bhutan.

Galder: Galder is a Norwegian guitarist, and vocalist.  His birth name is Tom Rune Andersen.  He is from the small town Jessheim, north of Oslo.  He is a founding member of the melodic black metal band Old Man's Child as well as the lead guitarist in Dimmu Borgir.  In 1993, under the stage name Grusom, he, Jardar and Tjodalv created Old Man's Child.  On Old Man's Child albums, he has performed vocal work, guitars, bass, and keyboards, though with a full line-up his primary instruments are guitar and keyboards, as well as vocals.  He joined Dimmu Borgir in 2000 but has kept Old Man's Child alive.

Augustus: Augustus (Latin: "Imperātor Caesar Dīvī Fīlius Augustus" ; 23 September 63 BC – 19 August 14 AD) was the founder of the Roman Principate and considered the first Roman emperor, controlling the Roman Empire from 27 BC until his death in AD 14.  He was born Gaius Octavius into an old and wealthy equestrian branch of the plebeian "gens" Octavia.  His maternal great-uncle Julius Caesar was assassinated in 44 BC, and Octavius was named in Caesar's will as his adopted son and heir, then known as Octavianus (Anglicized as Octavian).  He, Mark Antony, and Marcus Lepidus formed the Second Triumvirate to defeat the assassins of Caesar.  Following their victory at the Battle of Philippi, the Triumvirate divided the Roman Republic among themselves and ruled as military dictators.  The Triumvirate was eventually torn apart by the competing ambitions of its members.  Lepidus was driven into exile and stripped of his position, and Antony committed suicide following his defeat at the Battle of Actium by Octavian in 31 BC.

Jabez: Jabez or "Jabes" is a Biblical male given name from the Old Testament.  In 1 Chronicles, Jabez is a well-respected man (hinted to be an ancestor in the lineage of the kings' tribe of Judah, though none of his family is mentioned) whose prayer to God for blessing was answered (see 1 Chronicles 4:9-11).  The name is Hebrew (yabetz = יַעְבֵּץ) for "he makes sorrowful"; his mother stated "I gave birth to him in pain".  Jabez was labelled with "sorrow" at birth, but his prayer against contracting sorrow nullified the label.  His life contradicted his name.  Jabez's name is also mentioned in 1 Chronicles 2:55, possibly as a place named after him.  Jabez possibly could have been a Jewish scribe in his later years.  He might have been influential and well respected as a scribe because the city named after him was where the families of scribes lived.

Question: The Augustalia was a festival celebreated in honor of a man that had what name at birth?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "festival_name": {
      "type": "string",
      "description": "The name of the festival."
    },
    "honored_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person honored by the festival."
        },
        "birth_name": {
          "type": "string",
          "description": "The birth name of the honored person."
        },
        "title": {
          "type": "string",
          "description": "The primary title or role of the honored person."
        }
      },
      "required": [
        "name",
        "birth_name",
        "title"
      ],
      "additionalProperties": false
    },
    "celebration_date": {
      "type": "string",
      "description": "The date on which the festival was celebrated."
    }
  },
  "required": [
    "festival_name",
    "honored_person",
    "celebration_date"
  ],
  "additionalProperties": false
}
